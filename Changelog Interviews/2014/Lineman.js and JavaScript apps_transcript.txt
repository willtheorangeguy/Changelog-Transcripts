[0.00 --> 14.78]  welcome back everyone this is the changelog and i'm your host adam stekowiak this is episode
[14.78 --> 21.62]  number 128 jared and i talked to justin saros about his work on lyman js building javascript
[21.62 --> 27.64]  apps and much more today's show is sponsored by code ship pager duty and harry's we'll tell you
[27.64 --> 33.38]  a bit more about pager duty and harry's later in the show but our friends at code ship they're rock
[33.38 --> 38.72]  solid hosted continuous deployment service that just works you can easily get set up with continuous
[38.72 --> 43.92]  integration for your app in just a few steps and automatically deploy when all your tests pass
[43.92 --> 49.62]  code ship has great support for lots of languages test frameworks as well as notification services
[49.62 --> 55.06]  they easily integrate with github or bitbucket and can deploy to cloud services like roku
[55.06 --> 62.56]  aws nojitsu google app engine and even your own servers setup is easy takes just three minutes
[62.56 --> 68.68]  get started today with their free plan and make sure you use our code the changelog podcast again
[68.68 --> 75.10]  that's the changelog podcast when you use that you're gonna get a 20 discount for three months
[75.10 --> 82.60]  on any plan you choose head to coach ship.io and tell them the changelog sent you and now on to the show
[82.60 --> 89.74]  welcome back everyone we got a fun show lineup today today is friday august 1st we're actually
[89.74 --> 94.96]  broadcasting this show in particular live on five by five we don't always broadcast live but today is
[94.96 --> 99.96]  it's just one of those days we got to broadcast live so um i'm adam stikowiak i'm joined by
[99.96 --> 107.72]  jared santo our managing editor so jared say hello hello hello and we also have our our guest today on
[107.72 --> 113.14]  the show justin serrells justin how are you i'm doing fantastically well thank you fantastically
[113.14 --> 118.92]  well what makes you fantastically well um i am just really excited to have gotten over the hump on
[118.92 --> 124.32]  a dozen really annoying things that were on my plate this week after a two-week vacation
[124.32 --> 129.14]  wow yeah i saw on twitter you said you made it to friday and you were celebrating
[129.14 --> 135.34]  yep i celebrate every friday yes fridays are good days that we we had our sprints on friday we
[135.34 --> 141.06]  started going to one week sprints so fridays are good days is that working better were you doing
[141.06 --> 147.84]  two weeks previously we were yeah we i think the the shortness and the just a fast pace of of one
[147.84 --> 153.58]  week and it helps us bite-size things better gives us quicker iterations it's really helped us out a lot
[153.58 --> 158.30]  um helps our planning process i don't know just it seems like we just get through that quicker and we
[158.30 --> 162.92]  give ourselves breaks you know once a month we'll give ourselves like a a week to kind of catch up
[162.92 --> 168.40]  and you know three weeks on one week off kind of thing so that's cool man it's been cool yeah a
[168.40 --> 176.38]  little sidetrack there dev talk well justin we have you on the show uh we were uh to talk about linemen
[176.38 --> 183.20]  js amongst other things you've kind of been uh maybe a prolific would be the word uh open source
[183.20 --> 189.76]  contributor um i first found you i think uh because of some of your work with uh jasmine and
[189.76 --> 193.72]  some of the the testing tools that you've you've put out there so i've been using those for a long
[193.72 --> 199.82]  time but linemen seems to be um a bigger project that you're you're behind you're uh building and
[199.82 --> 206.12]  appreciate having you on i thank you i kind of want to kick off the conversation with quoting you to
[206.12 --> 213.46]  yourself um no that's always a good way so you can defend yourself uh no i have i cannot warrant
[213.46 --> 220.28]  anything that past me said past me was not a smart guy but we have it on tape so you have to stand by
[220.28 --> 227.60]  it um you said and this was recently i think you've even given talks on this uh as as recently as was it
[227.60 --> 233.02]  rails golf 2014 where the title of the talk is the quote that i'll say is that the rails of javascript
[233.02 --> 239.24]  won't be a framework um obviously we don't have time to go into your 30 minute discussion on that
[239.24 --> 244.72]  i know you have tons of details um around that sentence but maybe just kind of unpack it for us
[244.72 --> 249.28]  tell us what that means and why you say that and then how it kind of led into linemen if it did yeah
[249.28 --> 256.02]  so the the talk is broken up into two parts uh the first half is a discussion about uh application
[256.02 --> 260.50]  development as it is especially in this era where people are trying to build lots of uh you know
[260.50 --> 264.68]  whatever you want to call them fat client javascript applications meant to run in web
[264.68 --> 270.34]  browsers and then phone home to like you know a lightweight api on the back end um so just a
[270.34 --> 273.94]  discussion of like you know what's what's painful about that if you're using something like ruby on
[273.94 --> 280.50]  rails you know the monolithic aspect the fact that the sort of community has been uh gradually moving
[280.50 --> 286.08]  to node.js and ruby gems aren't you know uh quite quite quite so populated then the second half of the
[286.08 --> 292.60]  talk is like just like a basically like a a demo of how we've built lineman js to alleviate all of
[292.60 --> 298.60]  those problems with monolithic rails application development um but the the pivot in the middle
[298.60 --> 305.84]  i guess is maybe what the what the title is referring to which is right rails is um uh
[305.84 --> 311.60]  really fantastic for a couple reasons and i think that over the course of 10 years what we've learned is
[311.60 --> 316.80]  that uh some of the things that we initially loved about rails turn out to not be fantastic for like
[316.80 --> 323.62]  long-term long-lived projects um you know i break up rails uh responsibilities into sort of three
[323.62 --> 331.00]  categories there's the uh the build aspect right like all the rake tasks all of the confusingly uh
[331.00 --> 337.60]  task-like things that you have to type rails for instead of rake for um then there's the um
[337.60 --> 343.62]  uh uh actual application framework that's the the types that you're extending and the active support
[343.62 --> 347.78]  apis that you can just kind of reach for wherever you are in your app and so all the coupling between
[347.78 --> 352.52]  your custom application code with the framework code and all the lift that that gives you and then in the
[352.52 --> 359.14]  middle is just like uh uh sensible defaults that you don't have to specify and then conventions that we
[359.14 --> 366.04]  all just sort of follow socially like you learn about from a buddy or from a guide um and and as a
[366.04 --> 371.00]  result we don't have to repeat ourself from project to project and we don't succumb to uh what i might
[371.00 --> 375.82]  call like accidental creativity right which you see in a lot of other communities where it's like i've
[375.82 --> 381.40]  got this 500 line long grunt file over here i'll copy and paste it and i'll diverge it you know uh
[381.40 --> 388.14]  inadvertently um so when i look back on my experience with rails the the real the hardest thing to learn
[388.14 --> 394.52]  but the most valuable part was was sensible defaults and convention-driven design um the the application
[394.52 --> 399.92]  framework stuff has a lot of problems uh and the build stuff was really awesome in 2005 and it just
[399.92 --> 406.74]  has not progressed to to handle the sort of static assets we're building for the web very well um and
[406.74 --> 411.48]  so what i want to do is just like cargo call the really great stuff in the middle and then apply that
[411.48 --> 417.18]  to uh front-end web development um and what i'm finding is like in the node community that's like
[417.18 --> 422.42]  that's that's that's news to them right like they're they're very kind of unix velocity you want lots of
[422.42 --> 428.72]  different like an eclectic blend of tiny little modules to work with right as opposed to you know
[428.72 --> 433.04]  well here's just like a default project and then you can just specify how your project diverges from
[433.04 --> 439.14]  those defaults uh so culturally it's a it's a it's a you know i feel like it's a point of friction right
[439.14 --> 443.26]  like you got ruby s on one side who understand this but they've they're very much tied up in the
[443.26 --> 447.30]  ruby ecosystem and they don't want to leave it and then you have like because lineman's written in
[447.30 --> 450.76]  node.js you have node.js on the other hand where it's like all these people just like don't
[450.76 --> 455.28]  understand the cultural benefit of that but they do have the technical tasks and tools to to get
[455.28 --> 462.12]  awesome stuff done quickly so lineman comes into kind of like you said cargo cult what you thought
[462.12 --> 468.28]  were the good ideas and rails bring them over to the front end um via the command line and give that
[468.28 --> 474.12]  structure that we so desperately need that we're saying that's that's my hope and you know in
[474.12 --> 479.36]  practice at uh our agency uh test double where we're like you know a consultancy who builds a lot
[479.36 --> 485.18]  of apps uh what we we've been using lineman for for a couple of years now on most of our projects
[485.18 --> 489.80]  and my favorite thing about it is very similar to my favorite things about rails like i can hop into
[489.80 --> 495.14]  any one of our projects and i instantly know you know how to run stuff how to build stuff how to get
[495.14 --> 499.82]  the test running uh i know that it's already set up for travis ci out of the box and i can just push it
[499.82 --> 505.60]  um i i really love that uh if i look at somebody's application config i can just literally see like
[505.60 --> 510.36]  them declaring these are the ways that i'm not normal so i can understand what's unusual about
[510.36 --> 514.60]  their build and where their backends are and all their proxies and their server stubbing and stuff
[514.60 --> 520.78]  is all like you know really readily apparent um in fact if you want to uh kind of broaden the
[520.78 --> 525.48]  discussion just a little bit behind my tool i i got the chance to finally meet tom dale and
[525.48 --> 531.62]  yahuda katson person this year and as i've talked to them about their trials and tribulations and selling
[531.62 --> 539.70]  ember js outside of the rails community uh i feel like they're doing an analogous uh uh uh crusade
[539.70 --> 544.06]  from from the rails community's understanding of what makes a good application framework
[544.06 --> 549.98]  to you know no js land or or just to the web more broadly where people are kind of you know
[549.98 --> 555.70]  anti-frameworks because there's so much framework fatigue on the front end yeah and uh i think that
[555.70 --> 559.40]  they're trying to accomplish a lot of the same things especially when it comes to sensible defaults
[559.40 --> 563.62]  and and common conventions whereas my focus has been more on build tools as opposed to application
[563.62 --> 570.34]  framework design yeah so lineman itself not a framework it's a it's a tool and it works with
[570.34 --> 577.16]  the front end frameworks that you would want to use whether it be ember angular knockout perhaps all of
[577.16 --> 581.94]  the the popular javascript frameworks of the day um so it's not actually trying to solve the
[581.94 --> 587.84]  application uh framework problem or structure problem it's actually trying to solve the build tools
[587.84 --> 594.38]  problem it's a single responsibility principle thing yeah exactly so i mean if uh when you when
[594.38 --> 599.52]  you say lineman new project it's going to assume you've got a totally vanilla javascript and css app
[599.52 --> 604.56]  and and you just want to build it but as soon as you say like well i want to use ember then all you
[604.56 --> 611.50]  have to do is say npm tech tech save dev uh lineman ember and hit enter and it'll install you know
[611.50 --> 616.32]  a lineman ember plugin that will kind of behind the scenes totally dynamically without generating any
[616.32 --> 622.56]  cruft or crap in your project just modify the configuration and the tasks and the order that
[622.56 --> 627.26]  they run in so that now you're building an ember project um and and it's doing everything you know
[627.26 --> 631.58]  handle the templates appropriately and so forth uh same thing with lineman rails if you want to like
[631.58 --> 636.12]  you know proxy back to a rails application our goal has been all along to like avoid code generation
[636.12 --> 642.54]  but make it like dead simple to integrate with and build plugins for whatever whatever you want on the
[642.54 --> 646.26]  top of the stack whatever whatever application framework you want we want to be totally agnostic
[646.26 --> 651.24]  to that cool so if you don't mind i'd like to step back for a second we'll get back to lineman and the
[651.24 --> 656.22]  features and and the details there i kind of like to talk to you a little bit uh from a consultant
[656.22 --> 662.18]  perspective i also run a development firm and at test double you know you're making the decisions on
[662.18 --> 667.42]  behalf of your clients i assume lots of times which technologies to use uh which style of application
[667.42 --> 672.62]  they actually need right so we've seen this massive move towards rich javascript front ends especially
[672.62 --> 677.68]  in the you know the edge of the development community um there's lots of problems that can
[677.68 --> 683.88]  still be solved with traditional you know page based or rails you know application structure um
[683.88 --> 688.16]  how do you decide when when your clients come to you is it just based on the needs of the app
[688.16 --> 693.86]  and how often are a follow-up question how often are you doing the rich javascript clients and how
[693.86 --> 699.70]  often are you still doing traditional apps that's a great question i think that um there's really a
[699.70 --> 704.34]  third category too when you try to break down percentages of how we work uh there's a third
[704.34 --> 710.26]  category too which is like client already has a system and they need they need help and uh we're
[710.26 --> 715.28]  you know i think very pragmatic because what we want to be doing is uh build trust with the client by
[715.28 --> 721.80]  meeting them where they are um uh and to choose our battles to choose to like you know take a stand only
[721.80 --> 726.04]  where making a change from their perspective is going to like you know they're going to appreciably
[726.04 --> 730.72]  benefit somehow so sometimes like we're we're working in really eclectic and weird you know
[730.72 --> 736.88]  environments and we're totally cool with that because uh if it's solving the problem uh as well
[736.88 --> 740.28]  and as efficiently as possible and it's in a way that's copacetic with the client wants that's great
[740.28 --> 746.26]  but now to your question of like greenfield apps that we're just building most important thing to me
[746.26 --> 752.90]  is to understand uh what are they trying to get out of the out of the application is is user experience
[752.90 --> 757.78]  really important like if they want to have a really fantastic tight crisp enjoyable user experience
[757.78 --> 761.20]  because somebody's going to be in this application all day long maybe working out of it or maybe
[761.20 --> 765.96]  uh on the other end of the spectrum like it's a public facing application they want to be really
[765.96 --> 771.26]  sexy and convert a lot of users and build a lot of affect and loyalty then it starts to sound
[771.26 --> 775.06]  like rich client might make a lot of sense because anything happening locally in your browser is a much
[775.06 --> 780.20]  tighter feedback loop and you have a lot more kind of ux uh tricks in your toolbox but on the other
[780.20 --> 784.70]  you know on the other hand if what they need is like they don't have a lot of money uh they they
[784.70 --> 788.82]  don't have a lot that maybe they'll have a handful of users and it's a it's a seldom used app
[788.82 --> 795.42]  front-end application development like with javascript is like significantly more expensive and i think that
[795.42 --> 800.86]  some people don't acknowledge that because they're so busy trying to sell browser as the runtime
[800.86 --> 804.96]  everything's going this way but you have to acknowledge like it's doing a lot more work like
[804.96 --> 809.70]  a back-end rails app it's like a specification of the user interface we're just rendering some html the
[809.70 --> 814.36]  browser's actually doing the ui programming but like introducing a fat client application is just
[814.36 --> 818.10]  like a much more expensive thing because now you're building two things you're building an api application
[818.10 --> 824.98]  and you're building a fat client user interface application um and and i try to be as cognizant of
[824.98 --> 829.42]  the cost of that as possible in spite of the fact that i'm super duper excited about all the cool
[829.42 --> 835.86]  stuff you can do on the front end yeah i think i fall in that that that same category where um you
[835.86 --> 839.82]  know depends obviously on the customer's needs and on the actual business goals of the application that
[839.82 --> 845.04]  they're building and their budget and all sorts of things like that um oftentimes what i find is a
[845.04 --> 853.24]  very simple traditional web application um can serve companies quite well at first and then and you
[853.24 --> 857.80]  just kind of sprinkle in the javascript you know the interactions here you know make this uh do that
[857.80 --> 864.54]  fancy thing um maybe have some ajax based stuff but still doing the traditional style and then over
[864.54 --> 869.68]  time it gets to the point where they just keep asking for more and more and more of that to where
[869.68 --> 875.62]  even if you've been pretty diligent which i try to be with the the uh structure of the javascript
[875.62 --> 881.68]  side of the application which has been growing in line count right yep it gets a certain point where it
[881.68 --> 887.76]  becomes not unmaintainable but just not as efficient as if this would be you know an ember
[887.76 --> 893.14]  app with a with an api um do you guys the worst part of the worst part about that yeah the worst
[893.14 --> 900.10]  part about that particular phenomenon right is that um let me phrase it this way going back to sort
[900.10 --> 905.38]  of because uh um was it adam you mentioned that you just moved to one week sprints we were talking
[905.38 --> 911.24]  about like agile stuff right so one of the one of the one of my favorite agile dogmas is uh when you
[911.24 --> 915.38]  pull a story card and you're trying to implement it do the simplest thing that could possibly work
[915.38 --> 922.80]  right um i think a lot of agile teams fall into this trap of uh equating simplest with quickest to
[922.80 --> 929.86]  get done right and so that's the truth for sure so quickest to get done is let's just spin up a rails
[929.86 --> 935.44]  app put a view on there and then you know maybe iteration two three four we start sprinkling on
[935.44 --> 940.36]  unstructured javascript and sort of like the you know the the the front end equivalent of like one
[940.36 --> 948.06]  gigantic main method that we kind of like tease apart in an ad hoc fashion um the the problem with
[948.06 --> 953.98]  what i call like the simple the simple trap is you're kind of going up this complexity hill
[953.98 --> 959.12]  in a monolithic way uh in a totally unstructured way from the front end perspective and then all
[959.12 --> 963.44]  of a sudden you'll reach a point where it's just like you can't go any further and they want features
[963.44 --> 967.72]  that would demand of a fat client front end app like maybe it's a graphing tool and they want zoom
[967.72 --> 972.60]  and filter and all this stuff that you can't possibly rasterize on the back end uh there's no
[972.60 --> 976.50]  there's a huge chasm there there's no logical way to take the stuff that you've already built
[976.50 --> 982.88]  and iterate further to where they need to go you have to you have to break that monolith up now
[982.88 --> 988.70]  and and do some amount of rework and and build a new thing and breaking it up is really hard and and
[988.70 --> 992.82]  rework is really hard especially if somebody else is paying you for it and you're the one who
[992.82 --> 998.42]  recommended them that they go down that path in the first place so of the greenfield apps what do
[998.42 --> 1003.70]  you give me that percentage breakdown obviously just ballpark it uh new projects how how many are fat
[1003.70 --> 1015.38]  clients of our new of our new projects um probably two-thirds fat client one-third uh uh all back end
[1015.38 --> 1022.74]  just like a api to a uh well what do you know back end well i guess as i think about it i'm trying
[1022.74 --> 1028.86]  to think like when was the last time we had a client who who actually engaged us for a traditional like
[1028.86 --> 1037.62]  rails view layer yeah um i think maybe a fair percentage would be to say like 50 50 fat client
[1037.62 --> 1043.80]  web being 50 and then the other 50 being a combination of just uh like device integration network
[1043.80 --> 1049.74]  integration all back end services and also maybe a little bit of rail traditional rails crud um but
[1049.74 --> 1053.22]  we don't see a lot of traditional rails crud anymore because i think that the skills have commoditized
[1053.22 --> 1059.74]  a bit uh and it's you know a lot of people can get by just fine on that stuff without needing to call
[1059.74 --> 1065.88]  for help right cool interesting stuff i think you know those those decisions obviously as developers
[1065.88 --> 1070.90]  or as consultants whatever role we play we're making these decisions on which way do i go so now let's get
[1070.90 --> 1077.14]  back into lineman let's assume you know i'm convinced i need a javascript fat client lineman looks cool
[1077.14 --> 1082.42]  lineman says that its mission statement is to make fat client javascript web applications as easy to
[1082.42 --> 1087.46]  build as traditional server-side html web applications that's your guys's goal so what are the killer
[1087.46 --> 1098.94]  features what makes lineman awesome to work with so um caveat of uh when you're the person who built the
[1098.94 --> 1104.60]  thing you you you you use the thing differently than than anyone else will use the thing my usage
[1104.60 --> 1110.54]  patterns of lineman are probably very different than uh most of our users but so i can only really
[1110.54 --> 1114.00]  speak for myself because i'm not very good at marketing this thing i spent like a year and a
[1114.00 --> 1120.18]  half to to build that talk that you referenced at rails conf um my usage is i really like rapid
[1120.18 --> 1124.98]  prototyping new ideas quickly right so like i previously have been using rails for rapid prototyping
[1124.98 --> 1129.50]  but when it came to javascript interactions i love being able to say lineman new foo create a new
[1129.50 --> 1134.08]  project i got to build already and i can just start start writing code and it's immediately showing up
[1134.08 --> 1140.04]  in a browser um i like the consistency from project to project when we're all building lineman applications
[1140.04 --> 1146.70]  i like that we can take a common bit of uh one of our uh the biggest lineman users is rackspace um so
[1146.70 --> 1151.18]  there's a group at rackspace that's doing internal tooling and one of the cool things that they can do is
[1151.18 --> 1155.26]  they have like a sort of standard stack of lineman plugins and lineman actually supports meta plugins
[1155.26 --> 1159.98]  too so you could say like make a plugin called lineman rackspace and all it represents is like
[1159.98 --> 1164.38]  pulling in all of the plugins that it depends on at the versions that they specify and maybe any sort
[1164.38 --> 1168.68]  of deviations and configuration so you could literally as like an organization just settle on
[1168.68 --> 1174.90]  like this is our default you know initial project stack um and be off to the races on a new project in
[1174.90 --> 1181.06]  like two command lines um the other thing the other kind of half to the equation other than the
[1181.06 --> 1186.44]  like what lineman doesn't do like unlike yeoman it doesn't generate a whole bunch of garbage into
[1186.44 --> 1190.64]  your project that you can't tease out later can't upgrade later or have to deal with you know a
[1190.64 --> 1200.30]  community that's not supporting your your your uh bootstrap nonsense um the other thing that that i
[1200.30 --> 1205.02]  think is really great about lineman is that you don't have to throw the baby out with the bathwater
[1205.02 --> 1210.30]  from a server-side perspective like if i'm building a rails application um and i just want to you know
[1210.30 --> 1215.10]  do the next major feature on a standalone page as a lineman application that would be a fat client
[1215.10 --> 1219.82]  javascript application i can build that lineman application at in a world where that's the only
[1219.82 --> 1224.08]  thing that exists totally separately totally physically divorced but then lineman has features
[1224.08 --> 1228.42]  to proxy back to the rails application easily so like any request that lineman doesn't know how to
[1228.42 --> 1234.44]  handle it'll just phone home to rails um and uh that way you can develop against lineman's port but
[1234.44 --> 1239.50]  still be inside of your rails application and get all of the benefit without having to completely
[1239.50 --> 1245.60]  redesign your rails application to be completely just like you know api uh api only uh or divorced
[1245.60 --> 1251.12]  from any hint of erb or or templates that drop in little javascript variables so you can get up and
[1251.12 --> 1256.12]  running on almost any project immediately even if it's a long-standing existing one it's not only
[1256.12 --> 1261.12]  for greenfield projects so do you just check that code into your main app then or do you have
[1261.12 --> 1267.02]  do you keep separate repositories or either i guess either it depends on you know a person's priorities uh
[1267.02 --> 1273.16]  if the if the team is already uh figured out cracked the nut on how to do deployments well with multiple
[1273.16 --> 1278.04]  repos at multiple versions then this is just another repo uh and just like you'd probably put
[1278.04 --> 1284.02]  your iphone or android application in a separate repo um it can make sense to put your fat client
[1284.02 --> 1287.16]  javascript application in a separate repo because at the end of the day that's all it is it's just
[1287.16 --> 1292.38]  another client to your api but i think for most people especially right out the gate um because
[1292.38 --> 1296.42]  versioning is extra hard and because the deployment story can be more more complex just
[1296.42 --> 1303.72]  adding that to your repo as like a another root directory is probably a okay um and then on the
[1303.72 --> 1308.48]  the benefit of doing it that way too is that we have a gem for rails called rails lineman that you just
[1308.48 --> 1313.26]  you merely install the gem and tell it where your lineman app is and then whenever you run rake assets
[1313.26 --> 1318.16]  pre-compile like as part of your deploy it'll actually do a lineman build sneakily shove that into
[1318.16 --> 1321.20]  your public assets directory and so you don't have to configure it but you actually get
[1321.20 --> 1328.42]  kind of get all of lineman's assets for free without having to think let's pause the show for
[1328.42 --> 1333.94]  a minute give a shout out to a sponsor if you've ever gotten to work only to find out something
[1333.94 --> 1339.36]  happened while you're out the server's down customers are unhappy chaos everywhere you gotta
[1339.36 --> 1345.40]  listen up one of our new sponsors and i'm excited to have them on board pager duty pager duty eliminates
[1345.40 --> 1351.08]  the noise chaos and manual processes to help you streamline your entire incident
[1351.08 --> 1356.32]  life cycle and ultimately decrease the amount of time it takes you to resolve issues you can get
[1356.32 --> 1362.22]  reliable it alerting and on-call management you'll receive instant notifications when incidents are
[1362.22 --> 1367.84]  reported so you can quickly resolve those issues they're trusted by companies like etsy github
[1367.84 --> 1374.50]  nike and we want you to try them for free sign up today for a free 30-day trial at pagerduty.com
[1374.50 --> 1377.68]  slash the changelog and tell them the changelog sent you
[1377.68 --> 1385.56]  so you mentioned yeoman briefly and it seems like if lineman had a competitor it would be yeoman
[1385.56 --> 1392.60]  both tools trying to provide you know help for front-end projects um yeoman is a combination of
[1392.60 --> 1397.30]  yo which i believe and you can correct me if i got details wrong but this is a scaffold generator a
[1397.30 --> 1404.72]  code generator grunt which is the the the task runner and then bauer i believe is or the dependency
[1404.72 --> 1411.46]  management of some kind i think it's bauer um how does lyman compare to yeoman uh pros and cons of
[1411.46 --> 1418.30]  either side um we have a a table up uh at linemanjs.com where i spent some time answering specific
[1418.30 --> 1423.80]  questions from the community about this and i wish i had in front of me um so so go to linemanjs.com
[1423.80 --> 1429.82]  check out the table for probably better answers than this um but my um my off-the-cuff reaction is
[1429.82 --> 1439.02]  that yeoman misses some opportunities that lineman seized upon and it it does some things that i think
[1439.02 --> 1446.04]  are very attractive for adoption purposes but but long term have a poisonous effect on on the
[1446.04 --> 1451.96]  sustainability of projects one of the opportunities that it failed to realize is that there is a higher
[1451.96 --> 1459.18]  order concern than simply running tasks a build is really you know like a its own domain model it
[1459.18 --> 1463.64]  runs tasks but it has to figure out the order and when and how to do it in the in a way that's like
[1463.64 --> 1469.88]  maybe you know um iterative like if like say only one file changes just compile that one file and find
[1469.88 --> 1474.34]  a way to graft it in as opposed to rebuild everything on every single file change right so there's a whole
[1474.34 --> 1478.08]  bunch of build responsibilities that they just kind of left on the table that something like joe
[1478.08 --> 1487.08]  lissa's broccoli tool was built to be um the other aspect uh uh that that stands to me about yeoman that
[1487.08 --> 1493.82]  really bothers me is that it's got all of these community driven generators uh for you like they've
[1493.82 --> 1500.16]  got this website that's like you know pick which of the 15 bootstrap three generators you want if you
[1500.16 --> 1505.90]  want to pull like start a bootstrap project or if you want to start this project here and some of them
[1505.90 --> 1510.50]  are in total disarray some of them are relatively maintained some of them are maintained but they
[1510.50 --> 1516.22]  actually have like very weird or or incongruent opinions about how to do things well um but all
[1516.22 --> 1522.02]  of them just generate a lot of cruft that you then have to commit into your repository uh and when you do
[1522.02 --> 1529.72]  that if you need to upgrade later maybe none almost none of those generators have clear sane upgrade
[1529.72 --> 1533.98]  paths so it's like you're making a project and it's like at this point in time this project will and
[1533.98 --> 1538.42]  forever will be you know tied to this version of this one particular tool because we chose to
[1538.42 --> 1546.06]  you know uh get the convenience of an easy quick start um uh with without you know having to have
[1546.06 --> 1550.30]  paid the cost for a tool that sort of like embedded conventions for us it just sort of handed all this
[1550.30 --> 1555.00]  stuff um and that really that really bums me out because when i see that there's not a lot of help
[1555.00 --> 1560.44]  i can do for people other than recommend that they start fresh yeah i've used yeoman a little bit for a
[1560.44 --> 1564.88]  few small angular apps and i can definitely those statements resonate with me i found your table by
[1564.88 --> 1570.90]  the way so just a few other things here that you missed uh you provide html5 push state simulator
[1570.90 --> 1578.78]  built in um i think really the big differentiator from my perspective is the testing story so lyman
[1578.78 --> 1584.34]  seems to provide for those interested in in writing tests for their javascript which is a pretty good
[1584.34 --> 1590.78]  idea if you ask me um you have a test runner you have api stubbing and stuff like that um so that
[1590.78 --> 1596.54]  you can so you can easily get started testing can you talk about the how the test runner works yeah so
[1596.54 --> 1602.86]  the the test runner that we use is called testum uh and it was written by a uh a great developer down
[1602.86 --> 1609.24]  i think he's in atlanta his name is toby ho and uh testum is a test runner that was written to be
[1609.24 --> 1615.00]  completely agnostic of the test library so you can use testum with uh uh almost anything you can use
[1615.00 --> 1620.54]  it with obviously q unit jasmine and mocha the big three uh you could use it with casper you could use
[1620.54 --> 1628.06]  it with with with almost anything you want on on the library end uh and then on the other end it it's
[1628.06 --> 1632.78]  able to capture lots of different browser environments with a little tiny script and some
[1632.78 --> 1640.42]  socket io uh so you can easily run uh your tests in any browser you like like uh uh you know whether
[1640.42 --> 1645.40]  that's ie safari firefox or or what have you or or mobile browsers or different devices on your network
[1645.40 --> 1652.40]  if you have a device lab and so forth and uh it does all of this with a very sexy uh n curses like
[1652.40 --> 1658.30]  terminal ui that lets you um like you know arrow between the different the different user agents that
[1658.30 --> 1662.76]  are running your tests you can see how the uh error messages might differ from one to the next
[1662.76 --> 1670.44]  um and then it sort of ties a bow around all that with a very nice uh ci mode so this is all the
[1670.44 --> 1674.64]  interactive mode but in the ci mode it'll run under phantom js and it'll give you you know any format
[1674.64 --> 1678.70]  you want like whether you want the j unit style xml formatting or whether you want tap formatting
[1678.70 --> 1684.54]  uh so that you can you know aggregate those results in your ci system uh so testum is really like
[1684.54 --> 1690.00]  they toby did 100 of the heavy lifting there what lyman does just like it does with all of its grunt
[1690.00 --> 1694.20]  tasks that it runs and everything else is it just provides a default configuration that just works
[1694.20 --> 1701.12]  out of the box um and and this is maybe a little selfish but i also shove all of my um uh jasmine
[1701.12 --> 1705.08]  test helpers that i've built over the years into your helpers directory for you right off the gate
[1705.08 --> 1709.76]  um and i do that because i use them and i was sick of downloading them but hopefully you know people
[1709.76 --> 1714.96]  find some benefit from that as well cool yeah that leads me to my next question because uh you know
[1714.96 --> 1720.10]  talk about downloading uh helpers and whatnot the other but another big differentiator yeoman the
[1720.10 --> 1724.60]  third part of that would be bauer which is you know it's not really dependency management but it's
[1724.60 --> 1730.68]  a downloader so to speak um lyman seems to just completely punt on package management it's true
[1730.68 --> 1737.34]  yeah is that purposeful or it is purpose you got tired it's uh it's very intentional and i think that
[1737.34 --> 1742.86]  it's uh a couple years ago now i wrote a blog post called unrequired love about required js
[1742.86 --> 1749.50]  um and how i think that in open source my goal has always been to identify areas of pain
[1749.50 --> 1755.76]  and then think really hard about why am i feeling that pain and then and then sit and then think
[1755.76 --> 1760.24]  really hard again and then eventually start writing tools to alleviate that pain somewhat
[1760.24 --> 1766.74]  and i feel like the obsession with front-end package management tools whether it's require or browserify
[1766.74 --> 1771.42]  or to the extent that people use bauer as a dependency management tool when i agree with you it's not
[1771.42 --> 1777.64]  really it's more like a very fancy downloader right um what i worry is that they're identifying the pain
[1777.64 --> 1781.66]  of i've got all of these third-party scripts everywhere but then they they apply the wrong
[1781.66 --> 1785.00]  prescription which is let's give me something to manage all of these third-party scripts
[1785.00 --> 1790.12]  when a better prescription would be let's write leaner meaner applications that don't you know
[1790.12 --> 1793.82]  that are architected well enough that we can solve a lot more of our own problems without
[1793.82 --> 1799.88]  immediately leaning on a bajillion you know shitty javascript plugins everywhere um and
[1799.88 --> 1805.26]  also from the from the from the app code perspective where you know there's a lot of people who are
[1805.26 --> 1812.34]  using packaging tools to kind of organize and require uh explicitly their own code uh uh you know
[1812.34 --> 1816.52]  like say like i've got a model that my view wants to use i require that model from that view
[1816.52 --> 1820.92]  there's nothing wrong with that it's just it's not built into javascript it's not you know part of the
[1820.92 --> 1824.90]  language it's not something the browsers understand yet and so you're kind of marrying yourself to this
[1824.90 --> 1830.74]  one-off implementation that will probably look silly two three four years from now um when you
[1830.74 --> 1834.82]  could just solve it the way that you know by respecting what a javascript web application really
[1834.82 --> 1841.20]  is which is the you know it is equivalent to the concatenation of all of its listings so just know
[1841.20 --> 1846.76]  how to concatenate it right and then you're done and better yet write code that is order agnostic
[1846.76 --> 1850.96]  and design systems that don't matter what order you load stuff in so then you don't have to even
[1850.96 --> 1855.86]  worry about what order it gets concatenated in um those are the ways that we've tried to solve those
[1855.86 --> 1862.34]  problems now people like to use bauer we have a lineman bauer uh extension um that that you can use
[1862.34 --> 1868.26]  with lineman but i personally have been frustrated by it for for a lot of reasons one is that it it
[1868.26 --> 1874.70]  by default will go and grab master of your github repo and that's not a release right it's got a
[1874.70 --> 1879.92]  version probably in a file somewhere uh but it's it's going to be divergent from the release which
[1879.92 --> 1883.36]  has caused a bunch of my friends who maintain libraries to freak out because now they're
[1883.36 --> 1887.14]  getting all these issues filed against stuff that's happening in master when people are just
[1887.14 --> 1895.00]  grabbing the wrong artifact uh it encourages organ uh like open source maintainers to start committing
[1895.00 --> 1898.88]  generated artifacts and then track that separately so then the source of truth of like it is just
[1898.88 --> 1905.50]  counter diversion control in my opinion um and then the worst part kind of belies your first statement
[1905.50 --> 1909.30]  which is well it's not a dependency management tool it's a downloader like the fact that it
[1909.30 --> 1913.26]  seems like a dependency management tool gives everyone a false sense of confidence that it's doing
[1913.26 --> 1919.88]  things like you know negotiating uh version conflicts and transitive dependencies uh uh you know that
[1919.88 --> 1925.56]  that every single time you download a specific version of a dependency you're getting exactly the
[1925.56 --> 1931.44]  same one like you would be from npm or from ruby gems you're not and so those people using bower are
[1931.44 --> 1935.58]  like well don't commit your your vendor dependencies because you have a bower like part of your build
[1935.58 --> 1940.22]  will just pull those in and then you'll do a build and then they'll just be kind of transient um
[1940.22 --> 1945.78]  it's it seems totally backwards to me that yeoman on one hand will generate all of this cruft that is
[1945.78 --> 1951.18]  literally your application forever uh that you don't need and that you can't upgrade uh uh and then
[1951.18 --> 1956.34]  on the other hand not commit the actual stuff that's like literally your runtime the system
[1956.34 --> 1961.80]  that you're building uh that that isn't controlled by you shouldn't be controlled by you so i feel like
[1961.80 --> 1967.30]  it's just coming at a lot of these issues from diametrically opposed perspectives yeah
[1967.30 --> 1973.88]  yeah and so what do you do then you just like w get the file into a vendor and then you just
[1973.88 --> 1981.08]  i mean just old school style old school man yeah it it you know if it if it doesn't hurt if it's
[1981.08 --> 1985.50]  not broke don't fix it i i just have not run into the problems of scale that some other people i've
[1985.50 --> 1989.66]  talked to had like you know basically anytime i get into a fisty cuffs internet fight with somebody
[1989.66 --> 1994.72]  about this they eventually pull out like well my app is eight megabytes of compressed javascript so i
[1994.72 --> 1999.94]  have these problems i'm like okay cool but don't turn around and like offer this as generic advice of
[1999.94 --> 2005.88]  like best practices that everyone should be doing because whether that was a necessary eight megabytes of
[2005.88 --> 2011.32]  complexity which i doubt um or or not it's just not representative of most web applications it's a
[2011.32 --> 2015.66]  problem you can push off till later and every time i see people try to adopt it on day one whether it's
[2015.66 --> 2022.88]  browserify require um or even bauer it just introduces all of these stupid engineering problems that are a
[2022.88 --> 2027.92]  distraction from the goal of building an application and lineman's all about getting up and running and
[2027.92 --> 2031.20]  building an application quickly and not having to worry about those stupid engineering problems
[2031.20 --> 2038.40]  like like build get focusing on your build and so forth um and uh it seems to just not respect the
[2038.40 --> 2045.56]  cost of that right on so lineman you know lineman js interestingly the name is lineman js but if you go
[2045.56 --> 2054.60]  to github and you click on the language statistics uh 59 coffee script 40 javascript but i can't actually
[2054.60 --> 2060.84]  find where that javascript is coming from it seems like it's all coffee script i think it's probably uh
[2060.84 --> 2066.32]  in the archetype uh which is the project that gets generated when you line the new there's javascript
[2066.32 --> 2070.42]  in that i thought maybe there was some sort of thing that was automatically built that had the js in
[2070.42 --> 2078.08]  it or something no and in fact uh you know i understand why um there's a first of all there's
[2078.08 --> 2083.54]  the natural reticence to coffee script in the in the broader outside of ruby community yeah because it's
[2083.54 --> 2090.92]  different uh and it's non-standard and it is uh you know it looks foreign if you've not used a dynamic
[2090.92 --> 2094.52]  language before and it looks for foreign to some ruby who've never used a white space sensitive
[2094.52 --> 2100.28]  language before um personally i'm sold because i you know there's myriad benefits that we could talk
[2100.28 --> 2105.98]  about separately but um the things that are important to me is i want to write code that's as
[2105.98 --> 2110.26]  clear and as reliable and understandable and maintainable as i possibly can because maintaining
[2110.26 --> 2115.96]  open source is hard but i want to be handing people code that they can run with and and easily
[2115.96 --> 2121.92]  understand uh and make sense of and so when you install a lineman and then run a um you know lineman
[2121.92 --> 2126.62]  new and make a project everything is all javascript no coffee script gets generated unless you use the
[2126.62 --> 2134.54]  tac tac coffee um uh option to to convert all of that to coffee script for you um and so i feel like
[2134.54 --> 2139.36]  it's a kind of a straw man argument you're not the first person to bring it up some people have
[2139.36 --> 2142.32]  literally been like i won't use this because it was written in coffee script and that just seems to
[2142.32 --> 2147.38]  me like it's a coming from a point of entitlement right like i refuse to spend the 30 minutes it
[2147.38 --> 2151.74]  takes to learn coffee script because it's really a very very tiny language when you think about it
[2151.74 --> 2156.56]  and therefore your thing sucks and we should all not contribute to it and we shouldn't use it
[2156.56 --> 2161.64]  right plus as you say this is a tool that you use and as an end user it's complete it's a nothing
[2161.64 --> 2165.76]  to you whether what it was written in right it's generating javascript for you it's a command line tool
[2165.76 --> 2173.72]  um it shouldn't matter that being said like as you said some people uh you know they're very
[2173.72 --> 2178.08]  averse to coffee script have you gotten a lot of that kind of feedback with lineman maybe even on the
[2178.08 --> 2184.10]  contribution side how the the contributors worked uh contributors have been fantastic i mean i always
[2184.10 --> 2191.02]  want more of them uh i guess i'll break that up into two questions first on contributors i feel like
[2191.02 --> 2194.84]  because we've been using this every day for two years on almost all of our client projects
[2194.84 --> 2201.22]  uh lineman solves the problems i needed to solve and it is mature from my perspective i mean we never
[2201.22 --> 2205.62]  did a 1.0 release but it does almost everything i need pretty well and there's things i want to fix
[2205.62 --> 2211.64]  like there's rough corners but i can live with them pretty well um and so when people open issues uh or
[2211.64 --> 2217.36]  have problems i would really love if they would more often contribute uh to the project because it's
[2217.36 --> 2222.24]  their their itch is not my itch and so i could half-heartedly go and try to build it for them
[2222.24 --> 2228.04]  um but but really there's uh just sort of a depression that sinks in when you realize that
[2228.04 --> 2231.70]  you're spending a lot of time just trying to make other people happy on the internet for free
[2231.70 --> 2237.96]  uh just like arguing on the internet and uh uh it bums me out when people kind of like open an issue
[2237.96 --> 2243.66]  from from from a from a state of entitlement uh like hey your thing's dumb because it doesn't do this
[2243.66 --> 2248.18]  and then i i get the thing in my inbox and realize i'm blocking somebody and i feel really guilty and i feel
[2248.18 --> 2253.14]  beholden to them to like you know go implement that thing uh when you know 90 percent of people
[2253.14 --> 2258.70]  never even offer or think to open a pull request um that's just that that bums me out and now i've
[2258.70 --> 2262.30]  forgotten the first half of the question that i also was excited oh just if you have a lot of
[2262.30 --> 2267.94]  so-called haters because of the copy script i think there's an interesting point to this too which is that
[2267.94 --> 2275.56]  uh coming from the ruby community where like i think that like i see the same 100 150 people at all of
[2275.56 --> 2281.12]  these ruby conferences across literally the world it's a much much smaller tighter knit uh community
[2281.12 --> 2286.72]  and as a result we kind of all like you know there's a monoculture aspect to that you know
[2286.72 --> 2292.20]  high mind yeah yeah we have debates and arguments but then things settle down and we either separate
[2292.20 --> 2299.72]  into camps or we just sort of adopt the new the new way you can't do that with javascript because
[2299.72 --> 2303.86]  everybody is stuck with javascript the whole world is writing javascript and they're all from these
[2303.86 --> 2307.24]  different tribes and these different heritages and different back-end environments and so
[2307.24 --> 2312.50]  a lot of times i'll see people whether it's from ruby or python or dotnet or java they will enter
[2312.50 --> 2317.96]  the javascript world with nothing but the perspective of their back-end experience and then they'll
[2317.96 --> 2324.12]  immediately freak out because they can't see any agreement like what's the right way to do x right
[2324.12 --> 2329.46]  what's what's the standard way to do y and the answer is like of course there is no right way
[2329.46 --> 2337.44]  there is no standard way um and and you have to kind of identify just to signal to noise you know
[2337.44 --> 2344.02]  manage your life you have to identify a group that that seems to agree with you well enough that you
[2344.02 --> 2349.48]  can be productive uh and one of the ways that i have sort of self-selected a group when i'm working
[2349.48 --> 2355.02]  on node.js stuff is if somebody comes to me and says that because i write coffee script i'm my project's
[2355.02 --> 2361.32]  dumb and i'm dumb too i'm like boom bozo button i don't yep you're out of my tribe the world is much
[2361.32 --> 2366.06]  too big right for me to feel like i have to make absolutely everybody happy please tell me you have
[2366.06 --> 2371.60]  a real bozo button i was gonna say i like that button i want that button uh i well i i tapped on
[2371.60 --> 2376.38]  the lid of my water bottle when i said it so that'll be the new bozo button i guess i'd love to have that
[2376.38 --> 2384.22]  yes right and it just like automatically blocks them on twitter and uh github there could be an
[2384.22 --> 2390.42]  api and everything for it yeah yeah i love this because you know open source is so interesting we
[2390.42 --> 2395.12]  have you know the techno they're the purely technical aspects of it right which we can talk
[2395.12 --> 2400.58]  about all day long and debate and uh evaluate and improve and all that and then you have the social
[2400.58 --> 2407.94]  meta kind of like the people of open source and all of the interesting and troublesome
[2407.94 --> 2414.90]  situations that arise around that um then you have the corporate the corporate aspect where we see
[2414.90 --> 2421.80]  more corporate backing of open source um licensing like there's all these kind of conversations around
[2421.80 --> 2428.40]  open source that we can have and we do have um and justin you have a talk that's coming up
[2428.40 --> 2431.26]  you've been you've been working on it you have an abstract called the social
[2431.26 --> 2438.54]  coding contract which i think speaks into this milieu of the the community the open source community
[2438.54 --> 2442.50]  especially in in the world that you run which is really the ruby and javascript communities
[2442.50 --> 2447.44]  specifically um i'll just pull a quote you sent this to us i'd love to talk about it a little bit
[2447.44 --> 2450.54]  here i'll pull a quote out of this it's probably not going to get the gist but it's my favorite
[2450.54 --> 2456.54]  paragraph and you say sometimes i swear i can feel a teetering sensation from how precariously
[2456.54 --> 2462.24]  our applications are perched on top of an ever-growing web of open source dependencies
[2462.24 --> 2467.86]  fears that our tech stack is about to topple over have been for fomenting in recent years
[2467.86 --> 2474.16]  but are those fears founded that's kind of the question you pose um you have a specific
[2474.16 --> 2479.62]  scenario which kind of leads to this go ahead and speak into that and and tell us your thoughts on
[2479.62 --> 2490.50]  this yeah so i think the zeitgeist um right now is a little bit cynical uh at least among the people
[2490.50 --> 2497.54]  that that i follow on twitter and that i that i engage with in the community is that we've been
[2497.54 --> 2502.88]  on this sort of we've been riding this rocket of ever increasing convenience in the open source world
[2502.88 --> 2506.82]  it used to be the case that open source was a pain in the ass and you had to be really thoughtful
[2506.82 --> 2511.84]  when you pulled in an open source dependency not just like legally but like literally like pre-github
[2511.84 --> 2517.82]  pre all of these cool dependency managers like i remember like the pain even in 2004 of getting a jar
[2517.82 --> 2522.92]  and getting that jar to like in my class path and working in my java project correctly whereas like
[2522.92 --> 2529.92]  rubygems made it quite a lot easier bundler made it easier still uh npm makes it like almost comically
[2529.92 --> 2536.58]  easy to both publish you know dinky little scripts and also to consume them um we're so from a package
[2536.58 --> 2541.10]  management perspective it's easier and easier to slurp in new dependencies uh and it's easier and
[2541.10 --> 2547.06]  easier to publish new ones and so um because there's so many solved problems out there and no one wants to
[2547.06 --> 2554.22]  feel like they're reinventing the wheel every single application becomes a a kind of defined by the 15
[2554.22 --> 2561.76]  totally disparate things that it stands on top of and those things are maintained by for the most part
[2561.76 --> 2568.58]  white dudes in their 20s doing it in their spare time who might you know probably have a 40 chance
[2568.58 --> 2576.88]  of never committing to that thing again right and that is what runs the world software you know that's
[2576.88 --> 2581.68]  that's what runs pretty soon you know real-time systems even not like about several friends who
[2581.68 --> 2586.20]  work in real-time systems this trend is coming to real-time systems things that run hydroelectric
[2586.20 --> 2591.02]  jams things that run airplanes right those embedded devices are getting so strong now that they can
[2591.02 --> 2597.00]  realistically run you know uh if not dynamic languages certainly stuff like rust and go and
[2597.00 --> 2604.06]  that's been brought up in this culture of of of convenient uh uh open source grabs meanwhile we're
[2604.06 --> 2608.72]  seeing like in the news constantly all these open source projects that literally 80 percent of servers
[2608.72 --> 2612.66]  rely on be like oh there's a gigantic security hole and everything we thought was secure for the
[2612.66 --> 2618.96]  last 10 years on the internet wasn't yes uh we have all of these basically like you could almost just
[2618.96 --> 2624.64]  paint uh your application as a graph of single points of failure like here's all of the millions
[2624.64 --> 2629.72]  of things that could go wrong that could break us and we don't understand any of them because our
[2629.72 --> 2634.02]  understanding stops as soon as we've typed the name of the gem into our gem file or the name of the
[2634.02 --> 2640.44]  package into our package json and so the thrust of the talk is like not that this is necessarily bad
[2640.44 --> 2645.02]  and we're all doomed it's that users i think have a much greater responsibility to understand what
[2645.02 --> 2652.22]  dependencies they're pulling in who's maintaining them under you know what pretenses uh uh not just
[2652.22 --> 2657.56]  how how it's licensed but how is it being built like is it is it is there a healthy community around
[2657.56 --> 2663.66]  it um is it is it small enough to not be an albatross but is it big enough to have the gravitas
[2663.66 --> 2671.02]  necessary to be able to rely on you know stable releases and fixes in the future and i think most
[2671.02 --> 2675.44]  users have kind of just lowered their standards over time as the convenience has gone up from
[2675.44 --> 2679.06]  companies like that use open source like you mentioned companies companies have a similar
[2679.06 --> 2684.00]  responsibility like they're getting a tremendous lift a huge amount of free value from open source
[2684.00 --> 2689.60]  and and if i think of my friends who work in enterprises they have carte blanche ability now to
[2689.60 --> 2693.88]  use whatever open source they like maybe they have to run a license by a lawyer or something but then
[2693.88 --> 2698.86]  like if they try to spend two hours to submit a patch it's it's you know basically they have to
[2698.86 --> 2704.98]  either use vacation time and then still talk to the lawyers uh or or they just you know don't and
[2704.98 --> 2709.56]  can't and i think that corporations that are using open source and getting all of this tremendous value
[2709.56 --> 2716.14]  from it have a responsibility to give back something and i don't know exactly what that is yet but that's
[2716.14 --> 2720.24]  some some of the stuff i'm going to be chewing on for the talk but the maybe the more interesting
[2720.24 --> 2724.50]  part to me because i'm more you know i publish a lot of open source and not everyone does is i want
[2724.50 --> 2728.00]  to kind of peel the curtain back a little bit into just like what's the psyche of an open source
[2728.00 --> 2735.28]  maintainer and for me the the saddest thing about it is that i build tools to solve problems that i
[2735.28 --> 2740.96]  have and i get some day one gratification of like man i just solved that problem that i had i granted
[2740.96 --> 2745.12]  i spent all day on a tool to solve the problem when i could have solved the problem some other way in 30
[2745.12 --> 2750.40]  minutes but you know now i've automated it and that's fantastic but then days like two through n of
[2750.40 --> 2755.16]  the project are well i had that first problem but now almost all of my problems are maintaining this
[2755.16 --> 2761.08]  thing that solves that same problem for other people into perpetuity and when you build a thing
[2761.08 --> 2766.02]  because you wish it existed in the world you don't get to enjoy it the same way as if it had already
[2766.02 --> 2771.12]  existed because you have to maintain it you have to worry about it and you have to you take the heat
[2771.12 --> 2777.10]  when it doesn't work out for some stranger on the internet um and all of those things really
[2777.10 --> 2782.72]  contribute to the sort of burnout that we see in open source um and and that burnout feeds directly
[2782.72 --> 2787.92]  into the instability of all the dependencies that we stand on so there's just this uh healthy unhealthy
[2787.92 --> 2793.88]  burning of the candle at both ends that's going on uh and it's structural and we have to really think
[2793.88 --> 2800.12]  radically i believe to to figure out what's a sustainable way forward um for all of these
[2800.12 --> 2803.62]  shared tools because granted everyone no one wants to have to like you know resolve all the same
[2803.62 --> 2808.22]  problems in every single enterprise and just sort of have like this big nasty dark closet of wheel
[2808.22 --> 2814.84]  reinvention uh because that's you know similarly hugely error prone but there's got to be a better
[2814.84 --> 2821.42]  way uh to to sort of just find like that's why i called it the social coding contract like we have
[2821.42 --> 2828.44]  to find some sort of like you know cultural mores to um shift both our expectations as users and also
[2828.44 --> 2834.72]  how we view uh maintainers they are not these superheroes that that have like a bajillion stars on github
[2834.72 --> 2839.22]  and have figured out how to do software they're mostly just people who published a thing and it
[2839.22 --> 2845.56]  got popular and now their life is dominated by that thing let's pause the show for a minute give a
[2845.56 --> 2852.62]  shout out to a sponsor this sponsor is harry's and for many of us man or woman shaving is an absolute
[2852.62 --> 2860.48]  pain it sucks it's uncomfortable nicks cuts scrapes razor burn plus the razor blades today they're just
[2860.48 --> 2865.96]  crazy expensive and that's where harry's comes in they started by two guys who wanted a better
[2865.96 --> 2872.14]  product for shaving without having to pay an arm and a leg to get it harry's makes their own blades
[2872.14 --> 2877.68]  and they ask why pay 32 bucks or more for an eight pack of blades when it's just half the price with
[2877.68 --> 2884.88]  harry's on average an everyday shaver saves about 150 bucks a year on blades using harry's to wrap it all
[2884.88 --> 2891.04]  open a nice pretty bow satisfaction is guaranteed visit harry's.com right now and harry's will give
[2891.04 --> 2899.98]  you five dollars off if you use our special code changelog with your first purchase that's h-a-r-r-y-s
[2899.98 --> 2907.34]  dot com and enter the coupon code changelog at checkout and you get five dollars off start shaving better
[2907.34 --> 2914.26]  today wow so do you have any radical ideas are you just kind of broaching the topic at this point
[2914.26 --> 2919.74]  saying this is something that we need to talk about um i i have some but they're probably too early to
[2919.74 --> 2925.98]  speak with with any confidence i think that the um the overarching
[2925.98 --> 2934.14]  message is going to be that that both parties need to meet in the middle right users need to have a
[2934.14 --> 2938.50]  deeper understanding of what they're using you need to like default to open up source and look at how the
[2938.50 --> 2943.80]  source works and contribute back a little bit um because only if you're having the deeper understanding of
[2943.80 --> 2947.76]  what you're on top of could you ever hope to contribute there's like this demystification
[2947.76 --> 2951.78]  that occurs when you actually look at the source of the thing you're like oh wow that guy was a
[2951.78 --> 2959.16]  human huh i thought it was magic um yeah there was a real moment in my you know technical career
[2959.16 --> 2965.48]  as software developer where i went from being like too afraid to do that to like be that becoming my
[2965.48 --> 2969.40]  the first thing i do almost immediately sometimes to a fault where i'm like i'm gonna blame this
[2969.40 --> 2977.10]  dependency when really just my code is got a bug in it but but like i agree with you absolutely like
[2977.10 --> 2983.44]  you as users of open source like we should be hopping into that and being able to diagnose or try
[2983.44 --> 2990.08]  right it's difficult for beginners to do those kind of things but um you know the earlier and sooner you
[2990.08 --> 2996.14]  do it and dive into the mucky muck so to speak the sooner you realize like it's not magic in here this
[2996.14 --> 3001.52]  this black box has parts that make sense and some don't work and some do and and you grow as a
[3001.52 --> 3006.34]  developer as part of participating in that process i think that's changing though i think for beginners
[3006.34 --> 3013.18]  that's that's changing because of the source being so pointed to and pull requests being so social now
[3013.18 --> 3017.44]  i think that's that's beginning to evolve i think people are becoming more and more aware that
[3017.44 --> 3022.80]  their first resource should be not just asking your buddy hey how does this work or ask the maintainer
[3022.80 --> 3026.50]  hey where's the api for this or the docs for this or whatever it's like digging into the actual code
[3026.50 --> 3032.64]  themselves it's becoming i think that that thought jared is kind of evolving a bit i agree that it's
[3032.64 --> 3038.78]  evolving a bit and i think that github and pull requests um have helped but one of the things that's
[3038.78 --> 3043.24]  actually i think kind of unfortunate is that our tools have taken several steps back like i talked
[3043.24 --> 3049.70]  about just focus on ruby and javascript today say like ruby's debuggers aren't fantastic um ruby offers a
[3049.70 --> 3054.36]  lot of introspection capabilities of like what's going on in the runtime but not a ton of introspection
[3054.36 --> 3060.16]  about like where's this source and what is it and how do i open it um a node is about a bajillion
[3060.16 --> 3065.94]  times worse than this uh because uh debugging you know what's going on under the covers is notoriously
[3065.94 --> 3070.34]  difficult uh to the point that you know the operational standard in node is like oh well yeah
[3070.34 --> 3075.10]  every single node process leaks memory like a sieve so just make sure that operationally you can bounce
[3075.10 --> 3081.06]  those servers whenever you need to um and and it really starts to feel after a while like a black
[3081.06 --> 3087.44]  box like what's going on under here so i guess i mean one one approach would be invest the time in
[3087.44 --> 3094.10]  tools that make that lower that that barrier of entry to to hop over into the source code or even
[3094.10 --> 3099.16]  just like exclaim and visualize it and put it in your face even when you don't ask it to so that like
[3099.16 --> 3103.42]  you know sort of like code folding right in browser in editors what if you could just like every time
[3103.42 --> 3108.44]  you called a third party api you could unfold that code and see the source of that method like in
[3108.44 --> 3114.82]  every editor that sort of stuff would just dramatically i think uh increase the level of
[3114.82 --> 3122.52]  engagement from users yeah absolutely you think perhaps languages um like go and and russ have
[3122.52 --> 3128.16]  easier time developing those kind of tools we would have in our communities just because of the nature of
[3128.16 --> 3133.40]  the languages um it seems like this this thought kind of came into focus you said when uh you
[3133.40 --> 3139.46]  took over rspec given recently after jim after jim wyrick's death i know you are a huge fan of jim
[3139.46 --> 3145.12]  wyrick um can you speak to that kind of the process of taking over and just uh anything you like to
[3145.12 --> 3153.46]  about jim yeah um so i've taken uh over the project with uh another wonderful fella named doug elcorn he's
[3153.46 --> 3161.62]  at gaslight software in cincinnati um and i've only we've taken it over in name only uh we we haven't yet
[3161.62 --> 3165.10]  actually started digging into the code and starting to work through the backlog of issues
[3165.10 --> 3170.92]  um but it's funny because we started this process like five months ago and we only like got ruby
[3170.92 --> 3175.90]  gems access a few weeks ago and we're only able to announce it like last week and a big reason for that
[3175.90 --> 3182.98]  was uh a combination of of situational problems that are very common um i believe that like uh jim
[3182.98 --> 3188.50]  didn't specify this kind of stuff in a will right like like who's the executor of my open source
[3188.50 --> 3195.32]  cachet like who runs rake now right uh and as the world ages as like all this open source is around
[3195.32 --> 3199.46]  longer we're going to have to deal with this like literally like you need a living will for your open
[3199.46 --> 3205.06]  source you need to specify whose copyright it is if you die and who can maintain it because
[3205.06 --> 3209.68]  places like github that we have since learned will require stuff like that legally before they can just
[3209.68 --> 3217.32]  hand you a repository uh it's not enough that the guy passed away um uh a lot of other services are
[3217.32 --> 3222.50]  are you know very accommodating but uh you know maybe have a like less rigor about that kind of
[3222.50 --> 3226.62]  thing but then at the same time they're also operating on shoestring budgets and they just can't
[3226.62 --> 3232.04]  handle the the the volume of customer help requests that they have so like ruby gem specifically they
[3232.04 --> 3236.82]  don't have the funding to to spend a ton of time on support and so it took quite a while to get
[3236.82 --> 3243.16]  uh feedback from nick and evan about about how to move forward uh so so situationally that was
[3243.16 --> 3248.58]  that was painful um i think i think just structurally
[3248.58 --> 3256.78]  what i worry about is that we we just aren't geared for for
[3256.78 --> 3263.18]  sharing dependencies with other people sharing control with other people i guess the other half
[3263.18 --> 3267.56]  of the talk to get to give you sort of like we talked about the user responsibility the other
[3267.56 --> 3271.88]  half of the talk is like maintainers generally built their stuff to solve their own problem
[3271.88 --> 3278.74]  and when somebody else wants to help they're they're they're solving a slightly different
[3278.74 --> 3284.16]  problem they're solving a variation on the problem that the color is colored by their perspective
[3284.16 --> 3289.24]  and as a maintainer i don't want to cede control to that guy because he's going to like you know
[3289.24 --> 3293.40]  if he's really active he's going to kind of pull the project away from my center of gravity towards
[3293.40 --> 3297.72]  where he wants maybe it's how he codes things or maybe it's what it does and how it does what it
[3297.72 --> 3301.70]  does and so i think a lot of uh open source maintainers even though they're great people
[3301.70 --> 3307.38]  tend to be kind of control freaks because they've been burned you know however many times with pull
[3307.38 --> 3312.72]  requests that introduce bugs and then they have to maintain and so forth um but but i keep seeing all
[3312.72 --> 3318.28]  these projects that have literally one contributor on them uh and my goal is to try to discourage that
[3318.28 --> 3323.32]  in my own work uh and and try to pull in additional contributors and try to more actively solicit people
[3323.32 --> 3328.54]  for help not just because i'm i don't want to spend the time working on it constantly that would be
[3328.54 --> 3334.66]  great but because uh it is more stable the more people have access and control to things and have
[3334.66 --> 3341.42]  had eyes on it you know i've never read read rspec given 2.0's uh source code i was familiar with 1.0
[3341.42 --> 3347.36]  but 2.0 was a rewrite so i'm gonna have to go in basically with no help uh and totally figure it out
[3347.36 --> 3352.22]  soup to nuts and if i'd spent just a little bit of time pairing with jim and he had an open offer
[3352.22 --> 3358.78]  on the table for me to pair with him on it uh uh which i obviously regret not taking him up on
[3358.78 --> 3365.38]  uh now i'm totally on my own um to say nothing of how important you know his documentation is going
[3365.38 --> 3371.16]  to be to me which is another area a lot of open source fall short um so that project in particular i
[3371.16 --> 3375.90]  love it because it's just uh jim gave several talks on rspec given if you have any familiarity with
[3375.90 --> 3385.06]  rspec or with bdd style unit testing uh i think that given is a really really thematically honest
[3385.06 --> 3392.28]  conceptually pure way to write unit tests um and it has a lot of benefits that are just not obvious
[3392.28 --> 3396.80]  at first blush at first blush it looks like oh these are just aliases to give in and before each
[3396.80 --> 3401.74]  and so forth like that it's just more dsl kind of you know machinations but when you really dive in
[3401.74 --> 3407.34]  and you realize like the how the structure of the tests becomes much more clear and the uh the
[3407.34 --> 3413.54]  additional tools that it gives you with using less fewer keywords uh it's a fantastic tool and and i've
[3413.54 --> 3417.90]  got a port called jasmine given that does the same thing for jasmine which is why i've got the interest in
[3417.90 --> 3425.54]  maintaining both going forward um but anyway yeah i love the tool and and uh you know speaking on jim
[3425.54 --> 3433.42]  a little bit more broadly uh my goal is to be more like him in how i carry myself in the community
[3433.42 --> 3437.98]  and i i feel like a lot of people have said that after he passed away jeff casimir tweeted right after
[3437.98 --> 3444.24]  jim passed that um no matter who you were uh or or or what your idea was or what you had to say or
[3444.24 --> 3451.76]  whether jim had had had learned that thing that you learned a hundred years ago he treated you like
[3451.76 --> 3458.98]  you were fascinating and he uh uh got excited for your excitement and he just had so much joy in his
[3458.98 --> 3464.48]  heart that he couldn't wait to share with whoever was around him and he was so welcoming um that even
[3464.48 --> 3469.80]  when you know he was a well-rounded guy i mean he got mad at stuff i think one time he said that you
[3469.80 --> 3477.86]  you've never really understood a dependency until you've come to hate it um he he he could be biting
[3477.86 --> 3485.12]  like i i this is several years old now but like when he gave me criticism about about uh code that
[3485.12 --> 3491.54]  i wrote or how i wrote it uh you know i wanted just like you know you know that that uh uh that image
[3491.54 --> 3496.72]  where it's like you know lie down and ball try not to cry cry uncontrollably like i like it's really
[3496.72 --> 3507.60]  uh hit my ego hard but the reason he he was uh uh so so so i guess why it hurt me so much
[3507.60 --> 3513.46]  was because it's so true and his his feedback was so crisp and so grounded in just so much expertise
[3513.46 --> 3517.66]  and so much wisdom that he he'd you know he didn't get that wisdom because he was older and he'd been
[3517.66 --> 3521.72]  programming a long time he got that wisdom because he was incredibly thoughtful and introspective
[3521.72 --> 3527.94]  and careful and he managed to have both that aspect which i which uh you know i try to pride
[3527.94 --> 3534.04]  myself on but also this ability to very gracefully meet people where they are and get inside of their
[3534.04 --> 3540.56]  heads and um that's something that that i think that all of us could you know do a better job with
[3540.56 --> 3545.08]  and it just makes me really sad we're not going to be running into him at all the conferences
[3545.08 --> 3553.92]  throughout ohio from now on yeah absolutely man uh speaking of jim the ruby rogues did a a great
[3553.92 --> 3557.64]  tribute episode i don't know if you heard that or not episode 151 look it up while you're talking there
[3557.64 --> 3562.72]  uh the ruby rogues talk about jim and all the impact he had on them he had such a dramatic impact on
[3562.72 --> 3567.36]  so many it's just amazing how many people even though it's a small community that he specifically
[3567.36 --> 3574.84]  touched a huge loss to the ruby community well justin i think that's a good place to wrap
[3574.84 --> 3579.28]  appreciate you coming on we're excited about lyman and what you're doing there i've used it a little
[3579.28 --> 3584.72]  bit i'm excited to use it on some more projects and uh thanks for coming on and talking to us right
[3584.72 --> 3589.18]  on thank you guys i really appreciate being here and if anyone has any questions at all feel free to
[3589.18 --> 3594.30]  reach out to me on twitter or i'm justin at testdouble.com and specifically with lyman like
[3594.30 --> 3598.74]  we don't have an irc or anything so if you have a question or something's confusing just open a github
[3598.74 --> 3603.16]  issue it's not just about this code doesn't work we just want to have the conversation uh in in one
[3603.16 --> 3609.38]  place and help help everyone out awesome well we'll be back next week and let's all say goodbye
[3609.38 --> 3612.18]  bye so long
[3612.18 --> 3627.78]  like
[3627.78 --> 3630.88]  you
[3630.88 --> 3632.88]  you
[3632.88 --> 3662.86]  Thank you.
