[0.00 --> 15.10]  welcome back everyone this is the changelog and i'm your host adam stekowiak this is episode 131
[15.10 --> 22.32]  jared and i've talked to tom dale and yahoo the cats about the road to ember 2.0 today's show is
[22.32 --> 27.38]  sponsored by pager duty hired and digital ocean we'll tell you a bit more about hired and digital
[27.38 --> 32.94]  ocean later in the show but our new sponsor pager duty i'm excited to have him on board if you've
[32.94 --> 37.18]  ever gotten to work only to find something happen when you're out the server's down customers aren't
[37.18 --> 44.02]  happy chaos everywhere you gotta listen up pager duty decreases alerting noise for operations and
[44.02 --> 49.48]  developers when an incident occurs pager duty notifies the right team and team member with
[49.48 --> 54.88]  personalized alerts that fit everyone's communication preferences not only that they also have analytics
[54.88 --> 59.02]  tools that help you identify common problems allowing you to make system improvements
[59.02 --> 65.56]  proactively so you don't have to be woken up at 2 a.m sign up for a 14 day free trial at pagerduty.com
[65.56 --> 68.40]  slash the changelog and now on to the show
[68.40 --> 81.00]  we're here with uh tom dale yahoo the cats myself and jared santo we're gonna have this awesome
[81.00 --> 85.82]  conversation about the road to ember 2.0 i think it's been a long road a fun road you got lots of
[85.82 --> 90.68]  things happening on not only the product side where you use ember but the open source side where
[90.68 --> 96.14]  you got this great direction and a lot of uh a lot of steam happening here so i want to welcome you guys
[96.14 --> 102.46]  to the show so say hello hey great to be here and i guess we'll start with tom tom give a quick intro to
[102.46 --> 107.34]  kind of who you are and what you do it uh at tilde and then also what you're doing for ember
[107.34 --> 115.30]  oh sure yeah so hey uh my name's tom i'm one of the co-founders at tilde and uh i guess i have been
[115.30 --> 121.52]  working at tilde i realize now a good part of my career which is really rewarding so we bootstrapped
[121.52 --> 127.22]  tilde started about three or four years ago and we work on a product called skylight and i'm very
[127.22 --> 132.76]  fortunate in that i get to work on mostly the the front end of that which is just a big ember app
[132.76 --> 139.52]  so it's really nice to be able to dog food your own open source so so much and then i guess in the
[139.52 --> 145.04]  the rest of my time my nights and weekends is spent working on ember so you who and i wrote ember
[145.04 --> 150.02]  like three or four years ago now um and that was actually coming off the back i worked on and
[150.02 --> 155.80]  maintained sprout core at apple and the startup i left apple to go to after that yeah and you who
[155.80 --> 162.88]  yeah so i guess i've been programming for a while now uh i think you have yeah yeah i actually for a
[162.88 --> 167.12]  long time i hadn't been programming for that long but now it's been a while uh basically since the
[167.12 --> 174.80]  beginning of like the jQuery days i got to miss all the sad sad years of uh dark days of the web i.e.
[174.80 --> 180.18]  winning i basically came on right after the end of that which was great the fun times yeah i mean
[180.18 --> 186.20]  it was still there's still a lot of work to do but it was no longer a den of despair was that when
[186.20 --> 191.66]  firefox had just kind of taken up some yeah firefox just came out jQuery just came out rails just came
[191.66 --> 199.52]  out right so like basically there was hope for for once um so i did that for a while um i also did a
[199.52 --> 203.86]  few different companies and tilda like tom said the reason why i was really excited to do tilda was
[203.86 --> 209.26]  that i had done a bunch of i've been part of at an early stage a lot of vc funded startups and i was
[209.26 --> 215.52]  finally in a position to start one and try to bootstrap and um honestly it's everything i it's
[215.52 --> 223.16]  very frustrating at times obviously like anything in life but uh as a whole it's it's pretty much
[223.16 --> 228.32]  everything i hoped it would be and it indeed lacks many of the things that were sad about uh vc funded
[228.32 --> 233.32]  startups and you guys started off with tilda was all consulting wasn't it or did you have product
[233.32 --> 238.84]  plans right away i think we always knew that we wanted to do the product but uh
[238.84 --> 244.32]  unfortunately you know you had mentioned that he was at several early stage startups none of us was
[244.32 --> 249.90]  independently wealthy so it's pretty hard to bootstrap a company when you're just you know
[249.90 --> 261.20]  making an engineer's salary um so we we use consulting as a mechanism to avoid the whole vc uh the whole vc
[261.20 --> 267.24]  fundraising death march which has been really really great uh although as you just said stressful at times
[267.24 --> 273.32]  but i think actually the best thing for us about doing the consulting is it has really opened our
[273.32 --> 279.46]  eyes about how to run an open source project because we get to go around to so many different
[279.46 --> 284.60]  companies and each company has such a different culture has such a different process and has very
[284.60 --> 289.86]  different requirements and so being able to kind of peek behind the curtain at people who are all these
[289.86 --> 294.10]  different companies that are using ember and see how their needs are different but also most
[294.10 --> 300.04]  importantly how their needs are the same has been uh really really really helpful in terms of kind of
[300.04 --> 305.18]  steering ember in the direction it needs to go and also in terms of product like one thing that was
[305.18 --> 309.84]  pretty one thing that worked pretty well for us is when we started thinking about it we thought of a few
[309.84 --> 315.08]  different options and many of the options actually were similar to things that other companies have done
[315.08 --> 318.72]  and you know sold big to google but we actually focused on a product that we thought could be
[318.72 --> 323.70]  sustainable over the long term that we that we knew people would actually pay for and that constraint
[323.70 --> 328.80]  actually ended up being far more um interesting and important than a lot of the other constraints
[328.80 --> 333.82]  like we could build a lot of cool stuff but actually focusing on something that we knew people would
[333.82 --> 339.16]  pay decent money for actually is what drove us towards the product that we ended up building
[339.16 --> 345.38]  interesting so uh incorrect if my history is wrong but i feel like tilde and ember kind of were born
[345.38 --> 350.78]  around the same time i know it was originally sprout core and you guys kind of moved away from there
[350.78 --> 355.22]  was ember kind of like a core strategy of you guys from a business side or is open source a core
[355.22 --> 361.56]  strategy that you just said we have to do this alongside tilde well i think open source uh i don't
[361.56 --> 367.52]  want to call it a strategy because i think people may get the impression that we did ember because we
[367.52 --> 373.76]  want to become ember inc right and we want to sell these consulting packages you know and or be be like
[373.76 --> 379.34]  the mongo db or be like a meteor where the whole company the company is the open source product and the
[379.34 --> 383.92]  open source product is the company in a lot of ways right um but that's something that from the
[383.92 --> 389.22]  beginning we knew that we wanted to distance ourselves from because our belief is that the
[389.22 --> 394.80]  strongest open source projects are led not by one company but by a coalition of companies
[394.80 --> 400.58]  and and i'm very happy with where we've ended today because we could go out of business tomorrow
[400.58 --> 404.78]  and ember as a project would still continue to be very very healthy most of the maintainers do not
[404.78 --> 411.72]  work at tilde which is really really great um if anything i think open source is just a huge part
[411.72 --> 419.20]  of who especially yahuda and i are and that was one of the the benefits of starting our own company
[419.20 --> 424.34]  because so many times we've been at these corporations where we would have to expend so much
[424.34 --> 429.48]  energy just fighting with management trying to convince them that open source was a valuable thing
[429.48 --> 434.64]  yes and now we have our own place and we can say you know we don't have to have that discussion
[434.64 --> 440.10]  everyone coming in just assumes and knows that open source is a huge priority for us i can especially
[440.10 --> 444.52]  see that on your side tom as being at apple with you know the secrecy thing of course they do have
[444.52 --> 449.80]  open source things but i think wasn't sprout core was it open source uh sprout core was open source
[449.80 --> 454.92]  and it was definitely very unusual for apple to be open source at the time it was it was just a weird
[454.92 --> 460.18]  thing it was just it just didn't fit into the culture of apple and it was it was really really
[460.18 --> 466.84]  painful because every time we wanted to submit a patch publicly we had to hand prepare diffs that
[466.84 --> 471.84]  would be sent to a lawyer and we had to annotate each section of the diff explaining what was going on
[471.84 --> 476.04]  and identifying if there was anything that could be patentable oh sorry i gotta check on that one
[476.04 --> 481.32]  because that's it's like such a buzzkill it's like a lawyer-based pull request yeah i definitely i
[481.32 --> 487.02]  definitely agree with tom that i think it's less about making ember a big part of tilda and more
[487.02 --> 492.98]  just i think i agree me in particular but i think tom the reason we're friends is that we we share this
[492.98 --> 498.70]  um we care a lot about open source in general as people and as steve jobs said you should do the
[498.70 --> 502.86]  thing that you're passionate about and i think people often underestimate that they they underestimate
[502.86 --> 508.22]  the fact that you're going to be doing a startup for years and years of your life you actually
[508.22 --> 513.92]  need to be doing something that you can work nights and weekends that you can get up a night when
[513.92 --> 518.76]  things are stressful and still push through and i think the fact that we both really care about open
[518.76 --> 523.44]  source and everybody else at the company basically also cares about open source that means that when
[523.44 --> 527.92]  times are tough it's something that we can look at and say this is all worth it and i think if we had
[527.92 --> 532.88]  you know we could have built skylight with less open source and that would have been that would have
[532.88 --> 538.20]  been a possibly successful product but i think it would have given us less motivation to keep going all the
[538.20 --> 543.30]  time and i and i think people just yeah like i said people forget the fact that being passionate
[543.30 --> 550.58]  about what you're doing is how you keep going awesome and i mean why do we start our own companies
[550.58 --> 554.70]  or bootstrap if you have that privileges so that you can be the kind of company that you want to be
[554.70 --> 559.48]  so it makes total sense that you guys you guys are doing open source beforehand just that's who you
[559.48 --> 565.22]  are um so let's talk about ember maybe tom give us kind of the you know the blimp view of what ember
[565.22 --> 569.74]  is for those people i'm not exposed to the product and then maybe you could if you can give us a brief
[569.74 --> 574.06]  history of maybe how it started at sprout core i know it's been a long history but if you could
[574.06 --> 579.92]  summarize it and bring us up to where we're at today sounds good so i think at a very high level
[579.92 --> 586.56]  ember js is a javascript framework for building apps it's not really for building you know individual
[586.56 --> 591.50]  islands of richness it's not for building little uh you know widgets that you might put on your page
[591.50 --> 596.74]  it's for building client-side apps whose architecture is more similar to a phone app or a desktop app
[596.74 --> 604.56]  than a traditional server rendered web app but i think what's really interesting about ember is how much
[604.56 --> 615.44]  it's evolved so when we started ember in i think it was back in 2011 it was a purely view-based
[615.44 --> 621.28]  component library basically so it had handlebars templates and you could plug those templates into
[621.28 --> 627.42]  a some kind of data source which is usually a controller and that was it and i think if people
[627.42 --> 632.80]  know people know of ember today probably one of the things that they think about it one of the most
[632.80 --> 639.10]  you know widely known features is our router because the the router that we have in ember which
[639.10 --> 643.70]  basically keeps your application state in sync with the address bar in your browser that's
[643.70 --> 649.82]  definitely an industry leader i think we've got the best router on the market there and that didn't
[649.82 --> 656.02]  even exist when we started the project which is pretty incredible so this is kind of this iterative
[656.02 --> 661.10]  process that we've applied to ember where again we go and we talk with so many developers and we see
[661.10 --> 666.86]  where their pain points are and ember is all about just rolling common pain points for web developers
[666.86 --> 672.16]  into a single community solution that everyone can kind of use and agree on so we don't spend time
[672.16 --> 677.24]  everyone solving it a thousand different ways uh so when when we started we were just this kind of
[677.24 --> 683.14]  component library kind of similar to something like react today but quickly we discovered okay well
[683.14 --> 688.16]  people are having a lot of trouble one making apps that didn't feel broken because javascript apps felt
[688.16 --> 692.98]  and continue to feel today sometimes extremely broken in terms of like their back button and reloading
[692.98 --> 698.10]  uh so and we're also having trouble trying to figure out okay what data is on the screen what
[698.10 --> 701.94]  templates are on the screen right now keeping everything in sync and in other words bootstrapping the
[701.94 --> 708.66]  application as it as it starts up um and the router was kind of a nut crack for both of those you
[708.66 --> 713.36]  know we kind of cracked the nut of oh you can actually manage application state and have great urls
[713.36 --> 719.86]  through this single abstraction and so that was ember 1.0 was the introduction of this new router
[719.86 --> 726.12]  and over the past year we've been iterating a lot on what are the other pain points so the biggest
[726.12 --> 731.82]  one that we've identified in the last year is build tooling so every project every company we went into
[731.94 --> 735.54]  it's you know some people are using grunt some people are using gulp some people are using
[735.54 --> 742.86]  broccoli everyone's got a thousand different hand-rolled buggy scripts to handle the same set
[742.86 --> 747.20]  of problems everywhere and they're not shareable so we'd go in and i had to learn their build system
[747.20 --> 751.30]  because it was different from the last place i was at so ember cli has been the biggest component
[751.30 --> 756.04]  we've been working on this year it's been very popular so i i like to think of ember as having kind of
[756.04 --> 762.86]  involved sorry evolves into this complete front end stack where you can kind of take ember off the
[762.86 --> 767.36]  shelf you can boot up a new app in literally you know 30 seconds boom you've got a new ember app
[767.36 --> 772.38]  everything you need is there and you can start being productive right away cool i kind of stop you there
[772.38 --> 777.50]  i do i'm curious i have a question for both you guys you mentioned tom that you know the router and
[777.50 --> 781.88]  you got the broken back buttons and you said there's a lot of javascript apps that are just still kind
[781.88 --> 788.40]  of broken today yeah and i think we all feel that pain from time to time um there are some vocal
[788.40 --> 796.32]  kind of opponents to the front end stack uh that ember angular are providing um most notably you know
[796.32 --> 803.66]  dhh is kind of in the base camp crew um have kind of gone the other direction and um vocal people like
[803.66 --> 809.00]  i know gary bernhardt oftentimes just says don't ever use javascript because it always well gary says don't
[809.00 --> 814.70]  use any software at all that's true that's true he's generally mad at all software and he tends to
[814.70 --> 820.02]  make me mad too just listening to him like you know what you're right man so you know you guys
[820.02 --> 824.66]  have obviously heavily invested into javascript um i wonder what your guys take is on that is it just
[824.66 --> 829.28]  because we're doing it wrong or is there some fundamentally still like technology needs that
[829.28 --> 834.36]  need to be there before we can have robust reliable javascript apps so i actually find it a little bit
[834.36 --> 839.50]  ironic that dhh is so against the front end but i also understand it um and i i kind of want to answer
[839.50 --> 844.42]  the earlier question that you had which is about the history because it sort of feeds into this so i
[844.42 --> 849.80]  basically started my career working on a project called merb my open source career which was a
[849.80 --> 854.60]  competitor to the ruby on rails framework and essentially the idea behind merb was rails basically
[854.60 --> 859.94]  got it right but there are some problems that rails has most notably at the time the modularity and
[859.94 --> 864.54]  plugin system was pretty weak it didn't really have a well-defined way of hooking into the framework
[864.54 --> 870.90]  and you sort of just went out you the plugin system was like go svn clone some stuff into your directory
[870.90 --> 876.26]  and hope everything works and people weren't using ruby gems and the idea behind merb was let's get a lot
[876.26 --> 881.66]  more serious about what the plugin api actually is how plugins hook into the life cycle and let's try to
[881.66 --> 888.06]  keep the core a little bit smaller so that the things can be swapped out in a more predictable way that was the
[888.06 --> 893.02]  idea behind merb and when i went to work on rails that's sort of what we did and i worked on that for
[893.02 --> 898.60]  probably 18 months um revamping the plugin system rebuilding the controller system from the ground up
[898.60 --> 903.60]  to be built in a more modular way so that things could be in a layered way so things could be pulled
[903.60 --> 910.88]  out as needed and i think that that strategy is very effective because on the one hand the idea behind
[910.88 --> 915.00]  rails is everyone's doing the same thing all the time and because everyone's doing the same thing all
[915.00 --> 919.32]  the time let's have a single solution that the community maintains as a group that everyone
[919.32 --> 924.70]  agrees is the right answer right and that i think is very powerful because the alternative is what we
[924.70 --> 928.40]  see in the javascript ecosystem today for the most part which is that everyone starts a new project
[928.40 --> 934.06]  and then they spend like tom said literally weeks trying to figure out which set of tools is the you
[934.06 --> 938.96]  know the top the right point of at the hype cycle to to jump in and use it right so you have this
[938.96 --> 944.08]  mega hype fatigue every time anybody starts a new project they have to spend weeks trying to figure out
[944.08 --> 948.62]  what's the right thing and i think rails did a couple things really well it said we're going to
[948.62 --> 953.30]  have a shared solution but also we're not going to be like java and take forever to change every new
[953.30 --> 957.54]  version of rails is going to take a look around and try to incorporate and bring in things that the
[957.54 --> 962.64]  community has decided are the right practices but so at the point at the point of rails 2 there was a
[962.64 --> 968.48]  bigger problem which is that rails had gotten too big as an ecosystem to have one opinion be the only
[968.48 --> 973.62]  opinion and so there were some things that people were doing like rspec and hamel where people were able to
[973.62 --> 979.82]  sort of sneak in through the fact that ruby is a very dynamic language and you know break in say
[979.82 --> 985.46]  okay we're going to use hamel instead of erb but rails 2 internally was really not designed for this
[985.46 --> 990.12]  and so what was starting to happen was that new versions of rails tended to break plugins people
[990.12 --> 995.22]  would you know you may have in order to upgrade to rails 2 3 whatever you may have had to wait weeks
[995.22 --> 1000.68]  to get hamel or rspec to update and this was a really big issue and so i think what rails 3 showed
[1000.68 --> 1005.98]  was that you could have all the benefits of having a single maintained stack but you can build it
[1005.98 --> 1010.48]  internally in a nice modular way so that if people want to write a plugin that lets you swap out hamel
[1010.48 --> 1016.84]  or erb for hamel or test unit for rspec or whatever they want that you can have a reasonable assurance
[1016.84 --> 1021.24]  that things will tend to work and on the flip side you can have a reasonable assurance that the core
[1021.24 --> 1027.14]  team is still focusing on bringing in newer uh newer features from the ecosystem so a really good
[1027.14 --> 1032.76]  example of this would be the asset pipeline right i think the rails core team discovered that just
[1032.76 --> 1037.16]  you know concatenating javascript wasn't the end of the story we needed a bigger solution and so
[1037.16 --> 1042.70]  rails now has pretty much i think ember cli does a good job with this but a pretty close to best in
[1042.70 --> 1047.36]  class solution for uh building assets to the point where a lot of people will use rails just for the
[1047.36 --> 1051.88]  asset pipeline right and this is something this is sort of a balance that you have to that you have to
[1051.88 --> 1056.66]  have you want to build your stuff internally so it can be that you can um you can plug in at
[1056.66 --> 1061.58]  appropriate points you want to have a thing that the entire ecosystem uses and then you also want to
[1061.58 --> 1067.42]  make sure that you're able to iterate fast and i think unfortunately when dhh took a look at rail at
[1067.42 --> 1073.26]  ember at first and the entire ecosystem what he discovered correctly was that we were still extremely
[1073.26 --> 1077.78]  early days we were still trying to figure out what it even meant to build a complete front-end stack
[1077.78 --> 1084.38]  and the vast majority of the javascript ecosystem unlike the rails ecosystem which dhh is so used to
[1084.38 --> 1089.12]  hates the idea of building shared solutions everybody wants to build their own thing everybody
[1089.12 --> 1094.22]  wants people are so afraid of falling behind that they're willing to go and look at uh they're willing
[1094.22 --> 1097.48]  to try every new thing that comes out just to make sure that they don't miss something important
[1097.48 --> 1104.24]  so what ends up what ended up happening is dhh went he took a look at the situation i believe he uh his
[1104.24 --> 1108.68]  team tried to use backbone backbone is so far away from the philosophy of rails that it's not at all
[1108.68 --> 1115.10]  surprising to me that he considered it a total failure and then we ember at the time was completely
[1115.10 --> 1119.86]  unready to deal with people who were trying to do it we were we were we were pioneers essentially we
[1119.86 --> 1123.10]  were exploring the space we were trying to figure out what it even meant to build the front
[1123.10 --> 1128.98]  front-end application so today we saw ember sort of gets attacked or so ember is basically under
[1128.98 --> 1133.78]  attack from two sides there's one side where people are saying people are looking at ember as if it was
[1133.78 --> 1139.84]  the equivalent of a thing like react or backbone or angular and i mean angular 1.0 here angular 2.0 is
[1139.84 --> 1145.20]  trying to push a different direction but they look at ember and they say well it's you know the javascript
[1145.20 --> 1149.58]  community doesn't have this idea of convention over configuration they don't have this idea of trying
[1149.58 --> 1154.30]  to build a community around things i think if you're from rails it can feel it can feel very frustrating
[1154.30 --> 1161.14]  and you many people don't even really take a close look at ember to see these days if it or if it does
[1161.14 --> 1165.86]  it feels like rails right i don't mean feels programmatically like rails i mean feels like
[1165.86 --> 1171.74]  that kind of ecosystem where people are pushing forward um and then on and the other side so you
[1171.74 --> 1176.14]  have people from rails saying oh my god it looks like the javascript ecosystem is crazy and then on
[1176.14 --> 1179.90]  the other side you have all the javascript people saying oh my god how could you build such a large
[1179.90 --> 1184.96]  monolithic vertically integrated stack this is clearly terrible and so there's just a noise around ember
[1184.96 --> 1189.06]  uh is a little bit different because of the ecosystem and the noise around rails
[1189.06 --> 1195.72]  let's pause the show for a minute give a shout out to a sponsor hired.com is sponsoring the show this
[1195.72 --> 1203.52]  week and the url you need to go to is hired.com slash changelog podcast again hired.com slash
[1203.52 --> 1209.54]  changelog podcast and when you go there uh they're going to give you a they're going to double the
[1209.54 --> 1215.26]  signing bonus that they give you if you accept a job on hired.com from two thousand dollars to four
[1215.26 --> 1222.08]  thousand dollars every week on hired uh thousands of tech companies in san francisco new york seattle and
[1222.08 --> 1229.16]  la uh bid on hiring awesome developers providing the salary and equity up front some of their most
[1229.16 --> 1237.14]  in-demand jobs are web and mobile developers devops ui ux and even some product managers the average
[1237.14 --> 1244.28]  developer gets about five to fifteen offers with equity with salary all that up front uh and even
[1244.28 --> 1248.90]  if you're not looking for a job but you might know someone who is you can revert you can refer them to
[1248.90 --> 1254.78]  hired and get an awesome bonus as well if they accept the job and the amount of that one is one thousand
[1254.78 --> 1261.52]  three hundred and thirty seven dollars total leet so go to hired.com slash changelog podcast and get hired
[1261.52 --> 1268.70]  so do you think that the just the the the pioneering that has been going on and maybe perhaps the
[1268.70 --> 1275.90]  fragmentation and the ecosystem leads to um less than reliable javascript apps at the end of the day
[1275.90 --> 1283.56]  i think if you have the right abstractions you can absolutely build great javascript apps and and this is
[1283.56 --> 1290.34]  i i think where uh the the server rendered camp is a little bit wrong you know you can you can
[1290.34 --> 1295.90]  introduce a lot of complexity on top of people's existing stacks and they're willing to accept it
[1295.90 --> 1302.10]  but in order to get really really truly great performance out of a server rendered app like
[1302.10 --> 1306.92]  something written in rails you have to add a lot of complexity and that's complexity that if you just
[1306.92 --> 1311.10]  build the app in ember that you you don't have to deal with just to get that kind of performance
[1311.10 --> 1317.48]  right because you're moving the logic from the server to the user's browser there's nothing there's
[1317.48 --> 1324.00]  no cash in the world that is going to be faster than that right now if you're in a a really seasoned
[1324.00 --> 1329.96]  rails veteran you've got the stack you're super productive it doesn't really surprise me that
[1329.96 --> 1335.00]  people are kind of going to calcify into that right because they're super productive especially as the
[1335.00 --> 1339.54]  javascript ecosystem matures but there's going to be a day when the industry shifts and a lot of the
[1339.54 --> 1344.14]  people who have calcified on server rendering i think are going to end up with products that are being
[1344.14 --> 1348.72]  smoked by the competition because to be honest with you if you use a javascript app a really well
[1348.72 --> 1353.26]  done javascript app it does all the routing on the client side it has really rich interactions that
[1353.26 --> 1358.10]  just aren't possible when you have to have the browser and the server coordinate you use an app
[1358.10 --> 1364.02]  like that it feels so great it feels so fast going back to something that has to talk to a server just
[1364.02 --> 1369.62]  feels antiquated and again there are things you can do you know russian doll caching and so on but they
[1369.62 --> 1373.98]  introduce a lot of complexity especially for loot for new learners who may not be familiar with the
[1373.98 --> 1378.94]  stack now here's an additional concept you have to learn and a lot of people are on crappy wi-fi
[1378.94 --> 1385.20]  networks they're on slow 3g networks it doesn't matter how fast your app renders on the server if the
[1385.20 --> 1392.36]  pipe to get to them is slow so maybe for our listeners um maybe either of you could give maybe a
[1392.36 --> 1397.40]  couple ember apps that you think are like really well written javascript apps obviously obviously there's
[1397.40 --> 1402.00]  skylight which is your guys's product surely that which is the best one by far we like skylight if
[1402.00 --> 1407.08]  you want to see like the reference implementation skylight.io by the way yeah okay and i know heroku
[1407.08 --> 1411.72]  built their new dashboard oh that's gorgeous which is really nice are there any others just off the
[1411.72 --> 1416.40]  top of your head you know there's a wide range and kind of surprising you know i think uh maybe a year
[1416.40 --> 1423.10]  or two ago there was this meme that javascript is really great for you know toolbox apps or editor apps
[1423.10 --> 1427.96]  where you have to do a lot of interactivity and you have to log in you know uh any kind of like
[1427.96 --> 1432.30]  editing or management or any kind of creative thing but for content sites content sites obviously
[1432.30 --> 1437.58]  javascript is totally inappropriate but there's two major content sites that i can think of off the top
[1437.58 --> 1443.68]  of my head uh which is vine uh the twitter's video sharing app their whole web experience is an
[1443.68 --> 1450.56]  ember app it's vine.co uh and bustle is the other one uh bustle is like a pretty very successful uh kind
[1450.56 --> 1456.64]  of like women's news website bustle.com and the entire front end is ember and you can really feel
[1456.64 --> 1460.64]  it as you click around man it responds so so quickly and you wonder how the heck do they get
[1460.64 --> 1466.48]  it this fast and it's because it's a number app cool yeah and i think in terms of non-content sites uh
[1466.48 --> 1472.48]  discourse and ghost are two open people often ask about open source projects discourse and ghost are
[1472.48 --> 1477.26]  two open source projects that are written in ember and i think do a reasonably good job discourse is
[1477.26 --> 1481.52]  really really fanatical about performance so maybe if you go look at it you'll find some stuff that
[1481.52 --> 1485.76]  they do to really squeeze the last drop of performance out um ghost is a little bit more
[1485.76 --> 1490.70]  idiomatic but both of them are examples of real world fairly large and complicated ember applications
[1490.70 --> 1494.80]  that work and those are both open source so you can go take a peek under the hood and see how
[1494.80 --> 1499.04]  basically see how the sausage gets made and i think we're both pretty proud about how they turned out
[1499.04 --> 1504.24]  they're not these incomprehensible messes they actually i just love the fact that when i go look at ghost or
[1504.24 --> 1510.34]  or discourse or travis which is also um which is also uh an ember app that's open source and i go
[1510.34 --> 1515.58]  look around to try to get my head around what's going on it's pretty easy for me having rarely
[1515.58 --> 1519.50]  looked at this code base to get a sense of what's going on where things are located and all that
[1519.50 --> 1524.58]  which is a thing i got used to being true about rails but is rarely the case in javascript applications
[1524.58 --> 1529.34]  right when you drop into most open source projects it's like oh my gosh where do i even begin you kind
[1529.34 --> 1532.12]  of have to survey the entire code base just to even start adding a feature
[1532.12 --> 1536.80]  um but because of ember strong conventions i can drop into something like discourse or ghost or
[1536.80 --> 1541.14]  travis and i want to change this template i know exactly where the temple is because it's based on
[1541.14 --> 1546.86]  what the url i'm looking at is yep cool we'll link those up in the show notes for for the listeners to
[1546.86 --> 1552.52]  go click through and check out um but let's let's look to the future now so 10 days ago i'm looking here
[1552.52 --> 1560.88]  at uh a post on the ember js github the road to ember 2.0 rfc tom posted this i'm sure he didn't
[1560.88 --> 1564.78]  necessarily write the whole thing itself it looks like this was a community effort you know it just
[1564.78 --> 1572.82]  came to me in the shower and i wrote it down um but man well thought out first of all i mean i
[1572.82 --> 1578.38]  appreciate how much thought you guys are putting into into the software because that can only lead
[1578.38 --> 1585.00]  to good things but um maybe just high level summary i think if maybe i'll i'll give you what i think it
[1585.00 --> 1591.78]  says and you can you know refute or or uh say i'm right uh major points um that you made in this
[1591.78 --> 1597.46]  is that this is not going to be a big big bang rewrite you're trying to have stability with without
[1597.46 --> 1603.50]  stagnation this is a phrase you guys used um you had some big bets in 2014 you have some more big bets
[1603.50 --> 1609.34]  for the future a lot of this comes from learning from the community you're going to be simplifying
[1609.34 --> 1615.60]  things which is always nice especially when you had a thing that's been evolving over time um and
[1615.60 --> 1619.42]  you have some big features that you talk about there at the end is that is that a top level pretty
[1619.42 --> 1623.70]  good or did i miss something yeah i think probably the only major thing that people have talked about
[1623.70 --> 1630.66]  that is top level relevant is that a lot of the ideas that we got for ember 2.0 that are starting
[1630.66 --> 1637.08]  to land already actually came from uh the react project so react is a pretty great project i think
[1637.08 --> 1642.22]  they've been doing cool stuff they call themselves just the view layer um but their view layer has
[1642.22 --> 1647.26]  some really great ideas in it and a lot of the ways that we're thinking about simplifying going forward
[1647.26 --> 1652.06]  has been adopting some of the ideas from the react project cool now let's let's go back to the
[1652.06 --> 1657.92]  beginning the big bang rewrite to me okay so i've done some angular apps i've done i've done uh one ember
[1657.92 --> 1664.38]  app um which was about a year and a half ago before you guys were 1.0 and this seemed like a shot
[1664.38 --> 1669.86]  right across the angular bow here after their announcements uh at ng europe yeah i think a lot
[1669.86 --> 1676.12]  of people felt like we were trying to capitalize on their uh misfortune because i think yeah like
[1676.12 --> 1681.78]  the the stuff they announced actually wasn't new uh you know all the details had been out in the
[1681.78 --> 1686.32]  public for you know what at least six months uh but i think the way that they they presented it
[1686.32 --> 1691.92]  maybe um scared some people yeah scared some people they reacted pretty strongly to it yeah so i think a lot
[1691.92 --> 1699.04]  of people thought that we saw this news and you know started you know we went back to our dark
[1699.04 --> 1703.50]  smoky room and we're like how can we nail these guys um but the truth unfortunately is a little bit
[1703.50 --> 1710.02]  more boring um all of the all the plans all the details essentially that you see in that document
[1710.02 --> 1717.00]  were from the last two core team meetings now the most recent core team meeting very coincidentally
[1717.00 --> 1722.98]  was scheduled months in advance for around the time when the angular 2.0 announcement was was made
[1722.98 --> 1728.20]  um so the timing certainly looks suspicious i will i will grant people that but i promise you that
[1728.20 --> 1734.28]  i have an email list showing this is scheduled months in advance um and so the last two core team
[1734.28 --> 1738.98]  meetings we like to do face-to-face meetings with the core team we all fly into some city everyone
[1738.98 --> 1744.12]  pays out of pocket so it's really awesome of them and i thank all the core team members for you know
[1744.12 --> 1748.88]  really paying out of pocket to contribute to this open source project anyway how big is that team
[1748.88 --> 1755.08]  it's like 11 people now wow that's a big that's a big meeting that yeah it's a big meeting so we all
[1755.08 --> 1761.76]  fly into last time i think we did uh new york this time we did chicago and we all sit in a in a
[1761.76 --> 1765.66]  conference room for like eight hours over the weekend eight hours per day over the weekend and we
[1765.66 --> 1772.44]  try to really nail down the details of the roadmap of the framework and um everyone on the core team
[1772.44 --> 1778.80]  has a product that is built using ember or has clients who have products built using ember
[1778.80 --> 1786.72]  and so the commitment to stability without stagnation was not just to you know try to get back at angular
[1786.72 --> 1792.86]  i don't think anyone on the team is that petty it was simply the fact that we have strong incentives
[1792.86 --> 1797.26]  not to break anything because we've all got apps that we make our livelihoods from and i think on the
[1797.26 --> 1801.18]  flip side of of breaking things i think all of us have applications that are competing
[1801.18 --> 1807.62]  working with much bigger players we're running startups working with small companies and we can't
[1807.62 --> 1815.78]  afford to let the opinions of ember from 2011 calcify and control what we're able to do in 2015 so i think
[1815.78 --> 1819.60]  it was really important it's important for us to continue to look at what's going on and make sure
[1819.60 --> 1826.20]  that the cutting edge of what's possible on the web is also possible in ember so these are basically the
[1826.20 --> 1831.20]  two uh things that were the two pressures that seem very contradictory and actually kind of
[1831.20 --> 1838.10]  interestingly a lot of the response to the angular uh the angular announcement was well you need to
[1838.10 --> 1842.18]  make progress so what else other choice do you have you have to break everything and and i sort of think
[1842.18 --> 1846.20]  about think about it the opposite which is if you're breaking everything all the time then how do you ever
[1846.20 --> 1852.12]  get anything done right so you need to figure out a way it's basically like uh just it's a little
[1852.12 --> 1856.88]  harder and it requires more thought but it's not like we're the first people in the world to ever
[1856.88 --> 1863.62]  figure out a way to to improve the situation to make things more cutting edge without stagnating and
[1863.62 --> 1867.66]  in fact the web is all about that right the last five years everybody says moving at web speed but
[1867.66 --> 1871.96]  what is the web all about the web is all about not breaking the web while still adding the features
[1871.96 --> 1878.42]  right it's exactly this i i sort of found it ironic that people were using the web speed as a as a
[1878.42 --> 1882.76]  explanation for why you have to break everything all the time when the web as its prime directive
[1882.76 --> 1887.76]  has you can't break anything ever you know it's just annoying like trying to move things forward in a
[1887.76 --> 1894.56]  backwards compatible way requires a lot more time and it's it's just annoying to do as an engineer it's
[1894.56 --> 1899.70]  just annoying and and so that's why i think it's so important to use open source projects that are
[1899.70 --> 1904.32]  kind of aligned with your interests because i promise you if i was just working on ember as my full-time
[1904.32 --> 1908.38]  job i would not bother with this it's only because we have the product that we can't break that we
[1908.38 --> 1913.50]  go through the pain of maintaining backwards compatibility what's your guys's plan as far as
[1913.50 --> 1917.96]  doing that your methodology for maintaining the stability while you're still moving forward
[1917.96 --> 1924.18]  so i can talk about this and uh not surprisingly our plan is essentially derived from what the
[1924.18 --> 1929.12]  browsers do um the browsers sort of had exactly the same situation somewhere around the time that
[1929.12 --> 1933.80]  chrome came out the browsers were really excited about moving forward but they just but they were
[1933.80 --> 1940.26]  stuck in these multi-year-long release cycles i think firefox 3 36 was like this huge release that
[1940.26 --> 1945.98]  took forever and chrome was frustrated by this and they came up with this idea of the six-week release
[1945.98 --> 1951.30]  cycle and the way that that works is that every six weeks you take every time you add a new feature
[1951.30 --> 1956.40]  you add it behind a feature flag so it's encapsulated and every six weeks you decide what new features
[1956.40 --> 1961.72]  can make it onto the beta branch and every six weeks after that you move things from the beta branch to
[1961.72 --> 1966.28]  the release channel and the way that the way that this works is it allows people to be very very
[1966.28 --> 1970.58]  aggressive on the master branch they can do whatever they want they can add whatever features they want
[1970.58 --> 1976.68]  they can not break on the web but they can they can do things that are aggressive but that doesn't
[1976.68 --> 1981.52]  necessarily directly affect the next release that requires more thought about stability more thought about
[1981.52 --> 1986.58]  deprecations and things like that and so when we started when we hit 1.0 i sort of saw that we had
[1986.58 --> 1992.84]  the same problem and we adopted the six-week release cycle pretty much verbatim from chrome and firefox
[1992.84 --> 1997.26]  for ember and actually the rust project also recently announced that they're going to do the same thing so i
[1997.26 --> 2002.28]  think there's something to it if you're if you really care about balancing these two priorities of
[2002.28 --> 2008.74]  how to keep things stable and not break all the time but also keep things moving the idea of there's just
[2008.74 --> 2012.74]  this rhythmic cycle and every six weeks your features either made it and if they didn't make
[2012.74 --> 2017.12]  it they're just on the next it the chrome team calls us the train model so you either make the
[2017.12 --> 2021.70]  train or you're on the next train the level of pressure is super low people get their work done i
[2021.70 --> 2027.12]  haven't had it seems like you if you ship every six weeks the level of pressure would be insane but
[2027.12 --> 2031.90]  actually ember has been the least pressure that i've ever felt on an open source project for shipping in
[2031.90 --> 2036.94]  my entire career and that's because it's just you know that you can make the next one yeah you fall behind
[2036.94 --> 2040.28]  on a feature and instead of saying well we're going to push back the release and everyone has
[2040.28 --> 2044.22]  to wait you know weeks and weeks and weeks to get access to the bet get the benefit for all stuff
[2044.22 --> 2048.96]  that's already done well you know i don't get this feature done today but it'll be out within six
[2048.96 --> 2053.12]  weeks so and you're thinking a lot more about individual features than you are about big releases
[2053.12 --> 2060.80]  which i think is pretty awesome i want to talk a bit about the the big bets because sometimes you say
[2060.80 --> 2066.30]  bets it's sort of like you're not really sure and i guess to a degree maybe you weren't very sure so you
[2066.30 --> 2071.06]  you play some pretty decent bets 2014 that that worked out well and then some of those bets are
[2071.06 --> 2075.00]  kind of playing into what you're going to do with 2.0 can you talk a bit about um the work you did on
[2075.00 --> 2081.54]  the cli and eventually how es6 models will become first class citizens and in that respect so so i've
[2081.54 --> 2089.80]  been working on es6 modules for a couple of years um i'm i'm on tc39 and i was i joined the champion team
[2089.80 --> 2096.00]  you should explain what tc39 is yes absolutely so tc39 is it stands for technical committee 39 which
[2096.00 --> 2100.76]  sounds like something out of the central bureaucracy in futurama um that's like saying
[2100.76 --> 2107.86]  that's like saying el nino is spanish for the nino yes exactly exactly it's just the 39th
[2107.86 --> 2113.92]  technical technical committee that exists uh in ecma which i don't sense for like european computer
[2113.92 --> 2118.42]  manufacturing association or something like that anyway so that committee is responsible for making
[2118.42 --> 2123.78]  javascript and i joined the group of people working on the module spec pretty early uh not early in the
[2123.78 --> 2129.00]  module spec lifetime but i think early in people's consciousness about es6 modules existing and one
[2129.00 --> 2133.76]  of the first things that i really wanted was i said well modules are somewhat involved thing at the time
[2133.76 --> 2138.90]  modules didn't support single export or default export um and a bunch of other stuff and i said
[2138.90 --> 2142.48]  i think it's really important that we actually start getting some real world usage of modules
[2142.48 --> 2148.58]  so that what we feed back into the es6 process it has reality so i wrote a really bad transpiler
[2148.58 --> 2155.86]  for es6 modules to amd um and very early on both because i was a big believer in modules being a
[2155.86 --> 2160.70]  thing and because i really wanted to make sure that the thing that we shipped in out of javascript was
[2160.70 --> 2167.74]  good uh i moved a lot of the ember community over to using es6 modules and that was definitely a big
[2167.74 --> 2172.76]  bet because i think the whole even today the module ecosystem is heavily fragmented and there was a
[2172.76 --> 2179.72]  at the time there was this meme that well like tc39 made it so clearly it's going to fail everyone
[2179.72 --> 2185.56]  should just use common js modules and so i really just wanted to make sure that the thing that actually
[2185.56 --> 2192.22]  shipped was good was a good quality thing so we did that um some of the very earliest adopters of es6
[2192.22 --> 2198.18]  modules in the ember community really drove what ended up being the the es6 spec which i think is
[2198.18 --> 2202.74]  quite good now um basically has many of the features that people come to expect from node
[2202.74 --> 2209.62]  modules and i think along that process so basically before es6 modules were a thing it was pretty easy
[2209.62 --> 2214.64]  to just copy and paste some code put it into into a file and sort of develop the same way that most
[2214.64 --> 2219.82]  people developed and maybe concatenate at the end as a final build step but along basically as we added
[2219.82 --> 2224.62]  es6 modules it became clear that everybody who used es6 modules was going to need a build chain
[2224.62 --> 2230.20]  and so um stephan penner started to work on this thing called ember app kit and ember app kit was
[2230.20 --> 2234.88]  literally just a grunt script and a bunch of scaffolding and you would clone this grunt repo
[2234.88 --> 2240.90]  and this it sounds kind of lame um in retrospect but first of all having like one tool that everyone
[2240.90 --> 2247.52]  uses is great but second of all having um have having a thing that you're iterating on even if it's
[2247.52 --> 2251.46]  not the best thing in the world gives you a sense of what actually is the requirement so we spent
[2251.46 --> 2256.52]  i don't know like six months or a year uh iterating on ember app kit just to get a sense of what is
[2256.52 --> 2261.90]  actually the requirements and then more recently this year we moved to we moved all that learning
[2261.90 --> 2268.82]  into a more abstracted thing that you could download install update um unlike ember app kit and that
[2268.82 --> 2273.80]  became ember cli and i think just having like a central place where people could say like here is my
[2273.80 --> 2280.12]  build process it involves es6 modules and concatenation and maybe like hashes for so for cache busting
[2280.12 --> 2285.98]  and and you start with that set of things and then before long you have the add-on ecosystem you have
[2285.98 --> 2290.94]  uh additional tools you have like proxies pointing at your server you have all these additional workflow
[2290.94 --> 2294.38]  tools basically you get this you have a central thing which is like how you build an ember app
[2294.38 --> 2300.08]  and that ended up being it started with a little tiny kernel of like let's start getting more let's get
[2300.08 --> 2305.14]  into a modules world instead of a globals world and it has expanded more and more into like the way that
[2305.14 --> 2310.34]  people think about building ember applications and it's really fast i think it's really fast and is
[2310.34 --> 2316.46]  such a huge productivity booster stuff that people would spend literally weeks setting up and tailoring
[2316.46 --> 2323.28]  for their app now you get it in in seconds and in fact i haven't asked for anyone listening who may
[2323.28 --> 2328.80]  have tried ember before let's say a year or two ago and maybe it wasn't to your taste try it again with
[2328.80 --> 2334.38]  ember cli because for me this has just totally changed how i develop web applications i'm extremely
[2334.38 --> 2339.66]  excited about it yeah and by the way tom says literally weeks and it sounds like an exaggeration
[2339.66 --> 2344.70]  yeah not exaggeration yeah we've worked with clients where we're like there for three months and we're
[2344.70 --> 2349.48]  there's like two weeks later people are still discussing like should we use grunt or gulp or
[2349.48 --> 2356.16]  whatever and and there's like these huge meetings with all the quote-unquote stakeholders it's like oh my
[2356.16 --> 2360.54]  god like this is totally a solved problem why are we discussing this over and over i think especially
[2360.54 --> 2365.34]  rails developers will appreciate ember cli because i've i've talked to several rails developers
[2365.34 --> 2372.22]  self-identifying rails developers who told me i thought that i just hated javascript but then i
[2372.22 --> 2376.46]  tried to use ember cli and i realized that a lot of the stuff that i love about rails isn't inherent
[2376.46 --> 2381.52]  to ruby that i can have that same or similar experience in javascript too yeah i think this is
[2381.52 --> 2387.48]  actually a lesson that go made stark and i work on rust also and rust sort of copied which is like
[2387.48 --> 2391.62]  which is that people don't necessarily think that carefully about workflow tools but having
[2391.62 --> 2397.60]  amazing workflow tools sort of baked into the experience is pretty awesome because it's not
[2397.60 --> 2400.78]  like oh well i can just build my own workflow tools because having to build your own workflow
[2400.78 --> 2405.76]  tools is kind of like it's like peeking under the skirt right it's like oh now i have to think about
[2405.76 --> 2411.06]  all this stuff as opposed to okay i want to generate some docs here i have a tool command i generate
[2411.06 --> 2415.96]  some docs and just like having that work is pretty nice i'm gonna say friend of the show justin
[2415.96 --> 2422.60]  who i think we had on a few episodes back uh doing lineman js i saw him in your guys's uh rfc
[2422.60 --> 2426.96]  comments pretty excited about uh ember cli and what you guys are up to with that so that's a
[2426.96 --> 2432.00]  i think that's a big win here's a guy who cares a lot about build tools and command lines and that
[2432.00 --> 2437.36]  kind of thing yeah no lineman is is awesome and i think of ember cli is basically an evolution of like
[2437.36 --> 2443.16]  okay lineman is awesome it embraces a lot of these ideas what can we do if we bake in even more
[2443.16 --> 2447.28]  integration with the framework i mean to be honest bridging build tools on the front end to be honest
[2447.28 --> 2452.76]  one of the things that really really hurt the early ember build tools uh efforts and i think
[2452.76 --> 2458.10]  hurts a lot of other efforts as well is that the way most people start by building build tools
[2458.10 --> 2463.18]  rebuilds everything all the time or may end up rebuilding a lot every time you make any changes
[2463.18 --> 2470.16]  and i think gulp tries to deal with this and it's largely successful with some problems um but grunt
[2470.16 --> 2474.98]  doesn't solve it at all and a lot of people will build tool tool chains on top of grunt and they'll
[2474.98 --> 2480.42]  they'll have a whole you'll demo it they'll go to meetups they'll build small projects with it and
[2480.42 --> 2484.86]  then you start getting people trying to build bigger things on top of it and you're just like embedded
[2484.86 --> 2488.60]  inside of a big company and all of a sudden everything's super slow and there's not really
[2488.60 --> 2493.74]  a lot of feedback to say okay well maybe grunt was like not the best idea so we actually used grunt with
[2493.74 --> 2498.08]  the original ember app kit effort and it just became obvious very quickly that we needed something
[2498.08 --> 2503.38]  that would allow you to do incremental rebuilds which is it sounds obvious but for some reason
[2503.38 --> 2507.52]  in javascript the idea that you have an incremental rebuild that when you make a change to one thing
[2507.52 --> 2514.06]  you should only cause a compilation of the things that changed is still not conventional wisdom i would
[2514.06 --> 2519.22]  say and that was i would say getting to that point goes from being something that demos well and people
[2519.22 --> 2523.82]  like to play with and you know go to meetups and show and goes to something that can be a real
[2523.82 --> 2527.70]  productivity booster is actually solving that seemingly boring technical problem
[2527.70 --> 2532.72]  yeah let's pause the show for a minute give a shout out to a sponsor digital ocean
[2532.72 --> 2539.96]  simple cloud hosting built for developers in 55 seconds you'll have a cloud server with full root access
[2539.96 --> 2546.26]  and it just doesn't get any easier than that pricing plan started only five bucks a month for half
[2546.26 --> 2555.10]  gig of ram 20 gigs of ssd drive space one cpu and one terabyte of transfer that's a lot for five bucks a
[2555.10 --> 2561.96]  month digital ocean also has data centers all across the world new york san francisco amsterdam
[2561.96 --> 2567.80]  singapore and their newest region london you can easily migrate your data between those regions making
[2567.80 --> 2575.36]  your uh data always closest to your users use the promo code changelog november in lowercase it's
[2575.36 --> 2581.36]  important that you use lowercase changelog november to get a ten dollar hosting credit when you sign up
[2581.36 --> 2585.22]  head to digital ocean.com right now to get started and back to the show
[2585.22 --> 2592.08]  it seems like you guys have learned a lot from the community over the last couple years uh who do you
[2592.08 --> 2597.42]  touched on it with react you also said in the post that uh you saw from angular that easy onboarding
[2597.42 --> 2602.36]  is a big win for for getting people on board it sounds like the cli is going to help out in that effort
[2602.36 --> 2606.96]  tom maybe speak to the virtual dom what you've learned from react and how you guys are going to
[2606.96 --> 2612.86]  kind of get that stuff into ember here soon sure so i think a lot of the people this kind of gets
[2612.86 --> 2616.42]  back to the discussion we were having a little bit earlier about why do people still prefer to write
[2616.42 --> 2623.28]  server rendered apps and uh one thing that i didn't mention is that the programming model is just so easy
[2623.28 --> 2628.86]  right if you think about how people build uh server rendered apps request comes in you will get your
[2628.86 --> 2632.88]  model data out of the database you hand it over to your view layer to render and you return that
[2632.88 --> 2638.76]  output and that's it and every time you handle a new request because http is stateless you get kind of
[2638.76 --> 2647.28]  a uh you start from scratch conversely things like ember and angular have these two-way data bindings
[2647.28 --> 2654.90]  right and it's really easy to end up in especially a larger sophisticated application which is stateful
[2654.90 --> 2659.30]  so as the user's looking at it it's not like the state is getting reset you're constantly having
[2659.30 --> 2663.94]  to keep uh everything in sync yourself and you're making these changes to these objects and it's really
[2663.94 --> 2668.86]  easy unless you're diligent about it to end up with an application where you can't yourself reason about
[2668.86 --> 2674.68]  how data flows through it uh but in order to make two-way bindings work of course you kind of have to do
[2674.68 --> 2684.50]  that so to me the the brilliance in react is bringing back a programming model that is as simple as
[2684.50 --> 2691.14]  server rendered apps so for example you just set your model you know let's say you have a web socket
[2691.14 --> 2697.56]  and it gets uh new versions of a of a model streamed in every you know 30 seconds well all you have to
[2697.56 --> 2704.40]  do is take that model and say okay replace the old model with the new one and because react uh does
[2704.40 --> 2709.08]  this diffing strategy you basically re-render the entire app as though it was server rendered right it's
[2709.08 --> 2713.86]  not just set the model to a new model it's basically i want to replace this little bit of
[2713.86 --> 2718.58]  state and also re-render everything right i don't i don't want to have to figure out how to tunnel
[2718.58 --> 2723.12]  through the specific change just re-render the universe right so here's this change sounds like
[2723.12 --> 2726.62]  it would be slow i was gonna say doesn't that sound slow to re-render everything for a small change so
[2726.62 --> 2731.60]  that's the brilliance of of react i think is that they've uh figured out that javascript engines are
[2731.60 --> 2736.74]  so fast that you can quickly implement these diffing algorithms that go through and and quickly find
[2736.74 --> 2743.68]  the changes and reflect those uh from the virtual dom into the real dom very very cheaply right so so that
[2743.68 --> 2748.56]  to me is the core of react i think a lot of people like to reason about why it's becoming very
[2748.56 --> 2754.00]  popular but to me that's the nut of it is that it makes front-end programming feel as simple as it
[2754.00 --> 2759.20]  was when you were writing your rails app right and i think just to be clear i think there are
[2759.20 --> 2764.04]  definitely edge cases with that where you're re-rendering too many things and there's also
[2764.04 --> 2769.14]  problems with how do you know when you get a model from the server what exactly you poke at to get it
[2769.14 --> 2775.30]  to re-render um but i think the reason why people like react is that so many cases when you're
[2775.30 --> 2780.68]  building web applications are sort of these intra-component or inter-component cases where
[2780.68 --> 2785.02]  you have a little cluster of components and all the communication and all the state changes happen
[2785.02 --> 2790.40]  inside of this little cluster of components and you can get so far in react just by saying okay i you
[2790.40 --> 2795.20]  know i have this little widget the widget changes some state and re-render the little cluster of
[2795.20 --> 2800.04]  components that i'm inside of and don't have to worry about how to you know figure out how to
[2800.04 --> 2806.74]  tunnel some events through a data binding i honestly both ember and react and angular fell into a trap
[2806.74 --> 2812.06]  of even though both ember and angular have the notion of both events and data bindings i think data
[2812.06 --> 2817.62]  bindings feel so cool for cases where they're really appropriate that people start tunneling events
[2817.62 --> 2823.26]  through data bindings and that i think honestly when i look at the real critiques that a lot of react
[2823.26 --> 2827.50]  people have about ember and try to understand okay well you were an ember developer you were reasonably
[2827.50 --> 2832.36]  productive but you feel you find yourself way more productive and react what is what is happening
[2832.36 --> 2836.34]  one of the things that i see over and over again and what and this is something that really played
[2836.34 --> 2842.94]  into the ember 2.0 plan is that people are abusing i say abusing that sort of blames the victim here
[2842.94 --> 2848.30]  right i people are uh using a tool that that we're telling them is good which is two-way data
[2848.30 --> 2854.06]  bindings to express something that's fundamentally an event and i think a big part of ember 2.0 is to
[2854.06 --> 2860.70]  refocus energy away from two-way data bindings as the primary method of communication and move towards
[2860.70 --> 2866.48]  events as the first way that you think about it and you're starting to use data bindings one or two-way
[2866.48 --> 2870.80]  when they become appropriate for cases where they're appropriate and have them be sort of things that
[2870.80 --> 2875.76]  you start opting into as the situation yeah makes them i think that's definitely a mistake that we we
[2875.76 --> 2882.02]  made we added almost too much sugar around two-way data bindings and that kind of led people down
[2882.02 --> 2887.20]  this path of using them as an event bus it's kind of this really hacked together event bus and i think
[2887.20 --> 2891.28]  that was a lesson that maybe we actually over learned from angular because i remember watching
[2891.28 --> 2895.48]  presentations where people would show angular be like oh look at how easy it is to set up this two-way
[2895.48 --> 2900.22]  binding and i got i think i got a little jealous you know how how easy it was because that easy on
[2900.22 --> 2904.16]  ramp was so important and at the time two-way bindings were you kind of had to have them it was like
[2904.16 --> 2909.16]  you know um you had to have them even to participate in the in the competition but i think one thing
[2909.16 --> 2915.02]  that we should keep in mind is that this is a sad thing about the javascript community is that
[2915.02 --> 2919.80]  everyone's always looking for the one true solution so first it was two-way data bindings and now it's
[2919.80 --> 2927.54]  one-way data flow events right up actions down and it could be trans what is it trans uh it's the
[2927.54 --> 2934.14]  thing that came from the closure guys that transducers transducers right uh yeah could be channels or
[2934.14 --> 2937.80]  everyone's always looking for the one true solution that's what makes it tough about the
[2937.80 --> 2941.74]  javascript community there's always like the right way of building apps today and if you're not that
[2941.74 --> 2946.96]  way it's like you know get out but i think what's way more exciting and something that is like way
[2946.96 --> 2950.90]  more fun as a programmer and this is something that like i really love about the rust community actually
[2950.90 --> 2956.14]  is trying to trying to find contextually appropriate solutions so yes channels are great in some
[2956.14 --> 2960.24]  cases maybe transducers are great in some cases two-way data bindings totally great when you're
[2960.24 --> 2964.52]  building a form and you're just trying you just want to make sure that when you type something it
[2964.52 --> 2969.58]  actually updates the object and actually you don't have to have a callback but but trying to say like
[2969.58 --> 2974.14]  okay well i had situations where two-way data bindings were broken switch all the way to events i had a
[2974.14 --> 2977.80]  problem where events were broken switch all the way to two-way data bindings that's basically what we
[2977.80 --> 2983.16]  constantly see in the javascript community and it's to me by far the most frustrating thing yeah yeah but i think
[2983.16 --> 2990.70]  this is actually in my opinion the secret to ember's longevity is that you and i spend an inordinate
[2990.70 --> 2995.34]  amount of time talking about other frameworks and really analyzing them you know people really like
[2995.34 --> 3000.84]  this aspect people really hate this aspect well why let's try to really truly understand and we
[3000.84 --> 3006.52]  always incorporate that and fold that back into ember and i think that's why it always feels like uh you
[3006.52 --> 3012.34]  know i mean i think community is naturally kind of uh can kind of uh butt heads sometimes and i think that's
[3012.34 --> 3016.32]  why it was first it was ember versus backbone who's going to win ember versus backbone then it was like
[3016.32 --> 3019.46]  ember versus angular who's going to win ember versus angular and now a lot of people are like oh ember
[3019.46 --> 3024.56]  versus react who's going to win but the truth is we're going to keep we're shameless about stealing
[3024.56 --> 3028.82]  great ideas we still we stole some great ideas from backbone stole some great ideas from angular
[3028.82 --> 3034.82]  and now for ember 2 we're stealing a ton of great ideas from react and so in my mind the strength of
[3034.82 --> 3041.08]  ember and the reason why it has this longevity is because we don't have a problem saying you know what the
[3041.08 --> 3044.86]  way that we were doing before was bad let's do it this new way and let's make sure that everyone
[3044.86 --> 3048.62]  who's building an app today can get there that they have a path for transitioning but i think i think
[3048.62 --> 3054.36]  also to be clear we don't go and we don't whip around and say oh everything we were doing is totally
[3054.36 --> 3059.64]  broken i think there are totally legitimate use cases for two-way data bindings and totally legitimate
[3059.64 --> 3066.34]  use cases for all these things so it's more about finding what kate basically people got got kick
[3066.34 --> 3072.22]  puppy syndrome around two-way data bindings for good reason right and the answer is not i think
[3072.22 --> 3076.50]  often people throw the baby out with the bath water and every six months there's a new baby that's being
[3076.50 --> 3082.86]  thrown out with new bath water a lot of babies well it just seems like you're learning from the community
[3082.86 --> 3086.70]  well here i mean you say it well in the spot where you say learning from the community where you say we're
[3086.70 --> 3091.34]  well aware that we don't have a monopoly on good ideas that you'll incorporate things as they come along so
[3091.34 --> 3096.02]  it just kind of makes sense that that's the direction you head yep let me say this so you know
[3096.02 --> 3100.14]  obviously at the changelog like we've been watching we kind of just keep our thumb on the pulse it's
[3100.14 --> 3105.14]  what we do um so i've been watching your ember grow and i've been a part of the angular community
[3105.14 --> 3110.74]  and the backbone community and the ember community kind of on the fringes um i remember the old i think
[3110.74 --> 3115.24]  even you were on maybe it was javascript jabber back in the day with jeremy ashkenes talking about
[3115.24 --> 3120.44]  one-way versus two-way and for me the most surprising thing about your announcement here and i think the most
[3120.44 --> 3126.42]  um impressive actually is what you say here after a few years of having written ember apps
[3126.42 --> 3130.46]  we have observed that most of the data bindings and the template engine do not actually require
[3130.46 --> 3136.94]  two-way data bindings and just the the ability to say you know what it's not like it was a terrible idea
[3136.94 --> 3141.62]  but at the end of the day we're willing to grow and we're willing to say you know what this this is
[3141.62 --> 3145.66]  right now this is actually a better best practice we're not going to hold on to that old idea
[3145.66 --> 3150.86]  because it was yeah jeremy jeremy pulled that snippet and tweeted literally lol
[3150.86 --> 3158.72]  well it had to feel probably not too bad i mean so i i think what's kind of the mistake that we
[3158.72 --> 3162.38]  made is actually a little bit subtle and the mistake that we made was that at the time we said
[3162.38 --> 3167.62]  well there's one-way by data bindings and two-way data bindings and if you don't use a two-way if you
[3167.62 --> 3171.84]  use a two-way data binding without setting then it's just a one-way data binding so we could we
[3171.84 --> 3176.08]  thought we could simplify the model by just saying they're all two-way and just if you don't want to
[3176.08 --> 3180.76]  mutate something and don't and the mistake that we made there was that we didn't realize the
[3180.76 --> 3186.56]  importance of uh seeing from the point where you're actually writing out a component whether or not it's
[3186.56 --> 3191.92]  going to be mutated right so we basically from our perspective we said you know a one-way data binding
[3191.92 --> 3197.56]  is just a two-way data binding that isn't being set that isn't being mutated but that just wasn't a
[3197.56 --> 3202.92]  good programming model right people people would do something that they thought was a immutable data
[3202.92 --> 3207.46]  binding they would try to give some value to somebody expecting not to get set and then some
[3207.46 --> 3211.18]  other programmer somewhere else or some other third-party library all of a sudden would start
[3211.18 --> 3215.34]  mutating something and they would people would just get confused about what was going on so i think
[3215.34 --> 3221.86]  saying it's not enough to say it's just a two-way data binding that you didn't set let's explicitly say
[3221.86 --> 3226.06]  that you should opt into cases where you want it to be immutable i think ends up being good i think
[3226.06 --> 3232.42]  that's actually a lesson that we learned from rust in some ways yeah well we stole the syntax from
[3232.42 --> 3236.52]  rust but basically rust a lot of stealing happens sounds like uh sounds like we need to get you back
[3236.52 --> 3241.70]  on to talk about rust yahuda yeah seem pretty excited about it i know we were talking to steve klabnik who's
[3241.70 --> 3246.16]  a changelogger to have him come on and talk about rust so maybe we'll have both of you on sometime i think
[3246.16 --> 3252.84]  we're one of the first production users of rust actually yeah i think open dns is maybe the ape in
[3252.84 --> 3257.58]  earlier okay we're number two yeah happy to be number two we're used to it
[3257.58 --> 3265.32]  one last one last question just on the roadmap um back when i was using ember my biggest problem with
[3265.32 --> 3272.42]  it was just the how immature ember data was um sounds like it's still not hit a 1.0 is that true
[3272.42 --> 3279.08]  and what's the plans with ember data uh so we have not hit a 1.0 yet but we are very close
[3279.08 --> 3286.50]  um we kind of had to do a big rethink on ember data i think one thing that you'll see from our
[3286.50 --> 3290.94]  history is that we have a very strong commitment to semantic versioning and i think at this point
[3290.94 --> 3295.58]  you can trust us that when we declare 1.0 we we mean it that we're not going to introduce breaking
[3295.58 --> 3299.38]  changes uh unfortunately that does mean that we pack as many breaking changes as possible
[3299.38 --> 3305.08]  into not as possible but into the free 1.0 in other words squeeze into this yeah well we're just not
[3305.08 --> 3308.46]  that random yeah we're just not going to ship something that we're not proud of and that we
[3308.46 --> 3311.60]  don't think we don't feel if we don't feel confident that we can maintain it for the next
[3311.60 --> 3317.08]  you know two three four five years ten years we're just not going to ship it um and so finally with
[3317.08 --> 3321.38]  ember data i can confidently say that we've we've reached that point there's just a few little things
[3321.38 --> 3326.86]  that we need to button up before we declare 1.0 um but probably the biggest thing was trying to solve
[3326.86 --> 3331.18]  this issue of relationships it turned out i don't think we really fully appreciated this when we got
[3331.18 --> 3335.92]  signed when we signed up for ember data because on on the surface it looks just like an orm which
[3335.92 --> 3341.60]  you know looks like active record or any of these things um but it turns out to be an order of
[3341.60 --> 3346.74]  magnitude harder problem orms are pretty well understood because as it turns out orms have a
[3346.74 --> 3351.36]  synchronous access to the database you block the request while you access the database and your orm works
[3351.36 --> 3356.90]  but with ember data what i don't think we fully appreciated was that we were basically getting
[3356.90 --> 3364.06]  ourselves into a distributed computing problem where you have the source of truth on some server
[3364.06 --> 3370.94]  somewhere on some server on some database and at any given time you only have a small subset of that
[3370.94 --> 3376.10]  truth and it streams in over time and it can change and so you simply cannot get access to any
[3376.10 --> 3381.76]  information that you don't already have synchronously right yeah just impossible so we had to build a very
[3381.76 --> 3387.12]  robust system for dealing with this ambiguity and the fact that we could never have the full set of
[3387.12 --> 3392.34]  truth at once guaranteed and to be honest we tried the reason why ember data was so unstable was that we
[3392.34 --> 3398.94]  tried a bunch of different approaches and every essentially every approach had its ups and downs and we
[3398.94 --> 3406.92]  sort of move towards an approach that works but it it was not i think people people expect a much simpler
[3406.92 --> 3413.16]  kind of problem than it is yeah and i think if you look at the ecosystem uh there are libraries for
[3413.16 --> 3421.22]  like backbone has some very very uh simple i guess the charitable worth use uh data syncing built into
[3421.22 --> 3426.56]  it uh there are some libraries for angular is like rest angular and uh there's like a built-in resource
[3426.56 --> 3432.06]  dollar resource um but the thing that none of them tackle that was by far the biggest challenge is this
[3432.06 --> 3437.02]  notion of relationships so you know let's say i'm writing some blog software and i have a post and
[3437.02 --> 3441.88]  a post can have many comments that seems like the simplest thing in the world if you're a rails
[3441.88 --> 3447.24]  programmer a django programmer but actually modeling that building software that was flexible enough to
[3447.24 --> 3452.40]  handle that case was so difficult so i just i just want to be clear like obviously a lot of things have
[3452.40 --> 3458.10]  the notion of relationships in them right i think what tom is meaning here is that uh what a lot a lot of
[3458.10 --> 3463.26]  applications start off and they essentially download all the data they're ever going to see up front and
[3463.26 --> 3468.96]  they write you can easily write code that assumes that if you have post has many comments right and
[3468.96 --> 3472.48]  you're starting out that the comments were just downloaded together with the posts right with the
[3472.48 --> 3476.68]  posts right but then over time you're like well i have a huge blog i don't want to download every
[3476.68 --> 3480.58]  single comment so you break it apart so now your comments are asynchronous and then later on you
[3480.58 --> 3485.22]  discover and in ember this is not even avoidable you want to allow people to go directly to a
[3485.22 --> 3491.14]  a particular post right and now so basically the order that you may download the data is totally
[3491.14 --> 3496.24]  random and this is not uh people think oh well i just won't deal with that but not have not being
[3496.24 --> 3501.00]  able to link directly to something in an app in a javascript application is basically just a non-starter so
[3501.00 --> 3507.22]  very rapidly without even trying very hard you get into a situation where you have objects with
[3507.22 --> 3512.88]  relationships where the order that they come in is async is both asynchronous and not exactly determined
[3512.88 --> 3516.64]  but where you want them to be linked together and you want to be able to make changes to either
[3516.64 --> 3520.72]  side and have them reflected on the other side and basically the problem that i just described is the
[3520.72 --> 3527.54]  problem that we've been working on solving in ember data for the past 18 months before we tell off the
[3527.54 --> 3533.62]  the call and go into our super awesome question which is who is your programming hero to each of you
[3533.62 --> 3541.04]  uh maybe it might be best to close off by kind of summarizing what version 2.0 marks for ember i know
[3541.04 --> 3545.24]  you summarize it pretty well here in your rfc so i'm just sort of using that as a as a bullet plate
[3545.24 --> 3549.92]  either of you can take that but you know we got the jareds out there who've used the 1.0 and then
[3549.92 --> 3555.16]  i've used it all along but what's 2.0 and what's the onward uh direction so i'll give an i'll give an
[3555.16 --> 3560.06]  inarticulate answer and maybe tom can correct me if i get anything wrong but i think i think what 2.0 is
[3560.06 --> 3565.96]  is us taking a lot of efforts that have been going on in the community to build a full a complete
[3565.96 --> 3571.68]  front-end stack and making them part of ember itself so we have ember cli we have uh hopefully
[3571.68 --> 3577.30]  ember data and other pieces of the ecosystem and the ember inspector and basically saying these are
[3577.30 --> 3581.18]  all part of the first class experience of ember that every new ember developer should use
[3581.18 --> 3588.60]  yeah and i think uh kind of that goes along with that is that we really want to make ember as
[3588.60 --> 3592.68]  accessible as possible to the widest range of people uh widest range of people as possible
[3592.68 --> 3600.00]  and that means dropping the learning curve so ember 2.0 is really about thinking okay well we
[3600.00 --> 3603.96]  have two concepts here but i think there's one that can fit both scenarios so let's get rid of that
[3603.96 --> 3609.60]  extra concept uh basically really distilling it down to the essence of the framework as we've kind
[3609.60 --> 3615.12]  of as it's become more apparent over the past two years well we uh we always get some great answers
[3615.12 --> 3621.28]  when we ask these questions but uh feel free to to share a couple or just one uh it's really up to
[3621.28 --> 3627.52]  you but uh tom i'll start with you on can't pick each other though yeah that's cheating is that true
[3627.52 --> 3633.32]  actually i if i can get sentimental for a moment i have to say that yehuda is definitely my programming
[3633.32 --> 3639.36]  hero which is why it's such a privilege to get to work with him each day and i know that sounds like
[3639.36 --> 3644.96]  really biased because we started this company together but i have learned so much uh from him
[3644.96 --> 3649.98]  because i think he does a really awesome job distilling so many different people like he's
[3649.98 --> 3655.26]  constantly quoting maths to me he's constantly quoting dhh to me gang of four you know all of
[3655.26 --> 3660.88]  these historical things i have no idea how it keeps them all in his head so well yes i may be slightly
[3660.88 --> 3667.68]  better looking than yehuda absolutely only slightly that's gracious at the at the end of the day i i i have
[3667.68 --> 3670.88]  learned so much and for me it's a privilege to come into work every day and get to work with him
[3670.88 --> 3678.64]  sorry i feel like you need in another person no i think it's true it's you bro all right uh now i
[3678.64 --> 3684.82]  feel no it's not me now you're my how awesome that is a first though to have the hero on the show with
[3684.82 --> 3691.64]  the person who says it so sounds legit though it sounded sincere yeah it did i appreciate that tom
[3691.64 --> 3697.82]  all right who's your who's your hero so so my program hero is actually mats and i say this for
[3697.82 --> 3703.50]  a couple reasons so first of all i think mats is extremely uh underrated and i think part of that
[3703.50 --> 3710.20]  is the fact that mats is japanese and doesn't and speaks english uh with difficulty and he gets a lot
[3710.20 --> 3715.88]  of shit thrown his in his direction and i think he i could just imagine that it must get to him
[3715.88 --> 3721.02]  and but he doesn't he's not out on twitter battling the fight so people are just constantly
[3721.02 --> 3725.96]  talking about him as basically incompetent a moron idiot it's worst language designer ever worst
[3725.96 --> 3730.84]  implementer ever and i feel like uh people should give him a little more credit for building a
[3730.84 --> 3736.92]  language that is as successful as it is but i think i think other uh beyond that i think i looked i look
[3736.92 --> 3743.52]  at ruby 1.9 and i look at python 3 and people really really do not give mats enough credit for
[3743.52 --> 3748.94]  thinking through the requirements of making such a big breaking change um in a way that would get
[3748.94 --> 3755.52]  adoption and i i this is a topic for a whole different discussion but i think i think mats
[3755.52 --> 3761.34]  really does a really good job of thinking about how people use his software having some level of
[3761.34 --> 3766.76]  empathy for it and thinking about what you have to do to actually get people to move along um i'm not
[3766.76 --> 3772.00]  going to say max has never made any mistakes in his life obviously uh everybody building something as
[3772.00 --> 3778.16]  big and complicated as ruby makes mistakes and certainly mats is not the best vm author in the universe
[3778.16 --> 3783.60]  but i think mats has done a really great job of thinking about why people use software um my
[3783.60 --> 3790.28]  favorite uh my favorite thing he ever wrote or or presented is uh 2003 oscon talk which i can get you
[3790.28 --> 3797.76]  a link to where he basically talks about how uh just like human language inter uh controls how we
[3797.76 --> 3803.18]  think how human language makes us think in a particular way uh how programming language can do that
[3803.18 --> 3808.56]  and he talks about how he designed ruby to help people think clearly when they're programming and i i just
[3808.56 --> 3814.28]  think people don't give matt a lot of credit for being a really good language designer um when it comes
[3814.28 --> 3820.12]  to ruby i can say jared and i were just a keeper be weird in austin and uh it might have been a little
[3820.12 --> 3826.22]  bit biased because it was a ruby conference but we had uh we have this video coming out sometime soon
[3826.22 --> 3831.24]  called beyond code where we set pretty much interviewed um as many attendees as we possibly
[3831.24 --> 3837.38]  could on camera um so for once we're breaking into the video side of of i guess media creation but
[3837.38 --> 3843.68]  uh a resounding uh change jared the question was uh which software has changed your life the most
[3843.68 --> 3849.00]  summarizing that to a t but um everyone said ruby and all the things that was beautiful about the
[3849.00 --> 3855.70]  language so it's it's funny to hear you say how bad mask gets its criticism because he's japanese speaks
[3855.70 --> 3861.80]  slightly broken english and doesn't really translate that well but wrote a language that that helps
[3861.80 --> 3867.34]  programmers think in english so much better than they ever done before yeah and i think people just
[3867.34 --> 3873.16]  assume that a lot of a lot of people's success is is accidental and people i think say well maybe
[3873.16 --> 3878.08]  matt's in the right place at the right time but honestly reading that 2003 oscon presentation makes
[3878.08 --> 3882.48]  it clear to me that he was thinking very deeply very carefully about what he was trying to do
[3882.48 --> 3886.96]  we'll definitely get that that link in the show notes if you can dig that up and email it to us
[3886.96 --> 3892.00]  or text it to us or whatever let us know but uh we'll put that in the notes for sure well tom
[3892.00 --> 3898.42]  yahuda you guys are great um man i just sit back in awe you know tom you mentioned yahuda is one of
[3898.42 --> 3902.18]  your heroes i i don't often see my hero on here but you're definitely one of them yahuda because
[3902.18 --> 3908.12]  just the way you articulately explain what you do why you do it why the software should be a certain
[3908.12 --> 3914.10]  way and tom to what you mentioned on how he kind of um this isn't a yahuda party but
[3914.10 --> 3920.18]  but just the fact that like you you do you you quote the the greats you know so you you know
[3920.18 --> 3925.24]  take it like philosophers you keep those notes in your head you know to to make good software and you
[3925.24 --> 3930.26]  do it well if i might say the thing that's really astounding to me about yahuda is how much he's willing
[3930.26 --> 3936.06]  to play the long game so there are all of these open source projects coming to fruition right now you
[3936.06 --> 3942.74]  know with broccoli ember cli ember data es6 modules javascript promises ember itself all of these
[3942.74 --> 3948.32]  things you know being there i've seen him working on this stuff for four or five years like to me
[3948.32 --> 3953.58]  yahuda has such a crystallized vision in his head of what web development should be like and he also has
[3953.58 --> 3959.66]  the unrelenting energy and patience to work with people who are pretty obstinate to make that vision
[3959.66 --> 3963.30]  come true and to me that's just like a really astounding thing that's a quality that not a lot of people
[3963.30 --> 3970.68]  have i yeah i hope in general that if people feel moved by it that they think about playing the long
[3970.68 --> 3974.66]  game a little bit more i think programming could use a little bit more of it well you said the web
[3974.66 --> 3978.76]  speed earlier like as if we should just constantly break stuff which is good to a degree if you're
[3978.76 --> 3986.06]  trying to you know push a product but uh you know we shouldn't be so whimsical about how we ship it
[3986.06 --> 3991.54]  should be with purpose and plan and but at the same time to use your fc as a good example of
[3991.54 --> 3996.16]  listening to the community and adopting what works best and admitting when we're wrong and
[3996.16 --> 4000.10]  making changes as needed for the better of the community so and you can definitely i think you
[4000.10 --> 4006.28]  can gain a lot more momentum like gaining momentum takes time yeah and and if you do it slowly and
[4006.28 --> 4012.56]  carefully you gain a huge amount of momentum where you can definitely you can sprint out ahead really
[4012.56 --> 4017.62]  quick and then lose momentum if every six months you're asking people to do a whole new thing
[4017.62 --> 4022.52]  well the jared's mentioned earlier what to get you back on to talk about rust steve's definitely
[4022.52 --> 4026.86]  that would be awesome that calls well we've been wanting to have a conversation for a while but uh
[4026.86 --> 4031.20]  before we close off i want to give a quick shout out to three different sponsors that make this show
[4031.20 --> 4039.20]  awesome and possible aside from the guests of course um pager duty uh hired.com and digital ocean
[4039.20 --> 4044.90]  we're obviously hosted on digital ocean love those guys pager duty um keeps me from having to get up
[4044.90 --> 4049.26]  deep at night you know the call goes to the right person and hired uh you guys just awesome as well
[4049.26 --> 4055.70]  but uh great show today guys uh next week uh the next show we have planned is with dave canada on
[4055.70 --> 4060.98]  buckets.io so hopefully that's a uh then hopefully it does actually uh be the next one in case we
[4060.98 --> 4067.02]  actually have a show in between now and then but um let's say goodbye y'all bye bye well thanks for having us
[4067.02 --> 4071.10]  you
[4071.10 --> 4077.64]  you
