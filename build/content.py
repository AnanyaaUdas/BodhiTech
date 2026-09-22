# -*- coding: utf-8 -*-
"""all the words: copy, figures, client names, image urls.

no html in here - blocks.py decides what it looks like. this is the file a
non-developer can safely edit. australian spelling throughout.
"""

# phone, email and address. used in the header, footer and contact page,
# so changing it here changes it everywhere.
SITE = {
    "phone": "+61 485 980 712",
    "phone_href": "tel:+61485980712",
    "email": "info@bodhitech.com.au",
    "address": "470 St Kilda Road, Melbourne, 3000, VIC",
}

# bits of text that appear on lots of different pages, so they are written
# once here.

PILLARS = [
    ("Strategic Partner",
     "We transcend the conventional client-vendor relationship, positioning ourselves as your dedicated Strategic Partner."),
    ("Rapid Development",
     "Speed is at the core of our ethos. We believe in turning concepts into reality with unprecedented efficiency."),
    ("Budget-Friendly",
     "Unleash the power of technology without breaking the bank. We believe in making advanced technology accessible to businesses of all sizes."),
    ("Innovation Catalyst",
     "We thrive on pushing boundaries and exploring new horizons, consistently introducing inventive solutions that set you apart in the market."),
]

# same idea, but worded for the industry pages.
INDUSTRY_PILLARS = [
    ("Industry-Specific Solutions",
     "Designed to address the specific needs and challenges of your industry, providing targeted solutions that maximise efficiency and effectiveness."),
    ("Deep Industry Knowledge",
     "We bring a wealth of industry-specific insights to our solutions, ensuring that we deliver results that truly resonate with your business objectives."),
]

# client quotes. (quote, name, role, company).
TESTIMONIALS = [
    ("Perfect Strategic Partners",
     "We knew how we wanted to solve the business problem from a strategic point of view, and a high level perspective. But really understanding how to translate that into something that people could feel and touch was where we needed expertise and assistance. That was the gap that Bodhi filled in the beginning. Ever since then, each time and whatever it may be, Bodhi has always been able to fill gaps in our team and our own capabilities. And so we continue our growth.",
     "Tom Humphries", "Co-Founder and CEO, Boobobutt",
     "https://bodhitech.com.au/wp-content/uploads/2023/11/tom-1.webp"),
    ("Trust and Transparency",
     "One of the reasons I've stayed with Bodhi Tech is that there hasn't been any issues that they haven't been able to solve; a problem that they weren't able to solve. So anything that I've thrown at them, Bodhi Tech knows how to do it. I've got a level of trust in terms of their capability. On the other hand, if there is something that they can't do and they just tell me they can't do it. That's the level of transparency that they are willing to give me.",
     "David Plush", "CEO &amp; Co-Founder, Ume Co Pty Ltd",
     "https://bodhitech.com.au/wp-content/uploads/2023/12/david-1.webp"),
    ("Tackling Challenges Together",
     "My biggest challenge was my lack of knowledge. I felt I had a great idea but I didn't know what I needed to do to bring it to life. I didn't know who I was looking for. I didn't know what costs to expect. When I first spoke with the team at Bodhi Tech, they were able to break down everything so that I could understand the process. It's not just a case of &ldquo;okay, here's my money, go and do your thing&rdquo;, it has been a real partnership.",
     "Luke Ellis", "CEO, Take A Local",
     "https://bodhitech.com.au/wp-content/uploads/2023/11/luke-1.webp"),
    ("Revitalizing Innovation",
     "Collaborating with Bodhi Tech, particularly with Sid, their founder, was an absolute pleasure. What truly impressed us was Bodhi Tech's adeptness in transforming our vision into a comprehensive marketing strategy. Moreover, their design and web development team worked tirelessly to give our brand a modern, refreshed look. The revitalized website not only accurately reflects our brand but also radiates the innovation and modernity we aimed for.",
     "Jennifer Ford", "Manager, Dive Works Subsea Solutions",
     "https://bodhitech.com.au/wp-content/uploads/2024/03/Jennifer-Ford.jpg"),
    ("Dream Team",
     "Bodhi Tech's approach was a breath of fresh air. Instead of rushing into solutions, they took the time to understand our brand heritage, values, and aspirations. By embracing this methodical process, Bodhi Tech crafted a website that not only reflects our contemporary vision but also pays homage to our reputable standing. The outcome? A harmonious blend of modernity and tradition, leading to heightened online presence, increased client attraction, and tangible business growth.",
     "Vince Gill", "Managing Director, Capability",
     "https://bodhitech.com.au/wp-content/uploads/2024/08/Vince-Gill.jpg"),
    ("Proactive and Reliable",
     "Exceptional White-Label PPC &amp; Design Support of unparalleled quality. Their seamless integration into our team, managing our PPC and Paid Ads accounts with precision and creativity, has been a testament to their adaptability. Their proactive approach, quick turnaround, and deep expertise made them an invaluable partner for our agency. I highly recommend Bodhi Tech to anyone looking for reliable and top-tier digital marketing support.",
     "Dav Lippasaar", "Director &amp; Founder, SAAR&reg; Media",
     "https://bodhitech.com.au/wp-content/uploads/2024/08/SAAR%C2%AE-Media-Dav-Lippasaar.jpg"),
]

# the logos in the scrolling strip.
TRUST_LOGOS = [
    ("https://bodhitech.com.au/wp-content/uploads/2026/05/Loop-Logics-Logo-Black-Png-2048x263-1.webp", "Loop Logics"),
    ("https://bodhitech.com.au/wp-content/uploads/2024/02/Boobobutt-new.png", "Boobobutt"),
    ("https://bodhitech.com.au/wp-content/uploads/2024/02/Aridzone.webp", "Aridzone"),
    ("https://bodhitech.com.au/wp-content/uploads/2024/02/Conifr.webp", "Conifr"),
    ("https://bodhitech.com.au/wp-content/uploads/2023/12/Take-A-Local.png", "Take A Local"),
    ("https://bodhitech.com.au/wp-content/uploads/2024/02/Ume-Green-2.png", "Ume"),
    ("https://bodhitech.com.au/wp-content/uploads/2024/02/Montdami.webp", "Montdami"),
    ("https://bodhitech.com.au/wp-content/uploads/2024/11/chillilogo.png", "Chilli Promotions"),
]

# the client stories. each one becomes its own page plus a card on the
# client stories index, and they fill the accordion on the home page.
CASES = [
    {
        "slug": "case-chilli-promotions.html",
        "name": "Chilli Promotions",
        "category": "Promotional Products",
        "title": "Revitalising the brand Chilli Promotions",
        "teaser": "Chilli Promotions had an outdated, non-responsive website that presented them as a vendor of basic branded products rather than the full-service promotions partner they had become. We rebuilt the brand's digital presence around what they actually do.",
        "logo": "https://bodhitech.com.au/wp-content/uploads/2024/11/chillilogo.png",
        "thumb": "https://bodhitech.com.au/wp-content/uploads/2024/11/Chili-New.webp",
        "stats": [("+437%", "Online inquiries"), ("+312%", "Website traffic"), ("+203%", "Organic traffic")],
        "challenge": "Chilli Promotions faced an outdated, non-responsive website that failed to reflect their full capabilities as a comprehensive promotions partner. The site misrepresented them as merely a vendor of basic branded products rather than showcasing their complete range of services. They lacked an effective digital strategy to highlight innovative offerings and attract potential customers.",
        "solution": "Bodhi Tech conducted thorough discovery to understand their customers and market positioning. We developed a modern, responsive website accurately reflecting the brand's full-service capabilities, implemented a content strategy featuring blog posts and case studies, and optimised the site with SEO to drive traffic and sales.",
        "services": ["Website Design", "Website Development", "SEO Services", "Content Strategy",
                     "Responsive Website Design", "Improved User Experience",
                     "Performance Tracking Setup", "SEO Strategy and Implementation"],
        "tech": ["Figma", "WordPress", "PHP", "MySQL", "HTML", "CSS", "jQuery", "Bootstrap"],
        "quote": "After a disappointing experience with our previous provider, switching to Bodhi Tech was the best decision we made.",
        "quote_name": "Rion Shelley",
        "quote_role": "Brand &amp; Marketing Consultant, Chilli Promotions",
    },
    {
        "slug": "case-take-a-local.html",
        "name": "Take A Local",
        "category": "Travel Technology",
        "title": "Jumpstarting Take A Local, bringing a groundbreaking travel app to life",
        "teaser": "A first-time founder with a clear vision for a GPS-driven self-guided audio tour app, no technical background, and quotes well beyond his budget. We took him from idea to a live MVP in under six months.",
        "logo": "https://bodhitech.com.au/wp-content/uploads/2023/12/Take-A-Local.png",
        "thumb": "https://bodhitech.com.au/wp-content/uploads/2024/03/Thumbnail-TAL-2.png",
        "stats": [("98%", "Turn-by-turn accuracy"), ("&lt;6 mo", "Idea to live MVP"), ("50%", "Lower than agency quotes")],
        "challenge": "First-time founder Luke Ellis envisioned a self-guided audio tour app with GPS integration for Tasmania. Despite having a clear vision, he lacked technical implementation knowledge and received development quotes that far exceeded his budget.",
        "solution": "Bodhi Tech ran a strategic alignment process, then delivered an MVP within six months using Flutter for mobile and Laravel for the backend. We implemented Mapbox and Google Maps for real-time navigation with smart caching so the tours keep working offline.",
        "services": ["Cross Platform Mobile &amp; Web App Development", "Website Development",
                     "Brand Identity Design", "UX/UI Design", "Go To Market Strategy",
                     "Digital Marketing Services"],
        "tech": ["Flutter", "Laravel", "Sembast", "PostgreSQL", "Amazon AWS", "PHP", "Vue.js", "Bootstrap", "Ubuntu"],
        "quote": "My biggest challenge was my lack of knowledge. When I first spoke with the team at Bodhi Tech, they were able to break down everything so that I could understand the process. It's been a real partnership.",
        "quote_name": "Luke Ellis",
        "quote_role": "CEO, Take A Local",
    },
    {
        "slug": "case-boobobutt.html",
        "name": "Boobobutt",
        "category": "Kids' Activities Platform",
        "title": "Empowering Boobobutt",
        "teaser": "Meet Boobobutt, the trailblazing Kids' Activities Discovery Platform based down under in sunny Australia. Founded by Tom Humphries, who, inspired by his own little one, envisioned making kid activities a breeze for parents.",
        "logo": "https://bodhitech.com.au/wp-content/uploads/2023/12/boobobutt-white.png",
        "thumb": "https://bodhitech.com.au/wp-content/uploads/2024/03/Thumbnail-Boobobutt-2.png",
        "stats": [("150K", "Monthly traffic"), ("&lt;6 mo", "Ideation to launch"), ("4", "Brands grown from one")],
        "challenge": "Boobobutt possessed a strong concept but faced a critical gap: the non-technical founder needed guidance on translating business vision into technological reality. The platform required strategic direction and technical expertise to launch successfully.",
        "solution": "Bodhi Tech conducted comprehensive market research to validate and shape the product strategy alongside founder Tom Humphries' aspirations. We defined a Minimum Viable Product and provided the strategic guidance to bridge vision and execution, then stayed on as the platform grew into four brands.",
        "services": ["Website Development", "Website Maintenance", "Mobile App Development",
                     "Comprehensive Digital Marketing Services", "Staff Augmentation"],
        "tech": ["WordPress", "Flutter", "MySQL", "PHP", "Laravel", "Google Cloud"],
        "quote": "We knew how we wanted to solve the business problem from a strategic point of view. But really understanding how to translate that into something that people could feel and touch was where we needed expertise.",
        "quote_name": "Tom Humphries",
        "quote_role": "Co-Founder and CEO, Boobobutt",
    },
    {
        "slug": "case-capability.html",
        "name": "Capability",
        "category": "Management Consulting",
        "title": "Modernising Capability's brand and website",
        "teaser": "Capability, a prominent management consultancy established in 1994, provides strategic advice to major corporations and government agencies in Australia. They needed a modern presence that still felt trustworthy to a distinguished clientele.",
        "logo": "https://bodhitech.com.au/wp-content/uploads/2023/12/cap-logo.png",
        "thumb": "https://bodhitech.com.au/wp-content/uploads/2024/03/Thumbnail-cap.png",
        "stats": [("&gt;100%", "Increase in online visibility"), ("+256%", "Average session duration"), ("9/10", "Internal satisfaction score")],
        "challenge": "Capability's existing website was outdated and failed to reflect the brand's full potential. Leadership needed a modern, sophisticated website communicating their value proposition and attracting new clients, while maintaining the trustworthiness and credibility their corporate and government clientele expect.",
        "solution": "Bodhi Tech partnered closely with Capability, understanding its heritage and goals. We adopted a user-centred design process with extensive stakeholder feedback, creating a website that balances modernity with credibility and resonates with distinguished clients.",
        "services": ["Marketing Strategy", "UX/UI and Graphic Design", "WordPress Website Development"],
        "tech": ["Figma", "WordPress", "PHP"],
        "quote": "Bodhi Tech's approach was a breath of fresh air. Instead of rushing into solutions, they took time to understand our brand heritage, values, and aspirations.",
        "quote_name": "Vince Gill",
        "quote_role": "Managing Director, Capability",
    },
]

# the services we offer.
#
# add an entry here and everything updates by itself on the next build: the
# service gets its own page, a card on the solutions index, a line in the
# menu and a link in the footer. you do not touch any html.
#
# what each entry needs:
#   slug     the file name it becomes, e.g. "web-development.html"
#   name     the full title
#   short    the shorter name, for menus and breadcrumbs
#   summary  the one-line description shown on the cards

SOLUTIONS = [
    {
        "slug": "web-development.html",
        "nav": "solutions",
        "name": "Web Development Service",
        "short": "Web Development",
        "tag": "Solutions",
        "h1": "Web Development <em>Service</em>",
        "lead": "Elevate your online presence with our bespoke website development services.",
        "meta": [("100+", "Websites shipped"), ("5+", "Years in market"), ("74", "Net Promoter Score")],
        "summary": "We build websites that not only align with your brand but also deliver results aligned with your business goals.",
        "intro_h": "Crafting digital excellence: bespoke website development by Bodhi Tech",
        "intro_p": [
            "Your brand's digital journey begins with a website that goes beyond aesthetics. It's a dynamic reflection of your identity, a virtual gateway to connect with your audience.",
            "At Bodhi Tech, we understand that a website is more than just code and graphics; it's your 24/7 storefront, your brand ambassador in the digital realm. Whether you're a budding startup or a growing business, we're here to sculpt a web solution that aligns perfectly with your goals.",
            "Unleash the potential of your brand online. Let's build a website that not only looks impressive but also works wonders for your business.",
        ],
        "principles": [
            ("Strategic Partner",
             "We go beyond conventional service providers, aligning our expertise with your unique goals to craft tailored solutions. Elevate your brand with a partner committed to driving innovation, fostering growth, and ensuring lasting success in the dynamic world of technology."),
            ("User Centricity",
             "We believe that a seamless and intuitive user experience forms the foundation of a successful digital presence. By focusing on user needs, behaviours and interactions, we ensure that every design element serves a purpose, creating not just visually appealing interfaces but functional and engaging experiences."),
        ],
        "approach_h": "Our Approach",
        "approach_sub": "From the first discovery session to ongoing optimisation, here is how a Bodhi Tech website comes together.",
        "steps": [
            ("Discovery", "The journey begins with discovery. In our discovery session, we unravel the intricacies of your brand, goals, and aspirations. Together, we lay the foundation for a website that truly reflects your unique identity and resonates with your target audience."),
            ("UX/UI Design", "Once we've mapped out your vision, our design wizards work their magic. At Bodhi, user experience takes precedence, laying the foundation for visually compelling aesthetics. Understanding your audience and their needs is paramount, and it's the compass guiding our design philosophy."),
            ("Development", "In the development stage, we bring your digital vision to life with a commitment to industry-leading best practices. Our seasoned developers meticulously code each component, adhering to the highest standards of security, performance, and responsiveness. We prioritise scalability, ensuring your website not only meets current needs but is well-equipped for future growth."),
            ("Testing", "Our rigorous testing protocols go beyond standard practices, meticulously scrutinising every element to guarantee seamless functionality, optimal performance, and an impeccable user experience. From cross-browser compatibility to responsive design validation, our testing ensures that your website performs flawlessly across diverse platforms and devices."),
            ("Launch", "Experience the thrill of your website's debut with Bodhi Tech, where we handle every detail to ensure a stress-free launch. From domain setup to server configurations, leave the technical intricacies to us. Your focus remains on the excitement of unveiling your digital presence, while we expertly orchestrate a seamless launch."),
            ("Optimise", "The launch is just the beginning of our commitment to your digital success. We are continuously refining and enhancing based on real-time analytics, user feedback, and emerging trends. But that's not all: unlock additional value with our expert services in digital marketing and SEO."),
        ],
        "offer_h": "Digital excellence: websites, SEO, marketing and more",
        "offer_sub": "Crafting engaging websites and digital experiences tailored for your success",
        "offerings": [
            ("WordPress Development", "We love WordPress for its unparalleled flexibility and user-friendly interface, enabling us to seamlessly bring your digital vision to life with creativity and efficiency. Rely on our seasoned team of WordPress developers and designers to create a new website or revamp your existing WordPress site."),
            ("Bespoke Custom Build Websites", "Sometimes, off-the-shelf solutions fall short of capturing the essence of your brand. That's where our dedicated team steps in, meticulously crafting personalised websites that resonate with your unique identity, ensuring your digital presence is as exceptional as your vision."),
            ("eCommerce Websites", "Transform your business into an online retail powerhouse with Bodhi Tech's eCommerce website services. Whether you're looking to set up shop on popular platforms like Shopify, Maropost, BigCommerce, WooCommerce or build a completely bespoke custom store, our expert team ensures a seamless and visually stunning eCommerce experience."),
            ("Website Maintenance", "We understand that a website is a living entity that requires ongoing care and updates. From regular security checks to content updates and performance optimisations, our maintenance services ensure your website remains secure, up-to-date, and continues to deliver an optimal user experience."),
            ("SEO", "Beyond crafting visually stunning and functional websites, we ensure your digital presence doesn't go unnoticed. From keyword optimisation to strategic link-building, our SEO services are tailored to propel your website to the top of search engine rankings, enhancing your brand's discoverability and driving targeted traffic."),
            ("Digital Marketing", "Amplify your online presence with Bodhi Tech's extended digital marketing services, seamlessly integrating strategic PPC campaigns, engaging organic and paid social media initiatives, and Google Business Profile optimisation for enhanced local discoverability."),
        ],
    },
    {
        "slug": "marketing-strategy.html",
        "nav": "solutions",
        "name": "Marketing Strategy",
        "short": "Marketing Strategy",
        "tag": "Solutions",
        "h1": "Marketing <em>Strategy</em>",
        "lead": "Bodhi Tech crafts impactful marketing strategies, prioritising a strategy-first approach. We specialise in tailored plans to maximise brand visibility and achieve business goals effectively.",
        "meta": [("60+", "Strategies delivered"), ("5+", "Years in market"), ("74", "Net Promoter Score")],
        "summary": "Unlock your business potential with expert marketing strategy services designed to drive growth, engagement and brand success.",
        "intro_h": "Our transformational solutions elevating the success",
        "intro_p": [
            "At Bodhi Tech, we don't just implement marketing tactics; we craft comprehensive strategies that drive real results. We firmly believe that a strategy-first approach is the cornerstone of success in today's dynamic business landscape.",
            "A comprehensive plan can help your business achieve its goals and objectives through effective promotion and communication.",
        ],
        "principles": [
            ("Customisation and Tailored Approach",
             "We don't believe in one-size-fits-all solutions. Instead, we conduct in-depth research to understand your industry, target audience, and competitive landscape before a single tactic is put on the table."),
            ("Data-Driven Decision-Making",
             "We leverage analytics and key performance indicators to measure the success of each marketing initiative, so the strategy keeps sharpening itself against real numbers rather than assumptions."),
        ],
        "approach_h": "Our Approach",
        "approach_sub": "From initial discovery and meticulous planning to innovative design and seamless execution.",
        "steps": [
            ("Discovery and Research", "In the initial phase, our team conducts a thorough analysis to understand your business, industry, and market dynamics. This involves in-depth research into your competitors, target audience, and emerging trends."),
            ("Strategic Planning", "Based on the insights gathered during the discovery phase, we develop a comprehensive strategic plan tailored to your business needs. This plan outlines the overarching marketing goals, target audience profiles, and key performance indicators that will be used to measure success."),
            ("Implementation and Execution", "The implementation phase involves creating and deploying marketing campaigns across chosen channels. Content creation, design, and messaging are aligned with the brand strategy developed earlier."),
            ("Monitoring and Optimisation", "We regularly assess the performance of campaigns against established KPIs, analysing data and feedback to refine our approach. Insights gained from monitoring help us adapt to changing market conditions and consumer behaviours."),
        ],
        "offer_h": "Holistic marketing solutions for strategic success",
        "offer_sub": "Research, goals, multi-channel campaigns and data-driven optimisation for success",
        "offerings": [
            ("Market Research Excellence", "Our service includes in-depth market research to gain a profound understanding of your industry, competitors, and target audience. This involves analysing market trends, consumer behaviours, and competitor strategies. Through this offering, we provide you with valuable insights that form the foundation of a successful marketing strategy."),
            ("Strategic Goal Setting", "We collaborate with you to define clear and achievable marketing goals aligned with your overall business objectives. Our team works on developing a strategic plan that outlines the steps and tactics needed to reach these goals, ensuring your marketing efforts are purposeful and directed towards measurable outcomes."),
            ("Multi-Channel Campaigns", "Leveraging our expertise in various marketing channels, we design and implement multi-channel campaigns tailored to your business. By utilising a mix of digital and traditional channels such as social media, email marketing, content marketing, and advertising, we maximise your brand's visibility and engagement."),
            ("Data-Driven Optimisation", "A key differentiator of our service is the emphasis on data-driven decision-making. We monitor the performance of marketing campaigns in real time, utilising analytics and key performance indicators to assess their effectiveness and make informed adjustments to the strategy."),
        ],
    },
    {
        "slug": "ux-ui-graphic-design.html",
        "nav": "solutions",
        "name": "UX/UI and Graphic Design",
        "short": "UX/UI Design",
        "tag": "Solutions",
        "h1": "UX/UI and <em>Graphic Design</em>",
        "lead": "Discover a transformative blend of functionality and aesthetics with Bodhi Tech's UX/UI design services.",
        "meta": [("100+", "Projects designed"), ("9/10", "Client satisfaction"), ("74", "Net Promoter Score")],
        "summary": "Conversion-focused UI/UX and graphic design, blending aesthetics and functionality for impactful user experiences.",
        "intro_h": "Elevate user experiences with Bodhi Tech's UX/UI design services",
        "intro_p": [
            "At Bodhi Tech, we understand that a seamless and intuitive user experience is the heartbeat of successful digital solutions.",
            "Our UX/UI design services are not just about aesthetics; they're about creating meaningful interactions that captivate and engage your audience.",
        ],
        "principles": [
            ("User Centric Design",
             "Our empathetic approach ensures that every design decision is rooted in addressing user needs, fostering engagement, and enhancing overall satisfaction."),
            ("Strategic Design for Impactful Results",
             "While aesthetics are crucial, we go further. Our strategic approach guarantees designs that captivate, convert, and leave a lasting impression on your audience."),
        ],
        "approach_h": "Our Approach",
        "approach_sub": "Our process is rooted in the design thinking principle: empathise, define, ideate, prototype and test.",
        "steps": [
            ("Empathise", "User research is our starting point for every UX/UI project. In this phase, we step into the shoes of your users, immersing ourselves in their world. We go beyond surface-level understanding, seeking to grasp their needs, aspirations, and challenges on a profound level."),
            ("Define", "Armed with a profound understanding gained from user research, we transform insights into actionable strategies. We collaborate closely with you to outline project goals, establish user personas, and pinpoint the specific objectives that will guide our design journey."),
            ("Ideate", "This phase is a dynamic burst of creativity. Here, we break free from the constraints, fostering a collaborative environment to generate a myriad of innovative ideas. Through brainstorming sessions and ideation workshops, we explore diverse possibilities. No idea is too big or too small."),
            ("Prototype", "We take the concepts born during the ideation phase and transform them into interactive prototypes. This hands-on approach allows us to test functionalities, gather valuable feedback, and refine the user journey before committing to the final design."),
            ("Test", "We conduct rigorous testing, putting our prototypes through real-world scenarios to validate design decisions. User feedback is collected, analysed, and integrated into the refinement process. This iterative testing loop ensures we are doing everything we can to achieve our core objective."),
        ],
        "offer_h": "UX/UI and graphic design offerings",
        "offer_sub": "Research-led design that carries through from product screens to brand collateral",
        "offerings": [
            ("User Research", "Harness the power of empathy-driven design. Our research delves deep into user needs and behaviours, ensuring that every design decision is rooted in a profound understanding of your audience."),
            ("Design Sprint Facilitation", "Expedite your design process with our design sprint facilitation services. Condense months of work into a focused, collaborative week, accelerating your path to innovative solutions."),
            ("Design Thinking Workshops", "Empower your team with design thinking. Our workshops instil a design-centric mindset, fostering a culture of innovation and problem-solving within your organisation."),
            ("Graphic Design Services", "We extend our design expertise beyond the digital realm with our comprehensive graphic design services. Building on the principles of UX/UI design, our graphic designers seamlessly blend creativity and strategy to elevate your brand aesthetics across various platforms."),
        ],
    },
    {
        "slug": "staff-augmentation.html",
        "nav": "solutions",
        "name": "Staff Augmentation",
        "short": "Staff Augmentation",
        "tag": "Solutions",
        "h1": "Staff <em>Augmentation</em>",
        "lead": "Unlock the power of a dedicated team that not only meets your needs but seamlessly integrates with your company culture.",
        "meta": [("2x", "Clutch recognised, 2024"), ("5+", "Years placing talent"), ("74", "Net Promoter Score")],
        "summary": "Elevate your team's capabilities with seamless dedicated human resource solutions for enhanced productivity and expertise.",
        "intro_h": "Our transformational solutions elevating the success",
        "intro_p": [
            "We go beyond conventional augmentation by curating talent across software engineering, digital marketing, graphic design and sales.",
            "Cultural alignment and modern methodologies for distributed work environments sit at the centre of how we place people, not as an afterthought.",
        ],
        "principles": [
            ("Flexibility and Scalability",
             "Scale your team based on project requirements, workload fluctuations, or specific skill needs, without carrying permanent headcount you don't yet need."),
            ("Access to Specialised Skills and Expertise",
             "Tap into a vast pool of specialised skills and expertise such as web developers, designers and marketers, matched to the scope of the job in front of you."),
        ],
        "approach_h": "Our Approach",
        "approach_sub": "From initial discovery through to placement, we handle the search so you meet only the right people.",
        "steps": [
            ("Discovery", "During this stage, we thoroughly understand your requirements, objectives, and the specific skills needed so that we can find the right person who will fit your business goals, culture, and the scope of the job."),
            ("Talent Hunt", "We initiate a talent hunt to identify potential candidates. Using various resources, including databases, networks, and recruitment channels, we find professionals with the requisite skills and experience."),
            ("Screening and Assessment", "In the screening and assessment phase, the shortlisted candidates undergo a thorough evaluation. The screening process includes reviewing resumes, conducting initial interviews, and assessing technical skills."),
            ("Placement", "The next phase is for you to conduct final interviews and make the ultimate hiring decisions. The placement phase involves finalising the selection of candidates and integrating them into your team."),
        ],
        "offer_h": "Staff augmentation offerings",
        "offer_sub": "Outsourced talent, the right fit for your team",
        "offerings": [
            ("Talent Sourcing and Acquisition", "We excel in identifying and acquiring skilled professionals to meet specific business needs. This includes talent sourcing through various channels, such as job boards, social networks, and industry connections. We maintain extensive databases of qualified candidates and employ effective recruitment strategies to build a pool of suitable talent."),
            ("Skill Assessment and Screening", "A crucial aspect of staff augmentation is ensuring that candidates possess the required skills and expertise. We offer skill assessment and screening services to evaluate technical proficiency, soft skills, and cultural fit with the organisation, so the selected professionals align with your requirements and expectations."),
            ("Onboarding and Integration Support", "To ensure a smooth transition for the augmented staff into your organisation's environment, we offer onboarding and integration support. This includes facilitating the necessary paperwork, introducing new team members to your workflows and processes, and providing ongoing support during the initial stages of engagement."),
            ("Project Management and Oversight", "We go beyond talent acquisition and offer project management and oversight services. We assist in coordinating project timelines, ensuring that deliverables are met, and take regular feedback to help manage the augmented team effectively."),
        ],
    },
    {
        "slug": "digital-marketing-services.html",
        "nav": "solutions",
        "name": "Digital Marketing Services",
        "short": "Digital Marketing",
        "tag": "Solutions",
        "h1": "Digital Marketing <em>Services</em>",
        "lead": "Join forces with us and witness a transformation that goes beyond visibility. It's about leaving a mark in the digital landscape.",
        "meta": [("+437%", "Best-in-class inquiry lift"), ("+312%", "Traffic growth delivered"), ("74", "Net Promoter Score")],
        "summary": "SEO, social media management, PPC and more, tailored to boost your brand's visibility, engagement and overall digital success.",
        "intro_h": "Grow your brand with our dynamic digital marketing solutions",
        "intro_p": [
            "We redefine what's possible with expertise spanning SEO, PPC campaigns and social media strategies designed to enhance your online presence.",
            "Every channel we run reports into the same commercial goal, so growth in traffic shows up as growth in revenue rather than as a vanity chart.",
        ],
        "principles": [
            ("Beyond Visibility: Crafting Winning Strategies",
             "Dive into the extraordinary with Bodhi Tech, where digital marketing transcends the ordinary and every campaign starts from a position rather than a template."),
            ("Maximising ROI, Minimising Uncertainty",
             "Say goodbye to the guesswork. Bodhi Tech's digital strategies are finely tuned for one goal: maximising your return on investment."),
        ],
        "approach_h": "Our Approach",
        "approach_sub": "Understand the brand, build the strategy from insight, execute with clever tactics, then optimise without pause.",
        "steps": [
            ("Understanding Your Brand and Market", "We run a deep analysis of your brand essence, core values, target audience, and unique propositions before proposing a single campaign."),
            ("Strategy from Insights", "We create customised roadmaps aligned with your business goals through proven strategic frameworks, so every channel has a job to do."),
            ("Execution with Clever Tactics", "We implement optimised SEO and social campaigns combining creativity with precision, built to earn attention rather than buy it indiscriminately."),
            ("Continuous Optimisation", "Real-time monitoring, analysis, and adaptation of your digital presence, so the strategy keeps pace with the market rather than the reporting cycle."),
        ],
        "offer_h": "Digital marketing offerings",
        "offer_sub": "Let's grow your brand",
        "offerings": [
            ("Search Engine Optimization (SEO)", "Boost your online visibility and climb the search engine ranks with our SEO expertise. From keyword optimisation to technical enhancements, we ensure your brand is discovered by the right audience."),
            ("Paid Social Media Management", "Precision-targeted ad campaigns reaching your desired audiences through strategic placements and compelling creative, optimising budget efficiency at every stage of the funnel."),
            ("Organic Social Media Management", "Curating engaging content that fosters genuine audience connections, builds communities, and establishes a trusted brand presence."),
            ("Google Ads (PPC Management)", "Strategic ad placement ensuring maximum ROI through precision-crafted campaigns that deliver increased conversions, not just clicks."),
            ("Lead Generation", "Combining inbound and outbound strategies through captivating content and personalised outreach, transforming prospects into loyal clients."),
            ("Email Marketing", "Newsletters, automated campaigns, and targeted promotions delivering personalised content through strategically timed initiatives that nurture leads."),
        ],
    },
    {
        "slug": "mobile-app-development.html",
        "nav": "solutions",
        "name": "Mobile App and Platform Development",
        "short": "Mobile App Development",
        "tag": "Solutions",
        "h1": "Mobile App and <em>Platform Development</em>",
        "lead": "From crafting intuitive designs across platforms to building robust applications that meet the highest standards of quality and user experience.",
        "meta": [("98%", "Navigation accuracy shipped"), ("&lt;6 mo", "Typical MVP timeline"), ("74", "Net Promoter Score")],
        "summary": "Custom digital solutions that work exactly according to your business needs.",
        "intro_h": "Unlock the full potential of mobile technology with our end-to-end services",
        "intro_p": [
            "We deliver user-focused mobile applications addressing specific business needs while adhering to industry standards. Our services span the complete development lifecycle, from strategic planning through deployment and ongoing maintenance.",
            "We construct scalable, secure applications for iOS, Android and cross-platform environments, ensuring applications remain current with evolving market demands and technological progress.",
        ],
        "principles": [
            ("Built to Scale, Built to Last",
             "Applications are architected for growth from day one, with the security protocols and data practices your users and regulators expect."),
            ("One Team, Strategy to Store",
             "Strategy, design, engineering, QA and post-launch marketing sit under one roof, so nothing gets lost in the handover between vendors."),
        ],
        "approach_h": "Our Approach",
        "approach_sub": "The complete development lifecycle, from the blueprint through to the analytics that shape version two.",
        "steps": [
            ("Strategic Planning", "Crafting a blueprint by understanding what folks want, who they are, and where the trends are heading to make an app strategy that's spot-on."),
            ("UX/UI", "Weaving together designs that feel like second nature, making screens easy on the eyes, and experiences smoother than a well-oiled slide."),
            ("Development", "Building apps that stand strong, expand effortlessly, and guard user info like a fortress on iOS, Android, or any platform in sight."),
            ("Testing and Quality Assurance", "Putting apps through rigorous exams to fix any hiccups, ensuring they work like a charm on every gadget or scenario."),
            ("Integration and Deployment", "Merging the app with backend systems seamlessly and sending it off to app stores or business platforms hassle-free."),
            ("Maintenance and Support", "Playing guardian angel, giving apps updates and care, so they stay sharp, safe, and in tune with the ever-changing tech world."),
            ("Analytics and Optimization", "Playing detective with user data, fine-tuning apps based on how folks use them, making every tap count."),
        ],
        "offer_h": "Mobile app and platform development offerings",
        "offer_sub": "Comprehensive app development and optimisation services",
        "offerings": [
            ("Native and Cross-Platform Development", "Creating applications tailored for iOS or Android individually, or building cross-platform apps functioning across multiple operating systems using Flutter or React Native."),
            ("Backend Development", "Developing server-side architecture, databases, and APIs supporting mobile app functionality while ensuring seamless front-end and back-end communication."),
            ("UX/UI Expertise", "Blending creativity with functionality to design visually compelling and intuitively designed interfaces that engage audiences effectively."),
            ("Security and Compliance", "Implementing robust security protocols and ensuring regulatory compliance to safeguard user data and maintain trust."),
            ("Post-launch Services", "Providing post-launch monitoring, performance analysis, and scalability solutions alongside digital marketing services including PPC, paid and organic social campaigns, and strategic SEO."),
        ],
    },
]

# the industries we work in. same idea as SOLUTIONS above: one entry becomes
# one page plus a card on the industries index.

INDUSTRIES = [
    {
        "slug": "startups-and-smes.html",
        "name": "Startups and SMEs",
        "h1": "Startups and <em>SMEs</em>",
        "lead": "At Bodhi Tech our tech solutions are designed to empower and propel you into a brighter, purposeful future.",
        "summary": "We guide start-ups and SMEs from uncertainty to success, providing clear starting points and transforming conceptual ideas into tangible realities.",
        "meta": [("100+", "Projects completed"), ("5+", "Years of operation"), ("74", "Net Promoter Score")],
        "offer_h": "Our offerings for startups and SMEs",
        "offer_sub": "Support and guidance to help you thrive in today's competitive business landscape.",
        "offerings": [
            ("Business Consultation", "Our expert advisors provide personalised guidance and strategic insights to startups and SMEs, helping you navigate challenges, seize opportunities, and achieve business goals efficiently. Support covers market analysis through to strategic planning, tailored to your unique needs and objectives."),
            ("Minimum Viable Product Development", "We help startups and SMEs bring ideas to life through lean, strategic MVP development, whether mobile apps or websites. We focus on building functional, user-centric products capturing your core vision and ready for market testing, so you can validate ideas, gather user feedback, and scale with confidence."),
            ("Digital Marketing Solutions", "Digital marketing designed to help startups and SMEs cut through the noise, connect with target markets, and grow purposefully. Services include SEO strategies, data-driven PPC campaigns, and engaging social media content to help your brand stand out."),
            ("Staff Augmentation", "We connect startups and SMEs with skilled professionals in software development, digital marketing, design, sales and more, selected to fit your budget and culture. The focus extends beyond skills to finding talent that aligns with your vision and integrates seamlessly into your existing team."),
        ],
        "cs_h": "We understand your challenges",
        "cs_sub": "The pressures that come with early-stage growth, and the practical ways we work around them.",
        "challenges": [
            ("Limited Resources",
             "Startups and SMEs operate with real constraints across finances, manpower and technology, which limits the ability to scale, innovate and grow efficiently.",
             "Implementing careful budgeting and prioritising key investments helps startups and SMEs optimise the resources they do have, and put them behind the work that moves revenue."),
            ("Market Competition",
             "Crowded categories make it hard to be noticed, particularly when larger competitors can outspend you on every channel.",
             "Identifying unique selling points and targeting niche markets helps businesses carve a competitive edge despite saturation."),
            ("Building Brand Awareness",
             "Without an established name, earning the trust needed for a first purchase is slow and expensive.",
             "Developing consistent branding, storytelling, and digital marketing strategies establishes a memorable identity and builds customer trust."),
            ("Adapting to Changing Market Trends",
             "Market conditions and customer expectations shift faster than most small teams can re-plan against.",
             "Leveraging customer feedback and digital tools enables quick responses to market changes while remaining competitive."),
        ],
    },
    {
        "slug": "promotional-products.html",
        "name": "Promotional Products",
        "h1": "Promotional <em>Products</em>",
        "lead": "Your trusted industry insider and expert in promotional products. We've been instrumental in elevating the digital presence of numerous promotional products and merchandising companies, making us the go-to partner for transformative marketing solutions from custom websites to SEO and PPC.",
        "summary": "We understand the intricate nuances of the promotional product sector and the website needs that come with it.",
        "meta": [("+437%", "Online inquiries, Chilli"), ("+312%", "Website traffic, Chilli"), ("+203%", "Organic traffic, Chilli")],
        "offer_h": "Our offerings for merchandising and promotional product companies",
        "offer_sub": "We offer a comprehensive suite of services tailored specifically to meet the unique needs of businesses in the merchandising and promotional product industry.",
        "offerings": [
            ("Web Development", "Our expertise in the promotional products and merchandising industry means we know exactly what your website needs. We specialise in building websites that not only showcase your products and capabilities professionally but get customers through the door and streamline their merch selection and buying experience. Our team has built tailored e-commerce WordPress websites integrated with WooCommerce specifically designed for this sector."),
            ("UI/UX and Graphic Designing", "Our empathetic approach ensures that every design decision is rooted in addressing user needs and behaviour. We map the customer journey and identify where your customers may be dropping off to improve their experience on your website. Our strategic approach guarantees designs that captivate users, convert potential clients, and leave a lasting impression."),
            ("Strategic Marketing Consultation", "Our expert advisors offer personalised guidance and strategic insights for your merchandising company, helping you navigate challenges, seize opportunities, and achieve your business goals efficiently. From planning digital marketing tactics to a full go-to-market strategy, we provide comprehensive marketing consultation for promotional products companies like yours."),
            ("Digital Marketing Solutions", "With a team of digital marketing experts, we offer full stack digital marketing services that match the needs of your company. From optimising SEO to driving impactful PPC campaigns and creating captivating social media strategies, we have the expertise to elevate your online presence and grow your portfolio and client base."),
        ],
        "cs_h": "We understand your challenges",
        "cs_sub": "Four problems we see across the promotional products industry, and what actually solves them.",
        "challenges": [
            ("Educating Customers on Product Value",
             "Many customers view promotional products as low-cost giveaways, overlooking the strategic value they offer for brand recognition and customer engagement.",
             "A website with educational content such as blog posts, case studies and infographics can highlight how promotional products drive marketing ROI. By showcasing creative uses and measurable outcomes, companies can shift perceptions and emphasise their products' value."),
            ("Customisation Complexity",
             "Customers often struggle to understand customisation options like design placement, colour choices or logo sizing, leading to delays in the sales process or dissatisfaction with final products.",
             "An interactive website with a product customisation tool enables customers to visualise their designs in real time. This reduces back-and-forth communication, speeds up decision-making, and ensures customers are satisfied with their orders."),
            ("High Customer Expectations for Speed and Quality",
             "In an industry where quick turnarounds and high-quality products are expected, companies can lose business if they don't meet customer demands efficiently.",
             "An optimised website integrated with order tracking, automated updates and clear timelines can help manage customer expectations. Coupling this with high-quality product imagery and detailed descriptions ensures clarity and trust."),
            ("Keeping Up with Evolving Trends",
             "The promotional products industry constantly evolves with trends in branding, eco-friendliness and technology. Companies that fail to adapt risk falling behind competitors offering more innovative solutions.",
             "A modern website regularly updated with trending product categories, sustainable options and innovative ideas keeps the business relevant. Paired with digital campaigns highlighting these offerings, companies can position themselves as forward-thinking leaders in the market."),
        ],
        "featured_case": "case-chilli-promotions.html",
    },
    {
        "slug": "construction.html",
        "name": "Construction",
        "h1": "<em>Construction</em>",
        "lead": "With 5+ years of construction industry experience, Bodhi Tech offers solutions that combine expertise with cutting-edge technical skills to meet your business needs.",
        "summary": "We understand the intricate heritage and nuances of the construction sector, and we are dedicated to constructing success that withstands the test of time.",
        "meta": [("5+", "Years in construction"), ("2", "Ready-to-launch templates"), ("74", "Net Promoter Score")],
        "offer_h": "Our offerings for construction companies",
        "offer_sub": "We offer a comprehensive suite of services tailored specifically to meet the unique needs of businesses in the construction industry.",
        "offerings": [
            ("Strategic Marketing Consultation", "Our expert advisors offer personalised guidance and strategic insights for your construction company, helping you navigate challenges, seize opportunities and achieve your business goals efficiently. From market analysis to strategic planning, and from digital marketing tactics to a full go-to-market strategy, we provide comprehensive marketing consultation for construction companies."),
            ("Digital Marketing Solutions", "With a team of digital marketing experts, we offer full stack digital marketing services that match the needs of your construction company. From optimising SEO to driving impactful PPC campaigns and creating captivating social media strategies, we have the expertise to elevate your online presence and grow your portfolio."),
            ("Web Development", "Our expertise in the construction industry has led to us knowing exactly what your business website needs. We build websites that not only look professional but also drive conversions, and our team has combined that industry experience with web development expertise to create WordPress templates for the construction industry. From custom websites to quick, easy-to-implement templates, we can deliver and launch a world-class website for your construction company within weeks."),
            ("UI/UX and Graphic Designing", "Our empathetic approach ensures that every design decision is rooted in addressing user needs, fostering engagement and enhancing overall satisfaction. While aesthetics are crucial, we go further: our strategic approach guarantees designs that captivate, convert and leave a lasting impression on your audience."),
        ],
        "templates": [
            ("Classic Construction Website", "A proven, trust-first layout that leads with completed projects, certifications and testimonials. Ready to brand and launch."),
            ("Modern Construction Website", "A bolder layout built around large project photography, capability statements and a prominent enquiry path."),
        ],
        "cs_h": "We understand your challenges",
        "cs_sub": "At Bodhi Tech we understand your challenges and address the root causes with targeted solutions to drive lasting success.",
        "challenges": [
            ("Building Trust and Credibility",
             "Construction projects require large financial commitments, and potential clients may hesitate to work with companies that don't have an established, credible online presence.",
             "A professional website showcasing past projects, client testimonials, certifications and industry expertise builds trust and reassures potential clients of your capabilities and reliability."),
            ("Market Competition",
             "With a high level of competition in the market, many construction companies offer similar services, making it hard to differentiate and compete for attention.",
             "Strategic branding, combined with targeted marketing campaigns and an impressive online portfolio, helps construction companies stand out from competitors."),
            ("Limited Resources",
             "Smaller construction companies often face constraints in terms of finances, manpower and technology, hindering their ability to scale, innovate and grow efficiently.",
             "Digital marketing and a website provide cost-effective ways to reach a wider audience without needing a large sales team. Automating certain tasks through the website can also help optimise limited resources."),
            ("Client Acquisition",
             "Construction companies often struggle with fluctuating demand and a lack of consistent project pipelines.",
             "A well-optimised website with strong SEO and targeted digital marketing, such as Google Ads, social media and email campaigns, can drive a steady stream of leads and enquiries, ensuring a more consistent flow of potential projects."),
        ],
    },
]

# blog posts. this is just the title, date and summary for the cards - the
# actual article text lives in articles.py.

BLOG_POSTS = [
    {
        "slug": "blog-web-development-trends-2025.html",
        "title": "10 web development trends to watch in 2025",
        "excerpt": "AI-assisted builds, progressive web apps, voice search and serverless architecture are reshaping what a business website has to do. Here is what we are watching, and what it means for SMEs.",
        "date": "28 March 2025",
        "read": "6 min read",
        "category": "Web Development",
        "image": "https://bodhitech.com.au/wp-content/uploads/2024/08/New-Project.png",
    },
    {
        "slug": "blog-promotional-product-ecommerce.html",
        "title": "Boost your promotional product business: high-performing e-commerce website ideas",
        "excerpt": "Promotional product buyers want to see their logo on the product before they commit. These are the e-commerce features that shorten that decision, and the ones that quietly lose the sale.",
        "date": "16 August 2024",
        "read": "5 min read",
        "category": "Promotional Products",
        "image": "https://bodhitech.com.au/wp-content/uploads/2024/11/Chili-New.webp",
    },
    {
        "slug": "blog-optimise-website-on-a-budget.html",
        "title": "How to optimise your business website on a budget",
        "excerpt": "You do not need a rebuild to get more from your website. A practical, prioritised list of the improvements that cost the least and return the most for small and growing businesses.",
        "date": "1 May 2025",
        "read": "9 min read",
        "category": "Strategy",
        "image": "https://bodhitech.com.au/wp-content/uploads/2024/02/Montdami.webp",
    },
]


# hero imagery.
# currently a mix of Unsplash and bodhitech.com.au, all hot-linked. worth
# pulling local before launch so the site does not depend on either.

HERO_IMAGES = {
    "web-development.html": ("https://images.unsplash.com/photo-1551434678-e076c223a692?q=80&w=760&auto=format&fit=crop", "Engineers building a web platform"),
    "marketing-strategy.html": ("https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=760&auto=format&fit=crop", "Marketing performance dashboard"),
    "ux-ui-graphic-design.html": ("https://images.unsplash.com/photo-1531482615713-2afd69097998?q=80&w=760&auto=format&fit=crop", "Designers working through an interface"),
    "staff-augmentation.html": ("https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=760&auto=format&fit=crop", "An augmented team working together"),
    "digital-marketing-services.html": ("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?q=80&w=760&auto=format&fit=crop", "Digital marketing team at work"),
    "mobile-app-development.html": ("https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=760&auto=format&fit=crop", "Mobile application code"),
    "startups-and-smes.html": ("https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=1600&auto=format&fit=crop", "Startup team planning"),
    "construction.html": ("https://images.unsplash.com/photo-1541888946425-d81bb19240f5?q=80&w=1600&auto=format&fit=crop", "Construction site"),
    "promotional-products.html": ("https://images.unsplash.com/photo-1600880292203-757bb62b4baf?q=80&w=1600&auto=format&fit=crop", "Branded promotional merchandise"),
    "about-us.html": ("https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=760&auto=format&fit=crop", "The Bodhi Tech team"),
}
