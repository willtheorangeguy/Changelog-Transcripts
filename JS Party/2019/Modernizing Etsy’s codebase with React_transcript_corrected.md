[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.14] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to Linode.com slash Changelog.
[15.30 → 18.12] This episode is brought to you by Rollbar.
[18.42 → 24.34] Rollbar is real-time error monitoring, alerting, and analytics that helps you resolve production errors in minutes.
[24.68 → 28.60] And I talk with Paul Bigger, the founder of CircleCI, a trusted customer of Rollbar.
[28.60 → 32.96] And Paul says they don't deploy a service without installing Rollbar first.
[33.32 → 34.58] It's that crucial to them.
[34.86 → 36.60] We operate at serious scale.
[37.04 → 42.44] And literally the first thing we do when we create a new service is we install Rollbar in it.
[42.64 → 45.52] We need to have that visibility.
[45.94 → 50.44] And without that visibility, it would be impossible to run at the scale we do.
[50.58 → 52.54] And certainly with the number of people that we have.
[52.72 → 55.70] We're a relatively small team operating a major service.
[55.70 → 61.46] And without the visibility that Rollbar gives us into our exceptions, it just wouldn't be possible.
[61.84 → 62.00] All right.
[62.02 → 67.26] If you want to follow in Paul's footsteps and start deploying with confidence today, head to Rollbar.com slash Changelog.
[67.38 → 70.34] Once again, Rollbar.com slash Changelog.
[70.34 → 81.94] Welcome to JS Party, a community celebration of JavaScript and the web.
[82.16 → 84.62] Quick heads up, this episode does have some swearing.
[84.82 → 86.30] We normally bleep swear words.
[86.44 → 88.20] But in this case, it's just one word.
[88.40 → 89.56] It's repeated quite a bit.
[89.80 → 91.72] And it also is part of the conversation.
[91.94 → 93.64] You'll understand once you get there.
[93.64 → 97.88] So if you're listening with sensitive ears nearby, you might want to wait for a better time.
[98.24 → 99.66] But otherwise, here we go.
[103.44 → 104.72] All right.
[104.84 → 106.20] Hello, JS Party people.
[106.34 → 109.52] This is K-Ball reporting live from Jam stack Cone SF.
[109.86 → 113.78] I'm here with Katie Silver-Miller, front end architect at Etsy.
[113.86 → 114.26] Yes.
[114.46 → 114.70] Yes.
[114.70 → 115.50] As of today.
[115.88 → 116.38] As of today.
[116.48 → 117.12] That's amazing.
[117.50 → 117.70] Yeah.
[117.78 → 118.34] Big day.
[118.34 → 122.62] So I'm going to ask you about front end architecture and architecting because I think that's a good thing.
[122.62 → 124.32] But first, let's talk about your talk.
[124.48 → 124.66] Yes.
[124.66 → 127.36] So you had a talk here at Jam stack Cone yesterday.
[127.54 → 127.90] Is that right?
[128.06 → 128.10] Yes.
[128.10 → 129.18] Can you tell us a little bit about it?
[129.36 → 129.56] Yeah.
[129.66 → 132.58] So my talk was called Git on the Jam stack.
[133.20 → 139.94] So a couple of years ago, like three years ago now, I made this ridiculous website called Oh Shit Git,
[140.46 → 147.98] which is a list of problems that I got into with Git all the time and then a list of steps on how to solve them.
[147.98 → 153.42] And the website kind of went viral extremely unexpectedly to me.
[153.58 → 158.18] I feel like the name of it just captures a common sentiment among developers.
[158.70 → 158.74] Yeah.
[158.88 → 167.46] No, I really, I think that was like the key to success is that I came up with this ridiculous and memorable name for the website.
[167.46 → 171.68] And it surprisingly was still available to buy the domain.
[173.00 → 173.90] That's amazing.
[174.12 → 174.36] Okay.
[174.36 → 176.94] So talking about that and the Jam stack.
[177.14 → 177.66] Yeah, exactly.
[178.00 → 183.78] So yeah, Phil reached out to me and was like, hey, you know, you want to come and talk at this conference?
[184.62 → 185.92] And I was like, cool.
[186.50 → 188.76] I didn't even know what the Jam stack was.
[188.90 → 190.46] I had to go Google it.
[190.66 → 191.92] You know, I'd heard about it, of course.
[192.00 → 193.92] People are talking about it around the industry.
[193.92 → 197.20] But, you know, I didn't remember what J-A-M stood for.
[197.20 → 202.64] And so I was kind of like, are you sure you really want me to talk at your conference?
[203.02 → 204.34] And he was like, no, no, no, no, no.
[204.44 → 209.42] Like Git is such a huge core component of the Jam stack.
[209.56 → 211.84] And I'd love it if you could come and talk about Git.
[212.60 → 215.08] So, you know, I talk about Git a lot.
[215.08 → 218.22] I've given talks many times and workshops.
[218.96 → 228.36] And so I kind of used this as motivation to go out and learn about the Jam stack and how Git powers the Jam stack.
[228.36 → 241.66] And so I did that by actually taking oh shit git, which had been an index.html file that I crafted in about two hours, three years ago.
[242.24 → 252.46] And actually moved it into Git for the first time and rebuilt it with Eleventh as a static page builder.
[253.12 → 256.06] There's something ironic about oh shit git not living in Git.
[256.06 → 256.40] Right?
[256.72 → 256.98] I know.
[256.98 → 260.72] It was almost like a badge of honour at first.
[261.12 → 264.26] Like people would be like, oh, you know, is it in Git?
[264.44 → 265.52] Can I link to it?
[265.52 → 266.28] And I would be like, no.
[267.28 → 269.66] This is as old school as you get.
[270.12 → 270.94] Yeah, basically.
[271.28 → 272.62] So, yeah.
[272.76 → 279.52] And, you know, for a lot of years people have been reaching out and asking, hey, can I translate your content into my language?
[279.52 → 285.16] And my answer was usually that's a great idea, but not now.
[285.16 → 290.14] Because there really wasn't a good mechanism for people to submit new translations.
[290.14 → 297.68] So I kind of, you know, used this conference and this talk as motivation to enable that.
[297.68 → 300.14] And so now it's been translated into German.
[300.14 → 312.80] I think I've had people volunteer for French, Serbian, Turkish, Russian, Portuguese.
[312.80 → 316.16] So none of those are complete yet, but they're coming.
[316.16 → 320.30] So do you get them to make more inventive cursing for each one?
[320.30 → 322.90] Yeah, I kind of, it's funny.
[323.16 → 333.52] So the guidance that I gave in the instructions is basically like I use a lot of idioms and a lot of swears that, you know, probably don't translate directly.
[333.52 → 335.08] And I say, you know, just be free.
[335.34 → 344.80] And just all I ask is that you keep the oh shit part in some way, you know, whatever the equivalent of oh shit is in your language.
[345.40 → 345.42] So.
[345.82 → 345.98] Right.
[347.56 → 349.28] Skeins in German, I guess.
[350.30 → 351.66] Oh, skeins, Neisse.
[352.14 → 352.38] Skeins.
[354.62 → 355.38] Oh, dear.
[355.50 → 356.00] So, okay.
[356.10 → 359.14] So first experience with Jam stack stuff and rebuilding this.
[359.34 → 360.32] How did you feel?
[360.40 → 366.00] Because I know a lot of our listeners are probably looking at this and saying that looks kind of interesting, but I don't know.
[366.52 → 380.04] Yeah, I think, you know, it's my favourite thing by far, especially I decided to use Netlify for hosting and I decided to use Eleventh.
[380.30 → 384.78] Just because it was the simplest and quickest and easiest setup.
[384.78 → 390.50] And I know Zach personally, so I can reach out to him and bother him with questions.
[391.06 → 394.52] It always helps to know the maintainers or the authors of these frameworks.
[394.90 → 395.10] Yeah.
[395.38 → 396.50] This doesn't make sense.
[396.60 → 396.82] Right?
[396.82 → 399.96] But I, no, I think it's great.
[399.96 → 412.06] I think to me the real killer feature was, you know, I wanted to move into the stack and then basically immediately re-architect the entire page.
[412.18 → 417.00] You know, like at first I've just brought over my flat index.html file.
[417.12 → 417.34] Right.
[417.34 → 430.32] And then I went through the re-architecting and by using a separate branch in Git and then using branch deploy previews via Netlify, I had to...
[430.32 → 431.82] Which is so freaking amazing, by the way.
[432.06 → 435.10] Okay, I'm going to push this up and I get a preview right away.
[435.24 → 436.18] I can send it to someone else.
[436.18 → 437.14] I can send it to me.
[437.48 → 437.78] It's so cool.
[437.78 → 451.96] It's, I mean, I don't, you know, I'm assuming that, you know, these kinds of things don't happen in isolation and Netlify probably was not the first people to think of this or, but there's just something about it that makes so much sense.
[452.58 → 455.32] The execution that they have there is awesome as well.
[455.32 → 469.26] It was so seamless, and it really allowed me to feel comfortable re-architecting the site and going out and testing and looking at it and making sure that all the redirects work.
[469.26 → 484.12] I mean, the fact that you can even set up individual, like, redirects in a, you know, basically a TOML file and then push that out to your branch and the branch handles all the redirects the same way that, like, the regular site would.
[484.12 → 487.28] But that, I mean, it really made it so easy.
[487.90 → 504.74] So I think, you know, especially for blogging sites, you know, Ocean Cut's not necessarily a blog site, but it's kind of similar in a way that it's like I, you create the content, and it just stays the same, and it's not very dynamic.
[505.08 → 505.18] Right.
[506.18 → 509.00] So I think it's a really, perfect fit, basically.
[509.00 → 517.40] So, and there's been a lot of, I have been learning a lot from this conference about the way cooler stuff that the Jam stack can do.
[517.88 → 518.22] I know.
[518.38 → 518.56] Yeah.
[518.60 → 520.32] I keep, like, dabbling my toes in.
[520.38 → 521.38] I recently launched a new site.
[521.44 → 523.02] That is essentially a blog, right?
[523.08 → 525.32] But I'm like, okay, what can I do with this?
[525.36 → 526.02] This is fun.
[526.12 → 526.84] This is exciting.
[527.26 → 527.70] Yeah, totally.
[527.98 → 528.18] Yeah.
[528.24 → 530.08] There's some neat stuff going on.
[530.08 → 538.18] So you mentioned something that is going to segue me back into talking with you about something we talked about earlier, which are you said, oh, you re-architected it.
[538.20 → 538.46] Yeah.
[538.68 → 541.20] And you just got promoted to front-end architect.
[541.34 → 542.32] Yes, yes.
[542.42 → 545.08] Let's talk a little bit about what that even means in the front-end.
[545.24 → 545.46] Okay.
[545.46 → 548.50] Like, what does front-end architecture entail in your mind?
[549.10 → 549.40] Yeah.
[549.40 → 551.62] So I think it's a couple of things.
[552.76 → 565.16] So I think it's, we have all of these product teams at Etsy who are going out, and they're focused really on features and products.
[565.88 → 572.18] And then we have our front-end infrastructure teams, which I have been on, you know, my time at Etsy.
[572.32 → 573.72] I've always been on front-end infrastructure.
[573.72 → 588.36] And there's this problem where when you're in infrastructure, you're not building product, you know, you're thinking about the longer term and the bigger picture.
[588.36 → 593.98] And you want to make sure that you're providing tools and workflows that work for product engineers.
[594.28 → 594.58] Right.
[595.32 → 599.24] Because, frankly, product engineers don't always have time to think about that.
[599.36 → 601.04] You know, they're under time constraints.
[601.16 → 601.84] They have deadlines.
[601.84 → 604.84] They have financial goals they need to meet.
[606.10 → 624.48] So it's kind of been growing organically for a long time that I was moving more into looking at strategy overall and making connections with folks on product teams and reaching out to them and really being like, what are your stumbling blocks?
[624.62 → 625.44] What do you need?
[625.44 → 639.56] And then on the other side of things, you know, Etsy, we have this philosophy of using boring tech, which in the front-end space, I do.
[639.72 → 640.42] I love it as well.
[640.52 → 645.98] But I think that in the front-end space, it resulted in us falling behind the times.
[646.18 → 646.50] Right.
[646.50 → 663.16] And we've been working really hard to modernize our stack and get off of our, you know, we just switched from our old homegrown Requires build system that was built in 2011 to Webpack, finally.
[663.16 → 670.04] So there are a lot of different pieces of the stack that we need to modernize.
[670.28 → 673.76] And somebody needs to figure out how we're going to do that.
[673.92 → 674.18] Yeah.
[674.66 → 676.18] That's a fascinating problem.
[676.30 → 687.82] Because I like this philosophy of use boring tech is essentially saying, as I understand it, and you would know better than I did, but as I understand it, don't get shiny object syndrome.
[687.82 → 688.10] Yep.
[688.16 → 688.34] Right?
[688.52 → 691.82] Do what's going to work to solve the problem at hand.
[691.88 → 692.10] Totally.
[692.24 → 699.28] Without getting pulled into, oh, I got to microservice this, and I got to, you know, bundle all this, and whatever else is.
[699.38 → 702.30] But the challenge is you still don't want to build up lots of tech debt.
[702.42 → 702.56] Yeah.
[702.56 → 706.76] And you still don't want to, you know, fall behind in terms of capabilities.
[706.76 → 707.14] Mm-hmm.
[707.14 → 711.76] Because, yes, oftentimes the boring tech is good enough.
[711.84 → 712.16] Mm-hmm.
[712.62 → 714.98] But sometimes you lose a lot of productivity staying in boring tech.
[714.98 → 715.20] Totally.
[715.20 → 717.02] Because there are actual breakthroughs that happen.
[717.02 → 717.42] Totally.
[717.42 → 717.54] Totally.
[717.66 → 724.42] And I think that's something that we've seen is, you know, we have two different parts of the site.
[724.52 → 729.12] So there's like the public-facing site that everyone goes to when they're shopping on Etsy.
[729.24 → 735.78] And then there's a whole back-end site for the people who are selling their homemade items on the site.
[736.66 → 743.88] And for a long time there's been this split where the seller back-end was built first in Backbone and Marionette.
[743.88 → 748.74] And then a couple of years ago, I think in 2015, we started switching over to React.
[748.74 → 751.42] And now it's entirely built in React.
[751.42 → 765.00] But then our front-end buyer side because, you know, we haven't said, okay, we're going to accept the challenges of building a spa that actually works.
[765.04 → 767.40] Because obviously SEO is huge for us.
[767.64 → 767.76] Yeah.
[767.76 → 770.14] Performance is huge for us.
[770.14 → 770.32] Yep.
[770.32 → 781.42] So we had this mostly like jQuery-based JavaScript ecosystem in our buyer front-end.
[781.92 → 786.98] But it's getting to the point now where teams aren't just working on buyer or seller.
[787.12 → 790.04] They're working across the product, you know.
[790.22 → 790.36] Yep.
[790.36 → 796.26] And it's hard to have transferable skills between the two.
[796.60 → 796.88] Yeah.
[797.02 → 802.88] Well, and hard to have consistent design systems if you have to have totally different implementations and consistent interactions.
[803.28 → 803.46] Yeah.
[803.74 → 804.72] No, it's funny, actually.
[804.72 → 808.84] So for a long time my team owned the design system at Etsy.
[809.08 → 818.18] And we actually built an entire framework that would allow us to have a core vanilla JavaScript file for all of our design system components.
[818.18 → 824.38] That would then either get wrapped up in vanilla JS to handle all the DOM manipulation.
[824.70 → 831.58] Or it would get wrapped up in a React component that would handle the React lifecycle and all of that.
[832.00 → 835.74] Because we were like, everything's getting so out of sync.
[835.84 → 837.18] One version's accessible.
[837.46 → 838.88] The other version isn't.
[839.00 → 840.86] The functionality's slightly different.
[841.24 → 841.46] Yep.
[841.46 → 843.86] So, yeah.
[844.02 → 850.08] And I think also to that, you know, we hire a lot of folks who come out of boot camps.
[851.10 → 855.22] And they don't understand jQuery.
[855.42 → 856.26] They've never used it.
[856.34 → 857.04] They've never seen it.
[857.10 → 860.32] They don't have to worry about this.
[860.32 → 860.72] Yeah.
[862.06 → 867.16] And how all the crazy hoops you jump through to maintain what this is.
[867.16 → 869.24] Because they're used to ES6.
[869.38 → 871.46] They're used to building everything in React.
[871.60 → 872.80] Building a node on the server.
[873.58 → 873.76] Yeah.
[873.88 → 874.66] That is interesting.
[874.74 → 876.22] That's the other side of boring tech.
[876.54 → 879.06] Does that mean boring engineers?
[879.42 → 879.70] Yeah.
[879.76 → 880.20] Right.
[881.48 → 883.60] Or maybe I should say bored engineers.
[883.88 → 883.98] Yeah.
[884.14 → 884.30] Yeah.
[884.30 → 889.20] No, I think it leads to frustrated engineers.
[889.86 → 893.84] And it leads to frustrated infrastructure folks like myself.
[894.24 → 899.78] Because, you know, we see code that we know is not performant.
[899.88 → 901.56] That we know isn't written the best way.
[901.66 → 903.42] But I don't blame the engineers at all.
[903.58 → 907.72] Because they're used to this completely different programming paradigm.
[908.16 → 910.60] And you kind of throw them in and say, here you go.
[910.60 → 912.12] So, yeah.
[912.20 → 913.92] So, that's one of the big things that we're working on.
[914.02 → 920.50] Is figuring out how to do server-side React rendering.
[920.88 → 922.62] And then hydration on the client.
[922.82 → 923.74] So that we can do.
[924.96 → 926.42] We can share components.
[926.66 → 927.88] We can share knowledge.
[928.40 → 932.00] But we don't sacrifice SEO and performance.
[940.60 → 952.68] This episode is brought to you by DigitalOcean.
[953.00 → 956.94] DigitalOcean is the simplest cloud platform for developers and teams.
[956.94 → 963.74] With products like droplets, spaces, Kubernetes, load balancers, block storage, and pre-built one-click apps.
[964.06 → 969.66] You can deploy, manage, and scale cloud applications faster and more efficiently on DigitalOcean.
[969.66 → 976.08] Whether you're running one virtual machine or 10,000, DigitalOcean makes managing your infrastructure way too easy.
[976.44 → 978.86] Head to do.co slash changelog.
[979.08 → 981.90] Again, do.co slash changelog.
[992.02 → 993.58] Are you looking at next?
[993.74 → 998.70] Or is that because you've got so much established stuff you can't really go with a framework like that?
[998.70 → 1000.70] Yeah, so I think what we're looking at right now.
[1001.50 → 1005.70] So Airbnb has an open source thing called Hypernova.
[1006.48 → 1012.36] Which is basically a server that you pass a React component and a bunch of context data.
[1012.60 → 1015.22] And then it will render the HTML and return it to you.
[1015.48 → 1023.96] So what we've been exploring first is basically taking that and bolting it into our existing PHP framework.
[1023.96 → 1026.04] So we're like a big PHP shop.
[1026.30 → 1026.52] Right.
[1027.70 → 1033.50] And basically instead of using right now we have moustache files that we render on the server.
[1033.50 → 1043.14] There would be a way to sort of indicate, okay, this particular PHP view uses a JSX file instead.
[1043.62 → 1043.86] Right.
[1043.86 → 1046.78] And then it would go off and come back.
[1047.06 → 1052.12] The service would come back with the rendered markup, which we'd inject into the rest of the page,
[1052.20 → 1053.88] which is still probably coming from PHP.
[1054.30 → 1054.62] Right.
[1054.70 → 1055.50] And then that way...
[1055.50 → 1058.16] You basically use it as an external emulating engine.
[1058.32 → 1058.36] Exactly.
[1058.36 → 1062.58] You pass off PHP data as JSON that becomes context and renders interesting.
[1063.02 → 1063.24] Exactly.
[1063.74 → 1063.94] Okay.
[1064.08 → 1064.72] Now I'm curious.
[1064.94 → 1066.94] We're super early in the process.
[1067.30 → 1067.88] Yeah, yeah, yeah.
[1068.98 → 1070.60] Well, so I'll ask questions.
[1070.66 → 1071.60] And if you don't know, you don't know.
[1071.76 → 1071.80] Okay.
[1071.80 → 1075.32] So what's the...
[1075.32 → 1079.96] I assume you're having the server co-located, so it's on the same node as the PHP server where it's running?
[1080.04 → 1082.12] Or are you going over a network hop to render that template?
[1082.14 → 1085.72] So we are all in Google Cloud at this point.
[1086.22 → 1092.92] So I think that what we're looking at right now is that it would be a separate service running in Google App Engine.
[1093.62 → 1100.50] So it is effectively an HTTP request, but it's all happening internal to our Google Cloud clusters.
[1100.50 → 1102.98] So what kind of latency do you see from that?
[1103.66 → 1104.68] We don't know yet.
[1106.10 → 1111.06] We just have a proof of concept that just started.
[1111.18 → 1115.96] But my hope is that we can do a lot of caching.
[1118.82 → 1119.86] I'm thinking...
[1119.86 → 1125.14] I mean, obviously, we're going to have to wait and see what kind of features people are going to want to build out with this.
[1125.14 → 1134.86] But I'm guessing a lot of it is going to be things like, you know, a hard problem is sorting and filtering in search results.
[1135.78 → 1136.06] Right?
[1136.16 → 1142.58] Like, I'm hopeful that the markup for that isn't going to change a ton.
[1142.58 → 1147.20] It's more the items themselves that we display.
[1147.42 → 1158.38] And so I think it's going to require a lot of consideration and thought on how we structure the modules so that we can cache as much as possible
[1158.38 → 1168.16] and then reduce the surface area of the really dynamic content that's actually going to need to go all the way to the hypernova service.
[1168.36 → 1168.54] Yeah.
[1168.72 → 1169.30] Though, interesting.
[1170.32 → 1174.86] So can you send it a set of requests in one HTTP request?
[1175.58 → 1175.84] Yeah.
[1175.84 → 1179.14] I think we're getting a little outside...
[1179.14 → 1183.92] So my colleague, Allie Jones, is actually the one who's been working on the proof of concept.
[1184.28 → 1188.94] But I believe that it's parallelizable.
[1189.62 → 1190.76] I could be wrong.
[1191.76 → 1192.16] Interesting.
[1192.40 → 1192.58] Because, yeah, I'm thinking about...
[1192.58 → 1194.96] If it isn't parallelizable, we should make it.
[1195.26 → 1196.08] Yeah, yeah, yeah.
[1196.20 → 1196.62] Exactly.
[1196.80 → 1197.02] Well, yeah.
[1197.08 → 1201.12] Thinking about, right, like in that server-side world, which is...
[1201.12 → 1203.00] I think some of our folks are in that world.
[1203.06 → 1204.18] They're with Node and things like that.
[1204.18 → 1207.26] But network requests are the most expensive thing.
[1207.32 → 1207.54] Yep.
[1207.82 → 1212.38] And so imagining this situation, you either are going to want to do it at the page level,
[1212.48 → 1215.48] where you're just like, okay, this whole page is React, and I'm going to do one fetch,
[1215.52 → 1217.10] and it's going to render everything over there.
[1217.60 → 1221.62] Almost where PHP is just your data layer, and then you're passing that over.
[1223.20 → 1227.00] Or you'd want to have, like, here's the set of components I need,
[1227.04 → 1229.38] and I send them all in one request and get them all back.
[1229.38 → 1229.66] Yeah.
[1230.24 → 1234.16] Yeah, I think we're definitely more on the latter side of things.
[1234.18 → 1241.38] Because, you know, just thinking long-term about what the rollout plan is going to look like.
[1241.58 → 1246.12] I mean, it'll probably start with we'll pick one component on the page.
[1246.86 → 1253.66] You know, maybe it's the logged-in user menu or something like that that's highly interactive.
[1253.96 → 1256.18] Or maybe it's our conversations UI.
[1257.02 → 1257.30] Right.
[1257.30 → 1262.46] And we'll just pick that one little tiny piece of the page and then just start there.
[1262.72 → 1262.94] Yeah.
[1263.08 → 1270.32] With the expectation that, you know, a lot of the stuff that we serve in our markup, it's not dynamic.
[1270.48 → 1270.88] It doesn't need to be.
[1270.88 → 1272.02] It doesn't need to be in React.
[1272.08 → 1273.06] It doesn't need to be React.
[1273.26 → 1275.56] I love that because that lets you migrate gradually.
[1275.78 → 1275.96] Exactly.
[1275.96 → 1281.00] Which is something that is so often neglected in this ecosystem because we're like, okay, just use the latest and greatest thing.
[1281.00 → 1283.92] That doesn't work if you have a massive existing application.
[1284.62 → 1291.66] No, that's always the hardest problem, I think, in infrastructure is figuring out how do you do rollouts effectively?
[1292.22 → 1294.84] How do you stay on top of adoption?
[1294.84 → 1311.40] You know, we have a lot of things that are still kind of hanging around seven, eight, nine years later because we didn't focus as much as we probably should have on getting full adoption.
[1311.40 → 1330.44] And then it becomes this, like, compounding problem where when we want to try to build new things, we have to accommodate the four different historical architectures of Etsy.com that are still lingering in various corners of the code base.
[1330.44 → 1342.20] So, you know, all of our new infrastructure projects take twice as long as they probably should because we have to backfill.
[1342.56 → 1342.68] Right.
[1342.78 → 1343.64] It all has to keep running.
[1343.94 → 1344.00] Yeah.
[1344.12 → 1345.58] You can't start from scratch.
[1345.64 → 1346.40] You've got a business going.
[1346.50 → 1346.92] Exactly.
[1347.84 → 1348.94] So, it's kind of funny.
[1348.94 → 1360.74] We have a huge culture of rotations and boot camps at Etsy where folks can go and hang out on another team for a week or a month and just sort of get a taste for what other people are doing.
[1361.42 → 1365.36] And we've had multiple product engineers come and hang out with us.
[1365.56 → 1369.10] And at the end, they're like, I don't want to be an infrastructure engineer.
[1371.24 → 1373.46] I don't know how you do what you do.
[1373.54 → 1375.42] And I'm like, honestly, I don't know how you do.
[1375.54 → 1377.44] I could never be a product engineer again.
[1377.44 → 1381.68] And someone would be like, hey, Katie, you know, can you go build this feature?
[1381.88 → 1389.58] And I would be like, okay, here's a framework for building that feature that's going to make it more maintainable and robust and easier to build.
[1389.80 → 1392.68] And so, for life.
[1392.84 → 1395.54] I'm an infrastructure engineer for life.
[1396.04 → 1396.18] Yeah.
[1396.18 → 1406.28] So, I'm curious to explore this more because this kind of migration question is something that I think that we, it's underserved in terms of educational content for folks.
[1406.28 → 1414.44] So, you mentioned there's like four existing legacy architectures that I imagine you're trying to gradually remove at least some of the older ones.
[1414.56 → 1418.42] So, what's the process for, okay, we've decided we're moving on from this approach.
[1418.42 → 1424.34] How do you get there, you know, get to the next approach from there?
[1424.58 → 1424.82] Yeah.
[1425.02 → 1433.66] So, I think a lot of it is, you know, and I will be 100% honest that I think this is something that we're still constantly learning about.
[1433.66 → 1438.04] It's a really hard problem, and we don't always get it right.
[1438.74 → 1445.68] But I think a lot of it starts with thinking about developer experience.
[1446.48 → 1451.74] And, you know, I joke that I'm not a feature or a product developer, but really I am.
[1451.90 → 1455.82] And it's the product, though, that I'm building is for other engineers.
[1455.82 → 1474.32] And I think you have to have a lot of empathy and a lot of concern and care to make sure that the underlying structure of what you are building doesn't leak into the API that you expose for engineers to use.
[1474.32 → 1483.06] And that the API works in a way that the engineers who are using it think about it, you know.
[1483.26 → 1494.46] And so, you have to put yourself in the shoes of someone who's going to be using this and thinking what's going to be the easiest way for them to switch to using this.
[1494.60 → 1494.86] Right.
[1494.86 → 1505.18] And then I think it's just about partnering with teams, getting folks to, like, start to use what you built and have success with it.
[1505.22 → 1510.42] And then they share that and then other people start getting excited and want to use it, too.
[1511.52 → 1514.78] So, that gives me some about how you get them on the new thing.
[1514.84 → 1516.36] But how do you get rid of the old thing?
[1516.46 → 1517.04] Oh, God.
[1517.40 → 1518.24] It's hard.
[1521.30 → 1523.86] Ownership is a big problem.
[1523.86 → 1524.76] I don't know.
[1525.00 → 1528.76] I honestly don't know if other large organizations have this problem.
[1529.10 → 1530.74] I would wager they do.
[1530.74 → 1532.52] I would wager they probably do.
[1532.90 → 1543.66] But, yeah, that's something that we struggle with is what do we do with all of these ancient features that, for whatever reason, we don't want to get rid of, but nobody's actively working on them.
[1543.84 → 1544.04] Yeah.
[1545.12 → 1548.88] Because, honestly, the upgrade path for that is probably non-existent.
[1548.88 → 1549.88] Mm-hmm.
[1549.88 → 1560.60] So, I think something I've been kind of toying around with is coming up with a framework for, like, okay, let's rank our pages.
[1561.22 → 1570.18] A lot of times we rank things based on how much they contribute to, like, conversion or seller happiness or seller growth.
[1570.18 → 1575.86] And then we have these other pages, though, where it's not clear what their value is.
[1576.14 → 1576.22] Right.
[1576.22 → 1584.40] And maybe we need to sort of accept the fact that we're always going to have parts of the site that we're never going to upgrade or touch.
[1584.76 → 1588.92] And maybe what we need to do is wall them off into, like, a walled garden.
[1589.14 → 1589.64] Yeah.
[1589.64 → 1600.50] Where we don't worry about the fact that we're duplicating code or that we are, you know, taking copies of files that we're updating other places.
[1600.50 → 1604.32] But just sort of saying, okay, here be dragons.
[1604.72 → 1610.08] We accept that here be dragons, and we're not going to try to ever bring this forward.
[1610.28 → 1610.96] Mm-hmm.
[1612.18 → 1613.56] Because let's be realistic.
[1614.28 → 1616.52] That's what happens, you know?
[1616.52 → 1637.28] So, yes, that's something I've been kind of talking and thinking about with people a lot is, like, all right, can we make some wild gardens of code where we're not going to invest the time and energy that it takes to upgrade it until, as an organization, we decide that it's important.
[1637.64 → 1637.82] Yeah.
[1637.94 → 1639.14] No, that makes a ton of sense.
[1639.14 → 1644.62] Because, yeah, a migration path I've seen before or done before is you have sort of this walled garden of this is the old stuff.
[1644.62 → 1644.92] Mm-hmm.
[1645.54 → 1649.48] Or sometimes you start with you have a walled garden that this is the new and beautiful stuff.
[1649.48 → 1649.56] This is the new, yeah.
[1649.86 → 1653.98] And then you gradually, piece by piece, try to move things between one and the other.
[1654.06 → 1655.44] But you treat them completely differently.
[1655.72 → 1655.90] Yeah.
[1656.00 → 1667.62] I think the pattern that we've generally used is more of, like, a hybrid where we make the new stuff backwards compatible with the old stuff so you can kind of mix and match.
[1667.62 → 1671.54] Which has its, as with everything, there are trade-offs, you know?
[1671.54 → 1671.64] Yeah.
[1671.64 → 1683.96] Like, the trade-off with that is that the old stuff has a tendency to stick around longer, but it makes it easier to do, like, a gradual rollout, you know?
[1684.16 → 1688.38] I think, what is it, like, the Strangler Pattern?
[1688.44 → 1689.62] Have you heard of, like, the Strangler Pattern?
[1690.26 → 1692.26] I think so, but let's review it for the...
[1692.26 → 1706.80] It's a terrible name, but basically the idea is that you kind of, it's like a Strangler vine grows around a tree and then gradually eats the tree away and replaces it.
[1706.92 → 1715.22] So I think the idea is that you build new stuff around the old stuff and slowly kind of eat away at it until the old stuff is gone.
[1715.78 → 1717.30] I could be butchering that.
[1717.30 → 1724.22] I apologize in advance if I butchered what the Strangler Pattern means.
[1724.84 → 1727.04] It's a very graphic metaphor for code.
[1727.48 → 1734.48] Okay, we're going to wrap it up in this new stuff and Webpack is slowly going to strangle the life out of our old code.
[1734.48 → 1734.68] Yeah, yeah.
[1736.18 → 1737.86] Not to pick on Webpack, but...
[1737.86 → 1738.56] No, no.
[1739.26 → 1740.18] I like Webpack.
[1740.36 → 1742.48] I'm glad we actually have it now, so...
[1742.48 → 1752.44] Yeah, it's fun because it's easy to hate on Webpack because there are so many configuration challenges as far as they've come, but there's a reason we all keep adopting it, too.
[1752.50 → 1752.70] Yeah.
[1752.94 → 1759.46] You know if you go back to the older ways, like, you can't do a lot of the things you can now do with Webpack.
[1759.58 → 1762.10] And yeah, it's hard, but, like, complexity is conserved.
[1762.18 → 1762.96] It's got to be somewhere.
[1762.96 → 1772.36] Yeah, well, we have a team of three people whose entire job it was for a year was to figure out how to migrate us onto Webpack.
[1772.68 → 1775.70] So, it's not easy by any stretch of the imagination.
[1776.36 → 1776.50] Yeah.
[1777.14 → 1778.42] But it was worth it.
[1778.54 → 1779.18] You know, we...
[1779.18 → 1780.96] Again, with the boring tech, we sort of...
[1781.80 → 1790.42] It took us a little while, but once it became pretty clear that Webpack was, like, the de facto standard and the support is there,
[1790.42 → 1796.80] the maintenance is there, we said, okay, it's time to start using it.
[1803.26 → 1810.94] This episode is brought to you by Algeria, search technology to power your business, trusted by Twitch, Stripe, Adobe, and many more.
[1811.26 → 1816.84] Even us, yes, we use them to power our search, and we love the way they obsess over that developer experience.
[1816.84 → 1821.48] They let us fine-tune the index for the best results and report back what people are searching for,
[1821.72 → 1825.26] even servicing search terms that get zero results, which we love.
[1825.50 → 1829.98] Check the show notes for a link to get started for free, or head to algolia.com to learn more.
[1829.98 → 1847.70] Another topic I wanted to pick your brain on, though I'm supposed to get away from using that metaphor,
[1847.84 → 1851.68] because that's also a little bit of a weird visual there.
[1851.68 → 1853.00] This is a Halloween episode.
[1853.32 → 1853.86] I know, right?
[1853.86 → 1860.52] Another topic I wanted to ask you about, to not try any metaphors, is design systems.
[1860.80 → 1860.94] Yes.
[1860.94 → 1865.00] Because I saw that you were one of the authors of the Design System Handbook.
[1865.12 → 1865.32] Yeah.
[1865.44 → 1870.54] That I think Envision sort of coalesced together from different folks, and you brought it up a little bit.
[1870.66 → 1873.84] So tell us a little bit about how you think about design system.
[1873.94 → 1874.72] What makes a good one?
[1874.78 → 1875.68] How do you develop it?
[1875.68 → 1876.12] Yeah.
[1876.66 → 1883.70] Yeah, I think, so, you know, design systems to me, I think, is this natural progression that, you know,
[1883.72 → 1886.24] I've been doing this for almost 15 years.
[1886.76 → 1890.56] And throughout that time, I mean, it's had a lot of different names.
[1890.72 → 1893.06] First, it was style guide, and then component library.
[1893.06 → 1898.26] And, you know, it just makes sense.
[1898.40 → 1905.68] You know, every other, like, computing language uses small, reusable modules of code.
[1905.84 → 1909.00] So, I mean, it's an idea that just makes sense.
[1909.94 → 1913.72] But I think that, again, you know, kind of like what I said before,
[1914.60 → 1921.84] the difference between a successful design system and an unsuccessful one is really putting care into that API.
[1923.06 → 1930.10] And thinking about, all right, how, you know, the way that you build a, you know,
[1930.12 → 1939.00] a custom dropdown component to handle your specific product use case versus the way that you build something
[1939.00 → 1947.58] that is completely reusable and exposes an API that allows multiple different teams to inject their own data
[1947.58 → 1953.70] and their own interaction into a component that handles opening it, animating it.
[1954.36 → 1957.28] You know, how do you surface what the user selected?
[1957.98 → 1962.84] How do you handle accessibility is a huge challenge for things like that.
[1963.58 → 1965.54] You know, it's a completely different mindset.
[1965.54 → 1978.56] And systems thinking has to go into every layer of the design system, basically.
[1979.18 → 1987.48] And I think it's really exciting that several years ago, you know, gosh, it was probably eight or nine years ago now
[1987.48 → 1992.70] that I, at my job, I suggested that we create a reusable pattern library
[1992.70 → 1997.08] because I was getting so frustrated that, you know, it's like the Fifty Shades of Grey.
[1997.96 → 2004.44] Like, every single, you know, every single Photoshop document, because it was Photoshop then,
[2004.84 → 2008.92] they sent to me, had four different grays and they weren't standard and nothing.
[2008.92 → 2014.22] And I was like, for the love of God, please give me something that I can reuse.
[2014.84 → 2014.98] Yes.
[2015.34 → 2019.16] And I think at that point, the designers were kind of like, what?
[2019.54 → 2027.70] But it seems to me that designers are, like, much more on board.
[2028.00 → 2034.46] You know, a lot of organizations, and at Etsy actually, our design system initially came out of designers, not engineers.
[2034.72 → 2034.90] Yeah.
[2035.06 → 2036.38] Which I think is amazing.
[2036.56 → 2036.70] Yeah.
[2036.70 → 2045.80] You know, and I'm like, I'm really glad to see this kind of component-based development becoming a thing
[2045.80 → 2048.66] because it makes so much sense on so many levels.
[2049.06 → 2049.36] Yes.
[2049.58 → 2049.82] Okay.
[2049.88 → 2051.94] So, let me dig a little deeper into that.
[2052.00 → 2054.94] So, you mentioned systems thinking at each level of the design system.
[2054.94 → 2060.50] So, can you maybe play out, first, what are the layers of the design system that you're thinking of?
[2060.74 → 2064.76] And then maybe highlight a little bit about how systems thinking influences each one?
[2065.06 → 2065.22] Okay.
[2065.22 → 2065.62] Yeah.
[2065.62 → 2065.72] Yeah.
[2065.80 → 2075.96] So, I think, you know, it's sort of, if you think about, you know, Brad Frost introduced kind of the atomic design language a long time ago.
[2076.04 → 2078.26] And I think a lot of it still makes sense.
[2078.36 → 2080.48] You know, you kind of start with, like, what are your colours?
[2080.68 → 2081.44] What are your fonts?
[2081.56 → 2082.54] What are your icons?
[2082.54 → 2095.44] I'm thinking about putting together a colour palette that is something that designers can mix and match and express creativity,
[2095.44 → 2101.18] but also it meets accessibility requirements that you have strong guidelines about.
[2101.18 → 2107.26] Well, you never use the light gray on a white background.
[2107.38 → 2110.78] It only can be used for text on a black background, you know?
[2110.78 → 2114.24] And so, to me, I think that's one of the hardest pieces.
[2114.44 → 2126.24] And I'm glad that I work with really talented designers who can visually come up with, okay, this is what the visual and informational hierarchy of text on the page.
[2126.24 → 2132.18] That's the hardest part of any design system, I think, is something that you can reuse.
[2133.30 → 2141.20] And then from there, it's really thinking about components and what are the smallest pieces of your components.
[2141.20 → 2149.88] A lot of times, you know, a button might be, you know, I feel like that's the canonical thing for design systems because buttons are everywhere.
[2150.40 → 2151.26] Buttons are everywhere.
[2151.68 → 2153.04] You like to think they're simple.
[2153.40 → 2154.04] They are not simple.
[2154.04 → 2155.96] They are not simple at all.
[2156.26 → 2163.76] And, you know, I think, again, it kind of thinking about how do you write your CSS in such a way?
[2163.76 → 2178.04] You know, I think a lot of folks have adopted this idea of having a structural class and then themed classes and just thinking about the interactions between those and what options do you expose to people?
[2178.42 → 2180.80] How do you allow them to make the button bigger?
[2181.02 → 2182.66] How do you allow them to make the text bigger?
[2183.26 → 2185.94] What happens if they want to put an icon inside a button?
[2186.26 → 2188.94] What happens if the text wraps onto multiple lines?
[2188.94 → 2197.92] There are so many things you have to think about to build a component that seems so utterly simple, you know?
[2198.20 → 2198.40] Yeah.
[2198.40 → 2205.60] What's the difference between a button that submits a form versus a button that opens a custom dropdown?
[2207.86 → 2210.22] What about a button that changes the pagination?
[2210.68 → 2211.60] What does that look like?
[2211.70 → 2212.62] How do you build that?
[2212.88 → 2213.38] You know, so.
[2213.38 → 2221.50] And then from there, once you get into the more kind of complicated, you know, the interaction with a button is relatively easy.
[2222.06 → 2225.04] Although, obviously, the thinking about it is not.
[2226.72 → 2242.90] With your components, you know, that idea, again, of what are the smallest units that I can build, and how do they interact with each other and build up in order to make something really complicated like a modal overlay dialogue box, you know?
[2243.38 → 2260.64] Something like that, that is, it's massive in terms of making sure that the entire page is structured correctly so that a screen reader knows when this accessible dialogue box is open, that it should ignore everything else on the page.
[2260.82 → 2267.90] You have to know how to capture the focus and the tabbing, the handle tab order.
[2267.90 → 2273.52] You know, so there's all these, you know, so there's all these, like, really deep underlying facets to the interaction.
[2273.86 → 2282.26] But then there's also, like, what, how do I make it so that designers can use different sizes of it?
[2282.46 → 2290.60] What happens if they want to have a header or a footer that stays fixed in the modal and then the rest of it scrolls because it's taking over the whole page?
[2290.88 → 2291.70] What about mobile?
[2291.70 → 2293.44] Like, what about the tap interactions?
[2293.92 → 2300.90] So, I mean, it really, there's so much complexity on so every single level.
[2301.14 → 2305.54] And to me, the best design systems abstract away all of that complexity.
[2306.22 → 2316.46] And the folks who are, like, you know, the designers and the developers who use it, you know, maybe they don't even know that all that stuff is happening in the background.
[2316.46 → 2320.74] They just know that they can combine it, and it does what they want, you know?
[2320.94 → 2321.08] Yeah.
[2323.20 → 2323.90] That's interesting.
[2324.00 → 2328.86] It's almost like, so as we talked about, there's, so there's an implementation piece of this.
[2328.94 → 2334.40] But as you're talking about, there's thinking that is architectural thinking, but design, right?
[2334.46 → 2336.96] I don't know if I've ever seen the title design architect.
[2337.32 → 2337.44] Yeah.
[2337.44 → 2344.60] But it's almost like you need that separation of, like, I mean, there's a little bit of, okay, this person is specializing in graphical design, what the thing looks like.
[2344.60 → 2349.70] Like, this person's focusing on, I don't know, information architecture, I guess, is the closest area that I've heard.
[2349.94 → 2351.32] But, yeah, that's fascinating.
[2351.84 → 2359.74] And honestly, I think I've worked with, you know, several designers in the last four years at Etsy on building this design system.
[2360.00 → 2362.88] And they all are, like, design architects.
[2363.18 → 2366.38] You know, they think about those higher questions.
[2366.56 → 2367.54] They have systems.
[2368.38 → 2370.30] They have a systems' mindset, you know?
[2370.30 → 2379.10] And to me, I think that systems' mindset, really, it transcends just software architecture.
[2379.80 → 2379.98] Absolutely.
[2380.68 → 2381.24] Absolutely.
[2382.68 → 2383.68] That's super cool.
[2386.52 → 2388.98] I'm still, like, spinning thinking about design systems.
[2389.38 → 2391.60] I could talk about design systems all day.
[2391.60 → 2392.00] Yeah.
[2392.40 → 2392.84] Yeah.
[2393.00 → 2394.14] Well, and it's interesting.
[2394.70 → 2411.72] So, maybe the thing I would ask, if thinking about a design system from now the perspective of a front-end developer, what are the key pieces in terms of designing that API that are going to make a difference in the engineering utilization there?
[2411.72 → 2411.84] Hmm.
[2413.04 → 2416.58] Well, I think a lot of it really depends.
[2416.58 → 2422.28] So, there are a couple of different ways to approach how you build a design system.
[2422.54 → 2430.20] So, some design systems just provide, here are a bunch of CSS classes and some example markup.
[2430.20 → 2442.96] And you go out, and you build it in whatever language you're going to use, and you just use our classes, and you use our markup structure and you sort of handle everything else.
[2443.26 → 2448.70] And then there's all the way through to we provide all the components to you, basically.
[2448.70 → 2461.10] And I think the interesting thing about the API is a lot of times those components might be PHP markup or some other, like, server-side language.
[2461.66 → 2465.80] Or these days, most likely, it's probably, like, React or Vue components.
[2465.80 → 2480.38] And you want to have an API where engineers can pass in properties that correspond to the, you know, sort of like the CSS classes that you're going to apply.
[2480.80 → 2488.22] You know, so if they pass in, you know, button is huge, then it applies the button huge class.
[2488.36 → 2488.56] Right.
[2488.56 → 2505.34] And I think about the translation from a CSS class to a consistent property that you pass in a JavaScript component is fascinating.
[2506.14 → 2516.44] And then I think there's a lot around, you know, the design system that we use, we sort of provide these structural classes and themes,
[2516.44 → 2519.26] but then we allow folks to heavily modify.
[2519.64 → 2530.18] We have, you know, it's, I think, like, Bootstrap does this, Tailwind does this, where you have, like, margin classes, padding classes, borders, text colours.
[2530.64 → 2539.14] So there's a lot of thinking you have to do about, okay, so if someone is building this button, and they want to pass through additional classes and parameters,
[2539.14 → 2551.16] you know, having your React component set up to allow those properties to just get passed right through into the markup that gets output is really important.
[2551.46 → 2554.20] I think, you know, because there's a balance, right?
[2554.24 → 2562.70] Like, you can't have a property for every single possible thing that people are going to want to do with your components.
[2562.70 → 2574.22] So it's really about thinking, okay, how can I make it so that it's really clear when I pass in this prop, what's the markup going to look like when it comes out the other side?
[2574.22 → 2577.02] Well, there's kind of a deliberate constraints' thing, too, right?
[2577.14 → 2587.10] Like, an engineer might not be thinking about the fact that there are only certain spacings that fit within the design and the design system.
[2587.10 → 2593.26] And so by making that something that you're passing in where there's, like, I don't know, three different margin classes or something like that,
[2593.30 → 2600.20] you don't get engineers who are like, wait, but if I try to measure this with my pixel thing, it's actually 14 pixels instead of 15 pixels.
[2600.22 → 2600.90] Oh, God, no, no, no, no, no.
[2600.90 → 2612.62] That's, I think, honestly, that's just something that I work really hard to try to help engineers feel empowered to push back on designs that don't follow the system.
[2612.94 → 2613.28] Yes.
[2613.28 → 2627.88] Like, I generally tell them, I'm like, you know, if the designer hands you something that doesn't exist in the system, go out and build it with the system as close as you can get it to their design, show it to them, say, is this acceptable?
[2627.88 → 2643.84] And then if they say, no, this isn't quite right, that's when you can have a conversation about the trade-offs of writing custom markup, writing custom CSS, maintaining that in the long term versus using what's available.
[2643.84 → 2656.50] Or then you can have a conversation with your design systems team or whoever owns your design system about, hey, these patterns don't fit what my designers want to do anymore.
[2656.66 → 2663.00] So maybe we need to expose a new class or a new variable or maybe a whole new pattern needs to be developed.
[2663.00 → 2672.70] So I think a lot of times engineers, especially more junior engineers, will get handed a design, and they'll just go, they'll measure it, and they'll go, and they'll build it exactly.
[2673.58 → 2679.12] But if there's a good system in place, you know, you should never.
[2679.42 → 2680.50] You should never have to do that.
[2680.50 → 2681.14] You should never have to do that.
[2681.18 → 2683.36] You should never want to do that.
[2683.46 → 2683.68] Yes.
[2683.82 → 2687.24] That's a great way to unmaintainable CSS and markup.
[2687.26 → 2687.50] Exactly.
[2687.88 → 2688.92] This is how we got.
[2688.92 → 2696.12] But this is, you know, it's exactly that thing, which is why design systems exist in the first place is to solve those problems.
[2696.96 → 2703.52] So this raises another related and interesting question, which is, how do you think about the evolution of a design system?
[2703.52 → 2710.26] Because we'd all love to create the one perfect thing and then always be able to use it.
[2710.82 → 2711.90] And that's not reality.
[2712.12 → 2712.26] No.
[2712.40 → 2715.66] Like reality evolves and changes and our constraints change and things like that.
[2715.66 → 2725.10] So how do you think about sort of managing that process and making the trade-offs of, does this belong as a new thing in the design system?
[2725.10 → 2732.12] Or should we remove this option and do something either custom or build it closely with the system?
[2732.12 → 2732.38] Yeah.
[2732.38 → 2732.42] Yeah.
[2732.42 → 2749.82] I think as far as like the last question, you know, adoption and, you know, you don't, when you think about it, like you don't necessarily want or need to have everything in the design system.
[2749.82 → 2756.72] Like the stuff in the design system should be reusable by any team in any context.
[2756.72 → 2773.84] And maybe like the cool, flashy new thing that the designer on the search team needs is so specific to search that it's not about building something that's reusable.
[2773.84 → 2784.94] But what I generally tell people are build every component that you build custom on the site as if it were already in the design system.
[2785.28 → 2796.62] So that if we get to the point where we put it out there and other teams start using it, we can just copy and paste the markup and the structure and the CSS into the design system.
[2796.62 → 2814.70] And then everything is in alignment, and it makes it much easier because, you know, if you build it just kind of any haphazard way, if you're not thinking about, all right, if this is going to eventually be reusable, then we can't port it very easily.
[2815.72 → 2815.84] Yeah.
[2815.96 → 2822.82] That's a that's a tricky balance though, because as you mentioned, like product engineers, one, they're often under tight deadline constraints.
[2822.82 → 2829.40] And two, they may not even have the perspective of what are all the variables that people might want to change here.
[2829.86 → 2830.12] Totally.
[2830.32 → 2840.82] And I think we, we have a pretty good setup right now where a lot of those conversations are happening more in design crits.
[2840.82 → 2847.98] And the designers who work really heavily on the design system go to other teams crits.
[2848.20 → 2853.74] And there's like a global sort of all of Etsy design does a weekly crit together.
[2853.74 → 2870.88] So I think it's, it's about having those good relationships outside the design system world with, you know, the actual designers and engineers who are going to be using it and making sure that there's a really clear, open line of communication.
[2871.58 → 2871.70] Yeah.
[2871.74 → 2874.96] Just constant talking, communication back and forth.
[2874.96 → 2886.18] Well, and I mean, and it's funny because probably one of the busiest like customer service channels at, in our Slack instance is the design systems channel.
[2886.36 → 2886.88] Oh, interesting.
[2886.98 → 2889.66] People are constantly popping in and asking questions.
[2889.74 → 2890.96] How do I use this component?
[2891.26 → 2892.56] I want to do this thing.
[2892.64 → 2894.22] The designers asked for this.
[2894.74 → 2895.76] How do I make it happen?
[2897.46 → 2897.94] Yeah.
[2898.04 → 2899.28] So it's, it's a lot.
[2899.28 → 2915.74] You definitely have to have a very customer service mindset in order to work effectively on a design system team and relationship building, clear guidelines about contributions, you know.
[2917.02 → 2924.98] At least at Etsy, our design system kind of represents our, what we hope, you know, and we're not perfect.
[2924.98 → 2931.90] Nobody's perfect, but I like to think that it's, it's our highest ideals for what our front end code should look like.
[2932.56 → 2934.40] Everything should be perfectly structured.
[2934.74 → 2936.96] Everything should be perfectly accessible.
[2937.78 → 2939.84] Everything should be consistently named.
[2940.76 → 2954.52] Not that we always achieve that because we're humans, but, but I mean, in my opinion, I think if other people are building stuff in their own stack that follows the kind of lofty ideals and guidelines,
[2954.52 → 2960.16] that we put down for the design system, then they're going to be set up for success regardless.
[2960.50 → 2964.10] You know, it's not, these are good architectural patterns for everyone.
[2964.42 → 2975.10] You don't have to be a design systems engineer to think about how do I separate business logic from interaction logic.
[2975.84 → 2979.00] You know, these, these are important things everywhere.
[2979.56 → 2979.72] So.
[2980.36 → 2980.80] Absolutely.
[2981.64 → 2982.12] Awesome.
[2982.12 → 2992.08] Um, the only last note I have to talk with you is to, uh, highlight what I think you, on Twitter, you said was your career apex success.
[2992.32 → 2994.72] You recently were subtweeted by horse JS.
[2995.54 → 2995.84] Yes, I was.
[2995.94 → 2996.36] Yes.
[2996.66 → 2997.40] That was awesome.
[2997.50 → 2997.72] Yeah.
[2997.82 → 3005.12] I was, I was very, very lucky to be invited to MC, um, Scoff US in California.
[3005.12 → 3005.62] Oh, nice.
[3005.96 → 3006.22] Yeah.
[3006.40 → 3007.24] I missed it this year.
[3007.36 → 3008.18] I was sad to miss it.
[3008.18 → 3008.30] It was fun.
[3008.34 → 3010.16] It was my first Scoff, actually.
[3010.28 → 3011.00] Oh, they're wonderful.
[3011.12 → 3013.36] So I got thrown in the deep end, but, um, it was amazing.
[3013.48 → 3014.38] It was so much fun.
[3014.68 → 3016.36] I really enjoyed Ming.
[3016.46 → 3020.52] If anybody else wants me to MC their conference, I welcome an MC.
[3020.68 → 3022.02] It was a it was a lot of fun.
[3022.02 → 3030.32] Um, yeah, and I tweeted a picture from backstage and horse JS retweeted me like instantly.
[3030.64 → 3034.60] So I have theories now about, I think I know who horse JS is.
[3034.84 → 3043.68] At Scoff two years ago, there was a whole talk about unveiling horse JS, which they didn't because they staged it.
[3043.68 → 3048.04] But it was hilarious to have them doing that and have horsed JS subtweeting them as they're doing it.
[3048.08 → 3056.44] So we're like, we know that he or she was at Scoff doing this, listening to the talk about unveiling horse JS.
[3056.80 → 3057.68] Like it was hilarious.
[3057.68 → 3057.76] Yeah.
[3058.02 → 3065.76] I'm like, I'm like, I've actually, the person who I think is horse JS, I've asked them directly, like, do you horse JS?
[3065.84 → 3069.22] And they always say no, but I don't know if I believe them.
[3069.22 → 3074.70] I've also heard a perfect theory that it's not just one person, it's actually a bunch of people.
[3075.24 → 3079.54] And I think that makes, um, a ton of sense also, but.
[3079.84 → 3087.38] The data they did expose in that talk seemed to indicate that if it is multiple people, they are at least geographically co-located.
[3087.68 → 3088.12] Okay.
[3088.38 → 3088.62] Okay.
[3088.78 → 3089.10] So.
[3089.78 → 3090.26] Yeah.
[3090.38 → 3091.08] But, you know.
[3091.38 → 3091.92] Who knows?
[3092.62 → 3093.94] Horse JS is still out there.
[3093.96 → 3094.80] You can spoof geography.
[3095.10 → 3095.58] Come on.
[3095.58 → 3101.78] So yeah, so that was probably the, the, the highlight of my career.
[3102.66 → 3105.24] And of course it wasn't about anything like interesting.
[3105.40 → 3106.32] I said about JavaScript.
[3106.54 → 3108.74] It was like a picture, but that's okay.
[3108.76 → 3109.32] I'll take it.
[3109.56 → 3109.78] Yeah.
[3110.36 → 3110.86] All right.
[3110.94 → 3111.30] Awesome.
[3111.44 → 3112.52] Anything else you want to talk about?
[3112.68 → 3115.08] No, this has been a really awesome conversation.
[3115.20 → 3116.62] Thank you so much for inviting me, Kevin.
[3116.68 → 3117.70] It's so great to be here.
[3117.94 → 3118.26] Absolutely.
[3118.54 → 3119.52] Thank you for joining me, Katie.
[3119.64 → 3120.00] Thank you.
[3120.08 → 3120.42] Take care.
[3120.54 → 3120.76] All right.
[3120.80 → 3121.06] You too.
[3121.06 → 3123.84] All right.
[3123.92 → 3125.74] Thank you for tuning in to JS Party this week.
[3125.86 → 3128.80] Tune in live on Thursdays at 1 p.m.
[3128.84 → 3129.20] U.S.
[3129.34 → 3131.90] Eastern at changelog.com slash live.
[3132.30 → 3134.90] Join the community and Slack with us in real time during the shows.
[3135.28 → 3136.70] Head to changelog.com slash community.
[3137.32 → 3137.98] And do us a favour.
[3138.12 → 3139.30] Share this show with a friend.
[3139.62 → 3140.80] We're just going to have a podcast.
[3141.00 → 3142.58] Go into Overcast and favourite it.
[3142.98 → 3145.28] And thank you to Vastly, our bandwidth partner.
[3145.64 → 3147.16] Head to fastly.com to learn more.
[3147.56 → 3150.20] And we move fast to fix things around here at Changelog because of Rollbar.
[3150.20 → 3152.12] Check them out at rollbar.com.
[3152.56 → 3156.42] We're hosted on Leno cloud servers at the leno.com slash changelog.
[3156.48 → 3157.86] Check them out and support this show.
[3158.32 → 3160.30] Our music is produced by Break master Cylinder.
[3160.78 → 3163.76] And you can find more shows just like this at changelog.com.
[3163.92 → 3164.86] Thanks for tuning in.
[3165.10 → 3165.88] We'll see you next week.
