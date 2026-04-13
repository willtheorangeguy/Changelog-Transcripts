[0.00 → 13.12] this is js party your weekly celebration of JavaScript and the web good news everyone
[13.12 → 21.02] we just dropped dance party our third full-length album on changelog beats buy it on Bandcamp or
[21.02 → 27.34] stream it on Spotify Apple Music and the rest link in the show notes enjoy the draw
[27.34 → 35.40] thank you to our partners at fly.io launch your app close to your users find out how at fly.io
[35.40 → 37.92] okay hey it is party time you all
[37.92 → 49.46] what's up friends this episode of js party is brought to you by our friends over at oversell
[49.46 → 55.52] and I'm here with lee Robinson VP of product lee I know you know the tagline for oversell develop
[55.52 → 60.44] preview ship which has been perfect but now there's more after the ship process you have to
[60.44 → 66.66] worry about security observability and other parts of just running an application production
[66.66 → 71.82] what's the story there what's beyond shipping for oversell yeah you know when I'm building my side
[71.82 → 76.42] projects or when I'm building my personal site it often looks like develop preview ship you know i
[76.42 → 80.84] try out some new features I try out a new framework I'm just hacking around with something on the
[80.84 → 86.06] weekends everything looks good great I ship it I'm done but as we talk to more customers as we've
[86.06 → 90.88] grown as a company as we've added new products there's a lot more to the product portfolio of
[90.88 → 96.06] oversell nowadays to help pass that experience so when you're building larger more complex products
[96.06 → 100.58] and when you're working with larger teams you want to have more features more functionality so
[100.58 → 106.10] tangibly what that means is features like our oversell firewall product to help you be safe and to
[106.10 → 111.14] have that layer of security features like our logging and observability tools so you can understand
[111.14 → 115.70] and observe your application in production understand if there's errors understand if things
[115.70 → 121.44] are running smoothly and get alerted on those and also than really an expansion of our integration suite
[121.44 → 127.18] as well too because you might already be using a tool like a data dog, or you might already be using
[127.18 → 131.38] a tool at the end of this software development life cycle that you want to integrate with
[131.38 → 136.82] to continue to scale and secure and observe your application, and we try to fit into to those as
[136.82 → 143.90] well too so we've kind of continued to bolster and improve the last mile of delivery uh that sounds
[143.90 → 149.50] amazing so who's using the oversell platform like that can you share some names yeah I'm I'm thrilled
[149.50 → 155.88] that we have some amazing customers like under armour Nintendo Washington Post Zapier who use
[155.88 → 161.22] oversell's running cloud to not only help scale their infrastructure scale their business and their
[161.22 → 166.40] product but then also enable their team of many developers to be able to iterate on their
[166.40 → 171.94] products really quickly and take their ideas and build the next great thing very cool with zero
[171.94 → 177.74] configuration for over 35 frameworks oversell's front and cloud makes it easy for any team to deploy
[177.74 → 183.68] their apps today you can get started with a 14-day free trial of oversell pro or get a customized
[183.68 → 189.78] enterprise demo from their team visit versell.com slash changelog pod to get started
[189.78 → 194.68] that's v-e-r-c-e-l.com slash changelog pod
[194.68 → 224.66] hello js party listeners uh welcome to yet another week with us um we're excited to be able to
[224.66 → 229.52] very excited about today's show and today's guests um we're going to be talking about
[229.52 → 236.26] react server components and kind of deconstructing them with Dan Abrams who's here to kind of help
[236.26 → 243.50] us bust some myths set some truths do some deep dives set some facts I've already been fact-checked
[243.50 → 249.22] like seven times uh just in preparation for this show Dan's already set the record straight so I'm like
[249.22 → 255.02] excited to continue to be fact checked with us to kind of ride along with us for this ride today is
[255.02 → 261.26] Eric Clemens my friend who I invited to essentially play the realists role right because i I think I've
[261.26 → 266.74] been outside this React community for a little bit now, and you know i I'm coming at this from the
[266.74 → 273.84] skeptics perspective and Eric is like very deep within, and he's a realist, and he's like a lover of
[273.84 → 278.02] all the things, and he's been playing around with RCS, and he loves them, and so I'm really excited to
[278.02 → 282.88] kind of have his voice on the show and then of course you have Dan who's been you know part of
[282.88 → 288.62] the core team for many years and generally been educating the community um for many years around
[288.62 → 294.02] best practices and how to use React and all of that jazz so I'm super excited about today's
[294.02 → 300.18] discussion uh so with that said let's get started with introductions so welcome Dan uh can you tell us a
[300.18 → 304.66] little bit about yourself even though I feel like you don't really need an introduction yeah first
[304.66 → 312.38] thank you so much for inviting me I'm super happy to be here so i I started using react in 2014 I think
[312.38 → 319.44] and after that I joined the React team in 2015 and I've been on the React team for about eight years i
[319.44 → 325.98] think I'm currently on kind of break because so I joined blue sky which is a know a company that
[325.98 → 331.52] uses react and React Native so I'm actually learning React Native and like learning how to use it and I'm
[331.52 → 337.72] really kind of in the product development mindset as a user of React now so I haven't actually been
[337.72 → 344.06] very involved with the team and i kind of speak in personal capacity on this show so yeah Dan you know
[344.06 → 348.04] it feels like the React core team is a little bit like hotel California you know where you can never
[348.04 → 353.00] quite leave because I know you're not officially part of it but based on the internet you would never know
[353.00 → 357.06] you would never know right because you're you're talking about it, and you're just like you're you're
[357.06 → 361.28] in all the things I feel like it's actually the other way around because like officially I'm still on
[361.28 → 365.32] the team but actually like I haven't showed up to meetings for a while just because like I'm too
[365.32 → 372.12] like overloaded trying to learn React Native so i I do want to get back to it uh so I'm on a bit of a
[372.12 → 376.32] sabbatical I guess so you're talking about React Native I want to know when is blue sky going to have a web
[376.32 → 384.44] client it does yeah, so there is an uh sky dot app I think that's i I may be wrong but I think that's
[384.44 → 389.56] the in the current year we have like three different domains okay I keep forgetting which one is which
[389.56 → 396.16] okay I have to check out the web client uh that's great and so Eric again welcome back to the show um
[396.16 → 401.10] can you give our listeners a little bit of I mean you know besides you're a mega DX nerd tell us a
[401.10 → 405.80] little bit about yourself yeah yeah, thanks for having me of course, but it's interesting it's like I've
[405.80 → 411.22] been in the webspace for such a long time you know people are kind of like touting their tenure
[411.22 → 416.08] in web but what I think is fascinating is just like the evolution that's continually happening
[416.08 → 422.24] and one of which was like whenever react dropped I think like the 0.12 days the company I was at
[422.24 → 428.78] we were focused on just building kind of like web forms and as long as we got the job done they
[428.78 → 432.48] didn't really care like how we built things so we got to kind of you know cut ourselves on the bleeding
[432.48 → 437.54] edge a little bit, but the thing was like React really was a hero from the very beginning going
[437.54 → 442.64] from like an angular app and PHP apps like we went to server side react back in the day probably
[442.64 → 449.48] a little too soon and had to figure out like async data fetching and uh serializing data and stuff but
[449.48 → 456.42] the result of it was millions of dollars of actual like conversions that happened as a result of like
[456.42 → 462.26] faster rendering response times uh progressive enhancement basically was what we kind of like shot for
[462.26 → 468.26] there and so like React was the thing that kind of made us successful for I think six years of just
[468.26 → 474.16] continually to build on, and so I wouldn't be here if it weren't for react actually I'd say yeah
[474.16 → 479.98] and you have some pretty popular libraries to one of them being um click to component which i
[479.98 → 485.02] really love and I feel like most more people need to know about that and use it but um it's a
[485.02 → 489.82] component that like does you want to tell people about it yeah I mean everything's born out of a DX
[489.82 → 494.42] need right and I wish I could just be funded full-time to take all the paper cuts that developers
[494.42 → 499.50] deal with and like make them all 10x engineers but yeah the long and short of it is that most of the
[499.50 → 503.30] time when you're doing web development you see what's on the page you say that's either right or
[503.30 → 506.80] that's not right, and you just need to kind of go to the source code and going through like the dev
[506.80 → 511.38] tools won't get you straight to the source code uh but click to component as a wrapper there's a
[511.38 → 516.18] Chrome extension that I think has actually like surpassed it in terms of functionality and multi-framework
[516.18 → 520.94] support I don't have a name for it offhand but I think it's you know probably like the way to go for
[520.94 → 525.12] individuals who just want to look at the page go straight to the source fix it and have like a
[525.12 → 529.66] pass or feedback loop, but that's actually like the long and short of it is that like being able to
[529.66 → 536.64] focus on the like what you're trying to do and get all the annoying friction and steps out of the
[536.64 → 541.60] way in between you and just getting your job done and actually I think RSCS like play into that
[541.60 → 546.52] narrative pretty well that's awesome and excited to dig in so before we dig into RSCS i kind of want
[546.52 → 551.48] to do a couple of things like one I want us to tell like I want to hear from both of you on like what
[551.48 → 556.58] is your React love story because you know the three of us didn't find it right so like in theory
[556.58 → 562.96] we saw it, and we were like oh right so what's your React love story and then I want to get into
[562.96 → 568.04] kind of the evolution of React that will kind of take us into like RSCS and where we are today
[568.04 → 574.12] I'll kind of start first with my React love story um so for me, you know I think I came into react from
[574.12 → 580.86] the angular 1x world and backbone can JS and knock out like so many different things jQuery right like
[580.86 → 588.22] it's a whole smorgasbord of things including like rails PHP a lot of things and the thing for me you
[588.22 → 593.18] know what just clicked was that you know it is just like it just made sense like looking at a React
[593.18 → 597.82] component and the way things were structured the fact that everything was just JavaScript for me was the
[597.82 → 603.48] big like aha right because I didn't have to learn any additional syntax like if I wanted to loop
[603.48 → 608.52] or map or do whatever like it was just JavaScript um you know sure there were a couple of things you
[608.52 → 613.92] had to learn to learn around like what are the syntax around JSX right but for the most part everything
[613.92 → 619.00] just felt very intuitive and I think for me, it was just you know like starting to kind of become
[619.00 → 625.74] a lead at that point like it was just seeing the accelerator like seeing how much of an accelerator
[625.74 → 632.42] it was for teams uh quickly creating um components being able to kind of compose them easily being
[632.42 → 637.72] able to kind of organize their code in a better way it was just kind of like it went from you, you're
[637.72 → 642.62] able to kind of go from zero to hero very quickly and I think that was really exciting of
[642.62 → 647.44] course it came along with some pretty big shifts around like you had to use a compiler for the first
[647.44 → 652.66] time you know in the JavaScript world, and you know, and you're getting things from NPM, and you know
[652.66 → 658.08] and that was like that was new right but for the most part huge accelerator and I think you know
[658.08 → 663.84] was a huge fan of React I think for me where react started to kind of where I shifted into a skeptic
[663.84 → 668.98] was specifically around you know when I started to see frameworks like preach come along, and you know
[668.98 → 674.60] have very similar API with lower bundle size and better performance and I was like you know what i
[674.60 → 680.76] would really like more of a focus on performance um the other kind of skeptic like my skepticism kind of
[680.76 → 686.84] grew with you know how the suspense and concurrency and uh some of the other kind of shifts in the API
[686.84 → 690.46] where I was like you know what I really want to just focus more on performance like let's just fix
[690.46 → 695.18] that problem and then i kind of moved into different spaces and that's just kind of where I dropped off
[695.18 → 699.62] but for the most part like that that's my love story with react and I think it obviously really
[699.62 → 705.66] shifted the ecosystem forward as well in terms of design so Dan and Eric eager to hear from you
[705.66 → 710.48] both I think it's actually interesting you mentioned that you're interested in performance
[710.48 → 715.84] but then the things that kind of shifted your attention were like these are features for
[715.84 → 721.28] performance, so there is an interesting irony there it is ironic I think it was just that the API it
[721.28 → 726.44] wasn't just uh it was around the same time that I know suspense was kind of there to kind of
[726.44 → 731.78] improve perf to some degree, but the point is like the API around hooks I think the design
[731.78 → 737.44] also really bothered me specifically like I thought that like it just wasn't intuitive it is like it just
[737.44 → 742.30] it just kind of like everything in React was intuitive until like hooks came along for me like
[742.30 → 747.00] this is my personal opinion I think that's kind of where like for me like the seed of skepticism was
[747.00 → 752.36] like planted and like it just never fully gone away so but yeah but I'm I'm I'm hopeful
[752.36 → 759.08] like again like I'm I'm here to hopefully change my opinion on things so lets you know I'm I'm coming
[759.08 → 764.82] through this conversation with an open mind right so back to you sure yeah so for me, I think the first
[764.82 → 770.52] time I looked at the React I thought that that just looks silly but then i I wasn't I was pretty
[770.52 → 777.02] new to web development at the time so before that I was doing mostly desktop development uh with c
[777.02 → 784.92] sharp dot net and a little bit of mobile with iOS and also c sharp using what's now called Xamarin i
[784.92 → 790.32] don't know that's the thing anymore, but that's what I was using and then uh we started using angular
[790.32 → 798.30] 1.x uh for a little bit of build some UIs with it and at some point you know react came out i kind of
[798.30 → 804.40] dismissed it originally I didn't get it and then my colleague uh like a few months later my colleague
[804.40 → 809.56] sent the link to react again he was like no like you know check it out like there is something
[809.56 → 817.40] to this, and so I tried to like at the time I was actually um so I was working on an app uh where you
[817.40 → 823.84] could post different kind of like multimedia posts with like images galleries uh text and a bunch of
[823.84 → 829.82] stuff and uh I was at the time working on the like button so I needed to add you know like a like
[829.82 → 836.94] button you can press like it shows uh you like this or you and like Andrew you like this or like
[836.94 → 842.92] you and like three people like this so it has to like to show different things depending on you know
[842.92 → 848.52] what the data is and then like when you press it, it can kind of push it over into like one of these
[848.52 → 855.30] different states and I tried at the time we were using backbone, and you know like you, you had to write
[855.30 → 861.26] your initial template for you know the initial data, but then you had to listen to events or like did I
[861.26 → 867.50] press the button and then change you know the template dynamically to the final state and then
[867.50 → 872.56] with react just like the first time I tried it I realized oh I can just write an if statement so
[872.56 → 879.20] like if nobody liked this then return this if one person liked this return this and react handles
[879.20 → 885.26] the transitions between these states so i can just describe the user interface as a function of
[885.26 → 890.72] uh of state or like kind of like as a frame in the movie and there's only the current frame you
[890.72 → 897.16] never think about time and so this was my first react component just a like button and then
[897.16 → 904.82] we started uh trying it in a few more places and it kind of just ate our app from inside out because
[904.82 → 910.10] you know it started like somewhere deep and then if we gradually started using more and more react as
[910.10 → 915.48] we kind of climbed higher and even though like I think like that was before you know people were
[915.48 → 919.88] complaining about JavaScript fatigue and like all that stuff like we were excited because
[919.88 → 926.24] you know everything used to be so bad like it was just very hard to build dynamic UIs and
[926.24 → 932.28] we were rewriting our product in react at the same time as shipping features, and actually we were
[932.28 → 939.08] faster while doing the rewriting just because react enabled us to make everything so dynamic so that's
[939.08 → 942.94] kind of how I think that that that was that that moment for me, you knew what you're doing mentioning
[942.94 → 949.10] JavaScript fatigue there Dan i I see I was like reattaching Eric yeah eric had a famous viral
[949.10 → 954.76] blog post from back in the day titled exactly that yeah that was such an interesting thing because i I think
[954.76 → 960.52] that that blog post actually kind of got us talking a little more one-on-one because that was
[960.52 → 966.40] you know right before the creation react app abstractions and like those days babble preset
[966.40 → 974.06] MV wasn't a thing so and that that did strike a chord with I think like the React community but I don't
[974.06 → 979.48] think actually because of React I think it was because of everything else around react in retrospect
[979.48 → 986.02] but my it's so funny we have such interesting like and similar love stories like we kind of got into
[986.02 → 991.18] it around the same time as on the ground floor uh and I think like that's a bit of our honeymoon
[991.18 → 995.66] period where like a lot of people who got in there early they see react today and that's not the React
[995.66 → 1000.94] that like they fell in love with like 10 years ago it seems you know that they got that's that's me
[1000.94 → 1006.16] yeah it's like it was successful it got the job done but like it's not like how you do react
[1006.16 → 1012.02] any more it's like you've changed but i I haven't but yeah it was an incremental thing for us too like
[1012.02 → 1019.42] we had a phased business the page response times were like around 800 milliseconds or something like
[1019.42 → 1024.80] that and whenever we had the issue of just complex form logic, and we want to make sure that when we
[1024.80 → 1029.70] submit forms and validate data that the logic and PHP backend was the same as a front end that we're
[1029.70 → 1033.08] trying to improve for good experience and so like if only we could use JavaScript everywhere
[1033.08 → 1039.94] and once we did that the response times went to like 200 milliseconds and that was like our first
[1039.94 → 1044.94] attempt at using react and already got that much better and in e-commerce you improve like you know
[1044.94 → 1050.02] response times and conversions go up, and then we got it down to like to 40 milliseconds and the
[1050.02 → 1055.52] business is just like whatever you're doing step on the gas keep it up and so like we just went
[1055.52 → 1062.42] headstrong into everything else around react the whole JavaScript ecosystem like we got deep into
[1062.42 → 1068.76] webpack 2 at the time released we got async bundles to improve like uh and code splitting to improve
[1068.76 → 1074.44] performance even more and then looking outwards because of React success it made us look at other
[1074.44 → 1080.28] things like well what else could we do that this community is doing and led us to continuous deployment
[1080.28 → 1084.70] and we're deploying dozens of times a day for a business that was deploying you know once a week
[1084.70 → 1089.98] or once every two weeks, and you know had a multi-hour deployment process and so like I would say like
[1089.98 → 1096.86] react was kind of like that that first hit of the JavaScript drug that got us successful gave us that
[1096.86 → 1102.96] high and then and then we kept going with everything else in the ecosystem, and we had no idea you know
[1102.96 → 1108.80] people talk about like a new framework every day, but there's a new solution so often that solving some
[1108.80 → 1115.00] problem unique to maybe your case or not you know some uh that don't apply to you, and you get
[1115.00 → 1121.46] to just have a buffet of stuff that's potentially going to make your business better, and we were able
[1121.46 → 1127.00] to ride that wave for years until like I left the business like six years or something later after the
[1127.00 → 1134.32] initial adoption so yeah I mean i I think I'm doing python today you know Dan you're talking about like
[1134.32 → 1138.94] learning React Native and like I've had to learn python thank you ChatGPT and copilot for teaching
[1138.94 → 1145.30] me python syntax, but it makes me miss you know the velocity I had of being able to have end-to-end
[1145.30 → 1153.22] JavaScript react and that locality of behaviour yeah so well said Eric um and yeah like i you know this is
[1153.22 → 1157.90] like a pretty good segue into kind of you know the evolution of React because you know you mentioned
[1157.90 → 1162.34] that person from 10 years ago that was using react like maybe coming into it today would be like this
[1162.34 → 1168.76] feels very different right and I think I started at 0.12 0.13 like that's kind of when i when we kind
[1168.76 → 1174.06] of started using react in production, and you know we had a very innovative leader on the engineering
[1174.06 → 1179.96] side who was like very bullish on good tech and wasn't afraid of kinds of being on the bleeding edge
[1179.96 → 1184.74] and like you know even though that was very early like they were totally willing to kind of go all in
[1184.74 → 1190.66] on react uh and so Dan can you talk us through kind of React from 10 years ago to like where we are
[1190.66 → 1197.48] today right going from these components that were often used on the client right like specifically
[1197.48 → 1203.14] like they weren't always spas but like for the most part kind of going into kind of the server-side
[1203.14 → 1209.54] rendered revolution you know kind of fuelled by I think uh frameworks like Next.js, and then you know
[1209.54 → 1214.82] to kind of where we are today ushering in you know this kind of data uh fetching is a first class
[1214.82 → 1222.16] world with react server components so I can't yeah let me try to kind of recap the so what we're
[1222.16 → 1227.76] talking now about uh kind of paradigms of where we run the code right so not so much like the syntax
[1227.76 → 1235.44] but more just how we use computing resources and one way I like to think about it is like in
[1235.44 → 1241.10] in generally in app development but specifically in web development like in web development you always
[1241.10 → 1247.04] have to think about at least two computers right, so there's the computer you know the device that
[1247.04 → 1252.68] the user has so it could be their phone, or it could be like a desktop device you know it's like they're
[1252.68 → 1257.92] probably using the browser to open your app and then of course there has to be some other computer
[1257.92 → 1263.60] that actually sends the information to the user right so there has to be some kind of server
[1263.60 → 1270.98] you know that either sends HTML or JavaScript or both or some Jason and so the question is just like
[1270.98 → 1275.60] how do we use the resources of those of course there could be you know another computer earlier
[1275.60 → 1281.50] that maybe does the build, or you know when you deploy like somehow the code has to get from
[1281.50 → 1287.90] the developer's machine to that server, so there's also some kind of step of deployment and so the
[1287.90 → 1292.48] question is like how do we split you know the resources between these different computers and
[1292.48 → 1298.32] what do we actually make them do and so at the time when we just started using react I mean there
[1298.32 → 1304.30] were already different paradigms of how to split these resources so one very popular paradigm was
[1304.30 → 1311.48] kind of traditional server rendering uh unrelated like when I say server rendering I mean like PHP or rails
[1311.48 → 1321.02] where you mostly write your UI logic as uh stylish templates which you know you have some kind of
[1321.02 → 1327.56] uh control uh flow things like you have like loops conditions you have some kind of includes maybe so
[1327.56 → 1332.98] you can put one template into another template and that is happening completely on the server side
[1332.98 → 1339.52] so you're able to directly access any resources that are on the server so for example you can read from
[1339.52 → 1346.14] the database you can read from the file system of course you can also you know build a bunch of services
[1346.14 → 1352.42] and just talk to them by http on your server so that is something you can always do, but you're also not
[1352.42 → 1358.30] forced to do that if you know is it doesn't make sense for some task and so that that was kind of the paradigm
[1358.30 → 1365.28] but then within this paradigm it's pretty hard to build like very dynamic very instantly responsive user interfaces
[1365.28 → 1372.00] because if your UI logic is completely on the server then you have to talk to the server to get you know any
[1372.00 → 1378.80] kind of visual update and for some cases it's fine, but you know in like something like drag and drop interactions
[1378.80 → 1385.22] or gestures, or you know just like typing into an input and immediately like for example like filtering
[1385.22 → 1391.22] a list without going to the server uh stuff like this like you can't really express it in this
[1391.22 → 1396.96] paradigm very nicely and then that is where you know we started to shift in more work to the client
[1396.96 → 1404.98] where maybe you'd have some jQuery plugins that enhance the HTML you return from your server templates
[1404.98 → 1411.58] but that uh you know that let you add some instant interactivity where you know that the screen can
[1411.58 → 1417.98] update without a network round trip, and so I think that that was kind of like you know you could already
[1417.98 → 1423.00] kind of go extreme in either direction like already at the time right because like you could have
[1423.00 → 1427.98] everything that's like server rendered with something like PHP and maybe like a few jQuery plugins to
[1427.98 → 1433.36] just like enhance it in a few places, but there were also this approach of single page apps was starting
[1433.36 → 1439.86] to gain traction where you actually wouldn't send any HTML at all, and instead you would only send
[1439.86 → 1446.46] JavaScript and then the JavaScript would be kind of creating that you know initial HTML and managing
[1446.46 → 1453.48] that the Dom notes completely on the client and so the benefit of that paradigm is that you have the
[1453.48 → 1459.54] guarantee that you can always make an interaction instant so you have this guarantee that you know you're
[1459.54 → 1464.40] not going to get locked out of being able to like show immediate feedback because all the code is on
[1464.40 → 1470.26] the client and so all the code that's necessary to produce the UI is already available but then the
[1470.26 → 1475.22] downside of that is of course you have to download a lot more code kind of up front you don't show
[1475.22 → 1480.92] anything to the user while the code is loading so it's kind of bad for performance and it also
[1480.92 → 1486.46] complicates the mental model quite a bit because now you've had to move all the routing to the client you
[1486.46 → 1491.64] have to have some kind of caching for any data like you have to think about kind of state management
[1491.64 → 1496.84] like how long does this data live in which case does it invalidate like when is it okay to throw away
[1496.84 → 1502.46] so it's kind of like painful like differently but when react came out like these were kind of two
[1502.46 → 1509.12] popular paradigms and so react was used in both ways so for example at Facebook react was used more
[1509.12 → 1515.82] kind of in this like jQuery scenario where we'd initially use React for example like in the facebook.com
[1515.82 → 1522.22] web app react was used only like in the comments section of each post, so the entire page was server
[1522.22 → 1527.16] rendered with PHP, but the comment section was actually rendered with react and react kind of
[1527.16 → 1532.60] took over you know so that this particular piece can be instantly interactive whereas in the community
[1532.60 → 1538.68] I think some people adopted react like that whereas like other people already had single page apps
[1538.68 → 1544.04] with something like backbone or angular, and so they already had all their code on the client and so they
[1544.04 → 1549.58] started kind of replacing not like initially replacing just small parts of it uh with react but gradually
[1549.58 → 1556.38] because there is no you know it's not a server based paradigm you can kind of go all the way up and
[1556.38 → 1563.40] replace it with the React like completely, and so I think in 2015 or so react router got fairly popular
[1563.40 → 1569.66] so that that was I think like first kind of major like popular solution for routing fully
[1569.66 → 1574.76] on the client without you know going to the server to decide what the route should
[1574.76 → 1581.52] should show fully client-side paradigm and especially with you know when create react up came out it is kind
[1581.52 → 1587.70] of solidified this as you know this seems to be because like if everyone is running like all the server
[1587.70 → 1593.08] solutions are very different so you can't really like to release any tool chain that like addresses them all
[1593.08 → 1599.40] because it has to be custom anyway whereas if you're moving everything to the client like that's easier to kind of
[1599.40 → 1604.34] agree on that here's like the baseline of how these features could work and so create react app kind of
[1604.34 → 1609.80] made this approach even more popular because it became easier to start with you just you know you run it and
[1609.80 → 1615.48] you get yourself a spa I think you just answered a long question that I had Dan which is your know why
[1615.48 → 1621.46] when React was first released into the public like not necessarily internally why wasn't there a router
[1621.46 → 1626.76] you know and I think it's its obviously because Facebook wasn't using it that way right they were using it to
[1626.76 → 1632.52] kind of you know hydrate or like supercharge parts of their web app right but like essentially that's
[1632.52 → 1637.88] not how they were using it yeah yeah absolutely so that is yeah that is a part of the reasons like
[1637.88 → 1643.46] facebook generally doesn't release something that they are not themselves using and
[1643.46 → 1649.32] creator act app was an exception to that because creator act app was not used at Facebook at all but
[1649.32 → 1655.72] there was so much like frustration in the community about you know we have this like five different tools that
[1655.72 → 1661.72] need to talk to each other, and they're very like kind of finicky to configure and the idea with
[1661.72 → 1666.78] create react app was like it was it actually came out of uh like we were supposed to write a documentation
[1666.78 → 1673.54] page about setting up react, and it was just like it was embarrassing to write because it was like set up
[1673.54 → 1679.04] there's like five different tools and then like make this tool like talk to this it was very confusing
[1679.04 → 1684.48] and also like why it didn't make sense that like everybody has to every time each of these tools updates
[1684.48 → 1689.90] like everybody has to look for updated instructions so we're like okay let's just make a thing that
[1689.90 → 1696.40] that kind of hides them behind something that's like behind an abstraction level like the abstraction
[1696.40 → 1704.44] level kind of went up yeah and so that's how spas with react kind of became the norm I think but we
[1704.44 → 1711.16] already know like there are at least two or three problems there like in this paradigm so one problem is that
[1711.16 → 1718.24] we don't send any HTML on the initial load and that's just I think like when you don't know how
[1718.24 → 1725.68] to do it or like when there is no nice way to do it that's maintainable like I could kind of see it or
[1725.68 → 1732.34] understand it but I think like it, we figured out how to do it like we figured out good ways to do it
[1732.34 → 1738.80] that doesn't require you to write your code two times and for the first time with something like jQuery
[1738.80 → 1745.18] you know if you have like a jQuery combo box or like a drop-down or something you can't really
[1745.18 → 1752.98] produce HTML from it because the whole paradigm of jQuery is you operate on the Dom nodes so any UI
[1752.98 → 1758.60] logic is expressed as you take a Dom node you like change its attributes and so on so you can't really
[1758.60 → 1765.20] extract you know what is the initial render like what is the initial version of this UI you can't
[1765.20 → 1771.18] run some jQuery code and figure that out on the server but the thing that like was interesting
[1771.18 → 1777.00] about React was that because it's a function of state you could call that function with the initial
[1777.00 → 1784.88] state you get a tree, and then you can turn that tree into HTML, and so we had this like client-side app
[1784.88 → 1790.84] you know like it's its like conceptually client-side it's written for the client, but we figured out that
[1790.84 → 1798.70] actually you can run the client-side app on the server once per request produce HTML from it and
[1798.70 → 1804.78] then send the actual client-side program you know to the client so that it can boot up on top of that
[1804.78 → 1812.04] HTML and so that was the what's usually called SSR in like in the React paradigm it's just this ability
[1812.04 → 1819.20] to generate an initial kind of pre-rendered snapshot of the client-side app client tree but on the server
[1819.20 → 1825.00] so that's why it's called like server-side rendering, but it's really client rendering like pre-rendering
[1825.00 → 1831.02] the client on the server and there's like another variation of that that like next.js became
[1831.02 → 1838.42] like one of the popular kind of ways to like one of the first frameworks to do SSR in react although
[1838.42 → 1845.26] again like the ability to do SSR is provided by react itself right it's just reacted Dom slash server
[1845.26 → 1851.20] render to string that was like the initial API and then next.js was kind of like create react app
[1851.20 → 1858.84] but that that was designed around this idea that actually we already know how to pre-render the client
[1858.84 → 1865.36] tree on the server, but we might as well do that, and then you have this the other innovation it had was
[1865.36 → 1873.54] file system-based routing, so the idea was well in traditional PHP app if you go to you know pages
[1873.54 → 1879.26] slash about you only you know it has some script tags right like you're about that PHP or whatever
[1879.26 → 1884.58] it sends some script tags to the browser so you send different script tags like you have the ability
[1884.58 → 1891.68] to send a different client code depending on what page you're on and so in that sense the spa paradigm
[1891.68 → 1898.04] is a regression because now we send the code for all possible pages even though the user has actually
[1898.04 → 1903.52] requested a specific one so that's not really efficient and so the other thing that next.js did
[1903.52 → 1909.16] from the beginning was that unlike create react app where everything is sent as a single bundle
[1909.16 → 1914.60] or like you use bundle spitting, but you can only do this like once the code has downloaded in DJs there
[1914.60 → 1922.08] was like the components you used from the page would get sent as script tags you know in script tags for
[1922.08 → 1927.30] from those pages so code spitting was built in I was going to ask a question that I think you've like
[1927.30 → 1932.58] somewhat answered so like the whole SSR like remember like that function render to string right so
[1932.58 → 1939.40] ultimately like it wasn't the most performant and I'm curious like yeah was Facebook using that
[1939.40 → 1944.76] internally right because like i you know and if it was than like why wasn't the performance like
[1944.76 → 1951.02] more of a focus you know in subsequent releases just kind of like getting that down yeah so I think
[1951.02 → 1956.56] there's like a misconception in general when people talk about react performance because they a lot of this
[1956.56 → 1962.72] comes from kind of marketing you know like JS frameworks uh like benchmarks or something like
[1962.72 → 1970.58] this that runs uh like a tight loop with like one component level or like three component levels and that
[1970.58 → 1977.32] shows you it's kind of like looking at the microscope at like one tiny part of what actually
[1977.32 → 1983.88] executes whereas like in any real app most of the time is spent in executing the user's code like the
[1983.88 → 1990.16] code that you write your components and so the problem with render to string like you're absolutely
[1990.16 → 1995.14] right that there were performance issues with it but I think there's like a misconception that maybe
[1995.14 → 2000.26] these performance issues are just because like React was slow so let's just make react faster that's not
[2000.26 → 2004.92] really how it works because it's just a while loop like it doesn't it doesn't really do much you know
[2004.92 → 2009.86] it's its like a while loop that calls your components and concatenates them into a string so
[2009.86 → 2015.58] there isn't really much to optimize there uh the thing you could optimize is it's actually
[2015.58 → 2022.10] inefficient to well it's like about how do you sequence different things that the app needs to do
[2022.10 → 2028.76] so as an example like if you want your initial HTML to contain some data there is a question of like
[2028.76 → 2035.52] when do you kick off uh you know these data fetches so like do they happen during rendering somehow or
[2035.52 → 2041.64] do they happen ahead of time and typically because in react there was no support for asynchronous
[2041.64 → 2047.24] components or like there were no built-in asynchronous primitives you always had to do this
[2047.24 → 2054.10] if you wanted these data fetch you know results to be in the initial HTML you had to do them ahead of
[2054.10 → 2059.38] time so you had to do like a wait you know fetch or whatever and then render your tree which means
[2059.38 → 2064.86] you're not really using the computing resources of the machine because you could have started doing
[2064.86 → 2071.32] something, but you're waiting for all the data to be available before you start it so it's a sequencing
[2071.32 → 2076.68] problem and that is why like Facebook couldn't use even as Facebook started adopting so Facebook
[2076.68 → 2086.08] started rewriting their main app fully in react in 2017 maybe I'm I'm not sure 2018 like around the time
[2086.08 → 2093.30] and because render to string was synchronous like that was just a non-starter because for Facebook it's
[2093.30 → 2099.20] just the fact that you know a page is composed of many different things some of the things are going
[2099.20 → 2106.24] to be slower than others, and we can't wait for everything to be ready before we know emit all
[2106.24 → 2111.92] the HTML what we want to do is just stream it so we want to start rendering the components then if some
[2111.92 → 2118.30] of them are not ready we want to send some kind of loading placeholders or just hold the stream for a
[2118.30 → 2123.26] little bit and then when they're ready we kind of continue and we just emit more and more things
[2123.26 → 2127.76] in the stream and so you know answering your question of like why React didn't focus on that
[2127.76 → 2134.38] like React actually did focus exactly on this and uh but from these other perspectives so not from the
[2134.38 → 2138.96] perspective of like trying to make react faster because you just run into limitations of you know
[2138.96 → 2144.10] there's only so much you can do with the while loop but from the perspective of like how do we schedule
[2144.10 → 2151.30] the code written by the users you know of React so that we can stream as much as possible before we
[2151.30 → 2155.38] you know until we're blocked on some data that we just can't render something because we're
[2155.38 → 2161.16] waiting, and then we emit some kind of placeholders and so this is the suspense API where you can say
[2161.16 → 2166.72] like I want to send this like shimmer or a glimmer or like a loading state and then react will
[2166.72 → 2171.68] automatically send the rest later and so that that was streaming server rendering that's something that
[2171.68 → 2178.32] react 18 came out with and that Facebook had that was like without that Facebook could not have
[2178.32 → 2184.66] even moved to you know using react on the entire page, so this is fascinating to hear because
[2184.66 → 2190.32] it just I mean it kind of takes me back, and you know triggers some nostalgia, but also it's just like
[2190.32 → 2196.50] you know the data I'm going to use like this number so before PHP application 800 milliseconds react
[2196.50 → 2202.56] application 200 milliseconds and then finally we landed around like 40 milliseconds that was a win
[2202.56 → 2209.98] could it be some millisecond today yeah probably but at the time uh so it's an all the same data
[2209.98 → 2217.04] fetching existed so react was just the implementation detail of how were we going to make you know I think
[2217.04 → 2223.00] that UI as a function of state has done so much like heavy lifting in terms of like selling react
[2223.00 → 2228.46] and also like you know composing components and writing you know markdown with event handlers and
[2228.46 → 2233.10] everything kind of like together it just it clicked versus the progressive enhancement days of jQuery like
[2233.10 → 2237.24] you mentioned you know where you're primarily mutating Dom nodes, and you don't even know what it's
[2237.24 → 2243.10] you know even supposed to look like out of state 20 of 400 so whenever we got to 200 milliseconds
[2243.10 → 2248.38] the first actually I think open source library I wrote was called like react resolver, and it was using
[2248.38 → 2252.14] decorators at the time which are experimental, and they're that you know I'm actually had to remove
[2252.14 → 2257.20] from some old code on my job actually we had legacy decorators still in the code and like whoops got
[2257.20 → 2264.40] got to nix that, but anyway it effectively just wrapped components with you know hey fetch this API
[2264.40 → 2269.78] and then you can keep rendering and that's what got us to 200 milliseconds we were rendering the full tree
[2269.78 → 2276.56] synchronously whenever we hit basically that react resolver decorator it's like okay fetch the data
[2276.56 → 2280.66] you know there's going to be water falling, but we'll, we'll paralyze anything at the same time
[2280.66 → 2285.50] and then we're going to re-render the tree until we hit it again so like it was very inefficient but
[2285.50 → 2289.96] it's still four times faster than whenever we try to do it like with PHP and render the templates and
[2289.96 → 2294.24] everything finally we actually said well hang on do we need to fetch all this data right here
[2294.24 → 2300.06] and we took out some of the server side rendering, and we ended up rendering just basically the initial
[2300.06 → 2306.20] shell with like a suspense like spinner you know loader in the middle of the page and then the rest of it
[2306.20 → 2311.04] we fetched on the client and that's where the server was spending 40 milliseconds but in terms
[2311.04 → 2316.64] of the user experience it felt faster because now it was five times faster to actually see the code
[2316.64 → 2323.78] you know in front you know on your screen and so whenever I see react today it feels like all of
[2323.78 → 2329.42] the wild west paradigms and like you know hacks that I had to put together to get the experience I want
[2329.42 → 2334.80] of really taking all the data needs that never went away but I was just kind of moving on from the right
[2334.80 → 2339.54] to the left and then like you know threading them through different parts of the UIs to yield the
[2339.54 → 2345.36] best UX it just seems that like kind of overtime with the introduction of suspense that now it's like
[2345.36 → 2350.26] okay now there 's's first class primitives for me to use to get the behaviour that I had to hack
[2350.26 → 2356.14] around myself for so I would, you say like that's kind of accurate like these like what react is the
[2356.14 → 2363.76] react today compared to the React 10 years ago is to me honing in on web problems you the data
[2363.76 → 2370.00] fetching was always kind of there the latency across networks, and you know network boundaries and
[2370.00 → 2374.52] API calls was always there you know talking to the database was always there caching was always there
[2374.52 → 2379.82] where do you cache and how do you invalidate that stuff was always there what I see for reacting in the
[2379.82 → 2387.26] most recent like RSC discourse is we have 10 years of learning of people building you know going from
[2387.26 → 2392.42] counter examples which I personally don't find very helpful for illustrating you know the value of like
[2392.42 → 2396.76] frameworks anymore so I wish button counters disappeared unless its party kit showing a demo
[2396.76 → 2402.42] that's totally fine the party kit demos you know with like server side or like socket RSCS was pretty
[2402.42 → 2408.04] cool, but it just seems that like React is able to say like we can better serve this need with these
[2408.04 → 2414.68] better you know abstractions or paradigms or whatever, and also it's like it went from oh react
[2414.68 → 2419.90] doesn't have a router react isn't you bring your own router that sort of thing as part of that learning
[2419.90 → 2425.16] exercise and building more and more ambitious applications on react it seems that it became
[2425.16 → 2429.82] necessary for react to say well we got to work with bundler integration because you have to bundle an
[2429.82 → 2437.24] app today if you did a single page app yeah it made your React code base integrated everything
[2437.24 → 2442.78] was like co-located together it was all component driven it was instant from the UI, but it also ended
[2442.78 → 2447.44] up yielding like terrible dev experiences too and terrible user experiences because you started shipping
[2447.44 → 2451.98] you know 10 megabyte bundles as well so I see like the pendulum moving back and forth and as a result
[2451.98 → 2459.68] like new abstractions just had to arise as part of like that learning yeah I think so you jumped a
[2459.68 → 2465.84] little bit ahead to like server components which we know we do have to get to the topic at some
[2465.84 → 2471.40] point oh yeah we actually hold on dad before we like to respond to that I did want to kind of ask
[2471.40 → 2476.98] about the like uncanny valley right like that the problem where you know we send over this kind of
[2476.98 → 2482.22] serialized HTML that's like you know it looks intractable, but it's really there's still JavaScript
[2482.22 → 2487.86] that needs to be parsed um you know before that page is intractable and so like that was also like
[2487.86 → 2493.36] another issue that was like became a thing with server-side rendered uh like a lot of server-side
[2493.36 → 2499.14] rendered applications this wasn't specifically just a React problem right, and so I'm just curious also if you
[2499.14 → 2505.96] could kind of shed some light there and how RSC like potentially helps that yeah so where I do want
[2505.96 → 2512.22] to like to get to RCS just a little bit later because this is more like of a kind of history of I like
[2512.22 → 2518.16] Eric's framing of like we've learned for 10 years, and we actually took a step back and I think this is
[2518.16 → 2523.60] this is the point that's like maybe not coming across is that RSCS are kind of taking a step back
[2523.60 → 2529.02] from everything we've seen for the past 20 years and then kind of rethinking it like how could
[2529.02 → 2536.70] it works how do we apply all these lessons while having a component model, and so i I do like so
[2536.70 → 2542.08] far it kind of feels like we're keep stacking up like more and more you know complicated things to
[2542.08 → 2548.48] address issues but i you know I do feel like RSCS are also like a step back in like okay how do we
[2548.48 → 2554.18] make it simple again, but before we get to that so answering your specific question about like you're
[2554.18 → 2560.12] absolutely right there's this problem of okay if we do have a lot of JavaScript to send and we you
[2560.12 → 2565.14] know we send HTML, but then it looks like you know there's a button you click it nothing happens so this
[2565.14 → 2572.02] is something that was also a problem for facebook.com and this is like we kind of had a pretty long period
[2572.02 → 2581.44] of rethinking SSR and how SSR and this process of uh you know sending a pre-rendered app and then
[2581.44 → 2586.48] sending the code for the app and then having the code to the app kind of attached to that HTML so
[2586.48 → 2592.94] this is a process that we changed how it works in react and the key innovation there was also
[2592.94 → 2600.72] inspired by our old school PHP setup so uh there's this thing called big pipe which is like a technology
[2600.72 → 2607.66] Facebook used you know from 2010 or so like it, I think it was described in some blog post it's this
[2607.66 → 2614.18] idea of instead of sending all the code at once and even like all HTML at once you kind of send it
[2614.18 → 2620.96] in chunks because in HTML traditionally even if you stream it so like even if you send it as it becomes
[2620.96 → 2629.64] available streaming in HTML is depth first so you kind of have to stream each child after you know you
[2629.64 → 2634.60] kind of have to drill down into the tree as you're sending it but then if you have this problem where
[2634.60 → 2641.00] like for example maybe you have liked you serve a profile, and you have you know the profile feed
[2641.00 → 2646.20] you have the about section you have the photos section you have like events section something
[2646.20 → 2652.70] like this and let's say like the photos section is a little slow so in the traditional HTML model if
[2652.70 → 2657.84] it's slow you're like stuck on the server trying to send the HTML for it and like you don't have the
[2657.84 → 2663.68] data, yet you can't really skip over it like you're you're already in the HTML like you're you're kind of
[2663.68 → 2669.60] stuck there and then this idea that like Facebook used in its PHP setup was to have an abstraction
[2669.60 → 2676.06] that lets you break down the page into independent sections that were called pageless and each page let
[2676.06 → 2684.64] could have its own uh like data dependencies CSS dependencies JavaScript dependencies and the idea was
[2684.64 → 2691.10] to send it kind of breadth first so you kind of get the chrome of the page with this with the
[2691.10 → 2696.66] shimmers for pageless than like each page let can kind of you know stream in later, and it sends a
[2696.66 → 2701.52] little bit of glue code to just put it in the right place in the Dom and so it kind of keeps revealing
[2701.52 → 2707.20] like with nested like a train schedule you know like more data arrived let's let's reveal a bit more
[2707.20 → 2712.88] more like CSS arrived we're ready to reveal this piece and so this is something we integrated with react
[2712.88 → 2719.64] and this is what suspense is I mean suspense in general is just an API that lets you say this part
[2719.64 → 2725.72] of the tree if it's not ready show a glimmer or like to show a placeholder or like show like a spinner or
[2725.72 → 2731.44] whatever you specify so it's a very kind of designer concept it's like it's how designers think about
[2731.44 → 2736.94] loading states like they don't think about promises or the other fashion they just think about here's a
[2736.94 → 2742.46] part of the screen if it's not ready show this fallback here's like the fallback I designed and
[2742.46 → 2746.44] it's such a powerful concept because if it's declarative it means you can build technology
[2746.44 → 2752.80] that understands what to do if something's not ready and so like one thing you can use it for is
[2752.80 → 2758.08] is this kind of streaming where if on the server you encounter that like a piece is not ready you just
[2758.08 → 2763.20] you send the fallback and then you kind of load you know you send the rest of it later
[2763.20 → 2768.90] so this is this kind of how react solves this problem with like previously in traditional kind
[2768.90 → 2773.98] of server-side rendering solutions you had to download all JavaScript just for it to start
[2773.98 → 2780.12] kind of hydrating by hydrating I mean this process of attaching the event handlers and becoming
[2780.12 → 2785.96] interactive and so it kind of became like it had to become interactive in a single pass when all the
[2785.96 → 2792.50] code and all the data and all HTML has already been downloaded but with suspense, and you know you don't
[2792.50 → 2796.96] need to do anything special for if it's just you know it's just how it works if you specify the
[2796.96 → 2803.76] suspense placeholders around pieces of content that are maybe slower react actually hydrates it in
[2803.76 → 2809.04] chunks as well so it's able to kind of hydrate the first pass where all the things like outside
[2809.04 → 2815.32] you know photos and about and the feed become interactive than like as it gets a bit as a bit
[2815.32 → 2821.44] more code is downloaded like now it has the code for the feed composer so maybe you can like posts
[2821.44 → 2826.06] and all of this of course happens like you know within like something like 10 seconds so it's
[2826.06 → 2832.02] it's not about you know something super long-running, but it's just like chunked up so that it's able to
[2832.02 → 2837.74] do that in small parts yeah that makes perfect sense um I also feel like that's kind of a little bit
[2837.74 → 2844.24] of like the Castro islands uh like paradigm as well like you know where breaking things up into smaller
[2844.24 → 2849.20] chunks allows for kind of faster processing, and you know and better kind of prioritization of like
[2849.20 → 2854.60] what should load first etc, and you know just browsers are pretty fast at parsing JavaScript
[2854.60 → 2860.16] in general these days, but you know by chunking you're able to kind of like get shorten that time
[2860.16 → 2890.14] what's up friends I'm here with Conrad offerer from power sync is the
[2890.14 → 2895.04] sync layer that enables an offline first architecture to make your application real
[2895.04 → 2901.70] time and reactive comrade why is offline first local first a big deal right now for developers
[2901.70 → 2905.96] we're really excited about local first as a movement, and we think it's going to become the
[2905.96 → 2910.40] default architecture for a very large number of apps that are going to be built going forward
[2910.40 → 2915.90] just because it has huge benefits for both developers and end users so taking a step back just
[2915.90 → 2920.90] looking at what local first is so it's an architecture where your app code works directly
[2920.90 → 2925.18] with the client side embedded database which then automatically syncs with a back-end database in the
[2925.18 → 2930.42] background that's compared to cloud first apps where they mostly use a cloud data store via APIs
[2930.42 → 2937.10] that has some huge benefits for developers and end users having a local database and syncing with
[2937.10 → 2942.86] the cloud in the background the biggest benefit for end users is that everything in the app feels instant
[2942.86 → 2946.88] because the app is working with a local database, and you don't have to do round trips to the cloud
[2946.88 → 2951.74] there's no loading spinners everything can just load instantly it also means that the apps can be
[2951.74 → 2956.94] always available for the most part regardless of connection so even if the user goes offline the app is
[2956.94 → 2960.42] always available so like you said you know if you have a momentary lapse in connectivity if you're driving
[2960.42 → 2964.86] through a tunnel or if you're on the subway or if you're out in a rural area you don't have latency and
[2964.86 → 2969.30] the app can just keep on working and loading data out of the local database so this move to an
[2969.30 → 2975.90] offline first architecture what are the biggest benefits for developers the biggest benefit for developers is that it
[2975.90 → 2981.78] really simplifies state management, so state management is a headache for most apps developers typically work with
[2981.78 → 2987.28] some kind of state management library or framework there's a lot of kind of finicky aspects to it but with local
[2987.28 → 2995.30] first the global state is simply stored in the local database like a SQLite database and that really simplifies the app code
[2995.30 → 3000.96] it keeps your logic really simple and functional because your UI basically just reflects the content of the database
[3000.96 → 3005.02] so it just makes everything a lot simpler and then there are other benefits for developers too
[3005.02 → 3011.14] since you're working with data and logic locally your back end becomes simpler you have to do less API development
[3011.14 → 3015.18] on the back end you can shift a lot of stuff to the front end a lot of working with the data manipulating
[3015.18 → 3022.14] the data and logic, and they also reduce your back end compute load and compute cost and your dependency
[3022.14 → 3027.88] on the back end in general so it kind of takes the back end API off the critical path for the user using
[3027.88 → 3033.56] the application I like it very cool what's your goal with power sync our goal with power sync is to be
[3033.56 → 3038.38] framework-agnostic and eventually even back in database agnostic, but we already support flutter react
[3038.38 → 3045.48] native JavaScript for web apps Kotlin SDK is right around the corner our web SDK plays well with any
[3045.48 → 3051.06] JavaScript framework including Next.js yeah the goal is to be framework-agnostic, and we will also be
[3051.06 → 3055.18] becoming increasingly back end database agnostic so supporting additional back end databases not
[3055.18 → 3060.56] just Postgres but also Microsoft SQL server MySQL etc, but there's a ton of applications that can
[3060.56 → 3065.68] communicate with the cloud asynchronously where you can primarily work with a local database and
[3065.68 → 3070.72] therefore we think for the majority of apps local first will become sort of the default architecture
[3070.72 → 3077.58] okay the next step is to head to powersync.com slash changelog to learn more take your application
[3077.58 → 3084.80] offline first for free with power sync using their free tier no credit card required again powersync.com
[3084.80 → 3086.36] slash changelog
[3086.36 → 3095.84] so all of this like fun around server side rendering okay we have suspense and so where do we get to this
[3095.84 → 3102.58] like RSC how do react server components kind of come into uh fruition right like what problem are
[3102.58 → 3107.98] they I mean I think we've kind of maybe even set the problem up pretty clearly but I'd love to hear
[3107.98 → 3113.82] in your words like what problem are we solving by bringing this kind of data fetching as kind of first
[3113.82 → 3119.56] class as a React primitive yeah, so this is an interesting question because like I think we have this
[3119.56 → 3124.96] background of like here are things we've learned over the 10 years for example like one thing is like
[3124.96 → 3130.50] you want to be able to start doing the match report without waiting for like everything to finish
[3130.50 → 3135.78] like every previous stage to finish so you want things to be kind of like chunky you want to be
[3135.78 → 3141.68] able to like to send a part of the code and have like the rest load later and so on without waiting so you have
[3141.68 → 3147.08] like all these constraints of like what a good solution should look like another thing we learned is
[3147.08 → 3153.58] client server waterfalls are bad so you never really want a solution that forces you like you go to the
[3153.58 → 3158.54] server you get something back you start rendering it you're like oh I need to go to the server again
[3158.54 → 3164.18] you know like use effect fetch and use effect you're like go to the server again get something
[3164.18 → 3169.46] you continue rendering, and it's like oh we need to go to the server again it's just you know it doesn't
[3169.46 → 3175.88] it's its not efficient, but it's its how a lot of kind of single page apps end up working so we have
[3175.88 → 3181.04] all these constraints on what a good solution should look like but actually I like to think about react
[3181.04 → 3186.70] server components as you know not some kind of optimization, or you know not, not just some kind
[3186.70 → 3193.24] of like way to make things faster i kind of like to think about it as combining you know two mental
[3193.24 → 3198.68] models that have been pretty successful in the past like one is the traditional kind of request
[3198.68 → 3205.62] response mental model that we liked in PHP or rails where you know you're in the programming
[3205.62 → 3211.26] environment that has the data so you can easily kind of query it you can access it directly
[3211.26 → 3217.12] and then the other paradigm is traditional to react paradigm where you're on the client so you can
[3217.12 → 3223.04] instantly respond to interactions and so react server components kind of tries to answer the question
[3223.04 → 3230.44] what if you tied these two paradigms kind of together, and you could create components that span
[3230.44 → 3236.94] both of these worlds and as a concrete example you know it doesn't even necessarily require a server
[3236.94 → 3242.52] that runs JavaScript because you know another kind of thing we learned over those 10 years is
[3242.52 → 3249.14] if you have some code that's able to serve a request you can now also run that code during the build
[3249.14 → 3256.34] in some cases so that's that's how static generators like you know Gatsby or Jekyll in the ruby
[3256.34 → 3262.92] ecosystem work is that you can have a server but you have a tool that calls the server during the
[3262.92 → 3269.26] build with predefined file folders or slugs like for a block, and then you have the final product
[3269.26 → 3274.00] and then you can only you know it's enough to have a static server that just serves those files so you
[3274.00 → 3278.62] don't actually need to run a server and so react server components are kind of similar in that you know
[3278.62 → 3283.40] you could run a server with them, but you could also run them during the build if you're building
[3283.40 → 3288.20] something like a blog where you know ahead of time like what kind of routes you have and you just
[3288.20 → 3293.76] kind of pre-render them but I think the main thing that that's like important there is for example if
[3293.76 → 3301.30] I'm if I'm making a blog with react right like let's say I want to display a searchable list of my blog
[3301.30 → 3307.46] posts and let's say for example that I don't actually have like too many blog posts so I don't need to have
[3307.46 → 3313.30] like run a server that like executes the search I really want it to be like a local thing where like I have a
[3313.30 → 3320.00] text box I start typing into it, and it filters uh the kind of like a spa right like I just start
[3320.00 → 3326.96] typing and I already have the data it just shows the filtered posts, so the thing is in react i really
[3326.96 → 3333.76] want to be able to take things on the screen and make them into components so just like a designer
[3333.76 → 3339.70] thinks about the user interface like the designer doesn't think about server or client or like any of
[3339.70 → 3344.84] that jazz or like the designer doesn't care where the data is coming from they just say like here's
[3344.84 → 3352.08] an article here's a like a comment box or here's like a searchable list, but the problem is that in
[3352.08 → 3358.24] traditional react a searchable list that I described is kind of an impossible component because it depends
[3358.24 → 3364.94] on data from two different computers because it depends on the current state of the input so it depends
[3364.94 → 3370.08] on like what you've typed and like i as an author I just can't know that you know I can't know
[3370.08 → 3376.02] this ahead of time this is a computation on your machine, but then it also depends on the list of
[3376.02 → 3381.42] blog posts which is something that your computer can't know because that data is mine like I have
[3381.42 → 3387.26] to pass it to you somehow and so if you had is you had to write a component like this in traditional
[3387.26 → 3394.28] client-side react it would have to accept all blog posts as props so it would not be self-contained
[3394.28 → 3399.90] because it would need that data to be coming from somewhere so it's not really I can't really have
[3399.90 → 3405.24] like a block you know searchable block list component and like put it in two places because
[3405.24 → 3410.78] I would have to somehow plumb the data into it and so with server components the idea is that
[3410.78 → 3418.54] well what if you know the data could be coming from a parent component that just ran ahead of time
[3418.54 → 3424.96] on my computer so the component execution kind of becomes split where I can have like a component
[3424.96 → 3431.28] that runs on my computer that reads you know the list of blog posts, and it renders the component that
[3431.28 → 3437.34] will later run on your computer that does the actual filtering, and it's just a shift in mental model
[3437.34 → 3443.84] from when you like where is the data coming from because in traditional client-side spas and this model
[3443.84 → 3449.10] you kind of think of the data comes somewhere from the side you kind of think of like i write
[3449.10 → 3454.80] the component it does some kind of fetch you know and like the data is it like waits for something
[3454.80 → 3460.00] but with server components the mental model is kind of like well the data is just coming from a parent
[3460.00 → 3467.44] component that already ran like on the server or during the build so it's like the data always comes
[3467.44 → 3472.56] from above yeah so I think this is where I get a little confused Dan so you're saying that like
[3472.56 → 3477.22] the data comes from a parent component that calculates it ahead of time but like how do you
[3477.22 → 3481.92] how do you calculate it ahead of time i I mean you know if it's dependent on input that you get from a
[3481.92 → 3486.68] user I think that's a little yeah so you can imagine for example if I'm talking about like
[3486.68 → 3493.24] searchable blog posts component right what I do is I split it in two, so there is kind of like a
[3493.24 → 3500.26] boundary between them in react server components is it's called use client directive, but you can kind of
[3500.26 → 3505.84] think of it as being similar to a script tag, so there's this stuff inside the script tab you know
[3505.84 → 3510.86] that's the component that will run on your computer and then there's stuff outside of it that's like
[3510.86 → 3515.70] the stuff that runs ahead of time so maybe like one way to think of it is like you can imagine
[3515.70 → 3522.46] if this is PHP and jQuery instead of you know react on both sides then they have the PHP side that
[3522.46 → 3529.34] you know does like enumerates the folders in my blog, and then you know it would render a script
[3529.34 → 3535.32] tag with my jQuery code and pass some data to it, so this is kind of similar except you don't think
[3535.32 → 3542.76] in script tags at all it's just you kind of like write a component that does await FS.reader to read
[3542.76 → 3549.32] the files on you know on the server or during the build, and then you just say return your other
[3549.32 → 3554.52] component that is able to do the filtering and has you state in it, and you just pass block posts
[3554.52 → 3560.50] equals block posts to that component and then in the child component you just have all the block
[3560.50 → 3566.72] posts as props so you can filter them, and you can use state there so you kind of like think about it in
[3566.72 → 3572.98] in isolation here is like the first pass and here is the second pass yeah I'm not sure if this like
[3572.98 → 3577.94] is too abstract but yeah no, no i that's definitely not too abstract and I think it's syncing in a little
[3577.94 → 3583.14] bit more but yeah go ahead Eric, and we can kind of come back so you know being on like the know
[3583.14 → 3590.28] this reacts uh journey for so long it's that was the synchronous nature of React was the thing that i
[3590.28 → 3595.22] kind of thought that like initially I understood it you know whenever you have you know in my mind it
[3595.22 → 3600.20] was like okay if you as a function of state then you probably want this thing to you know be straight
[3600.20 → 3604.46] in straight out sort of deal you know introducing promises yeah as we learned from like the stately
[3604.46 → 3608.06] team you know it's like okay now you have like this whole complex state machine that you're going
[3608.06 → 3613.44] to deal with like with error states and everything but whenever I saw an async component within a weight
[3613.44 → 3618.96] for like data fetching it clicked for me because that's always how I expected it to kind of work
[3618.96 → 3624.52] and it just took you know basically years of like workarounds and basically wrapper components
[3624.52 → 3629.10] to effectively accomplish like what I was already trying to accomplish you know like within my code
[3629.10 → 3633.20] you know I mentioned react like resolver before but then like what kind of ended up happening is like
[3633.20 → 3638.52] we'd have a use effect doing a fetch and that component effectively turned into like the spinner
[3638.52 → 3643.52] loader component on the server whenever we rendered and spat it out and then like it finally actually
[3643.52 → 3650.76] did the fetch on the client so like to me seeing like async was the async component usage was that
[3650.76 → 3656.00] something that you know that started working because of RSCS or is it something that you know
[3656.00 → 3661.20] became supported because of suspense like what architecture allowed there to be an asynchronous
[3661.20 → 3666.22] component because it still requires because the async nature does there need to be a suspense boundary
[3666.22 → 3671.58] above anything that's you know an async component within a weight on the inside yeah so we currently
[3671.58 → 3677.06] only I mean in the future we might support some version of uh async components on the client too
[3677.06 → 3684.96] but currently it's only supported yeah in the in server components and I think like a big reason for
[3684.96 → 3692.24] that is avoiding performance uh foot guns because again the like what do you expect on the client in
[3692.24 → 3698.26] general is that you inspect uh instant interactions right so you expect that when you change some state
[3698.26 → 3703.42] we're immediately able to respond with some kind of you know some kind of feedback to the user
[3703.42 → 3710.54] and so if you could put arbitrary like async components into the tree then we don't we can't really show
[3710.54 → 3718.56] a new consistent tree until they have executed so that might introduce delays and so the way server
[3718.56 → 3725.04] you know the server components paradigm solves this problem is that all the async stuff actually happens
[3725.04 → 3731.88] ahead of time like on the server or during the build so you never have this issue where you change some
[3731.88 → 3738.86] state, and then it gets stuck because it's like it's waiting for something on the client like it's more
[3738.86 → 3744.52] like a request response model where all the server components output is already pre-computed by the
[3744.52 → 3749.74] time you know you get the page for like from your kind of client perspective they don't even exist like
[3749.74 → 3755.76] you only kind of see the props that they gave you so you just have props from somewhere you
[3755.76 → 3759.88] don't really kind of know where they're coming from and then if you do a navigation like that's where
[3759.88 → 3765.84] we do a refetch and on navigation we can, you know load the output of server components again
[3765.84 → 3772.22] for like the next page or for like a refresh of the data but again all the async stuff kind of
[3772.22 → 3777.68] executes on the server and then when you get it on the client it kind of feels synchronous so you can
[3777.68 → 3782.26] you know you just read them from props you don't really like think about like waiting for something
[3782.26 → 3787.28] got it yeah because on the server you don't have a consistency problem you know it's its really only a
[3787.28 → 3792.24] single state that ever gets rendered and that state comes from I guess it's instead of like a function
[3792.24 → 3798.04] of state equals like the UI is it like a function of the request yeah, yeah maybe a way of thinking
[3798.04 → 3803.28] about it on the server yeah it's yeah it's kind of like a function of URL and I mean you can also
[3803.28 → 3808.84] think of it like it's function of data in the sense of just like your kind of read state on the client
[3808.84 → 3814.12] like sure it's coming from React but kind of conceptually just like read something that's you
[3814.12 → 3819.58] know some memory on your computer that's state whereas like some memory on the server that's kind of
[3819.58 → 3825.08] data it's probably like something from the database or something from a file read, or even you know result
[3825.08 → 3830.86] of like fetching from microservices, but they don't have to be exposed to the client computer so it's
[3830.86 → 3836.06] just like UI is a function of data, and it's its kind of like UI is a function of both it's just
[3836.06 → 3841.72] executed in two stages like first all the stuff that depends on the data executes on the server
[3841.72 → 3847.32] that output gets sent to the client and that's your normal react tree that works as usual
[3847.32 → 3853.26] got it yeah and that's for me that's what where it clicks Dan like, so essentially there's a
[3853.26 → 3860.10] remote call that's executed from the client that's like go pre-fetch go pre-calculate these things
[3860.10 → 3865.82] right like go render out this part of the tree, and then you know based on these inputs and then
[3865.82 → 3871.50] send that back and that computation is done in the server, and so I think that's the piece that I needed
[3871.50 → 3875.20] to hear because you know you mentioned like the stuff happens ahead of time, but it's really when you
[3875.20 → 3880.10] say ahead of time it's really ahead of time of the page like fully rendering right like I mean like
[3880.10 → 3886.12] yeah it's just when you're like in the client first mentality you kind of think of the client code as the
[3886.12 → 3890.80] beginning of the world right it's kind of like this is where my program starts so you kind of
[3890.80 → 3896.28] like think oh like if I need data I need to like call for it, but the thing is like this client program
[3896.28 → 3902.96] was already sent by another computer server yeah, yeah so that all the data stuff could have just
[3902.96 → 3908.52] happened there and be inclined into the stuff that gets sent to you and that's how traditional kind
[3908.52 → 3914.04] of server-side rendering worked is like if jQuery plugins needed some data PHP could put that data
[3914.04 → 3920.08] into the page right so it kind of extends this idea that another way to think about it is it's its kind
[3920.08 → 3926.12] of like sending JSX over the wire almost except of course for first load you also want to send HTML
[3926.12 → 3932.44] but it's kind of like if you had one API endpoint and the only thing that API endpoint could do is
[3932.44 → 3938.54] return like give me a JSX for the next page and that's what it kind of responds with yeah and
[3938.54 → 3943.86] that's like really smart because it's your able to kind of do more with less you know like, and we're
[3943.86 → 3950.16] able to do earlier and leverage this like hidden server right like that we don't really
[3950.16 → 3956.78] think about a bit more efficiently definitely that, and also it lets you think in components so is kind
[3956.78 → 3963.20] of breaks down this you know like I have because usually you think of this as like two processes
[3963.20 → 3969.34] that are completely unrelated like prepare all the data prepare like you know deal with some state
[3969.34 → 3976.06] but like in this like filterable list example you know it's like specific data and specific state
[3976.06 → 3981.60] I needed to render an UI, and so I can kind of compose these components together and now I can
[3981.60 → 3987.12] have this filterable list component that I can just like render in different parts you know on different
[3987.12 → 3993.62] pages if needed with different props like you know I can, I just use it as a React component but if it's
[3993.62 → 4000.74] able to kind of access both the data you know from the server and the client part is able to access the
[4000.74 → 4005.94] the state and that kind of stuff so it's about full stack components that are composable
[4005.94 → 4010.52] you you you said something I thought was actually interesting is that like paraphrasing beside to
[4010.52 → 4014.86] the effect of you know when we see a component you know we see like a client component is like the
[4014.86 → 4021.62] start of it or start of the world or whatever and RSCS I think clicked for me because you know it was
[4021.62 → 4027.18] always starting on the server you know static generation to me was like an optimization of like
[4027.18 → 4032.24] well okay I'll just perform that first request on the server and cache it and write it out so like
[4032.24 → 4038.14] it always kind of clicked I think a lot of React developers came in at the single page app time
[4038.14 → 4043.16] and you know where it was all I mean I'm I'm working on an app today that's like I think the code base
[4043.16 → 4051.04] goes back six plus years with like react router three and so whenever we see that do you think that
[4051.04 → 4057.66] that client first sort of experience history or mentality is a reason why there was like a knee-jerk
[4057.66 → 4063.60] reaction to you know await dB SQL call or something like why are you doing a SQL call on my code I can't
[4063.60 → 4068.38] remember how long ago this happened but like the fact that a React component could access the database
[4068.38 → 4074.20] within the component seemed to like to spark some FUD do you think it was that kind of like client first
[4074.20 → 4079.82] mentality that allowed that sort of mentality to take place yeah I mean I think it's definitely I mean
[4079.82 → 4086.78] part of it is like sure like using SQL insider component on a conference slide like yeah you're gonna you
[4086.78 → 4091.04] know you're going to make some people mad that's just you know it is kind of a troll move a little bit
[4091.04 → 4096.62] but I got the point across right but I think like sometimes it is feels like maybe it gets the
[4096.62 → 4103.06] wrong point across because people have an expectation when they see react code that it executes on the
[4103.06 → 4108.54] client and so if you see react code doing like a SQL query you kind of think of like is it calling SQL
[4108.54 → 4114.16] from a client a lot of people for example like one of the misconceptions about RSC is that people think
[4114.16 → 4119.94] that it mixes client side and server side code in the same file so that actually never happens that's
[4119.94 → 4125.10] like something we don't allow specifically because it's very hard to understand like that's something
[4125.10 → 4131.14] that current solutions do sometimes like next pages router mixes server and client code in the same file
[4131.14 → 4137.80] remix mixes server client code the current version of remix does that but like in the future you know with
[4137.80 → 4144.72] like eventual uh hopefully like adopt a RSC we'd like to move where we never do that so like in
[4144.72 → 4150.78] the RSC model we never mix server and client code in the same file but I think yeah the knee-jerk reaction
[4150.78 → 4155.56] is partially just because when you see something shaped like a React component you think that it's
[4155.56 → 4161.26] something that has to execute on the client but I think it's kind of like uh you know like in the
[4161.26 → 4167.58] matrix movie uh where like neo realizes actually like the world is not real it's created from another
[4167.58 → 4172.68] world I think that's kind of like a similar you know if you're like client-centric like you write
[4172.68 → 4177.96] a component but like what do you think sent this component to the browser like there was a piece of
[4177.96 → 4184.40] code that did that where whether it's like a static file server or like an actual server that like
[4184.40 → 4189.08] emitted the script tag like there was some code that's responsible for your component getting there
[4189.08 → 4195.44] so what if you had full control over that code and what if you had a component model for that code as
[4195.44 → 4201.00] well so that you could write components that kind of span both worlds and that are able to you know
[4201.00 → 4206.84] pass data, and then you can reuse them yeah so Dan like what's fascinating like for me about
[4206.84 → 4213.52] better digesting this kind of paradigm is like there's this shift away from like you know what we
[4213.52 → 4218.78] would traditionally do to like to make a request to go get some Jason and then like you know take that and
[4218.78 → 4223.70] like rehydrate our apps right, and you see this also with uh HTML right with where they do this
[4223.70 → 4230.42] transfusion right they kind of skip that whole Jason serialization steps uh you know so but it is this
[4230.42 → 4236.94] very much feels like that but like with reacts uh primitives right so like how do we now just like
[4236.94 → 4242.72] skip a bunch of steps and just make data fetching first class build it into like the component
[4242.72 → 4248.72] and like give you a way to do that in a more efficient way like that that's kind of what's
[4248.72 → 4254.60] clicking for me yeah yeah I think philosophically it's kind of funny that HTML is you know HTML is
[4254.60 → 4260.46] it's like what if HTML had a component model right like HTML doesn't really have a component model because
[4260.46 → 4267.06] on the server you're expected to write templates that they made HTML stuff and then like HTML has like a
[4267.06 → 4272.12] bunch of attributes that kind of specify some client side behaviour so what if like you took
[4272.12 → 4278.70] you know HTML attributes they're kind of like angular 1.x directives so like what if we just
[4278.70 → 4283.34] turned that into react components and that would be the client side and then what if we took the
[4283.34 → 4288.80] templates that they made to HTML yeah and what if we turned that into react components and that will
[4288.80 → 4294.16] be server components yeah yeah and so now you have kind of React on both sides, and it always like the
[4294.16 → 4300.84] model is just it executes in two stages the server stuff executes first that produces the JSX that
[4300.84 → 4305.88] gets sent to the client and that's where state updates happen and so state updates can always be
[4305.88 → 4311.86] like instant because this is the part of the code that only depends on state and then the components
[4311.86 → 4318.42] that also depend on data that is the stuff where you know you do like a router refetch or server action
[4318.42 → 4323.84] or like you do like one of those things that are kind of triggering you know a refresh
[4323.84 → 4330.16] and then that sends you know that re-executes the components on the server that are necessary
[4330.16 → 4336.94] that sends JSX and because it's not sending HTML you know it can be turned into HTML that's what we do
[4336.94 → 4343.20] for first render but for kind of next navigations we actually don't we just send the tree itself
[4343.20 → 4349.48] and so this for example enables you to have animations between these trees, or it's kind of like
[4349.48 → 4354.70] just receiving new props like you're like well I guess like I got new props I can, you know react
[4354.70 → 4361.20] re-renders it without destroying the Dom so it's just a way to get props from the server okay so if
[4361.20 → 4366.34] we're looking at like the network right so if I have the network tab open like what am I seeing
[4366.34 → 4372.92] here using RSCS this is very interesting i think it's like it's fascinating how it works
[4372.92 → 4379.76] so I'll first talk about the case of navigations after the first load because first load is special
[4379.76 → 4385.04] because for first load we have to send HTML as well so that kind of like you know it has this like
[4385.04 → 4389.90] a program inside a program like we want to have the snapshot that the browser can display immediately
[4389.90 → 4394.98] because of course the browser doesn't understand like React's custom format but then for navigations
[4394.98 → 4400.48] we don't need HTML because we don't want to replace you know inner HTML and like lose all state so
[4400.48 → 4405.06] we actually just send the React tree so conceptually you can think of it as like what you're going to
[4405.06 → 4411.98] see is kind of like a juice x tree but in a different format so one way to think about it is
[4411.98 → 4418.78] so if you take a tag right like a DIV you can write it in HTML so you can write it you know
[4418.78 → 4426.06] angle brackets DIV, or you can write it as Jason so you could say like a type colon string DIV like it
[4426.06 → 4431.02] has to be a string right like we need to tell what kind of what kind of element it is and then if it
[4431.02 → 4437.44] has some attributes like you could say like type DIV props like class name something right so that's
[4437.44 → 4443.64] like a Jason object and so you can think of a React component tree or like actually like as a Dom tree
[4443.64 → 4449.48] like you could think of it as sending it as this like turning it into Jason right so you could say
[4449.48 → 4456.32] like type DIV props children a something and that would be like an anchor tag so you can kind of
[4456.32 → 4462.52] think of HTML as being expressible in like Jason format then the next thing is sometimes you know
[4462.52 → 4468.46] you also want interactivity and like client side code so you need to specify you need the client to know
[4468.46 → 4474.44] where to get that code right kind of like in HTML this is solved with a script tag so in HTML you just
[4474.44 → 4479.88] have like a script tag with some file name and then the browser will download it and like in our
[4479.88 → 4486.26] format it's kind of embedded into the tags so you could have you know type DIV which is a built-in one
[4486.26 → 4492.90] or you could have like type counter except wait like counter like it's not enough to send a string
[4492.90 → 4498.44] right because the browser doesn't know what the counter is so really we send an object that says source
[4498.44 → 4504.10] you know the URL to the script so it's the same as script source it's kind of like where to
[4504.10 → 4513.42] download that code from and the module ID so like counter is maybe module number 20 in main.js or like
[4513.42 → 4519.50] chunk something.js and so this just tells react oh here's how I download this code for the counter
[4519.50 → 4524.20] and this is why like react server component needs a bundler integration because we need a way
[4524.20 → 4531.38] to ask hey bundler go fetch the chunk and give us the counter component from it and so then react can
[4531.38 → 4537.84] use it so you really kind of see this tree that's you know kind of like HTML tree, but it's in Jason
[4537.84 → 4544.98] and it has built-in elements like strings, and it has kind of references we call it a client reference
[4544.98 → 4550.58] which is really just an object that says here's where to download the code for this component here's
[4550.58 → 4557.28] which chunk it's in and then the last part that's kind of important is we don't send it as Jason you know
[4557.28 → 4562.52] kind of as a normal depth first Jason object because that has the same problem I described
[4562.52 → 4567.64] earlier of like you have to your know drill down so instead of its kind of like Jason with holes
[4567.64 → 4573.30] where sometimes you just have like a hole that says like a hole number zero like hole number one
[4573.30 → 4578.76] and then the protocol actually sends them line by line, so there's like here's the hole number zero
[4578.76 → 4584.28] here's the hole number one and so this lets us like progressively show that tree and then the parts
[4584.28 → 4588.42] that are not ready the suspense boundaries you can have your own suspense boundaries that show
[4588.42 → 4593.98] fallbacks and so this lets us stream even if some data fetches are slow this lets us send as much of
[4593.98 → 4599.56] the tree as possible as early as possible and keep kind of streaming in the rest wow so we basically
[4599.56 → 4605.74] solved the problem that meta had or Facebook had right facebook.com had many years ago yeah this is
[4605.74 → 4611.18] fascinating and so you know this is like a good time to kind of ask about the bundler topic because I think
[4611.18 → 4616.86] one of the things I keep reading about is that oh well this you know react server components allow
[4616.86 → 4622.68] you to send up like less JavaScript to the client right like which I think is like fantastic um and
[4622.68 → 4627.90] because we're doing some of that compute off the user's machine right so we can kind of keep
[4627.90 → 4633.32] the JavaScript that's needed for that off the user's machine right like duh um can you talk about
[4633.32 → 4637.70] some of that a little bit that's like such a fantastic side benefit like I don't know if that was
[4637.70 → 4643.24] like the intended goal but like if or if that was just like a happy side effect but like I'm here for
[4643.24 → 4650.44] it either way um so yeah i think that's you know there's like a theme here is like I think
[4650.44 → 4655.82] like a React early on it's built on a very simple idea right like UI is a function of state and here
[4655.82 → 4662.74] it's kind of like React is a like UI is like a function of data and state that's partially applied
[4662.74 → 4667.60] over the network you know that that's like a super computer science way to say it but like
[4667.60 → 4672.54] it's just like a program that executes in two steps and the know the intermediate result
[4672.54 → 4678.12] of the first step is being sent and because conceptually this is a very simple idea and you
[4678.12 → 4683.18] know you could think of like PHP plus jQuery app is also it's a program for two computers but these two
[4683.18 → 4689.18] parts can't really like talk to each other in some well specified way, and we say no there is a way
[4689.18 → 4695.62] to talk to them one of them passes props to the other one that is how they communicate and so i
[4695.62 → 4701.70] think like you do get a lot of happy accidents from this model just by kind of the way it works
[4701.70 → 4706.90] like you said yes like it lets you send less code to the client because a bunch of logic could just
[4706.90 → 4712.34] you could run it ahead of time and this is maybe where like a comparison to something like Castro is
[4712.34 → 4718.30] very appropriate where if you think of like Castro templates they kind of serve the same role as
[4718.30 → 4724.48] server components like they execute ahead of time uh so you can, you know like on my blog I have this
[4724.48 → 4731.56] funny feature where I show the colour of my blog posts it's kind of like a gradient so like from
[4731.56 → 4739.62] older to you know from newer to older, but the gradient is adjusted by how recently I posted so you can see
[4739.62 → 4744.10] here are the recent posts because they're like in the brightest colour and then the old posts are like
[4744.10 → 4749.60] kind of closer to the end of the spectrum, and so i use a library that has the dust colour
[4749.60 → 4756.18] interpolation uh for that but because I do this while generating the posts I just do it on the server
[4756.18 → 4763.04] and I pass the interpolated colours as props to my components so I don't need to actually
[4763.04 → 4769.14] yeah but then if I wanted to your know like I could just move one line into the client component and now
[4769.14 → 4773.84] this library would be on the client, and now it would be able to respond to interact like if this
[4773.84 → 4778.78] was like an interactive colour picker then it would make sense to run it on the client this kind of
[4778.78 → 4784.22] this ability to like to shift things back and forth that is fascinating and the other thing that
[4784.22 → 4791.26] I think is maybe less well known but is actually also pretty valuable is not only we can send you know
[4791.26 → 4795.98] some code now we don't need to send to the client at all because it just you know runs ahead of time or
[4795.98 → 4802.06] like on the server but also for the code that we do have to send to the client we don't have like
[4802.06 → 4808.62] one giant bundle that's like always the same, and we don't even need to like I mentioned earlier like
[4808.62 → 4815.00] Next.js router uh kind of did the split by the route so like you send the code that's used by a route
[4815.00 → 4821.30] but with server components a bounder is able you know this is kind of more theoretical like current
[4821.30 → 4826.54] generation bundlers don't take advantage of this variable but in principle you only need to really
[4826.54 → 4833.30] send the code uh that's actually used you know that's necessary for the current request or like
[4833.30 → 4839.10] for a current page because this is another thing that like at Facebook was very important that if you
[4839.10 → 4845.22] send the code for the feed you don't want to send like the client code for all possible story types
[4845.22 → 4850.88] because there's like maybe like a hundred of them or if you're doing like a markdown you know if you're
[4850.88 → 4856.56] doing like a blog with uh client side examples in different pages you don't want to send like
[4856.56 → 4862.62] all the client code whenever you visit the blog like you actually want to send the code that's used by
[4862.62 → 4868.64] the current page and so because we execute server components execute on the server, and they return
[4868.64 → 4874.92] client components, and then you know the script tags are only sent for the chunks that are actually
[4874.92 → 4881.34] used by the output so that's like kind of like automatic like code splitting that's, and you don't even
[4881.34 → 4885.66] like need to write you know like dynamic imports or anything it's just it kind of falls out of the
[4885.66 → 4891.20] paradigm oh okay wow that's that is so cool what a really cool side effect yeah it makes sense like
[4891.20 → 4898.00] because a React server component could also have client components nested within it and like we don't
[4898.00 → 4903.14] really need to even process we don't need that chunk until we get you know until we're at the
[4903.14 → 4909.86] step of the interaction right so that's awesome, and so I mean like obviously this is gonna
[4909.86 → 4913.74] be a silly question now because I think we've really beat this topic to death right, but you do not
[4913.74 → 4918.50] need a quote-unquote server to use React server components right like this is like a pretty big
[4918.50 → 4924.30] misconception and this is because we're able to use the server that's used to kind of literally serve
[4924.30 → 4930.82] your app right so um so i I think there 's's kind of like different ways to look at it, you know
[4930.82 → 4935.90] there's like using react server components through the full where you like take full advantage of the
[4935.90 → 4941.44] paradigm and in this case it does make sense you know some things are just easier to do when you
[4941.44 → 4946.78] actually run a server that can run some JavaScript code, but there's kind of like you can take away
[4946.78 → 4953.40] different things from the paradigm because really like I think maybe the biggest misconception I think is
[4953.40 → 4959.04] people think of React server components as like somehow changing react or like it's like a because
[4959.04 → 4964.30] you get dropped into a different world by default it's like you're gonna you know when you write like
[4964.30 → 4970.88] a RSC app you get dropped into the server world first which is kind of like an Castro template but it
[4970.88 → 4976.74] looks like your familiar client world, and you're like why can't I use an event handler here like I expect
[4976.74 → 4982.12] to write the counter component I can do it and like it forces you to actually like you need to step into
[4982.12 → 4988.06] the client world to do that stuff but when you start on the server like you can do like file system
[4988.06 → 4994.54] reads or database and stuff like this, but again it's kind of like RSC is an extension of the React
[4994.54 → 4999.94] programming model so it's kind of like it's not like a replacement it's just here's the client react
[4999.94 → 5007.24] that we knew and here is like a complement to it here is like the other side that you can add and you
[5007.24 → 5013.52] choose how much of that side you want to add, and you also choose at which point it runs because if
[5013.52 → 5019.42] it runs you know if you want to have a completely static file server like with spas than of course
[5019.42 → 5025.16] you can't run any JavaScript code at request time, but you could run some at the build time and so this
[5025.16 → 5030.86] is this is kind of generalizing what static side generators have been doing except with react paradigm so
[5030.86 → 5037.38] you know this is what lets me write a blog that does FS. Read and then I specify generate you know
[5037.38 → 5044.56] the server component output for this list of pages because these are like pages on my blog and then i
[5044.56 → 5052.00] get like the build product is a bunch of JS a bunch of CSS and a bunch of HTML files and just a bunch of
[5052.00 → 5058.80] this pre-computed like Sony things that you know the client can download on navigation so that it
[5058.80 → 5064.86] doesn't blow away the state of the page it's kind of like Jason essentially right, but it represents
[5064.86 → 5070.08] rectories, so there's something you can totally do, but then you know if you want to take it and like
[5070.08 → 5076.22] you can kind of think of every spa as almost like it's kind of like a valid RSC app with a single
[5076.22 → 5082.32] server component that just returns you know the existing app so it kind of like falls into the
[5082.32 → 5087.62] model as well of course there's like nuances about routing like you can't really take advantage of it
[5087.62 → 5092.18] without the router being on the server side because you don't know what page is being requested
[5092.18 → 5097.50] to clarify you said there needs to be there like a bundler integration is required to kind of make
[5097.50 → 5103.14] all this magic happens and work right so like what bundlers are supporting this and like today
[5103.14 → 5109.84] yeah and what's what's on the roadmap yeah sure so I think this is also not exactly true it's like more
[5109.84 → 5115.98] again for it to be used you know to get like all the kind of benefits is designed like in principle
[5115.98 → 5122.94] like in theory you know uh you could have like an integration that puts all the client code into a
[5122.94 → 5127.78] single file and then like the bundler integration could be very simple because then
[5127.78 → 5134.12] you know it would just concatenate all client side code, but that's not really efficient the reason we
[5134.12 → 5139.66] need a bundler integration is because we've introduced this concept of directives, so there's use client and
[5139.66 → 5145.24] use server they don't actually mark client and server components this is one of the pieces where like
[5145.98 → 5153.02] is introducing misconceptions they kind of mark the doors between the worlds so use client kind of
[5153.02 → 5159.94] marks its kind of like a script tag it's like the rest of the imports from this point uh you know any
[5159.94 → 5165.32] code imported from this file is going to get into a bundle, so use client is kind of like an entry point
[5165.32 → 5170.72] like here's where the script tag starts and then anything imported from that is going to be in the
[5170.72 → 5176.86] know in the script tag and then use server is not for components it's kind of like a door into the
[5176.86 → 5182.32] server it's if you actually run a JavaScript server it's only useful in that case it's not useful
[5182.32 → 5189.56] for data generation, but it's where you mark an endpoint, so your server is kind of like here's server code
[5189.56 → 5195.06] that's callable from the client and so if you use something like RPC that is pretty popular these days
[5195.06 → 5201.26] it's a very similar idea it's just instead of writing fetch post on the client and then like
[5201.26 → 5207.62] request on post here I'm going to run this function you just import the function and if it has this
[5207.62 → 5213.82] directive it means react will give you like an async thing you can await, but it will actually post
[5213.82 → 5219.36] to that endpoint, and it's just a way to call functions so this is like the kind of features
[5219.36 → 5225.30] where you do the same things you could do like with PHP and jQuery right like you can send the
[5225.30 → 5231.28] script tag with a bunch of stuff and then later you can like call arrest like http post but really
[5231.28 → 5237.70] these two things are represented as imports so it's kind of like your PHP it's like if your PHP site could
[5237.70 → 5244.66] import a jQuery component and render it and then if your jQuery component could import a PHP endpoint
[5244.66 → 5250.30] and like you know post to it so this kind of integration is required a bundler so the question
[5250.30 → 5255.72] I have about like the, so the bundler integration makes sense right and these new um you know use
[5255.72 → 5260.42] server use client directives you know I like how you kind of put if it's like you know you can see
[5260.42 → 5264.86] use client and think of it as like a script tag you know it's kind of like a know just a point
[5264.86 → 5270.48] where things where the bundler will split off when I was migrating from the pages' directory of next.js
[5270.48 → 5274.80] to the app directory one of the very first areas that kind of pops up is like oh you're using
[5274.80 → 5281.14] like react to use state that should be a client component add this directive so why is the use
[5281.14 → 5287.14] state you know the React client side kind of primitives not sufficient of a heuristic to go off of
[5287.14 → 5292.24] because it seems that like early on when people were moving to the app directory they basically just
[5292.24 → 5296.68] searched their code base everywhere they had to use state import or use effect they would put use
[5296.68 → 5301.94] client at the top, but that's not right either is it yeah I mean you can do it this way it's just
[5301.94 → 5307.96] kind of painful way to migrate I think they now have it in the docs that the recommended way to
[5307.96 → 5314.50] migrate is you just take your entire you know pages directory you know in the pages directory the way
[5314.50 → 5320.10] it was structured is you had this like get server side props so get static props, so this is like the part
[5320.10 → 5325.70] of the file that executes on the server only, and then you have this like page component in the same file
[5325.70 → 5331.42] so you were previously you were mixing server and client for code in the same file and so in the app
[5331.42 → 5336.94] directory kind of the recommended migration is that you take this page component you move it to another
[5336.94 → 5343.72] file so that that is kind of your start of your existing tree you put use client at the top of just
[5343.72 → 5348.86] that file you don't need to add it to any other files you just put it into your kind of entry point
[5348.86 → 5355.56] and then your get server side props that is what now becomes a server component so server components
[5355.56 → 5361.88] are really kind of like in Next.js they serve the same function as get server side props in the
[5361.88 → 5368.70] old Next.js as like Castro templates it's just like this part that executes first and so you really
[5368.70 → 5376.22] need use client only in client components that are imported from a server component it's like the place
[5376.22 → 5383.70] where things turn into Jason it's like where if you pass props down they will become you know Jason get
[5383.70 → 5388.16] passed over the network, and then they will be revived so I think that that is kind of like how
[5388.16 → 5394.86] to think about migration is that you don't I think people think of it as a per-file kind of intuitively
[5394.86 → 5400.84] they think oh I need to open all files and put use client on the ones that are client but it really
[5400.84 → 5407.36] it's more like you have the entry point into your import tree so you have your like page component or
[5407.36 → 5412.22] something like this you put use client on top of that and that's actually enough and then maybe later
[5412.22 → 5418.12] you kind of pull some things out of it you know like maybe you have some data fetching deep down
[5418.12 → 5423.58] that you're like oh actually I'll just do this fetch above in the server component and I'll pass the
[5423.58 → 5429.58] result as a prop and so you kind of gradually can pull some things out of it out of the kind of client
[5429.58 → 5435.36] part to the top, but you don't need to like to add directives everywhere is there a reason why being
[5435.36 → 5439.88] tightly integrated with the bundler is there not an opportunity for bundlers to kind of like skip the
[5439.88 → 5443.74] directive part I mean except the use server from the client but like you know the
[5443.74 → 5449.10] render on the server and the very first time you hit an interactive client component which we know
[5449.10 → 5454.76] to have like use date or use effect like isn't that so isn't that the equivalent of you going in and
[5454.76 → 5460.96] saying use client so like is there like an opportunity to basically have engineers and react you know
[5460.96 → 5465.80] authors like to do less work and have to think about I guess like the paradigm less and just
[5465.80 → 5470.72] and the biggest shift is just going from client centric to just like you know starting on the
[5470.72 → 5475.26] server and then the interactivity is already built into react and the bundlers just needs to be a little
[5475.26 → 5480.64] smarter yeah no this is a great question and it kind of gets at some of this like kind of philosophical
[5480.64 → 5486.98] issues where you know there are things we've learned and one of those things is that actually
[5486.98 → 5493.78] being intentional about where the boundary is valuable because like we there were attempts to do
[5493.78 → 5501.38] like something that spans both worlds like sp.net web forms uh meet early meteor, and you know there
[5501.38 → 5507.14] were like attempts that try to treat server and client as this thing that's like there is really no
[5507.14 → 5513.84] boundary, but it's not really the right abstraction because the boundary exists it's the network boundary
[5513.84 → 5520.92] and so you want to know at which point what exactly are you sending and where is the point where you
[5520.92 → 5526.10] know I pass some props down, but actually they get turned into Jason, and later they'll get turned
[5526.10 → 5532.38] back from Jason and I want to be intentional where that happens both because that's you know you need
[5532.38 → 5538.42] to be aware of like sometimes maybe you're sending like a huge object and if you just did this like a
[5538.42 → 5544.14] couple of layers of hierarchy above you could just send a little bit of information instead of
[5544.14 → 5550.28] like letting it explode into this object so it's kind of like you know in Castro again like there's a
[5550.28 → 5555.98] separation between Castro templates and client islands and that it's a good separation because it lets you
[5555.98 → 5562.32] decide like which world do I want to put things in and in principle you know I think what you're asking
[5562.32 → 5567.90] for is like well could the bundler decide if there's like you state in this component and like
[5567.90 → 5574.30] automatically insert his client there, but then the problem is like not all components actually deal well
[5574.30 → 5580.14] with their props being sent over the network so you kind of want to be intentional like here's where
[5580.14 → 5586.00] I make the cut, but you also want to be able to move that boundary very easily so in this case it's
[5586.00 → 5591.00] like you just copy and paste it and move it to another file so it does take a bit of learning to
[5591.00 → 5597.50] like you know it is requires building like a little skill that is comparable to the skill you have to learn
[5597.50 → 5604.12] if you're writing like a PHP plus jQuery app or Castro plus react app like the skill is always there it's
[5604.12 → 5610.00] about where to make the cut except you can reuse code between both sides now because they compose
[5610.00 → 5614.56] because it's a single programming paradigm that's just such an excellent point because that being able
[5614.56 → 5620.96] to move the boundary you know it's its not so much that something like has state in it is that you can
[5620.96 → 5626.32] even float it a little bit higher too so you're in control over where that script tag kind of happens and I think
[5626.32 → 5632.20] that you know react has always done a good job of like thinking of escape hatches you know as part of
[5632.20 → 5636.66] just you know out of the box like you know not everything's going to work you know as a React
[5636.66 → 5641.48] component so we need to be able to escape out to like the rest of the world and be like a good citizen
[5641.48 → 5646.94] so knowing that some things some props are going to be serializable or whatever and being able to
[5646.94 → 5651.84] basically not get stuck to where you can't even adopt it you know, but you can just move that boundary
[5651.84 → 5657.16] that's that's really helpful to understand so that distinction between the two of it you know
[5657.16 → 5662.88] it almost reminds me like a webpack two days of like doing an async import and that becoming a
[5662.88 → 5667.92] code split boundary that is actually how it's so we had a kind of and actually going back to email's
[5667.92 → 5673.62] question because I haven't answered it, but there was a question about like what is the state of support
[5673.62 → 5679.72] for bundlers and kind of circling back to that it is actually very hard to retrofit
[5679.72 → 5686.12] this into existing bundlers because again it's like a conceptual shift of a bundler spanning
[5686.12 → 5691.98] kind of two applications except that they can reuse code between them, but it's two separate module
[5691.98 → 5697.94] graphs like in the for example if you're like in PHP world you can't really expect to like access
[5697.94 → 5703.72] you know modules from the jQuery like they're separated by this when you're inside the matrix you
[5703.72 → 5710.22] don't have access to like you know the food from I don't know if you watch the movie it's like two
[5710.22 → 5715.52] separate worlds you can bring stuff from the outer world into the inner one, but you know you can't like
[5715.52 → 5721.34] you need to be diligent about how to cross it and so the first thing we released you know in 2020 we
[5721.34 → 5728.34] when we released the first kind of specifications for the uh reactor recovered RFC which has changed
[5728.34 → 5734.82] so we did a few revisions in response to the first framework that adopted was hydrogen uh Shopify hydrogen
[5734.82 → 5740.06] and it was actually like it ran into a lot of problems that like some of them were known some
[5740.06 → 5745.44] of them we just didn't have a solution yet, and so they ended up abandoning it but they's actually
[5745.44 → 5751.86] their feedback that led to the directives because before that it was file name extensions but uh we
[5751.86 → 5758.78] together with our first kind of uh spec we also wrote a toy version of a plugin for webpack it's
[5758.78 → 5763.16] very slow so like it's not you know production usable because again it's its very hard to
[5763.16 → 5769.32] kind of retrofit it into a bundler that was not designed for thinking of like server and client as
[5769.32 → 5775.34] two separate programs that have doors into each other that that is really like the new paradigm here
[5775.34 → 5780.76] is just you have two separate programs, but they have these doors and like one kind of door is like
[5780.76 → 5788.32] render a tag with props and the other kind of door is like colon async post callback so they were not
[5788.32 → 5794.70] designed for this, but we did write like a super kind of simplified version of the webpack plugin and it
[5794.70 → 5800.94] actually internally used the same mechanism that webpack uses for dynamic imports because what we need is
[5800.94 → 5807.22] just like we need to create these chunks for you know like each use client we discover is like a
[5807.22 → 5813.82] potential split entry point so which yeah we just needed to create those files, and it's like a
[5813.82 → 5820.58] level you know it's like ideally if there's demand for this paradigm and if people really see its benefits
[5820.58 → 5826.44] you know we're kind of like skating like RSC is very ambitious and that it requires some features and
[5826.44 → 5832.64] bundlers that don't exist, and the idea is like we can kind of try to polyfill them with like plugins which is like
[5832.64 → 5837.50] what next is trying to do, but it's super convoluted, but this is also why they're like RSC is invested
[5837.50 → 5844.06] into turbo pack so turbo pack is designed for this like ability to have this like split worlds that
[5844.06 → 5850.98] talk to each other, and you know parcel is also designed for like this being extended like having
[5850.98 → 5857.80] this ability to have a combined graph from like two different isolated worlds so I think like as this
[5857.80 → 5862.54] paradigm becomes more commonplace the hope is that the next like maybe it's the person listening to
[5862.54 → 5867.60] this podcast like the next generation of bundler developers will treat it as a first class feature
[5867.60 → 5872.02] and like I don't know maybe like in 10 years it'll be a standard like dynamic import became a standard
[5872.02 → 5877.18] that's kind of like where we'd like to uh I think get to eventually but for now it's this like
[5877.18 → 5882.62] you know like webpack introduced require. Insure before dynamic import it's kind of like similar
[5882.62 → 5888.28] well yeah I mean this so I was going to ask about linting because like i I'm very curious to kind of
[5888.28 → 5893.18] get your thoughts on like if custom linting rules are going to help kind of wrangle that
[5893.18 → 5898.36] like use client use server kind of all the directives right like and kind of enforce
[5898.36 → 5901.90] best practices there but I feel like now I have a more interesting question
[5901.90 → 5909.76] around the bundler so I don't know can you maybe quickly answer my linting question yeah yeah okay
[5909.76 → 5915.84] so for the linting we actually we want to fail at build as early as possible so it's not even just
[5915.84 → 5921.66] like linting we actually like if you import we use this thing called import conditions which lets you
[5921.66 → 5927.84] run like specify that you're running code in like a different environment so react when the import react
[5927.84 → 5935.50] in the server world in the server RSC environment your state doesn't exist it's not and it's its not even
[5935.50 → 5940.54] just like it refuses to work it's like conceptually it's not even an export react doesn't export your
[5940.54 → 5946.54] state in this environment so it's its similar to like how you can't invert jQuery in PHP world it
[5946.54 → 5951.82] just doesn't make sense we want to fail early, so this is like the level of kind of protection we have
[5951.82 → 5957.78] now is we just like force you to add this direct like you can't forget about them because we're going
[5957.78 → 5962.74] to force you to add them but one thing that's missing is like type enforcement so one thing we want to do
[5962.74 → 5970.00] is if you mark a component like component file with use client we want typescript to enforce that all its
[5970.00 → 5975.56] props must be serializable so it shouldn't be able to like to accept functions, and you know things you
[5975.56 → 5981.26] couldn't pass from the server, but you can pass a server reference you know like a server action because
[5981.26 → 5985.82] it's not really a function it's like you know it's actually an object just specifying how to call it
[5985.82 → 5991.62] so I think like types enforcement will actually I think it will help explain the paradigm because when you see
[5991.62 → 5996.70] a type error you're like oh I see what's going on here like these things have to be like I'm crossing
[5996.70 → 6002.78] the network boundary that's why it's saying that there's like a mistake like listening to you talk
[6002.78 → 6008.32] about what role the bundler plays and how it's like a completely different paradigm from the way we've
[6008.32 → 6014.36] been bundling today because there's kind of two resolution graphs and whatnot it kind of like it's
[6014.36 → 6019.78] making more and more sense to me why you know next was really the first on the scene with kind of
[6019.78 → 6024.66] like being able to support this right they have the infrastructure they have the engineering power
[6024.66 → 6029.72] they have the all the things right they've got all all the pieces in place but at the same
[6029.72 → 6034.06] time like was it kind of somewhat of an unfair advantage that like they got there first like i
[6034.06 → 6038.18] don't know I'm just curious to hear your thoughts yeah so, so next was not the first integration the
[6038.18 → 6044.12] first integration was Shopify hydrogen next was experimenting with server components for a while but it
[6044.12 → 6050.22] didn't really it didn't really you know move to what we've seen like in the next 13 release until
[6050.22 → 6057.74] like maybe a year after when Sebastian has so when Sebastian left Sebastian is the person who led most of
[6057.74 → 6064.26] the design of modern react so he came up with hooks and with much of the design for server components as
[6064.26 → 6072.92] well and so this started in I think if I'm not mistaken 2017 with an internal post that is maybe has a
[6072.92 → 6079.02] spicy title uh what comes after GraphQL uh not in the sense of you know we're not like actually like
[6079.02 → 6083.68] you know Facebook is using GraphQL pretty heavily obviously doesn't want to actually like to replace it
[6083.68 → 6088.72] but it's just this idea of like if we have to write these clients that like download all the data
[6088.72 → 6094.76] download all the code and then apply the code to the data you might as well like to do some of that work
[6094.76 → 6099.44] on the server and that's how like a Facebook that was a pretty kind of normal thing because
[6099.44 → 6104.90] previously Facebook kind of started as a server rendered up with a server component paradigm called
[6104.90 → 6110.78] HP so it didn't really use like MVC like rails it was more like react components except they executed
[6110.78 → 6117.62] on the server and so it was kind of like that was like one of the ideas like GraphQL HP and Next.js
[6117.62 → 6123.50] would get server-side props like all these ideas kind of combined yeah, so the problem was like
[6123.50 → 6128.76] we wanted to deploy server components at Facebook and kind of start which is also you know they're
[6128.76 → 6133.44] hard to incrementally adopt because you kind of like have to adopt it from the top instead of from
[6133.44 → 6138.90] the bottom so like with server components if you have an existing app than the kind of the pathway
[6138.90 → 6144.06] to adoption is not that you like rewrite small parts of that app in server components it's more like
[6144.06 → 6150.24] you wrap your entire app, and you put the server components layer before them which maybe just like
[6150.24 → 6155.00] renders your app so it doesn't do anything, but then you can like start moving things a little bit
[6155.00 → 6160.54] into that world like from the client-centric world and so at Facebook this was not unfortunately
[6160.54 → 6167.42] possible due to technical limitations of how our PHP and JavaScript like you know we were running like
[6167.42 → 6173.42] a custom JavaScript engine it was not v8 the way it was communicating with PHP is like very different
[6173.42 → 6178.54] from how it's usually set up, but it's like most companies in open source, and so we were kind of faced
[6178.54 → 6184.84] with this choice of we know how to make this work like we have a solution for a bunch of issues that
[6184.84 → 6189.38] you know we've had for a long time we think we have something novel we think we have something that's
[6190.00 → 6195.92] like combines you know the best side of kind of client server paradigms like PHP plus jQuery or like
[6195.92 → 6202.56] Castro plus react or like it has liked it's kind of it has this like old characteristics you know like
[6202.56 → 6208.34] things we've learned over the 10 years of like you know streaming and like sending less code but also just
[6208.34 → 6213.06] full stack components this ability to write components that are encapsulated and span both
[6213.06 → 6218.72] worlds so we have this thing and we just you know we can't keep developing it because like meta is
[6218.72 → 6224.12] like Facebook was kind of stuck because of the custom bundler custom JavaScript engine custom setup
[6224.12 → 6229.32] between the server, and you know that, and it was already very optimized so it was kind of like
[6229.32 → 6235.42] in the local maxima and then the team that I'm not like assigning blame or anything, but it's just like
[6235.42 → 6240.94] we needed help from the team that maintained the custom you know all this bundling infrastructure
[6240.94 → 6246.62] at Facebook and that team was actually busy because they were all put on the like end-to-end
[6246.62 → 6252.92] encryption project for messenger and there was no nobody who could you know drive this kind of big
[6252.92 → 6259.84] you know technical redesign of like how all our data fetch and fashion works and so the choice was
[6259.84 → 6265.48] like do we sit on this technology for several more years just because meta is stuck or do we go
[6265.48 → 6272.82] somewhere else to complete it, and so we didn't want to sit on it and so uh Sebastian left meta and
[6272.82 → 6280.04] the question was like where can he complete the vision like, and you know the ask there is pretty big
[6280.04 → 6288.64] it's like develop a new generation bundler bet on this completely unproven technology and YOLO
[6288.64 → 6296.28] so the thing that you know with oversell it's oversell has kind of invested into just you know
[6296.28 → 6302.50] trusting Sebastian's direction so when Sebastian came to the Next.js team basically like on the first
[6302.50 → 6307.36] week he was like we're going to rewrite everything because you know we need to throw like these
[6307.36 → 6312.50] abstractions don't quite work anymore and like we need a new bundler we need like all these things
[6312.50 → 6319.22] need to be new and so that is like a very big bet to make for a very successful product like next was
[6319.22 → 6325.16] and you know next is paying the reputational cost and like oversell is paying the reputational cost for
[6325.16 → 6330.12] yeah let's just try this completely new thing that's like unproven and let's prove it out
[6330.12 → 6336.46] kind of in the fires of shipping to production and that's usually the process that you know if you're
[6336.46 → 6342.32] like consuming react from outside that's the kind of process that happened at Facebook so like you
[6342.32 → 6348.56] know when React was developed like you didn't see that process because uh you know it is like by the time
[6348.56 → 6353.86] it was open source it was already pretty solid so you didn't seem like you know the early React but
[6353.86 → 6359.10] this is kind of like seeing that process play out in the wild and yeah I think the biggest thing is
[6359.10 → 6366.28] just oversell was able to you know allocate a bunch of you know many full-time engineers to work it's
[6366.28 → 6372.66] like 10 maybe 10 people to work on this full-time for several years for something that's not proven
[6372.66 → 6380.72] because they believe in Sebastian's vision essentially and I think that's and like it, you know like parts
[6380.72 → 6385.04] of it are still kind of rough but I think it's getting to a place where it's actually getting really
[6385.04 → 6389.06] usable and proving itself out yeah that makes sense he said it really well
[6389.06 → 6394.30] too he said you know for history revisionists I went to for sale and change Next.js I didn't
[6394.30 → 6399.56] change react the React stuff was already there pretty much, and so i I think that's like really
[6399.56 → 6405.96] interesting so with Next.js being not so much you know the first one or like early
[6405.96 → 6410.40] adopter, but you know helping to like refine and dog food it, and you know and actually put the
[6410.40 → 6415.18] resources behind it to make it a reality is this going to be competitive you know first mover
[6415.18 → 6421.04] advantage for Next.js that or will like remix are they having to play catch up will other bundlers
[6421.04 → 6426.78] like well basically this is a very much a React thing but has to have that buy-in is this going
[6426.78 → 6432.38] to kind of create like a bit of a moat around Next.js because of their investment in it that
[6432.38 → 6437.86] others might not be able to immediately catch up to yeah I mean I think realistically that is the case
[6437.86 → 6443.72] currently I think not for technical reasons so you know it's its kind of unfortunate in the sense
[6443.72 → 6450.94] that technically like the work is layered very carefully so that you know all the parts that are
[6450.94 → 6456.52] not Next.js specific they're in react so there's like every feature is developed in a way like even
[6456.52 → 6461.70] things that people think are somehow associated with Next.js over sell like they're they're kind of
[6461.70 → 6467.56] layered in a way that wherever there is leverage by putting it into react so that like other
[6467.56 → 6473.82] frameworks can build around the same concepts, or you can make you know you can put a component on NPM
[6473.82 → 6479.12] that would work in any framework that adopts RSC like that that is kind of the goal of this you
[6479.12 → 6484.94] know why RSC why not just call it Next.js well because like we want we don't think there's you
[6484.94 → 6490.02] know these concepts are actually specific to a framework it's just the concept of splitting the file
[6490.02 → 6495.12] between the two worlds or like not the file but like splitting the know the modules between
[6495.12 → 6501.50] the two worlds and I think realistically currently it's just the team barely has time to document
[6501.50 → 6507.78] all the user face and stuff so documenting all the know like what is the like for example
[6507.78 → 6513.36] like for the wire format we don't document it because we provide the reader and the writer for this
[6513.36 → 6518.50] format they're in the React repo they're not in Next.js repo so like in principle anyone can use them
[6518.50 → 6523.40] but you just have to you know you have to know like which folder they're in and like what the API is
[6523.40 → 6528.48] and you can look at the tests like the tests are also there, but we don't just nobody has infinite
[6528.48 → 6534.22] time when like things are on fire and right now everything is on fire because people are starting to
[6534.22 → 6539.06] use it, and they run into all the bugs they run into all the missing features, and you know the top
[6539.06 → 6544.74] priority for the team is obviously just to make sure that this paradigm survives which means just like
[6544.74 → 6550.88] making it usable for end users but I think it's like things kind of we have you know yes like
[6550.88 → 6556.72] framework authors are kind of poking at playing with it now that there's some kind of knowledge
[6556.72 → 6561.64] that you know we have a group like we've had a group for a while internal for framework authors
[6561.64 → 6567.70] where they can just ask questions and like we try to reply as fast as possible but I think really
[6567.70 → 6573.52] the thing that will take it to you know the next level where you know people don't feel like there is
[6573.52 → 6579.38] some kind of like unfair advantage it's just there needs to be a bundler that supports this so that
[6579.38 → 6585.12] it's easier you know you take the bundler you take the React parts of this thing and you just you know
[6585.12 → 6590.80] you go wild with it and until that exists it's just like it's much harder to experiment because you have
[6590.80 → 6595.36] to either write a bundle plug in yourself which requires a lot of specialist knowledge I don't even
[6595.36 → 6601.08] know how to do it so it's yeah currently it's kind of you can only do this if you're willing to like
[6601.08 → 6607.32] invest months into understanding how to make the bundling work, but then you know with parcel
[6607.32 → 6613.14] adding support that's like close to built-in or like a plugin that's like really kind of fits into
[6613.14 → 6619.60] the architecture with turbo pack hopefully getting stable and hopefully being usable outside next
[6619.60 → 6625.16] years I really hope they make it like usable as standalone by but keep the support for directives
[6625.16 → 6630.02] I think these things will help it kind of propel more into mainstream because then people will be
[6630.02 → 6634.68] able to play with it and if you can just like you know just like fire up a node server and just
[6634.68 → 6639.96] like call this function and see you know see the output I think that's where people feel like oh i
[6639.96 → 6644.84] understand how this works I understand where the boundaries are so I don't feel like this is specific
[6644.84 → 6651.18] to next years but I think realistically it's true that just you know there is some you know proximity
[6651.18 → 6657.72] to if you take the burden of trying things out first then you also like to reap the benefits of
[6657.72 → 6664.12] kind of you do have a solution first yeah I mean i I think first I just want to say thank you
[6664.12 → 6669.60] so much for this incredible backstory in history uh Dan because I think you know it I think at least
[6669.60 → 6674.68] for me anyway I empathize with kind of oversell taking the heat right and like you said like they're
[6674.68 → 6680.10] taking the reputational cost and Guillermo has been someone who's like always made big bets on the web
[6680.10 → 6686.38] right like, and he's obviously someone who cares deeply about the web, and so I'm like wow like respect
[6686.38 → 6692.90] for like investing in this like and taking this big bet on RSC and like putting literal like
[6692.90 → 6698.70] cash money behind it, you know so but I mean like that's I can also see like I can see you know there
[6698.70 → 6703.34] is an of course a commercial angle in the sense of course and I think it's sometimes maybe
[6703.34 → 6710.72] misunderstood as like I think the angle there is kind of similar to the apple angle of like vertical
[6710.72 → 6716.30] integration, but it's its also a bit different because it's like all open source so it's kind of
[6716.30 → 6724.36] like I think the idea is what if you designed the architecture with kind of deployment model in mind
[6724.36 → 6729.56] and that is something that you know at a place like Facebook that's obviously how it's going to be
[6729.56 → 6734.88] you know like you have a whole team of infra engineers you know they will think about like how do we
[6734.88 → 6741.32] distribute work between like our data centres and our you know how do we cache things at which layers
[6741.32 → 6746.04] do we cache things and so on and then like smaller companies can't really like to afford to think about
[6746.04 → 6753.22] this and like Sebastian is like an architecturally minded person like cares both about
[6753.22 → 6760.06] you know how do we design it in a way that it doesn't run into the walls that we've seen over these 20
[6760.06 → 6766.94] years we know like PHP without caching will run into a wall like you know client side only will
[6766.94 → 6772.66] run into a wall graph kill only will run into a wall so it's kind of like designed like how do you
[6772.66 → 6779.02] design the paradigm so that it can be like distributed in a good way and then oversell is kind of like we're
[6779.02 → 6784.60] looking for a paradigm that can be distributed this way because we're actually a solution for you know
[6784.60 → 6789.62] distributing computation so this kind of fits perfectly so I think like that that is kind of the
[6789.62 → 6795.12] interest in like they want the paradigm that's able to full take full advantage of their of like
[6795.12 → 6799.44] the infrastructure they're building so it makes sense like that they want something that's that's
[6799.44 → 6804.90] like designed in mind yeah of course I mean you know it's also just like from an open source
[6804.90 → 6809.92] sustainability perspective like open source is sustainable when you align it to business incentives
[6809.92 → 6817.68] quite frankly like uh just real talk you know so just no hate there at all you know I there's just so
[6817.68 → 6822.18] much that we didn't have a chance to get into you all we have been talking for like forever I'm gonna
[6822.18 → 6828.04] like wrap with just a couple questions, so the name react server components because this is we talked a
[6828.04 → 6832.70] little bit about the community FUD right and some of the misconceptions and whatnot but like
[6832.70 → 6836.84] you know do you feel like if you could do it all over again would you pick with like would you
[6836.84 → 6841.76] Dan Abrams like right like you don't speak on behalf of everyone on the team but would you Dan
[6841.76 → 6847.30] ember off call it something other than react server components given the amount of confusion that
[6847.30 → 6853.06] this is ensued in the community I didn't see a better term I still haven't seen a better term I think
[6853.06 → 6860.52] it's its one of those cases like in react where we you know it maybe it is a bit arrogant but we kind
[6860.52 → 6867.78] of redefine what the term means because you know like with rendering like maybe it's unfortunate but
[6867.78 → 6874.26] like we needed a word and like in react rendering means just computing you know the UI not like
[6874.26 → 6879.80] painting it to the screen but uh it's just something we now people kind of use that word
[6879.80 → 6886.48] in the React sense and I think it's just one of those cases where we're I think we're staying true
[6886.48 → 6893.24] to the conceptual meaning of server and client because it's two programs one program sends the
[6893.24 → 6900.30] other program to like potentially another machine there is potentially like distance between them so
[6900.30 → 6906.74] the boundary has to be you know serializable and yeah kind of one program serves the other program
[6906.74 → 6913.74] but it's just you know it doesn't map exactly to the physical concept of like server and client because
[6913.74 → 6919.38] well like a server can be like a client to another server and so like it's like we just have to be you
[6919.38 → 6925.06] know like if I were to reintroduce this concept that maybe kind of talk about what we mean by the
[6925.06 → 6932.18] server and the client it's just like you know this server is the part that runs first and that returns
[6932.18 → 6939.90] you know the client part that runs second, and they can run but as we talked earlier right like even like
[6939.90 → 6946.94] 2016 like people already figured out you could take the client program run it on the node.js server
[6946.94 → 6951.98] and to produce initial HTML so like we've already put the client on the server before
[6951.98 → 6956.70] and then with something like Gatsby like there was like an insight oh actually you can run the server
[6956.70 → 6963.48] itself ahead of time during the build if you know all the requests you want to hit so we also put the
[6963.48 → 6969.00] server into the build or like a deployment, so these concepts are already kind of muddied and
[6969.00 → 6974.12] in the form the point of React components it makes sense this component kind of serves
[6974.12 → 6979.38] this other component so to speak so I think the name is still right we just had to explain what
[6979.38 → 6984.46] we mean by the name yeah yeah no that's great I'm proud of you for sticking with your guns Dan that's
[6984.46 → 6988.42] fantastic we could have just started a whole new rumour on the show you know maybe I just don't have
[6988.42 → 6995.22] I just don't have the imagination like maybe I'm just I doubt it I doubt it um and so Dan if people
[6995.22 → 6999.40] are like all right well you know as you're you know this better than I do you know the circle of
[6999.40 → 7004.92] people who use React is much larger than the people who use Next.js right there are tons of people
[7004.92 → 7010.04] who use next but like the React community is bigger than the next community and so
[7010.04 → 7015.14] and so you know for folks who are like oh I mean where can I get started where am I looking like
[7015.14 → 7020.62] what are official docs that I can be using and leveraging right like the rollout on this has
[7020.62 → 7025.32] been very unusual like compared to some of the other releases that we've seen from the React team
[7025.32 → 7030.66] right and so and of course there's been big shifts in the team itself right, so this is like now
[7030.66 → 7035.86] we have people from outside of meta that are part of core you know and I feel like as a result of that
[7035.86 → 7042.06] like there's more work in the certain parts of the sausage are being done in the open or being done in
[7042.06 → 7049.64] different places so i I'm curious like how do folks like actually get started on this at this point
[7049.64 → 7054.16] and like and then also like is there anything that we could have done, or you would have done
[7054.16 → 7059.72] differently with the rollout of this feature just given the FUD and confusion that folks seem to
[7059.72 → 7066.20] have yeah I think like in terms of getting started i you know realistically I just think next currently
[7066.20 → 7074.06] is the most complete kind of implementation of the vision so if you want to get like an idea of how it
[7074.06 → 7080.72] was kind of designed to work at least like by the person who originally designed it I think that is
[7080.72 → 7086.22] like a good way to look at it again it's still pretty rough just in terms of you know like the
[7086.22 → 7091.44] developer servers maybe not fast enough, so there are like many paper cuts but I think that is the
[7091.44 → 7097.18] place to kind of get the initial impression do you think it's production ready right now as of today
[7097.18 → 7104.72] February 2024 production ready is like a very subjective concept I think like Facebook used React in
[7104.72 → 7109.78] production way before most people would call it production ready there's definitely pretty large companies
[7109.78 → 7115.74] using you know Next.js app router in production right now, and you know both like hobbyist and
[7115.74 → 7121.96] big companies, but it does have I think like especially like there are some features that are less baked
[7121.96 → 7127.84] that are like currently being you know fixed but like parallel routes intercepting routes there were
[7127.84 → 7133.58] like a lot of bugs related to those that are being fixed right now so I think like in a year it I expect it
[7133.58 → 7140.42] to be a lot more kind of bug free, and you know like just doing the right thing I think currently it feels
[7140.42 → 7146.24] a little bit like a little shaky in some places and maybe like slower than you would like for just
[7146.24 → 7151.86] developer like the dev server is a bit slower so that's something I expect to see with turbo pack
[7151.86 → 7158.06] fixed so I think it's its ready for production in the sense of you can start building with if it's not
[7158.06 → 7163.58] going to change under you like in some significant way like the concepts are stable but I think like if
[7163.58 → 7168.80] you I guess like I think maybe actually the biggest part is just because the conceptual model is new
[7168.80 → 7174.56] there aren't really a lot of resources to kind of explain how to think in it or there aren't really like
[7174.56 → 7180.10] best practices that you know you can just it's its kind of like react in early days like if you would
[7180.10 → 7187.68] use react in 2014 then I think yes you can totally use app router if react in 2014 seemed to you know
[7187.68 → 7194.44] kind of draw to you, and you would rather like to wait to 2016 then I think this is similar like maybe you
[7194.44 → 7199.20] can wait a little bit and then give it a try when it's when there are more resources and more people
[7199.20 → 7205.80] kind of understand how to use it, and it's easier to find like answers that are correct yeah that makes
[7205.80 → 7210.96] sense that makes sense and so in terms of like your own risk for app it's not it's not even
[7210.96 → 7216.48] risk it's like your own appetite for being on the bleeding edge and like your team's capacity to kind
[7216.48 → 7224.36] of do a lot more learning through maybe reading source code and like experimentation and I think like
[7224.36 → 7229.12] not necessarily source code but I think it's just you know like you've talked about things like use
[7229.12 → 7235.66] client or use server that are like very misunderstood, and it's just like until there's like a couple of
[7235.66 → 7241.88] perfect blog posts the same way as like React was pretty misunderstood in 2014 and then like there
[7241.88 → 7246.76] were some talks there were some blog posts there were podcasts like this one right and like
[7246.76 → 7252.24] eventually there's like enough kind of knowledge between people in the ecosystem that they can help
[7252.24 → 7257.38] each other I think that's that's where it needs to get yeah well that that makes sense all right and
[7257.38 → 7263.36] my last question this doesn't even have to do with react server components um if you could make wave a
[7263.36 → 7271.04] magic wand for like one thing that you want to be on the web right whether it's a feature or even in
[7271.04 → 7276.40] a library like what's one thing that you wish was on the web that isn't there today yeah I mean I'm
[7276.40 → 7284.20] pretty selfish right like I'm i like react so I'm interested in like react getting better but I'd
[7284.20 → 7289.84] really love like a deep first class support for animations because this is something you can already
[7289.84 → 7294.66] do with like libraries like frame of motion so it kind of feels like well it's you know you can use
[7294.66 → 7300.72] if it's already there but like similar to how you know server components and kind of resolved a bunch
[7300.72 → 7306.78] of like it lets people compose you know the biggest yeah the biggest thing with React is always we want
[7306.78 → 7311.78] to let people compose things we want people to take different parts written by different people
[7311.78 → 7317.34] kind of connect them together and have the result still make sense whether you know like server
[7317.34 → 7321.76] component kind of extends it between like client and server so you can have this like Lego blocks
[7321.76 → 7328.06] that are spanning both worlds but you can still treat them as components and compose them and for
[7328.06 → 7333.62] animations like this is something like I'd also like to see where maybe the person writing the
[7333.62 → 7338.50] component currently like with frame of motion and animation approaches in other like most other
[7338.50 → 7343.64] libraries as well usually like you have to the person writing the component has to be aware
[7343.64 → 7350.50] that it's anima table so you kind of have to like to express the animation at the leaves whereas from
[7350.50 → 7355.92] kind of React's point of view like but like people to be able to like to write components and then you should
[7355.92 → 7361.68] be able to like to animate them from above and kind of say like I'm just changing this state from you know
[7361.68 → 7368.38] like gallery index one to gallery index three and i I also want to kind of show like this like gallery item
[7368.38 → 7373.08] you know the actual like carousel items created by somebody else like I want to specify where the current
[7373.08 → 7379.42] item is placed and then somehow you know you'd have like an API I think like view transitions API is
[7379.42 → 7383.18] like a step in the right direction I was just going to bring that up I was like I feel like that's like
[7383.18 → 7388.54] yeah like the baby you know that's kind of getting us there but yeah so we want to we want
[7388.54 → 7395.34] that but we want to integrate it with the component model so that it's also very composable and you can
[7395.34 → 7401.30] you know put things together written by different people and like animate them in a way that's you know
[7401.30 → 7405.72] doesn't break as you keep doing that and keep kind of expanding like there are many like small
[7405.72 → 7410.60] nuances of like what if you have many multiple animations at the same time that can like one of
[7410.60 → 7416.24] them wait for the other or should they happen like together what if like the state updates in the middle
[7416.24 → 7421.66] of the animation like should we kind of hold that state update back until it finishes so that there's
[7421.66 → 7426.54] all these like small things that are not really composable if you think about them in isolation
[7426.54 → 7432.42] but something like React could actually orchestrate it, and so I'd love to see that maybe in a couple
[7432.42 → 7439.04] of years that is so cool and also today I learned Dan Abrams is like an animation stork um did like
[7439.04 → 7447.22] like yeah clearly uh very passionate about animations um well Dan again it was an amazing this
[7447.22 → 7454.64] was just such a like mind-blowing like glee deep and dense and educational podcast discussion so
[7454.64 → 7459.50] we really want to thank you and Eric for joining us today for folks who are listening uh it's probably
[7459.50 → 7464.66] going to take a few listens to kind of get all the gems that Dan and Eric were sharing but worth a few
[7464.66 → 7472.78] listens if you're you've stuck with us this long thank you and um and yeah so just you know as
[7472.78 → 7477.70] hopefully this part of the ecosystem continues to mature we hope to be able to kind of have more
[7477.70 → 7483.14] discussions on this and kind of you know continue talking about it on the show and in the meantime
[7483.14 → 7489.22] we'll put links to a bunch of stuff that Dan has shared with us to kind of so you can take a look
[7489.22 → 7494.96] at some perfect blog posts and some good write-ups on this topic and yeah and let's use feel free to
[7494.96 → 7500.54] use the discussions area on our website for any questions or comments and yeah, thank you so much
[7500.54 → 7507.10] again Dan it's been a pleasure yeah thank you so much for hosting and for inviting me and also I apologize
[7507.10 → 7512.12] if i I know that some explanations were kind of long-winded and I also don't know which of them
[7512.12 → 7519.44] really work so I think I would like to appreciate if uh the listeners or the readers you know if you is
[7519.44 → 7524.76] you carried something away from this like write about it, you know write about it in your own language
[7524.76 → 7530.42] because I feel like the underlying concepts are kind of at the fundamental level they're as simple
[7530.42 → 7536.08] but then there are a lot of like historical baggage and kind of how they combine that that is
[7536.08 → 7541.52] more difficult, and so I'd appreciate it if people could help distill them down like in a better way than
[7541.52 → 7548.88] than I could do here yeah no that's like such a great call out um all right Dan so once again another
[7548.88 → 7554.68] one in the bucket this week and hope to catch you all next week when we'll be talking about something
[7554.68 → 7559.34] delightful as well I'm sure all right everyone cheers bye-bye
[7559.34 → 7581.04] all right that is JS party for this week thanks for hanging with us subscribe now if you haven't yet
[7581.04 → 7587.90] head to jsparty.fm for all the ways and don't forget to check out our fresh changelog beats
[7587.90 → 7595.22] the new dance party album is on Spotify Apple Music and the rest there's a link in the show
[7595.22 → 7601.74] notes for you thanks once again to our partners at fly.io to our beat freaking residents break master
[7601.74 → 7607.86] cylinder and to you for listening we appreciate you spending time with us each week next up on the pod
[7607.86 → 7613.92] we're talking angular again this time with a focus on the future keep your podcast app tuned right
[7613.92 → 7617.90] here we'll have that episode ready for your ear holes next week
[7617.90 → 7618.90] you
[7618.90 → 7622.90] you
