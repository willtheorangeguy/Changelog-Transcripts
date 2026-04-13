[0.00 --> 15.68]  what's up welcome back this week on the change law we're joined by daniel thompson
[15.68 --> 20.96]  co-founder and core member of tauri it's been a year since we had daniel on the show
[20.96 --> 26.68]  he catches us up on all things tauri their continued efforts towards tauri 1.5 which just
[26.68 --> 32.62]  released the launch of crab nebula and other people pushing the tower ecosystem forward
[32.62 --> 39.60]  and building on top of it the state of electron versus tauri user interface with tauri and daniel
[39.60 --> 45.48]  even surprised us with his idea of creating a web browser a massive thank you to our friends and our
[45.48 --> 52.52]  partners at fastly and fly this podcast got you fast because fastly is fast super fast globally
[52.52 --> 58.18]  check them out at fastly.com and our friends at fly help us put our app and our database close to our
[58.18 --> 64.22]  users all over the world with no ops and they'll do it for you too check them out at fly.io
[64.22 --> 79.10]  if i gave you a hundred dollars towards your air monitoring would you use it that's the great
[79.10 --> 84.46]  question we have for you today because century is a long-standing partner of ours a long-standing
[84.46 --> 89.92]  sponsor of ours and we love century and we think you'll love them too so the easiest way to get
[89.92 --> 94.70]  a hundred bucks towards your century bill is to use our code when you sign up changelog is the code
[94.70 --> 99.40]  this code gives you a hundred dollars which is basically three months free of their team plan
[99.40 --> 105.08]  that's on top of their completely free developer plan they also have a really cool sandbox so if you
[105.08 --> 108.64]  don't know much about century you've never tried it or you've never played with it and you don't want
[108.64 --> 113.44]  to install it right this second but you want to see how it works on sample data you can use that
[113.44 --> 118.26]  the sandbox is on their website we'll link it up in the show notes check it out again use the code
[118.26 --> 122.64]  changelog get a hundred bucks which is basically three months free on their team plan in addition
[122.64 --> 132.66]  to all the goodness they give you in the free developer plan check them out century.io that's s-e-n-t-r-y.io
[132.66 --> 162.48]  all right we're here with daniel thompson from towery
[162.48 --> 167.62]  back after about a year and a half we had you on the podcast welcome back daniel thanks it's really
[167.62 --> 172.98]  really great to see you guys again one of the main comments we got was how amazing your voice is
[172.98 --> 180.24]  i was kind of jealous yeah people were jelly of your voice yeah well you know i think that um
[180.24 --> 185.78]  i've gotten older so it's more raspy now you know i sound like my grandpa all of a sudden
[185.78 --> 191.74]  fast forward a year goes by and i'm 10 years older yeah it's been one of those years or what
[191.74 --> 200.44]  it's been a non-stop year yeah i mean we met i think last uh last summer yeah after the 1.0 was
[200.44 --> 207.26]  released talked about the plans for the future and and i mean i did review the show and i think we're
[207.26 --> 215.32]  pretty spot on you know this uh this this coming soon is going to be the release of the 2.0 which
[215.32 --> 223.84]  has uh mobile and embedded into it android and ios i found out that uh towery ios on the android makes a
[223.84 --> 232.52]  8.5 megabyte binary so competitive with react native and ios is a little bigger but you know i think that
[232.52 --> 239.18]  early adopters also have a lot to learn about how to get things really small and tiny and i guess
[239.18 --> 244.74]  it's one of the things that we see on twitter a lot people are like yeah my first towery app it's 14
[244.74 --> 251.24]  megabytes and i'm like did you minify did you put in those uh the special cargo flags for the release
[251.24 --> 257.14]  and they're like oh no and then they come back now it's only eight megabytes so i think we've still
[257.14 --> 262.22]  we've held true to that excellent to hear well for those who didn't listen the first time around
[262.22 --> 268.82]  that episode is called build tiny multi-platform apps with towery and webtech i remember we had a
[268.82 --> 275.04]  hard time naming that episode yeah we did because towery is a little bit it's not hard to explain but
[275.04 --> 278.98]  it's hard to like put into three words which is we'd like to be in the three to five word range
[278.98 --> 286.22]  so daniel for those who heard that but haven't heard much else of towery give the quick explainer so
[286.22 --> 291.26]  we're all on the same page well i mean first and foremost towery is a community of developers
[291.26 --> 295.42]  building stuff for developers and the stuff we like to build for developers are tools to
[295.42 --> 301.94]  help make apps we started out with desktop and now we're working toward mobile apps and you can
[301.94 --> 307.30]  bring any front-end framework you want in a lot of ways it's similar to electron and capacitor
[307.30 --> 315.30]  but we put a lot of special focus on the security of the framework as well as the ultimate bundle
[315.30 --> 321.40]  size we want things to be small and performant and not consume a lot of resources so that's how we
[321.40 --> 327.32]  how we started it and that's how things have been going so you have a lot of sponsors which is awesome
[327.32 --> 333.96]  i assume we talked to you after right after 1.0 and usually 1.0 is a time where people decide okay
[333.96 --> 340.14]  i can finally take this thing seriously and it's usually a boon for adoption have you had a lot of
[340.14 --> 346.42]  folks building stuff with towery since the release yeah i just recommend looking over at the um
[346.42 --> 352.66]  awesome towery repo at our github organization and it's kind of like endless scrolling lots of dev tools
[352.66 --> 363.78]  lots of games actually things are being built for communication and the rate at which i measure
[363.78 --> 370.70]  adoption though has has changed a little bit over the past year um there's some reasons for that but
[370.70 --> 377.68]  mostly we're seeing people come in with really innovative questions things that go outside of our
[377.68 --> 386.08]  expectations when we built the original project and in most cases we're finding that it's not necessarily
[386.08 --> 392.64]  an edge case but people have to start learning to maybe think differently about how they construct
[392.64 --> 399.92]  their apps and and move heavy lifting to the rust side and use the the the user interface for user
[399.92 --> 405.88]  interface things and not put so much logic and i think for a lot of you know classically recognized
[405.88 --> 410.88]  full stack devs it can be kind of complicated because you don't care where it runs it you know
[410.88 --> 416.68]  on the client in the browser on the cloud at the edge as long as it's running somewhere that's fine but
[416.68 --> 422.94]  we're trying to provide these these highly tuned opportunities and you know people are making
[422.94 --> 428.48]  musical instruments they're making drawing tools they're being creative and i think the the the
[428.48 --> 435.10]  biggest news out of our ecosystem is recently fig io which is a developer tool that gives you kind of a
[435.10 --> 443.50]  supercharged command line experience was just acquired by aws yeah i saw that and they use uh the
[443.50 --> 450.86]  windowing and the web viewing libraries of towri so they're part of the towri family and i guess
[450.86 --> 457.52]  the uptake has been has been really heartwarming to see and it's also you know it's early days i think
[457.52 --> 466.14]  a lot of projects are in stealth uh you know if you look at that awesome uh towri repo i don't know like
[466.14 --> 472.36]  10 percent of them are closed source which means people are you know making money selling their
[472.36 --> 478.20]  products there's ecosystem plays that are being being made where people are starting to offer
[478.20 --> 485.78]  license servers or license services or analytics people are creating integrations with you know
[485.78 --> 493.10]  supabase and airtable and firebase and you know you're starting to see these projects come in that
[493.10 --> 498.48]  have a set of requirements and people are solving the problems and i think that's the exciting part
[498.48 --> 505.58]  that we're at now you know last year when i was here we were really in the issue bubble and and the
[505.58 --> 514.14]  issue bubble in open source is a place where you only hear complaints you only hear problems you only
[514.14 --> 521.94]  see people struggling with what you've built and and over the past year we've started to hear from
[521.94 --> 531.88]  companies that are using towri internally we've started recognizing oh yeah right um engineers solve
[531.88 --> 536.84]  problems and if you're behind a corporate firewall you're going to solve your problem one way or the
[536.84 --> 542.76]  other and yeah i mean that's really awesome to hear just looking at the sponsors listed on the
[542.76 --> 547.14]  homepage there's lots of big names there as well so i assume they have some sort of interest in the
[547.14 --> 553.82]  success of the project do you find that the rust we focus a lot on the rust aspect of towri last time
[553.82 --> 558.82]  around it was just kind of digging into the tool and figuring out how to use it and one thing that
[558.82 --> 563.00]  you said that stuck with me at that time is you think that this is a nice you didn't say gateway drug
[563.00 --> 569.48]  but i will say that it's a nice entrance into the rust ecosystem and i wonder you know i've been
[569.48 --> 575.78]  tinkering a little bit with just the fringes of towri as i found in a use case i've been waiting for a use
[575.78 --> 581.36]  case to give it a try so i've been doing the getting started and dipping my toe into the water
[581.36 --> 587.92]  as it were and as a web developer you know full stack web developer whatever you want to call me
[587.92 --> 595.80]  somewhat intimidating even though nothing seems too dragon-y so far but i'm still just like
[595.80 --> 602.78]  not so sure about like you said where do i put things what belongs in rust what doesn't
[602.78 --> 609.30]  etc is that a common refrain are you answering those questions a lot do you think it's been a
[609.30 --> 614.86]  barrier to adoption because it's an opportunity for rust but it might be a barrier for towri i think
[614.86 --> 620.22]  it's both i really think it's both i know that people are learning rust because once you get to a
[620.22 --> 626.24]  certain point in building your app you're like oh i need to send a message from one window to another
[626.24 --> 634.26]  window and i have to use the rust bridge to do that or you you want to you know do tighter integrations
[634.26 --> 643.10]  with the cryptographic systems you want to avoid using the database inside of the web view so you
[643.10 --> 651.70]  you kind of have to start thinking about oh i'm going to say it wrong sql sqlites sql i don't tell you
[651.70 --> 657.08]  how to say that the database sql there you go richard hip told us how i still can't toe the line
[657.08 --> 663.42]  but adam always has it sqlite and you know to address your question we're seeing a lot more
[663.42 --> 671.06]  questions come up about using more rust in the background of a tower app than in the foreground
[671.06 --> 678.70]  of the the javascript side there are always still people just you know dabbling well look i think that
[678.70 --> 684.04]  the opportunities that people have to learn new programming languages come with risk and benefits
[684.04 --> 689.80]  and it's really up to the people to decide what they want to do we've seen both sides of this where
[689.80 --> 697.18]  people have jumped because rust is hard to learn we've also seen people embrace it and use toweri as a
[697.18 --> 705.82]  way to become a rust engineer so we've seen both and i think that what we've also seen are people
[705.82 --> 713.60]  who say well look i'm using python already i don't care about rust so open bb they made a a python
[713.60 --> 718.96]  adapter for one of the low-level libraries somebody else just recently posted an elixir
[718.96 --> 725.96]  kind of binding so you can use a phoenix channels instead of rust people are working on believe it or
[725.96 --> 733.24]  not a php backend so that you can write all your logic at php and still get all of the benefits of
[733.24 --> 739.06]  or type rust core and a user interface that can directly access both the rest apis through its
[739.06 --> 748.16]  javascript or call out to believe it or not php javascript ideas on the horizon as well so i i think
[748.16 --> 755.62]  that like what tallry itself started out as is one thing and where it's moving i think is another and
[755.62 --> 761.76]  that is turning into a collection of tools that you can kind of pick and choose how you want to piece
[761.76 --> 766.90]  them together that's really interesting to hear it sounds like there's enough value there enough
[766.90 --> 772.86]  interest to when even if rust is a barrier for you there's people that are like look i can work around
[772.86 --> 779.36]  this particular aspect of toweri by building a php backend for instance or providing access to elixir
[779.36 --> 784.86]  because i want to use it so bad and i don't really want to use this part of it so i mean that to me
[784.86 --> 791.74]  shows quite a bit of interest for people willing to you know break out their code editors and work
[791.74 --> 800.68]  around or code around these issues that's that's pretty cool but you have this year as we meet again
[800.68 --> 807.24]  you have more news obviously the mobile stuff is huge but you also have news around uh what's behind
[807.24 --> 814.96]  toweri open source strategy funding round there's lots going on there i know you had a very interesting
[814.96 --> 819.84]  take on open source last time can you tell us what you guys have figured out in terms of making this
[819.84 --> 826.62]  thing i don't know sustain and and thrive it's tricky we actually started a company last year
[826.62 --> 834.28]  some of us from the toweri working group started a company last year in november okay and it was
[834.28 --> 841.10]  really important to us that nothing changed from the outside it's still a militantly driven open
[841.10 --> 850.04]  source community that now is supercharged with a handful of engineers being paid full-time to do the
[850.04 --> 857.44]  research development and maintenance that a massive project like toweri needs and that company is called
[857.44 --> 867.16]  crab nebula we we chose crab nebula because we liked the idea of a place where stars are born a nebula is a
[867.16 --> 876.46]  a star factory if you will and we chose crab because well rust the the the icon the the avatar if you will
[876.46 --> 887.32]  is ferris the little crustacean rustation and now obviously you can't make a pitch to a vc and say we're
[887.32 --> 896.28]  just gonna serve as a charity and donate all of your money to open source things uh would be nice
[896.28 --> 904.94]  if they work that way maybe but i think that uh we we found the perfect vc uh to join us on this trip
[904.94 --> 914.40]  that's jj from oss capital west coast based venture group that only supports early stage open source
[914.40 --> 922.36]  projects commercial open source projects and through jj and through years and years of being around
[922.36 --> 930.88]  we sort of collected an all-star regiment of of angels who joined us along the way i could drop all
[930.88 --> 936.76]  of the names uh maybe you can edit them out or choose the ones you like but i think you know of the
[936.76 --> 945.26]  almost 30 angels that we have the good dozen that are really relevant um are you know novel ravikant
[945.26 --> 952.08]  from angel list automatic inc the company the investment arm of automatic from wordpress fame
[952.08 --> 959.64]  guillermo rauch the ceo of versell thomas domka the ceo of github uh tom preston werner the
[959.64 --> 967.30]  co-founder the original co-founder of github uh paul copplestone from superbase justin hoffman the
[967.30 --> 972.16]  former svp of elastic if i didn't say bob young i'll say his name again because he's amazing
[972.16 --> 980.98]  but amad mustikyu was the ceo of stability ai clement de long the co-founder and ceo of hugging face
[980.98 --> 988.40]  dave tier the founder of one password adam wiggins the co-founder of heroku navin gudropa the founder
[988.40 --> 995.14]  of noco db heather meeker if you know heather she's uh not only the general partner of oss capital
[995.14 --> 1003.56]  but wrote the book on oss licensing and you know we also have a couple people like uh cassidy williams
[1003.56 --> 1011.24]  who's the cto of condenda you maybe know her as cassidy also uh tijas kumar and i think what
[1011.24 --> 1020.18]  what drove us to work with this number of angels is getting to to know your idols the people that have
[1020.18 --> 1025.46]  built open source the people who are building open source and people who are poised to build the next
[1025.46 --> 1033.40]  open source who understand the challenges of not only having a product but also having the machinery
[1033.40 --> 1039.68]  the understanding and the ability to innovate into products and new products as they come out um
[1039.68 --> 1050.66]  so that happens and nothing changed at toweri i mean we kept on building toweri in line with our um
[1050.66 --> 1061.32]  foundations expectations but behind the scenes um we are working on a few products i mean other than
[1061.32 --> 1066.88]  investing time in toweri we're also auditing toweri that's one of the things that we love doing
[1066.88 --> 1073.32]  actually is auditing people's uh software that they built with toweri with rust you know we just
[1073.32 --> 1082.28]  completed an audit for a company called blue bay eye that uses toweri we don't really do custom
[1082.28 --> 1090.56]  development we do but we don't like we will pick from uh clients who want to have something done that
[1090.56 --> 1095.38]  aligns with our research goals that makes sense like we're not just out there cutthroat working
[1095.38 --> 1100.66]  for half a million dollars because somebody wants to pay us money to build something for them i mean
[1100.66 --> 1105.64]  we'd consider it but it has to align with our research goals things that we want to know things
[1105.64 --> 1111.82]  that we know that the community needs those are the kinds of uh of customers that we've been looking
[1111.82 --> 1119.18]  for and been finding we also recognized from the beginning that shipping apps is hard it's really hard
[1119.18 --> 1126.24]  like i mean anybody can build an app but once you're done how do you distribute it how do you update it
[1126.24 --> 1135.94]  how do you sign it and for that we're building a platform to empower the people to ship their apps
[1135.94 --> 1145.00]  like super easy super cheap in some cases totally discounted for open source and we know that this
[1145.00 --> 1151.14]  is going to get a little political i don't know if that's okay but we know that the incumbents uh like
[1151.14 --> 1159.30]  microsoft and apple and alphabets and meta and byte dance they have vested interests well maybe less
[1159.30 --> 1165.28]  byte dance but definitely the the platforms they have an interest in keeping a hold over a chokehold
[1165.28 --> 1170.76]  over the app signing process they keep such a chokehold on it that in my opinion it's not
[1170.76 --> 1176.26]  talked about enough in the supply chain like that final bit of app signing for gui apps and you know
[1176.26 --> 1181.46]  in some cases even cli apps it's just like oh yeah apple will take care of that for you we got you we
[1181.46 --> 1186.88]  got you come here come here and just give me your 99 euro or microsoft changing the game suddenly last
[1186.88 --> 1193.88]  april saying now you have to get an extended validation dongle or hsm but don't worry you can use our
[1193.88 --> 1201.02]  super secure never been hacked for azure platform for that google is a little bit less concerned i
[1201.02 --> 1207.24]  think that anything that impacts their ad business is going to uh be a problem for them but apps on
[1207.24 --> 1212.06]  devices keeps people on devices keeps them buying devices so i think that that that's okay for them
[1212.06 --> 1218.06]  but when i hear from people from the tower community that they are having problems signing their apps
[1218.06 --> 1223.22]  people aren't like some people don't even sign them they just ship their microsoft apps without a
[1223.22 --> 1229.90]  developer signature and they're like people will deal with it and there's no money solution here
[1229.90 --> 1236.54]  there's no lobbying we can do but we can in europe at least get involved with the european commission
[1236.54 --> 1247.48]  and its platform policy work serving as experts and you know making sure that these these changes
[1247.48 --> 1254.66]  are respected that other types of app stores can be on their devices other third-party apps can now
[1254.66 --> 1263.12]  starting in april in the european union by law have to be landing on these devices and you know i i feel
[1263.12 --> 1271.30]  i feel very very deeply about empowering the citizen developers out there who don't have the 99 euro or who
[1271.30 --> 1279.54]  are in a third world so-called third world country where 99 is just like a month of food but they still
[1279.54 --> 1284.78]  can build their apps but they can't distribute them and they have no access to these larger markets i find
[1284.78 --> 1291.34]  that compelling in a very sad way and i think that you know the the this mixture of good business good
[1291.34 --> 1298.78]  politics supporting the community is really in the dna of crab nebula so much to the point that
[1298.78 --> 1304.38]  one of our first products that we're going to be bringing out in q4 and you can find out about it
[1304.38 --> 1312.72]  just by following our socials is a dev tool because debugging anything is hard debugging towery is triple
[1312.72 --> 1321.52]  hard web has great dev tools apps not so much and we want people to be able to connect their app to an
[1321.52 --> 1326.14]  analyzer to figure out where things are going wrong or getting better and i i understand you're thinking
[1326.14 --> 1331.76]  daniel this is niche not many people are using towery but the the great news is that we're we're
[1331.76 --> 1338.48]  working together with other partners in the rust ecosystem to define and and use emerging standards
[1338.48 --> 1344.98]  so that the work that we're doing for towery people can be used by at first others in the rust
[1344.98 --> 1352.70]  ecosystem and later other ecosystems as they get interested in it and i i think the the final thing
[1352.70 --> 1359.64]  that i'd like to point out is that you asked how how is this how is this possible how can you keep the
[1359.64 --> 1367.96]  the energy going the the momentum going and in open source projects you generally have like three or
[1367.96 --> 1374.18]  four models one a company sits on top puts its thumb down it's not even benevolent dictator it's like
[1374.18 --> 1380.00]  we're doing this now this way we're calling our project open source and later on we can rug pull
[1380.00 --> 1388.28]  but another one is a benevolent dictator who decides the way the project goes generally takes all of the
[1388.28 --> 1394.72]  funds and other people contribute as they have time people come people go and what we have with
[1394.72 --> 1402.86]  towery though is is really quite compelling because from the core team five of the people are still around
[1402.86 --> 1409.70]  almost five years later and i think that that's a testament to the fact that we really enjoy doing it
[1409.70 --> 1419.60]  and yet i don't believe that it should be just the goal of one company in sitting in malta to finance
[1419.60 --> 1426.88]  an entire open source project right and we do have donors and that's amazing i think where where things
[1426.88 --> 1435.34]  are tending toward is toward applying for more systemic grants you know where we apply for funding from
[1435.34 --> 1443.34]  the european commission from organizations like nl net and potentially even other companies come and recognize
[1443.34 --> 1449.26]  the value that they've gotten from the community and start giving back i don't know i think that that that's a
[1449.26 --> 1456.92]  very long long play expecting people that get something for free to give back to a community that they're not so much
[1456.92 --> 1463.40]  involved in there's a lot to unpack there at the end of the last show i asked you about venture capital and the
[1463.40 --> 1469.32]  organization and things that would come from the one point over at least that was about a year ago and you
[1469.32 --> 1475.02]  kind of tease us a little bit with a topic we like to talk about with core doctorow choke point capitalism i think
[1475.02 --> 1480.86]  you're talking about that with app signing i think that's definitely a a position of hey if there's an artist
[1480.86 --> 1486.34]  shipping something there's a choke point at some point that says okay we're gonna collect our our toll our fee
[1486.34 --> 1491.40]  and that seems like what one part of your mission then you mentioned the core team and the model of open
[1491.40 --> 1497.92]  source which i think is interesting i'd love to touch all those obviously but uh maybe focus in on the
[1497.92 --> 1502.62]  organization itself like remind us what its license as remind us of the organization what has happened
[1502.62 --> 1508.70]  since one point to sort of formalize i know you mentioned crab nebula what exactly is the model of
[1508.70 --> 1513.74]  towery right now like how do you compare it to others you mentioned company atop rug polling we've seen
[1513.74 --> 1519.38]  that more recently and that's fresh and uh it's a fresh wound to the open source community
[1519.38 --> 1524.94]  yeah absolutely so nothing has changed in the organizational structure of towery itself there
[1524.94 --> 1531.58]  is still a board of directors there is still an entity held within a dutch foundation the proper
[1531.58 --> 1538.02]  name is the towery program within the commons conservancy all of the code is open source apache to
[1538.02 --> 1545.06]  mit dual licensed at your leisure we take potential license violations within our own code base very
[1545.06 --> 1552.84]  seriously we will investigate those and resolve them a lot of times uh it's a mistake usually it's
[1552.84 --> 1558.30]  something we can correct actually i think we've always corrected them so to summarize the licenses
[1558.30 --> 1567.22]  mit apache to it is still morally stewarded by the car the the commons conservancy and internally
[1567.22 --> 1574.70]  there is a working group composed of people who elect themselves to join to the working group currently
[1574.70 --> 1584.42]  there are about 45 members of the working group and i would say about 20 are active and these are not
[1584.42 --> 1591.74]  all employees of crime nebula i mean there's a large number of them but the majority of the current
[1591.74 --> 1598.78]  working group members are not and we even have other companies more or less explicitly involved or with
[1598.78 --> 1607.10]  or by association one of our board members actually works at microsoft so from the organizational side of
[1607.10 --> 1615.98]  the open source projects nothing has changed from the perspective of the company we are donating slash
[1615.98 --> 1621.50]  allocating i don't know how you want to say it full-time employees to spend all of their working time
[1621.50 --> 1630.54]  on research developments and maintenance of towering itself of the the core pieces of that tech and then
[1631.02 --> 1638.78]  the products that the the company itself makes and distributes are generally going to be at the very
[1638.78 --> 1643.18]  least source available we always want to make sure that people can see what we're doing and have faith in
[1643.18 --> 1649.18]  what we're doing a lot of the things will also be open source mit apache 2 as as we roll them out
[1651.50 --> 1667.18]  what's up friends today we have an awesome sponsor dot tech domains and they're giving this segment away
[1667.18 --> 1673.50]  to dot tech founders to showcase the amazing things that are being built on a dot tech domain through their
[1673.50 --> 1680.32]  startups dot tech program dot tech domains are the go-to namespace to build anything in tech and home to the
[1680.32 --> 1686.24]  world's most innovative startups for example a self-driving ai company that's raised 3.7 billion
[1686.24 --> 1694.88]  dollars and is building on aurora dot tech the most viral crypto app of 2023 is building on friend dot tech
[1694.88 --> 1701.12]  and an ai startup backed by sam altman and open ai is building on one x dot tech there are thousands of
[1701.12 --> 1707.36]  companies like this who are taking advantage of dot tech domains to reinforce their brand as tech focused
[1707.36 --> 1712.40]  and forward thinking but here's the cool thing instead of just selling domains dot tech domains
[1712.40 --> 1717.84]  wants to give their users a platform to show the world the amazing things their dot tech startups are
[1717.84 --> 1724.32]  building so if you're building on a dot tech domain or you want to simply apply to this startups dot tech
[1724.32 --> 1731.12]  program by going to startups dot tech slash changelog and filling out the form that way dot tech startups get
[1731.12 --> 1736.32]  to be in front of thousands of people like on this show and we get to learn about cool things they're building
[1736.32 --> 1743.84]  on dot tech again go to startups dot tech slash changelog once again startups dot tech slash changelog
[1758.16 --> 1766.16]  so crab nebula is the entity which has all these amazing angels correct correct and it's starting off as
[1766.16 --> 1773.04]  consulting and auditing but that's not the big picture that you drew for these angels that got them
[1773.04 --> 1778.56]  excited i would imagine it'd be okay to back something like that but your bigger picture is
[1779.20 --> 1786.16]  products services seems like some sort of distribution network of you know maybe app stores etc for the
[1786.16 --> 1794.56]  tower ecosystem is that what you're saying right we see consulting itself as a way to offset the cost of
[1794.56 --> 1801.12]  r&d yeah you know with with the addition of grants coming in that covers our rd costs because we align
[1801.12 --> 1809.44]  those tasks with r and d and auditing is important because it keeps our security team fresh and we're
[1809.44 --> 1815.04]  helping the ecosystem arguably with important projects that people are using by auditing them of
[1815.04 --> 1822.88]  course neither of those is that you know exponential curve that everybody is dreaming about and i think that the
[1822.88 --> 1832.08]  the long play for crab nebula is in the services of distributing solving this signing problem one way or the other
[1832.64 --> 1841.68]  and providing tools that bring joy to the act of development of software again you know and i think that what we're
[1841.68 --> 1851.44]  already seeing inside the team is we are generally very dissatisfied with products out on the market it's hard for us to find stuff that
[1851.44 --> 1859.44]  ticks all the boxes and there are a couple things that we are building internally that we might just spin off into a product
[1859.44 --> 1867.68]  itself just here you go world buy a seat have fun because i think that the benefit of working with all of these fantastic
[1867.68 --> 1876.40]  fantastic people is the perspectives that you get when you're analyzing a problem field and and seeing
[1876.40 --> 1882.88]  all of the the different ways in which people are criticizing things like oh the security is crap oh the layout
[1882.88 --> 1892.48]  so is this bootstrap 2.0 you know and it's a challenge to reel people in to say okay love we're not going to build that
[1892.48 --> 1897.28]  product right now we're going to solve our own problems on our own time but right now what we are
[1897.28 --> 1904.40]  building are these dev tools and building out the platform because those are the things that will scale
[1904.96 --> 1915.44]  especially once you consider that the mechanism for bundling signing and distributing it's kind of the same no
[1915.44 --> 1922.32]  matter what platform you're using you know if it's react native or it's electron or it's any any of the
[1922.32 --> 1931.84]  other competitors or competing systems to towering i guess is still just a bundle and a sign and a ship
[1931.84 --> 1939.60]  so that move there allows us to also become more than just the towering company i think that that's
[1939.60 --> 1945.52]  you know that's a risk that we identified really early and as a matter of fact it would technically be
[1945.52 --> 1951.76]  prevented by the statutes of the open source community no one entity can profit exclusively from
[1952.48 --> 1958.00]  towering itself we cannot be the towering company but we can be a towering company we can maybe be
[1958.00 --> 1962.96]  the best towering company but we can't be the only towering company and we are starting to see people
[1963.76 --> 1971.12]  start building their products around towering as well so so if you created a platform for towering you
[1971.12 --> 1976.24]  would desire other platforms for towering is that what you're saying like if you were like the app store for
[1976.24 --> 1981.04]  towering apps that did all the bundling and signing and whatever else is involved and allowed you to
[1981.04 --> 1987.76]  distribute your software to users crab nebula you're not going to be the next apple in that regard is
[1987.76 --> 1991.68]  that what you're saying like the open source bylaws make it so you you can't be that because i mean
[1992.24 --> 1998.96]  given your 100 success we would end up in the same place with we put you in the list we'd be like oh man
[1998.96 --> 2004.80]  microsoft and and apple and crab nebula like they're all like we would just add you to the list wouldn't we
[2004.80 --> 2012.56]  okay maybe maybe the ambition is a little bigger maybe the ambition is more to say that the the towering
[2012.56 --> 2018.00]  framework itself would be more aligned with something like javascript it's not a product towering is not a
[2018.00 --> 2025.52]  product in and of itself it's a way to get stuff done like javascript like php like ruby and we would
[2025.52 --> 2033.36]  like to consider ourselves as the people pushing that ecosystem forward and developing on top of it
[2033.36 --> 2039.60]  but we are not towering because towering can't be a product it can't monetizing open source for me
[2040.48 --> 2047.52]  is go ahead go off go ahead it's one of the scary parts about this no like i have a lot of friends in
[2047.52 --> 2051.36]  the industry and i don't want to piss anybody off but i really hate it when licenses get changed or what
[2051.36 --> 2058.32]  communities break down or when you know corporate interest and greed suddenly redefines community
[2059.12 --> 2064.64]  and then you find out what it is behind the community you find out oh it was the money
[2064.64 --> 2071.36]  behind the community if crab nebula and it's a startup right like startups have a gradient of
[2071.36 --> 2078.48]  potential success if crab nebula goes down it would suck for crab nebula towering can continue
[2078.48 --> 2083.04]  kind of right and i think that that's this kind of well i mean if you're funding some of the core
[2083.04 --> 2088.32]  team members and you're a a major financier behind the scenes of making things happen then obviously
[2088.32 --> 2094.00]  the economics of supporting it change you're right in the fact that it can continue but it you know
[2094.00 --> 2100.24]  it's financially stabilized to some degree by the success and the angels that you've you've mentioned so
[2100.24 --> 2103.12]  there is no way to completely remove yourself up from that so i'm not saying that's a
[2103.68 --> 2107.76]  strike against you it's just the truth i i i want to agree with you in principle
[2107.76 --> 2115.68]  but i'm not going you should you should because i'm right i i mean i know i know you're right for
[2115.68 --> 2119.68]  you and from where you're sitting no from from where you're sitting i think it makes a lot of
[2119.68 --> 2126.32]  sense but the point i was trying to make was and this is something i'm working with the the whole
[2126.32 --> 2131.36]  working group on and it's not something that's done in software very often i mean look at ecma script
[2131.36 --> 2137.44]  2022 it's never ending it's going to be typescript someday the point is i think at some point we
[2137.44 --> 2143.84]  can actually declare tower is done i'm not saying kubernetes done but done enough so that all you have
[2143.84 --> 2148.32]  to do is add little things and there's little bits of maintenance but done done to the point where the
[2148.32 --> 2155.04]  features have been completed and maybe that's the point in time where we get to start thinking about
[2155.04 --> 2160.96]  other stuff we'd like to build i don't know like a browser come on that's too much work is it
[2160.96 --> 2166.88]  if we lay the groundwork for that over time it might i don't know i'm not trying to get ahead
[2166.88 --> 2171.20]  of myself but i we have opinions we just shared our opinions on this do you listen our show often
[2171.20 --> 2176.88]  daniel by any chance i do i do we just went off on this we just went on like what we want in browsers
[2176.88 --> 2182.08]  me jared and nick on our talk show gino and friends so we were just like knee deep in this so
[2182.08 --> 2187.20]  we're just talking about an open source browser right that would be amazing so you're teasing us here but
[2187.20 --> 2194.16]  i mean yeah towery being done when the underlying platforms the deploy targets of towery are never
[2194.16 --> 2201.04]  finished it seems like okay maintenance but how much of a burden is that i mean ios 17 just came out
[2201.04 --> 2208.16]  certainly as the new versions of these desktop and and mobile platforms that you're creating apps for
[2208.16 --> 2213.12]  are changing they're moving targets so towery can't be finished unless it's irrelevant but maybe you could
[2213.12 --> 2218.24]  say just major efforts are done as a matter of fact at crab nebula this week we decided we're
[2218.24 --> 2223.60]  changing research and development changing its name research development and maintenance rdm because
[2223.60 --> 2229.20]  maintenance is that it's like that part of r&d that i think people forget like let's make a brand new
[2229.20 --> 2236.32]  framework and call it new and like rage on all of the things that everyone else thinks is a good thing
[2236.32 --> 2245.68]  and no i mean right now in the rdm department we are working on a grant from nlnet together with the
[2245.68 --> 2255.76]  awesome folks over at agalia to verify that we can use servo as a web view target for towery apps
[2256.56 --> 2263.84]  with early success seems quite actually quite good already for the short time that the agalia team has
[2263.84 --> 2270.40]  taken up the helm of working on servo and it's a long future and at some point people get bored and
[2270.40 --> 2276.08]  they start having silly ideas and i'm not saying we will build a browser i'm not saying we won't
[2276.72 --> 2282.72]  i do know that it's a massive undertaking an open source browser is going to require a ton of stakeholders
[2282.72 --> 2292.56]  a ton of specialists for a very long time and hey we're not raising money right now but i think that if
[2292.56 --> 2298.48]  you were to do something like that you would definitely have to have like the entire eu behind
[2298.48 --> 2303.04]  you you'd have to have the european commission behind you you'd have to have more than just money
[2303.04 --> 2310.64]  you need the the charm and the goodwill and i mean the drive kind of comes for free because otherwise
[2310.64 --> 2315.60]  we wouldn't be talking about it but i don't know do you guys remember our first conversation when i told
[2315.60 --> 2321.60]  you i've always kind of been interested in building tools yeah and for me one of the
[2322.64 --> 2328.64]  interesting side effects about working with towery is that lucas and i started way back in the day and
[2328.64 --> 2332.48]  we thought we were going to make a better electron we haven't gotten there yet electron is better in
[2332.48 --> 2338.08]  a number of ways i'll say it here towery is better in a number of ways it's a different thing but that's
[2338.08 --> 2343.52]  what we started out to do and along the way we built a community we made a ton of friends we started a
[2343.52 --> 2351.52]  company and then we realized you know actually maybe we should expand our reach a little bit
[2351.52 --> 2357.84]  right this updater and bundler that we built it's tightly coupled to towery and then you know at crab
[2357.84 --> 2361.84]  nebula we go to conferences we went to four this year or we will have gone to four this year at one of
[2361.84 --> 2369.76]  the conferences somebody rushed the table and was like guys hey can you please upstream the bundler
[2369.76 --> 2375.20]  because i'm using dioxys and like it would be great if i could just bundle and ship that way
[2375.92 --> 2381.04]  and you know we backburnered it because we had to get the the 2.0 we had to make that push to beta
[2381.60 --> 2388.72]  but internally we are working at internally at crab nebula we are working on the proof of concept
[2388.72 --> 2395.76]  research to upstream it and make it available to other projects outside of just pure towery the most
[2395.76 --> 2402.64]  exciting one is slint because you know we found out meeting with slint they have a different target
[2402.64 --> 2408.72]  audience but they are building desktop apps and they're using our low-level libraries tau and rye
[2408.72 --> 2415.12]  so all of a sudden this like the reason why towery became so popular in the first place in my opinion
[2415.12 --> 2422.00]  is because anybody could use the front-end stack if you're react or if you're svelte or if you're
[2422.00 --> 2429.28]  solid or view or angular or choose any one of the hundreds or even rust based ones like you and
[2429.28 --> 2434.80]  dominator and all that you could use this thing that we made for you we gave everybody a gift and
[2434.80 --> 2440.48]  it was like this is great and then we were still in this issue bubble right where we were seeing
[2440.48 --> 2446.08]  problems and comparing ourselves to others and feeling like oh there's competition out there
[2446.08 --> 2455.76]  and by reframing it from hey you know this we don't have to compete with dioxys or slint or electron
[2456.64 --> 2465.36]  we can help them do better things uh do things better right and by by moving out of that tight coupling to
[2465.36 --> 2472.80]  tau ricor um you know we are doing just that and i i think that i mean i haven't had the opportunity to
[2472.80 --> 2482.24]  speak to kore doctor all personally but i i think that this mode of deciding for cooperation instead
[2482.24 --> 2490.24]  of competition is really really rare in i mean an open source maybe but in in in venture capital
[2490.88 --> 2496.40]  type companies very likely yeah the competition helps you understand better who you are but we're
[2496.40 --> 2503.60]  gonna crush them we're gonna like you know and and i i see this i see the world differently i see it as
[2503.60 --> 2509.76]  a way for us to build tools to support other people and if they like our product they're gonna use it if
[2509.76 --> 2513.92]  they like somebody else's product they're gonna use that i have confidence that the products we're
[2513.92 --> 2519.20]  making are great and that people are gonna love them and use them and that's what i sold i didn't sell
[2519.20 --> 2527.04]  my soul to vc or to our wonderful angels i sold this firm belief in the fact that we are not only
[2527.04 --> 2532.32]  doing something great for each other great for the planet great for people's devices but also great for
[2532.32 --> 2538.40]  this ecosystem which is a subset of the markets that we can attract i like that sales pitch i don't see
[2538.40 --> 2544.00]  how you get from there to a web browser but i understand that if you get bored quote unquote then
[2544.00 --> 2548.88]  maybe you're like we need a big fish to fry and i would love to have somebody fry that fish daniel so i
[2548.88 --> 2555.20]  i would also buy that in terms of a massive effort to do that i put my money and time and voice behind
[2555.20 --> 2560.48]  that effort but to me the web browser thing is out of left field daniel i'm not gonna lie like i didn't
[2560.48 --> 2567.04]  ever expect you to say that today so i'm kind of confounded you know what does a web browser need
[2567.04 --> 2572.56]  like what's the one thing that it really needs that we did really well at tellery needs to be updated
[2572.56 --> 2577.84]  every freaking day it needs to be updated needs to be distributed across the planet to every kind of
[2577.84 --> 2584.48]  device every version of device every operating system it needs that kind of reach and you've done
[2584.48 --> 2591.84]  that already seems like the design for the platform that we are rolling out to beta later this fall
[2592.64 --> 2600.56]  early winter is capable of that so we've just kind of accidentally built one of the things we kind of need
[2600.56 --> 2609.60]  to ship a browser okay a research goal is to find a way to make servo window options for towery devs
[2610.24 --> 2616.88]  it's a it's a very interesting almost legendary collaboration right there between agalia and
[2616.88 --> 2621.52]  servo what's that mean servo window options tell us more about what that means exactly well i mean if
[2621.52 --> 2628.08]  you if you remember servo servo was a project from mozilla that was designed to support the work on
[2628.08 --> 2632.40]  firefox actually a lot of the libraries and crates that are there are still in use they never just got
[2632.40 --> 2638.56]  all deprecated but the team was lost to the course of funding or something i don't know and servo sort
[2638.56 --> 2645.28]  of languished for a couple years and about a year ago i don't know maybe in august or september we
[2645.28 --> 2651.04]  started thinking about what it would look like to get servo back on track but it was we didn't have
[2651.04 --> 2657.60]  the big enough team we didn't have any money to do that at the time and then agalia picked up a
[2657.60 --> 2667.60]  partnership with i believe it is future way which is a research and development group of ua company
[2668.16 --> 2675.52]  and they started working on updating all of the other crates on making a unified browser-like
[2675.52 --> 2682.32]  experience in in a window basically getting all the html the css to work i think they currently have
[2682.32 --> 2688.00]  compliance with css2 which is huge really really amazing javascript of course you know that's the
[2688.80 --> 2697.44]  unloved uncle browser and progress is being made there but what we're trying to do is leverage and work
[2697.44 --> 2710.32]  together with the servo group to leverage the servo web view as it were as a target instead of using
[2710.88 --> 2722.88]  webkit gtk wk web view web view 2 on the systems this way we can actually give everybody versions that
[2722.88 --> 2729.52]  they know are the same on these different platforms which is a sticking point for a lot of people and
[2730.24 --> 2735.68]  building a browser isn't something that i'm even committing to right now just to just to see that
[2735.68 --> 2740.16]  very clearly i think that's clear but should it become something that the the group is interested
[2740.16 --> 2747.20]  in in the future well we've laid the groundwork for it right if the pocs turn out if the the
[2747.20 --> 2753.76]  collaborations continue if the funding is made available if the funding is palatable if the
[2754.40 --> 2758.48]  engineers come together you know there's a lot of ifs and a lot of timelines and there's a lot of
[2758.48 --> 2768.64]  project management involved in that kind of thing
[2768.64 --> 2779.28]  what's up friends there's so much going on in the data and machine learning space
[2780.00 --> 2784.16]  it's just hard to keep up did you know the graph technology lets you connect the dots across your
[2784.16 --> 2790.08]  data and ground your llm in actual knowledge to learn about this new approach don't miss nodes on
[2790.08 --> 2795.04]  october 26th at this free online conference developers and data scientists from around the
[2795.04 --> 2800.64]  world will share how they use graph technology for everything from building intelligent apps and apis to
[2800.64 --> 2806.16]  enhancing machine learning and improving data visualizations there are 90 inspiring talks over
[2806.16 --> 2810.88]  24 hours so no matter where you're at in the world you can attend live sessions to register for this
[2810.88 --> 2828.00]  free conference visit neo4j.com slash nodes that's n-e-o the number four j dot com slash nodes
[2828.00 --> 2846.64]  i have one more if for you then an if and a what so if you could assemble all those pieces together
[2846.64 --> 2852.48]  if you could have all those resources then you know what would compel you to build a web browser and
[2852.48 --> 2859.44]  what does it need like what would differentiate the kind of browser you can envision comparatively to
[2859.44 --> 2864.48]  what's out there currently well first of all first and foremost like it absolutely has to be privacy
[2864.48 --> 2873.04]  respecting it has to be securely designed and i know those are two like simple words to just drop into
[2873.04 --> 2878.48]  a sentence like there it's easy to drop those two words into a sentence to say yeah it has to be privacy
[2878.48 --> 2887.60]  centric and secure by design but what that ultimately means is that in the context of local first apps we want
[2888.32 --> 2900.56]  we want i think that a solid approach would be to focus on that aspect of treating the individual as a human
[2900.56 --> 2911.44]  being and not a data point for harvesting their conversations the things that i say uh in a in this
[2911.44 --> 2920.24]  browser they shouldn't be tracked by something slurping up my voice and my face and uh the words i say and
[2920.24 --> 2929.12]  feeding it into some llm that's training on me i think that like those kinds of of privacy centric things
[2929.12 --> 2935.28]  have to be important i think you know ads should just disappear i did an artwork over a decade ago
[2935.28 --> 2942.08]  where somebody made a i think a firefox plugin where you could supply different banner sizes and then
[2942.08 --> 2948.32]  as i gave him a collection of images and then they would replace all the ads in the browser with artwork
[2948.32 --> 2954.80]  i loved that project never forgot about it i think that the way in which we've been
[2954.80 --> 2962.72]  been instrumentalized and forced to use the browser is kind of sad i mean i understand why there's a lot
[2962.72 --> 2970.00]  of big money behind it and big ad tech and um i think that the industry would be very much opposed to
[2970.00 --> 2978.80]  a browser without ads and secure by security i meant that things like your personal identification
[2978.80 --> 2987.28]  your secrets your credit cards your password management is done from of you know from first
[2987.28 --> 2998.72]  principles of preserving security integrity and reliability of data not just for yourself but for your
[2998.72 --> 3004.24]  device right i think that the easy way to look at security is to say oh it's just about my passwords
[3004.24 --> 3012.64]  the reality on the ground is that sometimes we share passwords right like um my mom and and her husband
[3013.28 --> 3020.64]  they had a shared password for their banking until i caught them and i was like no guys you can't do that you
[3020.64 --> 3028.48]  can't share passwords these days and i think that the entire model of passwords pass keys and cryptography
[3028.48 --> 3035.92]  needs uh a revision it needs to be treated in a way that is built is built off of those first principles
[3035.92 --> 3040.64]  that if it's not secure it doesn't ship well those were two aspects of the things that i put on my list
[3040.64 --> 3046.88]  adam of what we want in a web browser and uh i know what the main thing that we all agreed we didn't want
[3046.88 --> 3055.36]  was an ad company living inside of our web browser which is why we have gone elsewhere super interesting
[3055.36 --> 3061.20]  daniel i think if you ever do decide to plant your stake in the ground uh come here first and talk
[3061.20 --> 3068.48]  to us about it we would be happy to help you bootstrap support around that project it's something that
[3069.44 --> 3077.04]  i think the world does need and uh that's cool it just seems like from the towery people it's just it's
[3077.04 --> 3081.76]  interesting i understand that you you gave the reasoning why you've been thinking through this but for me
[3081.76 --> 3087.28]  it is a a bit of a pleasant surprise adam was you expecting him to talk web browsers today with
[3087.28 --> 3092.00]  daniel i didn't think we would no but i think the components you mentioned which you know the signing
[3092.00 --> 3096.00]  the delivery the distribution i agree with everything you said there daniel which you're
[3096.00 --> 3102.32]  you're essentially building the the necessary bones to build the skeleton of a browser and you know
[3102.32 --> 3105.76]  jared we just talked about that now obviously we're not going back to that friends episode but we are
[3105.76 --> 3113.04]  kind of in a way you know i don't use safari because it's got particular privacy or certain
[3113.04 --> 3118.80]  features like that i use it for you know graphics essentially like okay it gives me tabs that shares
[3118.80 --> 3122.64]  with my icloud like it gives me particular features like that not because it's more secure
[3123.20 --> 3128.32]  and i think that the browser you're talking about would be built on fundamentals that are for the people
[3128.32 --> 3133.92]  versus for the the corporation building the thing itself like that to me sounds like amazing foundation
[3133.92 --> 3141.20]  but no jared i was not expecting him well i mean there i'm it would also need more than just that
[3141.20 --> 3146.40]  of course but uh we don't need to talk about oh god it would need perfect visual representation it
[3146.40 --> 3151.76]  would need to have cc css 3 compliance there he goes it would need to have typescript from the get-go
[3151.76 --> 3158.32]  it has to have wasm i mean yeah of course there's a laundry list of things that make a browser a browser
[3158.32 --> 3165.20]  yeah performance right speed if it doesn't have those things that we like ascribe to browsers it's
[3165.20 --> 3169.52]  not a browser sure and i'm not saying baseline browser features i'm saying like it would need i
[3169.52 --> 3175.12]  know you chose the differentiating factors but also i think speed performance battery use these are things
[3175.12 --> 3179.76]  that are also very important alongside privacy and security so there's a lot of things that go into
[3179.76 --> 3186.96]  making a compelling browser if we might just hop that conversation back over to towery one thing that you
[3186.96 --> 3190.96]  said it was probably 15 minutes ago now that i was like this is interesting this is a change in
[3190.96 --> 3196.24]  perspective for you when you were talking about electron and competition and cooperation and vcs and
[3196.24 --> 3201.52]  towery you said that elect you set out to make it a better electron you didn't make that you made
[3201.52 --> 3206.64]  something different and it's better than electron in some ways and it's worse than electron in some ways
[3206.64 --> 3211.04]  and i would love if you just take a few moments to draw that out for people because a lot of us
[3211.68 --> 3216.00]  daniel are still in the point where we're thinking about towery and we're just we're not as far down the
[3216.00 --> 3219.76]  line as you are and you're thinking we're thinking like should i use this or should i use electron
[3219.76 --> 3225.52]  we're thinking about tooling and so that's a very interesting thing is like just that comparison of
[3225.52 --> 3233.60]  the two coming from your mouth about what is electron better at than towery and vice versa i think just to
[3234.24 --> 3241.12]  address it i made some mistakes engaging in this idea that towery is better than electron and
[3241.12 --> 3248.32]  here's why and i even got into a twitter battle with marshall of sound where i proved that we were
[3248.32 --> 3256.32]  better in some way and after reflecting on it i think that that there's a lot of things that electron
[3257.36 --> 3264.56]  brings to the table for example you might consider it's a a bad thing but it does bring a unified
[3264.56 --> 3272.32]  web interface to the major desktop platforms it's the same interface if you look at it in windows it's
[3272.32 --> 3277.68]  going to look the same as it is on on linux so i think that that's something that we don't currently
[3277.68 --> 3287.68]  have you also get an amazing general runtime of node.js bundled with joy that can do anything basically
[3287.68 --> 3295.52]  if you can think it in js your isomorphic skills are going to come in totally handy you're going to
[3295.52 --> 3301.76]  be able to follow documentation that's been built over i mean electrons like almost because it's 10 years
[3301.76 --> 3308.40]  old now like they've been around for a while and a lot of people loved it and grew up on it and made
[3309.04 --> 3316.08]  documentation made the whole tutorials you can learn about it and and not need to step out of your
[3316.08 --> 3320.88]  comfort zone so i think that that's something those are things that that electron has going for it
[3320.88 --> 3327.68]  towery what towery has going for it are you only ship the parts of software that you need to run it
[3327.68 --> 3335.76]  you don't need to ship a generalized runtime so by doing that we can reduce the actual engine size of
[3335.76 --> 3341.36]  a towery app down to five six hundred kilobytes maybe 400 depending on how aggressive you compress
[3341.36 --> 3348.08]  towery is also like i i might get some flack for saying this like people do benchmarks and they
[3348.08 --> 3353.04]  benchmark and they compare and like oh this is a hello world electron app this is a hello world towery
[3353.04 --> 3357.52]  app and this one starts up this fast and this one starts up this fast i know which is better
[3358.16 --> 3366.64]  but ultimately what's happening under the hood what's happening inside of the the core runtime is fewer
[3366.64 --> 3375.84]  sys calls fewer memory like less memory pressure and believe it or not a quicker startup like just the
[3375.84 --> 3384.40]  time it takes to open up a large binary is like linearly longer than opening up a small one it we're
[3384.40 --> 3392.40]  talking milliseconds here i guess you could split feathers but once you start thinking at a global scale of the
[3392.40 --> 3400.80]  the trillions quadrillions of apps that are installed out on the planet do they all need to have an
[3400.80 --> 3409.28]  individual eight or 12 megabyte node.js runtime if you have 10 of them on your on your desktop not so much
[3409.28 --> 3417.04]  and and i i i'm very much convinced that as towery technology gets more it gets adapted by more and more teams
[3417.04 --> 3427.28]  it does become a financial factor once you start to consider massive traction i mean if your app is
[3427.28 --> 3432.88]  downloaded a million times a day the difference between 200 megabytes and 10 megabytes is going to
[3432.88 --> 3439.52]  mean something to somebody in your accounting team and that's just the accounting side of it the transfer
[3439.52 --> 3447.28]  of this massive bundle costs electricity where you're not in a cold fusion world yet maybe at some
[3447.28 --> 3451.84]  point it won't matter anymore and we all have our little fusion packs built into our wrist yeah but
[3451.84 --> 3457.36]  until then we have to conserve electricity we have to protect the planet and every little thing we can do
[3457.36 --> 3462.88]  is important and as like i was saying as towery grows more and more relevant and more and more widely
[3462.88 --> 3471.44]  used beyond the the fig ios and space drives out there it actually concretely positively impacts
[3471.92 --> 3478.56]  the planet now you could argue that the most performant app the most secure app is the one you
[3478.56 --> 3483.76]  don't build but i think that's a that's a red herring i think that people are going to continue to build
[3483.76 --> 3488.72]  apps and we just want to make sure that they're you know sussed out with the right tools what does
[3488.72 --> 3496.80]  towery also do better than than node.js well we can integrate very easily with third languages there's
[3496.80 --> 3503.28]  actually a dynamic library example that lets you rig towery from c plus plus like i was saying before
[3503.28 --> 3514.08]  people are building elixir bindings and python wrappers and php engine backends and that ability for
[3514.08 --> 3521.04]  your preferred piece of back end and front end to come together with the towery components working
[3521.04 --> 3528.96]  as glue is the the really compelling part of it because i'm not gonna lie i wrote a lot of javascript
[3528.96 --> 3535.28]  in my life the thing about javascript is that and it's happened to me i'd be writing something and i
[3535.28 --> 3540.16]  wasn't sure which context i was in if i'm like on the front end of i in the server wait a second how does
[3540.16 --> 3547.52]  this work again you know that that isomorphism really i i lost my place sometimes and i think that
[3547.52 --> 3558.00]  the fact that you can now use rust elixir zinc c plus plus means that that there's a lot more entry
[3558.00 --> 3564.80]  points into the system and you know combined with the fact that the work we've done on the bundler and
[3564.80 --> 3573.52]  updater is going to become more broadly available to others in the ecosystems then i would argue that
[3573.52 --> 3582.56]  the towery project itself is grown beyond itself already i think that it's it's grown to see itself
[3582.56 --> 3588.08]  as a way of supporting the much larger ecosystem that third language thing is really cool i wasn't
[3588.08 --> 3593.44]  aware of that until you told me here earlier i think that's really really interesting and i agree with
[3593.44 --> 3599.60]  you i worked early on in some isomorphic contexts i think with meteor js where i was just as lost and
[3599.60 --> 3604.48]  where was i you know that the benefit of having all javascript really was lost in the fact that i
[3604.48 --> 3609.92]  still didn't know which area of the stack i was currently coding for so i've never had a problem
[3609.92 --> 3614.64]  hopping back between javascript and a different language like contextually especially ones that aren't
[3615.20 --> 3622.80]  dramatically different anyways i always thought that the isomorphic promise was somewhat spurious or
[3623.60 --> 3628.16]  not interesting to me anyway that's a side tangent but yeah third language is really cool it definitely
[3628.16 --> 3633.76]  allows tauri to bust outside of the box that it's currently in interesting you mentioned
[3634.40 --> 3640.56]  user interface to a certain extent as an electron advantage with regards to what they provide what does
[3640.56 --> 3646.64]  tauri provide when it comes to interfaces i was kind of as i was kicking the tires i was expecting kind
[3646.64 --> 3652.48]  of more like widgets and of the things where you can just like give me a file explorer give me a this
[3652.48 --> 3657.36]  thing widget and it would provide that kind of thing it's like none of that's there so is everybody
[3657.36 --> 3664.16]  doing their own thing inside of you know you grab some tailwind css and like start from scratch or how's it
[3664.16 --> 3672.00]  work technically you're right the various ways that people can interact with tauri are it's gonna sound
[3672.00 --> 3680.32]  stupid menus menus are part of the user human interface sure taskbar applications are you know
[3680.32 --> 3684.32]  these you have a little drop down or drop up that gives you a little insight close the app totally
[3684.32 --> 3693.04]  show me the open windows the window itself the copy buffer the keyboard the mouse the pointing device
[3693.04 --> 3700.24]  potentially multi-touch the microphone the camera like those are the the things that we wanted to make
[3700.24 --> 3708.88]  sure we got right and we like we talked about at one point even making a crate for people who want
[3708.88 --> 3716.88]  to play around with those little stoplights on their mac os and we we sort of decided you know if someone
[3716.88 --> 3720.72]  from the community wants to build a plugin we'll we'll support it and actually that's what happened
[3721.60 --> 3729.04]  now a window isn't just a window you know there's transparent windows and i'm being pedantic but it's
[3729.04 --> 3732.96]  important i think there's there's transparent windows there's windows with decorations there's
[3732.96 --> 3738.96]  windows with title bars these are all like classical things that we touch the size of the window the
[3738.96 --> 3746.00]  position of the window the relationship between windows the is the window on top but what do you
[3746.00 --> 3751.28]  put inside the window right so like the way that tauri is built there's two very low level
[3752.16 --> 3757.76]  some people call it deep tech i hate that but call it low level libraries one of them is called tau
[3757.76 --> 3764.08]  and that's actually a fork of the win it project that we've added to keyboard accelerators you know
[3764.08 --> 3772.24]  the command shift plus t or whatever and menus and the windows so we can create the window and all of
[3772.24 --> 3779.84]  this touchy feely stuff with tau and then you got to put something in tau there's a number of things
[3779.84 --> 3784.64]  that we currently offer the primary one is the web view that's what everyone knows it's html css js
[3784.64 --> 3790.96]  compliant up to ecmascript 2020 unless you're on let's see and then to get the less right unless
[3790.96 --> 3802.00]  you're on like mac 10.13 because it's using safari web view and what is it using exactly it's using wk
[3802.00 --> 3814.00]  web view on mac os it's using webkit gtk on linux and it's using web view 2 on windows web view 2 i will
[3814.00 --> 3819.04]  note is based off of edge which is based off of chromium so you do get a chromium like browser
[3819.04 --> 3827.20]  experience with all of the the lovely telemetry that microsoft puts into every app the lovely
[3827.20 --> 3834.96]  telemetry yes then on mac os it's the wk web view which is locked version locked to the safari that you
[3834.96 --> 3843.84]  have installed on your latest update and on linux it's webkit gtk which itself isn't totally feature
[3843.84 --> 3850.80]  uh compliant for example web rtc doesn't work there so we also built two other kinds of windows
[3850.80 --> 3859.12]  so there's an immediate mode gl type window called tauri egui which you have to use rust for uh it's
[3859.12 --> 3867.76]  a real good way around it right now but uh rerun.io is the company behind egui and it provides a javascript
[3867.76 --> 3876.32]  html and css free way of building user interface that we recommend for people who have high security
[3876.32 --> 3881.76]  requirements you know you don't paste your password into a javascript window because you never know what
[3881.76 --> 3886.32]  somebody builds with the node module that you installed so you use one of those and recently
[3887.20 --> 3895.20]  it's not actually been made super public yet but there is also a web gpu window type that you can
[3895.20 --> 3902.80]  create so for example the bevy game group they need the wgpu but they also would like to put some
[3903.36 --> 3911.20]  html type buttons on it so it was a research project with crab nebula we put that together in about a week
[3911.20 --> 3921.20]  so now you have more options and all ideally the future looks like either servo or cef
[3921.20 --> 3927.36]  chromium embedded framework both of them come with caveats and i mean cef would be the
[3928.40 --> 3933.84]  the quick way to do it but then you know we're shipping chromium to everybody again anyway that
[3933.84 --> 3938.16]  in and of itself and making it work on all of these different platforms oh my gosh then there's the
[3938.16 --> 3946.56]  mobile stuff as well has really led to us building these low-level tools and then expecting people who
[3946.56 --> 3953.52]  build front ends to create the kind of user interfaces they need and did you say earlier i
[3953.52 --> 3959.20]  kind of expected that to be the product of crab nebula so like i was thinking more along the tailwind
[3959.20 --> 3965.28]  css is the open source project and then tailwind ui is like the thing that you go and buy and so i was
[3965.28 --> 3970.32]  kind of expecting you did mention productizing some ui stuff but there's a lot different stuff in there i
[3970.32 --> 3976.96]  kind of expected that to be your your product play was all this additional layer on top that provides
[3977.60 --> 3984.40]  cross-platform widgets and cool looking things you can use you know the the doodads and the can i be
[3984.40 --> 3990.80]  honest with you i think that market is right now too small fair i think that that market needs two to
[3990.80 --> 3996.72]  five years to mature maybe two maybe less if we're really successful doing what we're doing but right now
[3996.72 --> 4002.40]  right it's not the time to bring that out i think that there's there's so many options for people to
[4002.40 --> 4008.80]  build stuff that yeah i mean fair enough i always get a laugh at the phrase can i be honest with you
[4008.80 --> 4015.04]  because it's like well what have you been doing this whole time daniel come on i i i meant i know i'm
[4015.04 --> 4021.44]  just kidding jared you know it's those in german they call them fluskel in german they call them fluskel
[4021.44 --> 4026.56]  what's that mean it's just like little flippers ah it's like little things you inject into a sentence
[4026.56 --> 4031.68]  to pass the time while you decide if you're actually going to say the thing you want to say
[4031.68 --> 4037.20]  right no i'm just giving you a hard time good stuff daniel we've talked about a lot is there anything
[4037.20 --> 4043.92]  obvious or big in cart regarding your news and your release 2.0 you mentioned like is this stuff
[4043.92 --> 4049.28]  burgeoning you have a product in the fall like what's coming out what's what else have we talked
[4049.28 --> 4055.60]  about or that you want to reiterate as a as a final thing well i mean right now tauri itself is
[4055.60 --> 4061.68]  close to entering the beta phase the beta phase means we've reached a compliance internally with
[4061.68 --> 4068.00]  our expectations of what it should do basically as soon as we mark tauri as 2.0 beta we're sending
[4068.00 --> 4073.52]  it off to audit it's going to be audited by two companies radically open security on one hand and on
[4073.52 --> 4082.88]  the other hand crab nebula because crab nebula has been auditing tauri since the 1.0 release 1.3 or 4
[4082.88 --> 4088.80]  you know whenever we started the company back in november and once the audit is completed and we've
[4088.80 --> 4097.36]  fixed the findings we will then mark tauri as rc0 give the community a good time to feedback reply
[4097.36 --> 4105.28]  make last minute changes and then we will release tauri 2.0 um i hesitate to give timelines because
[4105.28 --> 4111.04]  audits can find lots of things that you weren't expecting uh but we do expect to keep things speed
[4111.04 --> 4117.36]  we have a blog post about it on the tauri website where we we go into detail about it but the challenges
[4117.36 --> 4123.60]  of an open source community is that it's really hard i mean even with the you know venture-backed group
[4123.60 --> 4130.88]  like we are being involved it's really hard to give the community timelines i'd like to say a certain
[4130.88 --> 4137.20]  date but obviously you know we've learned that you know engineering sometimes just takes the time it
[4137.20 --> 4144.96]  takes but we're closing it on it and it will have mobile so i think we're we're checking off the the
[4144.96 --> 4151.36]  to-do list for for tauri right now well all exciting things daniel we of course hope the best for you
[4151.36 --> 4156.08]  always appreciate you coming on the show and discussing these things big picture little
[4156.08 --> 4163.28]  picture i love how you can go from this from the stars down into the nitty-gritty of web views just
[4163.28 --> 4168.80]  like that so we definitely appreciate your you're our kind of fella we appreciate you coming on and uh
[4168.80 --> 4173.92]  come back anytime especially when you're ready to announce your open source privacy focused browser
[4173.92 --> 4176.96]  project promise to do so thanks daniel
[4176.96 --> 4186.32]  just on the tale of our what do you want from a web browser episode on change like my friends here we
[4186.32 --> 4193.12]  are on this podcast talking about exactly what we all thought made the most sense an open source
[4193.12 --> 4199.68]  privacy focused web browser and daniel's talking about it so we're kind of excited about that are you
[4199.68 --> 4206.64]  at all interested in this coming to fruition if so let us know slack twitter comments
[4206.64 --> 4212.72]  take your flavor whatever works for you coming up tomorrow on change talking friends we invited our
[4212.72 --> 4218.88]  good friend christina warren film girl to talk about the death of physical media as it relates to
[4219.52 --> 4225.44]  netflix dvd shutting down as it relates to the era we're in where streaming is really taking over
[4225.44 --> 4232.48]  and being favored by the studios and everyone else it's a good show it was fun i hope you listen to it
[4232.48 --> 4238.32]  comes out tomorrow and a big thank you to our friends and our partners at fastly fly and type
[4238.32 --> 4247.28]  sense they have our back if you need amazing search an amazing cdn or the best place to host your things
[4247.28 --> 4252.96]  check out fly check out fastly and check out type sense they're all awesome but hey that's it
[4252.96 --> 4266.80]  the show's done we will see you tomorrow
[4266.80 --> 4268.80]  you
[4282.96 --> 4296.80]  you
