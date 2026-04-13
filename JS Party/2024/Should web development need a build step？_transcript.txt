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
[101.70 --> 109.88]  extra modules to get all off on and you know in the user profile having a profile picture and
[109.88 --> 114.76]  setting up to a bay right it's like like all this extra work that you have to do and with clerk i
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
[247.64 --> 261.86]  hello jsparty people i am jared your internet friend and i am excited because it's been too long
[261.86 --> 269.00]  far too long since we've done one of our yep nope style debate episodes we have an awesome
[269.00 --> 276.04]  set of debaters lined up for you first some guests we'll get to you eventually k-ball eric clemens is
[276.04 --> 279.80]  here what's up eric how you doing man hey i'm doing great thanks for having me always happy to
[279.80 --> 284.60]  have you on the pod a recurring guest now at this point i think third or fourth time on jsparty and
[284.60 --> 291.20]  we love having you so welcome and from compressed fm it's our friend amy dutton hey amy how are you
[291.20 --> 295.28]  hey what's up everybody thanks for having me you're always welcome you're always welcome we'll get to
[295.28 --> 302.58]  you eventually k-ball also on the panel we have nick nisi ahoy hoy nick ahoy hoy ready to debate and lose
[302.58 --> 307.28]  what what did your preparation look like nick how many hours how many days how many weeks did you
[307.28 --> 312.24]  spend preparing for this i asked you to remind me what the topic was yesterday and then i did nothing
[312.24 --> 317.80]  and you told me what side i'm debating today and i continued to debate or to look at nothing that's
[317.80 --> 323.48]  the kind of research we do right here at jsparty we are too prepared sometimes they say too prepared
[323.48 --> 328.72]  okay i guess i've stalled long enough k-ball is here he's been on tons of debates always happy to
[328.72 --> 334.14]  have you k-ball welcome to the show i'm excited i'm coming to this one cold nick found out yesterday
[334.14 --> 338.48]  i found out three minutes ago well you're already making excuses for yourselves these guys are
[338.48 --> 343.42]  definitely not going to represent well hopefully our guests are more prepared i know a little birdie
[343.42 --> 349.76]  told me that eric has prepared for both sides so that's some of that soong su art of war stuff
[349.76 --> 354.10]  right know yourself know your enemy i mean he's ready to go i mean shouldn't we say we have a whole
[354.10 --> 359.16]  career preparing for this oh see he prepared that statement you know look at this guy he's ready to
[359.16 --> 366.40]  rock okay so here is the premise should web development need a build step that's the question
[366.40 --> 374.00]  and we'll have two representing the yes answer and two representing the no arguing for yes web
[374.00 --> 382.66]  development should need a build step is nick and eric and arguing against team nope will be amy
[382.66 --> 389.62]  and k-ball we do this quasi formal in so far as we take turns i guess that's as formal as it's going
[389.62 --> 395.64]  to be and then i tally points and they're arbitrary and at the end i forget what the points were and i
[395.64 --> 401.20]  declare myself to be the winner that's basically how these debates go i think i'm undefeated thus far
[401.20 --> 410.54]  and we'll see how well you guys do so let's start with amy we'll go to amy first and then we'll kick it
[410.54 --> 416.80]  over to the other team so amy you have one minute on the clock should web development need a build
[416.80 --> 424.86]  step go no it should not the web was founded on open principles you can run html css and javascript
[424.86 --> 429.14]  in the browser and so you have all the tools that you need you shouldn't have to do any additional
[429.14 --> 434.12]  build steps by adding build steps you're only making it harder for people to get started and
[434.12 --> 438.76]  already the web is so fast and bandwidth is so great that you really shouldn't have to worry
[438.76 --> 443.14]  anymore about compiling i mean minifying or compressing or anything like that you should
[443.14 --> 447.84]  just be able to ship your files and they run within the browser i forgot to mention up top that
[447.84 --> 453.94]  if you hit your timer you'll hear this sound what that's of course bone skull saying what because
[453.94 --> 459.44]  we couldn't afford a actual bell however amy you did not use all your time you used 30 seconds any
[459.44 --> 464.02]  final words or is that your argument in a nutshell you know what this is such a strong argument that i
[464.02 --> 470.38]  don't even think it needs a full minute okay i like that closer what do they say in politics i
[470.38 --> 476.12]  yield my time or i don't know what they say something like that she yields it over we will now go to eric
[476.12 --> 481.80]  for the rebuttal what do you got eric yeah i mean it makes a lot of sense but it's inevitable that there
[481.80 --> 486.18]  will be some sort of bundling for performance reasons and it makes a lot of sense that you want to
[486.18 --> 491.68]  develop the way that your code gets delivered to your end users at the end of the day so bundling will be
[491.68 --> 499.54]  a step building will be a step and you know even though that the web eventually makes its way to
[499.54 --> 504.72]  browsers and language features are there you know we go through our proposal and stages you know one
[504.72 --> 511.02]  two three four five for browser adoption so if you ever want to you know get ahead or take advantage of
[511.02 --> 515.04]  new language features at some point you're going to have to build down to the lowest common denominator
[515.04 --> 520.84]  so i feel since it's an inevitability it's better to just embrace it early pay the tax
[520.84 --> 526.08]  soon up front get it out of the way and then you never have to think about it again i yield my time
[526.08 --> 534.42]  all right thank you keeping chris hiller off the show no need to use that what sound uh strong
[534.42 --> 540.38]  arguments i think but k-ball does now your turn you have one minute to state your case all right eric
[540.38 --> 546.64]  you said the web eventually makes its way to the future we're here baby it's 2024 people are used
[546.64 --> 552.68]  to things being slow because they're dealing with chat gpt all the time so like a little bit of a few
[552.68 --> 557.40]  microseconds you might shave off by bundling does not overcome i mean look at where we are today
[557.40 --> 561.50]  evergreen browsers you don't have to worry about lowest common denominator all these different pieces
[561.50 --> 567.90]  takes me to why if you don't need it you shouldn't do it build steps suck it's additional tooling you
[567.90 --> 571.88]  don't need it it takes time you don't need it it's brittle you have something that's different when
[571.88 --> 576.04]  you're doing local development for fast iteration than you have when you finally ship to the browser
[576.04 --> 582.24]  like why would you do all of that the browser is capable you've got es6 in the browser it's up to
[582.24 --> 586.74]  date you have import maps http2 is in the norm you don't need to bundle to get fast performance get
[586.74 --> 591.78]  things out there and bundling will even sabotage your cache expiry so you might actually give up some
[591.78 --> 598.60]  performance so i think yes you're right at one point in time building was the way to get to the
[598.60 --> 606.32]  future but we're here 2024 you don't need to build stuff what well said kball those bullet points
[606.32 --> 613.84]  sound like they came from somebody smart all right nick you have one minute to uh state your case with
[613.84 --> 621.62]  eric's oh all right well first off uh amy you said that uh there's a big beginner argument that you want
[621.62 --> 627.12]  to keep things simple to make it easy for beginners i agree 100 with that but i think that that's more of a
[627.12 --> 632.92]  dx story and not a case against build steps why does what does the build step have to be difficult
[632.92 --> 638.36]  it could be easy and we could make it easier make the tooling easier uh cable you talk about we have
[638.36 --> 643.46]  this magical world of evergreen browsers and we don't have to think about that that works really
[643.46 --> 649.06]  well if you're in this chromium bubble i guess but even if you want to say that every browser is is
[649.06 --> 654.38]  perfect now uh we have this other problem where we've regressed on the back end and now we have all of
[654.38 --> 660.04]  these back end steps and do you know how to use modules correctly in any given instance i don't i
[660.04 --> 666.80]  want to build step to wash that away for me and so i just need that plus like build steps give me this
[666.80 --> 672.88]  this superpower where i can write this condensed or terse code and have it magically spill out to be
[672.88 --> 679.22]  real code it's the real 10x developer it makes me the 10x developer and i want to embrace that and
[679.22 --> 685.28]  then i'll just drop my mic right here with the word typescript what sorry you still had time left
[685.28 --> 694.06]  but i just had to ask what okay nick drops the typescript mic none of us have yet determined why
[694.06 --> 701.76]  he did that but he did it he was opening the door i got it let's go around two and he is put me in
[701.76 --> 707.92]  coach put me in i was gonna say he's now set up amy for the most epic rebuttal of all times go ahead amy
[707.92 --> 716.76]  you got one minute now nick you mentioned typescript the thing is right now it's might be
[716.76 --> 721.64]  needed for a build step but should it like just because that's the way that we've been doing it
[721.64 --> 727.62]  doesn't mean that it that's the way it should always be done or be done in the future and i think you
[727.62 --> 732.54]  know typescript is fantastic i love typescript but let's just include it in the browser there's no need
[732.54 --> 738.48]  then to have a bundle step if we continue to use these things to push browsers forward instead of
[738.48 --> 745.86]  giving them excuses to uh you know stay in the dark ages and use bundling like let's push our tools
[745.86 --> 752.30]  forward yeah that's my main that's my typescript point okay cable 15 seconds for free if you want
[752.30 --> 758.56]  to use them it is shocking to me absolutely shocking that nick nisi of all people is invoking wanting
[758.56 --> 763.80]  more tooling because i don't know if y'all listen to the deep dive nick nisi uses more tools than any
[763.80 --> 769.40]  human on this planet he spends all his time down in his tools customizing his tools if you want to
[769.40 --> 773.14]  spend your time in tools you can be nick nisi and use a build step but if you want to get on to
[773.14 --> 779.60]  production development you probably shouldn't what please respect the what all right well said well
[779.60 --> 783.68]  said but you use more than 15 seconds so i'm going to dock you three points for that all right eric
[783.68 --> 788.14]  you're chomping at the bit i can see it let's hear it well i mean look you don't have to listen to me
[788.14 --> 792.18]  i mean you can listen to someone like rich harris and be like oh look you know this felt project
[792.18 --> 797.08]  they went to js doc and they're successful with that if you're developing a library that's probably
[797.08 --> 802.34]  true but if you listen to a typescript expert like matt pocock they'll say that you're going to
[802.34 --> 808.26]  continue to have large performance issues and bigger code bases as you grow over time unless you
[808.26 --> 812.78]  actually build your declaration files and that's the only way to be able to get into a more performing
[812.78 --> 818.06]  code base so at some point if you want performance you're going to have to build well said
[818.06 --> 822.24]  yielding the time nick you got 15 seconds that eric didn't use you want to say typescript a few
[822.24 --> 829.62]  times typescript i think the typescript in the browser would be cool except it might slow things
[829.62 --> 835.98]  down i remember the es3 to es5 era and that was a long dark age do we want that with typescript once
[835.98 --> 841.34]  it has to go through standards to get any new features that'd be terrible what all right good point
[841.34 --> 846.38]  cable a minute i'm gonna jump into some of what eric was saying about as you get to these larger
[846.38 --> 851.16]  complex situations and i think that actually speaks to another reason why build steps are bad
[851.16 --> 856.82]  they push you in the direction of additional complexity languages like typescript massive
[856.82 --> 861.56]  libraries that we can just count on our build step to worry about how is it going to truncate all of
[861.56 --> 867.16]  these different things we don't live in the zero interest rate world anymore we can't afford to be
[867.16 --> 874.00]  building gigabytes and gigabytes of javascript we should keep things simple and avoiding a build step
[874.00 --> 879.72]  leads you towards that simple approach less and less javascript is the answer not more and more
[879.72 --> 885.64]  30 seconds amy if you want to use them i totally agree with cable i'm gonna ask that he be on my team
[885.64 --> 886.44]  every single time
[886.44 --> 895.96]  but i think he's right just because you have the complexity and the build steps now doesn't mean that
[895.96 --> 901.42]  we should always have to have them i'm just gonna underline that point again well said okay this ends
[901.42 --> 909.54]  round two i've been keeping score and so far nick has negative three and everybody else has four
[909.54 --> 918.74]  so at that point it's now eight to one team k-ball and amy because eric has scored four points but
[918.74 --> 924.06]  nick has subtracted three off of them it's because of the he said typescript three times and so that's
[924.06 --> 930.46]  three negative points and so we're at eight to one and these points are 100 real and we'll now go to
[930.46 --> 938.84]  our final round in which you pick amongst yourselves one person to make your final case as a
[938.84 --> 946.50]  innocent bystander i will just say nobody has keyed in on the word should maybe that could be a fertile
[946.50 --> 952.60]  ground for argumentation we will start with eric and nick who's gonna make your guys's final argument
[952.60 --> 960.30]  you got one minute who wants to be the representative on team yep eric i think you should do it i'm coming
[960.30 --> 965.20]  in too hot and i'm just i'm shaking here thinking about my build stuff and you're also
[965.20 --> 970.12]  points from your team so far he has outscored you by quite a few so i think that's a good call
[970.12 --> 977.64]  all right eric uh any final arguments before we discuss freely what we really think yeah it's i think
[977.64 --> 984.10]  we're actually all on team build step i think it's just who performs a build step and so i totally agree
[984.10 --> 988.22]  that like you know we should be authoring this stuff in a way that's like simple that's low code
[988.22 --> 992.50]  where you don't have to think about the complexity and you know amy even mentioned moving this over
[992.50 --> 996.58]  to the browsers and that's what happens today with like what language features and so i think
[996.58 --> 1002.90]  we're all on board with like that natural evolution and so to nick's point it sounds like more if it's a
[1002.90 --> 1008.80]  dx issue and like a batteries included issue and you know as a guy who kind of spun up the javascript
[1008.80 --> 1015.68]  fatigue fiasco back in like 2015 or 2017 i wholeheartedly recommend that like the community and the
[1015.68 --> 1020.82]  ecosystem needs to get more mature here with a better out-of-the-box experience and so luckily
[1020.82 --> 1026.88]  we're moving that way with like vtest is getting close to zero config or no config uh matt pocock
[1026.88 --> 1031.56]  even has like a ts config library that just came out last week so you can have like one line typescript
[1031.56 --> 1036.22]  configuration so we're already pushing all that complexity left and eventually it's going to get
[1036.22 --> 1040.26]  towards browsers it's going to get towards your production build pipeline even whenever you publish
[1040.26 --> 1045.46]  packages you can author and typescript in jsr i believe this new package registry will take
[1045.46 --> 1049.68]  care of the compilation and publishing for you so i think we're actually all team build step
[1049.68 --> 1056.80]  well said good choice nick wait let eric take it amy and cabal who wants to represent final
[1056.80 --> 1062.60]  arguments for your team amy i feel like you i saw you reacting so i was gonna point to you
[1062.60 --> 1068.92]  that's up to you i can do it i'll do it i got it i got it she's got it she's got it talked her
[1068.92 --> 1074.02]  into it here we go okay we are all team build step in the sense of i'm not going to write zeros and
[1074.02 --> 1080.66]  one's binary like there will always be some type of build step in that sense but i shouldn't have to
[1080.66 --> 1087.28]  worry about minifying or compressing my code the browser should be able to handle that stuff so i
[1087.28 --> 1092.00]  shouldn't have to have a build step to compile all that stuff to put it in the best most performant way
[1092.00 --> 1098.68]  i should be able to do the typescript stuff we shouldn't make excuses for the tooling or for
[1098.68 --> 1105.44]  the browsers or things like that we should continue to push those forward and i would argue just
[1105.44 --> 1109.96]  because we do that now doesn't mean that that's the best thing or the way that it should be in the
[1109.96 --> 1116.16]  future very well i still have time you know you only had three seconds i was just waiting for it to
[1116.16 --> 1120.98]  run out oh good to give you the what and you finished well all right let's tally the points
[1120.98 --> 1128.04]  looking at these oh wait a second there comes one more argument that wasn't made comes from your
[1128.04 --> 1135.30]  moderator and it goes like this here's cool things that don't need a build step html html doesn't need
[1135.30 --> 1141.52]  a build step css css doesn't need a build step plain text one of the coolest things in the world
[1141.52 --> 1146.90]  plain text doesn't need a build step people people aren't built they're born fully formed
[1146.90 --> 1152.16]  and people are so cool love have you ever heard of love at first sight there's no build step there
[1152.16 --> 1155.74]  it's just a feeling therefore i win
[1155.74 --> 1167.82]  you did you forgot php you you need a mic drop oh php no no amy i said cool things that don't
[1167.82 --> 1174.68]  have a lambo oh thanks for the setup though that was great
[1174.68 --> 1193.92]  what's up friends i want to share an awesome new announcement from our friends over at crab
[1193.92 --> 1202.22]  nebula crab nebula is the official partner of tauri for the uninitiated tauri is a toolkit that helps
[1202.22 --> 1208.22]  developers make applications for the major desktop platforms using virtually any front-end framework
[1208.22 --> 1214.48]  in existence the core is built with rust and the cli leverages node.js making tauri a genuinely
[1214.48 --> 1219.84]  polyglot approach to creating and maintaining great apps so building applications with tauri has
[1219.84 --> 1226.26]  always been an incredibly joyful experience however once the applications are built distributing them
[1226.26 --> 1231.24]  and rolling out updates has always been cumbersome this is why we are thrilled to be part of this
[1231.24 --> 1236.58]  announcement from our friends at crab nebula on their latest product crab nebula cloud the problem
[1236.58 --> 1242.58]  really is the cost of distributing applications the security and the feedback and analytics just think
[1242.58 --> 1249.04]  about cost alone to distribute new applications at scale it can get very expensive when bundle sizes
[1249.04 --> 1254.24]  compound with a number of users which further compounds with frequency of application updates
[1254.24 --> 1260.78]  always be shipping right a 500 meg application distributed across 500 users with nightly updates
[1260.78 --> 1269.36]  leads to a total of around 7.5 million megabytes that's 7.5 terabytes transferred in a single month
[1269.36 --> 1274.54]  now based on popular cloud pricing this could easily lead to a bill in the ballpark of around
[1274.54 --> 1281.56]  90 000 that's a lot of dollars more so distributing updates requires complex cryptography to ensure that an
[1281.56 --> 1286.90]  update is the original safe artifact for users to download install and execute and then collecting
[1286.90 --> 1291.70]  meaningful analytics is more challenging with desktop applications compared to web-based services
[1291.70 --> 1297.76]  impacting the ability to make informed updates and improvements so at the heart of crab nebula cloud
[1297.76 --> 1304.24]  is a purpose-built cdn ready for global scale ensuring seamless integration with any cicd pipeline
[1304.24 --> 1311.58]  and first-class support for github actions and security updates are a first-class citizen leveraging the power of tower
[1311.58 --> 1320.58]  of toweri updater crab nebula cloud provides an out-of-the-box update server that any application call to check for signed updates and if the update is available
[1320.58 --> 1321.58]  immediately download and apply it in an instant over the air and of course toweri is open source and crab nebula is a company born out of open source and they're giving back to the open source community by giving steep discounts and
[1321.58 --> 1344.58]  subsidies to open source projects built with toweri to learn more get started and check out the docs go to crab nebula dot dev slash cloud that's crab c r a b nebula n e b u l a dot dev slash cloud
[1344.58 --> 1354.78]  c r a b nebula n e b u l a dot dev slash cloud once again crab nebula dot dev slash cloud
[1354.78 --> 1363.78]  a solid debate y'all i know we assign sides i'm curious why there was not more emphasis on the should because
[1363.78 --> 1371.74]  whether we need one or not the real debate is should we need one and i think it's a lot harder to argue that we should need one
[1371.74 --> 1377.98]  it's easy i think to argue that we do need one but i think should is a lot harder thing so i think nick and eric had a harder
[1377.98 --> 1383.62]  a harder side to debate if you had drilled down on the should guys cable you ignored it completely
[1383.62 --> 1389.14]  as a seasoned debater i wonder what what's with that strategy so i actually
[1389.14 --> 1397.06]  part of it is because i think we uh that building is actually useful uh you know when we moved from
[1397.06 --> 1402.94]  assembly language to compiled languages that was a step in the right direction it allowed us to move
[1402.94 --> 1408.24]  up several levels of abstraction and forget about all sorts of different types of optimization pieces
[1408.24 --> 1414.40]  that we used to have to worry about do i think javascript is the right target for our build step i'm not
[1414.40 --> 1418.18]  actually sure i think there's all sorts of other different things that we could talk about in terms of
[1418.18 --> 1424.92]  web assembly other different things but having a build step with regards to javascript as advanced as
[1424.92 --> 1429.80]  is in some ways it's also remarkably primitive right now we don't think about more advanced
[1429.80 --> 1434.34]  transformations we historically haven't thought about the levels of abstraction that starts to
[1434.34 --> 1439.22]  unlock now that is changing with some of the more advanced javascript frameworks right so you see
[1439.22 --> 1445.40]  an angular or a quick or these other uh frameworks that are starting to use that compilation step
[1445.40 --> 1452.92]  as a way to unlock new types of interaction paradigms and performance unlocks and things like that
[1452.92 --> 1457.24]  automatically for people and so i actually think we are starting to finally get to the place where
[1457.24 --> 1461.72]  we're using a build step in javascript land to do something useful and not just to work around
[1461.72 --> 1467.70]  problems in the ecosystem but that that having that perspective in the back of my head made it hard for me
[1467.70 --> 1473.00]  to come in from a should perspective uh and so i just stood with the where are we at perspective and
[1473.00 --> 1479.38]  went that way fair i think eric and nick it was smart for you guys to ignore the should because i think it's
[1479.38 --> 1487.78]  harder to state your case on the should than the do we right because i think in i think nine times out
[1487.78 --> 1495.86]  of ten in 2024 you still need a build step i think there are cases where you can write vanilla html vanilla
[1495.86 --> 1504.74]  css vanilla javascript es imported as individual files into a web page and serve that web page i think that i
[1504.74 --> 1510.50]  think that works once out of ten depending on the use case but i think do we still need one today
[1511.22 --> 1516.10]  90 of the time yes so i think that was smart for you all to to ignore the should and talk about where
[1516.10 --> 1519.70]  we're at what are your actual thoughts eric do you think we should need a build step or you think it's
[1519.70 --> 1525.54]  just a sad fact of reality a history yeah i'm trying to i'm trying to grapple with that one especially
[1525.54 --> 1532.10]  recently because i've written libraries without a build step and like rich harris it's like oh it's it's great
[1532.10 --> 1537.62]  being able to just copy paste code if i command click in vs code i go straight to the source
[1537.62 --> 1543.94]  definition if i want to patch you know third-party dependency all the there's no obfuscation it's so
[1543.94 --> 1548.74]  readily accessible and there's there's some caveats i'm sure with it but it was nice to be able to like
[1548.74 --> 1553.86]  prove that's possible but it definitely was like the untrown path and so when i think about like a
[1553.86 --> 1559.30]  build step outside of like do versus should i think about well what should a build step be doing
[1559.30 --> 1564.42]  that i don't really want to do i think about react compiler recently where you don't change the way
[1564.42 --> 1570.50]  you author your code but the compiler is making your code more performant just because you're adhering
[1570.50 --> 1574.74]  to like you know the paradigms and patterns within like react and i think like that's probably the
[1574.74 --> 1580.98]  more compelling case for should is whenever you buy into patterns of the ecosystem or language features
[1580.98 --> 1587.78]  or whatever you should have the computer making your code better more correct more performant like for free
[1587.78 --> 1592.74]  but whether or not that's that's a detail that you have to pay attention to is is the is a part where
[1592.74 --> 1597.14]  i'm like hung up on i'm yeah very much wanting everything to go to the left of like i shouldn't
[1597.14 --> 1601.70]  have to think about it and this should just become table stakes for i'm just going to write my stuff
[1601.70 --> 1608.82]  focus on the differentiating logic and the should is going to be outside of my responsibility so it's it's
[1608.82 --> 1615.06]  tough yeah i mean i think that is a really good point i think that performance optimizations are at
[1615.06 --> 1620.98]  odds with clarity and readability they always have been and oftentimes you'll find the code base where
[1620.98 --> 1628.90]  a certain code path needs to be highly optimized to run at speed or at low resource and you'll find
[1628.90 --> 1634.34]  comments in that section like here be the dragons because somebody has personally you know by hand
[1634.34 --> 1639.22]  done some fancy memory allocation stuff or whatever it happens to be in order to make that particular bit
[1639.22 --> 1644.98]  of code more performant right and therefore you it's hard to read because you're like what are they
[1644.98 --> 1652.18]  doing here it's it's some fancy footwork and ideally you could have both the both things you could have
[1652.18 --> 1660.26]  the clear right idiomatic code that is linting and everything else is great and your type trip compiler is
[1661.06 --> 1667.22]  nowhere to be found because you don't need one and everything's hunky-dory and then also get the performance
[1667.22 --> 1672.50]  right and really i mean that's kind of what react compiler's premise is right like don't rewrite your
[1672.50 --> 1678.82]  code right the way you'd normally write it and don't worry about hyper optimizing in the small we will do
[1678.82 --> 1685.62]  that work for you and i think that is a win-win nick do you have anything else to add besides the typescript
[1685.62 --> 1690.82]  stuff i mean you're kind of you're kind of a single faceted over there oh no not at all i mean that's just a
[1690.82 --> 1696.90]  perfect example i think like there's a lot of innovation that happened because there was this build
[1696.90 --> 1702.10]  step and it wasn't even really like introducing a build step you know before that there was things like closure
[1702.10 --> 1707.70]  compiler and like you know we were really relying on that for doing things like like doing a lot of
[1707.70 --> 1713.54]  optimization to make the web faster automatically things like dead code removal for example tree shaking
[1713.54 --> 1719.38]  those types of things but also like there's a lot of innovation that comes when you can add a build step
[1719.38 --> 1725.30]  a perfect example would be jsx like that's not actually part of javascript but we all probably use it
[1725.30 --> 1730.18]  with some framework or another at this point uh and that wouldn't exist without a build step and they
[1730.18 --> 1736.02]  could build that into the browser but how would they mess it up i i only like wonder that because
[1736.02 --> 1742.10]  you look at things that we have today like the dom api how easy is that or the web component spec like
[1742.10 --> 1748.42]  how easy are those to build with they're they're not which is why jsx is still like a prevalent thing for
[1748.42 --> 1753.14]  things like solid and for react and for other ones so there's a lot of innovation that comes from that
[1753.14 --> 1759.94]  but then uh as eric was mentioning like there's a lot of innovation that gets built on top of that
[1759.94 --> 1766.02]  to reduce the footprint that the build step takes in like a developer's mind or in like the the process
[1766.02 --> 1772.34]  the the flow of a of an everyday developer and i'm thinking of things like uh like uh the svelte
[1772.34 --> 1778.26]  compiler right you you write you can write this like regular code uh and then the compiler like figures out
[1778.26 --> 1781.94]  what needs to be reactive and now they have like the runes thing with signals and all of that but
[1781.94 --> 1787.22]  like we're moving more towards these primitives that make it easier to remove some of that compiler
[1787.22 --> 1792.90]  magic and make it easier but then we have things like uh tailwind tailwind has a build step because
[1792.90 --> 1797.78]  it takes the classes that you build that you actually use and builds them down and what's the
[1797.78 --> 1804.18]  big thing in tailwind 4 it's basically the removal of the config file for their build step in a big way
[1804.18 --> 1809.30]  and kind of moving it back into css so it's just dx improvements on top of the existing build step but
[1809.30 --> 1815.22]  the build step's not going away yeah i mean i feel like those performance pieces where it's like
[1815.22 --> 1818.82]  build this down compile those are the least interesting ones the ones that you highlight
[1818.82 --> 1826.18]  like jsx that's creating a new dsl for writing html that's a new abstraction it's a new way to think
[1826.18 --> 1831.14]  about things that lets you operate at a higher level of abstraction and be more productive that's where
[1831.14 --> 1835.78]  a build step gets really interesting um it allows you and it allows you to experiment with that in user
[1835.78 --> 1840.58]  space as you highlight so you don't have to do that innovation you know at the level of standards
[1840.58 --> 1847.06]  and browser so yeah i think there there's these two pieces here but the innovation side is what's
[1847.06 --> 1852.74]  really interesting and as build steps are becoming so prevalent because typescript is which it is a
[1852.74 --> 1857.38]  forcing function i think it unlocks things like that and i don't know that we've talked about this on
[1857.38 --> 1862.74]  the show but like languages like elm or other stuff where it's like let's just explore a fundamentally
[1862.74 --> 1869.86]  different way of writing our code thinking about our code and the build step lets us do that and
[1869.86 --> 1875.86]  compile it down to something that'll run today i genuinely do think we shouldn't need one but i think
[1875.86 --> 1880.82]  the performance argument is really interesting because like you said it is boring like i'm not going
[1880.82 --> 1887.22]  to write my javascripts or my css for that matter with like class a class b class c like that's unreadable
[1887.22 --> 1892.50]  but like when i say oh we can push stuff to the browser bandwidth is great i'm coming at that from
[1892.50 --> 1898.50]  a place of privilege and when you start thinking about things that need access now there are places
[1898.50 --> 1904.66]  where they don't have that same privilege a compiler that will minify all that stuff for you really does
[1904.66 --> 1909.30]  make a huge difference or when you're talking about spa applications and the fact that you can bundle
[1909.30 --> 1914.42]  pieces of javascript to send to the browser as you need it like that's a another huge performance gain i
[1914.42 --> 1920.74]  don't want to send a giant spa to the browser to download i mean everybody hates that giant wheel
[1920.74 --> 1927.62]  of like loading right yeah i agree i think http 2 is supposed to be our savior on a lot of this stuff
[1927.62 --> 1933.78]  because it was designed at least the tagline or some of the sales pitch was like you don't need
[1933.78 --> 1941.22]  like it's just as fast with h2 to send 15 small files as it is to send one large file which is what a
[1941.22 --> 1945.78]  lot of javascript bundling was about like let's just take all of our files into a single file because
[1946.34 --> 1952.50]  with h1 that multiplexing is not h1.1 there's like the feature but anyways there's like a connection
[1952.50 --> 1957.86]  each time i don't know the details anymore but it was just much faster to send one large file than 15
[1957.86 --> 1962.58]  small files and it's supposed to be with h2 that that was inverted and it's no longer a huge
[1963.38 --> 1970.18]  optimization to do that however it just seems like in reality that has not played out to be as much of a
[1970.18 --> 1976.82]  win as many of us were hoping for and so yeah i agree they put in everything as small and as
[1976.82 --> 1982.26]  packaged as possible especially on resource constrained devices and resource constrained
[1982.26 --> 1987.06]  areas is a huge win cable's point that i think might have been read out of the bullet points
[1987.06 --> 1992.90]  about cash expiry is a real one though so uh one big bundle you know you whenever you change something
[1992.90 --> 1998.58]  you expire the entire cache versus expiring smaller caches is a loss but i think it's a net win
[1998.58 --> 2004.10]  still from what i've seen did read that straight out of your points that came from you jerry to
[2004.10 --> 2008.82]  oblige i thought it sounded familiar that's why i won cable that's why i won nobody has actually
[2008.82 --> 2015.70]  addressed the root argument that love doesn't need to be built why should our websites need to be built
[2015.70 --> 2023.06]  it just needs to be maintained that's true uh well said well played i was gonna say that it's false
[2023.06 --> 2030.26]  it's a it's a false comparison i think uh maybe not every love is built some may arrive at first
[2030.26 --> 2035.38]  sight but many loves are built over time that sounds a lot like websites too well said i was
[2035.38 --> 2040.50]  curious like is is this a problem you know like with the build step to where it's becoming a smaller
[2040.50 --> 2047.38]  footprint like is this a spa air era kind of issue of like too much javascript and we're seeing
[2047.38 --> 2052.98]  i was looking at htmx not not just htmx as a library but how do they maintain it it's like a
[2052.98 --> 2059.70]  single deliverable file that's es11 compatible so it's authored without a build step in an es11
[2059.70 --> 2066.18]  compatible way so no es6 features until i guess like the next release um where they become es6 compatible
[2066.18 --> 2071.86]  but i think that's kind of like fascinating that we're we're pushing less of the client-side interaction
[2071.86 --> 2079.30]  into server-side behaviors and having you know islands and astro or react server components so
[2079.30 --> 2084.66]  like maybe some of the stuff of like the promise of http 2 is is less impactful because we're just
[2084.66 --> 2089.38]  trying to not send as much javascript anyway and we're trying to go to zero javascript i think the
[2089.38 --> 2094.58]  pendulum has has definitely swung that way and i'm here for it i think that's great there's a whole
[2094.58 --> 2099.70]  lot there's 10 years of spas that are just massive that are sitting out there in production apps that
[2099.70 --> 2105.46]  are three megabyte bundles and people are downloading all the time so while we are seeing that as a
[2106.02 --> 2113.14]  as a burgeoning trend and one that i hope continues i think that there's a whole lot of web apps that
[2113.14 --> 2121.46]  are just massive bundles of javascript still and i think that process is going to be one of tooling i
[2121.46 --> 2128.18]  think and trending versus you know switching i don't know i just see a lot of legacy out there
[2128.18 --> 2133.14]  that's just not going to change i mean jquery is still on 80 of websites is it 80 i was like that's
[2133.14 --> 2139.94]  probably two years old but that was about the number and so how long will large single page
[2139.94 --> 2146.34]  applications be that have were written years ago it's just still what they are it's it's a hard
[2146.34 --> 2150.90]  problem to to go ahead and either rewrite or actually a rewrite is probably easier than a
[2150.90 --> 2156.82]  transition in many cases and you know how how difficult big rewrites are yeah if a 13 megabyte
[2156.82 --> 2161.54]  single page app at work that i'm trying to figure out what is the future for this thing all right
[2161.54 --> 2166.66]  well what have you figured out so far it's kind of like what horse am i going to bet on to bring me
[2166.66 --> 2172.58]  into the future and so the recent announcement of react router or remix becoming react router is very
[2173.14 --> 2179.62]  pertinent so i was able to go from react router three to react router five and so the promise or at
[2179.62 --> 2184.82]  least the hope that i have is that anchoring to something like react router will let us push the
[2184.82 --> 2190.82]  complexity to the left eventually just server side render and do go from like a client loader to a
[2191.38 --> 2197.22]  server-side data loader because really the benefit that we want is to just have reloadable pages with
[2197.22 --> 2202.18]  smaller js bundles and so that's that's like the really compelling thing is i just wish there's one
[2202.18 --> 2207.62]  way to where like i could take a legacy spa and say just analyze my routes and turn them basically into
[2207.62 --> 2213.06]  like a file system individual bundled route that's that's really all i really want and so if all anything i
[2213.06 --> 2217.46]  have to do is just update react router to make that work that's that's isolated like one file
[2217.46 --> 2223.30]  yeah that's a huge win if that could actually work fingers crossed can you quickly flesh out all the
[2223.30 --> 2226.74]  things that go through your head when you say pushing to the left because you've used that phrase a number
[2226.74 --> 2230.42]  of times and i'm not sure that's something that all of our listeners are going to be familiar with
[2230.42 --> 2236.34]  yeah yeah it's and i'm likely in a bubble too is that um you know so i i think of like a feature kind
[2236.34 --> 2240.50]  of originating you know somewhere like on the server where it's deployed and then like to on the
[2240.50 --> 2244.50]  the furthest to the right is where the user is actually interacting with it so like often whenever
[2244.50 --> 2249.06]  you see like a diagram of like here's a network request and like it kind of goes through back and
[2249.06 --> 2253.78]  forth and the arrows point left and right it's kind of like that it's um you know so like if there's
[2253.78 --> 2259.06]  local code to the left of the local code would be like you know your cicd and to the left of that would
[2259.06 --> 2264.02]  be like production and that sort of thing so whenever i say something like pushing to the left what i
[2264.02 --> 2270.50]  really mean is like pushing it down away from users into like another layer yeah so from the
[2270.50 --> 2275.30]  client's responsibility down to the server responsibility right there's this term shift
[2275.30 --> 2282.50]  left which exists in a lot of i would say enterprise development contexts where you have especially
[2282.50 --> 2288.50]  around information security and best practices they will say you need to shift it left meaning
[2288.50 --> 2294.42]  make it earlier in the software development life cycle versus a thing that you put in at the end
[2294.98 --> 2300.26]  because well with security you can't actually bolt it on at the end if you're trying that you are
[2300.90 --> 2306.02]  doomed to fail and so i think pushing left shifting left these are terms that i've also had to wrestle
[2306.02 --> 2311.54]  with but now i know what they mean good good question cable to clarify to get all of us on the same
[2311.54 --> 2316.18]  page amy you you wanted to talk about shifting left php some more i know i pick on php it's just
[2316.18 --> 2322.58]  because it's fun i got no problem with the language in fact i have a lot of my career to php that being
[2322.58 --> 2327.78]  said you mentioned you want to you want to make the case why php is better than ruby and java i don't
[2327.78 --> 2333.14]  know if that was just a joke or if you actually have brought argumentation but i thought hey uh we've
[2333.14 --> 2338.74]  explored the build step i think probably to its logical conclusion this might be an interesting
[2338.74 --> 2343.78]  conversation do you do you like php better than ruby and java amy i do just because i know it
[2343.78 --> 2350.66]  okay so i did say it as a joke but i like knowing that it's gonna you know get some people excited
[2350.66 --> 2358.10]  yeah ruffle a few feathers but um yeah i mostly like php just because that's what i learned early
[2358.10 --> 2362.66]  on like i was building wordpress sites and the fact that i didn't have to worry about it build stuff i
[2362.66 --> 2368.66]  just upload a php file to a linux server and it works like that's feels magical as a beginner so
[2368.66 --> 2374.58]  that's kind of where that beginner argument comes from but i've recently been digging into laravel
[2374.58 --> 2380.18]  and really been watching the laravel verse full stack javascript debate online which has been really
[2380.18 --> 2386.02]  interesting and so you know i think it enter does enter this conversation when you start talking about
[2386.02 --> 2394.10]  a build process and the fact that you can just put a file on a server and it runs yeah that is the magic of php
[2394.10 --> 2399.62]  i used to even take my index.html and i remember just changing the file extension and then it would
[2399.62 --> 2404.90]  execute dynamic code you know and it was just so cool it's so easy and i built a lot of stuff that
[2404.90 --> 2409.86]  way or you just have your includes yeah exactly just start writing some php code i think i think i've
[2409.86 --> 2416.34]  mentioned it on this show before but my first attempt at a blog was a single php file and whenever
[2416.34 --> 2424.02]  i added a new blog post the php file just appended to itself with that post warnings warning do not try
[2424.02 --> 2431.14]  this at home i always have to disclaim that whenever nick brings it up this was an ingeniously
[2431.94 --> 2440.58]  naive thing to do nick did you have a guest book and a counter on your site as well i did it was
[2440.58 --> 2447.78]  of that era oh visit counters are cool i definitely had one of those i feel like that is one of those
[2447.78 --> 2452.66]  examples where you learn by doing uh and you do it and then you learn to never do it again yeah does
[2452.66 --> 2458.98]  that ever bite you nick oh probably that doesn't exist anywhere anymore so there's a reason the only
[2458.98 --> 2463.14]  thing worse you could do is actually like put a notice in your comment form like by the way when you
[2463.14 --> 2469.14]  write this comment it's going to execute server side on my vps you know just let them know they
[2469.14 --> 2474.18]  have to even do a javascript alert and see if it actually you know triggers i'm pretty sure it
[2474.18 --> 2480.18]  wasn't password protected in any way either so you know i was doing everything right was this a school
[2480.18 --> 2486.10]  project or no i was in school yeah i was in school but it was my personal blog at the time right when i
[2486.10 --> 2493.30]  was in school we only got one meg on the school server which oh you'd fill that up pretty quick with a
[2493.30 --> 2500.74]  comment form or one image oh yeah that's true one meg image yeah you have to use one of those small
[2500.74 --> 2505.14]  language models on that one don't bring it up jared don't bring it up we're not going to talk about
[2505.14 --> 2510.50]  language models in this episode i promise myself those could become your new build step right you
[2510.50 --> 2516.10]  write some sort of uh text based thing and then you run it through a language model to generate your
[2516.10 --> 2521.30]  typescript and then you run the typescript through a build process i would like to fund your startup
[2521.30 --> 2528.50]  no anyway yes if you said ai you should go back to this php blog idea that nick made let's fund that
[2528.50 --> 2533.54]  startup you know i bet you an llm will do a better job on that blog that's not hard
[2535.62 --> 2540.98]  a lot of my first server-side dynamic programming was hacking my wordpress blog like just actually the
[2540.98 --> 2546.66]  word pimping is probably better than hacking like back when i got started everybody's sidebar had cool
[2546.66 --> 2552.02]  stuff in it like your latest scrabbles i know you guys were last fm people but you'd like and it was
[2552.02 --> 2557.14]  so cool to listen to a song in your itunes and then go to your own website and be like jared just listen
[2557.14 --> 2564.02]  to hit me baby one more time by britney spears you know for instance last week what else did i throw in
[2564.02 --> 2568.90]  there images off flicker right just like pulling in all the things like here's all my socials i'm gonna
[2568.90 --> 2575.86]  pull them into my sidebar and that was surprisingly productive learning let's bring it back yeah right
[2575.86 --> 2581.54]  like currently reading we should where's the flicker nowadays there's no flicker say rip but i do think
[2581.54 --> 2585.94]  they're still around everyone just posted on instagram i guess all right but not really want to make a
[2585.94 --> 2590.82]  case why php is better than ruby or java fair enough it's better because you can just switch your
[2590.82 --> 2598.26]  html file to php and just execute and nobody has been able to match that developer experience yet really
[2598.26 --> 2603.94]  well i will say to nick's point you can make a typescript file by just changing the extension
[2603.94 --> 2610.42]  from js to ts true but it won't turn a static file to a dynamic one right right right it's just
[2611.06 --> 2617.14]  create it's just changing a perfectly good javascript file into well you know a better one
[2619.06 --> 2623.22]  all right well any other topics you want to take up i pasted this in the chat but i was curious about
[2623.22 --> 2630.74]  it though like what what is the gap that still like forces us to build that could potentially go
[2630.74 --> 2635.86]  away like so typescript's a big one right and typescript is it moves fast and apparently you know
[2635.86 --> 2641.62]  even minor changes can have breaking changes uh but there is some sort of like annotation comments
[2641.62 --> 2645.46]  coming to javascript i think i don't know where it is in terms of like staging but like some sort of
[2645.46 --> 2651.46]  typing or type checking proposal stage one yeah and so you have something like that and and jsx is the
[2651.46 --> 2656.58]  only other thing that kind of stands out to me of like if both of these frontiers you know had a
[2656.58 --> 2664.42]  solution for it that would be vanilla js would that would that become like uh yeah the final you know
[2664.42 --> 2670.10]  unburdening to let us actually have a real conversation of like okay do we need to have a build step anymore
[2670.74 --> 2674.74]  yeah what else would be missing i think you might still just have the performance argumentation and
[2674.74 --> 2681.14]  that's probably about it right okay ball what else we missing so i think once again i
[2681.14 --> 2688.50]  i'm going to bring this back to aspirations rather than current state because i i do think as we sort
[2688.50 --> 2692.98]  of hashed out in the debate with the current state we're actually shockingly close and to your point
[2692.98 --> 2699.54]  like if you get jsx in there like maybe a little bit of an alternate take on typescript that can work
[2699.54 --> 2706.42]  like you're fine i believe that that is underselling what we can do with a compilation step
[2706.42 --> 2713.22]  and i would look towards things like what quick is doing things like what svelte is doing things like
[2713.22 --> 2720.74]  what angular is starting to do where they are extending the set of primitives that are available
[2720.74 --> 2726.34]  and saying hey if you build something like this in this form it's like an extended version of what react
[2726.34 --> 2731.78]  is doing where this you know we take this to have special meaning that the compiler will then do
[2731.78 --> 2739.22]  transformations on and enable new capabilities and so i i actually think you know rather than asking
[2739.22 --> 2745.70]  what would it take to remove the build step we should be asking what new performance and productivity
[2745.70 --> 2754.82]  gains could we unlock if we think more about what we can do in a build step if we take more inspiration from
[2754.82 --> 2762.50]  compiled languages if we look at you know the different types of things that are hard to do
[2762.50 --> 2769.30]  in the web ecosystem today but by perhaps can constraining ourselves or doing something we could
[2769.30 --> 2775.62]  actually do automatically using a compiler i was very jfk i like that you know ask not what your build
[2775.62 --> 2779.62]  step can do for you but what you can do for your build step i mean i just fundamentally think we should
[2779.62 --> 2785.14]  be raising our aspirations here right like i think you know the web is incredibly powerful
[2785.86 --> 2792.26]  but there's so much more we could be doing with it and we we do see these sort of unlocks of like
[2792.26 --> 2799.22]  fast by default or like i mean you look at the islands stuff right like could that be we're explicitly
[2799.22 --> 2804.10]  configuring that could that be automatically detected in the way that like a quick does where it's just
[2804.10 --> 2808.58]  like it only loads it when you need to load it like all those different areas and i think the answer is
[2808.58 --> 2814.82]  probably yes but not if our goal is to do a buildless build or a buildless ship i think it's
[2814.82 --> 2820.02]  probably more embracing the things that where you say can we do a full analysis of this thing
[2820.02 --> 2826.82]  at build time when it's cheap and we're doing it once and optimize it so and transform it so that then
[2826.82 --> 2833.38]  when people are running this thing it is magical i don't know i think we've reached the pinnacle i can
[2833.38 --> 2840.50]  write sql statements in my react components now no comment from nothing wow he didn't even like
[2840.50 --> 2846.02]  look at you quiet he's like i'm not even gonna acknowledge that well i guess the question i mean
[2846.02 --> 2854.58]  cable i guess what you're saying is that a build process is i don't use the word a shim but it is a
[2855.22 --> 2860.18]  a way of pushing the platform forward like the platform is always going to trail the builders and
[2860.18 --> 2863.46]  the builders will be the ones who innovate and then that goes into the platform because i think
[2863.46 --> 2868.34]  what eric's question is is like what would need to be in the platform for it to be sufficiently optimal
[2868.82 --> 2874.26]  to deliver high quality web apps with all the best things without additional tooling no i'm gonna i'm
[2874.26 --> 2880.50]  gonna bring it back to to this concept of shifting left right and thinking about when you should do what
[2880.50 --> 2885.14]  so we think about this in terms of when we're developing things pushing things out to the edge pushing
[2885.14 --> 2891.14]  them close to the user but i think there's also a perspective of like a build step is conceptually a
[2891.70 --> 2897.46]  it's a pre-compilation it's an opportunity for us to do a whole bunch of assessment analysis and work
[2898.18 --> 2905.46]  before this thing ever gets close to a user and there's a set of things that we can do at that time
[2906.34 --> 2912.26]  that we're already doing but there's also probably a whole class of things that we have not yet explored
[2912.26 --> 2918.26]  where we could be optimizing this where we could be enabling ourselves to write software in a different
[2918.98 --> 2925.06]  more expressive way that then is handled before we have to worry about what is actually shipping out and
[2925.06 --> 2930.74]  getting touched by a user actually using that example of you know edge based services versus not
[2930.74 --> 2935.62]  like if you have a multi-tiered operational infrastructure let's say you have something that is
[2936.26 --> 2940.58]  you know has a set of edge functions but also has some things that have to be centralized and doing
[2940.58 --> 2945.94]  things one could imagine having a language that gives you enough expressiveness in the language that
[2946.26 --> 2950.50]  a build step can automatically assess okay here's the sets of things that can be split off and sent
[2950.50 --> 2954.10]  to functions that run on the edge here's the set of things that need to run in my central server
[2954.10 --> 2957.22]  here's the set of things that i can run at build time because they're going to be the same every
[2957.22 --> 2963.06]  single time and just push those up as static right like there's no reason we can't do that in fact i think
[2963.06 --> 2968.34]  there are some frameworks that like doesn't next do some of this where if you build it it can like push out
[2968.34 --> 2974.02]  some of its api endpoints to be you know edge functions and things like that like that is the type of thing
[2974.02 --> 2983.94]  that you can do at compile time that will save you loads of things at runtime and if we think about a build
[2983.94 --> 2989.86]  step not as a burden that we're trying to get rid of but rather an opportunity to let us think about things in a
[2989.86 --> 2996.34]  different way it can help us write simpler applications that still take advantage of our sort of multiple layers of operational infrastructure
[2996.34 --> 3002.82]  i just don't see how you can push further left than the platform like isn't that the furthest thing left and i don't just mean the
[3002.82 --> 3009.26]  browser i mean we also have the transport layer i mean we have the application layer we have layers below where we are writing
[3009.26 --> 3017.30]  code which would be further left in my opinion and more optimal than a compilation step wouldn't they not necessarily because
[3017.30 --> 3026.34]  they don't necessarily know your project model right so like it doesn't make sense to include my application logic
[3026.34 --> 3034.10]  in the platform but it might make sense to analyze my application logic at build time and say oh here's a set of
[3034.10 --> 3042.58]  things that we can pre-compute for you here's a set of things that we know you're not going to need on first page load so we'll split those out into a
[3042.58 --> 3050.82]  bundle that loads lazily right like there's all these different pieces of my application logic that don't have to
[3050.82 --> 3061.22]  actually arrive in one big blob of javascript that gets loaded by the user right or many small bundles of javascript that get loaded by the user
[3061.22 --> 3069.82]  yeah i just i i'm thinking do you include your web server as your application logic because i just feel like there's a lot of things you can do
[3069.82 --> 3077.50]  dynamically with your web server that are going to you can give those contextual hints to whether it's headers or whatever it is
[3077.50 --> 3085.14]  that don't require a build step like they're at request time so that was i that was a form of a question maybe it didn't sound like it
[3085.14 --> 3093.18]  are you excluding the web server from the application layer in this context or do you look at that as part of your application
[3093.18 --> 3097.42]  maybe that's a question for everybody like when you write an app do you think about the web server like a
[3097.42 --> 3103.82]  a server side rendered maybe it has some front end stuff as well do you all think about the web server
[3104.38 --> 3109.74]  as part of your application because here's here's a context in which i've expanded my my definition of
[3109.74 --> 3114.22]  my application because we have a cdn in front of our stuff it's out it's fastly right now it has a bunch
[3114.22 --> 3119.34]  of rules and stuff and i was complaining that i'm putting too much rules over here in the in the fastly
[3119.34 --> 3124.70]  dynamic routes and stuff and i want it in my application and then somebody said no that is your application
[3124.70 --> 3129.82]  and i was like yeah i guess you're kind of right and so now all of a sudden my third party cdn which
[3129.82 --> 3135.82]  has is effectively varnish in the cloud it actually is have a lot of logic that it's contextual to what
[3135.82 --> 3141.26]  we're up to there and so i shouldn't be thinking get it out of there unless i don't want it there
[3141.26 --> 3145.58]  i should be thinking like that also is part of my application so a lot of us i think either think
[3145.58 --> 3149.98]  in a front end or they think of a full stack and you're still just talking about dynamic application
[3149.98 --> 3155.02]  serving and not even broader than that which is like your web server is a very powerful tool
[3155.02 --> 3160.54]  you're getting all the way down into infrastructure as code right so where this starts to where this
[3160.54 --> 3165.66]  is really a question of is how are you thinking about managing and deploying and versioning these
[3165.66 --> 3170.54]  things at the scale that you're talking about right now you have what i think in that world would
[3170.54 --> 3176.78]  be called a pet as your server right you have one that you have carefully configured and set up
[3176.78 --> 3181.74]  it is a part of your application stack and it's there and i think as you scale up you need to
[3181.74 --> 3185.82]  transition from a model of these things as pets to these things as cattle where you can spin them up
[3185.82 --> 3191.98]  and spin them down at which point you need to much more carefully be able to manage their configurations
[3191.98 --> 3197.50]  in a way that is versioned and controlled so i think it's it's less like yeah that is all part of
[3197.50 --> 3203.34]  your boundary um that you can play with and how you think about it depends on your needs and like
[3203.34 --> 3210.30]  what level of kind of scaling and version control and team management you need to enable
[3211.02 --> 3215.74]  i don't understand why you think it's a pet where did you get that from because you have a single
[3216.38 --> 3221.90]  place that you are configured that you have hand tuned i mean that would be basically that is my code
[3221.90 --> 3227.10]  though there like that's still infrastructure as code like there's not a single machine yeah i guess
[3227.10 --> 3231.74]  that's it's like a it's like a mesh network of things that go all around the world right okay that's
[3231.74 --> 3238.22]  fair so yeah maybe it's not a pet so when you go to build time like are you just talking about my node
[3238.22 --> 3244.86]  app and my front end code are you talking about the holistic system that's where i'm good which are you
[3244.86 --> 3248.70]  talking about i think you could you could make an argument either way well i was wondering which one
[3248.70 --> 3253.58]  you were talking about i don't have an argument over here i'm just trying to follow i think your i
[3253.58 --> 3258.86]  guess your argument is that build steps should be a part of that no matter what your setup is because
[3258.86 --> 3263.58]  you can do fancy things at build time yeah it's interesting especially here in like you know the
[3263.58 --> 3268.94]  pet cattle analogy and it's in my mind it's like what i want to concern myself with you know what
[3268.94 --> 3274.94]  is what's the thing that i feel is like a responsibility for deliver value for the business you know and i
[3274.94 --> 3281.18]  want to make sure that's as high as possible with like as low noise and complexity you know infrastructure
[3281.18 --> 3285.74]  is code i i'd rarely like to deal with unless it's going to have some sort of differentiating value
[3285.74 --> 3291.42]  and i think that's like the benefit of platforms like versell where the abstraction is something
[3291.42 --> 3298.38]  like next or svelte and how it gets deployed uh you might just write you know a three-line function
[3298.38 --> 3303.18]  that returns hello world underneath like pages slash api slash whatever that's all you're concerned
[3303.18 --> 3307.74]  with that's what your application is that's what your business needs how that gets deployed it's not
[3307.74 --> 3312.22]  really your concern it becomes a responsibility of like the frameworks output and i think like that's the
[3312.22 --> 3318.14]  thing that's kind of like powerful is finding either language abstractions or like um you know like
[3318.14 --> 3323.10]  project you know file system conventions with like routing and other things like that to give you like
[3323.10 --> 3329.42]  the right set of primitives and you know i'm trying not to say like move it to the left but uh but now it
[3329.42 --> 3335.34]  becomes a responsibility of like your deployment platform on you know what how does this actually go out
[3335.34 --> 3343.74]  in a performant way so whenever you know um a hosting provider puts you know ddos protection in front
[3343.74 --> 3348.62]  of my site for free that's part of like the reason why like i want to leverage that abstraction versus
[3348.62 --> 3353.18]  writing my own infrastructure as code and having to configure my own like aws resources and
[3353.82 --> 3358.30]  uh arns and all that sort of stuff and so that that's the way i kind of see it is that there's a point where
[3358.30 --> 3363.02]  you kind of have to draw a line in the sand and say what i want to be responsible for and over time we're
[3363.02 --> 3369.02]  continually trying to make that as small as possible and have like terse clear code specific
[3369.02 --> 3374.06]  to the problem i'm actually solving for and not trying to solve for you know what does it take
[3374.06 --> 3379.66]  to get this thing out in the latest greatest you know safe performant way well said totally agree with
[3379.66 --> 3386.14]  that amy or nick either one of you want to chime in on this i don't think i have any anything to add
[3386.14 --> 3393.66]  that i think if i i rely so much on the tooling stuff of that and nick i know you said you love
[3393.66 --> 3399.82]  your tools i love my tools as well and some of that stuff to me is just table stakes when i look at
[3399.82 --> 3407.74]  hosting platforms and things like that to handle that stuff for me and like i can talk about tooling
[3407.74 --> 3411.74]  and bundling let them do all the work i don't want to have to worry about it i don't have to think
[3411.74 --> 3416.30]  about caching you know just the only time i care about caching is when i try and update something
[3416.30 --> 3421.26]  and it's not reflected on the site you know in that case give me a good way to bust it but
[3422.06 --> 3426.54]  other than that i would rather solve different problems fair nick let me ask you this question
[3426.54 --> 3434.14]  so we are web developers how much do you think about consider and use the http protocol in your web
[3434.14 --> 3440.22]  development are you leveraging http like do you use the compression the cookie i mean obviously we use
[3440.22 --> 3444.30]  cookies for that kind of stuff but i mean there's all kinds of things you can do with caching and
[3444.30 --> 3448.62]  that's that's an application layer protocol but it's one that it seems like a lot of us are largely
[3448.62 --> 3453.98]  ignoring and i'm wondering i'm not i'm not necessarily casting judgment for ignoring that i'm just wondering
[3453.98 --> 3459.90]  how much are we thinking about http as web developers and you are more of a full-time web developer than
[3459.90 --> 3465.90]  i am even these days so are you actively thinking about http in your day-to-day work nope
[3465.90 --> 3474.06]  okay uh yeah no i i just i don't think about it too much fair answer yeah uh amy same yeah well i was
[3474.06 --> 3480.06]  just gonna i don't think about it but i am gonna throw a thought out there i wonder if some of this
[3480.06 --> 3485.10]  just comes down to the fact that like with the javascript world we've become more serverless and so
[3485.10 --> 3492.78]  i do rely on tools like versell or netlify just to hey here's my github and go ahead and take my site
[3492.78 --> 3497.74]  put it up there and then i don't have to worry about it and so it'll be interesting as this pendulum
[3497.74 --> 3501.58]  swings the other way and then we have react server components we're having to configure servers
[3501.58 --> 3506.14]  we're having to think more about databases and how we interact with those different layers
[3506.14 --> 3511.98]  that all of a sudden now caching and http too like all these things they start to enter the
[3511.98 --> 3517.36]  conversation more because we don't have necessarily the tooling that handles it or doesn't handle it yet
[3517.36 --> 3522.40]  i think a lot of this comes back to kind of what eric was saying in terms of identifying the
[3522.40 --> 3527.52]  business problem we're trying to solve and doing the minimum possible things having the minimum set
[3527.52 --> 3532.72]  of things under our control to solve that and shifting as much of the rest of it as you can into tooling
[3532.72 --> 3540.00]  platform etc and depending on what you're solving as you start to expand bigger and bigger problems
[3540.00 --> 3547.60]  and also depending on the types of scale that you're addressing those things become things you
[3547.60 --> 3552.48]  start to have to worry about so there's a tremendous range of things that you can throw static html and css
[3553.12 --> 3560.88]  up on a static server s3 bucket what have you and you have solved the problem and now there's so many
[3560.88 --> 3566.40]  problems you don't have to worry about and that's phenomenal and then there's a layer you can do things with
[3566.40 --> 3571.28]  just a few javascript functions that versell is going to run for you really nicely and then there's
[3571.28 --> 3576.16]  a set of things that you need a little bit more server-side control and infrastructure to handle
[3576.16 --> 3581.28]  with and it kind of goes on and on and on until you're at one of these you know megacorps that are
[3581.28 --> 3585.44]  handling all of their own infrastructure and then you say okay it's the infra teams problem and i'm still
[3585.44 --> 3590.96]  going to worry about my little bundle but um i do think there is one tricky thing here though which is
[3590.96 --> 3597.36]  is thinking about how you move up and down those levels of complexity and i think we as developers
[3597.36 --> 3602.88]  often fall into two different failure modes one is we have a tool that we love and we try to use it
[3602.88 --> 3607.04]  for everything even though we probably don't need all of its complexity for things like this is the
[3607.52 --> 3612.00]  static websites that were you know massive gatsby applications or other things where you're like
[3612.00 --> 3617.52]  no you're putting some text files on a s3 bucket like that's all you should do and the flip side of
[3617.52 --> 3622.48]  that is holding on too long to the very simplified version and then jumping through all sorts of hoops
[3622.48 --> 3627.04]  to try to accomplish the thing that you need to do where if you were to expand your view of what is
[3627.04 --> 3632.08]  under your control maybe to jared's point like you know think about the routing piece as part of your
[3632.08 --> 3637.20]  application suddenly those problems become much easier to solve and so i think that would actually
[3637.20 --> 3641.28]  be kind of an interesting conversation i don't know we have too much time to dive into it now but of
[3641.28 --> 3646.96]  like how do you recognize when you are at the wrong layer of control and you need to either
[3646.96 --> 3652.72]  simplify the sets of things that you're doing or expand the boundaries of what you want to take
[3652.72 --> 3660.48]  control of yeah i love that we should let's earmark that for a future conversation i think that there's
[3660.48 --> 3667.28]  a lot to explore here and it's easy for us to live in our little world that we're currently in i think
[3667.28 --> 3673.44]  eric mentioned his echo chamber earlier with the whole shifting thing which now he brought so many more
[3673.44 --> 3679.20]  people and echoed it around for all of us to enjoy shifting things in various directions left right
[3679.20 --> 3686.00]  up down but it's helpful to think beyond your current scope i know there's this idea about a
[3686.00 --> 3690.40]  local maxima versus breaking out of that i can't remember the exact way you do it but like you can
[3690.40 --> 3695.92]  you can maximize your in your locality but not realize that there's an entire different way of going
[3695.92 --> 3701.44]  about what you're doing that's above and beyond anything you can maximize here in your current bubble for
[3701.44 --> 3708.24]  instance like you said cable i'm shipping a gaspy site to versell can you do that i assume you can
[3708.24 --> 3713.68]  do that and i got a problem because it takes forever and also i've got some dynamic stuff now
[3713.68 --> 3717.60]  that i need to like do some things i'm trying to use edge functions and i don't know where my serverless
[3717.60 --> 3722.32]  stuff is running correctly and i don't have visibility there and that feature is coming soon but i don't
[3722.32 --> 3727.12]  have it yet and it's like i'm making all this up obviously but then it's like wait a second there's a
[3727.12 --> 3732.32]  whole new world out there where you throw a you change the you change the file from an html to a
[3732.32 --> 3738.80]  php file and now it can do dynamic stuff and it's like oh you know like that's actually really powerful
[3738.80 --> 3743.44]  and maybe not the best solution but i think having these conversations and realizing like by the way
[3744.08 --> 3750.72]  http is a incredibly powerful and really world building protocol that we're all using all the time
[3750.72 --> 3756.64]  and as a web developer i think it's it does us well to understand it probably a little better than we
[3756.64 --> 3761.20]  currently do and i speak to myself as well because i know some stuff and i speak to people who really
[3761.20 --> 3766.00]  know http i'm like oh wow there's a lot of things i could do i had no idea about and then i don't need
[3766.00 --> 3772.96]  to offshore that to netlify for instance so i like that idea i like this conversation i feel like uh
[3772.96 --> 3779.44]  uh we've come to a really good place i'm excited any final words from our guests amy eric
[3780.56 --> 3786.64]  type script wow she's never coming back you know i was about to invite you back
[3787.60 --> 3791.60]  do you have a nick nacy type scripts audio thing you can just like put there
[3793.76 --> 3798.24]  yeah now amy uh nick's gonna have to invite you back because you've lost your invite from me
[3798.24 --> 3803.60]  eric how about you can you say anything wiser than what we just heard over there no i i really
[3803.60 --> 3809.04]  appreciate kball's framing recently that drawing that line i think is really interesting especially
[3809.04 --> 3813.20]  with the shift to serverless one of the things that's been in my mind is like when was the last
[3813.20 --> 3819.04]  time i deployed to vps when's the last time i ran my own server and what is the complexity there you
[3819.04 --> 3824.00]  know and that opens up so many doors to running other run times too like php and having it available
[3824.00 --> 3829.20]  and now it's like i may have forgotten that i may have lost that skill so it's kind of a shame to to
[3829.20 --> 3834.24]  be limited now with like the latest and greatest and lose all the possibilities that i used to take
[3834.24 --> 3841.28]  advantage of so food for thought thanks kball well said well said all right well this has been a yep
[3841.28 --> 3846.80]  nope debate if you don't know why we call them yep nope that's because you never used a yep nope.js
[3847.36 --> 3853.28]  library which was an old feature detection library from our old friend and one time jsparty
[3853.28 --> 3859.76]  panelist alex sexton so that's a shout out to alex every time we do this we say yep or nope it seems
[3859.76 --> 3867.12]  that the answer after this debate is it depends and probably yes probably yep wins more than nope but
[3867.12 --> 3877.68]  as always your mileage may vary so on behalf of our awesome guests eric clemens amy dutton and our awesome
[3877.68 --> 3896.16]  panelist nick neesey and kball was also here i'm jared this is jsparty and we will catch y'all on the next one
[3896.16 --> 3905.20]  we have 15 bonus minutes coming up after this outro for our changelog plus plus subscribers
[3905.20 --> 3912.56]  changelog plus plus it's better if you enjoyed this yep nope format let us know we'll do more like it and
[3912.56 --> 3917.44]  if you have an awesome premise you'd like us to debate leave a comment using the link in your show
[3917.44 --> 3923.60]  notes we're always on the lookout for topics that we can argue both sides on thanks again to our
[3923.60 --> 3931.44]  partners at fly the home of jsparty.fm and of course thank you to breakmaster cylinder our beat freak in
[3931.44 --> 3937.28]  residence if you haven't tried sentry yet for all your application monitoring needs use code changelog
[3937.28 --> 3944.00]  when you sign up for a team plan and save 100 bucks we love sentry maybe you will too that is all for now
[3944.00 --> 3947.52]  but come back and party with us again next week
[3947.52 --> 3960.64]  i don't think nick should have lost so many points though that's that seemed a little rough
[3960.64 --> 3965.78]  thank you well coming back from that negative three you were doomed when i assigned them on your team eric
[3965.78 --> 3972.36]  i'm sorry but it was over at that point i mean the guy just brings typescript to every single party
[3972.36 --> 3979.64]  you know this is a build step talk you thought you were safe now you have a friend there's no logic
[3979.64 --> 3982.20]  or reasoning to my side nick it's just pure
[3987.32 --> 3996.20]  it's better
