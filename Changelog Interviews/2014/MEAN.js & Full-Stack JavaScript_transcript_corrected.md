[0.00 → 14.40] welcome back everyone this is the changelog where members support a blog podcast and weekly
[14.40 → 21.02] email covering what's fresh and what's new in open source check out the blog at the changelog.com
[21.02 → 27.20] our past shows at five by five dot TV slash changelog you're listening to episode 119 and
[27.20 → 34.28] talk to the fellows behind mean JS Amos Aviv and Bowie Cohen mean JS is a full stack JavaScript
[34.28 → 43.10] solution using Congo dB express angle JS and node great show today it's sponsored by code ship
[43.10 → 48.52] Rackspace and Harry's we'll tell you a bit more about Rackspace and Harry's later on the show but
[48.52 → 54.54] our good friends over at code ship also a partner of the changelog they're a hosted continuous
[54.54 → 60.36] deployment service that just works easily set up continuous integration for your application today
[60.36 → 66.26] in just a few steps and automatically deploy when all your tests pass that's the way to do it
[66.26 → 71.66] code ship has great support for lots of languages test frameworks as well as notification services
[71.66 → 77.52] they easily integrate with GitHub Bitbucket and can deploy to cloud services like Heroku
[77.52 → 85.02] AWS notice google app engine or even your own servers get started today with their free plan
[85.02 → 93.94] setup takes only three minutes no excuses to have untested code in production head to codeship.io and
[93.94 → 101.48] also check out their blog which I love by the way blog.codeship.io one more thing to mention for our
[101.48 → 109.86] members um you can save between 294 and 2994 on your first year with code ship so make sure you take
[109.86 → 115.18] advantage of that the changelog.com benefits if you're not a member what are you waiting for
[115.18 → 120.82] membership is just 20 bucks a year, and you support us to support open source once again
[120.82 → 129.68] codeship.io sign up three minutes that's all it takes do it today and now on to the show
[129.68 → 139.76] we're joined today by Amos Aviv and Roe Schwaben Cohen talking about Mean.js it's a product oriented
[139.76 → 145.30] full stack JavaScript boilerplate so why don't one of you guys give us an uh well first why don't
[145.30 → 153.28] you guys introduce yourself I guess Amos you can go first um, so my name is Amos Aviv and I'm a developer
[153.28 → 164.68] a web developer for about uh 12 years now um I've been through the days of i5 and quicks mod uh through
[164.68 → 174.80] uh the birth of the uh new generation um browsers and finally to where we are today uh in this exciting
[174.80 → 182.40] new world of JavaScript uh in the server and stuff like that um I do a lot of um
[182.40 → 192.48] side projects I guess um because uh you have to do something for your soul um
[192.48 → 200.10] and one of the latest side projects I had was Mean.io um which evolved to be Mean.js
[200.10 → 207.56] um yeah, so there 's's a little bit of drama around that which we'll kind of touch on a little
[207.56 → 212.34] bit um later in the show but we know we'll kind of avoid that as much as possible just to kind
[212.34 → 217.34] of shine a light on the good of Mean.js um so that's cool so you've been around you've been doing
[217.34 → 223.68] this for a while yeah uh Roe yeah Roe why don't you so I've been a developer in Israel um for the past
[223.68 → 231.44] uh nine years I would say um yeah I come from a more of a PHP background but recently also found
[231.44 → 238.76] the light and node um very interested in like all of what this framework has to offer um and then
[238.76 → 244.60] angular is again one of the newer tools that I've started using in the past uh maybe a year or two
[244.60 → 253.52] um and I'm currently working for a company called leafy here in Seattle um yeah that's about it
[253.52 → 259.36] awesome so why don't you guys give us an uh introduction to what Mean.js is um in its current
[259.36 → 270.34] in its current form okay so um Mean.js is a full stack JavaScript boilerplate um it was born out of
[270.34 → 279.02] uh our attempt at um a better flow for this kind of stack, so the term was coined um in the MongoDB
[279.02 → 287.32] blog actually um, and we basically found out that it was super um efficient um almost basically wrote
[287.32 → 294.74] the stack um I think it was uh six or seven months ago no, no it was am I making a mistake yeah it's
[294.74 → 304.62] about uh a year ago um the blog post was uh written by a developer called Valery charpoy he uh on the
[304.62 → 313.02] MongoDB blog um I used to do uh I'm a freelance developer so i I'm involved in several projects
[313.02 → 320.82] and I recognized a certain pattern in projects where developers used MongoDB as the database
[320.82 → 330.62] uh node as the web server and uh angular JS as the client web framework um and decided uh
[330.62 → 337.38] uh those projects could look better be better organized if uh they put in some sort of order
[337.38 → 346.48] so I created uh a Mean stack uh which I used uh, uh for about uh two months before we released it as
[346.48 → 355.22] an open source um i i I thought the name Mean was cool and when I looked it up I found out uh
[355.22 → 364.98] several people are already using it uh so I just released it um as Mean um to address the namespace
[364.98 → 378.02] I guess um it can it is basically um was constructed to offer uh MVC whatever um structure to both the
[378.02 → 386.82] server side and the server side um in a way that um represents your entities properly um
[386.82 → 396.66] I think what i I tried to do uh was help developers from coming from strict type languages
[396.66 → 407.76] with background in a java um uh sp.net uh and stuff like that um step into the world of node.js
[407.76 → 416.42] web applications and feel a little more comfortable um and so the point of Mean uh just sorry to interrupt
[416.42 → 421.70] the point of Mean so it's its it's opinionated right it's Congo express angular node and this is
[421.70 → 428.02] something that you guys basically noticed was like a really common trend amongst uh for a node stack
[428.02 → 434.56] right which was this thing called Mean uh what is it about Mean.js now I've used all of these things
[434.56 → 441.00] and all of them are relatively easy to uh get started with on their own what is it about Mean.js that
[441.00 → 445.34] kind of makes it easier to get started with the whole stack rather than trying to do each one individually
[445.34 → 452.08] so I think uh the most important uh stuff we wanted to address the most important issue we wanted to
[452.08 → 459.42] address was um the interface between the different parts um you have your angular JS application uh
[459.42 → 466.58] running, and you want to communicate with your node server so your node server um it should present
[466.58 → 477.64] some sort of rest API for angular JS to use um, and we wanted that um uh interface point uh to be
[477.64 → 488.24] properly organized so when you download the stack you get um a folder structure uh and a couple of config
[488.24 → 494.56] files that help you configure the different parts of the application like um the connection point between
[494.56 → 503.62] node and uh MongoDB uh where we use the Mongoose module or uh a user authentication layer uh which uses the
[503.62 → 511.62] the popular passport module, and we wanted to give this all out of the box uh to feel to let uh developers just
[511.62 → 520.96] uh begin writing their code uh instead of uh I don't know trying to figure out how to um build their project
[520.96 → 531.46] um and just concentrate on building uh what they want instead of um the infrastructure which I used to see
[531.46 → 538.70] uh which I used to see developers uh taking a lot of time uh dealing with the infrastructure and the way
[538.70 → 545.98] the proper way to uh connect those parts uh so right means we have a very I think we have a very
[545.98 → 552.40] important um concept that we're trying to relay um with mean which is first we chose um
[552.40 → 562.18] only if not um like mostly if not only popular um components so um we intentionally chose to go with
[562.18 → 568.24] Congo instead of couch we intentionally chose to go with express instead of some other um, um framework
[568.24 → 575.06] uh that does rout we chose to reduce uh our jade imprint eventually because all of these things
[575.06 → 580.82] were been been coming from the community so we're trying to pick um again components that are really
[580.82 → 586.60] popular from the one hand and from the other we really wanted to not abstract away the simplicity of
[586.60 → 591.98] of all these frameworks so we don't want to create some sort of like a layer that takes all this
[591.98 → 596.62] complexity away from you as a developer we wanted it we wanted you to still be hands-on and really
[596.62 → 603.36] understand how the parts work but um that doesn't necessitate um you're learning each of the components
[603.36 → 609.02] and like really knowing how to integrate them properly um, and we found that it was really easy
[609.02 → 615.30] to start um creating vertical stacks uh which means like all the stacks in the server all the
[615.30 → 622.26] parts of the server and the client for a given entity um it made that whole process a lot easier and a lot
[622.26 → 628.92] faster right, so this is different from a lot of our listeners are subsists and this is different from
[628.92 → 634.46] rails and that rails is its own thing right it builds all the layers into its own thing and
[634.46 → 638.60] this would be similar if you guys were to say build your own express that had its own emulating and
[638.60 → 644.00] its own database and its own you know all that mean it takes the other tools so you still have
[644.00 → 649.54] complete control over the tools individually, and it allows you to, but it makes it easier to kind of
[649.54 → 654.68] connect it all together yeah I think one of the more uh prominent patterns we saw with uh
[654.68 → 661.74] with mean is the amount of forks um that were kind of unusual to yeah about um 1000 forks already
[661.74 → 667.38] yeah so like yeah the total is about 1000 forks and the reason for that is people
[667.38 → 672.12] like different flavours of mean, and they like different flavours of full stack JavaScript really
[672.12 → 677.74] um so if we look at this entire picture we're we're of the mind that um all these flavours are
[677.74 → 683.94] totally valid, and we're not necessarily opinionated um in a way that says like our flavour is better
[683.94 → 688.82] than any other flavour it's just that we found these tools to be super popular and super helpful
[688.82 → 694.54] and powerful, and we thought that they were our best choice for the scenarios where we were
[694.54 → 701.04] at the time so I was um, um developing for a startup called go mango and I had to rewrite my website
[701.04 → 706.14] really quickly, and it was sort of built with a lot of fragmented pieces of jQuery and angular
[706.14 → 712.08] and node in the back and some PHP and some botnet and all these systems were working together
[712.08 → 717.78] but not very well um and my first experience with mean.io was when I basically converted my website
[717.78 → 722.94] that was built before that um it took about eight months to build and I converted it in about two
[722.94 → 732.30] weeks so I feel I really felt a very significant and real um uh change in the speed uh of my
[732.30 → 737.78] development and I think it really has a lot to do with a fact that we're doing only
[737.78 → 743.94] JavaScript um and not like switching between languages which is immensely helpful, and it's
[743.94 → 750.94] sort of easier to keep on thinking sort of the same way um with thinking and i and i specifically
[750.94 → 756.96] mean about thinking modularity and thinking about you know um asynchronous um uh workflow instead
[756.96 → 761.70] of a synchronous workflow all of that together creates this effect of everything is so much easier
[761.70 → 768.22] and faster gotcha so the idea that you're using like Congo instead of couch or react and express
[768.22 → 773.74] instead of happy or Getty, or you know different things uh that's that's your choice but
[773.74 → 778.78] but what happens when like somebody forks this, and it's been right with all the same stack except
[778.78 → 783.24] react instead of Congo and that one kind of takes off as the popular fork like that's that's a real
[783.24 → 789.44] problem that this open source project faces um and so what happens there we're actually not yeah we're
[789.44 → 794.62] not seeing it as a problem yeah we're not this is a great yeah how else you can go so we're not
[794.62 → 801.52] viewing it as an uh we're not viewing it as a problem um we actually find this as a great opportunity
[801.52 → 811.00] uh we I personally hate uh um religious technical discussions like the editor wars of the 80s
[811.00 → 819.26] um i I find it extremely unproductive I believe everyone should choose their
[819.26 → 830.24] tools I'm really pro um, um a variety of tools so what we faced this early on uh ROI actually
[830.24 → 838.44] helped one of our uh more passionate developers um yeah martin Jenna he's like an awesome dude
[838.44 → 846.76] yeah he's like an awesome dude who runs the 100 Jas blog uh, and he wanted to make a mean fork
[846.76 → 857.66] using amber and ROI helped him to do so uh and uh when we saw this coming uh we and ROI uh started
[857.66 → 865.76] creating uh different forks of mean we created a Jane fork which used a juggling dB as an obfuscation
[865.76 → 874.76] layer for different databases um I played with the idea of um breaking the angular part and um
[874.76 → 883.88] um letting users re uh use the web framework frameworks they want like amber uh backbone knockout
[883.88 → 889.80] whatever you like um and I helped the company implement their own web framework inside mean
[889.80 → 897.44] so um we find this is actually one of the things we find uh inspiring because we don't see mean
[897.44 → 905.26] as uh as the goal we see it as a starting point for something much bigger um JavaScript full stack is
[905.26 → 912.78] a vision not yet uh fulfilled yeah it's very new yeah it's very new uh we experienced uh firsthand
[912.78 → 922.62] the chances in this field um as ROI mentioned um the quick uh the gain in performance
[922.62 → 927.78] developers uh developers get when they use a JavaScript um a full stack JavaScript boilerplate
[927.78 → 936.00] uh is impressive um, and we want to push towards that location we're even considering starting a project
[936.00 → 943.86] called BSFS we will talk about it sometimes sometime later but uh BSFS will contain the different flavours
[943.86 → 952.74] of um full stack JavaScript it's um it's uh in the far future I don't know how far but um
[952.74 → 957.54] it's still in its infancy yeah yeah yeah but but but that's okay that's um
[957.54 → 964.44] we find this as an opportunity not a problem we see we would like to see developers implement
[964.44 → 972.26] their own flavour of whatever they like stack um call it whatever I think we're trying to also like
[972.26 → 978.60] sort of take the discussion about JavaScript to like a newer place which talks about not only the
[978.60 → 983.84] components that you use but rather the patterns that we see emerging from these tools so like
[983.84 → 989.62] full like the full stack thing comes naturally because it's all JavaScript and all in one language
[989.62 → 998.80] so it's much easier to describe it that way um but i sort of feel that um with this
[998.80 → 1004.50] framework uh in mind we can start talking about more complex ideas and then start thinking
[1004.50 → 1009.58] about how are we collaborating across this ecosystem because like one of the problems we were facing and
[1009.58 → 1014.10] that's something that you start facing when you're doing full stack JavaScript is how do you do um
[1014.10 → 1019.34] package management for the front end for the back end and these are like larger issues that are
[1019.34 → 1026.14] relevant to the entire um sort of full stack uh JavaScript community right or ecosystem and not just to
[1026.14 → 1030.78] mean we're going to pause the show real quick and give a shout-out to our sponsors Rackspace
[1030.78 → 1036.90] they love open source they dedicate themselves to supporting open source and the developer community
[1036.90 → 1041.40] and they're doing that with the changelog they're supporting us they can support open source
[1041.40 → 1047.12] because we support open source um, and now you can make something awesome on them, they want you
[1047.12 → 1052.02] to come and sign up for this and get money basically to use their services it's pretty cool
[1052.02 → 1057.62] so if you're a maker each and every day you're thinking it's the new amazing awesome and you
[1057.62 → 1063.26] you want to put it out there Rackspace would like to give you something special just to say thank you
[1063.26 → 1068.90] sign up today for their developer discount and get three hundred dollars in free cloud services
[1068.90 → 1075.50] on your Rackspace cloud account this discount applies to new products like their performance cloud
[1075.50 → 1081.66] servers and cloud queues you're even eligible for early access that's right early access
[1081.66 → 1087.50] to new features and new products that they roll out so go ahead and sign up for this today make
[1087.50 → 1096.36] something awesome and get started today developer.rackspace.com slash dev trial so just out of curiosity
[1096.36 → 1103.40] FAMAS as somebody who is around in the editor wars um which editor is the right one to use with mean
[1103.40 → 1116.76] developers um developers prefer different kind of editors according to uh the way they used to um
[1116.76 → 1126.80] um program I think when you maintain um a large code base you would prefer using an IDE or um a tool that
[1126.80 → 1133.32] allows like a tool that allows you to dig deeper and and and assist you with understanding the
[1133.32 → 1140.54] complexity of your code and when you write a lot of code like we do uh i I prefer my editors as lean
[1140.54 → 1150.04] as possible uh I currently use sublime um sub the guy writing sublime is awesome um I'm addicted
[1150.04 → 1156.24] to multiple characters um so that's that was a joke question you're not supposed to really have
[1156.24 → 1162.88] an answer for that that's not fair any no you stepped into a field i I am I'm talking so much about
[1162.88 → 1169.04] we're both kind of like editor fanatics, and we're like totally interested in any new editor that comes
[1169.04 → 1174.20] around because part of us does feel that there is some sort of gap between what we need as developers
[1174.20 → 1178.98] when we're trying to like to maintain a full stack application it's sort of getting difficult because
[1178.98 → 1183.38] you're you're juggling a lot of balls and it sort of feels like sometimes you're encumbered by your
[1183.38 → 1187.84] editor um and yeah that's also another conversation we sort of want to have with people
[1187.84 → 1194.20] gotcha so actually uh to kind of ask this question uh I think it was roughly did you say you came from
[1194.20 → 1201.08] like PHP land yeah mostly yeah so one of the things to get started I mean specifically in like node land
[1201.08 → 1206.28] and with you know full stack JavaScript is the ability to learn and the ability to learn like the
[1206.28 → 1211.70] new environment and all that um what was it like for you and what is it how does mean kind of
[1211.70 → 1218.22] help people when they're getting started in node land so my experience was that um everything
[1218.22 → 1226.04] requires a lot of experimentation um and well once you get the gist of uh you know how JavaScript works
[1226.04 → 1232.26] in its core um once you start understanding that not everything is synchronous um everything sort of
[1232.26 → 1237.38] starts making more sense so I had a rough time starting out um and I didn't have a lot of
[1237.38 → 1241.66] documentation on node because I started playing with it when it was like still not really around
[1241.66 → 1249.18] um as a production uh framework at least um and what we're trying to do again is like sort of uh
[1249.18 → 1255.40] with mean is sort of start with uh frameworks that are already well known um already uh have a community
[1255.40 → 1262.66] and some sort of uh a well a good documentation um with them and we really tried with mean JS to
[1262.66 → 1267.58] expand our own documentation and sort of make it easy for you as a developer to start um fiddling with
[1267.58 → 1272.74] JavaScript because with mean because again if you're a JavaScript developer um and even if you're not a
[1272.74 → 1279.28] JavaScript developer it's not very complicated um whatever is happening on the service side is
[1279.28 → 1284.90] really quite simple it's a model and some routes and the stuff that's go and that's obviously
[1284.90 → 1292.48] like uh really simplifying the picture but in terms of what you need to uh know it's its it's very
[1292.48 → 1299.14] very limited um and and and the whole and the fact that we chose these popular stacks kind of uh
[1299.14 → 1304.20] created this weird effect that like our community support is sort of built-in, and we don't
[1304.20 → 1310.90] really need to invest in uh supporting each of the components on its own but rather we can only um
[1310.90 → 1316.36] sort of interact with issues that are pertaining to the stack itself and the way you connect these
[1316.36 → 1322.60] parts together so that sort of makes it easier to sort of document and solve issues and so on
[1322.60 → 1327.98] and so forth yeah unique part of your documentation with mean JS is like if you read through it the
[1327.98 → 1333.42] first you know I don't know 10 lines of the documentation are like go read Congo's documentation
[1333.42 → 1337.74] here's a manual to use go read expresses and documentation here's a guide to use go look at
[1337.74 → 1343.72] angular JS here's a guide and then like once you get past all that um right it's really just like
[1343.72 → 1349.50] you can read the whole documentation in one sitting and so uh you'll obviously want to yeah you'll want
[1349.50 → 1354.62] to come back to it and reference things, but it's neat because you guys do benefit this is an odd type
[1354.62 → 1361.06] of a project because as much as you are depending on other uh pieces of open source you're also
[1361.06 → 1367.88] benefiting from the other pieces of open source so one of the so the upside is you know as that piece
[1367.88 → 1373.26] as Congo progresses you guys progress with it as express progresses you guys you know progress with it
[1373.26 → 1380.10] what happens when something ships to Congo's you know like latest release and it, and it causes a
[1380.10 → 1386.66] conflict in your in mean JS like how does this work so actually this just happened because um express is
[1386.66 → 1396.94] about to release they're the fourth version um you kind of need to stay uh alert to those changes
[1396.94 → 1402.74] this is our mission like our mission is to support the different changes in the different
[1402.74 → 1412.74] packages we try to make those packages um as lean as possible um, um we try to use uh packages that are
[1412.74 → 1421.94] widely supported and not just like um a niche packages that might be uh deserted in a few um uh months or so
[1421.94 → 1429.78] uh so we have to keep up with those changes and offer uh an update to the uh to the stack itself um
[1429.78 → 1439.96] um updates are in general uh a huge issue when you offer a stack that is built from uh, uh different
[1439.96 → 1448.32] components, and you don't you don't wrap it like in a sealed uh module so any update you do
[1448.32 → 1453.66] uh must be supported by the community and that's what we try to do with mean JS we try to give it
[1453.66 → 1459.52] a more modular approach so we can update it without uh affecting or breaking your project
[1459.52 → 1467.90] um that's one of the biggest um issues we have we we we're yeah i think we're not we're not
[1467.90 → 1475.04] even trying to really solve these bigger issues um I think with projects like uh BSFS and that may
[1475.04 → 1481.10] may or may not happen uh we might again create enough discussion about the issues that that that
[1481.10 → 1487.10] pertain to all of us I mean yeah not just the mean stack but the been stack and the gene stack and
[1487.10 → 1493.04] the amen stack or whatever stack it is we're all going to have a problem with maintaining uh backward
[1493.04 → 1499.74] like our dependencies and maintaining our uh, uh backward compatibility um when we ship things that
[1499.74 → 1505.46] are super dependent on other packages and I don't think we're alone in this and again right now it's
[1505.46 → 1512.04] our mission to keep and keep maintaining a live very healthy stack um, but we see that this issue is
[1512.04 → 1517.10] going to happen for everyone so we sort of want to create a discussion about this as well so do you
[1517.10 → 1522.16] guys follow like beta or alpha releases of the other of the pieces of mean and and and like integrate
[1522.16 → 1532.46] you know kind of proactively um yeah we try to react to uh different changes when they do happen
[1532.46 → 1540.92] uh we try to predict what would happen to the stack um when the final uh release will be um but
[1540.92 → 1551.14] what we use is um luckily we have uh each dependency in the project is installed by using a package manager
[1551.14 → 1562.46] um right the amazing NPM and bower um tools help us maintain the project um uh solid while we test
[1562.46 → 1569.04] the different uh changes that come from the community so before we release a new uh we before we
[1569.04 → 1577.08] upgrade the versions of our dependencies we can test it without breaking the master branch of our uh project
[1577.08 → 1585.36] right so it is though unique because people are not basically building uh very
[1585.36 → 1589.84] simple applications on this and like the amount of complex this is basically a web framework uh really
[1589.84 → 1595.96] and it's not it's going to be hard to really predict um 100 of you know breaking changes, but we're
[1595.96 → 1602.92] we are doing our best yeah for sure so you guys have a few other uh requirements which are not like
[1602.92 → 1608.54] specifically mean you mentioned uh bower so you have NPM well that's node basically bower grunt
[1608.54 → 1613.98] uh a few other ones, so these were the same kind of thing went into picking these over like grunt over
[1613.98 → 1619.90] um gulp there's another one that gulp yeah just because they're like they're popular, and they're
[1619.90 → 1625.58] they're well-supported and this is that nature like why you chose these yeah basically and I think
[1625.58 → 1631.66] i I think that again there might someone might want to use uh gulp and that's super cool and if that
[1631.66 → 1638.10] works for them that's just another flavour of uh another full stack uh JavaScript uh boilerplate
[1638.10 → 1643.16] and I think it's super awesome, and it's just that we again just for that for those reasons alone
[1643.16 → 1648.26] right just like maintain backwards compatibility and to not break with every new release we're trying to
[1648.26 → 1657.24] pick the more uh supported and more uh well-founded uh um packages, and we will, we'll, we'll visit this
[1657.24 → 1663.98] uh in a couple of I don't know weeks or so when we'll uh gulp is an amazing tool that the
[1663.98 → 1672.12] the ecosystem is growing uh really fast but when it comes a time to choose between those two
[1672.12 → 1681.22] um I think we'll revisit this um discussion again um so we need to um again react to what the
[1681.22 → 1688.62] community where the community is leaning to toward yeah once you talk a little bit about BSFS you
[1688.62 → 1693.62] mentioned it and what is it and when can we uh when will we start hearing about it
[1693.62 → 1703.86] um so BSFS is like a grander idea our dream you can tell it you can, we can tell it this way it's our
[1703.86 → 1710.14] dream it is our dream and it sort of like tries to talk about again larger problems and issues that
[1710.14 → 1714.92] you see when you're starting to deal with full stack JavaScript and some of them is our it some
[1714.92 → 1719.80] some of those issues are uh like we talked about um you know what flavour to choose for what scenario
[1719.80 → 1725.12] and we sort of want to make it a level playing field and sort of uh give a face to all these
[1725.12 → 1730.14] flavours but just like maybe uh make sure that the most prominent ones uh are shown to everybody
[1730.14 → 1735.38] everybody the ones that use the most popular components should be on top we think um but on
[1735.38 → 1740.10] on on a larger scale we sort of want to talk about again the process of managing
[1740.10 → 1748.32] uh your file system and how you deal with uh deployment and how you deal with uh you know
[1748.32 → 1756.54] development cycles, and you know how do you integrate a product lifeline to your BSFS uh sort of workflow
[1756.54 → 1762.58] and we sort of want to address the larger issues that come with uh BSFS and not and not necessarily
[1762.58 → 1770.08] focus on one stack or the other um, and we hope to uh see something very soon I don't I don't think
[1770.08 → 1776.62] we have a set launch date for this yeah but uh yeah cool so you mentioned that I just wanted to
[1776.62 → 1782.10] make sure we hit on that a little bit uh going back to mean uh you have the concept of modules in
[1782.10 → 1787.68] mean and I noticed the only module that you have is mean SEO um where modules an original part
[1787.68 → 1794.08] of mean JS or is that a relatively new addition um it's um it's something we planned yeah it's
[1794.08 → 1802.56] something we planned um a few months back uh we had a little struggle uh relaunching mean as mean JS so
[1802.56 → 1809.58] uh we wanted to concentrate on writing uh proper documentation, but it's, but it's one of our main
[1809.58 → 1818.62] goals to um wrap mean with supplemental modules like the mean SEO module um it's not it's not the only
[1818.62 → 1824.52] model we want to build uh there are other models we plan on building um in the next couple of weeks
[1824.52 → 1834.34] we uh we're working on other tools but modules are definitely um one of the best ways to uh support
[1834.34 → 1843.58] a stack without uh breaking it like without um right making it um vulnerable too heavy yeah yeah
[1843.58 → 1849.24] so what constitutes like a module what would what can we expect to see in modules for mean
[1849.24 → 1856.36] um so we're looking at anything that's uh again cross sort of like cross stack and not necessarily
[1856.36 → 1864.32] for mean per se so uh the mean SEO module is uh doesn't necessarily have to work on uh mean itself
[1864.32 → 1871.34] it could work on other uh spas um this is a problem that again is very common to all of all
[1871.34 → 1877.42] all JavaScript seas um with crawlers and that sort of like solves it with node in the back end
[1877.42 → 1886.04] um we're looking at again uh looking at um at ways to improve uh loading uh your scripts onto the
[1886.04 → 1892.16] page um compressing them uh making sure that all that process is taken care of again behind the scenes
[1892.16 → 1896.40] and these are things that you don't necessarily have to care about if you just want to build a web
[1896.40 → 1901.22] application, but it would be better for you to have those things just to make sure your app
[1901.22 → 1908.02] is working properly um so we're looking into that we're looking into um some uh maybe we're not
[1908.02 → 1913.92] even uh completely sure that we'll go into a more commercial sort of side of it where we would try to
[1913.92 → 1920.96] maybe build a store or anything of that nature but right now we're we're really focusing on uh features
[1920.96 → 1928.66] that would make your stack uh work properly um and if we could um not necessarily build something
[1928.66 → 1934.32] that's super opinionated towards mean specifically but rather solve a larger problem for full stack
[1934.32 → 1940.52] applications right that'd be great gotcha, so somebody could take like ideally so mean SEO is
[1940.52 → 1945.58] an express middleware so anyone using express for a SBA could essentially pull that in is that right
[1945.58 → 1953.46] exactly we're going to pause the show real quick and give a shout-out to our sponsor Harry's uh this is a
[1953.46 → 1960.14] unique sponsor for the changelog we don't often get non-tech related sponsors but Harry's loves the
[1960.14 → 1966.24] changelog oddly enough they love open source too so it's kind of neat that uh they wanted to sponsor the
[1966.24 → 1971.98] changelog, but we welcome it it's its it's different so uh here you go Harry's was sparked
[1971.98 → 1978.60] by a personal experience of Andy and Andy is one of their co-founders and his experience that he had
[1978.60 → 1986.32] was is emblematic of the experience myself included but many of us guys have when we buy shaving
[1986.32 → 1993.58] supplies um this is any story tell me this somewhat resonates with your experience when you buy shaving
[1993.58 → 1999.90] supplies uh and this is in his words as first person I went to the drugstore I waited 10 minutes
[1999.90 → 2005.48] for someone to unlock the case where the razors were being held and I bought a four pack of blades and
[2005.48 → 2010.64] buying and I bought some shaving cream it wasn't the best purchase experience to say the least and i
[2010.64 → 2018.74] walked out and looked into my bag and I had a receipt for over 25 bucks worth of products and brands
[2018.74 → 2025.58] that really didn't speak to me as a customer I just felt like there had to be a better way and
[2025.58 → 2032.26] Harry's is focused on providing guys a great shaving experience for a fraction of the price
[2032.26 → 2037.94] of normal competitors you know I have to say myself I've been using the Gillette Mach 3 for
[2037.94 → 2046.36] I don't know since I was 17 I guess I mean forever and I'm using Harry's now Harry's is awesome it's a
[2046.36 → 2052.86] clean product design it looks phenomenal my wife uh would have bought it for me had she known about it
[2052.86 → 2059.82] prior to me finding out about it but um it's great it's um it's high quality the blades are engineered in
[2059.82 → 2066.20] their own factory uh in Germany for sharpness and strength uh blazer half the price of competitors
[2066.20 → 2073.36] like Gillette my current and uh previous brand I'm still kind of weaning off there but i love
[2073.36 → 2079.00] my harry's shaving kit it's awesome um, and it's shipped right to your door the look and feel the
[2079.00 → 2085.78] product is something you would be happy with the quality of the shave the price go to Harry's.com
[2085.78 → 2096.00] and use the promo code changelog to save five bucks on your first purchase Harry's.com h-a-r-r-y-s.com
[2096.00 → 2103.10] so looking through your changelog uh I think the biggest again going kind of not to hammer on the
[2103.10 → 2107.72] same point but like uh switching things out in an application like this is interesting to me, I think
[2107.72 → 2115.46] the biggest change I see was when you replace jade with swig and um uh you kind of hit on that a
[2115.46 → 2121.16] little bit why did you do that and like what kind of conversations did you all have to
[2121.16 → 2130.84] like decide to pull the trigger on that okay so um emulating engine um is a really um nice discussion
[2130.84 → 2140.08] we had with the community um the community of mean uh does have different preferences
[2140.08 → 2148.92] for different um they do prefer a certain um template engine we started with jade because it was most the
[2148.92 → 2157.00] most popular template engine um we moved this week because it was it's it is faster and uses HTML syntax
[2157.00 → 2165.52] um again the um to help develop developers um lower their learning curve of getting into min
[2165.52 → 2176.48] um we're actually working on a generator which is one of the most uh um, um revisited issue request like
[2176.48 → 2182.82] uh people are asking for a proper generator and that generator will support different um render
[2182.82 → 2189.58] engines especially when you consider that most of the views you use in a min application are
[2189.58 → 2198.58] basically uh angular views and not uh a back-end views uh that which uses uh template engines like jade
[2198.58 → 2208.00] era um hogan or any other template engine um but what we get a lot of opinions about it, we discuss
[2208.00 → 2215.00] about it a lot um we move to swig again because if it is faster uh, but we plan to support different uh
[2215.00 → 2220.74] view engines it's kind of interesting that you mention it because like um that was like one of
[2220.74 → 2225.52] the reasons we were talking about BSFS to begin with is because we saw that people were like
[2225.52 → 2231.66] feverishly um just changing the the the template engine yeah really a sore subject and people
[2231.66 → 2236.40] were like really up in arms about it and we sort of figured that like maybe a better way to go about
[2236.40 → 2242.58] it would be to not necessarily decide but rather supply a generator that could uh just open a new stack
[2242.58 → 2250.08] um with whatever emulating engine you want because anyway in mean we really don't uh don't use a lot
[2250.08 → 2256.36] of uh server site emulating like almost said so if we weren't really uh very, very opinionated but we
[2256.36 → 2263.18] did have our opinion and again the generator should maybe uh help with solve this problem yeah gotcha
[2263.18 → 2268.36] so you talk about the generator uh one of the questions how does somebody get started with mean what how
[2268.36 → 2272.56] would you recommend to somebody comes up to you and says I'm interested in you know
[2272.56 → 2280.18] building a spa how do I get started with mean um I think the first thing would be to uh look at
[2280.18 → 2284.96] look at the website um go to the website start reading the documentation it would be really easy
[2284.96 → 2291.12] to just download it um uh NPM install which would install all your dependencies, and you can run the
[2291.12 → 2297.24] server and sort of look around the code and I think for me personally I really learned well
[2297.24 → 2303.82] example um we included a full stack example of an article um so you can see all sorts of things that
[2303.82 → 2310.72] you could do from like the point where you define your model um through the routes and then the angular
[2310.72 → 2315.58] service and the views etc, and you can just like follow through the stack and sort of look at how
[2315.58 → 2322.62] it's implemented and then just play around with it maybe implement your own uh stack um it would be
[2322.62 → 2327.58] really easy to do when we have the generator out because all you would have to really do is pick a
[2327.58 → 2332.62] name and then set the structure, and then it would basically be reflected to you from the server in
[2332.62 → 2339.32] your in your angular side with a server service very easily so if is you do have you I think you
[2339.32 → 2344.90] to start using mean you do need some sort of background a bit in node like a very basic
[2344.90 → 2350.16] understanding of what it is and how NPM works maybe um, and you do need some sort of knowledge
[2350.16 → 2356.24] um uh and maybe even experience with angular um I wouldn't necessarily recommend this to someone
[2356.24 → 2362.14] who doesn't know any of these um at this point but uh if you do have that kind of uh knowledge and
[2362.14 → 2367.76] then for sure I think if you just download it and walk through the stack and all of its parts
[2367.76 → 2373.22] it's pretty self-explanatory and if that's not enough then, then almost has really worked and
[2373.22 → 2378.80] uh really hard on uh the documentation on the website and lastly and maybe most importantly
[2378.80 → 2384.96] we are here to answer anyone's questions, and we will do our our our best to really um reply to
[2384.96 → 2390.56] issues, and we really encourage everyone to ask and talk to us because we just love it and yeah I think
[2390.56 → 2394.98] one of the best things that happened to on a personal level to me and I think to almost as well was
[2394.98 → 2400.30] seeing the amazing reaction from the community and that's something that this is my first uh open
[2400.30 → 2405.54] source project um that I'm really committed to and I feel that the community support engagement
[2405.54 → 2410.82] has really made a difference and really made it worth my while um to actually do it, and it's super
[2410.82 → 2416.68] fun and people are awesome really the best part of my day is discussing with developers what they build
[2416.68 → 2425.54] well about the projects they do it's like answering those emails is like so it makes you feel like what
[2425.54 → 2430.72] you do matters you see people creating their dream project and they ask you for such a simple
[2430.72 → 2439.90] question such simple questions and you can really help them get through like right um so we are
[2439.90 → 2448.78] pretty communicative about um supporting uh the community um, and we do, and we'll, we'll make the
[2448.78 → 2455.76] documentation better I promise you that accepting forks yeah, yeah accepting forks we're totally
[2455.76 → 2461.98] accepting forks yeah and yeah and if you want to talk to us about uh your own uh JavaScript full stack
[2461.98 → 2469.38] flavour uh we totally encourage you to do that, and we are totally non-denominational so whatever
[2469.38 → 2474.62] kind of flavour you want to bring on to the table um I think we are going to limit um the scope to just
[2474.62 → 2479.60] JavaScript and not other languages at this point because otherwise it'll just be a big mess yeah um
[2479.60 → 2485.30] but yeah if you do have a stack we would love to hear from you so one of the things almost that you
[2485.30 → 2489.08] mentioned was you know it's like your favourite part of the day is answering emails about what people
[2489.08 → 2494.12] are building um anything that we know of like that you could tell me that people are using
[2494.12 → 2501.60] means in production to get started with um I don't know if I can disclose this information
[2501.60 → 2508.24] because no they trust me they show me their projects they show me their code i I don't know
[2508.24 → 2517.94] if they is I would like to um disclose their projects um I've seen people create uh simple applications
[2517.94 → 2526.36] um uh and an Makaton application or something like that uh and i I've seen people um restructure
[2526.36 → 2536.02] uh their companies 20 years old um stack uh in min um I'm actually helping a couple of
[2536.02 → 2544.66] companies doing so um um um but uh what we are about to open a built with section in our site and we
[2544.66 → 2551.06] will and we'll invite people to share what they're doing um but I've seen it so we'll look
[2551.06 → 2555.10] out for that yeah yeah look out for that I don't want to get you in any trouble here
[2555.10 → 2563.86] yeah yeah better not yeah awesome so uh for our guests that are just listening or for new listeners
[2563.86 → 2568.64] to the show we ask our guests the same questions uh at the end of every show so we'll go ahead and
[2568.64 → 2574.94] ask you them now the first one um I'll ask you uh roe first is for a call to action for the community
[2574.94 → 2584.14] um a call action a call to arms would maybe be um just build your stacks uh and just
[2584.14 → 2590.62] be involved in the discussion really um let your voice be heard um we really want to hear from you
[2590.62 → 2595.16] and we really want to hear uh what you think about our stack and if you have different ideas about how
[2595.16 → 2601.64] it should work or different stack we'd totally love to hear about it what about you AMS um let us
[2601.64 → 2607.30] know what we're doing wrong I think I guess um and how would somebody do this through GitHub issues
[2607.30 → 2613.18] yeah use the GitHub issues on Twitter we have a community section in our website you can use Twitter
[2613.18 → 2621.16] Facebook you can uh personally uh um drop me an email or something like that you can use the Google group
[2621.16 → 2629.34] um we're we're making ourselves available in in in an IRC channel um but I think the best way to do it
[2629.34 → 2635.62] is to just open an issue uh in the GitHub repository um asking us to change something
[2635.62 → 2641.18] or something like that okay cool yeah uh AMS if you weren't doing this what would you be doing
[2641.18 → 2649.82] instead oh i I would surf the amazing beaches of um Sri Lanka every day awesome for like 12 hours
[2649.82 → 2655.58] we've we've actually had a few people say surfing so uh so yeah that seems to be a common trend
[2655.58 → 2663.04] amongst uh developers what about you roughly um I'd probably be a musician I think okay what do you
[2663.04 → 2670.02] play yeah I play flute and piano go to roughly's SoundCloud page listen to what no, no no not yet I've been
[2670.02 → 2676.12] experimenting with like no, no encourage him he's making really nice music um
[2676.12 → 2686.46] that's roughly Schwaben Cohen on SoundCloud yeah I just thought it's sorry man that's fine that's awesome
[2686.46 → 2693.02] yeah sorry your music career begins now uh AMS you might need to be looking for a replacement for
[2693.02 → 2698.76] mean JS so nothing's gonna break this relationship don't worry we've been through a lot
[2698.76 → 2709.56] um a programmer hero oh that's a tough one that's an easy one for me uh Douglas Crockford for sure
[2709.56 → 2715.72] yeah um he's the good parts the good parts yeah for sure he's the guy who made uh JavaScript
[2715.72 → 2723.18] all make sense to me and I have watched all of his lectures on YouTube um read all his books he's
[2723.18 → 2729.32] just an awesome dude yeah for sure any for you AMS and AMS you could uh you could even say uh
[2729.32 → 2736.64] your parents we've had that before yeah oh that's um I think Dennis Ritchie which wasn't really
[2736.64 → 2745.18] appreciated at this time um he died the same day uh the same week Steve Jobs died uh invented the
[2745.18 → 2752.54] language and contributed to the Unix um it was really cool I like those ad guys
[2752.54 → 2762.22] in the duo of was and Steve Jobs i I'm I'm certainly the was um kind of guy yeah that's good
[2762.22 → 2767.64] yeah they need support to that's good yeah yeah totally they do cool stuff awesome they do cool
[2767.64 → 2774.16] stuff they just do it because they like to do it not any other yeah yeah yeah I mean you when
[2774.16 → 2778.86] you kind of start reading into a lot of that history you see that it's its generally the people
[2778.86 → 2783.48] with more moxie that become famous and not necessarily I mean not to not take anything
[2783.48 → 2788.28] away from Steve Jobs yeah of course I'm old but um that you know he has a moxie and that's kind of
[2788.28 → 2794.10] what propels him to like super stardom status versus you know the uh the Nazis of the world
[2794.10 → 2799.86] and was he so nice he loves to give you yeah yeah he's a nice guy he's a really nice guy
[2799.86 → 2807.04] awesome yeah well I wanted to say thanks so much for joining us on the show again it was uh
[2807.04 → 2812.66] AMS Aviv and roe Schwaben Cohen talking about mean JS which uh sounds like it's its it's just
[2812.66 → 2817.66] getting started, but it's got some tremendous uh movement behind it and I'm excited to kind of
[2817.66 → 2822.58] see where it goes um you mentioned this before but what is the twitter for mean JS that people can
[2822.58 → 2830.74] follow uh it's mean JS org the website is mean JS dot org um we're mean JS on Facebook and GitHub
[2830.74 → 2836.02] um we hope twitter would give us the mean JS name because it's abandoned for some reason
[2836.02 → 2844.94] uh but for now it's mean JS org um awesome yeah well we'll be back next week with another show uh sorry
[2844.94 → 2851.26] that we have been absent a little bit I've been starting a new uh a new job and so it's been kind
[2851.26 → 2856.50] hectic so uh for our listeners we will be back next week, and we'll be uh weekly from here on out so
[2856.50 → 2861.46] until next week let's say goodbye thank you guys thanks a lot guys
[2881.26 → 2888.64] uh
