[0.00 → 4.00] If you go to GitHub and you browse any kind of random repository, and you press
[4.00 → 9.30] the period key on your keyboard, like the dot, it all just of a sudden launches
[9.30 → 14.46] a full-blown code editor. Is that a progressive web app or is that a web app or is that an app or
[14.46 → 18.52] whatever is it? In many cases, it's not distinguishable from VS Code as a native
[18.52 → 24.38] application that you download. So this kind of experiences where we just become used to using
[24.38 → 29.24] apps in the browser without really realizing that we're using a progressive web app or a web app or
[29.24 → 34.64] an app. So what I'm getting to is maybe progressive web apps have just succeeded because we built them
[34.64 → 43.58] and don't really think about it anymore. This episode is brought to you by our friends at
[43.58 → 47.32] Square, developing the platform that sellers trust. Here's what you could do with Square. You could
[47.32 → 52.74] bridge more experiences. You could build online, mobile, and in-person commerce experiences that
[52.74 → 57.56] connect more customers and sellers. You can build custom booking solutions. Furthermore, you can create and track
[57.56 → 62.56] orders. You can accept payments. Furthermore, you can manage and curate inventory. Furthermore, you can organize customers.
[62.66 → 68.30] You can manage employees. You can extend Square gift cards to your app. You can use Afterpay. And
[68.30 → 74.64] all this is powered by the world-class Square APIs and SDKs that enable you to build full-featured
[74.64 → 79.80] business apps for yourself or millions of Square sellers. So much is available as a Square
[79.80 → 86.28] solutions partner. Learn more and get started at changelog.com slash Square. Again, changelog.com slash Square.
[86.28 → 106.54] This is JS Party, your weekly celebration of JavaScript and the web. Changelog has joined the Fediverse.
[107.34 → 114.02] Find our Mastodon instance at changelog. Social and connect with us at js party at changelog.social.
[114.02 → 119.86] Thanks to our partners at Vastly for delivering our pods superfast all around the world. Check
[119.86 → 126.16] them out at fastly.com. And to our friends at fly.io. Deploy your app servers close to your users.
[126.56 → 132.82] No ops required. Learn more at fly.io. Okay, it's party time, you all.
[132.82 → 148.86] Hello, JS Party listeners. We're back this week talking all about the web yet again. Surprise,
[149.16 → 154.46] I know. We've got a really special guest with us today. Before we introduce our guest on the panel
[154.46 → 160.74] with me today is my, I would say almost regular co-pilot these days, Nick. Oh, well, I just don't
[160.74 → 165.72] anyway, I don't feel like I always spoil introductions. So Nick, welcome. Welcome on the
[165.72 → 165.98] show.
[166.64 → 168.34] Ahoy, hoy. Good to see you, Mel.
[168.76 → 174.52] Good to see you. This is the first show that I'm like back in my own home. I've only been home for
[174.52 → 180.92] like 12 hours. And we've had like, I've already had like AV issues and like internet issues and all
[180.92 → 184.74] the things, all the things that you can imagine, all the tech issues have like concentrated into
[184.74 → 191.26] this show. But anyway, regardless, show started now, and we're super excited about our amazing guest.
[191.42 → 191.76] Oh, yeah.
[192.02 → 199.62] Yeah. Mega amazing. He's so amazing. He's got a PhD. Tom Steiner, senior developer relations engineer
[199.62 → 203.32] who works on the Chrome team at Google. Welcome, Tom.
[203.90 → 205.00] Thank you very much. Hello.
[205.40 → 209.54] Hello. Tom, why don't you tell us a little bit about yourself for folks who might not be familiar?
[209.54 → 215.46] Well, my name is Tom. I work on the Chrome team. But what I like most about my job is that I work
[215.46 → 220.04] on the Chrome team. But actually, I'm not that much advocating for Chrome. I do as well, of course,
[220.16 → 225.64] but I'm very much also advocating for the web. So the web is the product that I advocate for and
[225.64 → 231.74] specifically, more specifically, Project Fugue these days, which is all about making new use cases
[231.74 → 238.00] possible on the web by adding new APIs to browsers and browsers by definition is plural, not just one
[238.00 → 238.44] browser.
[238.88 → 243.76] I mean, that sounds like an amazing job. I have to say, you know, for many years, you know,
[243.76 → 250.36] I've been following a Chrome team for almost, you know, a decade now. And it's been amazing to see
[250.36 → 260.84] kind of, I think, that team specifically set the standard for how to do developer engagement and how to do
[260.84 → 266.90] developer advocacy and how to do developer education, like, well, I think for me, like, I always think of
[266.90 → 272.20] the Chrome Dev developer relations team as a whole, right? And there are different roles within the
[272.20 → 276.34] developer relations team. There are folks that work on engineering projects like Tom, there are folks that
[276.34 → 281.06] are really more focused on advocacy. I've always thought about that team as best in class. I do have
[281.06 → 285.06] to admit, though, just, you know, to be fair, Tom, if you're, I don't know how often you listen to this show,
[285.06 → 291.26] but I'm not sure if we have a ton of Chrome users anymore on the panel, right? I use a Chromium
[291.26 → 298.56] flavour as my primary browser these days, Brave. I also use Firefox. But I think regardless of our
[298.56 → 305.34] usage of Chrome, I think I'm a fan of the Chrome developer relations team. And I'm super excited to
[305.34 → 308.82] have you on the show today. So thank you and welcome, Tom.
[309.44 → 310.44] Yeah, thanks for having me.
[310.44 → 316.26] Yeah. So Tom, we've invited you here today to tell us all about Project Fugue. We're super,
[316.42 → 322.00] super excited to kind of finally have this topic on the show. It's been on my to-do list for a very
[322.00 → 328.30] long time. One of my perfect, very good friends, and I would say he's like my friend tour. I don't
[328.30 → 332.98] know if you know what a friend tour is, but he's like a friend and a mentor to me. Alex Russell was
[332.98 → 338.14] kind of the TL, the tech lead on this project and kind of helped really galvanize it. And he's at
[338.14 → 341.64] Microsoft now. But he was on my list. I was like, all right, I got to get Alex to come on the show
[341.64 → 346.20] to talk about Fugue. I got to get Alex, you know, and we just like never like made that happen. And
[346.20 → 351.62] I'm so glad to finally be talking about this. So can you tell our listeners, what is Project Fugue?
[352.28 → 357.12] And why are you working on it? And yeah, I mean, there's such an important project to the ecosystem,
[357.12 → 360.10] and there's so much to unpack. So educate us, please, Tom.
[360.42 → 363.66] Yeah, so let me start. You should definitely get Alex on the show.
[363.74 → 364.14] Oh, for sure.
[364.14 → 367.50] He's still around. He's still at Microsoft. He still does web stuff, obviously. So
[367.50 → 373.70] very much do make sure you get him on the show. And like, I will tell you my view of Project Fugue,
[373.82 → 378.72] but obviously Alex has been around for way more time than I have been. So he will have a different
[378.72 → 385.62] view. So also get his for sure. But like, what I will tell you is, when I started working on the
[385.62 → 390.34] Chrome team, I was looking for my niche. And on the Chrome team back then, everyone was doing
[390.34 → 396.20] amazing things like CSS Houdini and like, all the hot topics were being dealt with. So I looked at
[396.20 → 401.68] like, what are people doing on the web? I noticed this tendency where more and more people were
[401.68 → 407.44] building amazing applications on the web. And in many cases, these applications were lacking
[407.44 → 415.42] certain APIs. So there were gaps in the platform that the platform just didn't cover. And Fugue was
[415.42 → 421.58] this effort that people around Alex, but there's a lot more people around behind this have started.
[422.36 → 429.32] And they started by filling all those gaps. So initially, there was Chrome OS as an app platform.
[429.68 → 437.36] And they had a backlog of all these APIs that they ported over of sorts to be on the open web. So not
[437.36 → 443.84] like proprietary Chrome OS application platform, API interfaces, whatever, but like proper,
[443.84 → 450.54] on a standard track developed in the open APIs that people could agree on universally where browsers
[450.54 → 456.92] would say, hey, this is a good idea. Let's do it that way. But first, but also could say, yeah,
[456.94 → 462.20] we're in general, okay, with this API, but we don't like the shape. So let's refine it a little bit.
[462.40 → 467.28] Or and this also did happen where browsers would be like, oh, that's a terrible idea. We don't want to
[467.28 → 473.24] have this on the web platform. So with all these three different options of how APIs could play out,
[473.24 → 479.90] Fugue was or is still this effort of making stuff and use cases happen on the web. And in general,
[480.20 → 485.80] what we do see is there's developer enthusiasm. There's also skepticism when it comes to like,
[485.92 → 491.16] can I really use this on all browsers? What is the right strategy for building applications today?
[491.86 → 495.10] And yeah, I guess we can discuss some of these questions during the show.
[495.54 → 500.72] Yeah, no, oh my god, thanks for that great summary. I mean, there's so much to unpack here. And we're
[500.72 → 506.94] going to get into kind of some of the specifics on specific APIs that Fugue is enabling within a
[506.94 → 513.00] browser that's already near you or coming to you. I don't know. But I think what's more important is
[513.00 → 519.92] to kind of discuss the Galvin, like why, like, why was this project created? And Alex and I have had
[519.92 → 523.56] many chats, and I'm certainly going to have him back on this show. But it's going to probably be a
[523.56 → 527.70] wider discussion about like, how can we save the web? That's like a whole, that's like,
[527.70 → 531.06] like a three-hour conversation, we're going to need some alcohol for that, you know, it'll be
[531.06 → 536.38] probably a special edition show. But focusing this on Fugue, can you tell us a little bit about
[536.38 → 540.52] why this project was created? Can you tell our listeners about why? Like, what were we actually
[540.52 → 541.56] trying to do here?
[542.36 → 549.36] So talking to a lot of partners, so customers, companies, Google works with, we always got sort
[549.36 → 554.36] of the same message, which was, we need apps, we need different apps for different platforms.
[554.36 → 559.72] And we essentially need to build the same app, two times, three times, four times, depending
[559.72 → 565.02] on what platforms they needed to cover or thought they needed to cover. And most companies don't
[565.02 → 569.64] really like doing that. So there are a couple of companies who actually have the resources and
[569.64 → 575.42] actually do like building apps for platforms. But most companies, sort of they do it because
[575.42 → 581.30] they think they have to. And they're trying to avoid this as much as possible. So they try to
[581.30 → 586.36] build cross platforms. So using in the old days, something like Cordova, or they would
[586.36 → 592.64] both go like React Native as a route. Flutter these days is becoming very popular for this
[592.64 → 598.06] promise of writing once and then running everywhere. But yeah, in the end, people also always need
[598.06 → 603.14] a website. So it can be a web application, it can be just a gateway into your application
[603.14 → 610.12] that you then install for Android or Windows or macOS or whatever. But essentially, yeah, this
[610.12 → 616.20] desire of why not just have one app that we can use universally. And there's a couple of
[616.20 → 622.50] companies who have started doing that. And most companies are not there yet. But yeah, we see a
[622.50 → 627.22] lot of companies interested in at least reducing the number of platforms that they build upon.
[627.84 → 633.72] And I would also say COVID has played a huge role in it because COVID made desktop important again.
[633.72 → 639.70] So we've been like 2015 was like the year of mobile and everyone was looking at mobile web,
[639.80 → 645.18] and we still do. But COVID has sort of helped us roll back a little bit and look at, hey,
[645.36 → 650.64] desktop is a very important platform. And there are a lot of applications that people build for the web,
[650.80 → 658.72] and they run in the browser and people on their big 20 inch or whatever, 27-inch laptop screens or
[658.72 → 665.12] laptop screens. 27-inch laptop screens. I'm like, we need to meet these people. We need to get them
[665.12 → 670.48] on the show. We got to talk about backpacks. Furthermore, we have a lot to talk about with them. But
[670.48 → 677.78] absolutely. So anyway, big screens on whatever device. They run web apps in many cases, like
[677.78 → 683.86] looking at my computer right now, there's like a handful of apps. And most of them are really just
[683.86 → 690.62] web based. Everything else is macOS Finder and like some emulation software, but that's about it. So
[690.62 → 697.24] everything else is just on the web. And they are not websites, they're web applications. So
[697.24 → 702.32] I can create stuff here. We're creating stuff here right now. So this is a web based podcasting
[702.32 → 709.42] software. So there are a lot of web applications that we just use. And we live in the web. And this is
[709.42 → 716.02] waif was and is being built. Yeah, absolutely. It's really cool. So like this idea of like
[716.02 → 721.20] reducing your stack, right? And JavaScript being a universal stack. I mean, we've kind of been
[721.20 → 727.50] trying to do this for, I would say ever since Node became a thing, right? I mean, we made that shift
[727.50 → 734.86] with our server side stack. So Teams kind of, okay, using one language in the front end and quote unquote
[734.86 → 739.54] backend, right? I'd say for me, like I say quote unquote backend, because for me, like, what is
[739.54 → 745.44] backend even these days? Really? It's like, is it really a backend? Every backend has a front end and
[745.44 → 748.84] a backend. Like, I don't know, at least the back end that I've worked on. So unless you're working
[748.84 → 753.52] on the data layer, like, I don't even know really, is it the backend? I have no idea, you know?
[754.06 → 760.00] So we're teams are trying to kind of say, okay, we can't write iOS apps, Android apps, and JavaScript
[760.00 → 764.16] apps. We can't staff them. We can't maintain them. It's too much. And it's, I agree. It's a
[764.16 → 769.38] huge permutation to manage, especially across Android. Creating a quality Android application
[769.38 → 774.38] is like an act of God in some cases, really, right? Because there are tons of permutations
[774.38 → 780.04] that you need to support. And so can you tell us a little bit about kind of this play for the web,
[780.12 → 785.00] right? We've got React Native that's kind of been in this space, like you mentioned Flutter.
[785.28 → 789.62] It sounds like we're really trying to save the web from being engulfed by native applications.
[789.62 → 795.46] And for me, that's kind of how I've always read this. This is how I've smelled this project,
[795.62 → 797.44] right? Can you speak to that a little bit, Tom?
[798.50 → 806.24] So I think on mobile specifically, people still have the tendency to look for apps on the app stores.
[806.24 → 813.18] So on the Play Store, on the App Store, and like even on desktop, Apple tries to very hard make
[813.18 → 821.12] people look for apps on the App Store first, Windows as the Microsoft Store. So I think stores and like
[821.12 → 828.08] the way as a distribution mechanism stores work is still very much important. And looking at what we
[828.08 → 833.58] can do about that. So stores have advantages, like you can get your applications there, you can get
[833.58 → 840.32] reviews there, people can get a feeling, is this application addressing the needs I have for it?
[840.32 → 844.86] Like if you have an image editing application, what do others say about this application? Can it deal
[844.86 → 850.50] with whatever JPEGs? Does it struggle with large files and so on? So these kinds of things, people
[850.50 → 858.16] will leave in reviews. So there are a lot of advantages of having apps on the App Stores. And one trend that
[858.16 → 863.44] we've seen is people want to get their progressive web apps onto App Stores. And you may have heard of
[863.44 → 869.24] PWA Builder, that is a community project run by Microsoft folks that helps with that.
[869.24 → 876.46] So native apps and progressive web apps on App Stores can coexist, and they do coexist pretty well,
[876.46 → 881.92] I would say. On the other hand, we still see a lot of like lower quality apps that are essentially
[881.92 → 888.78] very much still like web applications, websites, sometimes in the worst case, that are poorly wrapped.
[888.90 → 893.82] And people leave reviews about those and say, ah, this is really just a website. It's not a great app.
[893.82 → 899.78] I think if you go this route and say, I want to get my application alongside native applications
[899.78 → 905.32] listed in a store, you need to make the effort of really making your app blend in and make it
[905.32 → 911.82] feel like an app and not like a wrapped website. So yeah, this is my sort of rambling answer to your
[911.82 → 912.40] open question.
[912.40 → 917.88] Yeah, no, no, that was a perfect point too. Like the app store is, it's got its hooks,
[917.98 → 923.36] right? It's a well-paved cow path for users, right? It's the thing that they know is the
[923.36 → 927.34] thing that they're familiar with. And for me, I have this burning question of like, what happened
[927.34 → 932.26] to PWAs, you know, in the sense that like, I thought PWAs were supposed to save us from this
[932.26 → 936.76] hellhole of like native applications. And I say that because I'm quite frankly, I'm very team pro
[936.76 → 943.08] open web. You know, native apps are maybe slightly better for user experience, right? But you know,
[943.08 → 947.64] not really great for the health of the web, specifically like user privacy as well, like
[947.64 → 951.74] user privacy, user data, there are all kinds of stuff that's like not so great, right? So browsers being
[951.74 → 956.82] this sandbox environment, and more kind of trusted environment, always kind of safer place to
[956.82 → 957.14] browse.
[957.94 → 962.70] With that, like, that's something I was thinking about too. Like, it's great adding these, these APIs and
[962.70 → 968.58] capabilities to the browser. But like, kind of just going towards what you said, Abel, the there's
[968.58 → 975.02] always like a the browser is a trusted place, but it's also a place I heavily distrust. And it's very,
[975.56 → 982.06] it's very obvious in the amount of like, content blockers, ad blockers, things that I add to my browser
[982.06 → 988.36] to make it more of a safe place, you know, get rid of this cookie, cookie banners, things like that. And
[988.36 → 993.74] those things, like, it adds a distrust. And then the first time I try and visit like, you know,
[993.78 → 998.90] something that I would just obviously trust on the web, but it's broken because of my,
[998.90 → 1005.66] my overabundance of, of trying to block everything, I immediately start like distrusting the platform
[1005.66 → 1009.92] more. I think like, I don't know where I'm going with that, just to call that out is like a
[1009.92 → 1015.80] a problem. It's like, it's a trusted place. But because there's so much distrust among the content
[1015.80 → 1021.64] there, it kind of sours everything because I'm overly cautious about the dangerous stuff.
[1022.12 → 1024.62] And it can break my experience for the good stuff.
[1025.14 → 1029.20] Yeah, I can maybe speak to that. So whatever happened to Progressive Web Apps? So first,
[1029.32 → 1035.66] maybe Abel to discuss this point that you brought up. Do you remember Ajax, like all uppercase Ajax?
[1035.66 → 1042.38] And a little bit later, it became first letter uppercase and the rest lowercase. So like more of a
[1042.38 → 1042.98] regular word.
[1043.52 → 1045.54] You mean we're not doing asynchronous JavaScript and XML?
[1045.80 → 1047.64] Here we go.
[1047.64 → 1054.36] What? You hear you are busting dreams and facts, you know, Tom and Nick Nisi. So naughty.
[1054.36 → 1060.30] So yeah, at some point, no one talked about Ajax anymore. It just had become the way we build
[1060.30 → 1068.20] applications, single page applications. And the same goes with HTML5. Do you remember HTML5 and CSS3,
[1068.20 → 1075.30] like all these logos that we put on our conference slides and like nowadays, everyone does HTML5 apps,
[1075.30 → 1080.88] or like, do we do HTML6 apps now? Or like, I don't know. So we just stopped talking about this.
[1081.06 → 1082.86] And I still remember my very long DOCTYPE.
[1082.86 → 1091.42] And a little bit the same is happening with progressive web apps these days. So people build
[1091.42 → 1098.30] progressive web apps of sorts, but I'm like, is it a P progressive web app if it's like not installable,
[1098.30 → 1103.42] or is it just a web app? Or like, what about the just like, do we need the just? Is it a web app? Is it
[1103.42 → 1109.24] just an app? Is it good? If you go to GitHub, and you browse any kind of random repository, and you press
[1109.24 → 1116.82] the period key on your keyboard, like the dot, it all just of a sudden launches a full-blown code editor.
[1117.30 → 1122.50] Is that a progressive web app? Or is that a web app? Or is that an app? Or whatever is it? In many cases,
[1122.50 → 1127.88] it's not distinguishable from VS Code as a native application that you download, and run, but it's an
[1127.88 → 1135.32] electron app, but it's not distinguishable in many cases. So this kind of experiences where we just
[1135.32 → 1140.58] become used to using apps in the browser without really realizing that we're using a progressive
[1140.58 → 1146.32] web app or a web app or an app. So what I'm getting to is like, maybe progressive web apps have just
[1146.32 → 1152.30] succeeded because we built them and don't really think about it anymore. So that's that. Nick, for your
[1152.30 → 1159.08] point about cookie banners and all these horrible things, I guess what we're seeing is people just
[1159.08 → 1164.68] being really careful on the web, because in many cases, all these cookie banners or some of these
[1164.68 → 1170.66] cookie banners wouldn't have to be people just put them up just in case to not get sued. In native
[1170.66 → 1176.42] applications, I think, and I'm not a lawyer, but in many cases, there would have to be some sort of
[1176.42 → 1182.16] GDPR notices as well. But people just don't put them up because it's just so hard to
[1182.16 → 1187.50] inspect what a native app does compared to what a web application does. So a lot of things that
[1187.50 → 1193.44] native applications do and like spy on us and sync periodically with whatever server while we're
[1193.44 → 1197.88] sleeping and this kind of horrible things, they're happening, but we don't really see what's going
[1197.88 → 1202.62] on there. So that's a great point on the web. Yeah. People can inspect and can see what's going on.
[1202.62 → 1211.06] And it's just so easy to get in this unfair comparison between the two platforms. But I'm a web person,
[1211.06 → 1215.26] so I'm very much biased. But at the same time, I'm trying to understand what is going on native
[1215.26 → 1220.96] as well. And they're doing horrible things as well. And web does horrible things. So
[1220.96 → 1224.32] Oh, for sure. The web is not innocent, by all means. I agree.
[1224.60 → 1228.54] Yeah, it's more out of sight for the native ones. But you're absolutely correct.
[1228.54 → 1233.60] It is for sure. Yeah. So we are here to fix both, hopefully. So if you talk to people from the Android
[1233.60 → 1238.88] defray team, they will tell you, look, a lot of Android apps do horrible things. And Android as a
[1238.88 → 1243.26] platform is also getting stricter about what apps can do in the background and so on. So
[1243.26 → 1247.96] there's some development happening there as well. Google has the privacy sandbox for the web,
[1248.08 → 1253.36] but now there's a privacy sandbox for Android as well. So what I'm getting at, this is a general
[1253.36 → 1259.56] movement, like apps in general, becoming more privacy aware, privacy-sensitive information not
[1259.56 → 1263.96] being shared in the background and so on. So there's a lot of development going on there.
[1263.96 → 1270.06] Yeah, no, that's a great answer, Tom, and a very, I'd say scientific and diplomatic answer as well.
[1270.22 → 1276.52] You know, I like your kind of innocent until proven guilty kind of stance for kind of examining these
[1276.52 → 1282.86] types of issues. I'm just kind of like guilty, you know, but yeah, so we have so much to get into
[1282.86 → 1288.66] and so much to unpack. So we'll be right back after these short messages.
[1293.96 → 1306.60] This episode is brought to you by Tercel, the platform that enables front-end teams
[1306.60 → 1311.72] to do their best work. Tercel combines the best developer experience with an obsessive focus
[1311.72 → 1317.34] on end-user performance. And I'm here with founder and CEO of Tercel, Fisher Rank.
[1317.68 → 1322.04] So Fisher, I had you on Founders Talk recently talking about making the web faster and how Tercel
[1322.04 → 1327.62] is built on three pillars, develop, preview, ship, but talk about why it's so important to make the
[1327.62 → 1333.06] web faster. I think first, the web is the most open and exciting platform to build on.
[1333.52 → 1338.60] And listeners are going to be enthusiastic about JavaScript, which is one of our areas of focus.
[1338.72 → 1345.08] We think that by creating amazing tools and open sourcing them, developers will go on to create
[1345.08 → 1349.30] amazing experiences for the end users. And I think that's where the concept of making the web
[1349.30 → 1355.30] faster to build and faster to end users. That's the crucial mission of Tercel. This is what's led
[1355.30 → 1361.36] to us investing all across the board to build this end-to-end platform. It started with the
[1361.36 → 1367.36] framework that you develop with, the workflow of pushing up a change and seeing it instantly and
[1367.36 → 1371.60] being able to share that change with your collaborators, all the way to shipping to the
[1371.60 → 1377.42] Edge network of Tercel that makes your site or application globally fast, globally available.
[1377.42 → 1383.16] So it's this very comprehensive mission of making the web end-to-end faster and more open.
[1383.42 → 1390.98] I love it. Globally fast, globally available on a more open web. Learn more at Vercel.com. Again, Vercel.com.
[1390.98 → 1417.20] All right, Tom, we're back. So exciting to be talking about this topic finally, because for me,
[1417.20 → 1424.56] Fugue feels like the browser's kind of breaking free. It's got legs now, right? This kind of
[1424.56 → 1431.20] traditional idea of the sandboxed browser that can't access file system and can't talk to the
[1431.20 → 1435.42] Bluetooth and, oh, we don't know. And like, you know, connecting with sensors and all these other
[1435.42 → 1438.98] things, you have to go through hoops. And right, like this idea of, you know, your browser being
[1438.98 → 1446.50] limited and consequently JavaScript apps also being limited, right? It's just kind of shattered now
[1446.50 → 1451.68] because Fugue is just like, nope, the web can do that. Nope, the web can do that. Oh, the web can
[1451.68 → 1456.60] also do that, right? So can you tell us about, let's just walk through your, what you think are
[1456.60 → 1460.40] kind of the shining stars of the Fugue project, especially the ones that are gaining a lot of
[1460.40 → 1464.38] traction. So we'd love to start with your first hit, Tom. What's your number one?
[1464.38 → 1470.64] So when it comes to apps, definitely my number one app example is still Photoshop on the web.
[1470.92 → 1474.88] They launched it, they make it, made it happen. What I want to call out about this,
[1474.98 → 1479.06] like in the early days when this really just launched, people were like, oh, wow,
[1479.10 → 1483.62] they brought Photoshop to the web. And then of course, haters were quick to point out like,
[1483.72 → 1488.98] yeah, you open this in Firefox and in Safari, and it doesn't work at all. But, and this is where the
[1488.98 → 1494.82] bot comes in. Adobe from the very start said, look, we're working super hard with Mozilla and with Apple
[1494.82 → 1501.02] to make Photoshop on the web happen on the web and not just on Chrome. They put out the version on
[1501.02 → 1505.90] Chrome first because Chrome was the first to implement the APIs and get them ready. But if you
[1505.90 → 1512.64] went to the, to the Photoshop website on Safari on day one, you were just greeted with like this
[1512.64 → 1516.76] message of, hey, you're not using a supported browser, like the classic Chrome only thing.
[1516.76 → 1521.94] But if you do the same today, you can open files and read-only mode now. And you can see the
[1521.94 → 1527.74] application Chrome is there. So in the sense of the UI is there, it's just read only at the moment.
[1527.74 → 1534.98] But the message that they said, say at top is this is not working yet. And we're working with Apple
[1534.98 → 1541.16] and Mozilla to get these APIs into the browsers. And there's a double negation in this tweet that
[1541.16 → 1546.72] Sean Wiesel sent. So Sean works on Adobe, and he said, there's not a single API
[1546.72 → 1552.80] that we're working on that is not on the standards track. So what I'm saying is every API they need
[1552.80 → 1558.70] in their application is on the standards track. It's just not implemented yet. So I think this is
[1558.70 → 1563.84] very important. If you are a big company like Adobe, of course, you have a lot of say when it comes to
[1563.84 → 1570.80] talking to Apple and talking to Mozilla. But I think the same can be sort of leverage for companies
[1570.80 → 1576.62] of all sizes. And if you're not a big company like Adobe, you can still in some if you're a lot of
[1576.62 → 1581.28] small companies, and you talk to these other vendors, and you say, hey, we have this application
[1581.28 → 1586.32] that's working fine in Chrome, and we don't want to tell our Firefox users to download Chrome, we want
[1586.32 → 1591.28] them to continue using their browser of choice. But we're needing this and this and this API.
[1591.76 → 1598.14] It's not implemented yet, or maybe it's buggy or whatever. So talking to browser vendors and
[1598.14 → 1603.22] bringing forward use cases that you want to cover and making sure that you communicate well,
[1603.46 → 1607.90] why these APIs are needed can be a recipe for success. And we've seen it with Adobe,
[1608.06 → 1613.46] which acknowledgedly, as I said, is a big company name. But so in the sum, a lot of smaller companies
[1613.46 → 1619.70] can add up and yeah, they can get the same pressure on other browser vendors to implement APIs. I'm not
[1619.70 → 1625.00] saying this is a recipe for universal success. So we have very clearly heard, for example, Apple say,
[1625.00 → 1631.36] like, I don't know, web USB is an API that they probably won't support ever. Maybe they will in
[1631.36 → 1636.54] the future. Who knows if like we bring forward the right use cases, maybe there's a change in how
[1636.54 → 1641.68] security on the web is handled. There's a lot of debate also when it comes to APIs on the web,
[1641.96 → 1646.64] what is the right way to ask for permission? Do people understand when you ask for permission? Is
[1646.64 → 1652.18] there a way to communicate really all the ways an API could be abused potentially in a small
[1652.18 → 1658.06] permission prompt? Like what is the right way there? And I think this is also a way for browser
[1658.06 → 1664.80] vendors to just innovate and say, we are Firefox, and we're going a permissions way that is different
[1664.80 → 1669.72] from all other vendors. So for example, very recently Firefox supported or started supporting
[1669.72 → 1676.50] web MIDI. The way they do this now, if I understand the concept correctly, is they sort of build an ad hoc
[1676.50 → 1682.84] extension that they can then block and say, if we see that the API is being abused, and we have an
[1682.84 → 1687.72] escape hatch, and they can just sort of, I think, revoke the ad hoc extension that was created.
[1687.88 → 1693.54] I might be misrepresenting the idea, but like the core idea is they innovate on the way the
[1693.54 → 1698.86] mission prompt is being shown by introducing a different vendor specific way of doing so.
[1698.86 → 1704.80] And yeah, maybe this is the recipe for success and for getting like more obscure and maybe more
[1704.80 → 1708.84] powerful APIs onto the platforms. So yeah.
[1709.34 → 1709.50] Yeah.
[1709.66 → 1714.66] You said you work through standards. I was curious, like, is that like what WG or like what kind of
[1714.66 → 1717.38] standards process do these APIs go through or does it vary?
[1718.06 → 1724.24] We start in the WING, the web incubator community group. But then like once we have incubated,
[1724.24 → 1731.24] of course, the final objective is to move onto the W3C, like the full standards track where we go
[1731.24 → 1737.26] through all the different stages. And I just prepared a couple of APIs, and I'm reading them out now that
[1737.26 → 1743.92] started on the WING, but that are now on the W3C. So there's the web share API, there's web transport,
[1744.30 → 1748.58] there's the file system living standard, there's web codecs, there's clipboard API and events,
[1748.98 → 1753.96] there's the multiscreen window placement API. So these are just a couple of examples of APIs that
[1753.96 → 1758.98] started in the WING and that then migrated over to the W3C.
[1759.54 → 1764.14] Yeah, that's a great question, Nick. Because really, for me, this, you really said a lot there,
[1764.34 → 1768.22] Tom, and I just kind of want to break things down for our listeners. Like there's this idea of
[1768.22 → 1774.72] standards adoption, right? Like we can create a standard, we can agree on how to implement thing
[1774.72 → 1781.16] A, but if thing A doesn't get implemented across all browsers, it kind of is useless to developers,
[1781.16 → 1787.42] right? To some degree. And so Apple has been, and I know you probably can't say this, or maybe you
[1787.42 → 1792.20] can, I don't know, but either way, like I'll say it, I don't work for Google, right? So Apple has been
[1792.20 → 1798.88] a tough player to bring to the table, right? They've really been a hard player to get to adopt a lot of
[1798.88 → 1803.20] the APIs that supported progressive web apps and all those other things. And they finally are there.
[1803.20 → 1810.16] And I think this story that you're telling of Adobe successfully launching Photoshop that works
[1810.16 → 1814.90] really almost like a progressive web app, right? Because it's like, it works more fully and richly
[1814.90 → 1820.66] on Chrome and or browsers that have adopted the APIs that they support. But this idea of like,
[1821.12 → 1826.24] actually having a huge vendor and a huge player like Adobe say, hey, we've implemented this and
[1826.24 → 1830.98] we're going to just tell our users, we're working with Apple to get this working in Safari.
[1830.98 → 1836.42] It really flips the script. I love this, like, let's be transparent and let's just be honest and
[1836.42 → 1840.30] let's implement stuff and let's tell users like, it's not that this doesn't work. It's just that,
[1840.38 → 1844.20] hey, this hasn't been implemented in Safari yet. If I was a business where my name was on a banner
[1844.20 → 1849.84] for a very popular website saying that like, oh, this doesn't work on my, on your site, I would be
[1849.84 → 1855.90] like, what, what? No, no, you're right. So I think that's genius. So really kudos to the Adobe team
[1855.90 → 1861.94] and you know, the product team that's kind of was able to kind of make bold bets and like
[1861.94 → 1866.44] bet on the web, you know, really, because really that's what the product team is doing, right?
[1866.46 → 1870.48] They're like, okay, we're going to take a chance. We're going to be the first. Nobody ever wants to
[1870.48 → 1876.28] be the first. Everybody, trust me, like there are so many overnights, like 10 year overnight successes,
[1876.28 → 1881.48] right? Projects like Fugue, like they've been in the works for years, and you're finally kind of
[1881.48 → 1887.06] starting to see the fruits of this, you know? And so, so kudos to that team. So Tom, let's get
[1887.06 → 1892.56] into kind of like what makes Photoshop successful, right? So what specific APIs are they using that
[1892.56 → 1898.50] are kind of really kind of showing off the power of these new APIs? So file system access is one,
[1898.58 → 1906.08] I guess, but you know, floor is yours. Yeah. So in Photoshop, it of course heavily depends on a
[1906.08 → 1913.06] decades old code base that they've taken and translated or transpired to WebAssembly using
[1913.06 → 1919.10] Scripted. And in Scripted, there are different ways of making applications happen. Like for example,
[1919.62 → 1925.06] in Scripted, they added SIMD support so that you can have a single instruction, multiple data. So
[1925.06 → 1930.52] essentially get more things done in parallel. They have P thread support so you can do stuff
[1930.52 → 1936.06] in background threads and so on. So Scripted is a very, very big topic. WebAssembly is a very,
[1936.06 → 1941.98] very big topic. I'm not an expert in any of these, but like what I have more insights into is the
[1941.98 → 1947.28] way Photoshop works is they have sort of a big swap file. So in Photoshop, you can open very, very
[1947.28 → 1954.20] big files that can reach gigabytes sometimes. The way this works is they have internally in Photoshop
[1954.20 → 1961.24] sort of swap file where they just randomly can access memory and write data and read data in parallel
[1961.24 → 1967.50] also into this file and from this file. And this primitive just didn't exist on the web.
[1968.10 → 1972.88] So what Chrome has built for them and what is now being standardized and what other vendors like Mozilla
[1972.88 → 1979.12] and Safari implement now as well, is the so-called origin private file system, which allows files to be
[1979.12 → 1984.02] created that are, as the name suggests, private to the origin, like Photoshop.adobe.com, for example,
[1984.02 → 1990.22] that only live in the context of this application. And yeah, they have certain performance guarantees,
[1990.22 → 1995.04] like you can write very performantly into them and read performantly into them. Like you don't have
[1995.04 → 2000.44] to wait for writes to be confirmed, which makes writing a lot faster. So all of these things,
[2000.86 → 2006.32] if you think web as well, there's a big problem, if you will, like we call it the mark of the web.
[2006.36 → 2010.62] So if you download a file from the web before you can execute it or open it, you get this warning,
[2010.62 → 2015.40] which tells you, Hey, this has come from the web and so on. There's safe browsing checks that need
[2015.40 → 2020.84] to happen. And of course, all of these checks take time within the OFFS, the origin private file
[2020.84 → 2026.04] system. These checks don't need to happen because technically they're files that are not really
[2026.04 → 2032.80] exposed to the user. So they live inside somewhere hidden in your browser. Technically,
[2032.80 → 2037.28] they don't even have to be files. They could be implemented as, for example, entries in a database.
[2037.28 → 2043.50] They just behave and feel to the developer like files. And I think this is the core thing here.
[2044.12 → 2048.90] How they're like the actual storage is an implementation detail that you as a developer
[2048.90 → 2056.02] don't have to know. And yeah, this makes working with these files so nice because to you as a
[2056.02 → 2060.12] developer, it just feels like, Hey, I'm opening a file, I'm writing into it and streaming data into
[2060.12 → 2066.44] it, whatever. So the look and feel is like a file, but then everything else, the other problems with
[2066.44 → 2069.40] files that you have on the web, you're going to have to be concerned about.
[2069.72 → 2074.32] Yeah, that's super cool. Tom, I feel like my head's a little like, I haven't been following
[2074.32 → 2079.62] this specific spec. So hearing where it is now, I'm like, what, what are we doing now? That's
[2079.62 → 2084.46] intense. Also, that sounds powerful. Besides, we had Debbie O'Brien on the show last week, we were
[2084.46 → 2088.42] talking about Playwright. And it was like, I was really we were pressed on time, I had to,
[2088.98 → 2093.16] I was really trying to avoid tangents. And I would say the same exact situation here. There are so
[2093.16 → 2098.46] many tangents, I feel like we could have an entire podcast on like, all the things ML did not say,
[2098.62 → 2102.34] I will take a really quick tangent for our listeners. I think this one is an important
[2102.34 → 2108.00] context I want to set for you all. So there's this concept of origin trials within Chrome. And it's
[2108.00 → 2111.88] like a fantastic concept. Tom, could you explain what that is to our listeners?
[2112.56 → 2118.12] So origin trials allows you to test new API's with actual uses. Why do we have this? So in the
[2118.12 → 2125.10] beginning, you might remember the like the early WebKit something prefixed API's. The idea there was,
[2125.46 → 2132.62] we agree, this is not an API that is standardized yet. It's an early test, maybe. So vendors thought,
[2132.74 → 2138.80] well, it's a clever idea to just prefix these APIs. The problem then is, because these features
[2138.80 → 2144.64] were in many cases very attractive, developers started using it and depending on it, which then
[2144.64 → 2151.62] ironically caused vendors like Firefox to implement things that are prefixed with WebKit just to be
[2151.62 → 2158.42] supporting all these use cases that developers had built. So learning from this, we're baking stuff
[2158.42 → 2165.36] into the web platform that then might just become baked in forever. And with no way to like to get back,
[2165.98 → 2171.98] origin trials was introduced as a safe way of playing with things that are in incubation still. So
[2171.98 → 2178.14] you could then just include a meta tag on your site. And if you have this meta tag on the site,
[2178.20 → 2183.26] the browser would detect it and then sort of unlock the API in question. So it's encoded in the meta tag
[2183.26 → 2191.72] token. Somehow what API is visible then if you have the token. And each token is also limited to a certain
[2191.72 → 2197.28] amount of time. So first you need to renew your token so that you really make sure that your web
[2197.28 → 2203.68] application stays up to date. So maybe there's been changes in the API so that if you change your
[2203.68 → 2208.24] token, you also need to change your code else it will stop working. But then in the end, of course,
[2208.52 → 2214.60] it's also important to not bake these maybe not mature yet APIs into the browser. So every origin
[2214.60 → 2221.12] trial is also just time boxed where we say it's supported from milestone X to milestone Y. And once
[2221.12 → 2227.18] milestone Y is over, either we just say, okay, the feature didn't work out. It's something that will
[2227.18 → 2233.88] be maybe iterated again upon, or we just, we say it's been a success. We can use it now. And more
[2233.88 → 2239.40] recently on the Chrome team, we introduced a concept of so-called gap-less origin trials, which means the
[2239.40 → 2245.48] origin trial would go straight into a feature that you could use in production. So this allows really
[2245.48 → 2252.08] to, if we have agreement on how an API shape should look like, that then the continuation would be
[2252.08 → 2257.74] there. You could start from the early days, go along the origin trial, and then take your users straight
[2257.74 → 2262.62] into prod. So that's the idea here. Yeah. Thank you for that awesome summary. And I didn't know that
[2262.62 → 2269.72] we have gap-less now. That's great. So the idea is like, we have this website called Nick'sBelovedTypeScript.org.
[2270.02 → 2275.32] Somebody should buy that domain if it doesn't exist. Nick gives it to Nick. But so Nick'sBelovedTypeScript.org,
[2275.72 → 2280.42] wants to use some API that isn't standardized yet, but that's implemented in Chrome specifically.
[2280.70 → 2284.76] So it's like, hmm, do we put like a set of instructions that's like, user, go to your
[2284.76 → 2289.42] settings, enable this flag. No, that's like, no, we're not going to do that. Right? And so how do
[2289.42 → 2295.02] we just automatically make it work for our users? And so you go to Chrome, you sign up for an origin
[2295.02 → 2300.36] trial, you give them your domain, and you get approved. And then it kind of automatically just
[2300.36 → 2305.30] works for your users. It's just like really, it's like basically a feature flag, but for web
[2305.30 → 2308.16] APIs, that's specific to Chrome. And it's like, awesome.
[2308.70 → 2310.74] That you control rather than the user, which is really...
[2310.74 → 2316.12] Exactly. That you control rather than the user. Exactly. For better or worse. Right? So make good
[2316.12 → 2317.06] decisions for your users.
[2317.60 → 2321.70] And I want to just call out quickly, Firefox has the same concept now. So in Firefox,
[2321.70 → 2329.18] very recently I've participated in the offscreen Canvas origin trial and Edge. So Edge, the Chromium
[2329.18 → 2334.96] based Edge, they also use origin trials now. So it's a concept that I think people like in general
[2334.96 → 2339.94] because of all the advantages that I just listed. So yeah.
[2340.14 → 2345.98] Yeah. Makes sense. So now that we know what origin trials are, let's go back to the file system API.
[2345.98 → 2354.22] Okay. So file system API was not initially on the standards track. It is now, obviously. I mean,
[2354.22 → 2360.78] it's been for a while, but I meant like, were origin trials kind of part of the story here for being
[2360.78 → 2366.18] able to actually experiment in the wild on this feature? Like, I'm curious, were teams, the teams
[2366.18 → 2371.42] like the Photoshop team use an origin trial initially, or are they using origin trials? Like,
[2371.42 → 2374.66] these are all open questions, Tom. I don't know the answers. Tell me.
[2375.06 → 2379.86] So we need to be a little bit careful here. So when you say file system API, there has been
[2379.86 → 2381.76] definitely more than one. Okay.
[2382.20 → 2387.10] There has been something like the file system entries API or something like that. So there have
[2387.10 → 2392.12] been several attempts also at standardizing, not just proprietary stuff, but really standardizing
[2392.12 → 2397.86] file system access on the web. What we can talk about specifically now in the context of Adobe,
[2397.86 → 2404.56] this is the origin private file system part. And more specifically there, the access handles.
[2404.56 → 2410.98] So the thing that gives you access to these files that are private to the origin. And there is,
[2411.10 → 2416.38] or has been an origin trial that Adobe has been taking part of. So they went through this entire
[2416.38 → 2422.20] process of breaking changes that from one origin trial version to the other, they needed to implement
[2422.20 → 2429.48] and so on. So now the origin trial is, I think it's over. But yeah, definitely there's the API
[2429.48 → 2435.22] that is agreed on universally. Now it's being standardized in a living standard, the file system,
[2435.68 → 2439.94] what's it called? The file system, I think it's just a standard's name now. Important to say is if
[2439.94 → 2445.42] you talk about file system access, there's the file system access API that has the so-called picker
[2445.42 → 2450.34] methods. So show open file picker, show save file picker, and so on. So this is not that.
[2450.34 → 2458.54] So the file system part that is being standardized now is first, how do we work with files in general,
[2458.78 → 2463.94] as like the file methods, to rename a file, to move a file, to delete a file, to create a file in the
[2463.94 → 2468.74] first place, to write to a file and so on. So this is being standardized. The way you can create a file
[2468.74 → 2474.32] is in the origin private file system or by using the picker methods. And the picker methods, these are
[2474.32 → 2481.52] like more powerful APIs. And this is also where we still have some disagreement on, because it allows
[2481.52 → 2486.00] you to open files from your local file system. And as I mentioned before, on the local file system,
[2486.12 → 2492.70] like the user visible files, you have all these problems, like what about ransomware attacks,
[2492.76 → 2499.22] where someone just gets access to your whatever projects folder, and then encrypts everything. So
[2499.22 → 2506.70] they want to get some ransom from you to decrypt again your files and so on. So it's a little bit
[2506.70 → 2511.56] more interesting when it comes to those picker methods. The other part, this is where we have
[2511.56 → 2516.54] universal browser agreement on. Yeah, and thank you. And I, like I said, I have not been following this
[2516.54 → 2520.82] spec. And it's like, it's so interesting to learn from you that this is it's diverged into all of these
[2520.82 → 2525.70] different things, which makes sense, right? There's been limitations that have been found. And so like,
[2525.70 → 2529.36] go like here, let's just instead of throwing the whole the baby out with the bathwater,
[2529.52 → 2533.74] let's focus on this one narrow part of the spec. And let's get this one narrow part, right.
[2533.86 → 2539.84] And I love that approach. And like, this is why standards work is like, I think I've said the word
[2539.84 → 2544.70] God's work already in this podcast, I'm going to say it again, it is God's work. So it's amazing.
[2545.06 → 2549.46] Hard work. So yeah, so lots to continue to unpack. So we'll be right back, everyone.
[2555.70 → 2567.40] What's going on, party people, this episode is brought to you by our friends at Lolo Code.
[2567.74 → 2572.54] Lolo Code lets you build cloud-agnostic serverless apps that make it easy to go from zero to one.
[2572.96 → 2576.90] If you're familiar with building serverless apps, you can think of Lolo Code as your backend with
[2576.90 → 2581.94] a visual editor, let you think and build at the same time. All this without having a provision
[2581.94 → 2586.84] or managed servers. So with no servers to worry about and an amazing visual editor to build your
[2586.84 → 2592.44] app, connect nodes and add any NPM libraries you need. You have no limitations and no complexity to
[2592.44 → 2598.00] deal with. And Lolo Code is low code is. You can even write your own integrations. This means you
[2598.00 → 2601.48] can build templates within your account or use templates that have been shared with you. For
[2601.48 → 2605.56] example, you can build a library function with Slack and then just connect it to your workflow or
[2605.56 → 2611.58] MongoDB or OpenAI or whatever else you're using parameters for in your code to create dynamic values.
[2611.94 → 2617.46] This makes Lolo Code very Zapier like, but for devs. Lolo is built for developers. So try it free
[2617.46 → 2625.06] today with no credit card required at Lolo.co slash js party. That's L-O-L-O dot C-O slash js party.
[2625.06 → 2631.54] And by our friends at Sentry, build better software faster, diagnose, fix, and optimize the performance
[2631.54 → 2638.90] of your code. More than a million developers in 68,000 organizations already use Sentry and that
[2638.90 → 2644.76] includes us. Here's the easiest way to try Sentry. Head to Sentry.io slash demo slash sandbox.
[2645.24 → 2650.68] That is a fully functional version of Sentry that you can poke at. And best of all, our listeners get
[2650.68 → 2655.20] the team plan for free for three months. Head to Sentry.io and use the code party time when you sign
[2655.20 → 2658.88] up again, Sentry.io and use the code party time.
[2676.64 → 2680.98] So first off, I love the name Project Fugue. It reminds me of that Simpsons episode,
[2680.98 → 2687.38] the Fugue fish. Fan Fugue-tastic. Is there a place, like a consolidated place where we can find out more
[2687.38 → 2693.08] about like what all is going down with Project Fugue and the different APIs that are being experimented
[2693.08 → 2698.88] with and the status of them and all of that? Yeah, sure. We have two places. So there's the
[2698.88 → 2703.84] Fugue API tracker that allows people to just see in the open what APIs are we working on,
[2704.26 → 2710.60] what is in our pipeline, what features are we implementing and just working on. And there's
[2710.60 → 2716.48] the Fugue API showcase where we show people who have been building applications, and you can go
[2716.48 → 2722.76] and see, just get inspiration what people have been building with these APIs. You can filter by API and
[2722.76 → 2727.88] you can see, I want to get a list of all the apps people have built with, I don't know, the local
[2727.88 → 2734.14] font access API or the file system access API or whatever. So you can just filter by API. You can
[2734.14 → 2740.14] search by app name if you know a specific app, and you want to see what APIs is a specific app using.
[2740.60 → 2746.74] So the showcase is really your destination for this kind of question. So if you want to just get
[2746.74 → 2753.10] inspiration, just purely browsing the API showcase, launching the applications, testing and playing
[2753.10 → 2758.62] with them definitely helps. In many cases, there's even source code links. So you can go there and see
[2758.62 → 2765.84] how did they do it? How did they implement local font access in whatever application? So you can see and
[2765.84 → 2770.00] get a feel for the code as well. I was just going to call that out. I was looking at the showcase and
[2770.00 → 2775.30] seeing the links to not only try the apps, but also view the source code. Like that's so helpful
[2775.30 → 2779.94] in being able to, to mimic what they're doing or get an idea of how to approach using the API,
[2780.08 → 2786.52] which is so, so helpful. Very much so. Yeah. And so like, I think we've maybe got time for one more
[2786.52 → 2792.76] API. I feel like every single API really requires its own dedicated show. So this is really just kind
[2792.76 → 2797.62] of a brief overview, ladies and gentlemen, a brief overview, very brief, free for the small b.
[2797.62 → 2803.24] So Tom, what's another favourite API of yours that you're like, this one should be it,
[2803.36 → 2807.40] regardless of what stage it's in. Let's just take the shackles off the standards process a little
[2807.40 → 2811.10] bit. What are you the most excited about? You know what? I'm going to cheat. I'm going to mention
[2811.10 → 2817.02] two. Okay. Cheat. Give us two. So first I want to mention the Clipboard API. Oh, yes.
[2817.50 → 2823.52] The way working with the Clipboard works is very interesting actually, because if you think about
[2823.52 → 2829.10] like Clipboard interactions, you can go to the macOS finder and copy a file and paste it. So then
[2829.10 → 2835.40] you paste a file. You can go into Photoshop and select everything and copy it. And then you have
[2835.40 → 2840.82] an image on your Clipboard and you can paste that image file in the sense of you paste the image data.
[2841.22 → 2846.32] If you think I'm going to a website and selecting everything, and then you paste it into, let's say,
[2846.38 → 2852.04] Word, you will see that you have pasted sort of HTML that then magically got translated into
[2852.04 → 2857.16] whatever Word thinks should be the best representation of this HTML content. So preserving,
[2857.32 → 2861.30] for example, the semantic information that something is a headline, headline one or so,
[2861.64 → 2867.54] would be translated into a heading level one in Word. But then if you press this magic key
[2867.54 → 2876.12] board shortcut, which is Command Shift V on a Mac, you will paste text only. So you're sort of losing
[2876.12 → 2881.24] this information and just pasting the text. And this is pretty powerful as a concept because
[2881.24 → 2886.52] with a Clipboard API, you can do the same thing. Now you can put different representations of the
[2886.52 → 2892.32] same content onto the Clipboard. So if you're building an application that edits SPG files,
[2892.34 → 2897.36] for example, you can put the image data on the Clipboard. But at the same time, you can also put
[2897.36 → 2901.86] the source code because it's XML based. So it's all readable. You can put the source code on the
[2901.86 → 2907.02] Clipboard. And then depending on the application context, if you paste into VS Code, you can paste the
[2907.02 → 2911.50] source code. And if you paste into something like Adobe Illustrator, you can paste the image data,
[2911.86 → 2916.18] you can do the same thing there on the Clipboard. And the way it works is super, super simple. If you
[2916.18 → 2921.28] look at the code, it's just essentially creating different blobs of different MIME types and putting
[2921.28 → 2927.72] them onto the Clipboard. So that's my first API that I really, really, really love. The second one is
[2927.72 → 2933.58] file handling. So it allows registered applications, progressive web applications,
[2933.58 → 2938.72] applications, web applications, whatever, to register themselves as a file handler.
[2939.36 → 2944.36] Which means if you have an example application that deals with.example files, you can say,
[2944.50 → 2951.78] hey, my PWA can become the file handler for.example files. Which means if people have a.example file
[2951.78 → 2957.46] in their File Explorer, Windows Explorer, or macOS Finder, or whatever, they can just double-click,
[2957.46 → 2965.10] and the PWA will open. Very, very powerful concept. And what I like most about it is it feels so
[2965.10 → 2970.20] natural. So once you've gotten used to it, you don't think anymore, is it a.example file and
[2970.20 → 2975.68] Word opens, or is it a.example file and the example app opens? And if it's well-made, you can,
[2976.00 → 2981.30] in many cases, not even spot a difference between a native application and a web application. Sort of
[2981.30 → 2986.52] what we said in the beginning, we are sort of back to there. If you build something that is well
[2986.52 → 2992.20] integrated into the operating system, people think of your applications like apps. And that's what you
[2992.20 → 2996.80] want to be at. So that's a point you want to be at. People don't think or should not have to think
[2996.80 → 3001.56] about how is something implemented, especially not users. They should just be using your app and be
[3001.56 → 3008.84] like, oh, wow, this is so cool for, I don't know, editing my video files or adding my.example files
[3008.84 → 3014.22] or whatever. So I think this is where you want to get at. People should be using your app without
[3014.22 → 3019.64] really thinking it's a web app. It's just something that fulfills their use cases, covers
[3019.64 → 3024.56] their use cases well. That's so important too, because it's, you're covering these minute things
[3024.56 → 3029.08] that users really wouldn't think about, right? And probably when you're implementing this, you don't
[3029.08 → 3033.46] think about it too much. But like when you click on something, you want it to open in the app that
[3033.46 → 3040.22] you would expect. And like that just gives it so much more of a native feel that it starts to become
[3040.22 → 3047.04] indistinguishable. So like, bravo on focusing on these little things that really add up to
[3047.04 → 3051.54] like the expected user experience, which is like so important for adoption.
[3052.08 → 3057.94] And that polish, right? And it's all this invisible work, like you're saying, Nick, like it's all the
[3057.94 → 3063.16] stuff that you, it's like, this is how you think it should work. But actually in order to get it to work,
[3063.16 → 3066.44] in the way that you think it should work, it actually is like, there are a lot of gaps that
[3066.44 → 3070.76] need to be filled. That's just not the way it was designed to work, right? And this, this example,
[3070.98 → 3076.84] Tom, that you shared of copying and pasting, like text with, you know, header texts and things with
[3076.84 → 3081.52] bullets and just being able to kind of copy and paste that seamlessly throughout different applications
[3081.52 → 3085.96] and windows and whatever else, you know, you think that that should just work, right? Like,
[3086.02 → 3090.26] oh, what do you mean? Text is text. Isn't there a standard? No, it's not, actually. Text is really,
[3090.26 → 3092.88] really complicated and blah, blah, blah, blah, blah, right? Like,
[3093.16 → 3099.76] so amazing to hear that. And I think, I think that's also to highlight, like going back to Nick's
[3099.76 → 3103.80] point, right? This idea of this, it should just work this way. I think that's one of the reasons
[3103.80 → 3109.04] why standards take as long as they do, right? Like there's people don't realize just how things don't
[3109.04 → 3114.42] actually work the way you think they do basically, right? I'm glad that we're doing that hard work.
[3114.42 → 3119.78] This maybe is a nice tangent as well, like very quick tangent file handling, as I said, is for
[3119.78 → 3125.42] installable applications that they can register themselves to become a file handler. But at the
[3125.42 → 3130.64] same time, if a browser doesn't have a concept of installation to begin with, so for example,
[3130.90 → 3136.54] Safari, for example, Firefox, they don't have proper installation on desktop. So on mobile, you can
[3136.54 → 3142.40] add applications to the home screen in Safari. But if you don't have this concept of installation,
[3142.40 → 3148.22] if you don't have this concept of file handling, you can still build the same amazing progressive
[3148.22 → 3155.28] web app. And people can still use your application in a tab and be very happy users. And if you have
[3155.28 → 3159.76] a browser that supports installation, if you have a browser that supports file handling, you can add
[3159.76 → 3165.12] these additional features. But in many cases, yeah, they are progressive enhancement, they will make
[3165.12 → 3170.28] the experience better, but you can still live and use the application without. And I think this is a
[3170.28 → 3177.88] very important concept to take home with progressive enhancement in many FBO API cases is very
[3177.88 → 3184.62] important. And once a browser then eventually maybe start supporting a certain feature, your app will
[3184.62 → 3190.44] just magically work. So we've been using progressive enhancement for a long, long time. But the idea
[3190.44 → 3197.58] is still fresh and maybe even fresher than ever. Thinking just about something like web codecs that allows you to
[3197.58 → 3206.02] do video and image and audio coding codec stuff in the browser. As a progressive enhancement, you can do it as a
[3206.02 → 3212.96] fallback, you can do it on the server. And if you have a browser that is capable of web codecs, you can just do it on the
[3212.96 → 3215.40] client. So I think this is where we can go to.
[3216.06 → 3222.58] That's amazing, Tom. And it's very hopeful to hear about all the work that's happening and all the kind of
[3222.58 → 3229.06] supercharged superpowers that are going to kind of continue evolving and continue being added to the web.
[3229.26 → 3235.38] It's really, as somebody who deeply cares about this platform, like I could not be more delighted to learn about all of this.
[3235.84 → 3241.90] I would say that like, it'd be great. I don't know if the FBO Showcase site has a list of like, here's all the things
[3241.90 → 3246.90] that native app can do. And here's all the things you still can't do in the, in the web. And here's where we are. Like,
[3246.90 → 3250.68] here's how we're doing. You know, here's how we stack up. I don't know if there's like a stack rank
[3250.68 → 3256.14] comparison, but we'll have to discuss that maybe with Alex and on another show. Cause that's,
[3256.30 → 3262.06] that's all we've got time for today. But it's been an absolute pleasure to kind of have you on the show,
[3262.30 → 3268.02] Tom. Thank you so much for kind of enlightening us. And I hope our listeners are inspired by all the
[3268.02 → 3272.58] really great things that are coming to the web that are on the web in some browsers already.
[3272.84 → 3275.76] It's really been very exciting to learn. So thank you, Tom.
[3275.76 → 3276.90] Yeah. Thank you.
[3277.40 → 3279.00] Thanks for having me. It's been an honour.
[3279.44 → 3284.00] Yeah. Been an honour. And so where can folks connect with you and learn more about you and
[3284.00 → 3284.66] all of that jazz?
[3285.16 → 3289.64] I'm Tomahawk on most places on the internet. So you can find me on Twitter still, but also
[3289.64 → 3295.60] on Mastodon. I'm Tomahawk at 2.café if you want to reach out there. But yeah, if you just search for
[3295.60 → 3299.38] Thomas Steiner Google, you will find me. I'm pretty searchable on the web.
[3299.74 → 3300.44] All right. Yeah.
[3300.74 → 3304.74] I would expect nothing less than for you to be Googleable.
[3304.74 → 3309.04] All right, everyone. It's been an awesome show. Thank you. We'll be back next week. Take care,
[3309.14 → 3309.84] everyone. Bye.
[3310.24 → 3311.46] Thank you very much. Bye-bye.
[3311.46 → 3316.46] Bye-bye.
[3316.46 → 3317.02] Bye-bye.
[3317.02 → 3317.64] Bye-bye.
[3317.64 → 3317.92] Bye-bye.
[3317.92 → 3323.98] This has been JS Party. Thanks for listening. Subscribe now if you haven't yet. Head to
[3323.98 → 3331.14] jsparty.fm for all the ways. It's December now, so you may be writing up your top slash favourite
[3331.14 → 3336.62] things of the year. If that's something you do, and we make your list, shoot us a message
[3336.62 → 3342.72] on Twitter at jsparty.fm or on Mastodon at js party at changelog.social. We'd love to hear
[3342.72 → 3348.28] about it. Special thanks once again to Vastly and Fly.io for partnering with us to bring you
[3348.28 → 3354.32] JS Party each and every week. You can check out what they're up to at fastly.com and at fly.io.
[3354.32 → 3358.90] And thanks, of course, to our mysterious friend, Break master Cylinder, for these beats.
[3359.52 → 3365.60] Next up on the pod, it's the Kevin and Kevin Show. That's K-Ball hosting and CSS evangelist
[3365.60 → 3371.66] and prolific YouTuber Kevin Powell guesting. The topic of conversation, learning and mastering
[3371.66 → 3376.10] CSS. Stay tuned for that. We'll drop it into your podcast app next week.
[3384.32 → 3385.46] K-Ball.
