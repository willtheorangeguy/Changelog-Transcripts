[0.00 --> 14.44]  welcome back everyone this is the changelog where remember support a blog podcast and weekly email
[14.44 --> 19.30]  that covers what's fresh and what's new in open source check out the blog at the changelog.com
[19.30 --> 25.86]  our past shows at 5by5.tv slash changelog and you can subscribe to the changelog weekly it's our
[25.86 --> 31.46]  weekly email covering everything that hits our radar in open source you can subscribe at the
[31.46 --> 37.30]  changelog.com slash weekly this show is hosted by myself as well as andrew thorpe andrew say hello
[37.30 --> 46.78]  yo yo yo yo this is uh this is episode 105 man it's crazy it's crazy it's just mind-blowing mind-blowing
[46.78 --> 53.50]  we're gonna run out of numbers eventually i think i think we might we might but uh today we have a
[53.50 --> 58.94]  an awesome guest on the show john o'nolan john you run this really cool thing called ghost so john is
[58.94 --> 62.98]  the creator of ghost he's uh he's on the show to talk to us so welcome to the show my friend
[62.98 --> 70.86]  hello thank you thank you for having me yeah man so um before we kick off the show i do want to
[70.86 --> 78.04]  mention um our sponsor for this show digital ocean they're really awesome uh cloud hosting provider
[78.04 --> 83.26]  they uh they've come on to sponsor the changelog for the next i think next three shows we're pretty
[83.26 --> 89.46]  excited to have their support they are dedicated to offering the most intuitive and easy way to spin
[89.46 --> 95.58]  up cloud servers um you get a cloud server up and running in 55 seconds which is an astounding
[95.58 --> 101.54]  number it's pretty quick pricing is is uh really affordable starts at five bucks per month get half
[101.54 --> 107.90]  a gig of ram 20 gig 20 gigs of ssd drive space one cpu one terabyte of transfer and they feature a
[107.90 --> 113.18]  pretty awesome uptime sla which is 99.9 i don't think you can get any more can you injure it's like
[113.18 --> 119.26]  that's unheard of i think three three nines three nines the golden the golden egg the golden egg
[119.26 --> 124.96]  that's the the unreachable mark that people aim for nah i see i see but they've got uh data centers
[124.96 --> 131.60]  in new york san francisco as well as across the pond over in answer dam a really awesome interface and api to
[131.60 --> 136.18]  make your own version of their interface if you'd like to uh they got kvm i'm sold
[136.18 --> 142.78]  uh digital ocean uh digital ocean.com we have oh that's cool i was talking to them today no way
[142.78 --> 148.74]  about what hosting uh yeah they're gonna they're gonna set up uh an auto installer for ghost which
[148.74 --> 152.58]  is very nice of them no way so you're working on that integrating with them so they seem like very
[152.58 --> 158.56]  cool guys nice that's good so everyone should buy their stuff yeah let me tell you how then since uh
[158.56 --> 164.12]  since john's basically sold everyone on this uh we have a ten dollar promo um if you when you go to
[164.12 --> 169.18]  sign up for your services with digital ocean when you enter your credit card information on that
[169.18 --> 177.02]  page there's a promo code uh filled there we're going to enter the changelog 104 that's the changelog
[177.02 --> 183.38]  104 you'll save ten dollars um members that at the tail end of the show i'm going to mention a a special
[183.38 --> 188.94]  thing for members of the changelog as you know we are member supported so if you are a member you can go
[188.94 --> 196.00]  log in go to slash benefits the changelog and you actually get a 20 dollar promo so if you're sold
[196.00 --> 200.18]  become a member support us and get an extra 10 bucks off your digital ocean services but
[200.18 --> 207.70]  go to the go to digital ocean.com sign up today use our code enjoy that super fast uh awesome cloud
[207.70 --> 212.24]  hosting service we love you digital ocean thank you for your support but let's get done with the show
[212.24 --> 219.72]  john what's up man how are you i'm very good i'm chilling as they say chilling as they say over
[219.72 --> 225.64]  in america yeah i'm just trying to fit in guys yeah well john why don't you kind of start off by
[225.64 --> 232.16]  giving us just a uh introduction background who you are where you come from so my name is john
[232.16 --> 237.68]  and nolan we covered that part already um i'm a designer primarily um i also code um on the front
[237.68 --> 243.00]  inside of things and i guess the most relevant part of my background is that i spent two years
[243.00 --> 249.62]  working as the deputy head of ui for wordpress um as an open source contributor um as well as doing
[249.62 --> 256.94]  you know a lot of freelance client work same old same old stuff and about a year ago um i came to a
[256.94 --> 263.40]  point where my frustrations with wordpress and building blogs with wordpress so really simple blogs or not
[263.40 --> 269.96]  using the full extent of wordpress's functionality um got to a point where i decided to put some of my
[269.96 --> 276.32]  ideas down on canvas as it were in a photoshop document and i put that into a blog post uh published
[276.32 --> 282.68]  it hoping to get a couple of thousand views maybe that would be cool um but the front page of hacker news
[282.68 --> 288.72]  and twitter later um and about a quarter of a million page views in the space of a couple of weeks
[288.72 --> 294.88]  um a little thing called ghost was born and i guess that's why i'm here today talking to you
[294.88 --> 304.62]  lovely people so ghost uh yes what is it so ghost is a new blogging platform it's built entirely in
[304.62 --> 312.44]  javascript um just to be you know cool like everyone else these days um and it is aiming basically stick
[312.44 --> 317.92]  blogging back to its roots um and the implication is that uh all existing blogging platforms fall into
[317.92 --> 323.58]  one of two camps they're either closed source proprietary um hosted and locked down so that
[323.58 --> 329.40]  would be medium subtle or tumblr or they used to be open source blogging platforms that have now
[329.40 --> 335.42]  evolved into fully fledged um content management systems which would be the likes of drupal joomla
[335.42 --> 342.82]  and wordpress and ghost is trying to still be open source but be only about blogging and have a real
[342.82 --> 348.72]  focus on design and usability um to make it appealing to consumers as well as developers
[348.72 --> 355.08]  so a lot of what i read as going through the you know ghost i don't know what the best way to say it
[355.08 --> 361.74]  the uh atmosphere no what's the the ghost community i read about a lot of people comparing it to
[361.74 --> 369.06]  uh wordpress right and so wordpress obviously as you said and it's no uh it's no secret that i don't
[369.06 --> 372.92]  know if i would say you're not a fan of wordpress or you're not a fan of using wordpress for writing
[372.92 --> 379.32]  or what but when you read through it it's no secret that um ghost is directly kind of aimed at the
[379.32 --> 386.30]  taking almost taking a shot at what wordpress has become and so it appears i mean from the outside
[386.30 --> 392.48]  looking in it's ghost is a writing platform it's a it's it's just a blogging service and so it more
[392.48 --> 399.00]  closely resembles subtle medium you know tumblr those types of things so why do you what is the
[399.00 --> 405.86]  reason that you kind of target your uh you know i don't know talk more about wordpress than about
[405.86 --> 412.42]  the other platforms um i think because it's it's most comparable at least in terms of technology i
[412.42 --> 418.12]  see um subtle medium these kinds of things more social networks you know you sign up to them
[418.12 --> 423.84]  you get a profile um whatever company it is decides on the design of your site and what your url structure
[423.84 --> 429.88]  is and whether or not you're allowed to back up your data or not um whereas an open source platform
[429.88 --> 434.00]  traditionally most of the time you run on your own servers you have access to your code you can
[434.00 --> 440.02]  install your own plugins your own themes um whatever and in that sense it's far closer to wordpress or
[440.02 --> 445.92]  any open source alternatives than what it is from a user-facing point of view from a user-facing
[445.92 --> 452.48]  point of view it's definitely um much more similar to medium or tumblr but what people um i think are
[452.48 --> 457.16]  interested in especially at the early stages of it um really getting built and coming to life
[457.16 --> 464.44]  is the technological side um and in that sense it's it's much closer to its open source uh comrades um
[464.44 --> 469.22]  but i i don't think it's it's fair to say i just dislike wordpress um i think wordpress is an
[469.22 --> 474.98]  incredible platform it's it's pretty much made my my entire career up until this point um the thing with
[474.98 --> 481.08]  wordpress is it really has grown into um bigger shoes than it started out in um you know back in the
[481.08 --> 485.24]  days when wordpress was just getting started there were no real simple content management
[485.24 --> 490.70]  systems or solutions that people could use so people deliberately started using wordpress for all
[490.70 --> 496.26]  sorts of other stuff building websites with it um way beyond its original intentions um of a simple
[496.26 --> 501.58]  blogging platform purely because it was the best thing that was around um and i love wordpress for
[501.58 --> 506.52]  doing those kinds of things um our marketplace at the moment that showcases ghost themes uh is actually
[506.52 --> 511.72]  running on wordpress um and i use wordpress for for tons of other stuff our developer site our vip
[511.72 --> 517.10]  developer site which has all our nightlies and developer docs also runs on wordpress um but for
[517.10 --> 524.12]  building a publication for building a blog it's it's too much now um for me uh and as it turns out
[524.12 --> 529.78]  for a lot of other people as well see i'm kind of in the middle there because we use um we use
[529.78 --> 535.18]  wordpress to produce the change hey adam yeah let me cut you off real quick we can it's very hard to
[535.18 --> 540.88]  understand what you're saying me why your audio is gone your audio exploded oh man i think there's
[540.88 --> 549.02]  a ghost in your house yeesh sounds like there's a vacuum on your microphone he says pick up without
[549.02 --> 557.68]  me okay uh so i guess the it's better for me to say that uh not that you dislike wordpress but that you
[557.68 --> 563.80]  you would say that wordpress is i don't know difficult to use when you're just uh creating a blog and it's
[563.80 --> 568.96]  funny because when i talk to friends of mine that want me to work on their website they you know they
[568.96 --> 574.06]  have a problem they have something wrong and they want me to fix it they're almost invariably they're
[574.06 --> 579.22]  in wordpress and i commonly tell people i haven't used wordpress since it was wordpress like i i don't
[579.22 --> 586.22]  know anything about wordpress now and the last time i used it it was just a blogging platform and so
[586.22 --> 593.28]  ghost is coming out and as just a blogging platform what do you think is going to help
[593.28 --> 599.94]  prevent you from growing into something much larger than that so that's probably um the most
[599.94 --> 604.90]  one of the most common questions i get is um you know people will build plugins on top of it and they
[604.90 --> 609.54]  will use it invariably for whatever they want how are you going to stop it from um essentially following
[609.54 --> 615.08]  in the footsteps of wordpress and the answer is is reasonably straightforward um the first part of it
[615.08 --> 620.60]  is we're absolutely not going to try and prevent anyone from from building anything on top of it they
[620.60 --> 625.92]  want to um so people absolutely will try and build content management solutions on top of ghost they
[625.92 --> 630.66]  will i'm sure try and build newsletter management systems e-commerce systems they're going to try and
[630.66 --> 636.00]  do all sorts of stuff on top of ghost and i'm sure a lot of it's going to be very cool um the biggest
[636.00 --> 641.98]  difference is going to be in the actual focus so as wordpress got a lot of people building stuff on top
[641.98 --> 647.86]  of it and a lot of demand for content management style features they shifted the focus of their core
[647.86 --> 653.50]  development to accommodate those users and that demand that they were getting at the time so rather
[653.50 --> 659.66]  than going down a route of focusing on publishing focusing on extending how posts work that type of
[659.66 --> 665.28]  thing we've seen them move in the last few years to stuff like custom post types which allows you to
[665.28 --> 671.36]  basically create your own types of content and different taxonomies so different types of categories
[671.36 --> 676.30]  and tags and for example you could run a whole bookshop where each thing that you write as a post
[676.30 --> 681.16]  is actually a book and it can have properties like an author and a publication date and all those
[681.16 --> 686.98]  sorts of things um they added functionality for multi-site so you can run multiple installs of
[686.98 --> 693.82]  wordpress off of a single install um so they moved the focus of core to enabling all these different
[693.82 --> 699.08]  types of functionality to the point now where the lead developers and and the founder matt mullerway
[699.08 --> 706.58]  uh call wordpress a uh an online operating system or a an application platform um so that's really the
[706.58 --> 712.34]  route they went with with their focus and what i'm saying is i can't prevent people building stuff on top
[712.34 --> 718.02]  of ghost but the focus of the core team the focus of the core platform is always going to be on blogging
[718.02 --> 723.92]  on publishing and on all the workflows that revolve around that um and i think that's going to be the
[723.92 --> 731.72]  biggest difference um as time goes on and it evolves as a platform gotcha so it it's more about just
[731.72 --> 737.56]  keeping the focus very uh i don't know narrow is the right word but just very succinct yeah so you
[737.56 --> 744.48]  found the this niche in between i think what wordpress is right that the you took a part of what wordpress
[744.48 --> 749.80]  is and that's just building an open technology and then this other thing that's starting to really grow
[749.80 --> 754.98]  online right now which is these writing platforms for some reason blogging you know blogging is is
[754.98 --> 760.90]  not new and it and it almost seems that it started to kind of disappear with like things like twitter
[760.90 --> 765.46]  and facebook and stuff but for some reason the desire to to write again is really coming back
[765.46 --> 772.02]  full force right and so um you found this niche where you're going to have this elegant user
[772.02 --> 778.60]  interface this gorgeous you know experience for writing and keeping it open why do you think that
[778.60 --> 784.62]  you guys are kind of the only people doing that or are you or do you know of any competitors or or if
[784.62 --> 789.44]  not and if not why do you think you guys kind of stumbled upon this when no one else have has
[789.44 --> 794.08]  well i mean i think we have a lot of competitors in the form of people like subtle and medium
[794.08 --> 799.20]  um but obviously the biggest difference between us and them is that we're open source
[799.20 --> 805.90]  and from an open source point of view there's there's a few people doing uh small projects um i think
[805.90 --> 814.20]  there's a guy who's got a thing called medium js um which is the medium editor in a single javascript
[814.20 --> 820.18]  file um so you can sort of have a really nice writing experience right um and you can embed that into a
[820.18 --> 826.02]  website but there's no one else who's done a kind of full-fledged um content management system
[826.02 --> 833.66]  um but i think the the non-open source competitors prove the market i think the kickstarter campaign
[833.66 --> 840.50]  shows the the market is there as well and i think it was to some degree right place right time
[840.50 --> 848.96]  and um now luckily we've got a lot of people who are quite excited about it gotcha so you said a
[848.96 --> 855.14]  little bit earlier that that the traditional i don't know open technology is a self-hosted solution
[855.14 --> 861.64]  but um ghost kind of is gonna hit both of those right self-hosted and you guys also have your own
[861.64 --> 866.98]  hosted version is that right yes so anyone can download the source uh run it on their own server
[866.98 --> 872.54]  obviously like any um application and then we're also going to have a click and go effectively
[872.54 --> 877.18]  hosted service for people who are not developers people who don't want to set up their own stuff
[877.18 --> 883.88]  um but we are going to try and keep that as as flexible as possible so with wordpress you have
[883.88 --> 889.86]  wordpress.com which is the hosted thing and .org which is the package you download um and the main reason
[889.86 --> 896.36]  uh less people use .com i mean there's still millions of them um who blog on wordpress.com
[896.36 --> 901.18]  every day but the reason you don't get really big uh blogs running on wordpress.com is that it's it's
[901.18 --> 908.32]  fairly tightly locked down so they have their own themes um and they have no plugins um which means if
[908.32 --> 914.20]  you want to have any control of your site or extend it beyond uh wordpress's core functionality
[914.20 --> 919.12]  uh you have no option to do that unless you self-host um whereas what we're going to try and do is still
[919.12 --> 925.36]  have a degree a fairly large degree of flexibility in our hosted service so we want to be the the go-to
[925.36 --> 930.90]  host for people if they need ghost hosting effectively um they can host it on our platform and still be able
[930.90 --> 936.70]  to use all the plugins all the themes um that they want to so that's a little bit of a reverse almost of
[936.70 --> 943.60]  the the point of view is it's you guys are going to try and basically i don't know so it's odd it's a
[943.60 --> 946.60]  weird way to put it right but but it's a cool thing because what you guys are going to try and do is
[946.60 --> 951.84]  say the community is going to be able to use ghosts to do whatever they want but our goal is to build
[951.84 --> 957.62]  the hosted version so that it's better than almost what you can do on your own or at least comparable
[957.62 --> 963.30]  right so that there's it almost there's no reason for you not to although it's an open technology
[963.30 --> 966.50]  you have the option to host it yourself we're going to take the pain out of that and do it for
[966.50 --> 971.62]  you without any limitations you got it so that's cool i mean that's that's how you guys are going
[971.62 --> 976.42]  to obviously make money or is that going to be free or how's that gonna no that's definitely going
[976.42 --> 983.06]  to be uh monetization strategy um of course the the extra little twist for ghosts to make it more
[983.06 --> 987.86]  interesting or in in some people's opinion more crazy is that as well as being uh open source we're
[987.86 --> 995.56]  also non-profit um so the effectively the hosted service will be funding um all of our future
[995.56 --> 1000.74]  development into ghost so anyone who is not a developer but wants to support open source software
[1000.74 --> 1005.84]  if they choose to host their blog with us effectively they'll be doing that because all of the money
[1005.84 --> 1010.76]  um that we make from that service will only get reinvested into the company uh to hire more
[1010.76 --> 1017.38]  developers to uh pay for the the life cycle of the product effectively um and that's that's my idea
[1017.38 --> 1022.36]  of of what i'm loosely referring to at the moment as uh sustainable open source of of the people who
[1022.36 --> 1027.16]  use the software and who benefit from the software as being able to in some way contribute back into
[1027.16 --> 1033.68]  um the pool of of money that gets used to develop the software by its contributors gotcha so we'll talk
[1033.68 --> 1037.46]  a little bit about the funding you guys we haven't i don't think we've mentioned it yet but you guys were
[1037.46 --> 1041.46]  backed on kickstarter so this project came about and you wrote a blog post and there was some interest
[1041.46 --> 1050.04]  so you created a kickstarter project um yes last week we had uh his name is eluding me it was gordon
[1050.04 --> 1056.08]  williams from espruino another kickstarter project actually javascript project on kickstarter and
[1056.08 --> 1062.08]  javascript as we know yeah yeah and he it was successful right and so he basically quadrupled his
[1062.08 --> 1069.54]  a goal and and is beginning you know production on it uh you went same route i think you actually
[1069.54 --> 1076.20]  were a little bit sooner or before him but you play you wanted 25 000 pounds and you reached almost
[1076.20 --> 1084.46]  200 000 which is tremendous i mean that's crazy how much more kickstarter allowed you to to raise than
[1084.46 --> 1088.74]  you even thought you were going to need um what was that like what was the the reception and the
[1088.74 --> 1095.14]  enthusiasm behind it like for you uh crazy uh roller coaster doesn't begin to describe it it was
[1095.14 --> 1102.88]  probably the most insane month of my life um i think the thing you don't really get from as an
[1102.88 --> 1107.14]  outsider looking at kickstarter campaigns when you haven't sort of created one yourself is it all looks
[1107.14 --> 1112.70]  very cool and it all looks very easy like someone put up this page that looks kind of you know like it
[1112.70 --> 1117.38]  might have taken a few hours and there was a video and i guess that took a day or two and then money
[1117.38 --> 1122.38]  rolls in right it looks like a kind of a get rich quick scheme and then you see all these projects
[1122.38 --> 1129.30]  that you know pebble and ouya which get millions of dollars um and you just it's very easy to look
[1129.30 --> 1133.20]  at it and think wow that would be amazing to just sit there and have all that money roll in and then
[1133.20 --> 1139.12]  be made for a couple of years um when you're on the other side of of the picture it's pretty scary
[1139.12 --> 1146.68]  um i mean to put it in context after the first week my hair was falling out the skin was falling
[1146.68 --> 1153.46]  off my face um off my arms and that was from the 19 hour days i was pulling just to keep up with the
[1153.46 --> 1160.86]  level of tweets emails and questions and press requests and everything coming in um and it pretty
[1160.86 --> 1167.12]  much hasn't stopped since then i've tried to to curb the number of hours i put into a somewhat uh
[1167.12 --> 1175.46]  survivable amount um but it's unreal how much work it is it's very fun it's very rewarding but it's
[1175.46 --> 1180.58]  incredibly incredibly hard work yeah i mean when you started and this i asked this question last week
[1180.58 --> 1187.12]  i'll ask you the same thing when you started you have a 25 000 or 25 000 pound goal so you basically say
[1187.12 --> 1196.18]  i think i in order to do what needs to be done i think i need 25 000 pounds and obviously you you get
[1196.18 --> 1203.04]  eight times that amount which means that a um there's a lot more people than you expected to
[1203.04 --> 1209.94]  uh you know back this thing and b that there's a lot more money to use than you originally anticipated
[1209.94 --> 1214.40]  which means you have to figure out a way to use that money um especially for someone like you who's
[1214.40 --> 1220.18]  doing this as a not-for-profit so what i've what i've heard about and what i've actually experienced in
[1220.18 --> 1224.94]  my own life from kickstarter was you know a product that somebody puts on kickstarter they want to raise a
[1224.94 --> 1229.54]  certain dollar amount and they get 10 times that amount well what what ends up happening is there's
[1229.54 --> 1235.62]  so many people that require or desire that product now that it's hard to keep up with uh the the the
[1235.62 --> 1241.52]  demand and so what you're kind of saying is is your demand might not be a physical product right
[1241.52 --> 1245.42]  because you're you're creating one product that you're going to be able to give to everyone so you
[1245.42 --> 1251.16]  might not have the problem of manufacturing you know instances of this product but what you do still have
[1251.16 --> 1258.52]  is you you basically based your team or your future of this thing on a certain goal and you get way more
[1258.52 --> 1266.58]  than that so how do you keep everybody interested that's in that that backed this thing when when it
[1266.58 --> 1272.70]  the growth was so much greater than what you originally anticipated so it's a good question it's hard um
[1272.70 --> 1279.70]  the what i was pretty conscious of this before starting um i think it's it's completely insane i don't know
[1279.70 --> 1284.90]  how the hardware uh kickstarter projects manage it but you see a lot of kickstarter projects that puts
[1284.90 --> 1291.92]  uh unnecessary fulfillment into their rewards uh just because they think that will entice people to
[1291.92 --> 1297.06]  back so for example projects that say you know back ten dollars and you will get a signed postcard
[1297.06 --> 1302.28]  from the creators and then every reward above ten dollars also includes the ten dollar award right
[1302.28 --> 1306.86]  it's all fun and games signing a couple of hundred postcards when you get up to six thousand
[1306.86 --> 1310.46]  and you have to buy the postcards and you have to pay the postage on the whole postcards
[1310.46 --> 1315.30]  internationally you want to kill yourself yeah and you've got people doing t-shirts you've got people
[1315.30 --> 1323.34]  doing uh like back at this reward level and choose from one of five color options uh all those things
[1323.34 --> 1328.04]  i think we wouldn't even have shipped any software by now if we had any rewards like that
[1328.04 --> 1335.62]  um so i set out to make it pretty clear cut there would be no physical rewards whatsoever no postage
[1335.62 --> 1342.24]  no um delivery anything like that and i stuck to trying to focus on three main things for the rewards
[1342.24 --> 1346.64]  that i knew would scale so one was the software like you say you make that once deliver it to everyone
[1346.64 --> 1352.68]  and then to actually give some people some incentive to to back at higher levels there was um either the
[1352.68 --> 1360.42]  hosted service so various numbers of months free on that which again would cost us nothing um or not
[1360.42 --> 1366.28]  very much and would scale quite easily and lastly um the kind of i don't know what you call it vanity
[1366.28 --> 1372.62]  rewards so the the vip rewards you get early access or you get a founder emblem on your name all stuff
[1372.62 --> 1377.48]  that would be a value to people that we could add that we could effectively deliver with a few lines
[1377.48 --> 1385.26]  of code as opposed to um manufacturing overhead um but to come back to then keeping up with the
[1385.26 --> 1392.78]  demand of having such an increased rate um if we had only hit the original goal which was 25 000 pounds
[1392.78 --> 1399.18]  to put it into perspective i think it's that's roughly 32 33 000 dollars i think it's significantly more
[1399.18 --> 1405.92]  than that yeah yeah the target the target would have been to for me to work on it for probably half a year
[1405.92 --> 1414.94]  um with my uh my uh sorry development lead which is uh hannah wolf and be able to ship kind of what we
[1414.94 --> 1422.14]  have now maybe a little bit simpler and then open it up to the community and go from there um i had a
[1422.14 --> 1427.64]  sense that it would either just hit the goal or it would go way way way over the goal the only thing i was
[1427.64 --> 1432.84]  reasonably sure of is that we wouldn't end up somewhere in the middle um so i had sort of planned for
[1432.84 --> 1438.70]  what we would do if it ended up going the way it did go um and so what we've been able to do with
[1438.70 --> 1443.58]  all the extra money is invest that into all the infrastructure surrounding the project which is
[1443.58 --> 1449.62]  uh you know setting up a hosted and hosted service which will scale uh for the next number of years
[1449.62 --> 1453.34]  by taking on a couple of extra developers so we could build more features faster
[1453.34 --> 1459.70]  um by setting up a much more sophisticated uh projects at this early stage after just four months
[1459.70 --> 1464.60]  um and by being able to ensure the the future of the projects for the next couple of years because
[1464.60 --> 1469.44]  we now have money in the bank that we can keep working on it um while we start to monetize the
[1469.44 --> 1474.90]  hosted platform so we have we have some buffer in the bank that means we're safe to keep working on
[1474.90 --> 1479.52]  the project and it's not just going to fall off the radar because a couple of the other open source
[1479.52 --> 1483.40]  projects that you might have seen on kickstarter you know they have this big flurry of activity
[1483.40 --> 1489.34]  while there's money in the bank then the money runs out and they say okay we're not really
[1489.34 --> 1493.72]  working on this anymore and it's up to you guys to maintain it now um and i definitely want to
[1493.72 --> 1499.34]  avoid that and make it a product that's really gonna stick around so i want to talk a little bit
[1499.34 --> 1503.96]  about the core team but before we do that i want to actually point out that you did actually have
[1503.96 --> 1511.76]  one physical reward that was not reached on the kickstarter project and i think it's funny because
[1511.76 --> 1517.16]  it was the was the ironic backer special right so if anyone backs it it was 3 000 pounds then
[1517.16 --> 1522.32]  basically you would get a large wordpress logo tattoo and make a video of it and send it
[1522.32 --> 1526.90]  yeah so no one did it though why you think why don't you think anyone did that that'd been hilarious
[1526.90 --> 1531.10]  i don't know i thought that would have been awesome there was actually someone created an
[1531.10 --> 1538.32]  indiegogo campaign to try and fund the kickstarter reward for the kickstarter campaign which was so
[1538.32 --> 1545.18]  like crowdfunding-ception it was awesome yeah but uh it didn't it didn't succeed but yeah i figured i mean
[1545.18 --> 1549.84]  not everyone's gonna like it i figured at least maybe we could get some reward money out of the
[1549.84 --> 1554.78]  people who don't like it but yeah apparently uh there weren't enough of them so in some ways that's
[1554.78 --> 1558.98]  good gotcha so what i want to get into a little bit is how big is the core team right now
[1558.98 --> 1568.74]  um so we have three people full-time and employed which is myself hannah and a guy called matthew harrison
[1568.74 --> 1575.62]  jones who's based in the uk and then we have roughly 20 22 open source contributors who have
[1575.62 --> 1582.24]  access to the repo and a writing code for us right now um before we open it up public and a network of
[1582.24 --> 1587.88]  probably between 15 and 20 more people who are contracted by us and are working on
[1587.88 --> 1594.56]  the infrastructure effectively so ghost.org the hosted platform all the whole network of systems
[1594.56 --> 1599.10]  that are surrounding the project so that's kind of what i want to get into so you have 15 and 20
[1599.10 --> 1604.48]  contracted and then three full-time so you have somewhere between 18 and 25 18 23 people that
[1604.48 --> 1612.16]  you're paying is that right yeah okay so when you i guess that's what i kind of wanted to ask is
[1612.16 --> 1616.78]  when you when you created this project and you had 25 000 pound goal i don't think that if you would
[1616.78 --> 1622.10]  have hit just 25 000 pounds you would have been able to afford that and so absolutely was that kind of
[1622.10 --> 1626.98]  in the plans was hopefully we'll go much more than that and we'll be able to pay these these types of
[1626.98 --> 1634.10]  roles or was that just a way to kind of keep it as a non-profit oh no no that was that was pretty much
[1634.10 --> 1639.04]  in the plan from day one uh was hoping you know i mean you don't like to jinx yourself but hoping we
[1639.04 --> 1643.44]  would hit that level and that would be an option so what would it what would look different if you
[1643.44 --> 1650.24]  would have gotten to 25 000 pounds and that's it uh we would probably have a really sketchy prototype
[1650.24 --> 1657.90]  it would already be just on github uh the websites would just be marketing pages and you could
[1657.90 --> 1663.88]  download the package and that would be it gotcha um and then we we would look to try and do some
[1663.88 --> 1668.42]  sort of fake hosted service probably partnered up with one of the cloud hosting companies just as
[1668.42 --> 1676.30]  like an affiliate reseller of them um and it would it would just look a lot smaller i think right it's
[1676.30 --> 1680.18]  interesting because i don't see on the kickstarter project i don't see any stretch goals right i don't
[1680.18 --> 1685.64]  see well we hit our we hit our our goal and now we're going to offer more incentive i don't see
[1685.64 --> 1691.02]  that what i see is that you guys are going to over deliver on what the project was you're going to
[1691.02 --> 1697.06]  give more than and so people that backed it might not even necessarily you know be expecting some of
[1697.06 --> 1700.46]  the stuff that that's going to come with ghosts and i think that's a good thing i think you know it's
[1700.46 --> 1705.94]  it's the the the demand is based on the product not based on the the incentive that you're going to
[1705.94 --> 1710.42]  give people and to me that that could that could help to establish security for this product
[1710.42 --> 1718.26]  i agree um so we we did set one stretch goal which was uh 250 000 pounds effectively 10 times the
[1718.26 --> 1725.00]  original goal and what the uh ambition was for if we hit that which we didn't was going to be to
[1725.00 --> 1730.86]  create and deliver a full marketplace effectively kind of a google play style app store
[1730.86 --> 1737.62]  um by the beginning of next year um we're going to start a a publication with ghost
[1737.62 --> 1745.06]  kind of like tumblr's in-house publication did for a while um and give everyone who backed the project
[1745.06 --> 1750.92]  i think an extra year of free hosting uh we didn't hit that in the end but effectively if we had hit that
[1750.92 --> 1759.04]  the only thing we would be doing is scaling up um yeah i mean the the product itself um but we kind of
[1759.04 --> 1763.34]  ended up in the best of both worlds by getting quite close to the stretch goal but not hitting it
[1763.34 --> 1768.20]  we had a lot of extra funds but without a lot of extra responsibilities right um so that was
[1768.20 --> 1773.06]  actually very helpful it's almost like you you put a 250 000 pound stretch goal so you really want
[1773.06 --> 1780.54]  249 000 pounds right yeah but you you don't say that too much right exactly uh so on on the website
[1780.54 --> 1785.28]  you have these things called ghost launch partners it looks like that's probably the the uh large
[1785.28 --> 1791.46]  backers on kickstarter or is that what are ghost launch partners yes uh it's the so we had a
[1791.46 --> 1798.28]  five thousand pounds that's the maximum level on kickstarter um for effectively companies who want to
[1798.28 --> 1802.92]  get behind the projects and in return uh they get their their logo on the website uh for a year
[1802.92 --> 1808.66]  um on all our printed banners for events uh for the next year or however long we end up using them
[1808.66 --> 1813.28]  for which might be longer than that and they got early access to the code base um and we'll have
[1813.28 --> 1819.14]  uh their plugins or themes anything they choose to build with ghost are featured on marketplace
[1819.14 --> 1824.18]  effectively gotcha two that stick out to me this is what's interesting is envato and code school who
[1824.18 --> 1829.64]  have their own writing platforms so what do you think it is about them do you think why did they
[1829.64 --> 1836.32]  decide to jump on ghost so different reasons for the two of them uh envato are really interesting ones
[1836.32 --> 1842.80]  um really cool company uh they have these huge their primary revenue source is their marketplaces
[1842.80 --> 1848.14]  um and they have huge huge business in the wordpress themes marketplace it's one of their
[1848.14 --> 1853.60]  biggest um money generators effectively um and they've had a lot of issues over the years
[1853.60 --> 1859.82]  um particularly in relation to the gpl and what is and what isn't gpl uh you know when it comes to
[1859.82 --> 1868.56]  images or php or javascripts or uh very long um sordid history shall we say and
[1868.56 --> 1874.04]  so they're always interested in platforms which people can build products for which effectively
[1874.04 --> 1878.88]  can go into their marketplaces and ghost is much simpler from the point of view of licensing being
[1878.88 --> 1886.32]  mit um makes it much less of a uh point of potential friction for them um so for them i think it's a
[1886.32 --> 1893.24]  great platform for them to to basically set up part of their marketplace for um for code school uh
[1893.24 --> 1899.30]  it's actually a really cool one um i did right at the beginning before we started on ghost i was
[1899.30 --> 1904.98]  learning node.js through code school um and some backbone as well and i absolutely loved their their
[1904.98 --> 1909.80]  system i'd used kind of all the obvious ones like code academy and um some of the other ones
[1909.80 --> 1915.96]  and theirs was by far the one i enjoyed the most um so i sent them a message uh when we actually put
[1915.96 --> 1921.32]  the kickstarter campaign live saying hey guys this is built in node you have like the best node
[1921.32 --> 1927.20]  tutorials i've ever done um if you get behind this i'm sure we would be sending a lot of
[1927.20 --> 1932.04]  people your way to learn node.js so that they could code stuff on ghost um and a couple of the guys
[1932.04 --> 1938.70]  um who i kind of got to know inadvertently through twitter uh from code school uh replied uh positively
[1938.70 --> 1946.38]  and they were very enthusiastic about it and it just kind of worked out awesome so the blog
[1946.38 --> 1953.68]  on ghost.org is that written in ghost it sure is i have a an odd question but you have the credit
[1953.68 --> 1958.52]  where credit is due and you list all the kickstarter backers yes someone has to type those in manually
[1958.52 --> 1967.44]  oh man that would have been bad no i exported a whole bunch of csvs combined them and then uh did
[1967.44 --> 1972.22]  a find and replace to organize them and let me tell you that nearly killed my my sublime text
[1972.22 --> 1978.88]  yeah i believe it this is the time was it over 5 000 so it's yeah almost 6 000 i think that's crazy
[1978.88 --> 1984.66]  so let's kind of talk about a little bit about the actual technology um we've you mentioned that node
[1984.66 --> 1988.82]  or that uh ghost is written in javascript and i think we've mentioned that it's a node project
[1988.82 --> 1993.72]  um on the website you kind of we can talk about that a little bit but on the website you were
[1993.72 --> 2001.82]  about on the uh sorry on the kickstarter project one of the uh faqs is um where was it it was about
[2001.82 --> 2007.82]  basically like node doesn't have any real-time components and your response was well building
[2007.82 --> 2012.72]  this on node will have some challenges but we're fascinated by the challenges what did you mean by
[2012.72 --> 2022.48]  that um so node is an interesting one the the most common question from the technological standpoint
[2022.48 --> 2026.66]  that i get is is first of all why isn't why is it not php you know you came from a wordpress
[2026.66 --> 2031.68]  background um originally when i put up the idea for ghost it was discussed as a wordpress
[2031.68 --> 2037.66]  fog um and a lot of people ask why why not php and why node.js um and there's a lot of reasons
[2037.66 --> 2044.98]  behind it really but the most obvious ones are that node is fundamentally at such a low level
[2044.98 --> 2049.56]  that we are able to solve problems about five levels deep that wordpress has never had a hope
[2049.56 --> 2056.30]  of solving um and one example that i i use quite often for this is uh is actually the first bug i ever
[2056.30 --> 2061.38]  reported to wordpress um which was a problem with their permalink system and it turned out i was
[2061.38 --> 2069.20]  trying to enable a setting um in wordpress to change my my url structure and it was hitting a url an
[2069.20 --> 2075.10]  error with mod rewrite um inside the apache configuration that it didn't understand um
[2075.10 --> 2080.70]  so it couldn't give me a good error and it was very confusing and i reported this bug and that's how i
[2080.70 --> 2086.12]  eventually got involved in wordpress um and that turned out to be a problem that wordpress couldn't
[2086.12 --> 2091.36]  solve the only thing it could do was create a nicer error message because wordpress lives on top of
[2091.36 --> 2096.52]  apache it lives on top of mysql lives on top of php it lives on top of all these technologies about
[2096.52 --> 2101.20]  five levels deep which have their own sets of intricacies and problems that wordpress can never
[2101.20 --> 2108.44]  get to um because it's just on top of them whereas node.js is as we i'm sure you and all your listeners
[2108.44 --> 2113.46]  already know is at a much lower level where it effectively is the server so spinning up something
[2113.46 --> 2119.56]  like some roots that do permalinks nicely is a problem that is not even thought about um you
[2119.56 --> 2126.02]  don't ever run into it you just do it and that's possible um at the same time that's not to say
[2126.02 --> 2130.62]  node doesn't have its own problems and its own intricacies that we face and that's where it
[2130.62 --> 2134.78]  kind of gets into what i was saying about being excited about solving problems because with
[2134.78 --> 2139.28]  wordpress it's sitting on top of all that stuff which occasionally can actually be helpful as it turns
[2139.28 --> 2144.06]  out for example when you want to send an email you pretty much always know with wordpress that
[2144.06 --> 2148.74]  send mail is going to be available and if someone forgets their password um you can send them an
[2148.74 --> 2154.94]  email reminder and that's going to work with node.js it's a lot harder as we found out recently to
[2154.94 --> 2160.12]  actually figure out if there's any way on the server to send an email to actually detect it and most of
[2160.12 --> 2165.86]  the time there isn't a way um so we have a slightly more complicated setup to get going with ghost where
[2165.86 --> 2171.14]  we have to try and detect if there's a way to send email available and if not ask people to put
[2171.14 --> 2177.04]  something in a configuration file using uh an external mail service so there's there's ups and
[2177.04 --> 2183.62]  downs um i think overall we're really excited about building it in javascript because i mean most of the
[2183.62 --> 2189.78]  future of the web seems to be written in javascript the the core fundamental backbone of every html5 api
[2189.78 --> 2195.70]  is javascript so it makes sense for us to create a really dynamic responsive interactive application
[2195.70 --> 2201.60]  on both the front and back end with javascript but it does throw up its occasional challenges but
[2201.60 --> 2208.44]  that's that's roughly the the reason gotcha so you you you said the backbone and i wanted to ask the
[2208.44 --> 2215.10]  you're using the express framework and you're using backbone and handlebars and how much thought
[2215.10 --> 2221.04]  goes into these decisions that are made uh and and how much of it is just kind of the uh
[2221.04 --> 2229.28]  you know ipso facto the way it's done a little from column a little from column b um to some extent
[2229.28 --> 2235.26]  we uh for some problems we research as absolutely as as much as humanly possible to figure out what
[2235.26 --> 2240.22]  the best solution is going to be and for other problems we are looking at it from a point of view
[2240.22 --> 2243.82]  of what does our team know how to use and what can we deliver on and use most effectively
[2243.82 --> 2251.50]  um to get it done um i'm by no means a javascript expert that's what i rely very heavily on my
[2251.50 --> 2257.12]  development lead hannah wolf for um who is amazing at that sort of stuff um but i'd be lying if i said
[2257.12 --> 2262.46]  that all of us weren't learning as we go with this i think with every project um if you're not learning
[2262.46 --> 2267.74]  then you're doing something wrong and we're learning a tremendous amount about all of these technologies and
[2267.74 --> 2272.46]  and how they fit together as puzzle pieces and the best ways to do things and i'm sure we've got
[2272.46 --> 2281.22]  a lot more to learn but uh very much enjoying it gotcha so hannah is from moo.com uh how'd you find her
[2281.22 --> 2287.54]  she's awesome so how we actually got to know each other was she banned me from a forum like eight years
[2287.54 --> 2298.02]  ago um we were we were both like beginner web designers around 2006 2005 six um and i don't know i'm i'm pretty
[2298.02 --> 2302.86]  obnoxious even these days but it was much worse back then um so she ended up banning me but we
[2302.86 --> 2307.30]  stayed in touch on twitter and there were no hard feelings uh and we've kept in touch over the years
[2307.30 --> 2313.90]  and just stayed really good friends um and she's a phenomenal developer uh she walks circles run
[2313.90 --> 2319.38]  circles around pretty much every other developer i've ever worked with and uh picks up new programming
[2319.38 --> 2325.08]  language in the space of like a week and build stuff with them um and she's incredible she's probably
[2325.08 --> 2330.26]  the only person who puts in more hours uh than i do on ghost and is still somehow alive
[2330.26 --> 2337.74]  yeah i think that i've actually i don't know if i've actually spoken with her but i've definitely
[2337.74 --> 2344.20]  uh come across her in different um conversations and seen her so i definitely think she's one of those
[2344.20 --> 2348.26]  yeah one of those people out there that you'll if you don't know who she is you will at some point
[2348.26 --> 2354.62]  um are all the are all the developers that are working on node that both contracted in uh just
[2354.62 --> 2361.52]  the the private open source community i guess i just coined that term private open source uh are
[2361.52 --> 2365.52]  they all node developers or any of them kind of have to learn node just because they were excited to
[2365.52 --> 2372.64]  get to work on ghost uh a mix definitely a mix and probably probably a slight majority in the latter
[2372.64 --> 2378.14]  category so people were really excited to learn ghost um who ended up learning more node or more
[2378.14 --> 2384.58]  javascript to do so um we had one guy who actually thought that ghost was a wordpress fork or written
[2384.58 --> 2390.16]  in php and then he he turned up in irc and he was like so this is not what i was expecting
[2390.16 --> 2396.78]  and uh he actually his name's gabor javorski actually turned out to be uh one of the most active
[2396.78 --> 2401.92]  contributors we've had since the start and and worked his ass off to uh to pick up node and to pick up
[2401.92 --> 2408.18]  javascript and to uh to do a whole ton of stuff it's been really really good awesome so the code
[2408.18 --> 2413.04]  has client and server what's the uh what's the breakdown of those two can you give me just kind
[2413.04 --> 2419.84]  of give me a high level uh overview of what the where the code breaks down at i can try i mean you
[2419.84 --> 2426.82]  probably want to have hannah back on on the podcast for this um we have obviously node on the server side
[2426.82 --> 2431.38]  and what we started off with was doing everything on the server side so server side views
[2431.38 --> 2438.36]  and um loading everything through express um then we had a guy called tim greaser i don't know if
[2438.36 --> 2444.14]  you've heard of him he's one of the maintainers of backbone yeah um start working on ghost with us
[2444.14 --> 2451.26]  and he was he was pretty much sold us on on the idea of transitioning our front ends or rather our
[2451.26 --> 2457.24]  client side to using backbone um and where we are at the moment is a weird sort of pivoting point
[2457.24 --> 2463.42]  which is that ghost is kind of half one and half the other so we have half of uh stuff happening on
[2463.42 --> 2466.84]  the client side and half on the server side and at the moment we're trying to figure out which way
[2466.84 --> 2471.22]  we're going to go with that because we're stuck between a rock and a backbone i don't know what
[2471.22 --> 2477.48]  saying a spine and a backbone don't say that because that's uh that's those are competitors
[2477.48 --> 2483.52]  okay we won't say that that's not funny at all yeah edit that out yeah let's cut that just kidding
[2483.52 --> 2488.82]  um and so we're trying to figure out what what the best way to go uh on that one's going to be
[2488.82 --> 2496.46]  and to some extent that depends on the contributors we get um obviously we are influenced by having
[2496.46 --> 2501.90]  someone who maintains backbone is extremely talented and working with backbone um and being able to solve
[2501.90 --> 2508.16]  some of those problems um and i think it will be it will be pretty natural for the project to evolve
[2508.16 --> 2513.40]  as more open source contributors come on board come on board later uh and have different skill sets
[2513.40 --> 2519.32]  but for the real uh technical nitty-gritty why are you doing this this way and this the other way
[2519.32 --> 2526.30]  i'm afraid you're definitely going to have to bring hannah back on here gotcha cool so ghost.org the blog
[2526.30 --> 2531.56]  is written in ghost uh anybody else that is using it in production at any point right now
[2531.56 --> 2537.92]  yeah i think we've got so we launched to all 6 000 kickstarter backers uh last friday
[2537.92 --> 2544.08]  uh which was kind of crazy uh we've had over a quarter of a million page views in the last five
[2544.08 --> 2551.36]  days um and a lot of people getting their first deployments of ghost up and running which for some
[2551.36 --> 2555.02]  people has been incredibly easy and for some people has been very frustrating uh you know the classic
[2555.02 --> 2560.46]  new software syndrome um but i think they're probably a couple of hundred blogs running in the wild
[2560.46 --> 2567.46]  uh right now on ghost which is cool yeah it's awesome so do you would you say that right now
[2567.46 --> 2572.06]  it is production ready or would you do you kind of say with a disclaimer like hey you can use it in
[2572.06 --> 2577.98]  production but there's a there's a date where we'll say it's actually ready uh i don't know i mean
[2577.98 --> 2583.56]  yeah it's production ready you can use it it works it's unlikely to explode we've we've patched all the
[2583.56 --> 2589.40]  major issues we can find and have found and haven't had any show-stopping bug reports as yet
[2589.40 --> 2596.30]  so it's as ready as ready can be when you call your version number 0.3 right you're talking to the
[2596.30 --> 2600.58]  the guy who's trying to look into the future for the next three years and see where it's going so
[2600.58 --> 2605.68]  i look at it and i'm not remotely satisfied the only thing i see when i look at it is all the stuff
[2605.68 --> 2611.04]  that's missing um so if you ask me if it's ready from for my personal opinion no absolutely not don't
[2611.04 --> 2616.60]  show it to anybody but right if we actually look at it realistically um is it ready can it work can
[2616.60 --> 2621.96]  it function is it a blogging platform yeah it is yeah it's funny it's actually the question i get
[2621.96 --> 2626.14]  asked all the time when i work on projects like you know especially side projects for friends they say
[2626.14 --> 2630.20]  is it done and i'm like well it's never done you know exactly i don't know how to really tell you
[2630.20 --> 2637.18]  it's not no it's not done but it's ready you know so uh cool well the uh the timeline kind of says
[2637.18 --> 2642.06]  that this month is when it was supposed to be released on github so you have six days left so
[2642.06 --> 2648.56]  when's it going on github it is going to be as this is going to be like a world exclusive are you
[2648.56 --> 2652.84]  ready for this i'm here i'm ready we we haven't we haven't announced the official date until now
[2652.84 --> 2659.90]  we are aiming for october 4th so we actually said mid-october but we're going to go for early october
[2659.90 --> 2667.20]  there you go you heard it here first people nice after that so after the github release uh that's
[2667.20 --> 2672.60]  just the code will be available for the whole world to hack on uh following that comes the hosted
[2672.60 --> 2677.46]  platform release to the kickstarter backers and then the hosted platform release for the general public
[2677.46 --> 2683.48]  exactly um what are you looking at maybe like a couple months between those pretty much we're
[2683.48 --> 2691.88]  rolling out a beta program for um i never know like england u.s beta or better like it varies so
[2691.88 --> 2697.68]  much but you know what i mean um one of those programs for backers starting this week um and we're
[2697.68 --> 2703.14]  just going to start getting a few people in um see how it goes see how it scales and add people over
[2703.14 --> 2707.92]  time the more the better it goes the more people will add and the faster the rate at which we will add
[2707.92 --> 2713.46]  them um i think we're aiming for roughly optimistically the end of the year for general public to be
[2713.46 --> 2719.88]  able to get on the hosted platform and perhaps more realistically uh the start of next year um but
[2719.88 --> 2725.44]  it really depends how the how some of the early testing goes um hosting node is is a whole other
[2725.44 --> 2731.68]  ball game that we're learning a whole bunch about right now and hosting multiple instances of node is
[2731.68 --> 2737.42]  uh an even bigger one that that's uh very interesting yeah there's a reason why you had to
[2737.42 --> 2741.54]  in my opinion you have to contract that out and pay for that whereas a lot of the actual
[2741.54 --> 2746.78]  software development can just be open source people contributing um it's difficult it's not
[2746.78 --> 2751.86]  the easiest thing in the world right now but you heard this you heard the uh episode a few weeks
[2751.86 --> 2755.92]  back we had isaac schluder on the the maintainer of node and and that's one of the things that they
[2755.92 --> 2760.64]  definitely want to um improve is just the documentation around all that and being able to
[2760.64 --> 2766.20]  make that easier for people so there's definitely some some uh learning and some experimentation that has
[2766.20 --> 2773.52]  to go on to to do that like i told you when i when when i started looking through the code it's almost
[2773.52 --> 2778.54]  impossible to look at it and run a little instance of it and not think to yourself i want to get
[2778.54 --> 2783.64]  involved with this and i think that's a good thing i think that i see a lot of projects i see a lot of
[2783.64 --> 2788.02]  open source projects and i don't know what it is about them but i think well this is a really cool
[2788.02 --> 2795.04]  project but i don't have the time or the effort i don't have the energy required to really get into
[2795.04 --> 2801.10]  this and yeah i don't know if it's the simplicity of ghost itself if it's the community that you can
[2801.10 --> 2804.28]  just kind of see is going to come up around it i don't know what it is but there's something about
[2804.28 --> 2809.02]  it that you say like i even if it's just a little bit i would love to get involved and help with this
[2809.02 --> 2815.62]  um i think that's something that happens organically and that everybody would would hope to to kind of
[2815.62 --> 2820.88]  acquire and you guys have i think that's a good thing so so congrats on that man and this is an
[2820.88 --> 2826.62]  awesome project thank you um maybe we'll have uh after the uh after the public launch maybe we'll
[2826.62 --> 2830.36]  have you back on with hannah to talk about some of the technical details and the struggles that you
[2830.36 --> 2834.30]  guys went through to to get this thing live because i'm feeling this is going to be pretty big so
[2834.30 --> 2840.24]  um definitely yeah that's what you mean the struggles or yeah yeah yeah the launch and the
[2840.24 --> 2846.12]  struggles and the epic fail that is bound to happen just kidding hey yeah except not really
[2846.12 --> 2852.74]  yeah exactly so i think we could talk about this for hours but we do have to wrap it up so if you're
[2852.74 --> 2858.08]  new to the show uh we kind of ask the same questions at the end of every episode um so we'll go ahead and
[2858.08 --> 2864.70]  start with those the first one is for a call to arms uh obviously the project is not public to the
[2864.70 --> 2871.12]  world yet but in october it will be um do you have something that you'd like to see the community
[2871.12 --> 2876.70]  kind of rally around first when this starts to spring up definitely i mean what we have right
[2876.70 --> 2882.74]  now on ghost.org is a big sign up button where you can drop in your name and email address and
[2882.74 --> 2888.36]  you'll get an email the second it is open to the world and you can have at it effectively um so if
[2888.36 --> 2892.40]  anyone who's interested who thinks it sounds like an interesting idea or it sounds like a terrible idea
[2892.40 --> 2895.74]  and you want to rip it to pieces or it just sounds like an idea you might want to hear more about
[2895.74 --> 2902.52]  uh drop your details into that box and we will let you know when it's around um there's a ton of
[2902.52 --> 2907.02]  information already on the the live site which is uh publicly available so you can read up a little
[2907.02 --> 2912.24]  bit more about it uh have a look at the kickstarter campaign the video um if you're interested but yeah
[2912.24 --> 2918.34]  definitely subscribe to the uh the newsletter and we will let you know when it's there gotcha if you
[2918.34 --> 2926.44]  weren't doing this so uh if you weren't doing this specifically yeah ghost um what would you rather
[2926.44 --> 2934.56]  be doing so two years ago i was doing web design uh just freelance for clients the normal sort of
[2934.56 --> 2940.04]  thing and i got pretty bored of that i was living in the uk um and what i decided to do because it
[2940.04 --> 2946.34]  seemed like a great idea at the time was sell all my worldly possessions um only keep sufficient
[2946.34 --> 2952.02]  things that would fit in a single backpack so basically a laptop uh an iphone uh a couple of
[2952.02 --> 2959.14]  like five t-shirts um and just took off and started traveling uh and i've been i'm still doing it
[2959.14 --> 2965.46]  actually i've been going for two years and what i like to do when i travel is pick a spot which has
[2965.46 --> 2971.90]  wind and has a beach and i love to go kite surfing and uh if i wasn't working on ghost i think i'd just be
[2971.90 --> 2977.88]  doing a whole lot more kite surfing whereas at the moment i'm uh semi based in austria hunkered down
[2977.88 --> 2984.94]  the little office and uh coding away yeah kind of a little odd side question do are you from austria or
[2984.94 --> 2991.44]  did you just find yourself there so i happened to be in egypt last year um kiteboarding not
[2991.44 --> 2997.18]  coincidentally and the manager of the uh the kite school where we're from i was kiteboarding so you
[2997.18 --> 3001.24]  but these kite schools you can kind of store your stuff and hang out with other people who are there
[3001.24 --> 3006.74]  and the manager of that kite school happened to be a very nice austrian girl um unbelievably attractive
[3006.74 --> 3013.02]  who i got to know over the course of a month and i liked her so much that i inadvertently ended up
[3013.02 --> 3016.84]  following her back to austria uh because she was trying to get away from me but that seemed like
[3016.84 --> 3023.00]  a terrible idea so i followed her um it's not stalking she said it was fine um and i've kind of
[3023.00 --> 3028.24]  been here ever since uh in and out i'm obviously traveling to and from the uk quite a lot for for
[3028.24 --> 3035.46]  business but uh yeah i'm spending quite a lot of time here cool so for somebody that has been a
[3035.46 --> 3041.34]  world traveler uh who's a programmer hero or somebody that's been impactful in your life
[3041.34 --> 3049.02]  um i would actually have to say hannah probably uh hannah's probably been the most influential uh
[3049.02 --> 3056.82]  developer programming hero in my life since the day she banned me uh back on that forum uh from back in
[3056.82 --> 3060.26]  the days when i was first learning php she was the one teaching me when i first started learning
[3060.26 --> 3064.34]  javascript she was the one teaching me uh and throughout the years whenever i've had a side
[3064.34 --> 3071.30]  project um to work on uh she's been the one who's been doing the behind the scenes hardcore back-end
[3071.30 --> 3077.00]  development work and she's incredible so yeah she's she's probably my biggest inspirational person
[3077.00 --> 3082.40]  uh from a programming development point of view uh and you should totally have her on the show and ask
[3082.40 --> 3089.82]  okay awesome i will definitely get her back on the show hopefully you guys can can hear me now i've
[3089.82 --> 3094.30]  kind of been quiet during the show because apparently i had some audio issues on my side so
[3094.30 --> 3101.34]  apologies about that but uh yeah it's definitely definitely fun to have you on the show i think the
[3101.34 --> 3106.48]  just the the project itself has a lot of a lot of great things about it you know you mentioned
[3106.48 --> 3111.56]  being a labor of love not for profit and then also the non-profit component to it as well and
[3111.56 --> 3117.46]  you know the the overfunding and being able to build the team you have is certainly you know maybe a
[3117.46 --> 3122.46]  more of a blessing than has been a curse which i know andrew you're kind of a fan of that question of
[3122.46 --> 3128.82]  overfunding kickstarters and what that means to to the actual people executing so but uh yeah i just
[3128.82 --> 3132.68]  want to thank you again for coming on the show john for uh you know building what you're you're
[3132.68 --> 3137.24]  building and the love you have for open open source and software development and you know
[3137.24 --> 3141.36]  i know you're losing skin and losing hair but taking the time to come on the show and
[3141.36 --> 3148.94]  tell your story is is certainly uh certainly much appreciated also um and since we both have kind of an
[3148.94 --> 3153.10]  affinity for digital ocean i want to give them another plug because they do help us make this show
[3153.10 --> 3159.30]  possible um one of the cool things that they asked me to mention this week was was something i thought
[3159.30 --> 3165.00]  was kind of unique the way they're calling for uh technical writers i don't know if um i know
[3165.00 --> 3168.92]  documentation is a big thing but they have this thing where you can go on there and create
[3168.92 --> 3175.94]  tutorials about how to use digital ocean better so you know optimization you name it um but you can
[3175.94 --> 3179.52]  write a tutorial they'll give you 50 bucks for writing the tutorial there'll be a link in the show
[3179.52 --> 3184.54]  notes uh on how to check that out but it's a pretty unique way they're uh empowering and engaging
[3184.54 --> 3189.72]  the community to kind of pick up this section of their website and and you know give credit to the
[3189.72 --> 3194.18]  authors and those who are helping create that content to to make using digital ocean services
[3194.18 --> 3200.04]  a lot better so there's no limit to how many you can write out there so if you want to make mad money
[3200.04 --> 3205.36]  you can it's kind of neat though so everyone should write a tutorial for how to get ghost running on
[3205.36 --> 3210.88]  digital there you go there you go there you go but uh yeah other than that i think the other thing i
[3210.88 --> 3216.22]  want to mention which i think is is uh we're proud to begin to start saying this uh for those who are
[3216.22 --> 3222.90]  members of the changelog um as we have partners and sponsors of the show we're working with them to
[3222.90 --> 3229.52]  get exclusive offers that are for members only so in this case and a couple other cases we're just
[3229.52 --> 3234.44]  propping this up now but you can go to the changelog.com slash benefits and if you're a member you can sign
[3234.44 --> 3239.08]  in if you're not a member you can see what's there but not use it but um so these are members only
[3239.08 --> 3244.84]  members only benefits for those who uh who support us but um digital ocean's got their 20 dollar
[3244.84 --> 3248.06]  promo there which is kind of neat so if you go there and sign in you actually get 20 bucks off
[3248.06 --> 3253.74]  versus 10 bucks off um and and that's really it but uh and then we also have the changelog weekly so
[3253.74 --> 3259.84]  if you if you want to keep up with andrew's brain my brain jared's brain and others on what's fresh
[3259.84 --> 3264.40]  and new and open source we're every saturday we're we're shooting out an email to everyone on that so
[3264.40 --> 3269.08]  it's uh it's pretty neat i wish i could have participated a bit more in this conversation
[3269.08 --> 3273.12]  it's kind of fun we'll have to have you guys back on the show for sure whenever you know uh
[3273.12 --> 3277.44]  officially launch and do some more cool stuff because i'm sure you'll bring some challenges
[3277.44 --> 3283.42]  back to the table for us but uh um yeah john thanks again for joining us on the show sorry for the
[3283.42 --> 3288.20]  extended kind of post show announcements and things like that just want to make sure that uh y'all know
[3288.20 --> 3292.02]  what we're doing because we're trying to kick butt and take names one day at a time right andrew
[3292.02 --> 3298.98]  yeah and uh you've got some good news andrew on uh on the guest for next week who's what's what's
[3298.98 --> 3305.46]  when there oh yeah we're hoping it's not set in stone yet so uh no angry emails please if it doesn't
[3305.46 --> 3309.70]  happen but hopefully we'll have someone from balanced on to talk about the balance dashboard um
[3309.70 --> 3315.46]  and among other things if you listened to our get it show with chad whitaker a while back he
[3315.46 --> 3321.12]  wouldn't stop raving about the balance dashboard and uh and and just the company itself so ever
[3321.12 --> 3324.80]  since then we kind of wanted to to try and get them on the show and it's starting to line up now so
[3324.80 --> 3331.02]  hopefully next week we will have balanced on the show um but if not we'll have somebody else that's
[3331.02 --> 3336.02]  awesome too you mentioned angry emails uh if you're listening you happen to have an angry email for us
[3336.02 --> 3341.24]  send it to andrew at the changelog.com just just that's where the tweet goes at we actually have
[3341.24 --> 3347.00]  an automatic forward for those we don't get any though if it uh it's a lexic carcer that looks
[3347.00 --> 3352.72]  for angry words and sends it that's right yeah that's it but uh yes great show andrew thank you
[3352.72 --> 3359.50]  for teeing this up john awesome work and uh thanks again to you the listener for tuning in we got
[3359.50 --> 3365.30]  something fun lined up for next week and the week after but until then let's say goodbye see y'all later
[3365.30 --> 3378.44]  you
[3394.44 --> 3394.78]  you
