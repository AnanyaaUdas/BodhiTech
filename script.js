
/**
 * Bodhi Tech Redesign - Core JavaScript Engine (v26)
 */

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
  // Mobile drawer
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

  // =========================================================================
  // TRANSFORMATIVE SERVICES SLIDER CONTROLLER (3 CARDS PER SLIDE - v26)
  // =========================================================================
  const servicesTrack = document.getElementById('servicesSliderTrack');
  const servicesDots = document.querySelectorAll('.services-dot');
  const servicesPrevBtn = document.getElementById('servicesPrev');
  const servicesNextBtn = document.getElementById('servicesNext');
  let currentServicesSlide = 0;
  const totalServicesSlides = 2; // Slide 0 (01-03), Slide 1 (04-06)
  let servicesAutoTimer = null;
  let isServicesHovered = false;

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

  // =========================================================================
  // EXPANDING ACCORDION SHOWCASE CONTROLLER (CASE STUDIES)
  // =========================================================================
  const accordionPanels = document.querySelectorAll('.case-accordion-panel');
  const accordionNavBtns = document.querySelectorAll('.case-nav-btn');
  let activeAccordionIdx = 0;
  let accordionAutoTimer = null;
  let isAccordionHovered = false;

  function activateAccordionPanel(idx) {
    if (!accordionPanels.length) return;
    activeAccordionIdx = idx;

    accordionPanels.forEach((panel, i) => {
      panel.classList.toggle('active', i === idx);
    });

    accordionNavBtns.forEach((btn, i) => {
      btn.classList.toggle('active', i === idx);
    });
  }

  accordionPanels.forEach((panel, index) => {
    panel.addEventListener('mouseenter', () => {
      isAccordionHovered = true;
      activateAccordionPanel(index);
    });

    panel.addEventListener('click', () => {
      activateAccordionPanel(index);
    });
  });

  accordionNavBtns.forEach((btn, index) => {
    btn.addEventListener('click', () => {
      isAccordionHovered = true;
      activateAccordionPanel(index);
    });
  });

  const accordionContainer = document.querySelector('.case-accordion-container');
  if (accordionContainer) {
    accordionContainer.addEventListener('mouseenter', () => { isAccordionHovered = true; });
    accordionContainer.addEventListener('mouseleave', () => { isAccordionHovered = false; });
  }

  function startAccordionAutoCycle() {
    if (accordionAutoTimer) clearInterval(accordionAutoTimer);
    accordionAutoTimer = setInterval(() => {
      if (!isAccordionHovered && window.innerWidth > 992) {
        const nextIdx = (activeAccordionIdx + 1) % accordionPanels.length;
        activateAccordionPanel(nextIdx);
      }
    }, 6000);
  }

  startAccordionAutoCycle();

  // =========================================================================
  // TESTIMONIALS SLIDER CONTROLLER (3 CARDS PER SLIDE)
  // =========================================================================
  const sliderTrack = document.getElementById('testimonialsSliderTrack');
  const sliderDots = document.querySelectorAll('.slider-dot');
  const prevBtn = document.getElementById('testimonialsPrev');
  const nextBtn = document.getElementById('testimonialsNext');
  let currentTestimonialSlide = 0;
  const totalSlides = 2;
  let testimonialAutoTimer = null;
  let isTestimonialHovered = false;

  function goToTestimonialSlide(slideIdx) {
    if (!sliderTrack) return;
    currentTestimonialSlide = (slideIdx + totalSlides) % totalSlides;
    sliderTrack.style.transform = 'translateX(-' + (currentTestimonialSlide * 100) + '%)';

    sliderDots.forEach((dot, idx) => {
      dot.classList.toggle('active', idx === currentTestimonialSlide);
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      goToTestimonialSlide(currentTestimonialSlide - 1);
      isTestimonialHovered = true;
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      goToTestimonialSlide(currentTestimonialSlide + 1);
      isTestimonialHovered = true;
    });
  }

  sliderDots.forEach((dot, idx) => {
    dot.addEventListener('click', () => {
      goToTestimonialSlide(idx);
      isTestimonialHovered = true;
    });
  });

  function startTestimonialAutoSlide() {
    if (testimonialAutoTimer) clearInterval(testimonialAutoTimer);
    testimonialAutoTimer = setInterval(() => {
      if (!isTestimonialHovered) {
        goToTestimonialSlide(currentTestimonialSlide + 1);
      }
    }, 6000);
  }

  startTestimonialAutoSlide();

  const testimonialsWrapper = document.querySelector('.testimonials-slider-wrapper');
  if (testimonialsWrapper) {
    testimonialsWrapper.addEventListener('mouseenter', () => { isTestimonialHovered = true; });
    testimonialsWrapper.addEventListener('mouseleave', () => { isTestimonialHovered = false; });
  }

  // CONTINUOUS COUNTER ANIMATION LOOP
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

  // Approach 1-2-3-4 loop
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

  // FAQ Accordion
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

  // Back to top
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

  // Contact form
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

  // AI Chatbot Logic
  const chatbotMessages = document.querySelector('.chatbot-messages');
  const chatForm = document.getElementById('chatbotForm');
  const chatInput = document.getElementById('chatInput');
  const promptChips = document.querySelectorAll('.prompt-chip');

  function scrollToBottom() {
    if (chatbotMessages) {
      chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
    }
  }

  function getTimeString() {
    const now = new Date();
    return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  }

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
    msgDiv.innerHTML = '<div class="msg-avatar">👤</div><div class="msg-bubble">' + formatMarkdown(text) + '</div>';
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

  function generateAIResponse(query) {
    const q = query.toLowerCase();

    if (q.includes('custom software') || q.includes('process') || q.includes('software process')) {
      return "Our **custom software development process** consists of four key phases:\n\n" +
             "1. 🔍 **Discovery**: We delve into your operational requirements and architectural needs.\n" +
             "2. 📐 **Architecture & Strategy**: We design scalable cloud backends, database schemas, and API workflows.\n" +
             "3. 💻 **Agile Development**: Fast, iterative sprints leveraging Flutter, GoLang, React, Python, or Node.js.\n" +
             "4. 🚀 **Continuous Deployment & QA**: 100% platform reliability, automated testing, and ongoing performance optimization.\n\n" +
             "Would you like to discuss a specific software idea or schedule a technical scoping call?";
    }

    if (q.match(/\b(hello|hi|hey|g'day|good morning)\b/)) {
      return "Hello! 👋 How can we help you with your digital transformation today? You can ask about our **Services**, **Client Case Studies**, **Development Process**, or **Book a Free Consultation**.";
    }

    if (q.includes('service') || q.includes('what do you do') || q.includes('capabilities')) {
      return "At **Bodhi Tech**, we specialize in:\n" +
             "• 🌐 **Custom Web Development** (React, Vue, WordPress, Shopify)\n" +
             "• 📱 **Mobile App & Platform Development** (iOS, Android, Flutter, Ionic)\n" +
             "• 📈 **Digital Marketing & PPC** (SEO, Google Ads, Paid Social)\n" +
             "• 👥 **Staff Augmentation** (Dedicated engineering talent)\n" +
             "• 🎨 **UX/UI & Graphic Design**\n" +
             "• 🎯 **Marketing Strategy & Roadmaps**\n\n" +
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
             "📞 **+61 405 500 551**\n" +
             "✉️ **info@bodhitech.com.au**\n" +
             "📍 **Melbourne, Australia**";
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



document.addEventListener("DOMContentLoaded", () => {
    const title = document.querySelector(".hero-title");
    if(!title) return;
    
    const text1 = "Where Innovation Meets ";
    const text2 = "Enlightenment";
    
    title.innerHTML = "<span class=\"cursor\"></span>";
    let i = 0;
    
    function type() {
        if(i < text1.length) {
            let typed = text1.substring(0, i+1);
            title.innerHTML = typed + "<span class=\"cursor\"></span>";
            i++;
            setTimeout(type, 35);
        } else if (i < text1.length + text2.length) {
            let text2Index = i - text1.length;
            let typed1 = text1;
            let typed2 = text2.substring(0, text2Index+1);
            title.innerHTML = typed1 + "<span class=\"highlight\">" + typed2 + "</span><span class=\"cursor\"></span>";
            i++;
            setTimeout(type, 50);
        } else {
            document.querySelector(".cursor").classList.add("blink");
        }
    }
    setTimeout(type, 400);
});

