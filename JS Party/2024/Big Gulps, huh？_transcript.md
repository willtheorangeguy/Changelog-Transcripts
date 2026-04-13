[0.00 --> 14.22]  you're listening to jsparty a weekly celebration of javascript and the web find us on the web
[14.22 --> 22.20]  at jsparty.fm on the fediverse at jsparty at changelog.social and of course wherever you get
[22.20 --> 28.62]  your podcasts just search for jsparty you'll find us thanks to our partners at fly launch your app
[28.62 --> 37.28]  near your users for peak performance fly makes it easy learn more at fly.io okay hey it's party time
[37.28 --> 48.30]  y'all what's up friends and party people i'm talking to you today about our friends over at
[48.30 --> 55.72]  clerk the complete suite of embeddable uis the full-on most comprehensive user management platform
[55.72 --> 63.60]  if you're using react or next js clerk is perfect for you embeddable uis flexible apis and admin
[63.60 --> 70.30]  dashboards to authenticate and manage your users and i'm here with clerk ceo colin sidoti colin give me
[70.30 --> 75.62]  the backstory why does clerk exist when we started clerk we were definitely frustrated that a lot of
[75.62 --> 83.42]  the authentication solutions both services or open source kind of didn't have a good ui built in and
[83.42 --> 88.72]  we would look at google's sign-in experience and google's user profile and it just had this like
[88.72 --> 95.38]  degree of polish and professionalism to it it just didn't come out of the box with everything else
[95.38 --> 101.70]  usually you start with just email password as the sign-in options and then you kind of have to add in
[101.70 --> 109.90]  extra modules to get all off on and you know in the user profile having a profile picture and
[109.90 --> 114.76]  setting up to a bay right it's like like all this extra work that you have to do and with clerk i
[114.76 --> 121.76]  think we really were inspired by stripe checkout where here's a checkout and it's great right like
[121.76 --> 126.80]  and we had this question of like why like why didn't that exist for auth really and so for clerk
[126.80 --> 132.50]  you drop in our components and it's really just a complete like end-to-end experience right out of
[132.50 --> 137.80]  the box with that high degree of polish high degree of professionalism that i think users have really
[137.80 --> 143.64]  come to expect these days okay so easy to drop in components really beautiful ui by the way i love
[143.64 --> 150.50]  it very nice clerk must be the most welcomed easy button when it comes to authentication good ui and
[150.50 --> 155.80]  all that right one of the most striking things you know still to this day i think clerk might be the
[155.80 --> 161.78]  only auth solution that comes with a user profile screen and it's so insane to think about because you
[161.78 --> 166.12]  need the user profile screen because that's where the user goes and they self-serve to set up to a bay
[166.12 --> 171.96]  and it ties back into the sign-in and so it's like we had to do that to be able to offer that
[171.96 --> 178.18]  experience but it's so bizarre to us auth depends so much on user profile yet most auth solutions don't
[178.18 --> 183.72]  include it and it's just this weird bizarre thing that never made sense to us and so approaching it
[183.72 --> 190.44]  from first principles we have it out of the box very cool so pixel perfect uis embedded in minutes
[190.44 --> 197.74]  react or next gs this is the easy button for you clerk is perfect for you it is a full-on comprehensive
[197.74 --> 204.26]  user management platform with as i said beautiful ui best of all they have pricing that scales with you
[204.26 --> 212.46]  they have a phenomenal free tier 10 000 monthly active users for free plus when you scale to a paid
[212.46 --> 217.64]  plan they have first day free this means you won't be charged for users who sign up and never return
[217.64 --> 230.24]  so that's phenomenal every feature you need now and as you scale get started at clerk.com at c-l-e-r-k.com once again clerk.com
[247.64 --> 262.20]  hello world it's your internet friends jared and k-ball just the two of us k-ball how you doing i'm doing
[262.20 --> 267.06]  all right not that often i get to spend this much quality time with you that's true just the two of
[267.06 --> 272.12]  us here what do you want to do just two of us well of course when it's the two of us we're gonna have
[272.12 --> 277.88]  break down javascript news right like that's what we do when we have our intimate time that is what
[277.88 --> 282.88]  we do in our free time when it's just the two of us zero typescript news today so you'll be happy
[282.88 --> 292.08]  to hear as our typescript aficionado is not here just me and you and we're talking html first so
[292.08 --> 300.00]  html first and first up on the docket it's another state of survey which we've covered from time to time
[300.00 --> 303.22]  this won't be the deep dive that we've done in the past where we spent an entire episode
[303.22 --> 311.32]  reviewing the state of but this is a state of html not state of javascript not state of css i believe
[311.32 --> 316.76]  there's a css one that we've done state of html you know you gotta give some html some love it is the
[316.76 --> 322.64]  bedrock of everything that the web is is it not i mean we gotta give it some love yeah absolutely i mean
[322.64 --> 326.10]  at the end of the day no matter how much javascript we put out there if the html isn't there
[326.10 --> 331.96]  what are they gonna do it's just a blank page so what is the state of html of course this is the
[331.96 --> 337.48]  annual survey i believe this is the second time they have done this one put on by our friend sasha
[337.48 --> 344.24]  grief and leah veru who's been on the pod a couple of times finding out what folks are using what
[344.24 --> 349.22]  they're not using and the full results we won't go through today you can check out the website which
[349.22 --> 354.40]  is linked up in the show notes but just a few items that i thought were of interest first of all
[354.40 --> 361.42]  under features being used there are questions around tooling which always piques my interest
[361.42 --> 367.56]  specifically site generators was highlighted which of these static or dynamic site generators do you
[367.56 --> 373.60]  regularly use cable did you look at the results or can i can i close you okay you know what the
[373.60 --> 379.92]  results are well i don't think anybody is surprised that next js dominates with almost 40 percent of
[379.92 --> 386.70]  respondents using this one regularly no surprise there necessarily i think what's more interesting
[386.70 --> 393.48]  honestly is if we so there's a set of these on here so there's next there's nuxt there's gatsby
[393.48 --> 400.00]  there's svelte kit these are all application frameworks right more than static site generators i think
[400.00 --> 407.66]  if we peel those away and look at what else is on there astro is kind of in the middle in a very fun way
[407.66 --> 415.54]  and they're doing great but astro eleventy jekyll and hugo all on there are more classic generators
[415.54 --> 423.50]  right exactly and you know it's neat to see jekyll right there's still a ruby generator right seven
[423.50 --> 430.74]  percent uh almost a thousand people so let me break it down one through eight here uh next js first with
[430.74 --> 439.46]  39 astro second with 18 nuxt with 12 gatsby at 10 eleventy coming in at eight percent jekyll like
[439.46 --> 445.84]  you mentioned seven and then hugo coming in six percent so a decent chunk of people are still using
[445.84 --> 453.94]  non-js static generators so both hugo which is in go and jekyll which is the og i think well it
[453.94 --> 459.70]  definitely popularized this category it's not the original static site generator but very popular
[459.70 --> 467.62]  because a little bit of history here tom preston warner of a co-founder of github wrote jekyll it
[467.62 --> 474.56]  was one of the first big open source ruby projects on github and he also wrote a very famous blog post
[474.56 --> 482.18]  called i believe i'm going from memory blogging like a hacker in which he made it cool to blog this style
[482.18 --> 487.84]  and jekyll just skyrocketed from there and became kind of the de facto for many years
[487.84 --> 494.76]  eventually being replaced by other tools but still out there yeah i mean i think this idea that markup
[494.76 --> 500.76]  is all you need for blogging for site generation for things like that it's really nice and it's clean
[500.76 --> 506.62]  and it maybe gets us out of the cycle of every developer who wants to blog and says oh but first i
[506.62 --> 510.88]  need to build a website for my blog like just use one of these frameworks write your blog and mark down
[510.88 --> 516.66]  and you're done right and there's also this situation that happened more in the past than it
[516.66 --> 522.14]  does now probably because of static generators but also because of the proliferation now of easy
[522.14 --> 529.78]  free hosting plans is that we had this thing called the slash dot effect which eventually became the dig
[529.78 --> 535.68]  effect right and then it became the hacker news or the reddit effect as different social aggregators
[535.68 --> 540.46]  kind of replaced each other but this was a situation where you would have a dynamically rendered
[540.46 --> 545.64]  web blog you know and every time and you wouldn't do anything you like it's wordpress or it's
[545.64 --> 550.38]  type machine what was the other one that was popular back in the day i don't know there's another
[550.38 --> 554.60]  one that was not wordpress but was very similar and so far as if you don't have caching turned on
[554.60 --> 559.32]  every time you get a server request you're just rendering that whole page over and over again
[559.32 --> 566.04]  which is totally fine until a popular until you get on slash dot or whatever until you're on slash dot
[566.04 --> 570.46]  and they send a bunch of traffic your way and then all of a sudden your website is down and that
[570.46 --> 573.80]  happened to a lot of hackers because we're not used to people reading our blogs you know
[573.80 --> 581.94]  we we we write in obscurity and then every once in a while a big you know personality or a slash dot or
[581.94 --> 587.40]  a dig would suddenly send a wave of traffic to your blog and at the one point when you want people to
[587.40 --> 592.80]  be able to read your site because they're interested you lose a bunch of opportunities one of the points
[592.80 --> 597.32]  that tom made in that blogging like a hacker which spoke and resonated with so many of us is like
[597.32 --> 603.92]  it's just html there's no website is down there's no rendering right it's pre-rendered and so you're
[603.92 --> 608.72]  never going to get slash dotted you're never going to get dig effect and that's why a lot of people i
[608.72 --> 615.80]  think were were into it back then it was like the original piece of let's actually send things close
[615.80 --> 619.96]  to the client let's have something where people can load something useful without having to touch our
[619.96 --> 625.20]  database right and so yeah they're still out there just probably because of good old-fashioned
[625.20 --> 631.44]  momentum but yeah a few of these would of course be offended if you called them site generators because
[631.44 --> 637.86]  they do so much more other ones gladly take the moniker i do think astro is kind of the interesting
[637.86 --> 643.90]  hybrid hybrid there because they have this very text-centered approach that was deliberate as a part of
[643.90 --> 648.52]  their philosophy i think we interviewed was it fred about that um just like kind of going into
[648.52 --> 656.50]  what they do and why but they also extend very smoothly into either full-on applications or
[656.50 --> 663.20]  little mini applets that are embedded as widgets in your site yeah almost their own category which is
[663.20 --> 671.18]  very cool and of course uh shout out to eleventy a long-time friend and uh guest of the show zach
[671.18 --> 676.38]  leatherman's little framework that could i mean they just had eleventy conf which was cool i'm not sure
[676.38 --> 681.14]  that's what it was called but it was an online only virtual event that zach put on and it seemed like
[681.14 --> 687.34]  it went really well so a lot of buzz and just love going on in the eleventy community which i want to
[687.34 --> 693.60]  share with folks definitely a cool project let's move on quickly now to ai tools uh which of these ai
[693.60 --> 700.22]  tools you regularly use to help you write code not exactly html focused question but still no surprises
[700.22 --> 708.84]  here most people chat gpt over half 52 got 34 using copilot and then just pulling up the rear
[708.84 --> 713.98]  google bard which i believe has been renamed already so i'm not sure when this yeah i don't think bard
[713.98 --> 718.78]  exists anymore and i yeah they renamed it gemini and i'm not sure if it still does code or i'm sure
[718.78 --> 724.66]  it does code but it does yeah i'm surprised to not see claude on here because and a few people i know
[724.66 --> 729.74]  who do this are like oh yeah claude is better for this type of stuff then yeah my guess is that the
[729.74 --> 734.74]  actual surveys were done a while back and this is such a fast moving thing that probably not even
[734.74 --> 739.32]  worth tracking without some sort of context of like there's brand new stuff all the time
[739.32 --> 749.24]  in fact gpt4o just came out supposed to be better so far i've used it for a day or so it feels pretty much
[749.24 --> 754.74]  the same to me but you know people are very impressed on social media last one here this is
[754.74 --> 760.34]  fun but hold on possibly most interesting on this is if we should play out the numbers a little bit
[760.34 --> 767.18]  how many people say they are not using an ai tool at all for code generation it's just 38 percent of
[767.18 --> 774.54]  respondents true so that inverting that means 62 percent of developers at least answering the survey
[774.54 --> 779.22]  are using some sort of ai code uh tool to help them code are you still writing code i can't
[779.22 --> 784.50]  remember occasionally yeah no i just get chat gpt to write it for me yeah i was gonna say you're
[784.50 --> 789.96]  managing chat gpt now no i i do write code occasionally i was debugging a tricky javascript bug yesterday
[789.96 --> 797.36]  nice those are always fun oh yes are any of the details interesting or no only only to rant about
[797.36 --> 805.26]  did you black out is it gone now no so it was dealing with react and an infinite scrolling component
[805.26 --> 811.34]  and the challenge was and a pet peeve i have about javascript which is javascript has all these array
[811.34 --> 817.26]  methods some of which that present sort of a functional interface right and some of them do
[817.26 --> 822.16]  sort of the natural functional thing of essentially create a copy that they're returning to you of the
[822.16 --> 828.06]  mutated data and some of them actually mutate in place and it turns out if you do dot reverse on a
[828.06 --> 832.58]  javascript array it mutates it in place and if that is state that you are getting from a hook somewhere
[832.58 --> 838.02]  and causes your react component to re-render every time you do it you can get up in a very nasty loop
[838.02 --> 846.86]  yeah so be cautious yeah ruby's the same way these languages that have you know some mutate some don't
[846.86 --> 853.70]  and i just am i appreciate like purely immutable languages for that reason because you never get
[853.70 --> 860.58]  bit by that particular inconsistency well did you use uh chat gpt to figure it out i did not
[860.58 --> 867.08]  nice all it's all kball baby just gave it all kball gpt here we go there you go so i uh recently
[867.08 --> 873.94]  wrote a little node server which is effectively puppeteer as a service just for our own dynamic
[873.94 --> 879.24]  share images you know it just takes the html and just renders it throws it on the s3 bucket or
[879.24 --> 884.32]  whatever and it's just a little puppeteer thing and i had not written like a node server for probably
[884.32 --> 888.90]  a decade honestly because i just don't write in back end i write elixir in front of my use javascript so
[888.90 --> 895.98]  but this was like i want to use puppeteer why go try to shove puppeteer somehow into elixir land
[895.98 --> 901.34]  which there aren't very many great tools or go with chromium direct anyways i was just like just use
[901.34 --> 908.78]  javascript man just and so i wrote a node server it's probably a hundred ish lines of code over a few
[908.78 --> 914.70]  hours and node's really nice now i mean we're gonna talk about a new release of node but like
[914.70 --> 919.86]  i thoroughly enjoyed it async awaits all good you know like you can set it in es modules mode
[919.86 --> 926.96]  all good uh chat gpt is really good at writing a few functions for me so i just you know i just like
[926.96 --> 934.28]  ah modern node well and that type of thing where you have a single purpose yeah small standalone thing
[934.28 --> 941.12]  is actually where these ai based code generators shine they're really good at one-offs um and generating
[941.12 --> 946.60]  those things and where they struggle a little bit more is when you're trying to sort of modify a big
[946.60 --> 950.82]  system and kind of dealing with lots and lots of different contexts they can do some things in there
[950.82 --> 955.10]  but they also fall on their face more often but that type of like here's an established piece of
[955.10 --> 960.14]  technology it's been around a while so it's in the training corpus i want to write a one per
[960.14 --> 965.92]  single purpose server like dang these tools are really good at that yeah absolutely all right now let's
[965.92 --> 970.42]  move on to a blast from the past this was a fun question have you ever used any of the following
[970.42 --> 978.44]  old school elements so these are now long since obsolete but still out there apparently these are
[978.44 --> 986.56]  html elements center marquee font frame set and frame blink of which the blink engine was named after
[986.56 --> 995.22]  applet plain text which i didn't even know about plain text is index and next id center being the most used
[995.22 --> 1000.50]  because hey in anger right we're just like maybe if i just wrap it in a center tag this thing will
[1000.50 --> 1009.74]  center uh 50 of people have used center that responded of course and then marquee uh 45 font 40 and so on
[1009.74 --> 1016.48]  i was curious with uk ball have you used any of these in the last uh five years five years maybe frame
[1016.48 --> 1022.78]  set and frame no that was more than five years ago no i don't think so yeah i don't think i have either
[1022.78 --> 1028.34]  maybe just marquee one time for fun like for nostalgic purposes but um i would fall into category
[1028.34 --> 1034.20]  10 33 percent of respondents have used none of the above but half of the people that took this have used
[1034.20 --> 1039.50]  the center element i guess reason enough that they would say yes to that question so that's kind of
[1039.50 --> 1046.16]  crazy to me but okay center it up is center still relevant for html emails i feel like that might be one
[1046.16 --> 1052.24]  place where so for our email i can only speak to my experience is that everything's basically just
[1052.24 --> 1057.94]  tables and rows in order to get to a certain like center and then you just write your content inside
[1057.94 --> 1063.84]  of that table and so that's what we use but maybe center works there as well i don't know possibly
[1063.84 --> 1070.12]  there is a new website you know can i use dot com how about can i email dot com have you heard of this
[1070.12 --> 1077.38]  it's necessary because html email technology stuck in the 90s it's so bad it's so hard i i still get
[1077.38 --> 1083.14]  with changelog news i still get emails a lot of people are like this doesn't look right mostly it's
[1083.14 --> 1092.66]  like do you use mjml no just just good old-fashioned html and tables i isn't mjml going to be react
[1092.66 --> 1099.64]  mjml is conceptually it's a pre-processing or template language i know i looked at it like
[1099.64 --> 1104.80]  version of it but it you know you can use it you could actually try to embed it in line but i would
[1104.80 --> 1109.20]  even more just use it to generate your html templates that you then use in your app right
[1109.20 --> 1115.10]  manually yeah ours was like i when i did this new iteration it was basically like just cargo culting
[1115.10 --> 1119.90]  what we did previously for changelog weekly which looked very similar but quite a little bit different
[1119.90 --> 1125.50]  you know and so i didn't i did look at mjml i remember thinking oh is it react and i was like yeah i'm
[1125.50 --> 1129.82]  just gonna do my own thing you know kind of stodgy but yeah i've heard good things about that
[1129.82 --> 1138.34]  anyways can i email.com definitely uh would promote the use of that for anybody in the unenviable
[1138.34 --> 1145.20]  position of having to craft their web pages for email clients which is even harder than the battle
[1145.20 --> 1151.76]  days of non-interoperability amongst browser engines all right let's move on uh definitely check
[1151.76 --> 1159.04]  out state of html.com for more there's a lot of good stuff on interoperability limited functionality
[1159.04 --> 1165.18]  what people will really want it sounds like people really want better forms better input support more
[1165.18 --> 1171.28]  widgets uh tabs they want we just want more widgets inside of our browsers versus having to reinvent
[1171.28 --> 1178.10]  the wheel over and over again we would love those things to be html native and maybe with this data
[1178.10 --> 1195.84]  someday they will be what's up friends this episode is brought to you by our friends at neon
[1195.84 --> 1201.60]  manage serverless postgres is exciting we're excited we think it's the future and i'm here with nikita
[1201.60 --> 1208.08]  shamganoff co-founder and ceo of neon so nikita what is it like to be building the future well i have
[1208.08 --> 1213.74]  a flurry of feelings about it coming from the fact that i have been at it for a while there's more
[1213.74 --> 1221.10]  confidence in terms of what the north star is and there is a lot more excitement because i truly
[1221.10 --> 1226.60]  believe that this is what's going to be the future and that future needs to be built and it's very
[1226.60 --> 1232.94]  exciting to build the future and i think this is an opportunity for for this moment in time we have
[1232.94 --> 1238.86]  just the technology for it and the urgency is required to be able to seize on that opportunity
[1238.86 --> 1246.40]  so we're obviously pretty excited about neon and postgres and manage postgres and serverless postgres and
[1246.40 --> 1251.62]  data branching and all the fun stuff and it's it's one thing to be building for the future and it's another
[1251.62 --> 1255.52]  to actually have the response from the community what's what's been going on what's what's the reaction
[1255.52 --> 1263.72]  like we are lately onboarding close to 2500 databases a day that's more than one database a minute of
[1263.72 --> 1270.14]  somebody in the world coming to neon either directly or through the help of our partners and they're able
[1270.14 --> 1275.40]  to experience what it feels like to program against database that looks like a url and the program
[1275.40 --> 1280.50]  against database that can support branching and be like a good buddy for you in the in the software
[1280.50 --> 1286.70]  development life cycle so that's exciting and while that's that's exciting the urgency at neon is
[1286.70 --> 1292.50]  currently is unparalleled there you go if you want to experience the future go to neon.tech on demand
[1292.50 --> 1297.92]  scalability bottomless storage database branching everything you want for the postgres of the future
[1297.92 --> 1300.50]  once again neon.tech
[1300.50 --> 1329.42]  what's up next on the docket looks like node 22 do that one next yeah let's do it speaking of node
[1329.42 --> 1336.96]  being nice these days yeah node 22 now available this was released april 24th so about a month back
[1336.96 --> 1346.42]  big release lots of notable changes uh specifically requiring es modules they got a built-in web socket
[1346.42 --> 1353.62]  client and now v8's been updated quite a bit uh what was interesting to you from this release anything
[1353.62 --> 1360.06]  yeah so i think the the requiring of es modules is a nice step forward it doesn't still doesn't work
[1360.06 --> 1364.78]  for every es module because you still have this like kind of awkwardness around synchronous versus
[1364.78 --> 1369.36]  asynchronous if it has a top level of weight i think it throws an exception or something like that
[1369.36 --> 1378.00]  but it is a step towards kind of finally having universal access to es modules without special
[1378.00 --> 1384.40]  configuration i think it's node basically throwing in the towel of saying yeah we know this is an ugly
[1384.40 --> 1390.98]  solution and it has drawbacks but people want es modules so let's do that so i think that's good
[1390.98 --> 1395.32]  i think it's still experimental i think it's not fully there but it's a step in the right direction
[1395.32 --> 1401.80]  having the web socket client just built in by default good stuff yeah good stuff one thing that stood out to
[1401.80 --> 1409.76]  me that i think was actually introduced in node 20 it's still experimental but it's improving is this
[1409.76 --> 1415.28]  idea of process-based permissions which i think was one of the big things that dino originally pushed
[1415.28 --> 1421.42]  forward as like you can enable which permissions are allowed for a process right and i love to see node
[1421.42 --> 1426.10]  pulling that back in or taking that inspiration and making it happen in node land because that is a
[1426.10 --> 1433.42]  huge huge security improvement to be able to say you know what there's no reason this process
[1433.42 --> 1439.24]  should be accessing my file system like just let it go yeah that's really cool and then the rest of the
[1439.24 --> 1446.46]  major wins it seems like was just by bringing v8 somewhat up to date 12.4 of course v8 has a bunch
[1446.46 --> 1452.56]  of stuff built into it and so you get the freebies by node running off a newer version of v8 looks like
[1452.56 --> 1459.58]  they got a web assembly garbage collection in their array from async so additional array methods set
[1459.58 --> 1467.54]  methods like all the goodies and that really is what is nice about writing node side javascript is
[1467.54 --> 1473.38]  like you're not dealing with like lowest common denominator functionality you don't have to go to
[1473.38 --> 1478.18]  can i use because like the answer is yes you can pretty much right if node does it you can do it
[1478.18 --> 1488.22]  and uh it really is a reason to enjoy some back-end javascript so check it out node 22 moving on to
[1488.22 --> 1494.06]  react react is still going they're still the gorilla they still are and they have a couple things going
[1494.06 --> 1499.38]  on that were notable uh one that just dropped yesterday and i know that nick was very excited
[1499.38 --> 1503.80]  about because he put it in our chat and said let's do a show so maybe a full show coming soon
[1503.80 --> 1511.40]  about this is the react compiler which is open source this is a new experimental compiler
[1511.40 --> 1517.70]  that the react team has open source to get early feedback from the community what does it do it's a
[1517.70 --> 1523.98]  build time only tool that automatically optimizes your react app it works with plain javascript and
[1523.98 --> 1530.30]  understands the rules of react so you don't need to rewrite any code to use it i mean free code
[1530.30 --> 1537.40]  optimizations why not right it's hilarious because it's another step uh one is community inspired i
[1537.40 --> 1543.62]  think again right they're looking at the things that you have us felt doing a you know the things
[1543.62 --> 1548.56]  that angular is able to do owning the whole ecosystem that you know things that quick is doing
[1548.56 --> 1555.28]  where they're saying hey we can make things faster by default because we run this build time compile
[1555.28 --> 1560.24]  step that can make all these optimizations and react is saying wait wait us too we could do that
[1560.24 --> 1565.96]  too so i think there's there's something really interesting and powerful there i do think it is
[1565.96 --> 1571.88]  also a reaction to the fact that it's the core of react it's really easy to write non-performant code
[1571.88 --> 1579.28]  and it's gotten very hard and labor intensive to keep react performant as your app scales and this is saying
[1579.28 --> 1584.84]  okay maybe what we can do is we can figure out tooling around that that that reduces some of that
[1584.84 --> 1592.68]  developer load you do still have to follow certain rules so it's it's kind of like in in frameworks like
[1592.68 --> 1597.94]  quick or something like that it won't work at all if you don't follow those rules right in react
[1597.94 --> 1604.58]  it'll probably work in some ways it just won't be fast or effective so this is saying okay you follow
[1604.58 --> 1610.98]  the rules you can get some automatic speed improvements yeah i wonder how easy it'll be to run like
[1610.98 --> 1615.72]  benchmarks without it and then just use it and then benchmarks with it and see if you get the
[1615.72 --> 1622.34]  wins to make it worth it to integrate it into what you're up to i don't know if it's planned to be run
[1622.34 --> 1628.88]  i'm not sure exactly like is this like part of your build step every time you compile your build your
[1628.88 --> 1633.46]  program to be launched or is it going to be like you run it once and it tells you how to rewrite stuff
[1633.46 --> 1638.84]  too i mean it says automatic but my impression was it was part of your build step which does then
[1638.84 --> 1644.84]  introduce some interesting questions around differences between development environment and
[1644.84 --> 1651.62]  prod or stage yes because notably this is written in rust this is not written it with node or with
[1651.62 --> 1657.82]  javascript tooling and so now are we going to ship another dependency perhaps or are we going to have
[1657.82 --> 1663.32]  a universal binary does rust do universal binaries i don't know um like go does so that you could just
[1663.32 --> 1668.62]  ship it like alongside the rest of the tool chain i don't know i think it's it's going to have to get
[1668.62 --> 1675.50]  built for your machine so that the react team might build a whole bunch of different distributions of
[1675.50 --> 1679.72]  this so you don't have to compile it yourself you just download the one that matches your architecture
[1679.72 --> 1685.20]  i don't know i mean i would assume it's like any sort of node based natural language extension it gets
[1685.20 --> 1691.22]  built at install time so you build it you install with node and it does it compile all very new all very
[1691.22 --> 1697.68]  experimental things to ask the team but out there in open source already so facebook github
[1697.68 --> 1702.92]  slash react slash compiler like it's in the compiler folder inside of the react proper they also have a
[1702.92 --> 1709.66]  blog post out maybe this isn't a blog post this is like in there learn the new react docs that talks
[1709.66 --> 1714.88]  about it and it says should i try out the compiler it says you do you don't have to rush into using the
[1714.88 --> 1718.72]  compiler now it's okay to wait until it reaches a stable release before adopting it so it's really
[1718.72 --> 1722.72]  exciting it's the community's up in arms about not up in arms that's a bad thing
[1722.72 --> 1728.24]  up in excitement about it but it's very much like the folks who are building and getting involved
[1728.24 --> 1734.70]  and probably early adopters trying it right now early days but stay tuned for perhaps an episode
[1734.70 --> 1741.38]  from us with some of the react team we know that joe savona was involved and he's been on the show
[1741.38 --> 1746.50]  before so probably can get joe back on to talk about what they're up to with that that's cool and then
[1746.50 --> 1755.78]  of course the much anticipated much awaited react 19 in beta as of april 25th perhaps you know perhaps
[1755.78 --> 1760.96]  you've heard perhaps you're running the beta i don't know if you like to live that close to the
[1760.96 --> 1768.12]  edge or not but first release in a long time it's still not released released but it's out there what's
[1768.12 --> 1773.70]  all in react 19 givall so there's some pretty interesting things i think one of the big headline
[1773.70 --> 1778.52]  pieces is okay react server components are actually production ready they're no longer experimental
[1778.52 --> 1783.80]  they're there they're a baked in part of it i think you know that's a that's a big step that's
[1783.80 --> 1788.52]  probably why it's taken so long but also we've all been sort of adapting to what are these things for a
[1788.52 --> 1793.64]  long time it's just kind of pushing that one step further another couple things i thought were
[1793.64 --> 1802.70]  interesting one is they introduced this new concept of actions and transitions which as far as i could
[1802.70 --> 1808.70]  understand it reading it i have not tried playing with it yet is kind of trying to absorb some
[1808.70 --> 1814.30]  classic patterns around how you handle state transitions between okay i'd made a change i send
[1814.30 --> 1819.58]  an api request i get something back i update a place like all those different things right now you have
[1819.58 --> 1824.28]  to there's a lot of like patterns you put in place to manage that smoothly and make sure it handles things
[1824.28 --> 1829.26]  like errors and optimistic updates and things like that and react is saying oh this is a common problem
[1829.26 --> 1834.64]  that everybody has let us absorb some of those patterns into the core framework and make it easy
[1834.64 --> 1840.42]  to use um one particular example that i thought was really nice is they have a new hook called use
[1840.42 --> 1846.44]  optimistic which essentially is like all right you're doing an update back to the server with this value
[1846.44 --> 1852.74]  let's optimistically update the ui to that value and have react put that in place but then automatically
[1852.74 --> 1857.82]  handle when the value comes back from the server or if there's an error or something like that to update it
[1857.82 --> 1864.04]  based on that like that's a really nice to smooth experience something that previously you either have
[1864.04 --> 1870.32]  to handle yourself or not handle and have either a slow ui or something that could get out of sync
[1870.32 --> 1878.68]  right loading spinner yeah so that's really nice they also introduced this new use method that as from
[1878.68 --> 1883.64]  what i can tell is basically it's a similar type of thing but it's trying to make the user experience
[1883.64 --> 1889.76]  or the sorry the developer experience around suspend a lot nicer so suspend has dealing with suspend
[1889.76 --> 1894.38]  and it's throwing promises and all of that has always been a little bit of a tricky developer
[1894.38 --> 1900.40]  experience and with this you basically can use a set of promises and then once this then suspend is
[1900.40 --> 1904.92]  off and doing something and when suspend comes back it automatically updates that in whatever your
[1904.92 --> 1910.98]  component is yeah a lot of a lot of kind of nice absorption of patterns around how to deal with
[1910.98 --> 1918.06]  asynchronicity and things that that people have been having to do by hand yeah i love optimistic uis i
[1918.06 --> 1923.18]  think it's definitely the way to go nine times out of ten everything's hunky dory right so why don't you
[1923.18 --> 1928.96]  just go ahead and update the ui assume if it was good and then have some sort of a reaction to a failure
[1928.96 --> 1936.68]  as the corner or edge case that it typically is but traditionally that's kind of a pain in the butt to
[1936.68 --> 1942.02]  code that up i mean it's just not as straightforward as just waiting for the response and then handling
[1942.02 --> 1950.26]  it from there so any tooling that allows more people to do optimistic uis i think is a big win
[1950.26 --> 1957.28]  so this use optimistic to me is pretty cool all right so react server components production ready
[1957.28 --> 1964.62]  we have actions and transitions which are kind of intimately linked in my mind according to what i read
[1964.62 --> 1972.36]  where it's basically an action is more of an idiom it seems than an actual formalized piece of the
[1972.36 --> 1977.82]  code base because they say by convention functions that use async transitions are called actions so
[1977.82 --> 1983.16]  they're just kind of calling certain functions actions and hoping that catches on i don't know
[1983.16 --> 1987.56]  am i understanding that correctly i think they're basically pulling these were things that were
[1987.56 --> 1992.94]  encapsulated in state management tools um right if you look at like a redux or things like that like
[1992.94 --> 1998.90]  action meant something there that is very similar to what this is and they're saying oh we're
[1998.90 --> 2003.48]  discovering that more and more especially now that we have context we have all these other tools for
[2003.48 --> 2009.14]  managing state directly in react people aren't using these heavy tools but then they're missing some of
[2009.14 --> 2015.34]  the functionality and niceties around that and so let's start building that into react so i think
[2015.34 --> 2023.00]  that concept of here's a straight state transition that triggers an asynchronous thing to happen that
[2023.00 --> 2026.92]  already existed that was a part of state management tools and react is saying we're gonna we're gonna
[2026.92 --> 2031.58]  have some developer experience around that just in court react very cool so do you know how long these
[2031.58 --> 2039.44]  betas tend to run before you actually get a finalized release it's a good question i don't actually
[2039.44 --> 2045.32]  know they look on their blog they don't call it beta one so i think they're assuming this is the only one
[2045.32 --> 2049.80]  so some projects will have like beta one beta two and then like a release candidate you know
[2049.80 --> 2056.78]  um i'm not sure how react does theirs but are we assuming this is going to be soon i mean it's been a month
[2056.78 --> 2065.82]  almost since the beta came out it's not clear to me yeah so just stay tuned i think the question i guess
[2065.82 --> 2074.20]  would be for your typical shop is react 19 actually ready to give it a shot yet or is it like because
[2074.20 --> 2078.58]  i remember back in the old days of ruby on rails for instance they would have a beta one a beta two
[2078.58 --> 2082.46]  a beta three however many betas they needed and then they'd have a release candidate one release
[2082.46 --> 2087.30]  candidate two and as a guy who was just trying to run some websites on rails but didn't want to fall
[2087.30 --> 2092.52]  behind i was like yeah i'm gonna wait you know until release candidate one because by then it's like
[2092.52 --> 2097.64]  this is pretty solid like barely anything will change between now and the big release and so i
[2097.64 --> 2102.18]  kind of had an idea of what that actually meant but if there's just one beta and then who knows and then
[2102.18 --> 2108.26]  it's going to release you wonder if the beta is baked enough for your common people to try it or if
[2108.26 --> 2113.80]  it's just like it says beta but you know gmail wasn't beta for like 12 years so yeah what does beta
[2113.80 --> 2123.44]  even mean anymore i don't see let's see it's on npm um i was trying to look in their github repo for
[2123.44 --> 2132.16]  if they have historical beta releases and see what was going on there and i didn't see it but they
[2132.16 --> 2137.78]  the beta isn't even on github right now so now i'm looking to see if it's on so i'm thinking that
[2137.78 --> 2145.48]  that's pretty not big so on their react 19 beta upgrade guide one of the notes at the top says
[2145.48 --> 2152.64]  this beta release is for libraries to prepare for react 19 app developers should upgrade to 18.3
[2152.64 --> 2159.34]  and wait for react 19 stable so i think if you're just an app developer even though the beta has been
[2159.34 --> 2164.56]  out for a month i would probably just sit tight unless you have a small code base you can try it
[2164.56 --> 2169.40]  real quick and see if anything broke but if you have like a significant app i don't think i would
[2169.40 --> 2173.52]  be hopping on this beta train because they say it's for libraries it's not really for regular devs yet
[2173.52 --> 2183.18]  yeah yeah it's not clear for 18.0 that looks like they did do a beta but it that's so long ago it's
[2183.18 --> 2187.98]  hard to read oh and then they in that one they went through alphas it was months and months and months
[2187.98 --> 2193.44]  i would i would not anticipate this is ready to go i think it'll be a while all right so there you have
[2193.44 --> 2199.82]  it there's our advice from two people who've been burned plenty of times to know better but still
[2199.82 --> 2204.28]  kind of want to check it out so we're like well should i go play with it on a side project yeah
[2204.28 --> 2210.56]  exactly start not production ready don't put it on your your money making endeavors at this point
[2210.56 --> 2219.94]  all right next up we got volt volt from some of our friends volt vlt.sh from some familiar
[2219.94 --> 2225.60]  faces and names maybe you remember darcy clark who's been on js party a handful of times talking
[2225.60 --> 2233.38]  security they are trying to build the future of javascript packages that's what the home page says
[2233.38 --> 2241.36]  uh what is this all about cable that is a great question i was trying to dig in and understand what
[2241.36 --> 2249.30]  it is so you've got a founding team which includes both the original creator of npm and a couple of
[2249.30 --> 2257.00]  folks who were in npm from early on have also done stuff in github things like that you have a website
[2257.00 --> 2264.34]  that is basically just sign up for news but also has this blog post their first blog post is aiming at
[2264.34 --> 2271.26]  essentially supply chain security right looking at oh there is this massive baked in vulnerability
[2271.26 --> 2278.22]  in how npm works and it leads to all these supply security right challenges and then if you look at
[2278.22 --> 2285.28]  their investor list they list out who all their investors are it includes two uh js party folks
[2285.28 --> 2290.86]  that we know amel is an investor uh for ross is an investor they're both called out by name there
[2290.86 --> 2300.28]  so are people like uh guillermo roche however you pronounce his name um evan you and i saw also a
[2300.28 --> 2306.16]  former vp of snick or sneak however you pronounce that so all of these signs like particularly you
[2306.16 --> 2311.04]  have ferocin there you have somebody from sneak in there as investor and you have this initial blog
[2311.04 --> 2318.02]  post about supply chain security i think what they're going to be trying to do is a new package
[2318.02 --> 2324.42]  management ecosystem that is secure by default that cuts off a lot of the like right now we have a
[2324.42 --> 2331.34]  whack-a-mole problem in npm package security there's all sorts of people attacking it from different ways
[2331.34 --> 2336.92]  but fundamentally there are vulnerabilities in the way that packages are managed in the javascript world
[2336.92 --> 2343.58]  and you can do either automated or manual reviews and all sorts of things to try to manage that and but
[2343.58 --> 2347.94]  my guess is this is trying to attack that core problem and build something that's going to be
[2347.94 --> 2353.64]  secure and verifiable by default so you all may remember the episode the massive bug at the heart
[2353.64 --> 2360.06]  of the npm ecosystem that was the first blog post uh by volt and i think darcy talked a little bit and
[2360.06 --> 2366.14]  he was very vague when he was on the show talking about what he was up to but he did mention that isaac
[2366.14 --> 2373.10]  schluter the original npm creator was with him and he has since recently in march announced like
[2373.10 --> 2379.86]  this funding round that cable is referring to and just still vague but interesting because mostly
[2379.86 --> 2387.30]  because of i guess the pedigree of the people who are either invested or on darcy's team it looks like
[2387.30 --> 2394.98]  these folks are serious js community people with some money behind them from very smart people i even
[2394.98 --> 2402.70]  see david kramer from sentry on the list i see michael jackson from remix uh investing as well so
[2402.70 --> 2409.94]  i'm curious what they come out with that being said i mean you do have ryan doll and the dino team
[2409.94 --> 2415.60]  coming out with their thing already in production the jsr registry so are we going to see now you know
[2415.60 --> 2421.12]  some competing at the registry layer beyond even what you see right now it seems like probably we're going
[2421.12 --> 2427.60]  to definitely feels like it's heading in that direction and i i think it's it's kind of a reaction
[2427.60 --> 2435.18]  to this sort of escalating number of supply chain security vulnerabilities that people have run into
[2435.18 --> 2442.84]  and a realization as people were digging into it that it is essentially unsolvable with the current
[2442.84 --> 2448.58]  systems and so now people are saying okay it's unsolvable we're trying to keep the lights on and
[2448.58 --> 2453.76]  patch things as we go but we got to attack the heart of the problem i think it's kind of cool that we
[2453.76 --> 2459.72]  have at least we assume what volt is building based on what they've said so far and who they are we have
[2459.72 --> 2466.30]  registries or package let's just call them packaging solutions uh coming out from the creator of node
[2466.30 --> 2473.06]  and then the creator of npm you know it's like decades later and it's like round two baby let's see what
[2473.06 --> 2481.12]  happens yeah well and it is it is interesting to realize i mean i think we look at react react the changes
[2481.12 --> 2487.70]  like that it's like the types of changes you'd expect in a very mature ecosystem of like okay we're
[2487.70 --> 2493.62]  absorbing these patterns from the community we're handling these things and then you have people
[2493.62 --> 2501.62]  saying you know what we have the foundations wrong let's reassess that and relook it it leads me to
[2501.62 --> 2509.66]  believe that there's still a long runway for innovation in the javascript community amen to that that's
[2509.66 --> 2518.68]  exciting times for sure so one more bit of i guess news i don't know what you call it i didn't put it
[2518.68 --> 2524.12]  in the doc cable so i'm gonna slap you with this one is the gulp developer survey we talked about the
[2524.12 --> 2531.10]  state of html and we talked about blasts from the past i mean i hadn't heard the term gulp except for
[2531.10 --> 2538.96]  in dumb and dumber when he says hey guys oh big gulps huh all right well see you later for years
[2538.96 --> 2544.84]  and yet uh here they come gulp has gone nowhere they had a recent release and they're actually
[2544.84 --> 2551.46]  introducing their own gulp developer survey did you use gulp first of all tell tell our young
[2551.46 --> 2557.30]  listener what gulp is and then we can talk about whether or not we used it oh man okay so gulp is
[2557.30 --> 2563.42]  fundamentally a javascript task runner back in the day before we had good build tools it got used as
[2563.42 --> 2571.62]  a de facto build system and at some point the ecosystem said hey you know what task runners don't
[2571.62 --> 2576.68]  actually make great build systems they're optimized for different things and so we had a variety of
[2576.68 --> 2582.18]  different dimensions um i think the first one was actually as so often as this case ember had this
[2582.18 --> 2587.14]  like build dedicated system i believe it was called broccoli or something like that something that went in
[2587.14 --> 2591.38]  that direction and then webpack said oh okay we're gonna get in the game and they started winning
[2591.38 --> 2596.36]  everything and most recently you have veet saying let's go back to basics build on top of es modules
[2596.36 --> 2601.80]  which to be fair we're not there back when these original build systems were working but let's build on
[2601.80 --> 2607.82]  top of this let's make things faster and so the kind of build ecosystem has evolved tremendously
[2607.82 --> 2614.00]  beyond what gulp or another task runner could do well let me mention the other big task runner
[2614.00 --> 2620.96]  which you're going to remember grunt grunt yes oh that was actually another big thing so those two
[2620.96 --> 2626.86]  fundamentally they had a philosophical difference so grunt was file-based would read everything you
[2626.86 --> 2630.16]  know read your stuff in from a file right out to a file and then the next whatever the next task
[2630.16 --> 2635.38]  would read in from files right out to files that obviously gates you performance wise on the
[2635.38 --> 2640.38]  performance of your file system gulp used a streaming approach you'd essentially stream tasks input to
[2640.38 --> 2644.66]  output input to output kind of go there which allowed it to be much faster on another set of
[2644.66 --> 2652.64]  dimensions now i too had not seen gulp in a long time part of that was my main exposure to gulp was
[2652.64 --> 2659.60]  through build systems however while build systems are not perhaps the best application of task
[2659.60 --> 2664.22]  record runners or a more dedicated system is actually better than a task runner there are tons of different
[2664.22 --> 2671.24]  things that do fit into a task runner paradigm and so it's not that surprising to me that gulp optimized
[2671.24 --> 2675.74]  for task runners still exists and i was looking at still getting like over a million downloads a week or
[2675.74 --> 2682.88]  something like that from npm it's still moderately widely used which is interesting and they are
[2682.88 --> 2688.52]  currently running a survey we invite you to help us explore the needs of the gulp community above and
[2688.52 --> 2693.90]  beyond the issues on github by completing the gulp developer survey before may 31st so as you listen to this
[2693.90 --> 2700.16]  you still have a few days to get it done if you are a gulp user please do the survey is anonymous and
[2700.16 --> 2705.76]  they just want to find out how people are using it and what they want from it so they can make it
[2705.76 --> 2710.50]  better i think as you get to a certain scale even a project like this which is they said a decade old
[2710.50 --> 2715.30]  you don't know exactly it's being used so much you don't know exactly how people are using it i remember
[2715.30 --> 2721.46]  we asked daniel stenberg from the curl project years ago now famously we asked him how he knows
[2721.46 --> 2728.88]  you know how people are using curl and he's like i have no idea like now he is he since developed
[2728.88 --> 2735.08]  like similar things that he can have a feedback loop from his users but he also had so many users
[2735.08 --> 2739.12]  using it in so many different ways that it was like how do you even wrangle that community anyways
[2739.12 --> 2743.80]  a lot of times you're not sure how people are using it and all you responding to is the
[2743.80 --> 2749.96]  squeakiest wheels who are using it inside your github issues right to support their to report their
[2749.96 --> 2755.34]  bugs and their feature requests and all these things and the squeaky wheels are awesome in a
[2755.34 --> 2763.24]  sense but they're also louder noises than necessarily represent your user base and so you can you can
[2763.24 --> 2768.02]  overcompensate for power users which i think happens a lot and it's hard not to well and sometimes those
[2768.02 --> 2772.24]  squeaky wheels are the people trying to use it for something it's not actually good at good point you
[2772.24 --> 2777.68]  have a large number of people using it for the things that it's good at and being very quiet but if you
[2777.68 --> 2781.78]  don't understand that that's what they're using it for you might not realize there's an opportunity to
[2781.78 --> 2787.96]  develop it even further in that direction yeah that's a really good point because oftentimes when
[2787.96 --> 2792.94]  we're trying to use something that it's not exactly developed for that's when we hit up against so many
[2792.94 --> 2798.58]  corners edges and limitations and so then we are the ones who are reporting these limitations
[2798.58 --> 2803.58]  and if you listen too much to those i've seen it happen you can really take a project in a direction
[2803.58 --> 2810.60]  that nobody except for a few really wanted to go in and it takes i think you know a certain level of
[2810.60 --> 2817.08]  experience and i guess confidence to say that's a really cool idea please do fork it you know take it
[2817.08 --> 2823.44]  over there and build that thing but that's not what this tool necessarily is and so you need to hear from
[2823.44 --> 2828.54]  not just those people even though they are often your best contributors and stuff but you need to hear from
[2828.54 --> 2832.90]  everybody and so that's what they're trying to do i mean i didn't even know gulp was still in active
[2832.90 --> 2836.76]  development so for me this is cool just to learn about that it's still out there doing its thing
[2836.76 --> 2843.38]  well and i think this is an example of a common problem for us right we see the hot shiny new stuff
[2843.38 --> 2848.32]  because that's what's making news and that's what people are exciting about but boring technology
[2848.32 --> 2854.68]  lasts a long time how many sites are still built on wordpress how many sites are still using jquery
[2854.68 --> 2861.62]  all those different things right like it's fun and exciting to be in the hot new world and when
[2861.62 --> 2866.04]  you're doing greenfields projects you probably want to start in the hot new world because there are
[2866.04 --> 2871.42]  benefits there's reasons why people are evolving in that direction however when you're not doing
[2871.42 --> 2878.92]  greenfields work if it ain't broke don't fix it yeah call back to our episode recently my interview
[2878.92 --> 2885.96]  with kelvin omerishone from the boring javascript stack i mean he's out there promoting sales js
[2885.96 --> 2895.44]  s-a-i-l-s not trying to sell js uh which is a server-side kind of rails alike in javascript from
[2895.44 --> 2901.78]  2012 2011 that's when it started and it's still just doing its thing and there's still people that are
[2901.78 --> 2908.38]  building new websites with it and like a whole little ecosystem of boring technology that's like
[2908.38 --> 2913.70]  building businesses that i hadn't known about until kevin made me aware of it and so cool stuff
[2913.70 --> 2918.34]  he he was so excited about the most boring things it was hilarious he's like i'm here to get you
[2918.34 --> 2925.16]  excited about boring tech well and it you know if you are interested in entrepreneurship and business
[2925.16 --> 2934.00]  a lot of times the problem you're solving is only sort of a technical problem yeah and you have a set of
[2934.00 --> 2938.26]  risks that you're taking on by trying to start a new business or a new product or a new feature line
[2938.26 --> 2944.34]  and if you can avoid having technology be one of your risks by using something that is boring but
[2944.34 --> 2949.28]  tried and true and just works out of the box and all of the error cases are already handled and all
[2949.28 --> 2956.24]  of the rough edges have been sandpapered down and it is easy to use and easy to adopt to adopt like
[2956.24 --> 2961.52]  that's one more risk you don't have to worry about absolutely so what are some examples of boring
[2961.52 --> 2968.76]  technology that folks could look at i would say postgres or my sequel right like boring relational
[2968.76 --> 2975.84]  databases relational databases um monolith application frameworks you know django laravel
[2975.84 --> 2982.04]  django rails sales you know things in that domain i mean i think we're seeing that a lot with react
[2982.04 --> 2988.42]  right react is actually becoming the boring technology it is it's being assailed by people saying it's you
[2988.42 --> 2994.00]  know it's not the new hotness anymore but that is actually in my opinion one of the reasons why a lot
[2994.00 --> 3000.96]  of people are using it because it just works for what it does object storage yep object storage blob
[3000.96 --> 3012.36]  storage i mean actually sqlite sqlite is a boring local database technology that like actually works for a lot
[3012.36 --> 3017.36]  of different things and you can you can run it live in your browser right you can do all sorts of different
[3017.36 --> 3023.86]  things with sqlite that give you if you want you know relatively simple but database-like functionality
[3023.86 --> 3028.54]  in a local environment whether you're shipping an app or you're running something in the browser like
[3028.54 --> 3034.70]  it just works really cool project that i've been watching called redka which is a re-implementation
[3034.70 --> 3042.96]  of redis with a sqlite back end so it's actually just sqlite but you have the redis apis so all redis
[3042.96 --> 3048.04]  clients work against it and it's not as fast as redis was but it's fast enough for most use cases and it's just
[3048.04 --> 3055.48]  the boring simplistic reliable sqlite at the end of the day that's pretty cool it's kind of a melding
[3055.48 --> 3060.78]  of the new and the old there because it's a new project but using all the tech because you know redis
[3060.78 --> 3065.68]  isn't exactly uh open source anymore so a lot of people trying to go out there and find alternatives
[3065.68 --> 3071.84]  moving forward from redis which i would have historically called at this point kind of a tried and true
[3071.84 --> 3078.30]  boring piece of tech but got exciting it got exciting recently for non-technical reasons yeah
[3078.30 --> 3084.74]  for all the wrong reasons redis got exciting again well i think node.js is pretty boring i mean because
[3084.74 --> 3090.74]  you know what's coming on the podcast is the dinos and the buns right and what's now the boring
[3090.74 --> 3097.42]  tried and true tech i mean node version 22 that's a lot of versions but rock solid all right well this
[3097.42 --> 3102.80]  is getting boring so let's end there i will not continue to pester you to list even more
[3102.80 --> 3109.22]  pieces of boring technology that's the news to discuss unless k-ball you have any other links that
[3109.22 --> 3113.54]  i didn't see or things that we didn't mention as we went along things i skipped over that you want to
[3113.54 --> 3119.62]  highlight before we end it i think that is all good the not boring is figuring out how to use ai in
[3119.62 --> 3125.76]  your projects but as we refer to yes recently like there's no better way to make a project slow and
[3125.76 --> 3132.32]  not valuable than throw an llm in where it's not useful that being said they are very useful in some
[3132.32 --> 3137.90]  domains right people are what did we say 62 percent of people using them to help them code yeah if you're
[3137.90 --> 3142.72]  not already trying that like see where you can find the value because i think and and the reason i bring
[3142.72 --> 3148.30]  this up is when we talk about boring and we talk about exciting technology i think we as as technologists
[3148.30 --> 3156.48]  as engineers tend to skew to the extremes we tend to either go to i'm going to try everything new
[3156.48 --> 3162.80]  this is so cool and we see this in the hype waves and like oh my gosh we got to do everything new
[3162.80 --> 3168.54]  or because we've been burned by that we go into the super skeptic side of like now there's nothing
[3168.54 --> 3174.30]  valuable here only do the old stuff only do the stuff that's proven and do things and i think
[3174.30 --> 3180.42]  the kind of using ai to code and using it in some of these domains is one of these where
[3180.42 --> 3187.48]  those two extremes are both dangerous they both are going to cause problems for you i think if you
[3187.48 --> 3193.24]  are way in on the hype you're going to end up in one of these you know using it where it shouldn't be
[3193.24 --> 3198.72]  used and end up in one of these places where like i go back to like the there was a chat bot on a
[3198.72 --> 3205.38]  airline website that gave away things that the airline did not actually have oh really like
[3205.38 --> 3209.34]  parts of it and then they were found legally liable they had to follow through on a contract
[3209.34 --> 3213.96]  because they said it's on your website you have committed to it so it's like a deal that the person
[3213.96 --> 3219.10]  wouldn't have got otherwise that deal that did not exist yikes and that's real money right there
[3219.10 --> 3223.48]  they were found legally liable for it right so if you go too far into oh these things are magic
[3223.48 --> 3230.78]  you will end up you know shooting yourself in the foot with them however they are not pure hype
[3230.78 --> 3235.72]  they're not crypto it's not just technology for the source of making money and not valuable for
[3235.72 --> 3242.26]  anything else sorry for us or whoever was it wasn't for us who was who was into crypto uh michael rogers
[3242.26 --> 3248.40]  yeah sorry but um it's not crypto it's not all scams there is real value there and if you're ignoring
[3248.40 --> 3253.46]  it because you're in that sort of like oh it's been overhyped so clearly there's nothing actually here
[3253.46 --> 3257.68]  you are going to get left behind and so i think that is in that domain of it's not boring
[3257.68 --> 3265.58]  but it's worth looking into but don't buy into all the total crazy agi next year hype right well said
[3265.58 --> 3272.06]  i agree on all fronts cool so aren't you also i saw on linkedin you were doing some sort of ai
[3272.06 --> 3278.88]  productivity thing you wanna i am doing ai stuff yeah so a couple different things so my uh the company
[3278.88 --> 3284.28]  i work for mento is a coaching company we're working on ai coaching tools which is kind of fun
[3284.28 --> 3290.24]  and it is trying to find that line of like okay let's not over promise but let's deliver something
[3290.24 --> 3296.06]  that's actually valuable to people and as a part of that we're uncovering all these different pieces
[3296.06 --> 3300.44]  around like how do we actually productively use it so i think what you probably saw was i'm giving a
[3300.44 --> 3306.94]  talk this summer on an application pattern around ai and here's the key piece of it so it uses the ai
[3306.94 --> 3311.52]  to interact with someone to extract some information but then you validate it with that person because
[3311.52 --> 3316.72]  one of the core problems with these ai tools is they will lie to you and they may get things right
[3316.72 --> 3322.46]  80 of the time even 90 or 95 of the time but if you're going to go and take what somebody has said to
[3322.46 --> 3327.16]  you and like go off and do something you need to validate it first and then once you validate it you
[3327.16 --> 3333.32]  can extrapolate from there so i think as we talk about ai like thinking about how do you validate
[3333.32 --> 3339.06]  what you're doing with it and what you're getting with it so if you're in that ai chatbot case is there
[3339.06 --> 3343.72]  a way you can formally represent whatever the agreement is you've gotten to and validate it
[3343.72 --> 3349.72]  formally okay these are the sets of offers that we actually can offer or run it by a human or do
[3349.72 --> 3356.30]  something else but like thinking about these patterns of ai is really useful and it is not reliable in the
[3356.30 --> 3362.12]  way we're used to thinking of software as being reliable right so we need to use it and then find a way to
[3362.12 --> 3367.72]  validate the outcomes very cool well hit me up with a link to whatever conference or whatever
[3367.72 --> 3372.28]  talk you're giving so we can hook people up in the show notes yeah for those who are interested in
[3372.28 --> 3379.82]  hearing about that sounds interesting to me indeed all right on behalf of kball and jsparty i'm jared
[3379.82 --> 3398.70]  we'll talk to you all on the next one all right that is jsparty for this week thanks for hanging with
[3398.70 --> 3405.10]  us you've heard kball and my thoughts now on all the news of late but what about your thoughts got any
[3405.10 --> 3409.70]  hot takes we'd love to hear from you there's a link in the show notes leave us a comment on the
[3409.70 --> 3415.90]  episode thanks again to our partners at fly.io to our mysterious friend breakmaster cylinder who
[3415.90 --> 3421.40]  cranks out fresh beads for us on the regular and to our friends at sentry use code changelog when you
[3421.40 --> 3427.18]  sign up to save 100 bucks on the team plan sentry's awesome we love it and we think you'll love it too
[3427.18 --> 3433.44]  code changelog 100 bucks off it's just that easy that is all i got but come back and party with us again
[3433.44 --> 3434.30]  next week
