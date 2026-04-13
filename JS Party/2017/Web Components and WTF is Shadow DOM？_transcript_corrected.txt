[0.00 → 5.22] Bandwidth for JS Party is provided by Vastly. Learn more at Fastly.com.
[9.14 → 13.22] Welcome to JS Party, a weekly celebration of JavaScript and the web.
[13.58 → 18.52] Tune in live on Fridays at 3 p.m. U.S. Eastern at changelaw.com slash live.
[18.88 → 22.90] Join the community and Slack with us in real time. Head to changelaw.com slash community.
[23.42 → 27.16] Follow us on Twitter. We're at JS Party FM. And now on to the show.
[27.16 → 32.38] Hey, everybody. Welcome to JS Party, where it's a party every week with JavaScript.
[32.84 → 36.80] We're going to talk a bit about web components, conferences, and processing today.
[37.54 → 38.64] Cool. Fun stuff.
[39.04 → 39.38] Yay.
[39.64 → 41.04] Let's get...
[41.04 → 44.62] Can you help me actually? Did you say web component conferences?
[45.14 → 47.04] The conferences specifically for web components?
[47.54 → 50.18] Yes. Yes. That's the topic. Those aren't two topics.
[50.64 → 53.54] I love the conferences about radio buttons.
[54.48 → 55.04] Hmm.
[56.00 → 56.44] Yeah.
[57.16 → 63.86] All right. So, uh, let's, let's, let's get into web components and custom elements and things.
[64.34 → 65.80] Shouldn't we say who we are?
[66.64 → 70.02] Oh, yeah, that's right. That's right. People don't know who we are. I'm Michael Rogers.
[70.36 → 73.40] We've also got Alex Sexton. Say hello.
[74.52 → 74.78] Hello.
[76.28 → 78.60] We've also got Rachel White. Say hello.
[79.28 → 79.68] Hello.
[79.68 → 84.82] We just brought the we just brought the pace way down. It's getting like smooth jazz pace now.
[84.98 → 88.66] I actually, I actually think, Michael, that your lag is high today.
[89.98 → 91.18] Oh, really? Is that what it is?
[91.34 → 92.18] Yeah. Correct.
[92.26 → 92.38] Okay.
[92.38 → 100.82] Uh, everyone else seems to be, uh, normal. Um, and whenever we talk to you, it takes you like a long time to reply.
[100.82 → 110.38] Well, I apologize. Um, Alex, why don't you tell us what web components are and what the whole deal is with custom elements and what the hell is a shadow dumb?
[110.38 → 126.20] Um, um, web components are the web standards, um, version of kind of the, the popular component driven model that people like to develop web applications in today.
[126.38 → 137.26] So the best way to think of web components, in my opinion, is to think about the current web platform, um, and think about how the things are implemented behind the scenes.
[137.26 → 144.62] So in the past, we've had a button element or a radio button element or a checkbox or a select menu.
[145.86 → 160.40] And, uh, in the really early days, this wasn't true, but for the last long time, if you were to go look at the browser implementation of a select box or an input element, it's just HTML, CSS, and JavaScript behind the scenes.
[160.40 → 168.68] It's, it's, it's implemented in the web platform, but it's behind this, uh, opaque thing called a button or this opaque thing called a select menu.
[169.30 → 177.24] Um, and so because of that, there was this disconnect on what the browsers could offer you versus what, uh, other web developers could offer.
[177.72 → 185.16] Um, and because of this, um, we wanted to shorten, uh, and small in that gap.
[185.16 → 188.98] And, uh, that's what web components are for.
[189.18 → 204.90] So, um, web components are so you could make your own button, um, that has not quite an opaque, uh, of an API, but you, you can make your own components that are standalone that you can pull into a page and use just as if you were using a button or a select.
[204.90 → 213.24] You could use the Alex button or the Michael button or the Michael select or the clock or the social widget component.
[213.50 → 226.02] So kind of like, uh, the React world or the Ember world where you're making these, uh, discrete components that have their own APIs and then using them, uh, as units, uh, of development.
[226.16 → 226.94] You can do that.
[227.02 → 228.10] It didn't necessarily come from that.
[228.10 → 236.44] It came before, um, I think both of those were super popular ideas, but it certainly has taken a longer ramp time as the standards track normally does.
[236.80 → 240.70] We can get into some of the technical implementation details of how this works.
[241.28 → 252.28] Um, but I also think you might've mentioned the shadow DOM already, and that's really just the DOM that, uh, exists inside the component rather than to the developer once they're using your components.
[252.28 → 261.46] So if you think about the old button, technically there's a span and a DIV or whatever inside there, inside the button, but that's not exposed to developers.
[261.70 → 272.06] And so in that same way, whenever you build the clock, uh, component, you don't have to expose all the different spans and DIVS and, uh, things inside your clock component.
[272.18 → 277.18] It just is a clock, and it's not necessarily like CSS selectable from, from outside.
[277.18 → 286.98] So is it just rendering these components in a cleaner way than having to, um, you know, like append all of those other things that exist inside the regular component?
[287.66 → 289.56] Well, everything still exists.
[289.62 → 296.98] It's like, you could take away the idea of, uh, web components, um, and, and shadow DOM or whatever.
[296.98 → 308.20] And it would just be a larger DOM with a lot more stuff in it with a lot more like, uh, like CSS scoping and, and, uh, there's a lot more chance for bleeding together of certain things.
[308.20 → 316.38] But yeah, uh, like there's nothing like super special about them, which is why they're so important, I think, for the future.
[316.38 → 330.18] Um, right now, uh, a lot of the, uh, like React and Ember model relies on whole massive libraries being able to run and execute and, and stuff prior to be able to see or use anything on the site.
[330.24 → 343.74] Whereas these web components can, since they utilize more of the web stack, the web stack can, uh, do a better job of rendering them instantly without, uh, as much work and execution of JavaScript and all that kind of good stuff.
[343.74 → 358.24] So it is more of the web platform, um, which isn't to say that like, as time goes on, I think, uh, Ember and, and React can start to kind of merge their different strategies to where you can write React like code and end up with web components.
[358.42 → 360.30] Um, which, which I think is totally possible.
[361.06 → 361.16] Cool.
[361.88 → 370.72] So I'm like trying to read this as you go through, because I've honestly, you know, like I hear the term shadow DOM thrown around a lot and.
[370.90 → 371.80] It's a very cool word.
[372.40 → 372.74] Yeah.
[372.74 → 372.78] Yeah.
[373.58 → 375.64] I mean, I could, you have to whisper it.
[377.06 → 382.74] It's one of those things that like, if you asked me what the shadow DOM was, I could make up a lot of stories about what it definitely isn't.
[383.54 → 396.58] Um, is, is there a way, I guess I'm, I'm, I'm, the site that I'm looking at right now is from the like the developers.google.com site about, um, the, the primers and getting started with the shadow DOM.
[396.58 → 397.58] Um, and they're talking about light DOM.
[397.58 → 400.48] Um, and they're talking about light DOM versus shadow DOM.
[400.48 → 410.58] Um, and they're showing, you know, um, an example that has a little bit more robust write-up or markup in it for the light DOM version.
[410.58 → 417.86] So with the shadow DOM, are you even seeing of the other components?
[417.86 → 422.76] If I was going to like to use dev tools and inspect it just like out of the box?
[423.76 → 423.88] Yeah.
[423.98 → 430.36] Dev tools, I think allows you to currently inspect shadow DOM of, of web components, not of native browser components.
[430.36 → 438.18] But yeah, kind of the whole, the whole idea is that like you can have a CSS class in, in their called button.
[438.86 → 448.22] Um, like it literally just updates all the button tags and that you no longer have to have like a super specific, uh, CSS class name added to that.
[448.28 → 449.22] I mean, you probably should.
[449.36 → 449.72] Yeah, yeah, yeah.
[449.82 → 450.48] Maybe whatever.
[450.48 → 454.88] But like the whole idea is that it's completely scoped to inside that web component.
[455.16 → 458.56] That way, uh, everybody can style their own web components however they want.
[458.56 → 461.24] And there's no worry about collision of those things.
[461.88 → 462.28] Okay.
[462.52 → 462.78] Yeah.
[462.86 → 465.52] I guess that does make a lot more sense if you're thinking of React.
[466.12 → 468.46] Especially if you're pulling in components from other people.
[468.94 → 477.68] So if so-and-so styled this button and so-and-so styled this clock and whatever, there's like in the React world, there's a there's a higher chance for collisions.
[477.68 → 486.40] And, uh, like the even like the box model, like one relies on the newer box model, one relies on the, you know, things like that, uh, are going to all change.
[487.18 → 487.30] Cool.
[487.30 → 492.62] So why is this stuff important to know for people that don't know what it is?
[493.58 → 508.38] Um, I think web components, uh, are definitely like, I think it's, uh, unfortunately a longer term vision for the web than it would have been if people didn't make such good user, uh, land libraries to do similar things.
[508.38 → 518.64] So I think there's like this very similar world to where we live in alternate universe where React didn't come out and Ember didn't do the component kind of version of their views.
[518.64 → 521.40] And web components really takes off.
[521.40 → 525.36] I think Polymer, uh, and web components get confused a lot.
[525.46 → 532.38] Polymer is kind of like a, uh, a library on top of web components that allows you to, to do a bunch of extra stuff.
[532.38 → 541.54] Um, like the React and Ember libraries would kind of offer you, including like building and, and, uh, fallbacks and all sorts of, uh, fun stuff.
[541.54 → 560.54] But I think, uh, if we want to get to a world where the web works as well as native applications on bad internet connections, uh, in slow mobile browsers, uh, then I think the web components vision is one of the few ones that literally can do that as well as a native application.
[560.54 → 568.12] Because it is using like native, uh, code in order to do the initial renders, and it can do layout better.
[568.28 → 574.40] It can do less, far less JavaScript execution, um, before it can render and all sorts of things.
[574.40 → 582.82] So it's able to utilize the web platform in a much more efficient way, which means that you can serve a wider audience and have a faster, better experience.
[583.54 → 583.64] Cool.
[584.58 → 590.16] So you mentioned that like, you know, React and Ember and a few people do stuff kind of like this, right?
[590.16 → 593.00] Um, well, it's fundamentally different.
[593.26 → 593.36] Yeah.
[593.38 → 593.50] Yeah.
[593.50 → 597.80] But you can like to create a class, and then you get a constructor that happens when you create these elements, right?
[597.82 → 598.54] Which is great.
[598.80 → 604.66] Um, and you do, you have ways to do that in all these different abstractions, but you didn't have a way to kind of do it natively.
[604.98 → 611.02] Other than the, the CSS scoping stuff, which is brand new, you can't really do that very effectively with tooling.
[611.12 → 611.96] It's really, really hard.
[611.96 → 619.16] Um, are there any aspects of web components that actually just give you abilities that you just never had before?
[620.16 → 631.56] Uh, there are things like people talk about element level media queries instead of like window level and the shadow DOM can kind of give you a an approximation of that, which is nice.
[631.56 → 639.40] Um, trying to think there are different like lifecycle events that like don't necessarily occur anywhere else except for in these components.
[639.40 → 645.58] Like a lot of the things that are available to you outside now were created for the purpose of web components.
[645.70 → 652.76] Like the template tag was created for the purpose of this as well as the shadow DOM is separate from the, uh, web component spec.
[652.76 → 656.12] And so you can kind of use it outside of web components.
[656.20 → 657.66] I, I assume, I don't know.
[657.76 → 659.70] It kind of can land in browsers beforehand.
[659.84 → 660.46] So I assume you can.
[660.98 → 663.78] So some things we already use are part of that.
[663.88 → 664.64] So I don't know.
[665.02 → 667.66] Some of it leaks back into the, the top level.
[668.16 → 670.94] Um, I need to look it up, but I'm sure there are a few things.
[671.84 → 671.88] Yeah.
[671.92 → 676.00] I'm actually using some shadow DOM stuff in it, in a thing that I'm not using web components at all for.
[676.12 → 680.24] Um, and it's, it's really useful just for that, that element scoped CSS stuff.
[680.24 → 680.68] Yeah.
[682.96 → 683.52] Yeah.
[684.78 → 687.32] Are we, are we done talking about web components?
[688.46 → 692.74] So there was a question, uh, in the chat, uh, did Google start this?
[693.70 → 702.56] Um, I think that while the, the Google people, uh, I think were the ones, this is all came out of the web manifesto.
[702.64 → 706.76] Um, I, I believe, uh, so that was a large amount of Google people.
[706.76 → 712.66] And I think the core authors of the specification, uh, started Google, but it is not a Google only thing.
[712.72 → 719.38] It is a specification in the W3C that has passed and is real and, uh, is in, uh, multiple browsers and things.
[720.04 → 724.14] So I think it is of Google, but not solely by Google.
[725.08 → 725.32] Right, right.
[725.36 → 732.34] I think you, you, you address the polymer thing where people tend to conflate this with polymer and polymer is a Google thing, uh, like very directly.
[732.34 → 734.10] Um, but this is much larger.
[734.94 → 744.36] I think one of the core problems there specifically was in the beginning, no browser implemented web components, but you could effectively use them if you used polymer.
[744.56 → 748.62] And so for a while, the only way to use web components was with polymer.
[748.62 → 756.92] And, and I think that kind of history caused this conflation versus, uh, other similar situations that that didn't happen in.
[757.78 → 757.80] Yeah.
[757.90 → 766.40] That, that's kind of a funny thing though, when you think about it, because one of the big benefits that they continue to talk about is that you don't need a bunch of JavaScript in order to do this.
[766.40 → 768.02] Like you don't need this giant library.
[768.14 → 769.46] That's, that's the benefit.
[769.46 → 773.78] And then people are conflating it with this giant library to do it before it was in the spec.
[773.78 → 774.06] Yeah.
[774.86 → 777.34] I think it is pretty fundamentally different though.
[777.54 → 783.92] Um, a, the size of polymer is pretty different from the size of, uh, say Amber or, or similar things.
[783.92 → 791.02] Uh, but also you can get initial renders and like working things before you have like full polymer execution.
[791.02 → 796.64] Like you can, you can see the page because it's CSS and HTML and the JavaScript hasn't executed yet.
[796.76 → 801.62] And, and that is, I think pretty fundamentally different thing than the other stuff.
[801.62 → 809.54] Well, do you think then that, like we talked a bit about react and Ember kind of eventually moving their implementations towards using web components.
[809.54 → 814.42] Do you think that this is going to be something that we, we just changed the way that we build our tools on top of them?
[814.42 → 817.70] Or is it actually a new enough model that it's going to change the tools that we build?
[817.70 → 821.64] Like, are we going to build very different tools and react and all of that in order to take advantage of this?
[822.52 → 822.58] Yeah.
[822.66 → 831.48] I definitely don't think that you could just take the current react and then like throw web components over the top of it, but you could take a very similar, like react.
[831.62 → 834.70] Uh, whatever we're on, uh, 16 or whatever.
[834.88 → 836.32] No, they have 16th react.
[836.74 → 837.68] Call it just 20.
[837.80 → 846.70] Um, could like, they could theoretically change a bunch of the API and then be outputting different things at the build stuff, but it would be a pretty huge leap.
[846.70 → 848.42] I wouldn't actually expect it to really happen.
[848.42 → 857.78] It would be more like some new person says, okay, the initial renders for web components are insane, but I don't like writing raw web components.
[857.78 → 860.94] It's here's this very reactive model that can do these things.
[860.94 → 873.90] Um, uh, one of the fundamental things I think, uh, that, that web components adds, uh, is the ability to do some of the, uh, data binding that, uh, some of these libraries do via Dom diffing and re-rendering every time.
[873.90 → 878.56] Uh, so I think that is actually another interesting reason to use it.
[878.72 → 890.42] Um, not necessarily like a killer because a lot of that's very fast and can get faster and all sorts of that stuff, but it's certainly an interesting thing where you can kind of bind to two sections together.
[890.42 → 897.22] You can bind, uh, properties on attributes of the, uh, web component to the inside of the web component.
[897.66 → 908.60] But yeah, I wouldn't expect that really react or Ember ends up with like a web component version, but someone would do the React for web components, and it's called we act or whatever.
[908.90 → 911.46] And that becomes a cool popular thing.
[912.42 → 912.94] Interesting.
[913.18 → 914.04] Very interesting.
[914.04 → 931.20] I'm trying to play out in my head, like how, how much of the web affects this, like in the future is like the way that, um, say if you use Stripe for instance, or, uh, I was using like the Tito embed the other day, like you get this JavaScript include.
[931.76 → 935.02] And, um, and then you kind of use like this custom element.
[935.02 → 942.08] And right now it has to do like all this crazy stuff to like to find that element and, and do a bunch of stuff kind of after load.
[942.08 → 948.44] Is it really going to change the model of how that kind of stuff is implemented where when you're like, Hey, you know, include my custom element in your page.
[948.74 → 951.84] Is it, is it going to work like really differently and a lot smoother than it does today?
[952.56 → 958.56] Yeah, I think, um, there, there are HTML imports, which I don't know if I have made it in, uh, to browsers yet.
[958.56 → 964.18] And there, there are a few things that, that make a lot of those things really cool.
[964.46 → 972.06] Um, so I, I have implemented a long time ago, uh, the, the Stripe JS, uh, credit card form as a web component just internally to try it out.
[972.08 → 985.28] And like the amount of work that I have to do to style safely and do all the third party JavaScript things in the current world versus the web component world is pretty vastly different.
[985.28 → 995.10] Uh, and, and the speed at which our component can kind of render and then be attached versus execute the JavaScript and then be injected, um, is also pretty different.
[995.10 → 1003.24] And if we know one thing about the performance of checkout pages is that like everybody who's ever tested is like, this matters a lot.
[1003.82 → 1010.46] So, um, I think it could be a pretty good fundamental change, uh, in the direction of rendering.
[1010.46 → 1020.70] And, and I think that that's what a lot of, like a lot of the cool wins are the modularity and the composability and the scoping and all those things that we've had trouble with on the web whenever you're building a large application.
[1020.88 → 1025.08] And I think those will be the things that people think about more than, than some of this stuff.
[1025.40 → 1032.52] But, um, the kind of the fundamental turn is that things can render and exist prior to JavaScript executing.
[1032.52 → 1049.10] And, and so the, uh, server side rendering isomorphic stuff changes in the way, like you don't necessarily need to do rehydration, uh, as much as you can do, uh, just like render things as web components.
[1049.10 → 1051.22] And then the JavaScript can, can kind of run after.
[1052.20 → 1053.04] What is rehydration?
[1053.16 → 1054.42] You just ran over that one.
[1055.14 → 1055.94] Oh, sorry.
[1056.06 → 1058.54] Uh, rehydration and a server side render.
[1058.54 → 1068.28] So, so like the competition to web components in the, in the, uh, world of frameworks these days is that you can get no JS to render your entire page.
[1068.58 → 1073.74] Uh, and as long as that is a deterministic output, uh, the render is a deterministic output.
[1073.74 → 1077.66] You can, you know, like to HTML it and then serve it as the initial load.
[1077.66 → 1083.10] And so, uh, no JavaScript has run, and it's just CSS and HTML and you can see the entire page.
[1083.16 → 1086.24] And I don't know if it works yet, but, uh, you can see the entire page.
[1086.24 → 1096.96] And then, uh, because that same render function can then run once the JavaScript has executed, it can come up with the exact same deterministic DOM that Node.js did.
[1096.96 → 1114.94] And instead of killing the whole page and then re-rendering it with the, the client side JavaScript, it can just kind of attach itself to the server side rendered thing and say, we claim these, uh, elements as the ones that we would have rendered had they not already existed.
[1114.94 → 1119.28] Kind of like a re-render that, uh, that occurs in, in React all the time.
[1119.36 → 1126.26] It's, it's kind of, uh, a basic property of React is that if you try to render something and all of it's still there, it's a no op.
[1126.32 → 1127.26] It's kind of the DOM diff.
[1127.34 → 1134.38] It's what's the diff between this virtual DOM that we created based on all the data and the one in the actual, uh, window.
[1134.38 → 1142.38] And if there's no difference, we won't do anything, but we'll kind of know that all these things are attached to like all of our handlers and stuff like that.
[1142.58 → 1145.06] So, uh, that's what rehydration is.
[1145.12 → 1150.66] It says, um, we can just attach ourselves to a server side rendered page without re-rendering it.
[1150.70 → 1161.52] And that is a pretty good, like if you, if you need speed, if you're a content website, especially you need speed and SEO and all that stuff, you should absolutely be doing a server side rendering with, with, uh, rehydration.
[1161.52 → 1166.16] Well, you just mentioned SEO, which means it's time for a break, and we get off this topic.
[1166.54 → 1169.62] So, so we're going to take a quick break.
[1169.76 → 1171.48] Uh, when we come back, we're going to talk about conferences.
[1172.84 → 1178.64] First sponsor of the show today is our friends at Century, helping you find and fix your errors in your applications.
[1179.18 → 1180.74] You can start tracking your errors today.
[1180.84 → 1181.58] Totally free.
[1181.84 → 1187.16] They support React, Angular, Ember, Vue, Backbone, and Node 3 more like Express and Koa.
[1187.16 → 1198.14] You can view actual code and stack traces, including support for source maps, see the errors URL, parameters, and session information, and even prompt your users for feedback when you have front end errors.
[1198.48 → 1200.30] Head to changelaw.com slash century.
[1200.50 → 1202.00] Start tracking your errors today for free.
[1202.34 → 1203.28] No credit card required.
[1203.56 → 1204.86] Get off the ground with their free plan.
[1205.16 → 1207.72] And when you're ready to expand your usage, simply pay as you go.
[1208.10 → 1210.58] Once again, changelaw.com slash century.
[1210.86 → 1211.96] And now back to the show.
[1211.96 → 1216.06] Now we're going to get into conferences a little bit.
[1216.40 → 1220.34] So, um, JavaScript has an amazing conference scene.
[1220.56 → 1223.66] There's a million, uh, little community conferences out there.
[1223.74 → 1225.90] It's really exploded in the last few years.
[1226.06 → 1228.66] Um, and we're just going to talk a little bit about speaking at conferences.
[1228.98 → 1236.56] Um, if you're thinking about going to a conference, what to look for, if you're thinking about applying to speak, what to look for, and maybe even a little bit about what it's like to run a conference.
[1236.56 → 1248.92] So, I would say if someone is looking into wanting to start attending some JavaScript conferences, the best thing that they could do is go to jsconf.com.
[1249.32 → 1252.96] So, it's the scoff family of conferences.
[1253.54 → 1261.68] And, um, I'm pretty sure what that means is first there was jsconf.us, and it was started by Chris Williams.
[1261.68 → 1266.16] And there's this whole, um, family of other conferences.
[1266.50 → 1271.48] And it has a strict code of conduct where, you know, you're, you're nice to everyone.
[1271.66 → 1278.16] There's no, you know, um, racism, misogyny, making assumptions about people, sexism.
[1278.32 → 1279.94] It's just like super welcoming.
[1280.34 → 1281.66] It's really fun.
[1281.86 → 1283.44] It was always at a great location.
[1283.44 → 1291.72] And then as people started attending these conferences, they were like, wow, it would be really awesome if we had this conference where I live.
[1292.14 → 1298.48] And so Chris started allowing other people to have, uh, conferences under the scoff family.
[1298.82 → 1307.66] And the way that you would be able to do that is if you've attended a scoff so that you know how they run, you know how that runs, uh, you're able to branch off.
[1307.66 → 1311.66] And now there's, there's like, I'm trying to count really fast.
[1311.76 → 1314.70] There's, there's two, that's four, eight, 12.
[1314.82 → 1320.54] There's 12 that are scoff underscore, like whatever country they're in.
[1320.66 → 1324.40] There's a scoff US or, well, there's not scoff US anymore.
[1324.76 → 1330.88] Um, for now there's scoff EU, which Michael and I will be going to, I'll be speaking.
[1330.88 → 1333.86] And there's scoff AU in Australia.
[1334.30 → 1335.92] And there's, there's just so many.
[1336.02 → 1342.40] If you listened last week, um, Juan talked about scoff Colombia and they're everywhere.
[1342.86 → 1346.86] And then there's not just the scoff, uh, namesake ones.
[1346.86 → 1348.58] There's, there's also robotsconf.
[1348.70 → 1349.68] There's Asunción.
[1350.12 → 1350.88] There's Cascadia.
[1351.66 → 1351.88] There's Empire.
[1352.64 → 1354.88] There are a lot of other ones that are under that umbrella.
[1354.88 → 1361.98] And it's usually, you know, like two to three days of just really, really well curated talks
[1361.98 → 1366.02] and workshops with a bunch of people that are like-minded.
[1366.46 → 1371.04] And it was the first conference that I ever attended in 2014.
[1371.10 → 1376.56] And I mean, it, it pretty much changed my life due to the people that I met there from
[1376.56 → 1382.56] seeing them speak and the people that inspired me to, you know, go out of my comfort zone and
[1382.56 → 1390.56] try and do more with JavaScript robotics and, um, just, just try and be a better programmer.
[1390.82 → 1394.24] And from there, here we are today.
[1395.28 → 1398.28] So there's, there are a lot of really awesome resources.
[1398.28 → 1402.74] And a lot of these conferences also have, um, you know, diversity sponsorships.
[1402.74 → 1409.54] So if you are from a, um, marginalized group or underrepresented minority, you can often attend
[1409.54 → 1413.32] at a severely, severely discounted rate, often sometimes free.
[1413.88 → 1415.04] That was a great breakdown.
[1415.54 → 1417.84] I don't think that we could have done that nearly as well.
[1418.92 → 1419.32] Yeah.
[1419.36 → 1423.66] Alex and I are, are both people that, you know, Chris helped out, uh, getting our events
[1423.66 → 1425.72] off the ground in that Scoff family.
[1426.02 → 1431.80] Um, for me, Nodemon and JS Fest and, um, for Alex, TXJS.
[1431.80 → 1434.52] But yeah, I mean, that's, that's a great group of conferences.
[1434.84 → 1440.00] Even the conferences that aren't quoted unquote Scoff family are really directly influenced
[1440.00 → 1441.80] by that, that whole thing.
[1442.02 → 1442.42] Yep.
[1442.60 → 1446.00] There are all kinds of new events popping up all over the place, and you can really see the
[1446.00 → 1448.90] the difference in the content and how people are treated.
[1448.90 → 1452.94] And, and I mean, a lot of the code of conduct stuff that is now pretty standard in conferences
[1452.94 → 1456.70] really started with Scoff, uh, US like a while back.
[1458.48 → 1459.94] Alex, do you have anything to add?
[1460.94 → 1461.34] Me?
[1461.80 → 1462.50] This Alex?
[1463.24 → 1463.68] Yeah.
[1463.96 → 1465.06] Uh, yeah, sure.
[1465.30 → 1466.84] Um, uh, I'd love to talk.
[1467.26 → 1473.62] No, uh, Michael and I, uh, we're both on staff for some of the earlier Scoff with Chris.
[1474.30 → 1480.32] Um, and I just wanted to share a story about, I think it was in Arizona, uh, and it was the
[1480.32 → 1485.32] morning of Scoff and, uh, like the first morning and everyone had to come register.
[1485.52 → 1490.20] We were like laying out badges and putting together bags for, for people to do.
[1490.20 → 1495.38] And I remember Chris and Laura scrambling to get everything right and putting everyone
[1495.38 → 1495.98] in their places.
[1495.98 → 1503.24] And then I look over and in the corner, Michael has this coffee grinder, Mason jar contraption
[1503.24 → 1506.42] and he's just grinding his own coffee in the corner.
[1506.72 → 1513.16] Um, and he was just like, I can't, uh, help you guys until I'm done grinding my own coffee
[1513.16 → 1515.72] and then pouring it over, over in this corner.
[1515.72 → 1522.78] Um, that's just maybe one of my favourite, uh, Michael Scoff, uh, stories.
[1523.20 → 1529.94] Um, I actually, uh, maybe have, uh, a, an observation that I don't know if it's true.
[1530.10 → 1535.50] It feels like the actual peak of conferences maybe occurred like two years ago.
[1535.60 → 1537.96] Not now that does that feel right.
[1537.96 → 1540.74] I feel like it was almost zero.
[1540.92 → 1545.64] And then Scoff US, uh, I mean, there was like a Jackson before that and some like jQuery
[1545.64 → 1548.52] camp or, you know, a few things like that.
[1549.22 → 1553.42] So what you're saying is the decline of conferences started when I started speaking.
[1553.78 → 1554.14] No, no, no, no, no, no.
[1557.44 → 1560.70] Uh, I'm not trying to imply that I'm trying to directly state it as fact.
[1560.70 → 1567.70] Um, the, the, no, I feel like there was kind of this explosion of conferences, uh, that
[1567.70 → 1568.72] that was nonlinear.
[1568.96 → 1571.50] So, you know, like 2010 was almost zero.
[1571.78 → 1578.00] Uh, and then by 2014 or so you had a ton of like city based conferences.
[1578.08 → 1583.38] And I feel like a lot of those have fallen off and now there's again, maybe a little more
[1583.38 → 1586.58] specialized like React comps or different things like that.
[1586.58 → 1590.00] I think that it's definitely, definitely getting more specialized.
[1590.28 → 1594.98] Because I mean, there, there used to be, uh, well, I think there was one year there was
[1594.98 → 1600.54] like Cascadia and Texas JS and Scoff US.
[1600.54 → 1604.28] And now we aren't going to have Cascadia.
[1604.48 → 1605.92] We're not going to have TXJS.
[1606.02 → 1607.70] We're not going to have Scoff US.
[1608.12 → 1611.06] There's not going to be a Scoff Iceland.
[1611.38 → 1614.02] There's only going to be, I think, Dinosaur.
[1614.02 → 1619.32] There's the one in Omaha put on by, uh, the Marlins.
[1620.46 → 1625.48] There's, um, you know, there's the Oklahoma ones.
[1625.74 → 1627.44] There's their, their group.
[1628.18 → 1633.14] Since we mentioned Oklahoma, they have a like a family of, uh, different events.
[1633.14 → 1638.84] Like they, they have like constant learning and meetups as well as, but the Oklahoma is
[1638.84 → 1640.62] their, their conference isn't called Oklahoma.
[1640.82 → 1642.94] I misspoke, but you can look them up.
[1642.94 → 1644.32] Sorry, I interrupted your entire thing.
[1644.76 → 1645.30] Oh, it's okay.
[1645.30 → 1655.38] I think that it's getting, um, a lot more spread out and there's not really any, I mean, it's
[1655.38 → 1659.02] hard to put on conferences of that scale.
[1659.02 → 1665.78] I think that the closest that I've been to where I felt that really like, I mean, every
[1665.78 → 1670.12] conference that I go to is pretty much, they're all really great, but there's just something
[1670.12 → 1678.30] special that hasn't been matched for me aside from like Nordic JS and Nordic JS like goes
[1678.30 → 1684.78] all out, and it's a different environment, obviously, because it's not here in the United
[1684.78 → 1685.38] States.
[1685.38 → 1687.74] But I mean, it's great.
[1687.74 → 1693.54] I think that there's also like a lot more speakers now, like people realized, Hey, people
[1693.54 → 1694.94] are, people are doing that.
[1695.06 → 1695.80] I want to do it too.
[1695.88 → 1697.82] Because I mean, that's what I did.
[1698.20 → 1703.16] Um, I wouldn't, I guess this is a good segue into how you can speak at conferences.
[1703.16 → 1708.32] Um, Jean Schopfer was like, Hey, Rachel, if you want to speak at conferences, you should
[1708.32 → 1709.16] just submit a talk.
[1709.20 → 1710.94] And I did, and it got accepted.
[1711.24 → 1712.86] And so I had to build a robot.
[1713.54 → 1717.28] And then I spoke at Scoff last call, and it was awesome.
[1717.28 → 1718.62] And I was like, this is fun.
[1718.74 → 1726.40] And I think that the best thing about speaking is being able to like to get people excited about
[1726.40 → 1732.52] something that they may not have been exposed to previously and, you know, inspiring people
[1732.52 → 1738.30] to, to try something new or that they are capable of doing whatever it is that you are
[1738.30 → 1739.02] talking about.
[1739.02 → 1744.22] Um, and I think that there's this weird stigma that people that speak at conferences are a
[1744.22 → 1747.30] little bit like, what's the right word that I'm thinking of?
[1747.30 → 1753.96] Like, like we're special or, or it's not like something that is hard to achieve, but I don't
[1753.96 → 1758.22] really think it is as long as you apply yourself, and you're, you're passionate about what you're
[1758.22 → 1759.86] speaking about, you know?
[1760.50 → 1761.20] Yeah, I agree.
[1761.46 → 1768.22] Um, I, I also got into speaking via just the open section of conferences where you not even
[1768.22 → 1769.22] like submit a talk.
[1769.22 → 1774.06] Like it's the, uh, it wasn't a five minute, it wasn't a lightning talk, but I think it was,
[1774.06 → 1777.90] you know, like a 15-minute style, just people sign up throughout the whole day.
[1778.22 → 1779.28] It's a third track.
[1779.74 → 1783.94] And I think that's a if you want to get your feet wet, that's a perfect time to go.
[1783.96 → 1789.88] Um, and try it and then maybe speak at a local meetup, uh, and then submit a talk.
[1789.92 → 1792.48] If you, if you want to just go slowly, absolutely.
[1792.66 → 1797.44] If you're interested in, you think you can do it, then, uh, then just submit.
[1797.56 → 1803.00] So I have a, I have a game I'd like to play, speak, attend stream.
[1803.62 → 1809.18] Uh, so we'll say three conferences, uh, which one would you speak at?
[1809.26 → 1810.36] Which one would you attend?
[1810.42 → 1811.48] And which one would you stream?
[1812.26 → 1812.78] Oh yeah.
[1812.78 → 1813.48] Let's play.
[1814.34 → 1815.02] Michael, you're up.
[1815.50 → 1815.86] Okay.
[1815.92 → 1817.58] Well, you got to throw the conferences at me, right?
[1817.58 → 1818.86] Oh, I have to give you the three conferences.
[1819.36 → 1819.70] Okay.
[1820.00 → 1820.30] Yeah.
[1821.42 → 1831.20] A Jackson in 2009, the second pirate themes Scoff and TXJS, uh, 2015.
[1831.20 → 1833.72] I'll let you see here.
[1833.80 → 1833.92] Okay.
[1834.12 → 1844.02] So, uh, attend would be TXJS because I'd like to just relax and enjoy Austin and not have
[1844.02 → 1844.62] to give a talk.
[1844.98 → 1851.46] Uh, speaking would definitely be the, um, the early JS comps because there was just a lot
[1851.46 → 1855.36] of perks of being a speaker back then, even more than today, probably.
[1855.36 → 1859.76] Um, and stream a Jackson cause who gives a what?
[1860.18 → 1863.08] That was the only conference that was, that was the jam.
[1863.54 → 1865.70] Uh, that was huge though.
[1865.74 → 1869.80] I mean like, like the, like the difference between like in a, in a thousand-person conference,
[1869.80 → 1872.50] seeing a talk live and seeing it streamed is just not that big.
[1872.50 → 1873.18] Yeah.
[1873.18 → 1879.52] That was like the first time you had John Resign, Douglas Crockford, Brendan Eich, and like
[1879.52 → 1881.06] one of the Mutuals people.
[1881.32 → 1885.96] Oh, and Andrew DuPont all on the same stage, just arguing about frameworks or whatever.
[1886.12 → 1887.94] It was, uh, terrible.
[1888.22 → 1888.66] Exactly.
[1889.94 → 1894.88] It was the first time something that terrible ever existed, which is kind of like, you
[1894.88 → 1901.54] know, car, car wreck situation is, uh, I, I, I thought it was, uh, pretty magical at
[1901.54 → 1903.94] the time, even though I wouldn't attend it currently.
[1904.22 → 1906.74] 2009 was a different lay of the land.
[1907.68 → 1915.74] Um, I, I guess somebody asked about like non JS conferences and I really actually haven't
[1915.74 → 1918.02] attended many non JS conferences.
[1918.48 → 1921.32] Um, so I'm going to defer to, to you two.
[1921.40 → 1925.42] I've heard good things about like OSCAN and some other things like that, but.
[1925.82 → 1926.70] It's a pretty different beast.
[1926.70 → 1933.00] I think, uh, there are lots of like full stack conferences and then the core language conferences
[1933.00 → 1936.08] of almost every language are usually pretty great.
[1936.08 → 1942.48] Like Ruby has some, like, I think a lot of the conferences in JavaScript that are great
[1942.48 → 1947.18] actually kind of stem from the style of conferences that the Ruby community, I think Chris has
[1947.18 → 1950.80] admitted as much that, uh, uh, I don't know which Ruby.
[1950.80 → 1951.34] Yeah.
[1951.34 → 1954.64] Ruby friend is kind of where he was like, Hey, this is a cool model.
[1955.24 → 1957.74] Um, and so I think a lot of the Ruby conferences are very good.
[1957.96 → 1964.20] Um, as well as like, uh, some of the full stack conferences and, um, like go has a good
[1964.20 → 1967.14] conference, go for con and, and, and all those things.
[1967.14 → 1972.08] I think there are lots of good community and kind of the more open source languages, uh,
[1972.08 → 1976.26] often have like similarly valued conferences.
[1976.26 → 1976.74] Yeah.
[1976.90 → 1984.48] I've heard excellent things about, um, strange loop, which is in St. Louis and full stack
[1984.48 → 1987.24] fast in Barcelona and rev cone in Virginia.
[1987.56 → 1993.76] And, um, a bunch of those other ones that don't really focus on any specific language.
[1993.76 → 1998.92] I think that you can get a lot more interesting, um, hybrids of talks when you have that kind
[1998.92 → 2002.08] of balance, even though I don't know, because I've never gotten to any.
[2002.08 → 2006.36] So I would say that there's really kind of two classes of conferences that you really
[2006.36 → 2007.78] have to look at and treat differently.
[2008.34 → 2012.98] One is the community conferences that we've been talking about, which the whole JS comp
[2012.98 → 2016.92] family is really like developers in the developer community decide that they want to do a community
[2016.92 → 2017.78] event for their community.
[2018.30 → 2024.90] And then there are really huge events that are usually run by media companies or by Google
[2024.90 → 2026.78] or Google or somebody like that.
[2026.84 → 2027.04] Right.
[2027.14 → 2030.90] Like then they're, they're completely, they're very, very different.
[2030.90 → 2035.64] And if you're thinking about speaking, I would say that, you know, like speaking in an O'Reilly
[2035.64 → 2040.64] event is more likely to maybe get you a job or to talk to people that will hire you potentially,
[2040.86 → 2044.22] um, then say like a two or 300 person community event.
[2044.64 → 2049.46] Um, but if you're looking to sort of like make friends and become more engaged in the community
[2049.46 → 2055.42] and, um, and really kind of like have, have a community impact, um, attending or speaking
[2055.42 → 2058.14] at the smaller community events is just a world different.
[2058.14 → 2064.22] But also in terms of quality of content, the quality is much higher in the community events
[2064.22 → 2068.42] because they don't have a bunch of sponsor talks that they had to sell in order to make
[2068.42 → 2069.40] the funding model work.
[2069.50 → 2074.74] They don't have, um, I mean, like, like, look, I mean, we've, Alex and I have been running
[2074.74 → 2075.78] conferences for a long time.
[2075.78 → 2081.24] And for, for a while, if you were running a JavaScript or a node event, you were the only
[2081.24 → 2081.78] game in town.
[2081.84 → 2083.04] There weren't any media companies.
[2083.04 → 2086.78] And so these huge companies would come up, and they would give us a bunch of money and
[2086.78 → 2088.96] they didn't really ask for all the stuff they ask for now.
[2089.38 → 2093.30] Now they don't sponsor a lot of the smaller events because there are these bigger events
[2093.30 → 2094.84] that are willing to give them like a booth.
[2095.00 → 2096.08] Like we don't have booths.
[2096.14 → 2096.28] Yeah.
[2097.76 → 2102.48] The bigger events are like, hold on, get ready.
[2102.54 → 2103.92] Who was ever editing this?
[2103.98 → 2105.72] I don't know if this is a word I'm allowed to say.
[2106.06 → 2107.84] They're like such a circle jerk.
[2107.84 → 2112.62] Like it's the same people doing the same stuff at every O'Reilly thing.
[2112.78 → 2118.06] And like, what, I don't need, are the O'Reilly, sorry, O'Reilly, um, just saying like, if they're
[2118.06 → 2121.76] recorded, how are they going to charge like a grand for a ticket?
[2121.76 → 2124.86] And like, who is even going to those?
[2124.86 → 2127.58] Like, is it just like other big companies?
[2128.18 → 2128.72] Um, yeah.
[2128.84 → 2131.14] So, you know, so I have some answers to that.
[2131.22 → 2137.74] Um, but having participated in some of that, so when a ticket costs a grand,
[2137.84 → 2140.16] people are not paying for the tickets.
[2140.56 → 2147.72] Um, and so I think that is a fundamental reason why the audiences are very different
[2147.72 → 2152.06] at the two different conferences is that it's people who often put up their own money to
[2152.06 → 2157.84] attend a community conference and then versus people whose company have sent them to a conference
[2157.84 → 2158.68] to learn things.
[2159.14 → 2162.44] So if you're going to send someone to a conference, you want to send them to the most reputable
[2162.44 → 2163.56] one that you can find.
[2163.56 → 2167.40] And O'Reilly is a very reputable name in tech education.
[2167.40 → 2170.52] And so you're going to send this and there are very big names on that ticket.
[2170.58 → 2174.08] And of course, like those people give the same talk every time because like you can't
[2174.88 → 2177.96] give 300 different talks in a year if that's your whole job or whatever.
[2178.52 → 2183.42] Um, and so I think you end up with an audience that cares a little less because they're not
[2183.42 → 2187.32] invested, which isn't to say that there aren't tons and tons of people who care a bunch
[2187.32 → 2188.50] in those places.
[2188.50 → 2192.22] But I think the environment becomes different because it isn't a bunch of people who are
[2192.22 → 2195.04] like, uh, necessarily all are on the same page.
[2195.14 → 2201.08] It's, uh, people who, and I, I want to be very clear that it's fine if you're a developer
[2201.08 → 2206.46] who goes to work programs, isn't interested in spending all your own money and going to
[2206.46 → 2209.16] a conference and then like go do the things that you love more.
[2209.26 → 2213.66] I think it's perfectly acceptable and good, uh, to have the wide gamut.
[2213.66 → 2217.72] But I think one of the reasons the community conferences are different, uh, is because
[2217.72 → 2222.34] the, the motivation for going is not my work is sending me here.
[2222.34 → 2224.94] It's, I want to learn all these things, uh, myself.
[2225.12 → 2227.80] Um, and I think I want to meet these people, right?
[2227.88 → 2228.12] Right.
[2228.20 → 2228.36] Yeah.
[2228.90 → 2235.80] And I guess you're going to get exposed to more passionate like talks versus pitchy talks.
[2235.88 → 2237.78] So that makes sense.
[2237.96 → 2238.10] Yeah.
[2238.10 → 2238.72] I'm a jerk.
[2238.72 → 2244.24] I'll also say that like, um, you, you would think that a thousand dollars for a ticket
[2244.24 → 2247.70] and in some cases the O'Reilly events have like a hundred thousand dollars for the platinum
[2247.70 → 2248.50] membership as well.
[2248.64 → 2252.92] You would think that they were just raking in money and, and that's why a lot of the
[2252.92 → 2254.00] quality was really low.
[2254.24 → 2259.24] But, um, on the organizing side, every time you go into a new 500-person bracket, when
[2259.24 → 2264.20] you go from 500 to a thousand people or a thousand people to 1500, you move away from
[2264.20 → 2268.52] a lot of different venues and catering options and all the things that you can do.
[2268.52 → 2271.80] You end up costing more money per attendee for lower quality.
[2272.22 → 2276.22] Whereas once you get to the size that say like a Google next is where there's like 10,000
[2276.22 → 2281.42] people there, those sandwiches cost like $40, and it's, and they're terrible and there's
[2281.42 → 2282.44] just no way out of it.
[2282.52 → 2285.98] You're locked into it because there's, there's only three places on the West coast that can
[2285.98 → 2287.98] hold you, and they know that they have you over a barrel.
[2288.68 → 2293.04] So this is, so a lot of what we're talking about for like the quality being higher for,
[2293.18 → 2296.76] for the smaller side is a lot of like the, the funding side of it too, where you,
[2296.76 → 2298.42] you can make a lot better choices.
[2298.42 → 2304.30] Like if you do a two or 300 person event in Portland, you can get the greatest food in
[2304.30 → 2306.46] the whole world brought to the event.
[2306.72 → 2307.74] It's so good.
[2308.28 → 2312.60] Um, but if you do a thousand-person event in Portland, you, your, your options are actually
[2312.60 → 2313.70] pretty slim and terrible.
[2314.54 → 2319.36] Dinosaur JS did something pretty awesome last year for food where they just rented a bunch
[2319.36 → 2324.16] of food trucks and had everybody walk to a big park, and it was, it was nice, but that's
[2324.16 → 2325.44] a smaller community conference.
[2325.44 → 2327.66] So that's, that's where you get that.
[2328.28 → 2334.96] So if I had one piece of advice for conference organizers around food is being very careful of
[2334.96 → 2335.54] food trucks.
[2335.86 → 2341.06] Uh, pretty much every food truck situation, including Michael's first foray into food trucks
[2341.06 → 2346.14] ends up with, uh, a line that is not gone by the time lunch is over.
[2346.14 → 2351.56] Um, so you really have to plan either a food truck that can pre-make everything and just
[2351.56 → 2356.76] hand things out to people or get so many food trucks that they can handle like the concurrency
[2356.76 → 2358.08] of, of enough people.
[2358.64 → 2363.62] Um, uh, pretty much every food truck, like by far the majority of food truck situations
[2363.62 → 2366.90] end up poorly, uh, which is why I've avoided them at TXJS.
[2367.00 → 2372.02] Even though food trucks are delicious, and it's a perfect idea, it's, it's very hard to,
[2372.10 → 2372.66] to manage.
[2372.66 → 2377.44] And so if you're running a conference, be very, be very aware of, of that problem.
[2377.80 → 2379.46] So, so here, here's, here's the tip.
[2379.52 → 2382.34] You, you have to find a food truck that also does catering.
[2382.34 → 2385.86] So if they say specifically that they also do catering, they don't just come and park
[2385.86 → 2386.10] there.
[2386.20 → 2390.18] Then they, in their prep kitchen, they know how to make a ton of something and then show
[2390.18 → 2392.02] up with all of it and everybody can eat right away.
[2392.52 → 2397.36] Um, the, the, the, the, Alex is, is talking about was a node cone in 2012.
[2397.36 → 2401.32] And we actually did two different food trucks, one of which was very good at that.
[2401.32 → 2403.52] And everybody ate and got out of there in time.
[2403.52 → 2405.80] And the other one didn't process the line for an hour and a half.
[2405.84 → 2407.18] And we had to push everything back.
[2407.76 → 2413.72] Um, I'd like to circle back really quick to people that are interested in wanting to speak
[2413.72 → 2414.40] at conferences.
[2414.40 → 2422.76] Um, so I know that in New York, there's this really great thing that Tracy Hines and Justin
[2422.76 → 2429.30] put out called a right to speak where people get together, and they have like abstract ideas
[2429.30 → 2434.92] or just maybe even like a few talk topics that they're interested in, you know, workshopping
[2434.92 → 2437.16] and trying to help people flesh them out.
[2437.16 → 2444.16] And if you're, I would suggest if you are interested in speaking, don't do it unless
[2444.16 → 2447.36] you're super passionate, not don't do it.
[2447.36 → 2447.94] Like don't do it.
[2448.94 → 2456.56] Don't, don't do it unless you're actually like really legitimately passionate about what
[2456.56 → 2457.86] it is that you're talking about.
[2457.86 → 2463.30] Cause there's nothing worse than somebody that's there, obviously just because they wanted to
[2463.30 → 2468.06] go to a conference, and they thought that they could speak because everybody else was doing
[2468.06 → 2472.84] it, and they get up there, and it's just like the driest painful thing to watch.
[2473.28 → 2479.30] Um, aside from that, I would also suggest saying, read a lot of abstracts, go on, you know,
[2479.36 → 2484.60] past few years of conference sites, see what the talks look like that people have written,
[2484.80 → 2489.82] um, see the tone that they use, tell like the story that you were trying to tell.
[2489.90 → 2492.78] Don't just tell me what it is you're going to teach me.
[2492.78 → 2495.28] I want to know why you want to teach somebody that.
[2495.28 → 2504.28] And I've read a lot of, uh, I, I did some, um, proposal reviews for, um, empire and you
[2504.28 → 2506.02] would be so surprised.
[2506.18 → 2510.16] Well, you two wouldn't be so surprised, but everybody out there that thinks that everybody
[2510.16 → 2515.78] out there that thinks that, oh, they can't write an abstract you get, I would say, let's
[2515.78 → 2522.76] say you get a conference that has 300, uh, applications and there's maybe only 30.
[2522.76 → 2525.52] 30, uh, 30 speaking slots.
[2525.76 → 2531.88] I guarantee you like two thirds of all of those submissions are going to be terrible anyway.
[2531.88 → 2536.26] Because it's people that are just like putting in a sentence where it's like, I want to talk
[2536.26 → 2542.36] about react components, or I think it would be really neat to talk about, you know, currying
[2542.36 → 2547.68] or something like the, the people that actually put in effort are the ones that have a way better
[2547.68 → 2551.00] chance than the people that are just throwing their hat in the ring for the sake of it.
[2551.32 → 2551.64] Yeah.
[2551.94 → 2552.22] Yeah.
[2552.34 → 2557.02] But before I kind of stopped doing, uh, organizing conferences, because I was kind of burning out
[2557.02 → 2557.28] on it.
[2557.38 → 2561.50] The main advice that I put in the CFP every time was tell me a story.
[2561.58 → 2563.62] Like it should have a beginning and a middle and end.
[2563.70 → 2565.46] I don't need to know about the technology.
[2565.56 → 2566.66] I can read the docs for that.
[2566.68 → 2569.72] And a lot of these abstracts just look like an outline of the documentation.
[2569.72 → 2574.14] What I want to know is like, why did you create it, or why did you decide to use it?
[2574.22 → 2578.58] Like, what is that, that narrative that makes this a compelling thing to learn and to get
[2578.58 → 2578.86] into?
[2579.00 → 2582.18] Because if it's, if you're just telling me what the documentation says, like I could
[2582.18 → 2583.18] do that when I leave.
[2583.38 → 2588.26] The job of a speaker is not to teach everybody in 20 minutes how to use something.
[2588.26 → 2592.50] It's actually to teach them why it's compelling enough that they would go home and continue
[2592.50 → 2593.00] to learn it.
[2593.58 → 2593.68] Yeah.
[2593.76 → 2597.72] I think that's exactly what I was going to say is, is that as a speaker and as someone who
[2597.72 → 2603.98] choose the speakers, I absolutely would be fine if everyone walked away having learned
[2603.98 → 2608.38] nothing except for being inspired to go learn more.
[2608.62 → 2613.32] Like I saw the value proposition in X, and now I want to go read the docs.
[2613.60 → 2619.50] Like I gained enough motivation from that talk in order to go put in the work to actually
[2619.50 → 2624.90] learn it because anyone reading documentation to you for 20 minutes is not going to be compelling.
[2624.90 → 2628.18] Um, and this is a waste of your money for the most part.
[2628.56 → 2634.78] So I totally agree that definitely inspire people, like give them the and I don't mean
[2634.78 → 2639.24] like, uh, slimy Wiley, uh, everybody is great.
[2639.42 → 2642.30] Uh, everyone is a special unicorn type inspiration.
[2642.52 → 2643.84] Those talks can be very good too.
[2643.94 → 2649.66] I'm not against those talks, but I mean like really, uh, talk about why you're excited about
[2649.66 → 2655.40] something and how it changed things for you or something like that or, or why it's important
[2655.40 → 2657.74] for like the web or something.
[2657.82 → 2661.32] And I think those types of talks really go over much better.
[2662.06 → 2665.46] I want to hear about the journey, not, not the steps.
[2665.92 → 2666.36] Yeah.
[2666.98 → 2668.54] That's a that's a good way to put it.
[2668.64 → 2668.82] Yeah.
[2669.36 → 2669.58] Cool.
[2670.08 → 2674.82] On that note, I think we can take a break now and when we come back, we'll get into the
[2674.82 → 2675.58] project of the week.
[2676.86 → 2682.08] If you're looking for trusted freelance talent, ready to join your team right now.
[2682.08 → 2687.54] I mean, like within the week, call up all my friends at top tile, T O P T A L.com.
[2687.68 → 2693.24] And as a listener of the show, you might actually be one of those developers or designers looking
[2693.24 → 2698.58] for awesome freelance, independent contractor type opportunities where you can still be a
[2698.58 → 2699.10] remote worker.
[2699.20 → 2702.44] You can still have the freedom you have right now, which means you can travel anywhere.
[2702.44 → 2704.80] You can be anywhere and do what you do.
[2705.20 → 2706.06] We love top.
[2706.10 → 2708.14] They've been supporting this show for a very long time.
[2708.42 → 2709.84] They're perfect friends of ours.
[2710.04 → 2712.80] If you want a personal introduction, I'd be glad to give that to you.
[2713.08 → 2715.74] Email me, Adam at change law.com.
[2715.94 → 2717.80] Otherwise head to top.com.
[2717.86 → 2720.64] That's T O P T A L.com to learn more.
[2720.92 → 2722.64] Tell them Adam from change law sent you.
[2722.90 → 2724.16] And now back to the show.
[2726.32 → 2726.98] All right.
[2727.12 → 2731.34] Today's project of the week or this week's project of the week, I should say, uh, is P five
[2731.34 → 2731.88] JS.
[2731.88 → 2734.26] Uh, so why don't you tell us about this, Rachel?
[2735.10 → 2735.50] Sure.
[2735.72 → 2739.72] Um, so P five JS is a JavaScript.
[2739.72 → 2744.06] I'm going to say homage because it's not a direct port of processing.
[2744.52 → 2748.88] Um, what it does, I guess I have to start by telling you what processing is.
[2749.08 → 2757.18] Um, so processing is this open source thing and IDE that's ancient.
[2757.18 → 2760.38] It's about 14, 15 years old, I think.
[2760.38 → 2766.68] Um, and it was made explicitly for people that were, um, you know, big beginners in programming
[2766.68 → 2774.04] and visual artists to use something to make some really cool, uh, visualization stuff and
[2774.04 → 2774.98] graphics and art.
[2774.98 → 2777.32] Um, it, it, it's built on top of Java.
[2777.32 → 2779.20] It uses a simplified syntax.
[2779.20 → 2786.08] And, um, basically what it does is it lets you export your projects as desktop apps for,
[2786.44 → 2788.52] um, either windows, Mac or Linux.
[2788.52 → 2793.42] So you can't really show it on the web though.
[2793.42 → 2794.98] So it's like a standalone thing.
[2794.98 → 2797.74] Um, the power behind it is really great.
[2797.90 → 2799.26] Uh, it has great FPS.
[2799.70 → 2803.90] Uh, you can build some really robust things, but you can't do things on the web.
[2803.90 → 2812.84] So somebody built another port of it, um, which was actually John Resign and some other students
[2812.84 → 2814.62] to make processing JS.
[2814.92 → 2820.22] And so processing JS is a more true port of processing to JavaScript.
[2820.94 → 2823.70] Um, you don't have to totally rewrite your code.
[2823.78 → 2829.70] You use processing JS to take your processing files and be able to run it in HTML five.
[2829.70 → 2833.52] It uses regular expressions to convert the Java into JavaScript.
[2833.90 → 2839.46] And it lets you have some pretty like, uh, mangled JavaScript.
[2839.46 → 2844.20] That's not readable afterwards, but you, you get the same effect and it, it runs on canvas.
[2844.58 → 2855.08] So in comes P five, um, P five is a really awesome, accessible, uh, library made by Lauren McCarthy,
[2855.08 → 2862.88] who, um, was at NYU ITP and the processing foundation, which deals with, um, like processing JS and
[2862.88 → 2865.68] a lot of other ports of processing to other languages.
[2866.22 → 2873.34] And, um, um, what they wanted to do is they wanted to make it so that people could do the
[2873.34 → 2878.98] same kind of things that you would do with processing, but, um, a little bit looser written.
[2878.98 → 2886.44] So it's not going to be exactly the same with all the, um, super involved animations that
[2886.44 → 2888.94] you can do with your, your regular processing.
[2889.26 → 2895.54] But with P five, it lets you write more natural JavaScript to do some really cool stuff in the
[2895.54 → 2901.94] browser involving a lot of shapes and interactions and, um, you know, artsy stuff.
[2902.00 → 2903.58] It's all canvas based.
[2904.00 → 2907.22] There are a bunch of other plugins that you can get for it.
[2907.22 → 2912.16] So there's the P five library, which is just, you know, the regular access to the shapes
[2912.16 → 2918.16] and stuff, but there's also P five Dom, which lets you interact with HTML five objects, um,
[2918.16 → 2919.16] outside the canvas.
[2919.16 → 2922.60] You can do like video, audio, webcam input text.
[2922.60 → 2924.90] I was messing around with the video one.
[2925.00 → 2926.16] It's, it's really cool.
[2926.28 → 2933.18] It essentially grabs each pixel in the video and maps it to a drawn instance of whatever shape
[2933.18 → 2935.30] that you'd use and hides the video.
[2935.30 → 2941.58] So it makes, um, basically an animation of whatever video you give it to, but with shapes
[2941.58 → 2943.54] instead, uh, for each pixel.
[2944.02 → 2949.58] Um, there's also P five sound, which uses web audio stuff, and you can do playback and affect
[2949.58 → 2952.94] a lot of the stuff in the canvas that you would build art with there.
[2953.44 → 2958.82] Um, there's P five serial, which lets you do serial communications with stuff and lets you
[2958.82 → 2960.66] interact with it with P five.
[2960.80 → 2965.28] There's so many, there's also like bots, which was, um, made by Sarah Rough Polaris.
[2965.30 → 2967.32] Who's a New York based dev.
[2967.38 → 2968.14] Who's a Kickstarter.
[2968.26 → 2968.80] There's speech.
[2968.90 → 2969.66] There's geolocation.
[2969.86 → 2972.12] There's just like so much stuff that you can do.
[2972.30 → 2979.58] And the, the best thing for me, um, is you don't necessarily even need to understand JavaScript
[2979.58 → 2980.92] to jump in and use it.
[2980.98 → 2985.30] I've seen a lot of people that are just, you know, starting out as game devs who are used
[2985.30 → 2987.26] to unity and some C sharp stuff.
[2987.26 → 2990.24] And they heard that you could do some fun stuff with P five.
[2990.24 → 2993.54] So the reference material on the site is awesome.
[2993.90 → 2995.30] The examples are awesome.
[2996.26 → 3000.50] It's just really neat, especially for people that are interested in doing some more creative
[3000.50 → 3005.80] coding and finding out what they can do with, uh, with canvas.
[3005.80 → 3012.56] And there's another, um, person who teaches that ITP named Daniel Schiff man, who has a
[3012.56 → 3015.64] really, really amazing YouTube channel called the coding train.
[3015.64 → 3023.14] Um, and they make video tutorials every week that goes from the beginning of, you know, basic
[3023.14 → 3029.46] P five stuff to super advanced things like Perlin noise, which is, uh, this algorithm that
[3029.46 → 3034.08] allows you to create true, like randomized noise for cool glitchy.
[3034.08 → 3037.50] Well, it's actually used mostly for like terrain generation.
[3038.20 → 3044.34] Um, but it's, they're perfect videos, and it explains it in a in an accessible way.
[3044.74 → 3050.82] And if anybody is interested in trying out that kind of stuff, I highly recommend checking
[3050.82 → 3052.00] out those resources.
[3053.10 → 3054.24] ITP is so cool.
[3054.52 → 3056.90] Everything ITP ever does is just rad.
[3058.30 → 3058.82] Yeah.
[3059.10 → 3063.72] Like, uh, Clay Shirk is like still a teacher there and they just, yeah, I've known a few people
[3063.72 → 3065.26] that have gone through there and done their program.
[3065.26 → 3071.84] And it's just this amazing mashup of like code and art and kind of thinking about social
[3071.84 → 3072.16] good.
[3072.34 → 3073.08] It's pretty rad.
[3073.74 → 3073.90] Yeah.
[3073.96 → 3075.26] It's also very expensive.
[3075.26 → 3079.30] So if you don't want to go to ITP, but you want to mess with the tools that people there
[3079.30 → 3081.34] use, P five is a good start.
[3081.50 → 3082.82] Three JS is a good start.
[3083.04 → 3084.94] Um, those are all good places.
[3085.62 → 3086.02] Awesome.
[3086.08 → 3087.26] I'm going to play with this later today.
[3087.26 → 3090.74] I have actually been meaning to poke around with some art stuff.
[3091.00 → 3094.94] So the music notes on the back of the webpage are pretty fun to, yeah.
[3095.28 → 3095.60] Yeah.
[3095.86 → 3099.86] Like people that are super, this is like a challenge that I'm going to give.
[3099.86 → 3108.80] Um, if you, you know, have never really tried to do anything artsy or, you know, you're just,
[3109.08 → 3113.80] you're just a JavaScript dev, and you build, you know, web stuff all the time.
[3113.80 → 3119.76] Um, I would love if you tried to make something neat with P five.
[3120.18 → 3125.24] Um, because if you know, JavaScript, like in and out with your heart, then you should
[3125.24 → 3130.92] be able to do some like really, really awesome stuff with, um, a lot of P five stuff is just
[3130.92 → 3135.52] like iterating through objects to do the place shapes randomly.
[3135.88 → 3138.80] Uh, please make something with it and tweet it at me.
[3138.80 → 3143.74] Because I just want to see what other cool things that people can use to do this.
[3144.22 → 3148.20] Um, I also think it's a good, it's a perfect accessible library for people that are
[3148.20 → 3153.44] trying to try something new and want to try and make something every day because you could
[3153.44 → 3157.10] make something with this in like 15, 20 minutes, just like a little code sketch.
[3157.10 → 3162.78] And, um, I don't know, it's going to help you get used to, you know, regular JavaScript,
[3162.92 → 3166.06] but also a new library that makes pretty art.
[3167.24 → 3167.64] Sweet.
[3168.08 → 3168.78] All right.
[3168.96 → 3169.84] Are we ready for picks?
[3170.18 → 3171.24] We'll have their picks ready.
[3172.22 → 3172.66] Totally.
[3172.66 → 3174.02] I hope you all do.
[3174.16 → 3174.44] Okay.
[3174.62 → 3175.94] I'll, I'll go, I'll go first.
[3176.22 → 3179.18] Um, mine is, is, it's kind of a shameless plug, actually.
[3179.86 → 3186.04] Um, I decided, I stopped organizing events a little while ago because it was too much work.
[3186.46 → 3191.66] Um, but I did now kind of take on this new event that we're trying out called slide list.
[3191.66 → 3193.20] So it's at slide list.org.
[3193.20 → 3197.58] But the idea is that, um, no slides, it's a 15-minute talk.
[3197.58 → 3200.16] That's really telling a story within a theme.
[3200.36 → 3203.32] So the theme for this first one is, is what is your superpower?
[3203.94 → 3207.98] Um, so we'll have some great talks about that, you know, without any slides that people can
[3207.98 → 3210.18] just get up and do their, their narrative.
[3210.26 → 3213.94] So, you know, if you're interested in attending, it'll be in San Francisco in July.
[3214.18 → 3215.08] Tickets are up now.
[3215.08 → 3217.90] Um, and I'm still looking for a few talks as well.
[3218.00 → 3221.32] So if you want to, if you have an idea for a talk in that theme, get hold of me.
[3222.36 → 3227.76] My superpower is, uh, calling Michael Rogers bullshit.
[3231.36 → 3232.76] That's a really limited power.
[3232.86 → 3234.50] Like that requires me being around.
[3234.70 → 3236.42] Yeah, no, it is unfortunate.
[3237.42 → 3238.82] Uh, very portable.
[3238.82 → 3241.86] My pick is a person.
[3242.06 → 3242.66] It's Mike West.
[3243.22 → 3251.40] Uh, Mike West is not that visible outside the web app security, uh, world, but has
[3251.40 → 3253.96] like a massive impact on the security of the web.
[3254.08 → 3256.28] He kind of, uh, I don't know if he's an official leader.
[3256.38 → 3262.38] I assume he is of the web application security working group, uh, which is a W3C group.
[3262.38 → 3269.34] He kind of drafted, uh, like a ton of the security stuff that currently is being added to the
[3269.34 → 3274.28] browsers, um, in the last, you know, like five years, uh, including like CSP and a lot
[3274.28 → 3278.70] of like the cookie updates and, and header changes and things like that.
[3278.70 → 3285.16] Uh, sub resource integrity, um, all these different, uh, cool security upgrades.
[3285.16 → 3291.48] And so I would encourage you to both follow Mike West on Twitter, uh, and follow
[3291.48 → 3295.60] the web app sec, uh, mailing lists because they're not actually that crazy.
[3295.90 → 3300.34] Um, I think they're, they're somewhat followable and, and that's pretty fun and cool.
[3301.20 → 3301.36] Cool.
[3301.70 → 3306.22] Um, my pick this week is a person and a book.
[3306.32 → 3312.46] Um, Sarah Drainer released this book on O'Reilly since I said so many nice things about O'Reilly
[3312.46 → 3313.38] conferences earlier.
[3313.38 → 3315.36] I'm going to say nice things about this book.
[3315.42 → 3315.82] Actually.
[3316.34 → 3321.44] Um, I also apologize if I said her last name incorrectly, but, um, she released this
[3321.44 → 3327.52] really cool book on SVG animations, which like, I know that we like briefly touched on SVG
[3327.52 → 3331.14] stuff on, on one of the other picks, uh, which was like data sketches.
[3331.14 → 3336.40] But if you were like wondering, how do I make SVG animations gorgeous?
[3336.40 → 3339.86] Like I want, um, better UX implementations.
[3340.16 → 3345.36] Uh, her book was released within the past week and I think she said it's the number one
[3345.36 → 3349.34] new release for programming books on Amazon, and it looks great.
[3349.34 → 3353.88] So if that's something that you have more questions about, check it out.
[3354.62 → 3355.06] Awesome.
[3355.74 → 3357.36] Now I'm going to go eat a horse.
[3360.24 → 3363.08] And with that, uh, we're all done for the, for the week.
[3363.22 → 3368.34] Thank you all for tuning in, uh, rate us on iTunes, uh, check us out live every week
[3368.34 → 3369.08] on Fridays.
[3369.36 → 3373.28] Uh, you can go to the changelog.com and, uh, goodbye everybody.
[3373.40 → 3374.10] Thank you very much.
[3374.10 → 3375.64] All right.
[3375.68 → 3378.36] That wraps up this episode of JS party.
[3378.54 → 3381.68] Join the community and slack with us in real time during the show.
[3381.74 → 3384.40] Head to changelog.com slash community.
[3384.78 → 3385.70] Follow us on Twitter.
[3385.76 → 3387.86] We're at JS party FM special.
[3388.00 → 3391.28] Thanks to our sponsors century and top towel.
[3391.44 → 3395.72] Also thanks to fast, our bandwidth partner at the fastly.com to learn more.
[3395.88 → 3400.36] This episode was edited by Jonathan Young blood and the theme music was produced by break
[3400.36 → 3401.18] master cylinder.
[3401.18 → 3402.58] We'll see you again next week.
[3402.82 → 3403.56] Thanks for listening.
