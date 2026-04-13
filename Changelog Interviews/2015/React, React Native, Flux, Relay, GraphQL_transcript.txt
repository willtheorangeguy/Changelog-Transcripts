[0.00 --> 16.10]  welcome back everyone this is the change log and i'm your host adam stekowiak this is episode 149
[16.10 --> 23.04]  and on today's show we have some awesome guests from facebook christopher chadeau and spencer
[23.04 --> 29.46]  aarons both software engineers at facebook on the react team got some great announcements today too
[29.46 --> 35.96]  as well we talked about react react native especially react native going open source the
[35.96 --> 42.90]  announcement came yesterday at facebook's annual conference for developers f8 as it's known we also
[42.90 --> 48.82]  talked about flux relay and graphql in depth great conversations with those guys from facebook
[48.82 --> 55.94]  we also had some awesome sponsors for the show code ship top towel and digital ocean we'll tell
[55.94 --> 60.50]  a bit more about top town digital ocean but our friends at code ship specifically someone who's
[60.50 --> 67.46]  super impressed with code ship and how it helps them ship faster is a cto at product hunt and i quote
[67.46 --> 74.52]  at product hunt we use code ship as the backbone of our team's test and deployment processes and
[74.52 --> 78.48]  andreas has lots of great things to say about code ship and the way they help them perform but
[78.48 --> 84.14]  specifically they're using parallel ci a brand new feature that helps them deploy 10 times faster
[84.14 --> 89.76]  and if you want you and your team to ship faster you have to run your builds in parallel with
[89.76 --> 94.94]  parallel ci you can now split up your test commands in up to 10 test pipelines this lets you run your
[94.94 --> 100.82]  test suite in parallel and drastically reduce the time it takes to run your builds they integrate with
[100.82 --> 106.82]  github and bitbucket of course you can deploy to cloud services like roku aws and many more and you
[106.82 --> 111.60]  can get started today for free with their plan that gives you 100 builds a month and five private
[111.60 --> 117.26]  projects completely for free or you can use our offer code when you upgrade and that code is the
[117.26 --> 122.80]  changelog podcast and that's going to get you 20 off any plan you choose for three months so head to
[122.80 --> 127.36]  codeship.com slash the changelog to get started and now on to the show
[127.36 --> 135.24]  hey everybody we're back we got uh the folks from facebook here talking about react js
[135.24 --> 142.60]  a lot of other fun stuff that's coming out of react js react native flux relay graph ql a lot of fun
[142.60 --> 146.62]  stuff christopher you're here uh and spencer you're here welcome to the show my friends
[146.62 --> 152.06]  glad to be here yeah same way yeah and jared we also got you on the call as well we can't forget
[152.06 --> 156.86]  you man you're such an awesome man no way we would never forget jared i'm excited to be here i'm
[156.86 --> 162.38]  excited to hear about react so we've been planning this call i think behind the scenes for a better part
[162.38 --> 168.16]  of a month and a half just trying to pin down the best time to get you guys on the show to talk about
[168.16 --> 174.48]  what you're doing with react js can can we kind of intro each of you sort of talk about the react team
[174.48 --> 179.00]  and then we'll go into more of an introduction of what like react is and then go into the rest of the
[179.00 --> 187.12]  story yeah so my name is christopher and i heard about react about a year before it was open sourced
[187.12 --> 193.46]  and this was jordan who showed me a prototype of like some crazy functional
[193.46 --> 202.36]  libraries that he was working on and this his whole idea was to we're going to re-render the entire
[202.36 --> 209.88]  app on every single update and this sounded like crazy inefficient and everything but i realized that
[209.88 --> 216.86]  if this was efficient then it will solve like so many problems with uh so many bugs that we have
[216.86 --> 223.60]  with apps and that are all related to updates and so i didn't think about uh of it like for two weeks
[223.60 --> 228.48]  and then i was like oh maybe i should try it and i tried it and even if it was like super alpha
[228.48 --> 237.18]  it was extremely fast like faster than uh my manual manipulation i could write and i was like hooked
[237.18 --> 245.18]  that day and so for basically like a year i convinced like my entire team and like all the org to use react
[245.18 --> 251.74]  and i helped on the open source uh effort and this is how i got involved and spencer how about yourself
[251.74 --> 258.64]  uh so i definitely came from a different perspective um so i was actually uh managing the
[258.64 --> 266.66]  um facebook newsfeed teams on ios and android at the time and we were struggling with dealing with this
[266.66 --> 273.58]  massive app with hundreds of contributors and um our compile times had gotten astronomical and it was
[273.58 --> 280.42]  it was very slow to uh to iterate on the app and fix bugs and move things forward um and then i found out
[280.42 --> 286.76]  from um some of these guys that had been hacking on this new react native thing uh after react js was
[286.76 --> 293.14]  pretty um pretty you know getting pretty mature internally uh and it was it was very impressive they had this
[293.14 --> 298.80]  like ultra fast reload um so you could just change your product code and reload it right away and all this
[298.80 --> 305.04]  kind of good stuff and i was like oh man we need this so i switched from management back to uh coding
[305.04 --> 311.84]  uh as an engineer and joined the project full-time to try and make it a reality uh internally and uh
[311.84 --> 314.72]  eventually uh for the community um as open source
[314.72 --> 319.94]  awesome so maybe step back a second let's talk about react itself and
[319.94 --> 326.16]  what it is we've been tracking it on the changelog for some time and you can't ignore the groundswell of
[326.16 --> 331.52]  excitement around certain projects this is one that's just been slowly building steam and uh
[331.52 --> 337.08]  everybody is is quite excited about so uh why don't y'all take this one uh what is it exactly and then
[337.08 --> 344.36]  why are people so excited about it yeah so what it is it's a library to build user interfaces
[344.36 --> 352.46]  and this is a big world and this is not a framework or anything but this is a way for you to build
[352.46 --> 359.92]  to write uh user interfaces and for user interfaces it's basically like the dome so divs and spans and
[359.92 --> 367.06]  like events and the way you write this is the first big fundamental pillar is it's in javascript
[367.06 --> 373.14]  there is no templating language like you don't have to use strings like this is pure javascript and you
[373.14 --> 378.90]  use javascript to create objects that are going to be rendered and one of the big twists
[378.90 --> 385.64]  is that you don't have an update function so usually when you build your interfaces you first
[385.64 --> 390.86]  render everything and then you have to hook up all the events and when something changes you got to
[390.86 --> 398.64]  find the right element and then modify it and the really magical aspect of react is
[398.64 --> 406.26]  you're going to re-render like all the time and inside of react is going to do a diff between the
[406.26 --> 411.38]  previous version you re-rendered and the next version you rendered and it's only going to apply
[411.38 --> 419.38]  like those small mutations and the great thing is that because it's so focused on only doing this
[419.38 --> 425.98]  then you can integrate it like everywhere on top of like any platform so for example at facebook we had
[425.98 --> 431.76]  like many different libraries and framework and ways to access data and we're able to plug react like
[431.76 --> 437.44]  everywhere and in open source like this is the same and the great thing is this is not only about
[437.44 --> 445.08]  the browser about the dom it's abstract enough to render any tree and so we used it to render ios tree
[445.08 --> 453.12]  and android tree with react native so this is like the two minutes intro of react yeah a lot of things
[453.12 --> 458.38]  that come out of this uh virtual dom server side rendering descriptive warnings custom event systems
[458.38 --> 463.76]  things like that are what sort of people clamor to this came out of the ad org and really has done
[463.76 --> 469.52]  a lot for the business itself one of the things was predictability and being confident with change
[469.52 --> 473.50]  can you talk a little bit about the predictability that came from this and how that's helped engineers
[473.50 --> 480.72]  be more more efficient and being able to have confident changes one of the great success stories of react
[480.72 --> 487.60]  was an early one um which was that the um the ads product uh interface where um like small business
[487.60 --> 493.58]  owners and stuff would go to the website to to place ads and manage their campaign and stuff um was an
[493.58 --> 498.34]  extremely complex web application um and there's tons of different features and all sorts of stuff you
[498.34 --> 505.64]  can do um and it had turned into this giant labyrinth um that was extremely difficult to change without
[505.64 --> 512.00]  causing some sort of side effect bug um somewhere else in the in the application um because of this
[512.00 --> 516.74]  kind of imperative style of like going in and manipulating different parts of the dom and having
[516.74 --> 522.90]  to update a whole bunch of cascading bits of state here and there um because you just changed one one bit
[522.90 --> 531.00]  and so when the when the team um basically rebuilt it in react um they found that their uh rate of new
[531.00 --> 537.26]  bugs being introduced um had gone through the floor so there was very few bugs um coming into the system
[537.26 --> 543.60]  in the first place and then also when um when a bug did come in um it was much easier to figure out
[543.60 --> 548.88]  what was going wrong and make a targeted fix um really quickly um so bugs were resolved very quickly
[548.88 --> 554.84]  and with without a lot of frustration uh and then even went to the point that um new people uh coming
[554.84 --> 560.34]  into the company very fresh maybe straight out of uh college uh actually felt comfortable in the code
[560.34 --> 565.22]  base because they could understand what was going on because this declarative nature and um
[565.22 --> 570.14]  componentization of the code um they could say like oh this is clearly what's going to happen if i make
[570.14 --> 575.22]  this change and they didn't have to you know have years of experience with like the whole labyrinthine
[575.22 --> 579.86]  system in order to feel like they're not going to break something by jumping into the code and adding a
[579.86 --> 586.32]  feature fixing a bug or something like that um so that helped the team grow and move a lot faster and
[586.32 --> 593.18]  make a much more stable uh product that um our advertisers really appreciated that makes a lot
[593.18 --> 599.48]  of sense from an approachability standpoint for developers i'm curious how designers take to it
[599.48 --> 605.18]  people who are used used to only working with html and css because as you said it's all javascript
[605.18 --> 609.76]  components seem to break out really nicely so in that regard i think it would be more approachable
[609.76 --> 616.98]  perhaps than other systems but um how do you work a designer into the flow of you know working with
[616.98 --> 623.28]  react yeah so one of the interesting thing about facebook is uh designers do not contribute to the
[623.28 --> 629.80]  code base so designers do like mugs and like use like quartz composer to do like really nice interaction
[629.80 --> 636.26]  interactivities but they don't actually like go in the code base and change things so this has not been
[636.26 --> 644.88]  an issue like at facebook but okay uh instagram we which we acquired uh a few years ago on the other
[644.88 --> 653.16]  side like the designers do change color regularly and like if you look at uh gsx and the component
[653.16 --> 660.94]  system like this looks familiar enough to be uh like html so they were basically able to like jump in and
[660.94 --> 667.52]  like make design changes like really easily and also one of the things i think we should talk about is
[667.52 --> 675.20]  like designer are not like inferior people that cannot uh like code sure like there's this notion
[675.20 --> 680.30]  that designer like if it's javascript like this is the end of the world they cannot like do anything
[680.30 --> 688.02]  and this is not true like i would say like the previous environment of like developing environment was too hard
[688.02 --> 693.90]  so you had to like spend a lot of time being trained to like write javascript and what we've
[693.90 --> 700.66]  tried to do is react is to make it as simple as possible and this is not like trying to do the lowest
[700.66 --> 708.18]  like uh trying to appeal like the masses but this is to try to make a really good engineer even more
[708.18 --> 714.82]  efficient and using this approach we found that it was making like the library a lot more approachable
[714.82 --> 719.86]  and designer like didn't need to like weeks of training to be able to jump in the code base and
[719.86 --> 727.20]  change it that makes sense uh you mentioned jsx can you unpack that for us so jsx is a syntax extension
[727.20 --> 735.62]  for javascript that instead of doing function calls to uh render your application you use uh brackets
[735.62 --> 744.70]  angle brackets uh that looks like html so the origin of jsx is back in the days in php uh
[744.70 --> 752.94]  version of facebook uh we had a big security issue so we used to use string concatenation in order to
[752.94 --> 758.90]  build the interface and as you know when you concatenate strings uh it's super easy to introduce
[758.90 --> 766.66]  xss vulnerabilities vulnerabilities we're basically just echoing out the strings yeah and like we we
[766.66 --> 771.82]  couldn't solve this problem and like someone from the security team uh came up with this syntax
[771.82 --> 780.62]  extension from php so instead of um using string literals to like write html he augmented the syntax of
[780.62 --> 787.42]  php to write angle brackets and like being able to add attributes and the interesting thing about this
[787.42 --> 795.82]  is now because it's inside of the syntax of the language we know everything which is syntax is html and
[795.82 --> 804.86]  needs uh needs uh to be rendered as is but everything else needs to be escaped and so it solved all of
[804.86 --> 811.66]  the issues all of the like excesses vulnerability issues that were on the website and so this was a big
[811.66 --> 819.34]  win for security but it turned out that now that you have like this uh php object to uh render those
[819.34 --> 825.90]  elements now we are able to like write custom tags custom elements and so this is how we started with
[825.90 --> 834.70]  all the component effort and now we're using like uh components and to render like the php part part of
[834.70 --> 842.22]  facebook uh like the entire facebook app and now and afterward we ported it to javascript which is jsx and
[842.22 --> 850.14]  react is jsx an optional uh component or is it a required piece of react yeah it's optional um it
[850.14 --> 854.46]  actually there's just a static transform that translates it into the actual function calls
[854.46 --> 859.58]  it's making behind the scenes and so you can just call those directly if you want um and skip the jsx
[860.38 --> 864.78]  okay so there's a build step is that part of some tooling that you guys have released as well or
[864.78 --> 872.70]  yep there's a jsx binary that adds a transform step to do it and the interesting thing is because
[872.70 --> 879.74]  this is not uh required then other languages that compile to js for example closure scripts
[879.74 --> 883.98]  or coffee scripts that are able to use react but without the jsx part
[886.54 --> 893.02]  and since react is really just a view layer i've i haven't tried it myself but you seems like you can
[893.02 --> 897.66]  fit in with with many other toolkits like an angular or an ember if you are so inclined is that
[897.66 --> 902.54]  fair to say yeah you can definitely mix and match and um because also react components are
[902.54 --> 907.50]  componentized you can kind of stick them into the tree wherever you want so that's how it initially got
[907.50 --> 911.66]  adopted at facebook um is that we had all this other crazy stuff going on but you could be like
[911.66 --> 915.50]  oh i want to try this react thing and you could just reimplement one little widget on your page
[915.50 --> 921.74]  uh and they would they would play nice together yeah that was the initial implementation of react
[921.74 --> 928.30]  and facebook was the comments feed right uh yes yeah so you can just pick a piece of the page and
[928.30 --> 933.50]  shove it in there and kind of is isolated that makes it really easy to pick it up and give it a shot
[933.50 --> 939.50]  without having to go whole hog into it yeah definitely and also like it's a two level so you can embed
[939.50 --> 946.86]  it anywhere you want but inside of react you can also uh make a component that is uh just a jquery
[946.86 --> 954.54]  a plugin or like some arbitrary note so you can like plug it in uh you can have your custom uh code
[954.54 --> 960.22]  base on top of react and below react as well awesome well i want to ask you about react native
[960.22 --> 964.54]  we're pretty excited about it but let's pause first uh hear a word from a sponsor and when we get back
[964.54 --> 971.90]  we'll talk about react native i want to share a more personal note today with you about our awesome
[971.90 --> 976.86]  sponsor top towel you've heard us talk about top towel several times for long time listeners you
[976.86 --> 981.58]  know that top towel has been supporting the show for the better part of a year to a year and a half
[981.58 --> 987.66]  now uh if you want to go to their website while i'm talking here it's t-o-p-t-a-l.com it's one of the
[987.66 --> 992.94]  best places to work as a freelance software developer uh we've been working with top towel like i said for
[992.94 --> 998.14]  about a year year and a half now and over this year and a half i've gotten to know their co-founder
[998.14 --> 1002.86]  brendan very very well i love what they're doing for the software development community they care
[1002.86 --> 1008.30]  deeply about software developers having awesome engagements to work on and they also care about
[1008.30 --> 1013.50]  awesome engagements having really awesome software engineers to work with them so they really make
[1013.50 --> 1018.62]  the marriage between a business with great opportunities and an engineer needing great
[1018.62 --> 1023.34]  opportunities to work on they make that marriage possible well we took our relationship to the next
[1023.34 --> 1027.50]  level and went there ourselves we're building something very cool behind the scenes here at the
[1027.50 --> 1031.98]  the change log to power the future of what we're becoming you're gonna love what we're doing we
[1031.98 --> 1036.86]  hired a software engineer through top towel his name's hafael so if you're a member and you're in
[1036.86 --> 1042.14]  the members of the slack room say hi to hafael he's in there but i wanted to tell you just how deeply
[1042.14 --> 1046.86]  we care about our relationship with top towel and how much we trust who they are and if you're
[1046.86 --> 1051.74]  freelancing right now as a software developer and you're looking for a way to work with top clients
[1051.74 --> 1057.34]  maybe even us on projects that are interesting to you challenging uh and using the technologies
[1057.34 --> 1063.42]  you want to use i will go as far to say that top towel is the place for you head to top
[1064.14 --> 1069.98]  tal.com slash developers that's top towel.com slash developers learn more and tell them the change
[1069.98 --> 1077.10]  lol sent you so you mentioned earlier that you have these components you have this declarative way of
[1077.10 --> 1081.66]  defining the components and you've kind of abstracted that away from the actual rendering
[1081.66 --> 1086.38]  and what falls out from that is the ability to render not just to the dom but to other
[1086.38 --> 1092.82]  view layers i think it was flipboard who came out with react canvas uh kind of to much applause and to
[1092.82 --> 1097.56]  some controversy around you know is the web technologies good enough for 60 frames per second
[1097.56 --> 1102.46]  uh which is always fun to talk about but you guys have taken that a step further they're
[1102.46 --> 1108.22]  rendering it a canvas and you guys at your conference in january i believe it was announced
[1108.22 --> 1113.74]  react native do you want to talk about that for us yeah so uh i mean the general concept is that you
[1113.74 --> 1121.18]  still just have a view hierarchy right it just happens to be like ui kit um like ui views or android views
[1121.74 --> 1130.70]  um or dom nodes um and the the same react principles react algorithms um they all apply to to each of them um and so
[1130.70 --> 1137.02]  basically there's a bridge layer that translates the javascript to the native platform uh and then
[1137.02 --> 1144.06]  you have kind of like a crud interface of you know create update and you know we just use that to add
[1144.06 --> 1150.22]  nodes um into the system modify them set properties delete them yeah and the rest is um you know a bunch
[1150.22 --> 1156.54]  of the platform specific um native stuff to um make the system work but that's kind of the basic idea
[1156.54 --> 1162.38]  when uh when you came out with react native uh from what i understand it's getting the best part
[1162.38 --> 1166.54]  out of native but also getting the best part out of the web as well can you talk about that a bit
[1167.26 --> 1171.10]  yeah so one of the main things that was slowing us down on native i mean we could build you know
[1171.10 --> 1176.22]  beautiful apps that that performed really well and were really great but it was just a lot slower uh
[1176.22 --> 1181.34]  to develop and iterate a lot of this was because our build times had gotten really slow but you know
[1181.34 --> 1185.90]  just in general it's it's not the web where you can just rapidly prototype and reload the page and
[1185.90 --> 1191.34]  and all that kind of stuff yeah i mean we we look to um be able to to solve those simultaneously get
[1191.34 --> 1196.30]  the the performance and the the platform standardization of the native side but then
[1196.30 --> 1200.94]  also the ease of development on the website with being able to reload uh we also brought some other
[1200.94 --> 1209.42]  abstractions including uh layout system uh and styling so now you can um write something similar to css
[1209.42 --> 1214.86]  uh that's actually pure javascript to style your nodes uh similar to like style sheets uh and you can use
[1214.86 --> 1221.34]  use the flex box um layout algorithms to lay out your nodes so now instead of the the standard
[1221.34 --> 1227.82]  like especially on ios of you know actually doing a bunch of algebra or arithmetic to calculate how
[1227.82 --> 1232.70]  the views should be laid out on the screen um you can just say like you know flex direction row or
[1232.70 --> 1239.18]  column and they'll automatically like stack up um they'll stretch to fill their parent or wrap text and
[1239.18 --> 1243.66]  all these kind of things um that you're used to on the web um which also takes a lot of the burden out
[1243.66 --> 1251.42]  of the kind of traditional um native development so it sounds like it's maybe yet another pre-processor so
[1251.42 --> 1257.50]  is that what you're talking about when it comes to an alternate way of doing style sheets the way react
[1257.50 --> 1265.50]  works is the only interface with a dome is uh three operations one which is a create a dome node and
[1265.50 --> 1272.46]  attach it somewhere in the dome the second one is update this dom node and the third one is uh delete
[1272.46 --> 1280.62]  remove the the dom node and in uh before that there's all the react diff algorithm that outputs those three
[1280.62 --> 1286.86]  things and so we are still using javascript and we're still using react and all of this but we
[1286.86 --> 1294.46]  re-implemented those three operations instead of doing it for the dome we send them from javascript to
[1294.46 --> 1300.62]  objective c and in objective c we create a view we modify the view and we remove the view that
[1300.62 --> 1306.62]  makes sense totally makes sense so hmm so you're not running a web view inside of a native app it's
[1306.62 --> 1313.50]  not like a wrapper it's actually just real native rendering native components and so what's so the goal
[1313.50 --> 1319.18]  i'm trying to i'm trying to i'm trying to understand the big win is it just that you can use the web
[1319.18 --> 1324.86]  technologies which you know and love or is it cross-platform or what's what's the biggest win
[1326.38 --> 1332.46]  so jordan who created react and was at the beginning of react native is obsessed with performance and
[1333.58 --> 1341.34]  for like months he tried to get a 60 fps list like infinite scrolling list like newsfeed on the web and
[1341.34 --> 1351.10]  he couldn't get it to work as uh fast fast enough and so uh what he tried is it took the react native
[1351.10 --> 1358.30]  like our very early experiments and used the exact same code but instead of rendering uh divs and spans
[1358.30 --> 1367.10]  and images uh he rendered uiview ui image and uilevel and without changing anything it got 60 fps without
[1367.10 --> 1374.38]  even trying and so this is how like the project really really started we had a confirmation that
[1374.38 --> 1381.90]  the browser is not like fast enough uh this is like how it started and then we were able to get a lot of
[1381.90 --> 1389.98]  wins because it turns out that all of the native ui components from ios are extremely well designed and
[1389.98 --> 1398.22]  well-made and like all the gestures are right and are very high quality and while it's theoretically
[1398.22 --> 1405.82]  possible to implement zoos uh on the web like i've never seen anyone uh do it as well as the native
[1405.82 --> 1415.66]  counterparts and so by being able to reuse them by default uh this is a big win for the project and it's also
[1415.66 --> 1423.98]  uh it's also interesting because i would say it's a broken glass effect so because like all of the
[1423.98 --> 1430.14]  core components are so high quality and so well made like the ios community are extreme is extremely like
[1430.78 --> 1435.10]  careful about making like really well designed interactions and things like this but if you look
[1435.10 --> 1443.50]  at the web because there's no such example like it's okay to ship like inferior quality app and we've
[1443.50 --> 1449.26]  seen this like even at facebook like on the website like we could make it a lot better but we haven't
[1449.26 --> 1455.26]  done so because like we were not pushed far enough by the platform and the like mentality and the ecosystem
[1456.38 --> 1461.18]  but you're saying the web has some broken windows yeah and so we're all just kind of adjusting to fit
[1461.18 --> 1468.46]  that ecosystem yeah i should also ask that resonates a little bit you also asked about the cross-platform
[1468.46 --> 1473.26]  nature um yes yeah so one of the one of the big advantages we've seen is that um
[1473.26 --> 1479.66]  now there's one unified development experience um independent of what platform you're running on so
[1479.66 --> 1485.66]  you learn javascript you learn react and you learn some of these like style sheet concepts and abstractions
[1485.66 --> 1490.70]  and that travels with you to whatever platform you're working on of course the platforms also
[1490.70 --> 1497.18]  have a lot of platform specific idioms right so the actual design and the way the app like looks and
[1497.18 --> 1502.70]  feels and the way navigation works and those kind of things are unique um but now the actual code that
[1502.70 --> 1507.50]  you're writing and the way you're working and the tools that you're using uh are much more consistent
[1507.50 --> 1514.46]  and so you can have um the same developers more easily moving between platforms uh as they build out
[1514.46 --> 1521.18]  a similar experience on on multiple um devices or operating systems or what have you um we also have
[1521.18 --> 1527.42]  the flexibility that we can reshare whichever code we'd like to it very rarely makes sense to share all of
[1527.42 --> 1534.14]  the code um but like the lower levels of application logic like business logic is usually the same uh
[1534.14 --> 1539.42]  and it's decoupled from the view layer right um and so that code can all just be shared across the
[1539.42 --> 1546.14]  applications and then you can decide you know where in the stack you want to re-implement um the the
[1546.14 --> 1552.06]  presentation uh and so we've actually been able to move around pretty quickly across platforms without
[1552.06 --> 1558.54]  spinning up um more specialized people um that you know know the intricacies of the the android runtime
[1558.54 --> 1564.78]  and all that kind of stuff yeah and also i want to add something on this which is if like people
[1564.78 --> 1571.02]  like i was on the photos team and we had one big issue which which was that uh developers on ios could
[1571.02 --> 1578.06]  not uh write anything on android could not write anything on the web so we had whenever we wanted to do
[1578.06 --> 1583.50]  uh like a new feature we had to staff three different people to work on the exact same thing
[1584.30 --> 1592.54]  and the issue with this is now it makes like silos so now like there's ios engineers that are thinking
[1592.54 --> 1598.22]  about ios and like this mentality and they don't talk to android engineers and they don't talk to web
[1598.22 --> 1606.46]  engineers and so not only it takes three times the amount of energy to build features but you also like
[1606.46 --> 1613.58]  get a lot less communication between zoos and like they get a further apart and this is not good because
[1614.22 --> 1621.26]  now it's you're you're putting people at war between each other like now instead of like having everyone
[1621.26 --> 1627.02]  wanted to like build the best product now oh you're going to compare between ios and android i'm the best
[1627.02 --> 1635.26]  or and also as a mentality effect if it's not really fun to implement the same thing as someone else
[1635.26 --> 1640.46]  because like you want to do like something unique and now like if you think it's best now you've got
[1640.46 --> 1647.66]  to convince the two other people that they also should do that and so like it causes like a lot of
[1647.66 --> 1654.14]  issues like people issues well then you gotta you can't just yeah you have to have so many people to
[1654.14 --> 1659.50]  implement a single feature because simply because of platform differences you're not really trying to do
[1659.50 --> 1663.82]  a right once you know run everywhere kind of situation which is what tom said in his keynote
[1664.38 --> 1669.42]  you're really trying to do everyone understands how to use react and react can work everywhere so
[1669.42 --> 1674.70]  it's not like right once put it everywhere it's more like learn it once and then do it everywhere write
[1674.70 --> 1682.06]  it everywhere yeah yeah which really yeah sorry i should say it really breaks down knowledge silos inside
[1682.06 --> 1688.30]  of an organization and brings all the engineers that seems really great too for team building too right
[1688.30 --> 1692.46]  because you've got really smart people on three different sides of the fence basically they're in
[1692.46 --> 1697.50]  their own silos and can't really mesh together get lunch together talk through features together and
[1697.50 --> 1702.14]  really even take it above and beyond the bar that you're already going to because they're in their
[1702.14 --> 1708.38]  they're in their silos and sort of camping on their own areas yeah and those experts also tend to be
[1708.38 --> 1715.26]  more fragmented themselves because now you're you're spreading the products across more people because you have the
[1715.26 --> 1720.14]  platform specific verticals right and so now instead of having one engineer that knows how to build
[1720.14 --> 1724.94]  this product super well on all platforms you'll have three engineers that know how to build three
[1724.94 --> 1731.10]  different products each on their own platform right um and so now any individual engineer is
[1731.10 --> 1738.30]  fragmented across pms designers projects that kind of thing which is continuity better team building
[1738.30 --> 1743.18]  that's um that's that's definitely the way to go jared you got a question yeah i'm just now starting to
[1743.18 --> 1748.62]  think man like in a practical sense like using react native you're you i'm wanting to get my hands on
[1748.62 --> 1753.42]  it now because i'm thinking like how do you use this thing is it like are you chilling like if you're
[1753.42 --> 1758.70]  doing an ios app in react native are you chilling inside xcode are you are you just having some
[1758.70 --> 1764.86]  javascript files and you have some sort of build tool like how does it work so the way it works is most of
[1764.86 --> 1771.10]  it for the develop the random developer is going to be uh javascript so mostly going to write javascript
[1771.10 --> 1778.54]  and react and internally we use atom uh for debugging but a lot of people use sublime and i'm here
[1779.82 --> 1786.30]  i use sublime yeah and so this is like for the random developer but then what we really want is
[1787.34 --> 1793.74]  you can access every single feature of native that you want and the way we did it was to implement a
[1793.74 --> 1801.02]  plugin system that lets you write arbitrary objective c or java and this means that if for
[1801.02 --> 1808.62]  example apple ships a feature on apis that is not available yet for a new upgrade like you can you
[1808.62 --> 1814.06]  can like bridge it it's going to be a bit like verbose and complicated but like you can do it and also
[1814.06 --> 1820.86]  it's really useful for being able to run like really high performance things for example like image decoding
[1820.86 --> 1828.14]  while there is asm js and like this kind of thing like at this point like it adds a layer of
[1828.14 --> 1835.18]  indirection and you want to be able to use a real thing with threads and with malloc and like controlling
[1835.18 --> 1841.74]  like the very low level so but then like this is a use case for like more advanced so you're going to
[1841.74 --> 1847.90]  like do it less but this is really what makes it stand out from the web as it is right now yeah so you
[1847.90 --> 1852.94]  have that that full power of the plugin system to write whatever modules you want so you can just
[1852.94 --> 1858.94]  write you know random files that are you just have some js function you call it executes the native thing
[1858.94 --> 1864.86]  or you can actually wrap like view components so say you know you already have an app and you wrote
[1864.86 --> 1869.82]  some really cool widget that you you know don't want to just throw the code away you can actually just
[1869.82 --> 1874.14]  bridge it right into your react native app and make it available so you don't have to just throw all
[1874.14 --> 1879.50]  that out or if you know there's something about it that you need more closer access to like the native
[1879.50 --> 1886.46]  apis you can do that if you need but because it is this we made it as easy as possible to bridge in
[1886.46 --> 1891.74]  these these like new like plugins we're also hoping that the community can kind of expand that surface
[1891.74 --> 1897.26]  area really easily as well and we can kind of build like a community supported library of all sorts of
[1897.26 --> 1903.02]  neat like widgets and you know native capabilities and and things like that that are really easy to just kind of
[1903.02 --> 1907.42]  drop into your app well now that we got pretty much everybody excited about that let's let's get
[1907.42 --> 1912.86]  them excited about something else as well you've got some dates some dates coming up that are pretty
[1912.86 --> 1916.22]  important to you what what's going to happen on those days and what's so important to you
[1917.10 --> 1924.78]  yeah so yesterday we open sourced react native so as of today like you should be able to like just
[1924.78 --> 1931.74]  go on github and npm install and like start to use it that's now that's that's exciting so technically
[1931.74 --> 1937.50]  technically christopher you're speaking in the future to the past yes because we're recording
[1937.50 --> 1943.34]  this in the past but you're listening to this on a friday which is march 27th so on the march 26th
[1943.34 --> 1947.90]  facebook announced react native and it's open source well you announced it a while ago but it's open
[1947.90 --> 1953.34]  source now yeah you guys announced it back in january and here we are in march it seems like was
[1953.34 --> 1957.50]  there just some cleanup that had to be done some extraction that that you had to pull it out
[1957.50 --> 1964.54]  yeah so the story behind this is uh we organized the react js comp and we had no plan of like
[1965.10 --> 1969.90]  open sourcing react native and we were like we wanted to open source it at some point but
[1970.62 --> 1977.02]  like we were not ready and one month before the conference we were like this is like the best place
[1977.02 --> 1983.42]  to announce it like there's no better place and so like we were like like there's no way in one
[1983.42 --> 1989.18]  month we're going to be able to like make it open source ready so what we did was we're going to
[1989.18 --> 1994.54]  like clean up as much as possible and see the dates where we are and we were not ready so we were like
[1994.54 --> 2001.02]  okay we can we are ready enough for like people to trade but not everyone so we gave it gave access to
[2001.02 --> 2006.94]  attendees at the conference and then we're like okay we're going to run to work as fast as possible to
[2006.94 --> 2013.02]  make it ready and now we're able to get like something that we are proud of even if it's like super
[2013.02 --> 2018.94]  early like you can like start building up with this yeah everyone at the conference it was at react
[2018.94 --> 2025.74]  conf back in january got access to the github repo so you had a private it was already on github
[2025.74 --> 2033.10]  but you kind of gave access early to those attendees but yesterday uh march 26 you you actually open
[2033.10 --> 2039.26]  source it to the world that's correct and this was not a really good place and i don't recommend
[2039.26 --> 2044.22]  like doing the same thing because like this is like people were storming the gates weren't they
[2044.22 --> 2050.22]  yeah and this is like making so much hype and like yeah we really want like people to try it and see
[2050.22 --> 2055.02]  for themselves instead of like listening to us saying that this is the best thing in the world
[2055.02 --> 2061.02]  and this is what we've been trying to do is react is this is what we think but like please
[2061.02 --> 2065.26]  try it and make an opinion for yourself when you say try do you mean try it as in use it or try it as
[2065.26 --> 2068.94]  and like build something with it because obviously they couldn't build something with it but to try it
[2068.94 --> 2075.10]  they could use uh facebook groups was was your first as far as i can tell is your first usage
[2075.10 --> 2080.54]  internally of of react to building brand new or react native so i would say like yeah i would say
[2080.54 --> 2086.30]  both like try to develop something with it and if you're not convinced try the groups app or the ads
[2086.30 --> 2093.82]  manager app and one interesting thing about the groups app is it's half react native and it's half
[2093.82 --> 2100.22]  uh objective like just normal objectivity and what's interesting is try the app and see if you can
[2100.22 --> 2107.18]  detect which one is native and which one is react native and if you cannot find out the difference
[2107.18 --> 2112.78]  and it means that we've done a good job this means that we are able to write i can't tell the difference
[2112.78 --> 2118.70]  so you did a good job i use it i've been playing with the groups because um here in my neighborhood we
[2118.70 --> 2124.30]  actually have a facebook group that we use for our neighborhood and it's amazing you know it's it's
[2124.30 --> 2127.74]  good for getting to know your neighbor for one and just kind of keeping in touch with what's going on
[2127.74 --> 2132.06]  in the neighborhood but we're me and my wife are always on it just kind of keeping up with our
[2132.06 --> 2137.50]  neighbors and whatnot so that's one of the groups i use quite a bit on facebook so i was like that's a
[2137.50 --> 2141.98]  good thing i've been using it for a couple days now and really been enjoying the push notifications and
[2141.98 --> 2149.50]  i can't tell it's not that it's a half and half app at all well thanks that's the goal i think i think
[2149.50 --> 2155.34]  one of the reasons why people people got so excited is that you know this this is not an r d project i
[2155.34 --> 2160.06]  mean it started off as one a while back but uh one thing that i appreciate about what you guys do over
[2160.06 --> 2165.98]  there at facebook with your open source is you know you do wait and you do use it in production and
[2165.98 --> 2170.22]  you kind of you know the term is dog fooding of course we've heard that plenty of times but
[2170.22 --> 2174.30]  you're actually like you have production apps that use react native this is not like hey this might
[2174.30 --> 2177.90]  be a thing that works it's like nope this is really a thing that works and we're using it
[2177.90 --> 2181.98]  and so that makes the announcement so much more tangible and people want to get their hands on
[2181.98 --> 2187.50]  it because you can actually do production things with that today yeah that's super exciting we have
[2187.50 --> 2193.82]  a very firm commitment to our open source uh portfolio to only launch things that we really believe are
[2193.82 --> 2199.34]  very useful work well um at least for our internal use cases uh but also that we think will be
[2199.34 --> 2204.30]  useful to the community as well and so you know react native is one of those if we ended up not
[2204.30 --> 2207.74]  using it internally we wouldn't have open sourced it because you know there must have been something
[2208.38 --> 2215.90]  not quite there about it uh paper doesn't use react native does it no paper uses a another
[2215.90 --> 2221.18]  library that we did open source called async display kit uh and so that came before uh react
[2221.18 --> 2228.30]  native was um even a thing at all internally and actually react native is is starting to think of a lot
[2228.30 --> 2234.22]  of like similar optimizations that we can make inspired by the async display kit uh open source
[2234.22 --> 2238.78]  library for example one of the things that traditionally makes apps slow or drop frames or
[2238.78 --> 2244.46]  whatever is doing the layout synchronously on the ui thread and if you have a lot of complex layout to
[2244.46 --> 2249.82]  compute uh it can take longer than one frame and then you miss your frame deadline and drop a frame
[2250.46 --> 2257.26]  but async display kit did uh for paper is make it really easy to compute your layout on a separate
[2257.26 --> 2262.30]  thread uh and allocate nodes and and do all this kind of stuff uh in the background without blocking
[2262.30 --> 2267.50]  your ui thread uh and react native gives you a similar capability so we mentioned earlier that we
[2267.50 --> 2274.06]  have this flex box style uh layout paradigm um so you you know you write like flex box style rules and
[2274.06 --> 2280.46]  your styles and then the system computes the the layout like the frame positions and all that all of that
[2280.46 --> 2285.82]  layout calculation is also done on a background thread rather than on the main thread so even if your
[2285.82 --> 2290.14]  layout is very complex and it takes a few frames to compute we're not going to be blocking you know
[2290.14 --> 2295.26]  your scroll or whatever while that happens um so we have you know kind of a synergy between our
[2295.26 --> 2300.14]  different um different libraries even if they're not actually sharing any code um just based on their
[2300.14 --> 2309.34]  their time lineage so react native supports ios and android out of the box any other platforms that
[2309.34 --> 2315.18]  support or in the pipeline yeah so android hasn't shipped yet um we're working on an app now uh and
[2315.18 --> 2320.62]  it's not part of the open source yet um but we're we're working very hard to to ship that app and uh
[2320.62 --> 2326.78]  and get it into the the open source for the community so for the release the initial release is ios first
[2326.78 --> 2332.22]  then and later yeah yeah and this goes back to your question like to your remark that we only open
[2332.22 --> 2337.26]  sourcing that we use in production we don't have an android in production so it doesn't make sense yet
[2337.26 --> 2346.14]  to open source it and right now we don't have any other plans but we really designed the systems to be
[2346.14 --> 2353.26]  uh modular so it shouldn't be that hard like it's going to be a lot of work but like the system is
[2353.26 --> 2361.26]  designed to support like uh windows phone like 10 then or something like if you have like other platforms
[2361.26 --> 2369.26]  and we we see it with react react there's a react canvas uh back end there are some people that did
[2369.26 --> 2380.46]  uh react open gl uh back end some uh svg back end so like this is open ended especially you mentioned
[2380.46 --> 2386.14]  something there that's not kind of kind of had earmarked to talk about which was the the blocking
[2386.14 --> 2390.62]  portion of a garbage collection of javascript running that in the same the main thread and
[2390.62 --> 2397.02]  what that means for frame eight and jared you you mentioned earlier about um flipbook and react canvas
[2397.02 --> 2404.06]  and whatnot flipboard flipboard what did i say flipbook flipbook a little close yeah that's pretty
[2404.06 --> 2409.50]  close close enough i don't use flipboard so that's why it's a flipbook to me facebook flipbook you know
[2409.50 --> 2415.58]  we're all about the books around here uh my bad but you know talk about the non-blocking aspect
[2415.58 --> 2419.58]  on things like garbage collection and what that means for frame rate and what that means for
[2419.58 --> 2426.94]  the animations and transitions that that react native allow yeah so right now um like i said the layout and
[2426.94 --> 2431.10]  all that is done on a background thread but all the javascript is also executed on a background thread
[2431.10 --> 2437.66]  uh so the way the system is architected is that everything um goes across a serializable
[2437.66 --> 2443.42]  asynchronous bridge uh between the the native runtime and the the javascript engine so this means
[2443.42 --> 2449.66]  we're we're not doing any um like custom uh like synchronous hooks um it's literally just serializing
[2449.66 --> 2454.86]  the commands um into json and passing those back and forth uh so that means the js can take as long
[2454.86 --> 2462.30]  as it needs to to compute um a batch uh and the the interface is free to you know scroll and respond
[2462.30 --> 2468.14]  while that's happening um obviously if you have critical things with react with uh js in the loop
[2468.14 --> 2474.38]  you know then it it can get stalled um and right now we've done a lot to make sure that's not the case
[2474.38 --> 2479.10]  um but we'd like to actually lift that restriction and potentially introduce some uh multi-threaded
[2479.10 --> 2485.02]  javascript architectures and um some other optimizations there so that we can make it a little bit easier to
[2485.02 --> 2491.82]  run critical sections uh in your javascript um yeah and also you mentioned uh garbage prediction
[2491.82 --> 2496.70]  and we were super afraid at the beginning that oh we're using javascript we're going to be hit by
[2496.70 --> 2501.66]  the garbage collector but it turns out this has never been an issue so far like we've never
[2502.54 --> 2508.38]  dropped a frame because of it and one of the reasons is we're using javascript core and it has a
[2509.10 --> 2516.38]  multi-threaded garbage collector and it's concurrent so that your javascript can run and the garbage
[2516.38 --> 2521.58]  collection is going to run at the same time it's not going to block except for the sweep phase but
[2521.58 --> 2530.30]  the sweep phase is chunked and has a deadline limit so in practice this hasn't been an issue
[2530.94 --> 2537.34]  that's that's um good to mention that because the show just before this episode 148 um jerry
[2537.34 --> 2542.54]  wasn't on the call but i had a call on on the topic of go with andrew jaron and one of the things they're
[2542.54 --> 2550.30]  doing with go is uh is opening up to be able going to mobile more or less ios and android support and one
[2550.30 --> 2555.10]  of the things we talked about was the concurrency and go and garbage collection and and the importance
[2555.10 --> 2560.62]  of that and how that sort of pauses the application or pauses that thread and even for a few milliseconds
[2560.62 --> 2565.50]  of 10 milliseconds and then that provides that that pause that sort of drops your frame rate next thing
[2565.50 --> 2569.74]  you know your transitions aren't the way they should be your animations get blocked and you have sort of
[2569.74 --> 2576.94]  a kludgy ui and a kludgy ux so that's a pretty important feature there we're gonna take a quick break
[2576.94 --> 2582.70]  come back and talk about flux relay and graph ql some highly important topics that are pretty
[2582.70 --> 2589.82]  fun to talk about so we'll be back in just a sec over 400 000 developers have deployed to digital
[2589.82 --> 2596.70]  oceans cloud digital ocean is a simple cloud hosting provider built for developers in 55 seconds that's
[2596.70 --> 2601.82]  all the time it takes you'll have a cloud server with forward access and it just doesn't get any easier
[2601.82 --> 2607.82]  than that pricing plans are super inexpensive just five bucks a month for half a gram 20 gigs of ssd
[2607.82 --> 2614.54]  drive space one cpu core and one terabyte of transfer all digital ocean servers run on ssds that
[2614.54 --> 2619.98]  means they're blazing fast they have tier one bandwidth support and come with private networking use our
[2619.98 --> 2624.70]  special link to get a ten dollar hosting credit when you sign up head to the changelog.com
[2624.70 --> 2633.50]  slash digital ocean to get started and now back to the show all right we're back flux relay graph ql where
[2633.50 --> 2642.94]  should we begin with with these three topics here maybe with flux so the history of flux is uh the team
[2642.94 --> 2650.94]  that was working on the message on chat uh they had one big issue which was updates were out of sync
[2650.94 --> 2658.30]  so for example uh you had a notification uh chat notification someone sent a message and you you
[2658.30 --> 2664.78]  need to like update the the chat tab at the bottom right of the screen and the buddy list at the right
[2664.78 --> 2672.54]  of the screen and the notification icon and like many other places in the ui and the way it was organized
[2672.54 --> 2678.70]  before it anytime there was an update you needed like manually in the code to go to all of those places
[2678.70 --> 2687.82]  and and modify the dump notes and this was horrible because uh things were getting out of sync and all
[2687.82 --> 2693.74]  the time and it was super hard to know why and to traverse the issues and so the idea that they had is
[2694.38 --> 2701.18]  we're going to have a centralized place where we're going to have all our data and we're going to use
[2701.18 --> 2707.66]  something called a one-way data flow so instead of having like the model that talks to the views that talks to
[2707.66 --> 2714.86]  the model that talks to uh to the controller and like in all those places there's going to be only one
[2714.86 --> 2721.82]  way to do it when the view there's an event on the view that changes they're going to send an action to
[2721.82 --> 2729.18]  the model and the model is going to call the view again and like only it only goes in this one direction
[2729.90 --> 2736.30]  and it's all like all of the issue but what it meant is that they had to re-render the entire thing like
[2736.30 --> 2743.90]  basically all the time and in parallel there was this react library that we was working on at facebook
[2743.90 --> 2748.38]  which was like we're going to re-render everything all the time and it's going to be fast enough
[2748.94 --> 2756.30]  and the two like actually converge so and they were a good fit together so you can use like the one-way
[2756.30 --> 2761.82]  data flow architecture of flux with react render and they work like really well together
[2761.82 --> 2770.14]  so flux was uh it's kind of an would you consider it an architecture or an implement yeah it's not a
[2770.14 --> 2776.06]  specific tool it's a way of going about things similar to how model view controller would be a way of
[2776.94 --> 2783.26]  organizing your application that being said you guys you know flux is the thing that you guys do with
[2783.26 --> 2790.14]  your uh web apps and your react apps and so you and you provided flux as kind of a was there a
[2790.14 --> 2795.74]  specification or just a some documentation on how a flux application will work and then you guys had
[2795.74 --> 2804.62]  your own implementation yeah so we have a website uh facebook.github.io slash flux and we have only one
[2804.62 --> 2811.74]  part of like source code which is a dispatcher and then the rest is like documentation of how we design
[2811.74 --> 2819.34]  the system internally but like this is like create actions and mutations like this and like it's basically
[2819.34 --> 2825.10]  like a way for you to architect your app but like there's no specific code but is that because it's
[2825.10 --> 2831.02]  so application specific the way you end up going about it yeah like there's no like stores they're
[2831.02 --> 2839.26]  just uh javascript objects and actions are just a json payload so like there's not that much code but
[2839.26 --> 2844.54]  there's a lot of uh flux libraries that try to implement the flux pattern we will give like
[2844.54 --> 2852.62]  more concrete things so you may want to start with them if you want yeah there's a whole list of them
[2852.62 --> 2859.26]  yahoo has one the best thing about these is the names that came out of it so you got flux you got reflux
[2859.26 --> 2869.50]  flummox marty.js of course uh mcfly material flux you got a whole ecosystem of flux uh implementations and
[2869.50 --> 2875.58]  in fact i think we even covered in weekly a flux comparison which is a repo on github if you search
[2875.58 --> 2880.78]  flux dash comparison a guy who basically went and implemented the same app uh across all these
[2880.78 --> 2888.54]  different fluxes so yeah vibrant vibrant ecosystem of flux isn't there not yeah one of the interesting
[2888.54 --> 2896.22]  thing is so when we open source react like we uh we just said like oh we're using like this internally
[2896.22 --> 2902.38]  like flux and we on irc we were talking about it but like we didn't care that much because we just
[2902.38 --> 2908.22]  wanted to focus on the view but like the demand was so crazy and so uh when an engineer at facebook
[2908.22 --> 2913.34]  like just did a blog post about flux just saying like how it's working so that people can have a
[2913.34 --> 2920.86]  reference and like everybody jumped on it like this was like if facebook was the messiah and like this
[2920.86 --> 2928.78]  was the way to go so i would say like this is like this went a bit overboard and so this is how we
[2928.78 --> 2934.38]  are doing it and it's working well and we hope it's going to work well for you but like again like
[2934.38 --> 2941.66]  we don't know your specific use case yeah and then you guys um shortly thereafter started talking about
[2941.66 --> 2947.10]  another thing which seems to be i don't know if you call it a spiritual successor or maybe just inspired
[2947.10 --> 2952.54]  by flux it's it's this is actually a framework now this is not just an architecture it's called
[2952.54 --> 2958.14]  relay yeah um an unreleased framework announced probably around the same time as react native
[2959.02 --> 2963.74]  which appears to be kind of doing the same stuff that flux you know is architected to do as far as
[2963.74 --> 2968.38]  actions data fetching so on so a lot of talk about relay yeah a lot of the philosophies are very
[2968.38 --> 2973.42]  similar right it has the the one-way data flow and and these kind of things having the centralized
[2973.42 --> 2979.34]  store for all your data um but uh one of the one of the problems we ran into with the flux architecture
[2979.34 --> 2985.90]  was keeping our client and server code in sync right so um especially like the way our like chat
[2985.90 --> 2991.98]  system was it was engineered is that basically the server endpoint there's just one um would basically
[2991.98 --> 2998.38]  have to prepare all of the data that the client could potentially want right and package that all up and
[2998.38 --> 3003.42]  then ship it down to the client in one big bundle and if you you know changed anything on the client
[3003.42 --> 3008.86]  it was very difficult to make certain that you know that data is um you know going to be available from
[3008.86 --> 3013.10]  the server uh and then when you're looking at the server like oh man we're fetching all this stuff like
[3013.10 --> 3018.22]  is some of this wasteful can we get rid of it it was very difficult to make sure that that piece of data
[3018.22 --> 3023.34]  is never going to be accessed by the client right and so keeping those in sync was very difficult and it led to
[3023.34 --> 3029.18]  to bloating the responses because in order to be safe and make sure we didn't introduce bugs
[3029.98 --> 3036.62]  we're more conservative with removing data from the payload uh and so what um relay um which is tightly
[3036.62 --> 3043.66]  coupled to graphql uh enables us to do is that the client actually specifies every single piece of data
[3043.66 --> 3050.70]  that it wants uh with the query and so it basically requests it explicitly from the server like you know i
[3050.70 --> 3055.98]  want you know the actor and i want their name and i want the their hometown and their phone number
[3056.46 --> 3061.82]  but i don't care about their birthday or whatever right uh and then the server can prepare that request
[3061.82 --> 3066.54]  specifically for that client and send it exactly what it asked for uh and so now the overfetching
[3066.54 --> 3072.94]  problem is gone the synchronization problem is gone uh and you know the the interaction there
[3072.94 --> 3077.82]  ends up being a lot more efficient and easier to work with what that also means kind of acts as a
[3077.82 --> 3083.50]  wrapper around the react component right and so because of that it's just waiting on that data
[3083.50 --> 3089.02]  it's kind of a prerequisite yeah for the component to render so react can basically just chill there
[3089.02 --> 3094.38]  wait till it's all resolved and then finally render you kind of you shake out a lot of complexity and
[3094.38 --> 3100.14]  dealing with transition states and loading spinners and stuff like that right exactly yeah the react
[3100.14 --> 3105.82]  component declares exactly what data it needs from the server and then the relay framework um makes sure that
[3105.82 --> 3111.26]  uh all of the different components that are going to be rendered together in that page load or um that
[3111.26 --> 3118.94]  view um it it combines all of their data fetching into one um one query and then fetches that in a batch
[3118.94 --> 3125.02]  uh and then it also manages updates and all these kind of things so if you uh you know if you're doing
[3125.02 --> 3131.66]  an infinitely scrolling list and you want to uh like scroll load some more data it'll handle like you know fetch
[3131.66 --> 3136.38]  like changing the cursors for the the query and appending that data and then updating only the
[3136.38 --> 3144.54]  components um that need the updated data and and things like that so and you say it's tied to graphql which
[3144.54 --> 3149.10]  to me i think is like you know you have rest and then you have this other way of querying an api
[3150.46 --> 3156.78]  yeah so the idea is the idea behind graphql is so the rest endpoint it gives you like the path to
[3156.78 --> 3162.38]  to an to an element but it doesn't say what attributes you want from the element and so what
[3162.38 --> 3170.38]  graphql does is it lets you specify the path like the exact set of attributes that you want and
[3171.02 --> 3179.18]  another benefit of graphql is by nature this is uh hierarchical so you can like deep down like you
[3179.18 --> 3186.54]  can dip down many times and it solves the program called n plus one fetching program so if you want to
[3186.54 --> 3191.26]  fetch a list and then each element of the list and for each element like another list
[3192.46 --> 3197.50]  if you are using the traditional rest endpoint you first need to fetch the list and then do
[3198.22 --> 3204.30]  20 queries for each element and then for each element do like 20 other queries and graphql makes
[3204.30 --> 3211.42]  it all go into one single query so whereas you you normally would get a singular rest resource this
[3211.42 --> 3217.18]  is like grabbing a tree basically yeah and you get it all in one query which is great for performance
[3217.98 --> 3222.22]  is graphql what you guys just you guys just came up with that is this uh is there prior art or
[3223.58 --> 3232.06]  in the wild out there so the history of graphql is uh when we re-implemented the ios app from web
[3232.06 --> 3241.74]  to native we needed a way to like fetch data and what we needed was to like get a json and like the
[3241.74 --> 3247.34]  engineers working on graphql that invented them saying like oh but i know i want this json so what
[3247.34 --> 3253.74]  i'm going to do is just going to remove all the values and keep like the shape and they decided that
[3253.74 --> 3261.18]  this was graphql and this is like as simple as this and they've been using it on the newsfeed ios
[3261.18 --> 3268.78]  for like three years now and on the and it spread like all the ios app is using graphql the android
[3268.78 --> 3275.26]  app is using graphql and the reason why we didn't talk about it yet is because if you want to implement
[3275.26 --> 3281.74]  graphql you need to change your entire backend because now your backend has to uh talk graphql and
[3281.74 --> 3288.46]  we didn't think it was like worth enough like changing your backend just for graphql like
[3288.46 --> 3295.18]  without any library but now that we are integrating graphql with relay we think like the benefit is
[3295.18 --> 3301.18]  like big enough so that we can like convince people to use like to change their backend to use graphql
[3301.98 --> 3307.98]  because like their code is going to be much better so graphql you guys obviously have your
[3307.98 --> 3312.06]  implementation if you've been running it in production for a few years is that something
[3312.06 --> 3316.78]  that's going to be available or is it already available yeah so the tricky thing about our
[3316.78 --> 3323.26]  implementation is our implementation talks to our facebook stack in php and things like this
[3323.26 --> 3329.02]  and this is not like reusable so the way it's going to are going to open source this is we're going to
[3329.02 --> 3335.50]  give a specification of the language so grammar and like what things means and we're going to provide
[3335.50 --> 3342.70]  custom implementations for uh popular things so we're going to have a node node modules that
[3342.70 --> 3351.42]  learns that knows how to take a graphical response and talk to mysql or postgres or mongodb and return it
[3351.42 --> 3359.02]  and so from this like uh prototype like reference implementation then people are going to be able to use it to
[3359.02 --> 3365.74]  uh adapted to the backends great so there'll be a specification and uh i've seen an implementation out
[3365.74 --> 3371.18]  there i tell you what you guys announced react native you got relay coming out you got graphql coming out
[3371.18 --> 3377.34]  you're really good at building buzz for your open source products um you're able to announce react
[3377.34 --> 3381.02]  native is now available which means most of our listeners have already quit listening they're out there
[3381.02 --> 3387.18]  playing with react native we i asked on twitter last night uh if people had questions you know for the
[3387.18 --> 3393.02]  react team and it was when can we get relay when can we get graphql they're chomping at the bits can you
[3393.02 --> 3400.06]  give us anything as far as like what we're looking at for these uh frameworks and tools so a few months
[3401.26 --> 3410.38]  so yeah same like uh we announced relay but we didn't expect like that crazy amount of hype uh from it
[3411.18 --> 3416.78]  so we're like oh we're going to explain like graphql and relay and like people are going to like see oh yeah
[3416.78 --> 3421.02]  this is a good idea and then like move on but like they didn't and now like we're asked like
[3421.98 --> 3427.02]  every single day like when is coming out when is coming out so like their entire graphql team and
[3427.02 --> 3432.30]  relay team uh shifted focus they stopped doing any development and they are just focused on open source
[3433.26 --> 3440.86]  so like in a couple of months you're going to be able to use it sorry for the wait yeah i think you
[3440.86 --> 3445.02]  guys will know better next time that uh yeah next time you announce and pre-announce something that
[3445.02 --> 3449.02]  they'll be knocking your door they've got flamed a little bit too on the on the pre-announce even of
[3449.02 --> 3453.74]  of facebook or sorry react native too is that you know how can you announce something that's not
[3453.74 --> 3459.42]  actually out there yet although you do have an app in the wild so that that does make some sense
[3459.42 --> 3465.02]  seems like with graphql um you know if the i'm not obviously here to like prioritize your guys's
[3465.02 --> 3470.22]  workloads or anything but like it's a specific similar to how with flux like you guys release flux as an
[3470.22 --> 3474.78]  idea as a as a description uh graphql obviously will need some sort of specification if it's going
[3474.78 --> 3480.14]  to have multiple implementations you know if the specification could at least be um shared front as
[3480.14 --> 3484.22]  far as that then other people could hop on it because obviously everybody has their own back-end
[3484.22 --> 3489.58]  stacks and data stores so we can start having that ecosystem similar to fluxes perhaps while we wait for
[3490.14 --> 3494.30]  you know your guys's canonical implementation yeah that's definitely the first step uh and the guys are
[3494.30 --> 3501.10]  working on coming up with the the full like um spec for the the language um but unfortunately like
[3501.10 --> 3506.30]  it came about pretty quickly when we were first implementing it racing to build the new um ios app
[3506.30 --> 3511.42]  and there's definitely some warts so they're working on trying to smooth out some of those warts that we've
[3511.42 --> 3516.94]  been living with for a while uh so that the community doesn't have to have to deal with them um and so
[3516.94 --> 3520.30]  they're they're trying to figure that out as quickly as they can and then they'll uh they'll put something out
[3520.30 --> 3526.06]  there it sounds like you guys might have gotten kicked out of your room too during this conversation
[3526.06 --> 3531.82]  you guys move around over there yeah we did yeah well that's that's actually good timing anyways
[3531.82 --> 3535.74]  because we're we're about to close up we could probably drill a little further on a couple of
[3535.74 --> 3539.66]  thoughts here but uh you know one of the things that you guys pointed out i'd love to have you back
[3539.66 --> 3545.18]  on the show whenever this becomes more and more real um around react native is the component library
[3545.18 --> 3549.42]  whenever that's you know whenever you can release something new about that please keep in touch
[3549.42 --> 3553.90]  because that's something that's you know for me particularly is is uh perked my ears up because
[3553.90 --> 3562.22]  i was thinking geez that'd be so nice to to be able to you know learn one place to use react js and um
[3562.22 --> 3567.82]  and have that library available but well guys thank you so much for joining me and jared on this call
[3567.82 --> 3572.14]  today i know that uh everyone's pretty excited about react itself but then also react native coming out
[3572.14 --> 3579.26]  uh huge announcement flux uh the the idea there but then relay coming and graph ql coming later
[3579.26 --> 3584.62]  uh in a few months that sounds pretty cool so let's close the show there and with that uh thanks
[3584.62 --> 3588.94]  everybody for listening and we'll we'll say goodbye now so goodbye great thanks for having us
[3588.94 --> 3589.74]  yeah
[3589.74 --> 3600.70]  mega
[3601.42 --> 3603.42]  yeah
[3604.22 --> 3605.26]  uh
[3605.26 --> 3606.22]  you
[3606.22 --> 3607.54]  Baby, baby, baby
