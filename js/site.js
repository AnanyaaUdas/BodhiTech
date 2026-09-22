/* all the site js. no framework.
   loads on every page, so `if (!el) return` means "not on this page". */

window.toggleBodhiChat = function(e) {
  if (e) {
    e.preventDefault();
    e.stopPropagation();
  }
  const win = document.querySelector('.chatbot-window');
  const btn = document.querySelector('.chatbot-launcher');
  if (!win) return;

  const isOpen = win.classList.contains('active');
  if (isOpen) {
    win.classList.remove('active');
    btn && btn.classList.remove('active');
  } else {
    win.classList.add('active');
    btn && btn.classList.add('active');
    setTimeout(() => {
      const input = document.getElementById('chatInput');
      if (input) input.focus();
      const msgBox = document.querySelector('.chatbot-messages');
      if (msgBox) msgBox.scrollTop = msgBox.scrollHeight;
    }, 50);
  }
};

window.closeBodhiChat = function(e) {
  if (e) {
    e.preventDefault();
    e.stopPropagation();
  }
  const win = document.querySelector('.chatbot-window');
  const btn = document.querySelector('.chatbot-launcher');
  if (win) win.classList.remove('active');
  if (btn) btn.classList.remove('active');
};

document.addEventListener('DOMContentLoaded', () => {
  // mobile drawer. locking body scroll while it is open is the bit that gets
  // forgotten, and without it the page behind scrolls under your thumb.
  const mobileToggle = document.querySelector('.mobile-toggle');
  const drawerClose = document.querySelector('.drawer-close');
  const mobileDrawer = document.querySelector('.mobile-drawer');
  const drawerBackdrop = document.querySelector('.mobile-drawer-backdrop');
  const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

  function openDrawer() {
    if (mobileDrawer) mobileDrawer.classList.add('active');
    if (drawerBackdrop) drawerBackdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    if (mobileDrawer) mobileDrawer.classList.remove('active');
    if (drawerBackdrop) drawerBackdrop.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (mobileToggle) mobileToggle.addEventListener('click', openDrawer);
  if (drawerClose) drawerClose.addEventListener('click', closeDrawer);
  if (drawerBackdrop) drawerBackdrop.addEventListener('click', closeDrawer);

  mobileNavLinks.forEach(link => {
    link.addEventListener('click', closeDrawer);
  });

  // services slider.
  // three cards per slide on desktop, one on a phone. the slide count is
  // derived from the card count rather than hardcoded, so adding a service in
  // content.py does not need a change here.
  const servicesTrack = document.getElementById('servicesSliderTrack');
  const servicesDots = document.querySelectorAll('.services-dot');
  const servicesPrevBtn = document.getElementById('servicesPrev');
  const servicesNextBtn = document.getElementById('servicesNext');
  let currentServicesSlide = 0;
  const totalServicesSlides = 2; // slide 0 (01-03), slide 1 (04-06)
  let servicesAutoTimer = null;
  let isServicesHovered = false;

  // moves the carousel to a slide and updates the dots underneath.
  function goToServicesSlide(slideIdx) {
    if (!servicesTrack) return;
    currentServicesSlide = (slideIdx + totalServicesSlides) % totalServicesSlides;
    servicesTrack.style.transform = 'translateX(-' + (currentServicesSlide * 100) + '%)';

    servicesDots.forEach((dot, idx) => {
      dot.classList.toggle('active', idx === currentServicesSlide);
    });
  }

  if (servicesPrevBtn) {
    servicesPrevBtn.addEventListener('click', () => {
      goToServicesSlide(currentServicesSlide - 1);
      isServicesHovered = true;
    });
  }

  if (servicesNextBtn) {
    servicesNextBtn.addEventListener('click', () => {
      goToServicesSlide(currentServicesSlide + 1);
      isServicesHovered = true;
    });
  }

  servicesDots.forEach((dot, idx) => {
    dot.addEventListener('click', () => {
      goToServicesSlide(idx);
      isServicesHovered = true;
    });
  });

  // advances on its own every few seconds, pausing while the pointer is over it.
  function startServicesAutoSlide() {
    if (servicesAutoTimer) clearInterval(servicesAutoTimer);
    servicesAutoTimer = setInterval(() => {
      if (!isServicesHovered) {
        goToServicesSlide(currentServicesSlide + 1);
      }
    }, 6000);
  }

  startServicesAutoSlide();

  const servicesSliderWrapper = document.querySelector('.services-slider-wrapper');
  if (servicesSliderWrapper) {
    servicesSliderWrapper.addEventListener('mouseenter', () => { isServicesHovered = true; });
    servicesSliderWrapper.addEventListener('mouseleave', () => { isServicesHovered = false; });
  }

  // the client stories accordion. it switches panels on its own every few
  // seconds, with a progress bar on the active tab, the photo drifting, and
  // the numbers counting up.
  //
  // the bar and the switching run off the same timer on purpose. when they
  // had separate timers they slowly fell out of sync.
  //
  // it pauses when you hover it or scroll past it.
  const accordionPanels = document.querySelectorAll('.case-accordion-panel');
  const accordionNavBtns = document.querySelectorAll('.case-nav-btn');
  const accordionContainer = document.querySelector('.case-accordion-container');
  const ACC_REDUCE = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const ACC_DWELL = 6500;

  let activeAccordionIdx = 0;
  let isAccordionHovered = false;
  let accordionInView = false;
  let accordionElapsed = 0;
  let accordionLastTs = null;
  let accordionRaf = null;

  /* the dwell bar lives inside each pill. */
  accordionNavBtns.forEach((btn) => {
    if (btn.querySelector('.cnb-progress')) return;
    const bar = document.createElement('span');
    bar.className = 'cnb-progress';
    bar.setAttribute('aria-hidden', 'true');
    btn.appendChild(bar);
  });

  function accordionBar(idx) {
    const btn = accordionNavBtns[idx];
    return btn ? btn.querySelector('.cnb-progress') : null;
  }

  function resetAccordionBars() {
    accordionNavBtns.forEach((btn) => {
      const bar = btn.querySelector('.cnb-progress');
      if (bar) bar.style.transform = 'scaleX(0)';
    });
  }

  /* count the figures up from zero. */
  function countUpPanel(panel) {
    if (!panel || ACC_REDUCE) return;
    panel.querySelectorAll('.expanded-metric-val').forEach((el) => {
      const node = el.firstChild;
      /* only the leading text node - the trailing "+" is its own span */
      if (!node || node.nodeType !== 3) return;
      if (!el.dataset.raw) el.dataset.raw = node.nodeValue;

      const raw = el.dataset.raw;
      const parts = raw.match(/^(\D*)([\d.,]+)(.*)$/);
      if (!parts) return;

      const pre = parts[1];
      const post = parts[3];
      const digits = parts[2];
      const target = parseFloat(digits.replace(/,/g, ''));
      if (isNaN(target)) return;
      const decimals = (digits.split('.')[1] || '').length;
      const grouped = digits.indexOf(',') > -1;

      if (el._countRaf) cancelAnimationFrame(el._countRaf);
      const t0 = performance.now();
      const dur = 1100;

      const write = (v) => {
        let out = v.toFixed(decimals);
        if (grouped) out = Number(out).toLocaleString('en-AU');
        node.nodeValue = pre + out + post;
      };

      write(0);
      const step = (now) => {
        const p = Math.min(1, (now - t0) / dur);
        write(target * (1 - Math.pow(1 - p, 3)));
        if (p < 1) {
          el._countRaf = requestAnimationFrame(step);
        } else {
          node.nodeValue = raw;          /* restore the exact original text */
          el._countRaf = null;
        }
      };
      el._countRaf = requestAnimationFrame(step);
    });
  }

  function activateAccordionPanel(idx) {
    if (!accordionPanels.length) return;
    activeAccordionIdx = idx;

    accordionPanels.forEach((panel, i) => panel.classList.toggle('active', i === idx));
    accordionNavBtns.forEach((btn, i) => {
      btn.classList.toggle('active', i === idx);
      btn.setAttribute('aria-selected', i === idx ? 'true' : 'false');
    });

    accordionElapsed = 0;
    resetAccordionBars();
    countUpPanel(accordionPanels[idx]);
    keepPillInView(idx);
  }

  /* nudge the pill rail, not scrollIntoView - that drags the whole page */
  function keepPillInView(idx) {
    const nav = document.querySelector('.case-accordion-nav');
    const btn = accordionNavBtns[idx];
    if (!nav || !btn) return;
    if (nav.scrollWidth <= nav.clientWidth + 4) return;   /* not scrolling */
    const target = btn.offsetLeft - (nav.clientWidth - btn.offsetWidth) / 2;
    if (typeof nav.scrollTo === 'function') {
      nav.scrollTo({ left: target, behavior: ACC_REDUCE ? 'auto' : 'smooth' });
    } else {
      nav.scrollLeft = target;
    }
  }

  accordionPanels.forEach((panel, index) => {
    panel.addEventListener('mouseenter', () => {
      isAccordionHovered = true;
      if (index !== activeAccordionIdx) activateAccordionPanel(index);
    });
    panel.addEventListener('click', () => activateAccordionPanel(index));
  });

  accordionNavBtns.forEach((btn, index) => {
    btn.addEventListener('click', () => {
      isAccordionHovered = true;
      activateAccordionPanel(index);
    });
    btn.addEventListener('focus', () => { isAccordionHovered = true; });
    btn.addEventListener('blur', () => { isAccordionHovered = false; });
  });

  if (accordionContainer) {
    accordionContainer.addEventListener('mouseenter', () => { isAccordionHovered = true; });
    accordionContainer.addEventListener('mouseleave', () => { isAccordionHovered = false; });

    if (!ACC_REDUCE) accordionContainer.classList.add('has-parallax');

    /* touch. no hover on a phone, so a tap pauses and it resumes after 4s. */
    let touchX = 0, touchY = 0, touchResume = null;
    const pauseForTouch = () => {
      isAccordionHovered = true;
      clearTimeout(touchResume);
      touchResume = setTimeout(() => { isAccordionHovered = false; }, 4000);
    };

    accordionContainer.addEventListener('touchstart', (e) => {
      const t = e.changedTouches[0];
      touchX = t.clientX;
      touchY = t.clientY;
      pauseForTouch();
    }, { passive: true });

    accordionContainer.addEventListener('touchend', (e) => {
      const t = e.changedTouches[0];
      const dx = t.clientX - touchX;
      const dy = t.clientY - touchY;
      pauseForTouch();
      /* ratio check, or a diagonal page scroll flicks the panel across */
      if (Math.abs(dx) > 55 && Math.abs(dx) > Math.abs(dy) * 1.6) {
        const n = accordionPanels.length;
        activateAccordionPanel(((activeAccordionIdx + (dx < 0 ? 1 : -1)) % n + n) % n);
      }
    }, { passive: true });

    const nav = document.querySelector('.case-accordion-nav');
    if (nav) nav.addEventListener('touchstart', pauseForTouch, { passive: true });

    /* the one clock. dwell bar, auto-advance and parallax all read from it. */
    const accordionTick = (ts) => {
      if (accordionLastTs === null) accordionLastTs = ts;
      const dt = Math.min(64, ts - accordionLastTs);   /* clamp tab-switch gaps */
      accordionLastTs = ts;

      if (!ACC_REDUCE) {
        const rect = accordionContainer.getBoundingClientRect();
        const centre = rect.top + rect.height / 2 - window.innerHeight / 2;
        const span = (window.innerHeight + rect.height) / 2;
        const prog = Math.max(-1, Math.min(1, centre / span));
        accordionContainer.style.setProperty('--par', (prog * 26).toFixed(1) + 'px');
      }

      /* no width gate - it used to only advance above 992px */
      const running = !ACC_REDUCE && !isAccordionHovered &&
                      accordionInView && accordionPanels.length > 1;

      if (running) {
        accordionElapsed += dt;
        const bar = accordionBar(activeAccordionIdx);
        if (bar) {
          bar.style.transform = 'scaleX(' +
            Math.min(1, accordionElapsed / ACC_DWELL).toFixed(4) + ')';
        }
        if (accordionElapsed >= ACC_DWELL) {
          activateAccordionPanel((activeAccordionIdx + 1) % accordionPanels.length);
        }
      }

      accordionRaf = requestAnimationFrame(accordionTick);
    };

    const startAccordionClock = () => {
      if (accordionRaf) return;
      accordionLastTs = null;
      accordionRaf = requestAnimationFrame(accordionTick);
    };
    const stopAccordionClock = () => {
      if (!accordionRaf) return;
      cancelAnimationFrame(accordionRaf);
      accordionRaf = null;
    };

    if ('IntersectionObserver' in window) {
      new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          accordionInView = e.isIntersecting;
          if (e.isIntersecting) {
            startAccordionClock();
            countUpPanel(accordionPanels[activeAccordionIdx]);
          } else {
            stopAccordionClock();
          }
        });
      }, { threshold: 0.25 }).observe(accordionContainer);
    } else {
      accordionInView = true;
      startAccordionClock();
    }

    /* backgrounded tabs pause rAF, so drop the gap or it jumps three slides */
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        stopAccordionClock();
      } else if (accordionInView) {
        accordionElapsed = 0;
        resetAccordionBars();
        startAccordionClock();
      }
    });
  }

  // counter strip. counts up once on first reveal, and does not re-run when
  // the section comes back into view.
  const counters = document.querySelectorAll('.counter-number');

  function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3);
  }

  function runContinuousCountCycle() {
    counters.forEach(counter => {
      const target = parseInt(counter.getAttribute('data-target'), 10) || 0;
      const duration = 1500;
      const startTime = performance.now();

      function frame(now) {
        const elapsed = now - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const currentVal = Math.floor(easeOutCubic(progress) * target);

        counter.textContent = currentVal;

        if (progress < 1) {
          requestAnimationFrame(frame);
        } else {
          counter.textContent = target;
        }
      }

      requestAnimationFrame(frame);
    });
  }

  runContinuousCountCycle();
  setInterval(runContinuousCountCycle, 4500);

  // approach phases. the travelling pulse on the connector line is pure CSS;
  // this only keeps the active phase in step with it.
  const stepCards = document.querySelectorAll('.approach-step-card');
  const progressFill = document.querySelector('.approach-progress-bar-fill');
  let currentStepIdx = 0;
  let approachTimer = null;
  let isApproachHovered = false;

  function activateStep(idx) {
    if (!stepCards.length) return;
    currentStepIdx = idx;

    stepCards.forEach((card, i) => {
      if (i === idx) {
        card.classList.add('active');
      } else {
        card.classList.remove('active');
      }
    });

    if (progressFill) {
      const pct = ((idx + 1) / stepCards.length) * 100;
      progressFill.style.width = pct + '%';
    }
  }

  function runSequentialLoop() {
    if (approachTimer) clearInterval(approachTimer);
    approachTimer = setInterval(() => {
      if (!isApproachHovered) {
        const next = (currentStepIdx + 1) % stepCards.length;
        activateStep(next);
      }
    }, 2800);
  }

  activateStep(0);
  runSequentialLoop();

  stepCards.forEach((card, index) => {
    card.addEventListener('mouseenter', () => {
      isApproachHovered = true;
      activateStep(index);
    });

    card.addEventListener('mouseleave', () => {
      isApproachHovered = false;
    });

    card.addEventListener('click', () => {
      activateStep(index);
      isApproachHovered = false;
    });
  });

  // FAQ. one open at a time - opening a row closes whatever was open.
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach((item, index) => {
    const header = item.querySelector('.faq-header');
    const body = item.querySelector('.faq-body');

    if (index === 0) {
      item.classList.add('active');
      if (body) body.style.maxHeight = body.scrollHeight + 'px';
    }

    if (header) {
      header.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        faqItems.forEach(otherItem => {
          otherItem.classList.remove('active');
          const otherBody = otherItem.querySelector('.faq-body');
          if (otherBody) otherBody.style.maxHeight = null;
        });

        if (!isActive) {
          item.classList.add('active');
          if (body) body.style.maxHeight = body.scrollHeight + 'px';
        }
      });
    }
  });

  // back-to-top button, revealed after one viewport of scroll.
  const backToTop = document.querySelector('.back-to-top');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      if (backToTop) backToTop.classList.add('show');
    } else {
      if (backToTop) backToTop.classList.remove('show');
    }
  });

  if (backToTop) {
    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // contact form.
  // front-end only: this validates and gives feedback, then stops. nothing is
  // posted anywhere yet. wire it up before launch, and do not let the success
  // message imply it sent until you have.
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const btn = contactForm.querySelector('button[type="submit"]');
      const originalText = btn.innerHTML;
      btn.innerHTML = 'Sending Request...';
      btn.disabled = true;

      setTimeout(() => {
        btn.innerHTML = '✓ Request Sent Successfully!';
        btn.style.backgroundColor = '#10b981';
        contactForm.reset();

        setTimeout(() => {
          btn.innerHTML = originalText;
          btn.disabled = false;
          btn.style.backgroundColor = '';
        }, 4000);
      }, 1000);
    });
  }

  // chat widget.
  // keyword matching against a handful of canned replies, nothing more. it is
  // a contact shortcut wearing a chat interface, and the copy is written so it
  // never claims to be anything else.
  const chatbotMessages = document.querySelector('.chatbot-messages');
  const chatForm = document.getElementById('chatbotForm');
  const chatInput = document.getElementById('chatInput');
  const promptChips = document.querySelectorAll('.prompt-chip');

  // helpers for the chat window below.
  function scrollToBottom() {
    if (chatbotMessages) {
      chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
    }
  }

  function getTimeString() {
    const now = new Date();
    return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  }

  // turns **bold** and line breaks in the canned replies into html.
  // escapeHtml runs first so nothing the visitor types can inject markup.
  function formatMarkdown(text) {
    return text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" style="color: var(--secondary); text-decoration: underline;" target="_blank">$1</a>')
      .replace(/\n/g, '<br/>');
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  function showTypingIndicator() {
    const indicator = document.createElement('div');
    indicator.className = 'typing-indicator';
    indicator.id = 'typingIndicator';
    indicator.innerHTML = '<div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>';
    if (chatbotMessages) chatbotMessages.appendChild(indicator);
    scrollToBottom();
    return indicator;
  }

  function removeTypingIndicator() {
    const indicator = document.getElementById('typingIndicator');
    if (indicator) indicator.remove();
  }

  function addBotMessage(text) {
    const msgDiv = document.createElement('div');
    msgDiv.className = 'chat-msg bot';
    msgDiv.innerHTML = '<div class="msg-avatar"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 11.6a8.2 8.2 0 0 1-8.8 8.2L4 21l1.2-3.4a8.2 8.2 0 1 1 15.6-6z"/><path d="M8.6 10.8h6.8M8.6 14h4"/></svg></div><div class="msg-bubble">' + formatMarkdown(text) + '</div>';
    if (chatbotMessages) chatbotMessages.appendChild(msgDiv);
    scrollToBottom();
  }

  function addUserMessage(text) {
    const msgDiv = document.createElement('div');
    msgDiv.className = 'chat-msg user';
    msgDiv.innerHTML = '<div class="msg-bubble">' + escapeHtml(text) + '</div><span class="msg-read-time">Read ' + getTimeString() + '</span>';
    if (chatbotMessages) chatbotMessages.appendChild(msgDiv);
    scrollToBottom();
  }

  // this is the whole "AI". it looks for a few keywords and returns a
  // written-in-advance reply. there is no model behind it.
  function generateAIResponse(query) {
    const q = query.toLowerCase();

    if (q.includes('custom software') || q.includes('process') || q.includes('software process')) {
      return "Our **custom software development process** consists of four key phases:\n\n" +
             "1. **Discovery**: We delve into your operational requirements and architectural needs.\n" +
             "2. **Architecture & Strategy**: We design scalable cloud backends, database schemas, and API workflows.\n" +
             "3. **Agile Development**: Fast, iterative sprints leveraging Flutter, GoLang, React, Python, or Node.js.\n" +
             "4. **Continuous Deployment & QA**: 100% platform reliability, automated testing, and ongoing performance optimization.\n\n" +
             "Would you like to discuss a specific software idea or schedule a technical scoping call?";
    }

    if (q.match(/\b(hello|hi|hey|g'day|good morning)\b/)) {
      return "Hello. How can we help you with your digital transformation today? You can ask about our **Services**, **Client Case Studies**, **Development Process**, or **Book a Free Consultation**.";
    }

    if (q.includes('service') || q.includes('what do you do') || q.includes('capabilities')) {
      return "At **Bodhi Tech**, we specialize in:\n" +
             "• **Custom Web Development** (React, Vue, WordPress, Shopify)\n" +
             "• **Mobile App & Platform Development** (iOS, Android, Flutter, Ionic)\n" +
             "• **Digital Marketing & PPC** (SEO, Google Ads, Paid Social)\n" +
             "• **Staff Augmentation** (Dedicated engineering talent)\n" +
             "• **UX/UI & Graphic Design**\n" +
             "• **Marketing Strategy & Roadmaps**\n\n" +
             "Which area would you like to explore?";
    }

    if (q.includes('approach') || q.includes('step') || q.includes('how do you work')) {
      return "Our **4-Stage Journey**:\n" +
             "• **Phase 1: Discovery** — Unravelling brand opportunities.\n" +
             "• **Phase 2: Strategise** — Purposeful roadmaps over short-term tactics.\n" +
             "• **Phase 3: Design & Develop** — Bringing digital excellence to life.\n" +
             "• **Phase 4: Launch & Optimise** — Continuous scaling and sustained ROI.";
    }

    if (q.includes('consultation') || q.includes('contact') || q.includes('book') || q.includes('price') || q.includes('cost')) {
      return "We would love to connect! You can submit your inquiry in our [Consultation Form](#bottom_contact), or reach us directly at:\n" +
             "**+61 485 980 712**\n" +
             "**info@bodhitech.com.au**\n" +
             "**Melbourne, Australia**";
    }

    return "Thank you for reaching out! As your **Strategic Digital Partner**, Bodhi Tech combines strategy, design, and software engineering to fuel your growth.\n\n" +
           "Feel free to explore our **[Services](#services)**, review our **[Case Studies](#case-studies)**, or **[Book a Consultation](#bottom_contact)**!";
  }

  function handleChatSubmit(e) {
    if (e) e.preventDefault();
    const query = chatInput ? chatInput.value.trim() : '';
    if (!query) return;

    addUserMessage(query);
    if (chatInput) chatInput.value = '';

    showTypingIndicator();
    const delay = Math.min(800, Math.max(300, query.length * 10));

    setTimeout(() => {
      removeTypingIndicator();
      const response = generateAIResponse(query);
      addBotMessage(response);
    }, delay);
  }

  if (chatForm) chatForm.addEventListener('submit', handleChatSubmit);

  promptChips.forEach(chip => {
    chip.addEventListener('click', (e) => {
      e.preventDefault();
      const promptText = chip.getAttribute('data-prompt') || chip.textContent;
      if (chatInput) {
        chatInput.value = promptText;
        handleChatSubmit();
      }
    });
  });
});



/* ---- part 2: scroll animations ----
   REDUCE is true if the visitor asked for less motion. check it. */

document.addEventListener("DOMContentLoaded", () => {
  const REDUCE = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* looping animations pause off-screen. a dozen of them running on sections
     nobody is looking at is how you flatten a battery. */
  if (!REDUCE) {
    const liveEls = [".hero-section", ".tech-section"]
      .map((s) => document.querySelector(s))
      .filter(Boolean);
    const syncLive = () => {
      const vh = window.innerHeight || document.documentElement.clientHeight;
      liveEls.forEach((el) => {
        const r = el.getBoundingClientRect();
        el.classList.toggle("anim-live", r.top < vh + 160 && r.bottom > -160);
      });
    };
    let liveScheduled = false;
    const onLive = () => {
      if (liveScheduled) return;
      liveScheduled = true;
      /* one check per frame - a fast flick fires these dozens of times */
      const run = () => {
        liveScheduled = false;
        syncLive();
      };
      if (typeof requestAnimationFrame === "function") requestAnimationFrame(run);
      else setTimeout(run, 100);
      setTimeout(() => {
        if (liveScheduled) run();
      }, 250);
    };
    window.addEventListener("scroll", onLive, { passive: true });
    window.addEventListener("resize", onLive, { passive: true });
    window.addEventListener("load", syncLive);
    document.addEventListener("visibilitychange", syncLive);
    if ("IntersectionObserver" in window) {
      const liveObs = new IntersectionObserver(
        (entries) =>
          entries.forEach((en) =>
            en.target.classList.toggle("anim-live", en.isIntersecting)
          ),
        { rootMargin: "160px 0px" }
      );
      liveEls.forEach((el) => liveObs.observe(el));
    }
    syncLive();
  }

  /* word-by-word reveal. the split is destructive, so it runs once and
   guards on a data attribute. */
  function buildReveal(el) {
    if (!el || el.dataset.revealReady) return;
    const tokens = [];
    const pushWords = (text, cls) => {
      text.split(/\s+/).forEach((t) => {
        if (t) tokens.push({ text: t, cls: cls });
      });
    };
    [].forEach.call(el.childNodes, (node) => {
      if (node.nodeType === 3) pushWords(node.textContent, "");
      else if (node.nodeType === 1) pushWords(node.textContent, node.className || "");
    });
    el.innerHTML = tokens
      .map(
        (t) =>
          '<span class="r-word"><span' +
          (t.cls ? ' class="' + t.cls + '"' : "") +
          ">" +
          t.text +
          "</span></span>"
      )
      .join(" ");
    el.classList.add("reveal-h");
    el.dataset.revealReady = "1";
    [].forEach.call(el.querySelectorAll(".r-word > span"), (s, i) => {
      s.style.transitionDelay = i * 55 + "ms";
    });
  }
  const showReveal = (el) => el && el.classList.add("is-in");
  const hideReveal = (el) => el && el.classList.remove("is-in");

  /* the hero title gets the fancier treatment: character by character. */
  const heroTitle = document.querySelector(".hero-title");
  if (heroTitle) {
    // letter by letter, typewriter cadence. keep the highlighted word's class
    // on its characters or the accent colour is lost in the split.
    const parts = [];
    [].forEach.call(heroTitle.childNodes, (node) => {
      const cls = node.nodeType === 1 ? node.className || "" : "";
      (node.textContent || "").split(/(\s+)/).forEach((chunk) => {
        if (!chunk) return;
        if (/^\s+$/.test(chunk)) { parts.push(" "); return; }
        const letters = chunk
          .split("")
          .map(
            (ch) =>
              '<span class="r-char"><span' +
              (cls ? ' class="' + cls + '"' : "") +
              ">" +
              ch +
              "</span></span>"
          )
          .join("");
        parts.push('<span class="r-word">' + letters + "</span>");
      });
    });
    heroTitle.innerHTML = parts.join("");
    heroTitle.classList.add("reveal-h", "wind-h");
    heroTitle.dataset.revealReady = "1";
    [].forEach.call(heroTitle.querySelectorAll(".r-char > span"), (s, i) => {
      s.style.setProperty("--wx", (-0.45 - Math.random() * 0.75).toFixed(2) + "em");
      s.style.setProperty("--wy", (Math.random() * 0.6 - 0.1).toFixed(2) + "em");
      s.style.setProperty("--wr", (-4 - Math.random() * 9).toFixed(1) + "deg");
      s.style.transitionDelay = i * 45 + "ms";
    });
    if (REDUCE) showReveal(heroTitle);
    else setTimeout(() => showReveal(heroTitle), 300);
  }

  /* the card deck. --i and --mag do the positioning. */
  const deck = document.getElementById("heroDeck");
  if (deck && !REDUCE) {
    deck.classList.add("is-armed");
    setTimeout(() => {
      deck.classList.remove("is-armed");
      deck.classList.add("is-fanned");
    }, 500);
  } else if (deck) {
    deck.classList.add("is-fanned");
  }

  /* the hero scrub. fan collapses, heading un-types, copy slides away. */
  (function heroScrub() {
    const section = document.querySelector(".hero-section");
    if (!section || !deck || REDUCE) return;
    /* live, not read once. as a one-time check, narrowing the window left the
      desktop path running at phone width. */
    const NARROW = window.matchMedia("(max-width: 768px)");

    const cardEls = [].slice.call(deck.querySelectorAll(".deck-card"));
    const pillEls = [].slice.call(deck.querySelectorAll(".deck-pill"));
    const heroContent = document.querySelector(".hero-content");
    const phase2 = document.querySelector(".hero-phase2");
    const phase2Inner = document.querySelector(".hero-phase2-inner");
    const chars = heroTitle
      ? [].slice.call(heroTitle.querySelectorAll(".r-char > span"))
      : [];

    /* split the phase-2 heading into characters so it can type itself in. */
    const p2Title = document.querySelector(".hero-phase2-title");
    let p2Chars = [];
    if (p2Title) {
      const frag = [];
      [].forEach.call(p2Title.childNodes, (node) => {
        if (node.nodeName === "BR") { frag.push("<br>"); return; }
        const cls = node.nodeType === 1 ? node.className || "" : "";
        (node.textContent || "").split(/(\s+)/).forEach((chunk) => {
          if (!chunk) return;
          if (/^\s+$/.test(chunk)) { frag.push(" "); return; }
          const letters = chunk.split("").map((ch) =>
            '<span class="r-char"><span' + (cls ? ' class="' + cls + '"' : "") + ">" + ch + "</span></span>"
          ).join("");
          frag.push('<span class="r-word">' + letters + "</span>");
        });
      });
      p2Title.innerHTML = frag.join("");
      p2Title.classList.add("reveal-h", "wind-h", "is-in");
      p2Chars = [].slice.call(p2Title.querySelectorAll(".r-char > span"));
      p2Chars.forEach((s, i) => {
        s.style.setProperty("--wx", (-0.4 - Math.random() * 0.7).toFixed(2) + "em");
        s.style.setProperty("--wy", (Math.random() * 0.5 - 0.1).toFixed(2) + "em");
        s.style.setProperty("--wr", (-3 - Math.random() * 8).toFixed(1) + "deg");
      });
    }
    const ghostChar = (s) => {
      s.style.opacity = "0";
      s.style.filter = "blur(8px)";
      s.style.transform = "translate3d(var(--wx),var(--wy),0) rotate(var(--wr))";
    };
    const clearChar = (s) => {
      s.style.opacity = ""; s.style.filter = ""; s.style.transform = "";
    };

    const clamp = (v, a, b) => (v < a ? a : v > b ? b : v);
    const smooth = (e0, e1, x) => {
      const t = clamp((x - e0) / (e1 - e0), 0, 1);
      return t * t * (3 - 2 * t);
    };
    const lerp = (a, b, t) => a + (b - a) * t;

    /* phase 2: the cards fan out into a right-leaning diagonal pile. */
    const PILE = {
      "-3": { x: -170, y: -78, r: -3, s: 1.0 },
      "-2": { x: -95, y: -48, r: 1, s: 0.97 },
      "-1": { x: -22, y: -22, r: 5, s: 0.93 },
      "0": { x: 52, y: 4, r: 8, s: 0.9 },
      "1": { x: 126, y: 30, r: 11, s: 0.87 },
      "2": { x: 198, y: 56, r: 14, s: 0.84 },
      "3": { x: 264, y: 82, r: 17, s: 0.81 }
    };
    const model = cardEls.map((c) => {
      const i = parseFloat(c.style.getPropertyValue("--i")) || 0;
      const key = String(Math.round(i));
      return { c: c, i: i, mag: Math.abs(i), pile: PILE[key] || { x: 0, y: 0, r: 0, s: 0.9 } };
    });

    let scheduled = false;
    /* how much of the travel this window can hold. the cascade IS the
       animation, so scale it down rather than switch it off. */
    const fitFor = (deckW, kpx, shift) => {
      const vwNow = document.documentElement.clientWidth || window.innerWidth;
      const cardW = cardEls[0] ? cardEls[0].offsetWidth : deckW * 0.19;
      /* half the card's BOX - it ends up rotated, so the corners stick out.
          0.62 is measured, not derived. */
      const halfBox = cardW * 0.62;
      /* deck shift plus the outermost pile offset. PILE["3"].x is 264. */
      const travel = deckW * shift + 264 * kpx;
      const room = vwNow / 2 - halfBox - 22;
      return travel > room ? Math.max(0.2, room / travel) : 1;
    };

    /* ---- narrow screens ---- */
    const applyNarrow = () => {
      /* sticky over a two-screen hero, so progress is just how far past the top
         you are. not hijacked. */
      const vh = window.innerHeight || document.documentElement.clientHeight;
      const track = Math.max(1, section.offsetHeight - vh);
      const q = clamp(-section.getBoundingClientRect().top / track, 0, 1);

      /* is-scrub kills the transition, or the cards ease after the scroll */
      deck.classList.toggle("is-scrub", q > 0.004);
      deck.classList.toggle("is-collapsing", q > 0.04);

      const deckW = deck.clientWidth || 600;
      const kpx = deckW / 1000;
      const fit = fitFor(deckW, kpx, 0.16);
      const kx = kpx * fit;
      const collapse = smooth(0.05, 0.46, q);
      const scatter = smooth(0.42, 0.96, q);

      model.forEach((m) => {
        const fanX = m.i * 0.09 * deckW;
        let x = lerp(fanX, 0, collapse);
        let y = lerp(m.mag * 10 - 6, 0, collapse);
        let rot = lerp(m.i * 4, m.i * 0.5, collapse);
        let s = lerp(1.04 - m.mag * 0.04, 0.78, collapse);
        if (scatter > 0) {
          x = lerp(x, m.pile.x * kx, scatter);
          /* flatter than desktop - the heading stays put on a phone, so a full-height
           pile runs straight through it */
          y = lerp(y, m.pile.y * kpx * 0.55, scatter);
          rot = lerp(rot, m.pile.r, scatter);
          s = lerp(s, m.pile.s, scatter);
        }
        m.c.style.transform =
          "translate(-50%,-50%) translateX(" + x.toFixed(1) + "px) translateY(" +
          y.toFixed(1) + "px) rotate(" + rot.toFixed(2) + "deg) scale(" + s.toFixed(3) + ")";
      });

      /* and the deck settles back down rather than climbing up the page */
      deck.style.transform =
        "translate(" + lerp(0, deckW * 0.16 * fit, scatter).toFixed(1) + "px," +
        lerp(lerp(0, -10, collapse), 4, scatter).toFixed(1) + "px)";

      /* the award pills have nowhere to sit once the fan closes, so fade them */
      pillEls.forEach((pl) => { pl.style.opacity = (1 - smooth(0.02, 0.3, q)).toFixed(3); });
    };

    const apply = () => {
      scheduled = false;

      if (NARROW.matches) {
        if (heroContent) { heroContent.style.opacity = ""; heroContent.style.transform = ""; }
        if (phase2) { phase2.style.opacity = ""; phase2.style.pointerEvents = ""; }
        applyNarrow();
        return;
      }

      const vh = window.innerHeight || document.documentElement.clientHeight;
      const track = section.offsetHeight - vh;
      if (track <= 0) return;
      const p = clamp(-section.getBoundingClientRect().top / track, 0, 1);
      const scrubbing = p > 0.004;

      deck.classList.toggle("is-scrub", scrubbing);
      deck.classList.toggle("is-collapsing", p > 0.04);

      if (!scrubbing) {
        deck.style.transform = "";
        model.forEach((m) => (m.c.style.transform = ""));
        pillEls.forEach((pl) => (pl.style.transform = "", (pl.style.opacity = "")));
        if (heroContent) { heroContent.style.opacity = ""; heroContent.style.transform = ""; }
        if (phase2) { phase2.style.opacity = ""; phase2.style.pointerEvents = ""; }
        if (phase2Inner) { phase2Inner.style.opacity = ""; phase2Inner.style.transform = ""; }
        chars.forEach(clearChar);
        p2Chars.forEach(ghostChar);
        return;
      }

      const deckW = deck.clientWidth || 900;
      const kpx = deckW / 1000;                  // scale the pile offsets to the deck size

      /* between ~1024 and 1330 the outer card used to clip on the right edge */
      const fitX = fitFor(deckW, kpx, 0.22);
      const kx = kpx * fitX;                     // horizontal pile scale only
      const collapse = smooth(0.04, 0.30, p);    // fan -> one tight stacked card
      const spin = smooth(0.26, 0.44, p);        // the single card rotates
      const scatter = smooth(0.44, 0.9, p);      // card breaks into a right-leaning pile
      const pillT = smooth(0.02, 0.14, p);       // tag bubbles leave
      const untype = smooth(0.16, 0.38, p);      // phase-1 heading un-types (ghost trail)
      const h1gone = smooth(0.22, 0.42, p);      // whole phase-1 heading block clears out
      const p2in = smooth(0.46, 0.72, p);        // phase-2 layer fades up
      const p2type = smooth(0.5, 0.86, p);       // phase-2 heading types itself in

      model.forEach((m) => {
        const fanX = m.i * 0.09 * deckW;
        const fanY = m.mag * 10 - 6;
        const fanR = m.i * 4;
        const fanS = 1.04 - m.mag * 0.04;
        // fan collapses to one tight stack, almost no residual spread
        let x = lerp(fanX, 0, collapse);
        let y = lerp(fanY, 0, collapse);
        let r = lerp(fanR, m.i * 0.5, collapse);
        let s = lerp(fanS, 0.72, collapse);
        // then the stack opens into a right-leaning pile
        if (scatter > 0) {
          x = lerp(x, m.pile.x * kx, scatter);
          y = lerp(y, m.pile.y * kpx, scatter);
          r = lerp(r, m.pile.r, scatter);
          s = lerp(s, m.pile.s, scatter);
        }
        m.c.style.transform =
          "translate(-50%,-50%) translateX(" + x.toFixed(1) + "px) translateY(" +
          y.toFixed(1) + "px) rotate(" + r.toFixed(2) + "deg) scale(" + s.toFixed(3) + ")";
      });

      const deckY = lerp(lerp(0, -30, collapse) + lerp(0, -26, spin), -120, scatter);
      const deckX = lerp(0, deckW * 0.22 * fitX, scatter);
      const deckRot = lerp(0, -18, spin) * (1 - scatter);
      const deckScale = lerp(lerp(1, 0.66, spin), 0.94, scatter);
      deck.style.transform =
        "translate(" + deckX.toFixed(1) + "px," + deckY.toFixed(1) + "px) rotate(" +
        deckRot.toFixed(2) + "deg) scale(" + deckScale.toFixed(3) + ")";

      if (heroContent) {
        heroContent.style.opacity = (1 - h1gone).toFixed(3);
        heroContent.style.transform = "translateY(" + (h1gone * 12).toFixed(1) + "px)";
      }
      pillEls.forEach((pl) => {
        pl.style.opacity = (1 - pillT).toFixed(3);
        pl.style.transform = "scale(" + lerp(1, 0.6, pillT).toFixed(3) + ")";
      });

      if (phase2) {
        phase2.style.opacity = p2in > 0.001 ? "1" : "0";
        phase2.style.pointerEvents = p2in > 0.55 ? "auto" : "none";
      }
      if (phase2Inner) {
        phase2Inner.style.opacity = smooth(0.48, 0.66, p).toFixed(3);
        phase2Inner.style.transform = "translateY(" + lerp(24, 0, p2in).toFixed(1) + "px)";
      }
      // phase-2 heading types itself in, in word then character order
      if (p2Chars.length) {
        const show2 = p2Chars.length * p2type;
        for (let k = 0; k < p2Chars.length; k++) {
          if (k < show2) clearChar(p2Chars[k]);
          else ghostChar(p2Chars[k]);
        }
      }

      // phase-1 heading un-types from the end, leaving a soft grey ghost trail
      if (chars.length) {
        const keep = chars.length * (1 - untype);
        for (let k = 0; k < chars.length; k++) {
          const s = chars[k];
          if (k < keep) {
            clearChar(s);
          } else {
            const f = clamp((k - keep) / 5, 0, 1);
            s.style.opacity = (0.16 * (1 - f)).toFixed(3);
            s.style.filter = "none";
            s.style.transform = "none";
          }
        }
      }
    };

    const onScroll = () => {
      if (scheduled) return;
      scheduled = true;
      const run = () => { scheduled = false; apply(); };
      if (typeof requestAnimationFrame === "function") requestAnimationFrame(run);
      else setTimeout(run, 16);
      /* fall back to a direct call if rAF is throttled, e.g. a background tab. */
      setTimeout(() => { if (scheduled) run(); }, 120);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });
    document.addEventListener("visibilitychange", apply);
    section.__heroScrubApply = apply; /* test/debug hook */
    /* let the fan-out finish first, or the two fight over the transforms */
    setTimeout(() => {
      deck.classList.add("is-scrub");
      apply();
    }, 760);
  })();

  /* Tech stack: logos scattered round the copy, flying in then drifting. */
  const techScatter = document.querySelector(".tech-scatter");
  if (techScatter) {
    const techCards = [].slice.call(techScatter.querySelectorAll(".tech-badge-card"));

    /* wrap the contents - float on the inner, entrance on the outer. two
     transforms on one element and one wins silently. */
    techCards.forEach((c) => {
      const inner = document.createElement("span");
      inner.className = "tech-badge-inner";
      while (c.firstChild) inner.appendChild(c.firstChild);
      c.appendChild(inner);
    });

    /* [x%, y%, size px]. hand-placed - a generated ring looked generated. */
    const SPOTS = [
      [8, 15, 112], [22, 5, 90], [37, 15, 84], [6, 41, 104], [15, 64, 88],
      [27, 85, 108], [11, 93, 88], [43, 90, 82],
      [92, 15, 112], [80, 5, 90], [64, 16, 84], [95, 42, 104], [85, 64, 88],
      [73, 86, 108], [90, 93, 88], [58, 90, 82]
    ];
    techCards.forEach((c, i) => {
      const spot = SPOTS[i % SPOTS.length];
      const x = spot[0], y = spot[1];
      c.style.left = x + "%";
      c.style.top = y + "%";
      c.style.setProperty("--sz", spot[2] + "px");
      c.style.setProperty("--fx", Math.round((x - 50) * 2.4) + "px");
      c.style.setProperty("--fy", Math.round((y - 50) * 2.6) + "px");
      c.style.setProperty("--d", (i % 8) * 55 + "ms");
      c.style.setProperty("--dur", (4.6 + (i % 5) * 0.5).toFixed(2) + "s");
      c.style.setProperty("--delay", (-(i % 7) * 0.6).toFixed(2) + "s");
    });

    if (REDUCE) {
      techScatter.classList.add("is-in");
    } else {
      let techDone = false;
      const flyIn = () => {
        if (techDone) return;
        techDone = true;
        techScatter.classList.add("is-in");
        techObs.disconnect();
        window.removeEventListener("scroll", techOnScroll);
        document.removeEventListener("visibilitychange", techCheck);
      };
      const techCheck = () => {
        const r = techScatter.getBoundingClientRect();
        if (r.top < window.innerHeight * 0.9 && r.bottom > 0) flyIn();
      };
      const techObs = new IntersectionObserver(
        (entries) => entries.forEach((en) => en.isIntersecting && flyIn()),
        { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
      );
      techObs.observe(techScatter);
      let techTick = false;
      const techOnScroll = () => {
        if (techTick) return;
        techTick = true;
        requestAnimationFrame(() => {
          techTick = false;
          techCheck();
        });
      };
      window.addEventListener("scroll", techOnScroll, { passive: true });
      document.addEventListener("visibilitychange", techCheck);
      techCheck();
    }
  }

  /* the same word reveal, applied to every section heading on the page. */
  const sectionHeads = [].slice.call(document.querySelectorAll(".section-title"));

  sectionHeads.forEach(buildReveal);

  if (REDUCE) {
    sectionHeads.forEach(showReveal);
  } else {
    let pending = sectionHeads.slice();
    const sweep = () => {
      pending = pending.filter((h) => {
        const r = h.getBoundingClientRect();
        const inView = r.top < window.innerHeight * 0.9 && r.bottom > 0;
        if (inView) showReveal(h);
        return !inView;
      });
      if (!pending.length) {
        window.removeEventListener("scroll", onScroll);
        document.removeEventListener("visibilitychange", sweep);
      }
    };
    let ticking = false;
    const onScroll = () => {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(() => {
        ticking = false;
        sweep();
      });
    };
    /* the observer does the work. scroll and visibilitychange are a fallback
     for when it doesn't fire, bfcache being the one that bit me. */
    const headObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((en) => {
          if (en.isIntersecting) {
            showReveal(en.target);
            headObserver.unobserve(en.target);
          }
        });
      },
      { threshold: 0.2, rootMargin: "0px 0px -10% 0px" }
    );
    sectionHeads.forEach((h) => headObserver.observe(h));
    window.addEventListener("scroll", onScroll, { passive: true });
    document.addEventListener("visibilitychange", sweep);
    sweep();
  }

  /* the workhorse. RISE_GROUPS gets .anim-rise then .in, staggered.
   a new section usually just needs a selector adding here. */
  const RISE_GROUPS = [
    ["#services", ".service-bento-card"],
    [".blogs-grid", ".blog-card"],
    [".contact-landscape-bento", ".contact-hub-sidebar, .contact-form-side"],
    [".hub-pillars-list", ".hub-pillar-item"],
    /* subpage containers. add to this list, don't write a new reveal. */
    [".bento-grid", ".service-bento-card"],
    [".listing-grid", ".blog-card"],
    [".cs-grid", ".cs-card"],
    [".result-grid", ".result-card"],
    [".pillar-grid", ".pillar-card"],
    [".tech-badge-row", ".tech-badge-card"],
    [".split-aside", ".principle-card"],
    [".hero-mosaic", ".mosaic-tile"],
    [".page-hero-meta", ".phm-item"]
  ];
  let riseGroups = [];
  RISE_GROUPS.forEach(([csel, isel]) => {
    /* querySelectorAll - a page can hold several of these and querySelector
       silently animates the first and leaves the rest invisible */
    [].forEach.call(document.querySelectorAll(csel), (c) => {
      const items = [].slice.call(c.querySelectorAll(isel));
      if (!items.length) return;
      items.forEach((el, i) => {
        el.classList.add("anim-rise");
        el.style.setProperty("--d", (i % 8) * 70 + "ms");
      });
      riseGroups.push({ c: c, items: items });
    });
  });

  /* contact panels come in from their own side rather than both from below. */
  const cSide = document.querySelector(".contact-hub-sidebar");
  const cForm = document.querySelector(".contact-form-side");
  if (cSide) cSide.classList.add("anim-rise--left");
  if (cForm) cForm.classList.add("anim-rise--right");

  if (REDUCE) {
    riseGroups.forEach((g) => g.items.forEach((el) => el.classList.add("in")));
  } else if (riseGroups.length) {
    const fireGroup = (g) => g.items.forEach((el) => el.classList.add("in"));
    const riseObs = new IntersectionObserver(
      (entries) => {
        entries.forEach((en) => {
          if (!en.isIntersecting) return;
          const g = riseGroups.find((x) => x.c === en.target);
          if (g) fireGroup(g);
          riseObs.unobserve(en.target);
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
    );
    riseGroups.forEach((g) => riseObs.observe(g.c));

    const riseSweep = () => {
      for (let i = riseGroups.length - 1; i >= 0; i--) {
        const r = riseGroups[i].c.getBoundingClientRect();
        if (r.top < window.innerHeight * 0.92 && r.bottom > 0) {
          fireGroup(riseGroups[i]);
          riseGroups.splice(i, 1);
        }
      }
      if (!riseGroups.length) {
        window.removeEventListener("scroll", riseOnScroll);
        document.removeEventListener("visibilitychange", riseSweep);
      }
    };
    let riseTick = false;
    const riseOnScroll = () => {
      if (riseTick) return;
      riseTick = true;
      requestAnimationFrame(() => {
        riseTick = false;
        riseSweep();
      });
    };
    window.addEventListener("scroll", riseOnScroll, { passive: true });
    document.addEventListener("visibilitychange", riseSweep);
    riseSweep();
  }

  /* the approach cards, revealing in sequence. */
  const approachGrid = (stepGrid) => {
    const steps = [].slice.call(stepGrid.querySelectorAll(".approach-step-card"));
    stepGrid.classList.add("reveal-armed");
    steps.forEach((s, i) => (s.style.transitionDelay = i * 130 + "ms"));

    let stepDone = false;
    const revealSteps = () => {
      if (stepDone) return;
      stepDone = true;
      stepGrid.classList.remove("reveal-armed");
      const wrap = stepGrid.closest(".approach-timeline-wrap");
      if (wrap) setTimeout(() => wrap.classList.add("connectors-in"), 500);
      setTimeout(() => steps.forEach((s) => (s.style.transitionDelay = "")), 1400);
      stepObs.disconnect();
      window.removeEventListener("scroll", stepOnScroll);
      document.removeEventListener("visibilitychange", stepCheck);
    };
    const stepCheck = () => {
      const r = stepGrid.getBoundingClientRect();
      if (r.top < window.innerHeight * 0.88 && r.bottom > 0) revealSteps();
    };
    const stepObs = new IntersectionObserver(
      (entries) => entries.forEach((en) => en.isIntersecting && revealSteps()),
      { threshold: 0.15, rootMargin: "0px 0px -8% 0px" }
    );
    stepObs.observe(stepGrid);
    let stepTick = false;
    const stepOnScroll = () => {
      if (stepTick) return;
      stepTick = true;
      requestAnimationFrame(() => {
        stepTick = false;
        stepCheck();
      });
    };
    window.addEventListener("scroll", stepOnScroll, { passive: true });
    document.addEventListener("visibilitychange", stepCheck);
    stepCheck();
  };

  if (!REDUCE) {
    [].forEach.call(document.querySelectorAll(".approach-steps-grid"), approachGrid);
  }

  /* the simple case: add a class when the container scrolls in, nothing more. */
  const containerReveal = (el) => {
    if (REDUCE) {
      el.classList.add("in");
      return;
    }
    let done = false;
    const fire = () => {
      if (done) return;
      done = true;
      el.classList.add("in");
      obs.disconnect();
      window.removeEventListener("scroll", onScroll);
      document.removeEventListener("visibilitychange", check);
    };
    const check = () => {
      const r = el.getBoundingClientRect();
      if (r.top < window.innerHeight * 0.86 && r.bottom > 0) fire();
    };
    const obs = new IntersectionObserver(
      (entries) => entries.forEach((en) => en.isIntersecting && fire()),
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
    );
    obs.observe(el);
    let tick = false;
    const onScroll = () => {
      if (tick) return;
      tick = true;
      requestAnimationFrame(() => {
        tick = false;
        check();
      });
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    document.addEventListener("visibilitychange", check);
    check();
  };

  /* querySelectorAll, so a subpage can hold more than one of each container. */
  [".feat-list", ".faq-flow", ".counter-blocks", ".tst-masonry"].forEach((sel) => {
    [].forEach.call(document.querySelectorAll(sel), containerReveal);
  });

  /* the client stories filmstrip: slides sideways to centre the active card. */
  const caseCont = document.querySelector(".case-accordion-container");
  if (caseCont) {
    const casePanels = [].slice.call(caseCont.querySelectorAll(".case-accordion-panel"));

    /* wrap the panels in a track, so one transform slides the whole strip. */
    const caseTrack = document.createElement("div");
    caseTrack.className = "case-track";
    while (caseCont.firstChild) caseTrack.appendChild(caseCont.firstChild);
    caseCont.appendChild(caseTrack);

    /* slide the strip so the active card lands in the centre of the frame. */
    const centerActive = () => {
      let ai = casePanels.findIndex((p) => p.classList.contains("active"));
      if (ai < 0) ai = 0;
      const card = casePanels[ai];
      const shift =
        caseCont.clientWidth / 2 - (card.offsetLeft + card.offsetWidth / 2);
      caseTrack.style.transform = "translateX(" + Math.round(shift) + "px)";
    };
    centerActive();

    /* the accordion controller only toggles .active; re-centre when it does. */
    const caseMO = new MutationObserver(centerActive);
    casePanels.forEach((p) =>
      caseMO.observe(p, { attributes: true, attributeFilter: ["class"] })
    );
    let caseResizeT;
    window.addEventListener("resize", () => {
      clearTimeout(caseResizeT);
      caseResizeT = setTimeout(centerActive, 150);
    });

    /* cards start collapsed in a stack and deal out on scroll, like a hand
     being dealt. */
    if (!REDUCE) {
      caseCont.classList.add("deal");
      casePanels.forEach((p, i) => (p.style.transitionDelay = i * 100 + "ms"));

      let caseDone = false;
      const dealIn = () => {
        if (caseDone) return;
        caseDone = true;
        caseCont.classList.remove("deal");
        setTimeout(
          () => casePanels.forEach((p) => (p.style.transitionDelay = "")),
          1400
        );
        caseObs.disconnect();
        window.removeEventListener("scroll", caseOnScroll);
        document.removeEventListener("visibilitychange", caseCheck);
      };
      const caseCheck = () => {
        const r = caseCont.getBoundingClientRect();
        if (r.top < window.innerHeight * 0.85 && r.bottom > 0) dealIn();
      };
      const caseObs = new IntersectionObserver(
        (entries) => entries.forEach((en) => en.isIntersecting && dealIn()),
        { threshold: 0.15, rootMargin: "0px 0px -10% 0px" }
      );
      caseObs.observe(caseCont);
      let caseTick = false;
      const caseOnScroll = () => {
        if (caseTick) return;
        caseTick = true;
        requestAnimationFrame(() => {
          caseTick = false;
          caseCheck();
        });
      };
      window.addEventListener("scroll", caseOnScroll, { passive: true });
      document.addEventListener("visibilitychange", caseCheck);
      caseCheck();
    }
  }
});
