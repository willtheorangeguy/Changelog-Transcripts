[0.00 --> 11.14]  Welcome to JS Party, your weekly celebration of JavaScript and the web.
[11.66 --> 16.36]  Thanks to our friends at Fastly for shipping all of our pods super fast all around the world.
[16.66 --> 18.34]  Check them out at Fastly.com.
[18.62 --> 22.78]  And to Fly, host your app servers and database closer to your users.
[23.12 --> 24.32]  No ops required.
[24.88 --> 27.08]  Learn more at fly.io.
[27.08 --> 30.02]  And hey, we have a new partner, TypeSense.
[30.40 --> 32.40]  Lightning fast, open source search.
[32.68 --> 33.86]  No PhD required.
[34.26 --> 36.30]  Check it out at typesense.org.
[36.66 --> 38.96]  Okay, hey, it's party time, y'all.
[38.96 --> 56.12]  Ahoy hoy.
[56.44 --> 59.50]  Welcome to another exciting edition of JS Party.
[60.34 --> 62.42]  Today with me, I'm Nick Neesey, by the way.
[62.56 --> 66.24]  And today with me is Chris Hiller, a.k.a. Bone Skull.
[66.28 --> 66.74]  How's it going?
[67.20 --> 68.22]  How's it going, Nick?
[68.68 --> 69.44]  I'm excited.
[69.68 --> 70.64]  I'm excited that you're here.
[70.78 --> 72.30]  I'm excited that our guest is here.
[72.34 --> 74.06]  And that guest is Zach Leatherman.
[74.20 --> 75.08]  Zach, how's it going?
[75.54 --> 76.26]  Hey, good.
[76.36 --> 77.32]  How are you all?
[78.34 --> 79.88]  Couldn't be more excited.
[80.44 --> 84.74]  It's a beautiful March morning or afternoon, I guess, depending on where you're at.
[84.98 --> 87.08]  And the sun is out.
[87.20 --> 88.10]  It's a beautiful day.
[88.14 --> 91.64]  And it's almost exactly a year since we've had you on the show.
[91.74 --> 92.76]  So welcome back.
[93.42 --> 94.46]  Last time you were here.
[94.46 --> 95.10]  It's party time.
[95.10 --> 97.30]  Yeah, a party every day.
[99.14 --> 104.30]  Last time you were here, I think we had you on to talk about going full time on Eleventy.
[104.88 --> 109.36]  And so that means that you've been at it for probably just over a year now.
[109.56 --> 111.42]  And how has that experience been?
[111.60 --> 112.30]  It's still amazing.
[112.48 --> 113.06]  It's still awesome.
[113.24 --> 116.38]  I'm still like super pumped to go to work every day.
[116.38 --> 120.98]  And yeah, I think it's been awesome for Eleventy the project.
[121.24 --> 125.66]  And I'm just really excited about what's coming next for Eleventy too.
[125.98 --> 126.16]  Yeah.
[126.24 --> 132.18]  Speaking about Eleventy too, I was pleased to hear that it was re-architected and rewritten
[132.18 --> 134.86]  from the ground up to use GraphQL and React.
[135.92 --> 137.18]  Can you talk about that?
[137.18 --> 141.32]  That's a very interesting question.
[141.46 --> 142.78]  I don't know where you heard that rumor.
[144.04 --> 149.36]  It was in fact not re-architected from the ground up and it does not have any React compatibility.
[149.68 --> 155.28]  Although you can technically use JSX with it and TypeScript with it in version two.
[155.28 --> 158.58]  So it's a little bit nicer experience there.
[158.92 --> 161.84]  I want to state for the record that Zach was the first one to bring up TypeScript.
[162.38 --> 162.92]  Not me.
[164.02 --> 165.66]  I guess that means it's fair game now.
[165.86 --> 168.54]  And may it be the last time we talk about it.
[169.30 --> 170.86]  Is this TS Party or JS Party?
[170.96 --> 171.32]  I'm sorry.
[171.78 --> 172.18]  Which one?
[172.24 --> 174.10]  Whenever Nick's on, it's TS Party.
[174.52 --> 174.70]  Yeah.
[175.06 --> 175.22]  Yeah.
[175.68 --> 178.94]  So we have a .11d.ts file now.
[179.00 --> 180.34]  Is that the new big thing?
[180.94 --> 182.58]  Yeah, you can do that with the ES build.
[182.58 --> 186.22]  And if you search for it on the docs, there's an example of how to get it going.
[186.44 --> 187.64]  I was 100% kidding.
[187.88 --> 191.58]  And now you just got me really excited because I did not actually realize that.
[191.78 --> 192.02]  Yeah.
[192.06 --> 195.90]  I mean, we had a contribution come in that enabled that using ES build.
[196.22 --> 196.70]  So nice.
[196.98 --> 197.12]  Yeah.
[197.12 --> 197.86]  I think it's really great.
[198.32 --> 200.04]  I don't use it personally, but I think it's really great.
[202.80 --> 206.08]  So why don't you tell us a little bit about what you've been up to the last year?
[206.50 --> 207.72]  Yeah, just a lot of stuff.
[207.72 --> 211.94]  So we have basically been working on the 11d 2.0 release.
[212.58 --> 214.04]  For almost the entire year.
[214.60 --> 220.78]  And also, I think the other big flagship thing that we did was release WebC, which is kind
[220.78 --> 226.80]  of like a server rendered single file component format for web components using a lot of the
[226.80 --> 232.80]  same conventions that are built into web components and an HTML parser to do that.
[232.80 --> 237.14]  So trying sticking as close to web standards as possible, but really getting some good
[237.14 --> 239.96]  server rendered markup out of it.
[240.36 --> 245.76]  Really trying to handle some of the biggest complaints that you see when you're talking
[245.76 --> 248.66]  about web components, at least from a framework author's perspective.
[248.66 --> 253.66]  Yeah, that is kind of one of the things that has always been difficult with me around web
[253.66 --> 258.26]  components is just like how to actually like slot it in and use it.
[258.30 --> 263.36]  Because full disclosure, the only time I've really fully used web components was the version
[263.36 --> 267.14]  zero spec, which is not anything like it is now.
[267.68 --> 270.44]  And much worse, or at least not.
[270.78 --> 272.48]  It wasn't terrible, but it's much better now.
[272.48 --> 277.76]  And but it's still always like you have to use the components, but you also have to define
[277.76 --> 280.56]  the components somewhere and kind of put all of that together.
[281.14 --> 287.40]  And I'm pretty excited about WebC being a way to kind of flush all of that out.
[287.58 --> 288.80]  So that's that's really cool.
[289.12 --> 292.02]  I want to dig into WebC a little bit more in full.
[292.14 --> 297.38]  But besides that, what are some other big changes that came to 11d2?
[297.68 --> 300.14]  Yeah, I mean, there is just a ton of stuff.
[300.14 --> 302.38]  It's probably hard to go through the entire release notes.
[302.56 --> 308.06]  But with our 2.0 release, we one of the first things we did was strip out the browser sync
[308.06 --> 311.08]  dependency and use now we have our own dev server built in.
[311.36 --> 316.10]  And that is really manifested itself as a huge reduction in our node dependencies.
[316.58 --> 323.36]  I think we went from like 120 megabyte node modules folder down to like 30 megabytes.
[323.62 --> 327.36]  So the install times are much faster, the project is much lighter.
[327.82 --> 329.98]  And yeah, I think it's really great all around.
[330.14 --> 335.16]  I think the other big flagship things that really went into it are investments in our
[335.16 --> 335.98]  plugin ecosystem.
[335.98 --> 340.06]  So we have a bunch of like official plugins that are bundled with 11d core.
[340.34 --> 345.28]  I think maybe the coolest one or the one that I'm most excited about is our edge rendering
[345.28 --> 350.02]  plugin that really allows you to do 11d templates on the edge.
[350.02 --> 357.66]  So it unlocks a whole ton of different no client JavaScript use cases that weren't possible before.
[357.66 --> 365.64]  So customized content for a single user, form handling, cookies, all that kind of server side
[365.64 --> 372.00]  stuff that I think really, in many ways has been taken over by other templating languages
[372.00 --> 376.58]  and wasn't really as available in JavaScript as much as we would like.
[376.58 --> 380.22]  So yeah, I'm kind of an old school fan of PHP.
[380.52 --> 386.58]  And I think this really unlocks a lot of like things that I really love to do in PHP in a
[386.58 --> 387.32]  really light way.
[388.00 --> 392.04]  Good question about the, so why did you swap out BrowserSync?
[392.58 --> 393.26]  Just curious.
[393.74 --> 393.88]  Yeah.
[393.88 --> 398.80]  So the original issue I think that we ran into with BrowserSync was we started to get a lot
[398.80 --> 403.00]  of NPM audit and security vulnerability audits coming back from the tool.
[403.00 --> 409.66]  And those were handled like on a somewhat timely basis, especially considering if the project
[409.66 --> 415.02]  is like, I don't know exactly how it's funded or maintained, but I think fixes came out pretty
[415.02 --> 415.78]  good for it.
[415.88 --> 422.82]  It wasn't terrible, but we did want something lighter and something that was under the purview
[422.82 --> 427.76]  of Eleventy, something that we could change and update and have full control over what
[427.76 --> 429.46]  the experience was.
[430.08 --> 432.26]  And some cool features came out of it as well.
[432.36 --> 436.70]  Now we have like a DOM diffing live reload feature in the dev server.
[437.38 --> 442.90]  So you don't necessarily have to do full page reloads for HTML changes now, which is kind of
[442.90 --> 443.12]  cool.
[443.36 --> 448.52]  But so basically you had to implement hot reloading from scratch, yeah?
[449.00 --> 449.30]  Yeah.
[449.60 --> 449.90]  Yep.
[449.94 --> 450.42]  That's true.
[450.94 --> 452.70]  How was that experience?
[452.82 --> 454.18]  It actually wasn't too bad.
[454.18 --> 456.40]  It was much lighter than I would have expected.
[456.70 --> 461.78]  A lot of the utilities for that, the WebSocket stuff is built into Node.
[461.90 --> 466.64]  I mean, there's a lot of stuff you get for free from the Node ecosystem, not even necessarily
[466.64 --> 470.40]  as a package, like a third party package that you would install.
[470.56 --> 473.20]  It's like first party Node things.
[473.54 --> 478.82]  So we have live reload implemented with WebSockets and yeah, it works great.
[478.82 --> 481.98]  Kind of going back to the Edge plugin.
[481.98 --> 485.80]  I'm just curious, like, can you give a use case of where you might use this?
[485.92 --> 488.36]  I'm trying to understand what it is.
[488.96 --> 489.08]  Yeah.
[489.08 --> 493.46]  It's kind of the ability to run a templating language on request.
[494.10 --> 498.32]  And it's a little bit, I mean, it's, it kind of feels like a serverless request, but it's
[498.32 --> 501.30]  a little bit lighter weight thing.
[501.30 --> 504.04]  And we architected the plugin a little bit differently.
[504.56 --> 510.68]  You can kind of think of it as a separate template that runs in an Edge function.
[511.46 --> 517.54]  So anything that you can do in an Edge function, you can do in an Eleventy Edge template.
[517.54 --> 522.70]  So you can handle, you can read values of cookies, server side cookies, you can set and read values
[522.70 --> 523.14]  of cookies.
[523.36 --> 525.62]  You can find the user's geolocation.
[525.98 --> 528.56]  You can have access to post requests.
[529.00 --> 531.56]  So you can actually do handle form submissions.
[532.40 --> 534.74]  There's just a ton of stuff that you can do server side.
[535.34 --> 536.84]  That's, yeah, kind of neat.
[537.68 --> 542.00]  Does it have access to things like, like other pieces that you would get normally through
[542.00 --> 542.44]  Eleventy?
[542.56 --> 545.48]  I'm thinking like collections and, and things like that.
[545.48 --> 550.34]  No, I mean the, the Eleventy Edge, well, I mean, you can link those things up.
[550.46 --> 554.02]  You can expose data from your build into the Edge function.
[554.36 --> 559.66]  That is a definite possibility, but you, it's more of like a, it's a, you're building a template
[559.66 --> 561.36]  that can run on the Edge.
[561.58 --> 567.80]  So it has a, there's like a, a certain runtime limit that's built into the platform.
[568.20 --> 573.38]  I think it's like a 50 millisecond execution time that's built into Edge functions.
[573.38 --> 575.40]  So they need to be very, very lightweight.
[575.74 --> 581.40]  And because of that limitation and because of the sort of scoped down version of these
[581.40 --> 583.48]  templates, they're very speedy and very fast.
[583.48 --> 588.86]  So normally with like an AWS Lambda, you're going to see a slow startup time.
[589.68 --> 594.62]  And I think with a lot of those, what a lot of providers have tried to do is put a caching
[594.62 --> 595.56]  layer in front of that.
[595.56 --> 602.10]  So Netlify has like an on-demand builder, which will, after the first request comes in,
[602.12 --> 603.78]  it will just cache that URL for you.
[603.82 --> 609.26]  So any repeats to that will just be served as a static file, but an Edge function runs
[609.26 --> 609.86]  every time.
[610.10 --> 615.00]  So it needs to be much more lightweight and most Edge functions will finish running before
[615.00 --> 619.52]  that cold start of the, the serverless function is even stopped.
[619.52 --> 622.12]  So yeah, Edge functions are quite a bit speedier.
[622.68 --> 626.54]  So I, I, I've never used Edge function stuff.
[627.00 --> 632.36]  And so, but I know with Eleventy, what you do is you run Eleventy and it, it, it reads
[632.36 --> 634.92]  your stuff and it, it poops out some files.
[635.32 --> 637.24]  So now then what do you do with those?
[637.34 --> 638.40]  What do you do with those files?
[638.48 --> 643.18]  If, if you're trying to deploy stuff to the edge, I mean, what's the, like, what's the
[643.18 --> 645.20]  development workflow look like?
[645.20 --> 647.56]  What's the, like, how do you deploy it?
[647.80 --> 654.68]  Like, do you run Eleventy on some cloud machine and then it, it deploys your, you know, your
[654.68 --> 656.76]  code to the, how does that work?
[657.32 --> 657.50]  Yeah.
[657.58 --> 661.38]  So Netlify actually works with a thing called Dino.
[661.60 --> 663.00]  So they run Dino in the cloud.
[663.70 --> 669.26]  So Eleventy is actually processing your template on request and the Eleventy build generates
[669.26 --> 671.98]  that template to run in the Edge function.
[671.98 --> 677.20]  So, I mean, it's like all these pieces that are kind of working together, but the authoring
[677.20 --> 682.04]  experience is pretty nice because the, the only thing you have to do in an Eleventy build
[682.04 --> 688.00]  specifically is that you just use a short code to demarcate what you want to run on the
[688.00 --> 688.26]  Edge.
[688.36 --> 694.48]  So you just use your normal Eleventy build template and you just use an Edge short code
[694.48 --> 700.14]  inside of it to sort of say, I want this block of code in my HTML template or in my whatever
[700.14 --> 702.10]  templating language you want to use.
[702.32 --> 706.22]  I want this piece of the page to run and to be dynamic on the Edge.
[706.50 --> 711.08]  So in that way you can combine build and Edge templates together.
[711.08 --> 715.06]  And I think a very unique way that a lot of other frameworks aren't doing.
[715.70 --> 724.00]  And so like what you can do is I assume then run your Eleventy build on Netlify, right?
[724.00 --> 727.00]  As like a, like a static site build.
[727.14 --> 733.82]  And then part of that will end up getting deployed to whatever functions thing they have, right?
[734.36 --> 734.54]  Yeah.
[734.68 --> 734.94]  Yeah.
[734.94 --> 736.58]  Netlify handles all that for you.
[736.68 --> 743.00]  So really the only thing you need to do is add the Edge plugin, the Eleventy Edge plugin
[743.00 --> 745.42]  and the rest should be handled for you.
[745.96 --> 746.12]  Yeah.
[746.12 --> 746.94]  It's really pretty slick.
[747.04 --> 747.48]  I like it.
[747.48 --> 754.60]  But I do want to say like, I feel like the ecosystem in a way is like fighting this tension
[754.60 --> 761.92]  of like build time versus request time things that has probably existed in the JavaScript
[761.92 --> 763.72]  ecosystem for a very long time.
[764.20 --> 769.74]  And some frameworks are going all in on request time page rendering.
[769.74 --> 771.90]  So I think Remix is one that does that.
[772.06 --> 773.92]  And Fresh, I think, is another one that does that.
[773.92 --> 777.96]  But Eleventy is at its core still a static site generator.
[778.20 --> 779.18]  We're build first.
[780.12 --> 785.90]  We want to use the build to optimize your pages, whether those end up in an Edge function or
[785.90 --> 786.16]  not.
[786.96 --> 792.76]  And yeah, Eleventy is going to continue to be a site builder, a static site builder as
[792.76 --> 793.90]  its core functionality.
[794.10 --> 799.70]  We're just layering these extra things on top because really a static build, I really feel
[799.70 --> 800.40]  this to my core.
[800.40 --> 804.12]  It gives you the most portability if you need to change hosts.
[804.32 --> 808.12]  And I feel like that is a valuable thing, even though I work for Netlify.
[808.60 --> 812.72]  I feel like it is a very valuable thing to have a portable site that you can put on a different
[812.72 --> 813.14]  provider.
[814.18 --> 816.66]  And yeah, Netlify has been very supportive of that, too.
[817.10 --> 821.08]  We added a deployment page to the Eleventy docs and we have a ton of different deployment
[821.08 --> 822.04]  providers on there.
[822.62 --> 825.32]  And I was encouraged to do that by folks at Netlify.
[825.54 --> 828.66]  So yeah, very supportive of that methodology.
[829.22 --> 829.94]  Yeah, that's great.
[829.94 --> 835.64]  Another thing that I noticed while perusing the Eleventy YouTube channel, which you should
[835.64 --> 841.88]  check out, we'll have it in the show notes, was support for VEAT.
[842.30 --> 846.20]  And I'm just curious what that means in terms of Eleventy.
[846.72 --> 853.30]  Yeah, the Eleventy core, and I think I've talked about this a bunch before, we don't really
[853.30 --> 858.42]  want to tightly couple the Eleventy project to any specific bundler.
[858.42 --> 862.02]  And that's just because bundlers come and go.
[862.12 --> 865.66]  And I want Eleventy to exist on a very long time frame.
[866.68 --> 871.22]  And I personally, I really believe that Eleventy will probably outlast VEAT.
[871.22 --> 875.40]  And I will work very hard to make sure that that is true.
[875.68 --> 876.86]  But I love VEAT.
[876.92 --> 877.78]  I think VEAT's awesome.
[878.30 --> 884.44]  I just don't want to couple the Eleventy project to a bundler in a tight coupling kind
[884.44 --> 884.74]  of way.
[884.74 --> 889.76]  So we did actually ship a VEAT plugin for Eleventy last year.
[890.48 --> 893.98]  And folks have been using that to use VEAT with Eleventy.
[894.18 --> 897.26]  We run VEAT as a middleware in our dev server.
[897.52 --> 903.82]  So you get some of the great benefits out of the VEAT bundler and some of the great benefits
[903.82 --> 905.30]  from using Eleventy at the same time.
[905.48 --> 908.68]  So yeah, I think the two things can coexist in a nice way.
[908.68 --> 909.12]  Yeah.
[909.40 --> 914.94]  Are those things like access to VEAT's plugin ecosystem, like things like that?
[915.12 --> 923.32]  Or I guess my usage of Eleventy always results in like zero client JS, which is a good thing.
[923.82 --> 928.38]  But I guess I'm just trying to understand how that I'm trying to understand from my perspective
[928.38 --> 933.40]  what that buys me that just the regular like Eleventy build doesn't.
[933.84 --> 937.60]  I mean, a lot of people love VEAT's asset bundling.
[937.60 --> 944.22]  So the stuff that's built in to sort of bundle your JavaScript and CSS into per route assets.
[944.62 --> 945.58]  I mean, that's a nice feature.
[945.72 --> 949.02]  And that's something that you can also do with Eleventy as well.
[949.58 --> 955.58]  So I mean, it's really just about expanding the Eleventy ecosystem to include compatibility
[955.58 --> 956.56]  with more things.
[957.18 --> 962.42]  So if you love VEAT and you haven't been exposed to Eleventy, you'll probably want to use both
[962.42 --> 963.84]  those things together.
[964.14 --> 964.48]  Right.
[964.48 --> 968.02]  Until I win you over and try to reduce your dependencies down to zero.
[969.68 --> 974.40]  Yeah, that's so like Mocha has been a user of Eleventy for a long time now.
[974.88 --> 980.18]  And R, I say R, I'm not even working on it anymore, but I implemented it.
[980.52 --> 986.02]  So it just, there's like, I don't know, like 20 lines of JavaScript, right?
[986.02 --> 990.34]  And it's, there's hardly anything to be done.
[990.74 --> 994.04]  And it, that's what I love about Eleventy.
[994.14 --> 1000.58]  There's no, there's no extra fussing around with tree shaking and all this extra bundling.
[1000.74 --> 1003.54]  And, you know, I don't even know if we minify anything.
[1003.54 --> 1009.34]  We just, we just ship a little bit of code and we compress like images or something like
[1009.34 --> 1009.60]  that.
[1009.78 --> 1010.66]  But that's about it.
[1010.80 --> 1013.22]  And that's what I love about Eleventy.
[1013.32 --> 1016.96]  It's just like out of the box, it's just dead simple.
[1017.24 --> 1022.68]  And that's really all you need for so many sites.
[1022.68 --> 1029.12]  But, you know, it seems like, you know, with, with the plugin ecosystem, you can use it to
[1029.12 --> 1030.30]  scale up from there.
[1031.12 --> 1031.60]  Yeah.
[1031.70 --> 1033.70]  And it can scale pretty far.
[1033.78 --> 1041.00]  I think, I think maybe the thing, the JavaScript ecosystem at large maybe bought into too hard
[1041.00 --> 1046.22]  was that a lot of folks just need HTML and CSS to build their sites.
[1046.22 --> 1053.04]  And anything on top of that is just an extra layer of complexity and unnecessary dependencies
[1053.04 --> 1057.40]  that really eat into your long-term maintenance of a project.
[1058.14 --> 1063.42]  I had, we just, so we just released the 2.0 release and someone had posted on Mastodon how
[1063.42 --> 1068.80]  they were going to upgrade to 2.0 and it was actually going to, they picked up a project that
[1068.80 --> 1072.42]  was a couple of years old and didn't, it didn't require them to make any changes.
[1072.42 --> 1078.50]  So I think that's kind of a, maybe a unique thing to the JavaScript ecosystem, a tool that
[1078.50 --> 1084.56]  exists in the JavaScript ecosystem is that when you have such a lightweight project with
[1084.56 --> 1091.92]  like a relentless focus on reducing third-party dependencies, it really does allow you to maintain
[1091.92 --> 1098.54]  things long-term in a way that I think is enticing for a lot of people that don't want to
[1098.54 --> 1102.34]  necessarily do a ton of maintenance to bring an old project back up to speed.
[1102.42 --> 1109.12]  As someone who is trying to go from version 4.0 of a project to version 5.0 or 5.whatever.
[1109.98 --> 1112.82]  And I'm looking at it and I'm like, this is probably like six months of work.
[1113.30 --> 1114.70]  I really appreciate that.
[1114.76 --> 1120.66]  I'm not going to call out the project because I don't want to shame them, but yeah, it's monumental
[1120.66 --> 1122.28]  in its complexity.
[1122.28 --> 1140.96]  Hey there, it's K-Ball from JS Party and I want to talk to you about a new service I'm
[1140.96 --> 1141.86]  offering for engineers.
[1142.12 --> 1146.44]  As you advance from junior to senior to staff engineer or move into management, there comes
[1146.44 --> 1150.46]  a point where the skills that got you to where you are are not enough to keep you moving forward.
[1150.46 --> 1154.18]  Where the answer to your question isn't on Stack Overflow because your problem has more
[1154.18 --> 1157.36]  to do with people and how to get them to make the right choices than about writing code.
[1157.92 --> 1158.28]  Congratulations.
[1158.78 --> 1160.90]  You've reached the border to becoming an engineering leader.
[1161.10 --> 1164.70]  If you're lucky when you hit this point, you have a manager or senior peer that can help
[1164.70 --> 1165.90]  guide you through the transition.
[1166.22 --> 1168.60]  But most of us aren't that lucky and that's where I want to help.
[1169.08 --> 1172.96]  Coaching engineers through the transition to becoming engineering leaders was the most satisfying
[1172.96 --> 1174.04]  part of my last job.
[1174.18 --> 1176.06]  And now I'm offering it as a paid service.
[1176.06 --> 1179.96]  Now, you may have never worked with a coach before and you're not sure what it would look
[1179.96 --> 1180.12]  like.
[1180.30 --> 1180.78]  I get it.
[1180.90 --> 1184.68]  That's why I'm offering free exploratory sessions to try it out, learn what it's like
[1184.68 --> 1186.40]  and work through a challenge you're facing right now.
[1186.66 --> 1191.04]  So if you're curious or you're feeling stuck, head over to kball.llc slash coaching.
[1191.20 --> 1194.18]  You can learn more about what I'm offering and sign up for your free exploratory session.
[1194.18 --> 1197.48]  That's kball.llc slash coaching.
[1197.48 --> 1217.04]  So, Zach, with 11.82, what broke?
[1217.38 --> 1220.80]  What was the major release there?
[1221.06 --> 1225.22]  Yeah, I mean, I think the biggest thing was, as I mentioned, that default dev server experience.
[1225.22 --> 1231.90]  So we did switch the default dev server from BrowserSync to our own internal dev server.
[1232.12 --> 1237.24]  And I think that was a big enough change in itself to merit a full version release.
[1237.36 --> 1241.02]  But there were a few other breaking changes that went into it.
[1241.06 --> 1246.06]  And we do have an upgrade helper plugin that analyzes your project and sort of reports what
[1246.06 --> 1248.28]  changes you need to make inside of it.
[1248.80 --> 1254.84]  But, I mean, it should be fairly straightforward for folks to upgrade from 1.0 to 2.0.
[1254.84 --> 1259.30]  And I think that that has definitely manifested itself in the feedback that I've seen.
[1260.16 --> 1264.90]  That's very kind of you to provide a plugin that does the migration.
[1265.72 --> 1268.98]  Or rather, it just tells you how to do the migration.
[1269.46 --> 1270.16]  That's, yeah.
[1270.52 --> 1276.62]  I mean, it's very selfish of me because it saves me helping everyone individually.
[1277.04 --> 1279.70]  So that is a trend, though, that I've seen with a lot of projects.
[1279.70 --> 1284.10]  They're like, oh, we can show you, you know, these are the things that are going to break.
[1284.16 --> 1287.92]  Like, it's almost like a, I'm thinking of like Homebrew's Brew Doctor, right?
[1287.96 --> 1290.04]  It kind of shows you these things are broken.
[1290.66 --> 1296.64]  And then some projects also ship like code mods that are like, for this very specific thing,
[1297.00 --> 1298.74]  run this and we'll just go fix it for you.
[1298.80 --> 1300.32]  Like changing imports.
[1300.70 --> 1301.52]  Yeah, that's nice.
[1301.64 --> 1301.80]  Yeah.
[1302.02 --> 1302.62]  Super cool.
[1303.16 --> 1303.84]  Yeah, that's awesome.
[1304.28 --> 1304.82]  I approve.
[1304.82 --> 1308.30]  Did you want to talk anything else on 11d2 or?
[1308.92 --> 1310.52]  No, let's talk about WebC.
[1311.12 --> 1311.34]  Okay.
[1311.74 --> 1316.86]  But before we do that, I just want to say that, you know, this project, really cool.
[1317.10 --> 1322.10]  I picked it up for my blog because, you know, it's a very popular, very demanding blog.
[1322.38 --> 1323.76]  And 11d was up to the challenge.
[1324.14 --> 1325.00]  So I appreciate that.
[1325.48 --> 1329.50]  But it's because it ships no JS bundle at all.
[1329.58 --> 1331.30]  Like, it's just, there's no JS at all.
[1331.36 --> 1332.32]  It just ships everything.
[1332.76 --> 1333.94]  And it's super easy to put together.
[1333.94 --> 1335.00]  I love all of that.
[1335.32 --> 1339.92]  Another cool project in this space that also hit 2.0 recently is Astro.
[1340.18 --> 1345.00]  And we just had Fred on a couple episodes ago to talk about Astro 2 and where they're
[1345.00 --> 1345.60]  going with that.
[1345.82 --> 1349.16]  And he just dished on 11d like constantly.
[1349.28 --> 1352.48]  So this is your turn to kind of retaliate.
[1354.28 --> 1356.58]  What is the definition of dished?
[1356.72 --> 1359.36]  He, you would not believe the things he, no, I'm kidding.
[1359.50 --> 1360.12]  He's great.
[1360.12 --> 1365.60]  I think 11d did come up as like a, a very, a project with like a very similar viewpoint
[1365.60 --> 1367.06]  on, on how to do things.
[1367.28 --> 1369.76]  But obviously he loves 11d.
[1369.90 --> 1372.36]  I assume that the feeling is mutual here.
[1372.50 --> 1373.76]  So I just, I don't know.
[1373.76 --> 1377.14]  I just wanted like to give you the opportunity to compare the two because they're both like
[1377.14 --> 1381.08]  in the same realm, kind of solving very similar problems from slightly different angles,
[1381.08 --> 1383.18]  but also very, very similar angles too.
[1383.82 --> 1383.94]  Yeah.
[1383.94 --> 1388.90]  I think there is a lot of overlap between 11d and Astro and I think Astro is a great
[1388.90 --> 1389.34]  project.
[1389.46 --> 1396.46]  I really, in my opinion, I really love to see anyone that sort of is helping out in the
[1396.46 --> 1398.40]  HTML space.
[1398.40 --> 1404.68]  So the HTML super friends as it were, because we really, we need allies if we're going to
[1404.68 --> 1407.36]  like improve the web in this way.
[1407.36 --> 1411.80]  And it can't just be one framework or one ecosystem that does it.
[1411.98 --> 1413.52]  So the more the merrier.
[1413.76 --> 1419.12]  So if anyone else wants to make an HTML first framework, I encourage you because we really
[1419.12 --> 1425.34]  need all the friends we can get as we like, I don't know, build this army of people that
[1425.34 --> 1432.18]  are sort of going away from the spa first, JavaScript first client side, JavaScript first
[1432.18 --> 1432.86]  mindset.
[1432.86 --> 1435.98]  So yeah, the more the merrier, in my opinion.
[1436.56 --> 1440.06]  I saw, I can't remember where I saw it, but it was, it was some graph that showed like,
[1440.10 --> 1443.98]  you know, 11d, Astro, next, remix, all of these.
[1444.08 --> 1447.32]  And it showed the amount of minimal JS runtime.
[1447.46 --> 1448.62]  It's probably my blog.
[1448.86 --> 1449.82]  It probably was.
[1450.30 --> 1451.96]  And 11d and Astro were both at zero.
[1452.22 --> 1456.28]  And then all of the rest had at least some client side JavaScript that they had to ship
[1456.28 --> 1456.74]  by default.
[1456.98 --> 1460.46]  So that's why I wanted to ask, because you're very similar in that.
[1460.46 --> 1465.34]  Another, another piece is, and, and like, I've been playing around with Astro a lot
[1465.34 --> 1465.68]  too.
[1466.02 --> 1469.96]  And when I approached Astro for the first time, kind of going in, I didn't really start until
[1469.96 --> 1471.66]  after 2.0, to be honest.
[1471.94 --> 1478.24]  But when I, when I did, I kind of assumed like, oh, this is going to be kind of like 11d, but
[1478.24 --> 1483.48]  I'm going to be able to use the comfort and safety of react of the react ecosystem that
[1483.48 --> 1486.00]  I have been, you know, what is, what is that?
[1486.00 --> 1493.48]  Like I've been stuck in for years and as I did it, I actually have written zero react
[1493.48 --> 1493.94]  with it.
[1494.00 --> 1495.40]  It's all been Astro components.
[1495.68 --> 1500.26]  And I thought that that was really cool because it's like, there are these single file components
[1500.26 --> 1502.46]  that let you put kind of everything together.
[1502.80 --> 1504.50]  And I was like, oh, this is so cool.
[1504.50 --> 1506.52]  And I'll just be completely honest with you.
[1506.62 --> 1511.08]  My, my blog has been using liquid, I think, or no, none jokes for 11d.
[1511.08 --> 1516.06]  And I'm not like the project just always feels like it's, you know, when I go to the documentation
[1516.06 --> 1519.84]  for like how to do things with, with none jokes, I'm just always like, this doesn't look like
[1519.84 --> 1521.32]  it's been touched in 15 years.
[1521.46 --> 1521.98]  Yeah, it hasn't.
[1522.08 --> 1522.24]  Yeah.
[1523.26 --> 1524.84]  And that never made me feel good.
[1524.86 --> 1525.92]  And I'm like, oh, this is really cool.
[1525.96 --> 1527.28]  I wish 11d had something like that.
[1527.28 --> 1530.40]  And then I was like, wait a minute, didn't Zach just come out with something that is kind
[1530.40 --> 1531.36]  of similar to this.
[1531.60 --> 1533.28]  And I think that's what WebC is, right?
[1533.28 --> 1540.02]  Yeah, I mean, in many ways, WebC is a new template syntax with the focus on web components
[1540.02 --> 1542.32]  and HTML and web standard conventions.
[1543.32 --> 1545.72]  So yeah, I think that that is, that is very true.
[1545.96 --> 1552.56]  I think that WebC will be seen as a successor to some of these templates syntax that aren't
[1552.56 --> 1556.32]  maintained very well anymore as the maintainers sort of move on.
[1556.42 --> 1561.42]  But I will say that liquid, the liquid template syntax is still very well maintained.
[1561.42 --> 1569.60]  And we sponsor the author, I think, with some of our $11 every month to help maintain that.
[1569.88 --> 1571.82]  But yeah, liquid is very well maintained.
[1572.02 --> 1573.14]  None jokes, not so much.
[1574.08 --> 1581.10]  So even though it's like web component-y, if you start using this, you still don't have
[1581.10 --> 1582.38]  to ship JavaScript, right?
[1583.02 --> 1583.56]  Yeah, correct.
[1583.72 --> 1586.86]  There's no client-side JavaScript built into it.
[1587.08 --> 1587.36]  Yeah.
[1587.36 --> 1594.44]  And so you kind of get component authoring experience without any client-side JavaScript
[1594.44 --> 1596.22]  requirement at all.
[1596.46 --> 1601.90]  And I do have a couple of really cool demos on the Eleventy documentation about how to
[1601.90 --> 1606.70]  add interactive components with client-side JavaScript interactivity built in.
[1606.70 --> 1615.28]  And we have some nice kind of bundley features, bundler-esque features, to sort of minimize the
[1615.28 --> 1617.84]  amount of JavaScript that gets sent to the client.
[1618.16 --> 1620.94]  And there's going to be a lot more coming there soon, too.
[1621.02 --> 1627.64]  I've been working on all-week improvements to sort of WebC bundling and asset bundling.
[1628.04 --> 1631.30]  And yeah, I'm really excited about the stuff that's coming next.
[1631.30 --> 1632.02]  Yeah.
[1632.54 --> 1635.14]  And you mentioned having some cool demos.
[1635.58 --> 1637.72]  I was just watching a couple of them earlier.
[1638.14 --> 1645.30]  And you really start off with a WebC template that is, or a WebC file that is just the string
[1645.30 --> 1646.36]  of text that you want to show.
[1646.42 --> 1648.06]  Not even any HTML markup.
[1648.22 --> 1649.44]  It's just that.
[1649.52 --> 1649.74]  Yeah.
[1649.74 --> 1652.52]  And it just works, which is really, really cool.
[1652.90 --> 1654.02]  And then you kind of incrementally.
[1654.22 --> 1657.86]  Yeah, I think that's very, maybe surprising for a lot of folks that come from a React
[1657.86 --> 1664.02]  background, where React had a lot of limitations around what kind of, like the, I don't know,
[1664.10 --> 1668.64]  the setup or the requirements around what can go into a React component.
[1669.02 --> 1670.64]  We're very strict for a while.
[1670.94 --> 1673.82]  And yeah, Eleventy is just freeform content.
[1674.44 --> 1676.50]  Or WebC, excuse me, is just freeform content.
[1676.50 --> 1678.46]  So you can put anything inside of a component.
[1678.46 --> 1679.22]  Yeah.
[1679.60 --> 1687.06]  And kind of going on my comparison with, between that and like Astro templates, like you progressively
[1687.06 --> 1693.02]  enhanced that text to then include some markup and then include some styles in a style tag.
[1693.12 --> 1696.82]  And that style tag just kind of gets thrown into the head of the page that the component
[1696.82 --> 1697.58]  is used on.
[1697.70 --> 1699.70]  But you could also scope it, which was really cool.
[1699.84 --> 1702.98]  So you could just have extremely scoped CSS for that.
[1703.56 --> 1705.34]  And same thing with like script text.
[1705.36 --> 1707.18]  Those just get kind of bubbled up.
[1707.18 --> 1709.40]  Do you want to talk about how you do that?
[1709.52 --> 1714.06]  How you progressively enhance it into being not so static and maybe adding in a little
[1714.06 --> 1716.62]  bit of client-side JavaScript where it's necessary?
[1717.32 --> 1717.46]  Yeah.
[1717.50 --> 1723.08]  I mean, I think it all comes down to a really core understanding of what progressive enhancement
[1723.08 --> 1726.18]  is and the benefits you can get out of progressive enhancement.
[1726.18 --> 1732.60]  I feel like the things that I've used throughout the years have really had a misunderstanding of
[1732.60 --> 1737.32]  like different tools and frameworks that I've, that I've seen as like a comparison.
[1737.32 --> 1742.30]  I've really had a fundamental misunderstanding of what progressive enhancement is.
[1742.30 --> 1748.78]  And I think that's kind of fair because progressive enhancement is, it's kind of a complicated thing
[1748.78 --> 1751.30]  to, I don't know, teach someone.
[1751.74 --> 1757.02]  Especially when you're coming into web development from when you're baseline, the thing that you
[1757.02 --> 1758.70]  learned on was a bundler.
[1758.70 --> 1763.62]  And maybe the things that you've learned from the beginning sort of violated those progressive
[1763.62 --> 1766.22]  enhancement core strategies.
[1766.56 --> 1772.48]  So I think that when it comes to WebC, the sort of really neat thing is that you have full
[1772.48 --> 1776.78]  control over what you want the progressive enhancement of a component to be.
[1777.14 --> 1782.28]  So I have a demo on the WebC docs that is, I think it's like six or seven different
[1782.28 --> 1786.68]  progressive enhancement strategies for an image comparison component.
[1786.68 --> 1792.56]  So it kind of shows you, it's kind of that classic, like here's an image, there's two
[1792.56 --> 1797.32]  different images and you can slide back and forth between them to show the first image
[1797.32 --> 1801.78]  or the second image to sort of compare before and afters of an image.
[1802.36 --> 1807.82]  And so I built that in like six or seven different ways to show how much control you have over
[1807.82 --> 1810.34]  the progressive enhancement of individual components.
[1811.02 --> 1816.62]  And if you're creating a component that can be reused, you can even have multiple,
[1816.68 --> 1820.20]  different progressive enhancement strategies built into the component itself.
[1820.90 --> 1825.76]  And the app developer can theoretically choose between one or more of those.
[1826.38 --> 1831.94]  And I love that level of control because I really think that it does depend on individual
[1831.94 --> 1832.64]  use cases.
[1833.44 --> 1837.88]  And if you are too prescriptive about the progressive enhancement strategy of a component,
[1838.32 --> 1841.20]  it isn't going to have as much long-term benefit.
[1841.20 --> 1845.78]  And you won't be able to use it for maybe the next project that you want to build if it
[1845.78 --> 1847.46]  isn't customizable enough.
[1848.20 --> 1854.20]  So I don't know, that's sort of a long-winded way to say that, yeah, Eleventy and WebC, I
[1854.20 --> 1861.12]  think really both have that core ethos of, I really want folks to have as much control over
[1861.12 --> 1862.90]  the authoring experience as they can.
[1862.90 --> 1870.06]  And I think in some respects that can be frustrating too, because more control means that you need
[1870.06 --> 1873.68]  to sort of piece things together in a more manual way sometimes.
[1873.94 --> 1879.42]  And I'm always working on striking the correct balance there between, yeah, having to author
[1879.42 --> 1882.18]  too much and over-automating things.
[1882.18 --> 1889.38]  So I think that there's definitely, in competing frameworks, I've definitely seen over-automation
[1889.38 --> 1893.68]  or over-abstracting of things and it makes it just hard to use it.
[1894.06 --> 1894.90]  So, yeah.
[1895.56 --> 1901.08]  Well, one thing that I'm curious about with this, so these components, like it's right
[1901.08 --> 1904.54]  in the name, WebC, I'm immediately drawn to web components.
[1904.54 --> 1910.70]  But you also mentioned that this could be like kind of a successor to some of the other
[1910.70 --> 1913.80]  templating libraries that Eleventy currently supports.
[1914.04 --> 1918.48]  Does that mean that you could use this at like a page level and have like entire pages
[1918.48 --> 1919.36]  built out of WebC?
[1919.92 --> 1920.70]  Yeah, for sure.
[1920.96 --> 1921.28]  Nice.
[1921.36 --> 1926.60]  Yeah, you can do full WebC pages, you can do WebC components, you can actually do, we
[1926.60 --> 1931.34]  have extensions to let you do WebC inside of other template languages as well.
[1931.42 --> 1932.76]  We have some shortcuts for that.
[1932.76 --> 1940.78]  You can use the render plugin that is new in 2.0 to render just a small block of WebC
[1940.78 --> 1942.64]  inside of your existing project.
[1942.94 --> 1944.74]  And yeah, I think that's useful.
[1945.00 --> 1945.10]  Yeah.
[1945.28 --> 1946.88]  But Dick, why would you want to do that?
[1947.18 --> 1952.90]  Like, isn't it nice to keep your, like, okay, your docs and markdown, right?
[1953.32 --> 1953.50]  Yeah.
[1953.98 --> 1959.58]  Based on what I had seen of WebC and setting that up and a question that I actually, I have
[1959.58 --> 1962.66]  a follow-up question that kind of leads into this, I guess, is.
[1963.26 --> 1968.42]  For me, that seems like a more appealing setup than what I'm currently using, which is Nunchucks.
[1968.78 --> 1970.78]  In hindsight, I probably should have chosen Liquid.
[1971.28 --> 1972.30]  But I didn't.
[1972.44 --> 1978.74]  And WebC seems like a nicer approach that kind of lets me bundle things a little bit more.
[1978.80 --> 1984.08]  But one thing I wanted to ask about was like, does it, so like I saw, you know, it has the
[1984.08 --> 1986.56]  standard markdown or markup that you can put in it.
[1986.56 --> 1990.86]  And script tag and CSI, like it handles those to move them and whatnot.
[1990.98 --> 1996.88]  But does it have some kind of like special tagging or templating for like doing some other
[1996.88 --> 1999.18]  things that I would do with those other templating libraries?
[1999.22 --> 2002.76]  I'm thinking specifically like looping through a collection, for example.
[2003.22 --> 2004.24]  Can it do things like that?
[2004.24 --> 2007.66]  Yeah, we have a JavaScript render function tag.
[2007.80 --> 2012.92]  So you can just write arbitrary JavaScript inside of your HTML and that will render on
[2012.92 --> 2013.36]  the server.
[2014.16 --> 2017.44]  And so, yeah, we have a ton of different extensions built into it.
[2017.54 --> 2022.26]  And you can, with the Eleventy WebC plugin, you can use Liquid inside of WebC.
[2022.26 --> 2026.96]  So, I mean, the possibilities are kind of endless.
[2027.46 --> 2033.24]  But yeah, I would focus on, if you're using WebC, I would focus on maybe trying to move
[2033.24 --> 2039.48]  away from those existing template syntaxes if you can and just go to raw JavaScript.
[2040.10 --> 2041.14]  But some folks like it.
[2041.24 --> 2041.94]  So I don't know.
[2042.04 --> 2043.08]  I'm not going to tell them what to do.
[2043.42 --> 2043.52]  Sure.
[2044.36 --> 2047.92]  I mean, that's one of the perks of Eleventy too, is it's so versatile in what it supports.
[2047.92 --> 2051.78]  So it really should appeal to everyone, theoretically.
[2052.26 --> 2053.48]  That's what I'm trying to do.
[2069.98 --> 2073.08]  Hello, friends.
[2073.50 --> 2076.76]  This is Jared here to tell you about Changelog++.
[2076.76 --> 2083.68]  Over the years, many of our most diehard listeners have asked us for ways they can support our
[2083.68 --> 2084.94]  work here at Changelog.
[2085.18 --> 2087.66]  We didn't have an answer for them for a long time.
[2088.02 --> 2094.76]  But finally, we created Changelog++, a membership you can join to directly support our work.
[2094.76 --> 2101.76]  As a thank you, we save you some time with an ad-free feed, sprinkle in bonuses like extended
[2101.76 --> 2105.96]  episodes, and give you first access to the new stuff we dream of.
[2106.44 --> 2109.86]  Learn all about it at changelog.com slash plus plus.
[2110.06 --> 2113.38]  You'll also find the link in your chapter data and show notes.
[2113.98 --> 2117.02]  Once again, that's changelog.com slash plus plus.
[2117.24 --> 2117.86]  Check it out.
[2118.24 --> 2119.24]  We'd love to have you with us.
[2119.24 --> 2129.40]  Now, where do you see WebC going from here?
[2129.60 --> 2131.28]  Well, actually, let me back up a little bit.
[2131.40 --> 2135.60]  Because one thing that we didn't talk about was like the actual, like everything that we've
[2135.60 --> 2141.78]  kind of talked about right now has just been kind of raw HTML, CSS, and possibly JS.
[2141.78 --> 2147.14]  But if you want it to actually be a web component, then you do have to introduce that client side
[2147.14 --> 2147.84]  JS, right?
[2148.28 --> 2149.42]  Or am I wrong about that?
[2149.94 --> 2150.10]  Yeah.
[2150.24 --> 2155.76]  So the web components specifications, which is kind of like a family of different things
[2155.76 --> 2160.58]  of a bunch of different specs, has a custom elements registry that you can do.
[2160.80 --> 2168.28]  And so that will basically tie an existing HTML element to a JavaScript class.
[2168.28 --> 2174.86]  And so anytime that you add a component with that tag name to your HTML, it will be registered
[2174.86 --> 2178.22]  through this client side JavaScript class that you can use.
[2178.84 --> 2184.44]  And it's really kind of neat because then you don't have to, it works with completely dynamic
[2184.44 --> 2184.84]  pages.
[2185.10 --> 2191.14]  So even if you add elements later in the page cycle, maybe you fetch those with the fetch
[2191.14 --> 2196.24]  JavaScript on the client, it will automatically initialize those components for you if they're
[2196.24 --> 2196.90]  already registered.
[2196.90 --> 2201.58]  So yeah, a lot of that stuff is given to you for free by the platform.
[2202.12 --> 2207.28]  And that's things that you could not do in a competing framework because you would have
[2207.28 --> 2212.90]  to tie into those lower level browser things to be able to, yeah, get that functionality
[2212.90 --> 2213.56]  for free.
[2213.92 --> 2216.64]  So I'm trying to keep as close to the platform as possible.
[2216.90 --> 2217.06]  Yeah.
[2217.16 --> 2221.66]  Just because I don't want to maintain things that will change later.
[2221.78 --> 2224.58]  And the JavaScript ecosystem has so much churn.
[2224.58 --> 2228.28]  I feel like that is just, it's just churning and churning and churning.
[2228.64 --> 2230.92]  And that's just a byproduct of how big it is.
[2231.50 --> 2233.66]  There's just a ton of people working in this space.
[2233.86 --> 2239.32]  And so, yeah, I really try and stay as close to the platform, which moves, it has historically
[2239.32 --> 2240.10]  moved slower.
[2240.26 --> 2246.18]  It feels like it's going much faster now than it has in the past, especially in CSS land.
[2246.30 --> 2250.76]  Man, I just having trouble keeping, keeping up with all the new CSS things that are coming
[2250.76 --> 2250.98]  out.
[2251.50 --> 2251.86]  Same.
[2252.40 --> 2256.66]  But I think that that's a good strategy for outlasting VEAT, like you were saying, like
[2256.66 --> 2262.52]  just for longevity, sticking as close as possible to the platform really probably will pan out
[2262.52 --> 2264.44]  as a huge benefit in the end.
[2264.62 --> 2267.02]  So, yeah, I totally understand that.
[2267.46 --> 2271.94]  Kind of going back to like registering those web components, would the main reason that you
[2271.94 --> 2278.06]  would want to do that as opposed to just keeping it kind of vanilla HTML and CSS, would
[2278.06 --> 2281.70]  that be for like the lifecycle methods of it?
[2281.78 --> 2284.46]  Or is there another reason that you might want to do that?
[2284.72 --> 2284.86]  Yeah.
[2284.94 --> 2291.40]  So if you go to the very first demo that I built with WebC, it does use like a custom
[2291.40 --> 2298.14]  element for just that quintessential like counter demo that everyone builds in JavaScript
[2298.14 --> 2298.62]  frameworks.
[2299.10 --> 2299.72]  Look at this.
[2299.78 --> 2300.50]  It has a button.
[2300.70 --> 2302.28]  It can increment a number.
[2302.80 --> 2307.72]  And that is the thing that everyone loves to see when it comes to new JavaScript frameworks.
[2307.72 --> 2314.06]  So, yeah, I mean, that really allows you to tie in the interactivity to the button for
[2314.06 --> 2316.60]  very easy and cheap way to do that.
[2316.76 --> 2322.56]  So it kind of you can scope your event listeners to those individual elements inside of the
[2322.56 --> 2324.98]  inside of the custom element tag.
[2325.10 --> 2329.10]  And it really sets you off to the races in a much in a pretty nice way.
[2329.18 --> 2330.92]  I really like the authoring experience of it.
[2330.92 --> 2337.80]  And then one other question I had about that was, I think that button, that counter example
[2337.80 --> 2339.26]  is kind of what I'm thinking of here.
[2339.86 --> 2345.18]  You know, on that, in that example, you initialized several counters on the page and they all kind
[2345.18 --> 2345.72]  of had that.
[2345.84 --> 2352.20]  Is 11d or the WebC compiler doing something special to ensure that only the JavaScript for
[2352.20 --> 2355.30]  one of those is getting added to the page at a time?
[2355.30 --> 2360.46]  Yeah, I mean, we deduplicate the client side JavaScript and the client side CSS that comes
[2360.46 --> 2362.40]  out of the individual components.
[2363.50 --> 2367.52]  So I think you'll see similar things in like the Svelte compiler.
[2367.72 --> 2370.04]  I really love the Svelte compiler and how that works.
[2370.54 --> 2373.86]  They really deduplicate the CSS that comes out of that.
[2374.44 --> 2377.60]  And so the same niceties are built into the WebC stuff as well.
[2377.60 --> 2384.06]  So even if you have like seven or eight or nine or 10 instances of that counter component,
[2384.06 --> 2388.10]  you'll only see one instance of the client side JavaScript show up.
[2388.96 --> 2396.56]  And just as a sneak preview, we do have this like cool asset bucketing feature that's built
[2396.56 --> 2397.28]  into WebC.
[2397.96 --> 2405.52]  So I think what a lot of bundlers do is they don't have maybe deep insight into how the page
[2405.52 --> 2406.28]  is marked up.
[2406.28 --> 2412.56]  And so with the WebC asset bucketing feature, you can actually say I have this component.
[2412.74 --> 2418.88]  I want it to load in a different stage of the web pages lifecycle so I can defer this
[2418.88 --> 2421.24]  component's assets to a later time.
[2421.84 --> 2426.68]  And I get full control over where that bucket gets loaded and how that script and CSS gets
[2426.68 --> 2429.58]  loaded because I get to declare that on my page.
[2430.40 --> 2436.26]  And yeah, the next version of WebC, we're going to have some really cool ways to have those
[2436.28 --> 2442.66]  buckets be loaded in a very optimized way in that sometimes you'll want to hoist those
[2442.66 --> 2445.68]  to the top level buckets or bundles.
[2445.88 --> 2449.54]  And we're going to have, yeah, a lot of really cool features come out.
[2449.76 --> 2454.94]  It's going to optimize how those assets are loaded, even when they may not like live in
[2454.94 --> 2458.02]  the same bucket in WebC land.
[2458.02 --> 2463.56]  I know that was very confusing, but hopefully I'll be able to clean it up, clean the marketing
[2463.56 --> 2466.34]  of the feature up when I finish it up.
[2467.30 --> 2470.06]  So that's some really cool stuff that 11d2 can do.
[2470.30 --> 2476.36]  And with WebC, like it really seems like a really great combination for this next generation
[2476.36 --> 2481.06]  of 11d and static site generators, which I'm really excited about.
[2481.16 --> 2484.08]  But I'm curious, what are you thinking comes next?
[2484.74 --> 2491.38]  I mean, I feel like our big flagship feature that we're going to work on for 3.0, which
[2491.38 --> 2497.52]  I'd like to see canaries out pretty shortly for that, is that we're we want to do ECMAScript
[2497.52 --> 2497.92]  modules.
[2497.92 --> 2503.58]  So that's maybe the biggest requested feature for folks in 11d land right now is that we're
[2503.58 --> 2505.68]  still doing common JS templates.
[2506.32 --> 2515.04]  And so I do want a first party ESM story inside of 11d and the ability to use ECMAScript modules
[2515.04 --> 2517.88]  for your configuration file, I feel like is a big one.
[2517.92 --> 2521.04]  And that will unlock asynchronous configuration files, too.
[2521.62 --> 2526.50]  So that should give us a lot of, I don't know, wider compatibility with what configuration
[2526.50 --> 2533.38]  files can do, because I think a lot of times folks end up using event emitter stuff inside
[2533.38 --> 2539.22]  of early 11d events lifecycle to sort of work around the asynchronous limitations of config
[2539.22 --> 2539.90]  files right now.
[2540.12 --> 2542.48]  And yeah, I'd like to clean that up quite a bit.
[2542.56 --> 2544.88]  And I think ESM will do that for us.
[2545.06 --> 2546.50]  So yeah, I'm super excited about that.
[2546.56 --> 2549.72]  I think it's going to be a great addition to 11d for sure.
[2550.30 --> 2555.68]  And you can use 11d in ESM projects now, but your configuration file does need to be
[2555.68 --> 2557.68]  CGS or common JS right now.
[2557.86 --> 2563.88]  So yeah, this is really just going to unlock first party ESM on 11d config files.
[2564.38 --> 2564.58]  Nice.
[2564.82 --> 2567.56]  Just don't take the CGS away, please.
[2567.94 --> 2569.00]  No, I definitely won't.
[2569.18 --> 2570.52]  I don't think I would be able to.
[2571.86 --> 2572.70]  Not a fan?
[2573.32 --> 2573.98]  Not for Node.
[2574.42 --> 2581.02]  Yeah, I do kind of wish that Node's VM module specifically worked better with ESM.
[2581.02 --> 2586.02]  I don't feel like it has a first party, like a, it doesn't work as well as the common
[2586.02 --> 2587.02]  JS version does.
[2587.54 --> 2592.48]  It's, I don't know why it's still an experimental mode, to be honest, because it's, I think it's
[2592.48 --> 2594.66]  been out for years and years and years.
[2594.78 --> 2601.54]  But yeah, if any Node folks are listening, let's get that VM, get that VM package up to
[2601.54 --> 2601.76]  date.
[2602.26 --> 2602.36]  Yeah.
[2602.44 --> 2604.50]  Somebody just has to care enough to do it.
[2604.92 --> 2605.14]  Yeah.
[2605.62 --> 2606.48]  So maybe it's me.
[2606.94 --> 2607.86]  Is that what you're saying?
[2607.86 --> 2608.64]  Maybe it is.
[2608.78 --> 2609.02]  Yes.
[2610.00 --> 2611.36]  That's kind of how Node works.
[2611.74 --> 2611.76]  So.
[2612.28 --> 2612.80]  Open source.
[2613.36 --> 2613.74]  Mm-hmm.
[2614.12 --> 2614.36]  Yeah.
[2614.74 --> 2620.20]  I'm trying to, trying to participate in this conversation, but I heard TypeScript support
[2620.20 --> 2621.68]  in, for all of that.
[2621.76 --> 2623.94]  And so I'm like, why do you need anything else?
[2624.06 --> 2625.10]  Just compile the way you want.
[2625.46 --> 2630.26]  Compilers are another dependency that hampers your long-term maintenance of a project.
[2631.06 --> 2631.46]  True.
[2631.64 --> 2633.48]  I'll just keep repeating that forever and never, never.
[2633.48 --> 2638.46]  I feel like I would use TypeScript features if it was built into the language.
[2639.20 --> 2639.84]  I'm like.
[2640.26 --> 2640.76]  Like Dino.
[2641.84 --> 2642.76]  Is it though?
[2643.26 --> 2644.94]  It's not built into the language.
[2646.82 --> 2648.08]  It's built into the runtime.
[2649.48 --> 2650.50]  Yeah, that's true.
[2650.94 --> 2651.24]  Anyway.
[2651.74 --> 2654.02]  That is a good hair to split, I suppose.
[2656.40 --> 2659.70]  Anything else exciting coming out in 3.0 or beyond?
[2660.18 --> 2661.84]  Any kind of like, I don't know.
[2661.84 --> 2664.82]  And also, I want to ask about like WebC.
[2665.06 --> 2666.26]  Where is WebC going?
[2666.80 --> 2666.90]  Yeah.
[2666.96 --> 2670.42]  I mean, I really think that the coolest thing that's coming out of WebC right now is going
[2670.42 --> 2676.24]  to be like a tighter integration with our island is land partial hydration component,
[2676.38 --> 2676.82]  web component.
[2677.66 --> 2683.92]  And so, yeah, you'll see a lot of really cool sort of automated bundling features in that.
[2683.92 --> 2693.66]  So, and I feel like that is like really diving WebC into some application use cases, even
[2693.66 --> 2697.22]  though I don't really buy into the sites versus application dichotomy.
[2697.56 --> 2704.54]  But I mean, islands kind of gets you more in the direction if you like have that continuum
[2704.54 --> 2705.96]  of sites and apps.
[2705.96 --> 2711.46]  It really, the islands architecture really does satisfy a lot more of those requirements.
[2711.86 --> 2711.88]  So.
[2712.42 --> 2717.76]  You're going to have to define islands for some of us, unfortunately.
[2718.40 --> 2720.72]  Islands is just a fancy way to say lazy loading.
[2721.70 --> 2725.86]  And I know that's a very spicy take, but I'm sticking to it.
[2726.66 --> 2728.22]  It's a spicy lazy loader.
[2728.30 --> 2729.14]  That's all it is.
[2730.86 --> 2732.38]  We've rebranded the term.
[2732.38 --> 2737.30]  Yeah, I know that there's been a lot of discussion in the last couple of weeks about like the
[2737.30 --> 2740.60]  overlap between islands and progressive enhancement.
[2740.94 --> 2747.40]  And I really do think that islands is kind of a separate consideration from progressive
[2747.40 --> 2747.84]  enhancement.
[2748.60 --> 2751.68]  Yeah, it's more a lazy loading thing than it is a progressive enhancement thing.
[2751.72 --> 2756.96]  And there is overlap between the two, obviously, but you can have something that is an island
[2756.96 --> 2758.60]  that has terrible progressive enhancement.
[2758.60 --> 2762.10]  So I think in Astro, you can do like a client only component.
[2762.38 --> 2764.20]  I think if I'm correct.
[2764.38 --> 2767.02]  And that has very bad progressive enhancement, right?
[2767.22 --> 2772.54]  Because there's if if you don't have JavaScript, it's not going to even show the component.
[2772.74 --> 2778.82]  So and that might be for something on your page that is not like the core use case of the
[2778.82 --> 2780.26]  page that might be perfectly acceptable.
[2780.26 --> 2785.74]  But yeah, you do need control over as it goes back to the original.
[2785.96 --> 2789.58]  The thing I was saying earlier, you need full control over the progressive enhancement of each
[2789.58 --> 2792.84]  individual component on the page and how it loads.
[2792.92 --> 2794.28]  It really ties into that.
[2794.94 --> 2796.14]  So I hope that answered your question.
[2797.02 --> 2799.60]  Yeah, no, I think that's a good summary of it.
[2799.60 --> 2805.14]  And there's a page on on like Astro's Islands that we can put in the show notes that I think
[2805.14 --> 2811.10]  comes from a post by Jason Miller, who created Preact, kind of talking about that terminology.
[2811.66 --> 2815.94]  And I know that that like you mentioned fresh earlier, fresh, I think, is built all around
[2815.94 --> 2817.36]  this concept of islands.
[2817.36 --> 2820.92]  So another cool framework to to look into there.
[2821.20 --> 2823.34]  Now, you were talking about progressive enhancement.
[2823.84 --> 2826.16]  And I don't mean this to be a trolling question.
[2826.16 --> 2829.24]  And I'm not trying to like get a spicy answer or anything.
[2829.24 --> 2835.30]  I'm just genuinely curious your thoughts on the the idea that JavaScript would be turned
[2835.30 --> 2835.60]  off.
[2835.72 --> 2837.42]  Is that a legitimate thing?
[2837.72 --> 2838.16]  Do you think?
[2838.64 --> 2840.36]  I mean, that's not really how I think about it.
[2841.22 --> 2846.14]  That's not like a core use case that is like in my brain as something that I want to solve
[2846.14 --> 2847.16]  for the sites that I build.
[2847.16 --> 2853.00]  I more think of it as at each stage of pages load.
[2853.00 --> 2856.56]  And how does that look when it's while it's loading?
[2856.56 --> 2862.10]  So, yeah, I'm trying to like, yeah, I think that there's like a classic Jake Archibald tweet,
[2862.22 --> 2866.64]  which is which talks about it's not really about having JavaScript disabled.
[2866.80 --> 2870.22]  It's about what the page looks like before JavaScript has loaded or initialized.
[2870.50 --> 2870.58]  Yeah.
[2870.72 --> 2874.28]  Now, a lot of folks work around that by rendering on the client, which is terrible.
[2874.54 --> 2875.42]  But yeah.
[2875.42 --> 2875.46]  Yeah.
[2875.90 --> 2876.10]  Yeah.
[2876.10 --> 2879.02]  That's a different I guess that's a different problem and a different story.
[2879.40 --> 2880.14]  No, totally.
[2880.30 --> 2884.88]  And I I didn't mean like I said, I wasn't trying to get like a drama filled answer out of that
[2884.88 --> 2890.78]  or anything or but I kind of started thinking about that as I was watching that demo of
[2890.78 --> 2893.46]  you with the with the counters with WebC.
[2893.46 --> 2898.78]  And you had like a Chrome plug in that was you're toggling JavaScript on and off showing that.
[2899.22 --> 2901.32]  And I think you really did a good job of highlighting.
[2901.72 --> 2909.96]  Like when I turn JavaScript off, this is like the the intermediary step of like this component hasn't loaded like the JavaScript of it hasn't loaded and hydrated yet.
[2909.96 --> 2920.50]  So this is what it's going to look like when it's in that state versus I'm I'm pushing for this like use case where somebody has JavaScript completely turned off.
[2920.64 --> 2928.84]  It was more like what happens before this hydration, the problems and then like, you know, a network latency and things like that can really exacerbate that time.
[2928.84 --> 2935.54]  So having the component not be clickable in that state was a really good thing because it just wouldn't wouldn't do anything.
[2935.60 --> 2937.52]  It would be a confusing experience for the user.
[2937.62 --> 2939.00]  So I totally get that.
[2939.08 --> 2946.46]  The no JavaScript thing is like a use case only for hacker news commenters as far as I can tell.
[2947.08 --> 2948.60]  Well, I think this is a good example.
[2949.00 --> 2958.76]  This is a good example of like using that as a it's almost like a dev tool to show kind of intermediary steps where JavaScript failed for some reason or something along.
[2958.84 --> 2961.52]  Those lines to where you're not in the state that you expect.
[2962.38 --> 2962.46]  Yeah.
[2962.50 --> 2970.40]  And on the image comparison demo that I have up, I actually used an island with like a max width of viewport max width of zero.
[2970.40 --> 2975.26]  So it would never hydrate to show in a side by side way.
[2975.46 --> 2978.74]  Here's the no JS version versus here's the JS version.
[2979.66 --> 2988.82]  So that's another way that I've used in demos, at least to show the pre I would call it the pre JavaScript version of of how it renders versus the.
[2988.84 --> 2990.50]  Post JavaScript version of how it renders.
[2990.50 --> 3003.94]  And I think just going back to that that counter demo, I think I have it set up where it will actually start with an input type number and it toggles it to a I think an output element when the JavaScript renders.
[3003.94 --> 3014.06]  So even if you're interacting with the component before the JavaScript has loaded or your bundle has loaded, you still get a form element that you can increment and decrement.
[3014.06 --> 3035.12]  And yeah, I think we've all sort of had that experience of being on the subway or being on a train or something and and the page doesn't load all the way or you're driving around in the passenger seat of a car looking at your phone and you go in between towers or something and and the connectivity gets in a not solid.
[3035.12 --> 3042.16]  So yeah, so just trying to handle as many of those cases as possible to make the page as robust as possible to totally.
[3042.92 --> 3050.48]  Now, one more question that I have is with WebC and I haven't looked at like the the underlying code for it and how you're doing it all.
[3050.54 --> 3052.76]  But I assume that that's like effective.
[3052.88 --> 3055.86]  It is like a WebC compiler for lack of a better word.
[3055.86 --> 3058.52]  Right. Like it's doing that some kind of compilation.
[3059.04 --> 3069.08]  Yeah. It uses the parse five HTML parser, which is like the standards based parser for that includes all the weird quirks that go into HTML parsing.
[3069.24 --> 3072.76]  So you get the same exact parsing experience that you would expect.
[3073.00 --> 3082.90]  And then, yeah, we just basically have a serializer, our own custom serializer that iterates over that AST that comes back from parse five and creates a HTML representation of that.
[3082.90 --> 3092.08]  So nice. Now that Eleventy has this taste for compilation through WebC, do you see compilation expanding anywhere else going forward?
[3092.32 --> 3095.76]  I don't know what you're alluding at, but no, I don't think so.
[3096.16 --> 3098.40]  Or at least I have no short term plans for that.
[3098.90 --> 3102.20]  I'm not even sure the context of the question in a larger sense.
[3102.60 --> 3103.74]  Is there something you had in mind?
[3104.12 --> 3105.94]  No, not really. I suppose.
[3105.94 --> 3113.00]  I'm just curious, like, are there more use cases that you could solve for with that compilation?
[3113.54 --> 3115.90]  But it has a lot of tradeoffs the other way.
[3115.98 --> 3118.76]  So I'm not sure if that's a direction you wanted to go.
[3119.42 --> 3129.52]  Yeah. I mean, I think that this is like the template syntax stuff and the processing of HTML and WebC is maybe as far as I'd want to go.
[3129.52 --> 3134.10]  And I think I'd farm out the rest of this stuff to other projects if folks want to use it.
[3134.66 --> 3140.06]  So if you want to extend your own CSS processing pipeline into WebC, you can do that.
[3140.16 --> 3144.64]  You can actually override our WebC scoped behavior with your own custom behavior.
[3144.64 --> 3148.80]  If you want to write your own scoped CSS implementation.
[3148.80 --> 3156.56]  If you want to wire up Babel to do JS processing or whatever, you can do that if you want.
[3156.72 --> 3160.94]  But again, I'd come back to do you want to add all those extra dependencies?
[3161.46 --> 3167.36]  I think that I don't know the temptation when folks work on projects is they want to work on the cutting edge.
[3167.36 --> 3177.68]  They want to work on the very newest features that come out before they're sort of GA or before they're supported in browsers on the client specifically.
[3177.68 --> 3183.84]  And you get into this weird trap where you add these dependencies to process this stuff.
[3184.18 --> 3189.76]  And maybe the specification changes or maybe the preprocessor went ahead of things.
[3189.76 --> 3198.24]  You saw that a lot in CSS and JS implementations where they just couldn't keep up with the specifications that were coming out.
[3198.76 --> 3202.44]  I think a lot of folks have maybe some issues with Tailwind in the same way.
[3202.44 --> 3209.92]  Where it almost seems like Tailwind is having trouble keeping up with the speed of features that get delivered in CSS world.
[3210.38 --> 3211.54]  And I don't know if that's actually true.
[3211.64 --> 3223.00]  But you see that it's like the same like you add a layer or an extra dependency to work ahead of the game in a way to try and get access to these cutting edge features.
[3223.00 --> 3224.72]  And it really can come back to buy you later.
[3224.72 --> 3227.42]  So I've just exercised caution.
[3227.82 --> 3229.74]  He just wants to use TypeScript in the WebC.
[3230.16 --> 3230.34]  Okay.
[3230.72 --> 3232.00]  TypeScript in browsers.
[3232.50 --> 3233.72]  Implement TypeScript in browsers.
[3233.92 --> 3236.28]  It says WebC type JS.
[3236.74 --> 3240.24]  And he wants that to say TS instead of JS.
[3240.78 --> 3241.18]  That's true.
[3241.28 --> 3242.18]  That's what Nick wants.
[3242.88 --> 3245.96]  Nick gets commission every time he converts a project to TypeScript.
[3247.42 --> 3248.66]  Brought to you by Carl's Jr.
[3248.66 --> 3256.66]  Yeah, I guess I was trying to ask if Eleventy Lang or something was coming down the pipeline later.
[3257.32 --> 3262.82]  But no, I think that's a great answer and a great way to wrap up this show.
[3263.44 --> 3267.50]  Zach, before we do, where can folks find you these days?
[3267.50 --> 3270.16]  Well, you can go to the Eleventy Docs, eleventy.dev.
[3270.86 --> 3274.00]  And also, Zachly.com is my website.
[3274.00 --> 3276.84]  And I'm pretty active on Mastodon now.
[3276.96 --> 3280.82]  So if you want to be friends on Mastodon, find me there through my website.
[3281.20 --> 3282.20]  Yeah, it's a fun place.
[3282.92 --> 3283.22]  Well, cool.
[3283.36 --> 3284.66]  Thank you so much for joining us.
[3284.84 --> 3290.02]  We will just go ahead and pre-schedule you for a year from now to talk again about...
[3290.02 --> 3290.62]  Sounds good.
[3291.04 --> 3291.90]  WebC version 2.
[3292.08 --> 3293.02]  WebC 2, yep.
[3293.20 --> 3294.10]  Eleventy Scripts.
[3294.24 --> 3295.54]  You heard it here first.
[3296.42 --> 3297.12]  Eleventy Conf.
[3297.64 --> 3300.72]  And all these other things I can pre-sign you up for.
[3300.76 --> 3301.18]  Oh, no.
[3301.68 --> 3302.80]  Yep, exactly.
[3304.00 --> 3306.50]  Yeah, so thank you so much for joining us.
[3306.66 --> 3307.36]  Thank you, Chris.
[3307.50 --> 3309.36]  And this party is over.
[3309.72 --> 3311.68]  Thank you, Zach, for your work on Eleventy.
[3311.94 --> 3312.40]  Oh, yeah.
[3312.54 --> 3313.10]  Thank you.
[3313.46 --> 3314.46]  Thanks for using it.
[3324.52 --> 3325.54]  All right.
[3325.68 --> 3327.54]  That is JS Party for this week.
[3327.72 --> 3328.42]  Thanks for listening.
[3329.38 --> 3333.24]  Zach isn't the only one hanging out on Mastodon these days.
[3333.24 --> 3338.10]  You can connect with us on the Fediverse at JSParty at changelog.social.
[3339.02 --> 3342.74]  Oh, and did you know we're also on Insta, TikTok, and YouTube?
[3343.40 --> 3350.42]  Search for Changelog in your favorite short form video playing thing, and you'll find a bunch of fun clips from all of our shows.
[3350.42 --> 3357.22]  Thanks once again to our partners, Fastly and Fly for helping us bring you JS Party each and every week.
[3357.52 --> 3360.84]  Check them out at Fastly.com and Fly.io.
[3360.84 --> 3366.24]  And thank you to our beat master in residence, the mysterious Breakmaster Cylinder.
[3366.94 --> 3367.80]  So mysterious.
[3368.46 --> 3369.32]  So Cylinder.
[3369.32 --> 3379.72]  Next up on the pod, Dan Abramov and Joe Savona from the React team sit down with Nick and I to discuss React's place in the front end ecosystem.
[3379.72 --> 3395.16]  They also respond to recent SPA fatigue and React criticisms and explain to us in detail all about React server components, what they are, where they fit in, and where they're taking the next big version of React.
[3395.92 --> 3397.22]  Stay tuned for that.
[3397.54 --> 3399.42]  We'll have it ready for you next week.
[3399.42 --> 3409.76]  Game on.
