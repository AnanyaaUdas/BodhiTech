# -*- coding: utf-8 -*-
"""the long bodies: blog articles and legal pages.

kept out of content.py so that file stays readable. each is a plain html
fragment. give any new h2 an id or it won't show in the contents sidebar.
"""

# blog articles.

TRENDS = """                    <p>As we advance into 2025, the landscape of web development is undergoing a dramatic transformation. Driven by the relentless march of technological innovation, evolving user expectations, and the demand for seamless, immersive digital experiences, developers must stay abreast of the latest trends.</p>

                    <p>This article explores ten pivotal web development trends set to redefine the industry in the coming year, with a focus on practical applications and strategic insights for businesses and developers alike.</p>

                    <h2 id="ai">1. AI-powered web development</h2>
                    <p>Artificial Intelligence is revolutionising web development, empowering developers with tools that automate coding tasks and enhance user experiences. Site builders now integrate AI assistants, and developers leverage AI for code generation and quality assurance.</p>

                    <h2 id="serverless">2. Serverless architecture for scalability</h2>
                    <p>Serverless architecture, while still utilising servers, removes the burden of server management. Cloud providers dynamically allocate and scale resources, leading to cost-effective and efficient application development.</p>

                    <h2 id="wasm">3. WebAssembly for high performance</h2>
                    <p>WebAssembly enables near-native performance in web browsers, facilitating the creation of complex, high-speed web applications. It is a vital trend for developers aiming for optimal performance.</p>

                    <h2 id="pwa">4. Progressive Web Apps for enhanced user experience</h2>
                    <p>Progressive Web Apps bridge the gap between web and mobile applications, offering a fast, reliable and engaging user experience without requiring app store installations. They are crucial for improving user engagement and accessibility.</p>

                    <h2 id="jamstack">5. Jamstack for speed and security</h2>
                    <p>Jamstack architecture, built on JavaScript, APIs and Markup, decouples the front end from the back end, resulting in faster and more secure websites. This approach is gaining traction for its performance and scalability benefits.</p>

                    <h2 id="motion">6. Motion UI for interactive designs</h2>
                    <p>Motion UI enhances user engagement by incorporating animations and interactive elements into web designs. This trend is essential for creating dynamic and captivating user interfaces.</p>

                    <h2 id="blockchain">7. Blockchain integration for secure applications</h2>
                    <p>Blockchain technology is finding its place in web development, enabling secure transactions and the creation of decentralised applications. Its application is expanding across a range of sectors.</p>

                    <h2 id="voice">8. Voice search optimisation with voice interfaces</h2>
                    <p>Voice User Interfaces are becoming increasingly prevalent, allowing users to interact with web applications via voice commands. Optimising for voice search is now a critical consideration.</p>

                    <h2 id="fiveg">9. 5G connectivity for immersive web experiences</h2>
                    <p>The rollout of 5G technology is transforming mobile web experiences, supporting responsive and immersive applications. This trend is vital for delivering high-performance mobile web solutions.</p>

                    <h2 id="sustainable">10. Sustainable and ethical web development</h2>
                    <p>Ethical web development prioritises user privacy, security and environmental sustainability. Adopting green web practices is becoming increasingly important for responsible development.</p>

                    <h2 id="melbourne">Web development trends in Melbourne</h2>
                    <h3>Localised content and sustainable tech growth</h3>
                    <p>Melbourne's web development scene is characterised by a strong emphasis on local content, sustainable practices, and support for the burgeoning startup ecosystem.</p>

                    <h3>Mobile-optimised websites and advanced frameworks</h3>
                    <p>Mobile-first design is paramount, alongside the adoption of modern frameworks such as React and Vue.js.</p>

                    <h3>AI-driven security and user-centric design</h3>
                    <p>Enhanced security measures, AI integration and a focus on exceptional user experience are also key trends across the city's agencies and product teams.</p>

                    <h3>E-commerce expansion and a vibrant tech community</h3>
                    <p>The e-commerce sector is experiencing significant growth, and community engagement within the local tech scene is thriving.</p>

                    <h2 id="conclusion">Conclusion</h2>
                    <p>To remain competitive in 2025 and beyond, web development agencies and professionals must embrace these emerging trends. Whether it is the integration of AI, the adoption of sustainable practices, or catering to the specific needs of local markets like Melbourne, staying informed and adaptable is crucial for delivering exceptional web experiences.</p>

                    <blockquote>Thinking about which of these actually matter for your business? <a href="contact-us.html">Book a free consultation</a> and we will tell you which ones are worth your budget and which are noise.</blockquote>
"""

TRENDS_TOC = [
    ("ai", "1. AI-powered development"),
    ("serverless", "2. Serverless architecture"),
    ("wasm", "3. WebAssembly"),
    ("pwa", "4. Progressive Web Apps"),
    ("jamstack", "5. Jamstack"),
    ("motion", "6. Motion UI"),
    ("blockchain", "7. Blockchain"),
    ("voice", "8. Voice search"),
    ("fiveg", "9. 5G connectivity"),
    ("sustainable", "10. Sustainable development"),
    ("melbourne", "Trends in Melbourne"),
    ("conclusion", "Conclusion"),
]

PROMO = """                    <p>In today's digital landscape, a mere online presence is insufficient, particularly within the competitive promotional products sector. Your customers expect a streamlined experience, from browsing your product range to obtaining quotes and placing orders, all within a unified platform.</p>

                    <p>Whether you are an emerging promotional merchandising company catering to businesses with smaller minimum order quantities, or a large corporation specialising in sustainable merchandise, your website serves as the primary conduit to your target audience. Here are the strategies that make the difference.</p>

                    <h2 id="navigation">Enhanced navigation with mega menus</h2>
                    <p>A swift and intuitive website encourages visitor engagement, driving increased conversions. A mega menu navigation bar facilitates effortless product discovery, minimising friction throughout the purchasing journey.</p>
                    <blockquote><strong>Tip:</strong> Prioritise rapid site loading speeds, mobile responsiveness, and clear, detailed product visuals and descriptions.</blockquote>

                    <h2 id="seo">Search engine optimisation for increased visibility</h2>
                    <p>Optimising your website for search engines is crucial for attracting organic traffic. Enhance your rankings with targeted keywords, optimised product pages and pertinent content. Mobile optimisation, technical SEO and local SEO are essential for improving site performance and visibility. Read how we did exactly this for <a href="case-chilli-promotions.html">Chilli Promotions</a>.</p>
                    <blockquote><strong>Tip:</strong> Implement analytics tools to monitor and refine your optimisation strategies for superior outcomes.</blockquote>

                    <h2 id="quotes">Automated quote generation</h2>
                    <p>Offer a seamless quotation process, enabling customers to effortlessly upload logos and select colours. A transparent quoting calculator and an intuitive ordering system minimise friction and reduce cart abandonment on your custom merchandise online store. Use quote automation to deliver quotes directly to customers' inboxes.</p>
                    <blockquote><strong>Tip:</strong> Employ quote automation to identify and engage potential customers, facilitating effective nurturing and conversion.</blockquote>

                    <h2 id="trust">Building trust and authority</h2>
                    <p>A professional promotional product e-commerce platform, featuring customer reviews, case studies and secure payment options, fosters trust and credibility. Trustworthy websites instil confidence in customers, reinforcing your authority within the merchandising industry.</p>
                    <blockquote><strong>Tip:</strong> Display clear trust signals, such as secure checkout and authentic customer testimonials.</blockquote>

                    <h2 id="leads">Lead capture and management systems</h2>
                    <p>Use forms for quotes, enquiries or newsletter sign-ups to capture valuable leads. These leads can be nurtured into loyal customers for your merchandising company with targeted email campaigns or special offers.</p>
                    <blockquote><strong>Tip:</strong> Implement automated email workflows to nurture leads and boost conversion rates.</blockquote>

                    <h2 id="integrations">CRM and inventory management integrations</h2>
                    <p>Integrating CRM and inventory management systems with your promotional products website streamlines processes, reduces errors and improves the overall customer experience.</p>
                    <blockquote><strong>Tip:</strong> Synchronise your inventory and customer data to provide real-time updates and seamless order management.</blockquote>

                    <h2 id="social">Leveraging social proof</h2>
                    <p>Display customer reviews and user-generated content to increase trust and credibility in the promotional products industry. Integrating social media keeps your brand top-of-mind and boosts social proof.</p>
                    <blockquote><strong>Tip:</strong> Feature customer testimonials prominently and encourage sharing on social media to increase trust and engagement.</blockquote>

                    <h2 id="conclusion">Conclusion</h2>
                    <p>The promotional products market is highly competitive. That is why your website is more than just a digital storefront, it is an essential tool for business growth. A high-performing website can drive more traffic, convert visitors into loyal customers and improve operational efficiency.</p>

                    <p>By ensuring your site is user-friendly, optimised for search engines and integrated with the latest tools and technologies, you can stand out from competitors and set the stage for long-term success. Investing in your website's performance is not just an option, it is a strategic move to accelerate growth and future-proof your merchandising business.</p>

                    <p><a href="contact-us.html">Contact us for a free website consultation today.</a></p>
"""

PROMO_TOC = [
    ("navigation", "Mega menu navigation"),
    ("seo", "Search engine optimisation"),
    ("quotes", "Automated quote generation"),
    ("trust", "Building trust and authority"),
    ("leads", "Lead capture systems"),
    ("integrations", "CRM and inventory"),
    ("social", "Leveraging social proof"),
    ("conclusion", "Conclusion"),
]

BUDGET = """                    <p>In today's digital landscape, a website is essential. However, maintaining an optimised site can be challenging, particularly for small businesses operating on tight budgets. Are you regularly updating your website? How often do you audit its performance? Are you encountering errors in Google Search Console?</p>

                    <p>The good news is that you can achieve significant improvements without incurring substantial costs. This guide provides a range of free strategies and tools to enhance your website's performance and visibility.</p>

                    <blockquote><strong>Important note:</strong> while the tools mentioned here are free, they will require your time and effort.</blockquote>

                    <h2 id="speed">1. Supercharge your site speed</h2>
                    <p>Website speed is a critical factor for both user satisfaction and search engine rankings. A slow website leads to frustrated visitors and higher bounce rates. You can make significant improvements without spending anything.</p>

                    <h3>Compress your images</h3>
                    <p>Large image files are notorious for slowing down websites. Optimising them reduces file size without sacrificing visual quality. Use free online tools like <strong>TinyPNG</strong> and <strong>Squoosh</strong> to compress your PNG and JPEG files. For WordPress users, install free plugins such as <strong>Smush</strong> or use the free tier of <strong>ShortPixel</strong> to automate image optimisation. Aim to keep image sizes under 70&nbsp;KB.</p>

                    <h3>Minimise HTTP requests</h3>
                    <p>Every element on your webpage requires a separate request to the server. Reducing these requests noticeably improves loading speed. Check whether your theme offers options to combine CSS and JavaScript files, and use free CSS sprite generators to combine multiple small images into a single file.</p>

                    <h3>Enable browser caching</h3>
                    <p>Browser caching lets visitors' browsers store static elements locally so they are not downloaded again on subsequent visits. On WordPress, install free caching plugins like <strong>W3 Total Cache</strong> or <strong>LiteSpeed Cache</strong>. On other platforms, check your hosting provider's documentation for server-level caching and configure appropriate expiry times for static assets.</p>

                    <h3>Choose reliable hosting, even on a budget</h3>
                    <p>Your hosting provider significantly impacts speed and reliability. Research budget-friendly shared hosting known for speed and uptime, and compare introductory offers while keeping an eye on server response times and uptime guarantees.</p>

                    <h2 id="mobile">2. Make your website mobile-friendly</h2>
                    <p>With the majority of internet users browsing on mobile devices, a responsive website is no longer optional.</p>

                    <h3>Embrace responsive design with free themes</h3>
                    <p>Responsive design adapts your layout to fit different screen sizes automatically. Explore the free responsive themes in the WordPress.org repository; <strong>Astra</strong>, <strong>OceanWP</strong> and <strong>GeneratePress</strong> are popular, highly-rated options.</p>

                    <h3>Validate mobile-friendliness</h3>
                    <p>Regularly test your site for usability issues on mobile devices. Pay attention to viewport configuration, touch element sizing and text readability.</p>

                    <h3>Consider Accelerated Mobile Pages</h3>
                    <p>AMP is an open-source project designed to create very fast-loading mobile pages. On WordPress, consider the free official AMP plugin for key content such as blog posts and product pages.</p>

                    <h2 id="seo">3. Lay the foundation for search engine success</h2>
                    <p>SEO does not have to break the bank. Several free tools can materially improve your visibility in search results.</p>

                    <h3>Conduct keyword research</h3>
                    <p>Understanding what your potential customers search for is the first step. Use the free version of <strong>Google Keyword Planner</strong>, and explore tools like <strong>Ubersuggest</strong> or <strong>AnswerThePublic</strong> for additional ideas. Focus on long-tail keywords that are specific and less competitive.</p>

                    <h3>Master on-page SEO</h3>
                    <p>On-page SEO involves optimising the content and HTML of individual pages. On WordPress, the free version of <strong>Yoast SEO</strong> provides valuable guidance on titles, meta descriptions, headings and keyword use.</p>

                    <h3>Boost local visibility</h3>
                    <p>For businesses with a local presence, claim and fully optimise your free <strong>Google Business Profile</strong> with accurate information, engaging photos and actively managed customer reviews.</p>

                    <h2 id="analytics">4. Track your progress with free analytics</h2>
                    <p>Understanding how visitors interact with your website is key to making informed decisions.</p>

                    <h3>Gain insights with Google Analytics</h3>
                    <p>Set up <strong>Google Analytics</strong> and integrate it with your website to track traffic sources, bounce rate, time on page and goal completions.</p>

                    <h3>Monitor performance with Google Search Console</h3>
                    <p>Verify your website with <strong>Google Search Console</strong> and regularly check for errors or warnings affecting your visibility, and submit your sitemaps.</p>

                    <h2 id="marketing">5. Leverage free marketing tools</h2>
                    <p>Promoting your website does not always require a hefty advertising budget.</p>

                    <h3>Harness the power of social media</h3>
                    <p>Identify the platforms where your target audience spends time, develop a consistent content strategy and use native features for posting and engagement. Free scheduling tools like the free plan of <strong>Buffer</strong> help manage your presence efficiently.</p>

                    <h3>Build relationships with email marketing</h3>
                    <p>Start building your list using the free plan of <strong>Mailchimp</strong>, <strong>Brevo</strong> or <strong>MailerLite</strong>. Offer valuable incentives for sign-ups and segment your list for more targeted communication.</p>

                    <h3>Attract organic traffic with valuable content</h3>
                    <p>Creating and sharing informative content significantly boosts organic traffic over time. Use free design tools like <strong>Canva</strong> to create visually appealing graphics, and focus on high-quality, keyword-optimised content that addresses your audience's needs.</p>

                    <h2 id="ux">6. Enhance user experience</h2>
                    <p>A positive user experience keeps visitors engaged and encourages them to return.</p>

                    <h3>Keep your design clean and intuitive</h3>
                    <p>Prioritise clear navigation menus, legible fonts and a consistent visual style. A simple, easy-to-navigate website is crucial.</p>

                    <h3>Structure content for easy reading</h3>
                    <p>Use headings and bullet points to break up text and highlight key information. Ensure your headings are descriptive and incorporate relevant keywords.</p>

                    <h3>Test your user flow</h3>
                    <p>Manually test the key user journeys on your site, and ask friends or colleagues to navigate it and provide feedback. Consider <strong>Microsoft Clarity</strong>, which is completely free, or the free plan of <strong>Hotjar</strong> for basic heatmaps and session recordings.</p>

                    <h2 id="monitor">7. Continuously monitor and optimise</h2>
                    <p>Website optimisation is an ongoing process. Regularly test your website using the free versions of <strong>GTMetrix</strong> and <strong>Google PageSpeed Insights</strong>, pay attention to the identified issues, and prioritise implementing the suggested optimisations.</p>

                    <h2 id="conclusion">On a budget? No problem</h2>
                    <p>Optimising your website on a budget is entirely achievable by focusing on these key areas and leveraging the wealth of free tools available. By dedicating your time and effort, you can significantly improve your website's performance, attract more visitors and ultimately grow your business.</p>

                    <p>If you do not have the time but also have budget constraints, we are here to help. Book a 30-minute free business consultation with us and we can evaluate how we fit within your budget. If you are not ready yet, you can also check out our <a href="web-development.html">web development services</a> or the <a href="client-stories.html">work we have done</a> for other businesses like yours.</p>
"""

BUDGET_TOC = [
    ("speed", "1. Site speed"),
    ("mobile", "2. Mobile-friendly"),
    ("seo", "3. SEO foundations"),
    ("analytics", "4. Free analytics"),
    ("marketing", "5. Free marketing tools"),
    ("ux", "6. User experience"),
    ("monitor", "7. Monitor and optimise"),
    ("conclusion", "On a budget? No problem"),
]

ARTICLES = {
    "blog-web-development-trends-2025.html": {"html": TRENDS, "toc": TRENDS_TOC},
    "blog-promotional-product-ecommerce.html": {"html": PROMO, "toc": PROMO_TOC},
    "blog-optimise-website-on-a-budget.html": {"html": BUDGET, "toc": BUDGET_TOC},
}


# legal pages.
# placeholder wording. have a lawyer read these before launch.

PRIVACY = """                    <p>This Privacy Policy applies to all personal information collected by Bodhi Tech Pty Ltd (we, us or our) via the website located at bodhitech.com.au (the Website).</p>

                    <h2 id="collect">1. What information do we collect?</h2>
                    <p>The kind of Personal Information that we collect from you will depend on how you use the Website. The Personal Information which we collect and hold about you may include the information described below.</p>

                    <h2 id="types">2. Types of information</h2>
                    <p>The Privacy Act 1988 (Cth) (Privacy Act) defines types of information, including Personal Information and Sensitive Information.</p>
                    <p><strong>Personal Information</strong> means information or an opinion about an identified individual or an individual who is reasonably identifiable:</p>
                    <ul>
                        <li>whether the information or opinion is true or not; and</li>
                        <li>whether the information or opinion is recorded in a material form or not.</li>
                    </ul>
                    <p>If the information does not disclose your identity or enable your identity to be ascertained, it will in most cases not be classified as Personal Information and will not be subject to this privacy policy.</p>
                    <p><strong>Sensitive Information</strong> is defined in the Privacy Act as including information or opinion about such things as an individual's racial or ethnic origin, political opinions, membership of a political association, religious or philosophical beliefs, membership of a trade union or other professional body, criminal record or health information.</p>
                    <p>Sensitive Information will be used by us only:</p>
                    <ul>
                        <li>for the primary purpose for which it was obtained;</li>
                        <li>for a secondary purpose that is directly related to the primary purpose; and</li>
                        <li>with your consent or where required or authorised by law.</li>
                    </ul>

                    <h2 id="how">3. How we collect your Personal Information</h2>
                    <ul>
                        <li>We may collect Personal Information from you whenever you input such information into the Website, a related app, or provide it to us in any other way.</li>
                        <li>We may also collect cookies from your computer which enable us to tell when you use the Website and also to help customise your Website experience. As a general rule, however, it is not possible to identify you personally from our use of cookies.</li>
                        <li>We generally do not collect Sensitive Information, but when we do, we will comply with the preceding section.</li>
                        <li>Where reasonable and practicable we collect your Personal Information from you only. However, sometimes we may be given information from a third party; in cases like this we will take steps to make you aware of the information that was provided by a third party.</li>
                    </ul>

                    <h2 id="purpose">4. Purpose of collection</h2>
                    <ul>
                        <li>We collect Personal Information to provide you with the best service experience possible on the Website and keep in touch with you about developments in our business.</li>
                        <li>We customarily only disclose Personal Information to our service providers who assist us in operating the Website. Your Personal Information may also be exposed from time to time to maintenance and support personnel acting in the normal course of their duties.</li>
                        <li>By using our Website, you consent to the receipt of direct marketing material. We will only use your Personal Information for this purpose if we have collected such information directly from you, and if it is material of a type which you would reasonably expect to receive from us. We do not use sensitive Personal Information in direct marketing activity. Our direct marketing material will include a simple means by which you can request not to receive further communications of this nature, such as an unsubscribe link.</li>
                    </ul>

                    <h2 id="security">5. Security, access and correction</h2>
                    <p>We store your Personal Information in a way that reasonably protects it from unauthorised access, misuse, modification or disclosure. When we no longer require your Personal Information for the purpose for which we obtained it, we will take reasonable steps to destroy, anonymise or de-identify it. Most of the Personal Information that is stored in our client files and records will be kept only as long as needed to fulfil our record keeping obligations.</p>
                    <p>The Australian Privacy Principles:</p>
                    <ul>
                        <li>permit you to obtain access to the Personal Information we hold about you in certain circumstances (Australian Privacy Principle 12); and</li>
                        <li>allow you to correct inaccurate Personal Information subject to certain exceptions (Australian Privacy Principle 13).</li>
                    </ul>
                    <p>Where you would like to obtain such access, please contact us in writing using the contact details set out at the bottom of this privacy policy.</p>

                    <h2 id="complaints">6. Complaint procedure</h2>
                    <p>If you have a complaint concerning the manner in which we maintain the privacy of your Personal Information, please contact us using the contact details set out below. All complaints will be considered and we may seek further information from you to clarify your concerns. If we agree that your complaint is well founded, we will, in consultation with you, take appropriate steps to rectify the problem. If you remain dissatisfied with the outcome, you may refer the matter to the Office of the Australian Information Commissioner.</p>

                    <h2 id="contact">7. How to contact us about privacy</h2>
                    <p>If you have any queries, if you seek access to your Personal Information, or if you have a complaint about our privacy practices, you can contact us at <a href="mailto:info@bodhitech.com.au">info@bodhitech.com.au</a>, by phone on <a href="tel:+61485980712">+61 485 980 712</a>, or by post at 470 St Kilda Road, Melbourne, 3000, VIC.</p>
"""

PRIVACY_TOC = [
    ("collect", "1. What we collect"),
    ("types", "2. Types of information"),
    ("how", "3. How we collect it"),
    ("purpose", "4. Purpose of collection"),
    ("security", "5. Security and access"),
    ("complaints", "6. Complaint procedure"),
    ("contact", "7. How to contact us"),
]

TERMS = """                    <h2 id="intro">1. Introduction</h2>
                    <p>1.1. These terms and conditions govern the use of the website www.bodhitech.com.au (the Website) provided by Bodhi Tech Pty Ltd (ABN 62 159 494 412), a digital marketing and software development agency registered in Victoria, Australia.</p>
                    <p>1.2. By accessing or using the Website, you agree to be bound by these terms and conditions.</p>

                    <h2 id="use">2. Use of the Website</h2>
                    <p>2.1. You may browse the Website for information and engage with the Company's services as outlined on the Website.</p>
                    <p>2.2. The content of the pages of this Website is for your general information and use only. It is subject to change without notice.</p>

                    <h2 id="privacy">3. Privacy Policy</h2>
                    <p>3.1. Use of the Website is also governed by our <a href="privacy-policy.html">Privacy Policy</a>.</p>

                    <h2 id="ip">4. Intellectual property</h2>
                    <p>4.1. All content on this Website, including text, graphics, logos, images and software, is the property of the Company and is protected by Australian and international copyright laws.</p>
                    <p>4.2. You may not reproduce, distribute, display or transmit any content on this Website without the prior written consent of the Company.</p>

                    <h2 id="links">5. Links to other websites</h2>
                    <p>5.1. The Website may contain links to other websites provided for convenience. They do not signify that we endorse the website or websites.</p>
                    <p>5.2. We have no responsibility for the content of the linked website or websites.</p>

                    <h2 id="liability">6. Disclaimer of liability</h2>
                    <p>6.1. Information provided is for general purposes only. While we endeavour to keep the information up to date and correct, we make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability or availability of that information.</p>
                    <p>6.2. Any reliance you place on such information is therefore strictly at your own risk.</p>

                    <h2 id="law">7. Governing law</h2>
                    <p>7.1. These terms and conditions shall be governed by and construed in accordance with the laws of the State of Victoria, Australia.</p>

                    <h2 id="changes">8. Changes to terms</h2>
                    <p>8.1. The Company reserves the right to modify these terms and conditions. Users will be notified of any changes, and continued use of the Website constitutes acceptance of the modified terms.</p>
"""

TERMS_TOC = [
    ("intro", "1. Introduction"),
    ("use", "2. Use of the Website"),
    ("privacy", "3. Privacy Policy"),
    ("ip", "4. Intellectual property"),
    ("links", "5. Links to other websites"),
    ("liability", "6. Disclaimer of liability"),
    ("law", "7. Governing law"),
    ("changes", "8. Changes to terms"),
]

LEGAL = [
    ("privacy-policy.html", "Privacy <em>Policy</em>", "Privacy Policy",
     "This Privacy Policy applies to all personal information collected by Bodhi Tech Pty Ltd via the website located at bodhitech.com.au.",
     "6 Feb 2024", PRIVACY, PRIVACY_TOC),
    ("terms-and-conditions.html", "Terms &amp; <em>Conditions</em>", "Terms &amp; Conditions",
     "These terms and conditions govern the use of the website www.bodhitech.com.au provided by Bodhi Tech Pty Ltd.",
     "10 Dec 2023", TERMS, TERMS_TOC),
]
