[0.00 → 15.68] what's up welcome back this week on the change law we're joined by Daniel Thompson
[15.68 → 20.96] co-founder and core member of kauri it's been a year since we had Daniel on the show
[20.96 → 26.68] he catches us up on all things kauri their continued efforts towards kauri 1.5 which just
[26.68 → 32.62] released the launch of crab nebula and other people pushing the tower ecosystem forward
[32.62 → 39.60] and building on top of it the state of electron versus kauri user interface with kauri and Daniel
[39.60 → 45.48] even surprised us with his idea of creating a web browser a massive thank you to our friends and our
[45.48 → 52.52] partners at fast and fly this podcast got you fast because quickly is fast superfast globally
[52.52 → 58.18] check them out at fastly.com and our friends at fly help us put our app and our database close to our
[58.18 → 64.22] users all over the world with no ops, and they'll do it for you too check them out at fly.io
[64.22 → 79.10] if I gave you a hundred dollars towards your air monitoring would you use it that's the great
[79.10 → 84.46] question we have for you today because century is a long-standing partner of ours a long-standing
[84.46 → 89.92] sponsor of ours, and we love century, and we think you'll love them too so the easiest way to get
[89.92 → 94.70] a hundred bucks towards your century bill is to use our code when you sign up changelog is the code
[94.70 → 99.40] this code gives you a hundred dollars which is basically three months free of their team plan
[99.40 → 105.08] that's on top of their completely free developer plan they also have a really cool sandbox so if you
[105.08 → 108.64] don't know much about century you've never tried it, or you've never played with it, and you don't want
[108.64 → 113.44] to install it right this second, but you want to see how it works on sample data you can use that
[113.44 → 118.26] the sandbox is on their website we'll link it up in the show notes check it out again use the code
[118.26 → 122.64] changelog get a hundred bucks which is basically three months free on their team plan in addition
[122.64 → 132.66] to all the goodness they give you in the free developer plan check them out century.io that's s-e-n-t-r-y.io
[132.66 → 162.48] all right we're here with Daniel Thompson from tower
[162.48 → 167.62] back after about a year and a half we had you on the podcast welcome back Daniel thanks it's really
[167.62 → 172.98] really great to see you guys again one of the main comments we got was how amazing your voice is
[172.98 → 180.24] I was kind of jealous yeah people were jelly of your voice yeah well you know I think that um
[180.24 → 185.78] I've gotten older so it's more raspy now you know I sound like my grandpa all of a sudden
[185.78 → 191.74] fast-forward a year goes by and I'm 10 years older yeah it's been one of those years or what
[191.74 → 200.44] it's been a non-stop year yeah I mean we met I think last uh last summer yeah after the 1.0 was
[200.44 → 207.26] released talked about the plans for the future and I mean I did review the show and I think we're
[207.26 → 215.32] pretty spot on you know this uh this coming soon is going to be the release of the 2.0 which
[215.32 → 223.84] has uh mobile and embedded into it android and iOS I found out that uh tower iOS on the android makes a
[223.84 → 232.52] 8.5 megabyte binary so competitive with React Native and iOS is a little bigger, but you know I think that
[232.52 → 239.18] early adopters also have a lot to learn about how to get things tiny and tiny and I guess
[239.18 → 244.74] it's one of the things that we see on Twitter a lot of people are like yeah my first tower app it's 14
[244.74 → 251.24] megabytes and I'm like did you minify did you put in those uh the special cargo flags for the release
[251.24 → 257.14] and they're like oh no, and then they come back now it's only eight megabytes so I think we've still
[257.14 → 262.22] we've held true to that excellent to hear well for those who didn't listen the first time around
[262.22 → 268.82] that episode is called build tiny multi-platform apps with tower and web tech I remember we had a
[268.82 → 275.04] hard time naming that episode yeah we did because tower is a little bit it's not hard to explain but
[275.04 → 278.98] it's hard to like to put into three words which is we'd like to be in the three to five word range
[278.98 → 286.22] so Daniel for those who heard that but haven't heard much else of tower give the quick explainer so
[286.22 → 291.26] we're all on the same page well I mean first and foremost tower is a community of developers
[291.26 → 295.42] building stuff for developers and the stuff we like to build for developers are tools to
[295.42 → 301.94] help make apps we started out with desktop, and now we're working toward mobile apps, and you can
[301.94 → 307.30] bring any front-end framework you want in a lot of ways it's similar to electron and capacitor
[307.30 → 315.30] but we put a lot of special focus on the security of the framework as well as the ultimate bundle
[315.30 → 321.40] size we want things to be small and performant and not consume a lot of resources so that's how we
[321.40 → 327.32] how we started it and that's how things have been going so you have a lot of sponsors which is awesome
[327.32 → 333.96] I assume we talked to you after right after 1.0 and usually 1.0 is a time when people decide okay
[333.96 → 340.14] I can finally take this thing seriously, and it's usually a boon for adoption have you had a lot of
[340.14 → 346.42] folks building stuff with tower since the release yeah I just recommend looking over at the um
[346.42 → 352.66] awesome tower repo at our GitHub organization, and it's kind of like endless scrolling lots of dev tools
[352.66 → 363.78] lots of games actually things are being built for communication and the rate at which I measure
[363.78 → 370.70] adoption though has changed a little bit over the past year um there are some reasons for that but
[370.70 → 377.68] mostly we're seeing people come in with really innovative questions things that go outside our
[377.68 → 386.08] expectations when we built the original project and in most cases we're finding that it's not necessarily
[386.08 → 392.64] an edge case, but people have to start learning to maybe think differently about how they construct
[392.64 → 399.92] their apps and move heavy lifting to the rust side and use the the the user interface for user
[399.92 → 405.88] interface things and not put so much logic and I think for a lot of you know classically recognized
[405.88 → 410.88] full stack devs it can be kind of complicated because you don't care where it runs it you know
[410.88 → 416.68] on the client in the browser on the cloud at the edge as long as it's running somewhere that's fine but
[416.68 → 422.94] we're trying to provide these highly tuned opportunities, and you know people are making
[422.94 → 428.48] musical instruments they're making drawing tools they're being creative and I think the the the
[428.48 → 435.10] the biggest news out of our ecosystem is recently fig Io which is a developer tool that gives you kind of
[435.10 → 443.50] supercharged command line experience was just acquired by AWS yeah I saw that, and they use uh the
[443.50 → 450.86] windowing and the web viewing libraries of tori so they're part of the tori family and I guess
[450.86 → 457.52] the uptake has been really heartwarming to see, and it's also you know it's early days I think
[457.52 → 466.14] a lot of projects are in stealth uh you know if you look at that awesome uh tori repo I don't know like
[466.14 → 472.36] 10 percent of them are closed source which means people are you know making money selling their
[472.36 → 478.20] products there's ecosystem plays that are being made where people are starting to offer
[478.20 → 485.78] license servers or license services or analytics people are creating integrations with you know
[485.78 → 493.10] sup abase and Airtable and firebase, and you know you're starting to see these projects come in that
[493.10 → 498.48] have a set of requirements and people are solving the problems and I think that's the exciting part
[498.48 → 505.58] that we're at now you know last year when I was here we were really in the issue bubble and the
[505.58 → 514.14] issue bubble in open source is a place where you only hear complaints you only heart problems you only
[514.14 → 521.94] see people struggling with what you've built and over the past year we've started to hear from
[521.94 → 531.88] companies that are using tori internally we've started recognizing oh yeah right um engineers solve
[531.88 → 536.84] problems and if you're behind a corporate firewall you're going to solve your problem one way or the
[536.84 → 542.76] other and yeah I mean that's really awesome to hear just looking at the sponsors listed on the
[542.76 → 547.14] homepage there are lots of big names there as well so I assume they have some sort of interest in the
[547.14 → 553.82] success of the project do you find that the rust we focus a lot on the rust aspect of tori last time
[553.82 → 558.82] around it was just kind of digging into the tool and figuring out how to use it and one thing that
[558.82 → 563.00] you said that stuck with me at that time is you think that this is a nice you didn't say gateway drug
[563.00 → 569.48] but I will say that it's a nice entrance into the rust ecosystem and I wonder you know I've been
[569.48 → 575.78] tinkering a little bit with just the fringes of tori as I found in a use case I've been waiting for a use
[575.78 → 581.36] case to give it a try so I've been doing the getting started and dipping my toe into the water
[581.36 → 587.92] as it were and as a web developer you know full stack web developer whatever you want to call me
[587.92 → 595.80] somewhat intimidating even though nothing seems too dragon-y so far but I'm still just like
[595.80 → 602.78] not so sure about like you said where do I put things what belongs in rust what doesn't
[602.78 → 609.30] etc is that a common refrain are you answering those questions a lot do you think it's been a
[609.30 → 614.86] barrier to adoption because it's an opportunity for rust, but it might be a barrier for tori I think
[614.86 → 620.22] it's both I really think it's both I know that people are learning rust because once you get to a
[620.22 → 626.24] certain point in building your app you're like oh I need to send a message from one window to another
[626.24 → 634.26] window and I have to use the rust bridge to do that or you want to you know do tighter integrations
[634.26 → 643.10] with the cryptographic systems you want to avoid using the database inside the web view so you
[643.10 → 651.70] you kind of have to start thinking about oh I'm going to say it wrong SQL SQLite SQL I don't tell you
[651.70 → 657.08] how to say that the database SQL there you go Richard hip told us how I still can't toe the line
[657.08 → 663.42] but Adam always has it SQLite, and you know to address your question we're seeing a lot more
[663.42 → 671.06] questions come up about using more rust in the background of a tower app than in the foreground
[671.06 → 678.70] of the JavaScript side there are always still people just you know dabbling well look I think that
[678.70 → 684.04] the opportunities that people have to learn new programming languages come with risk and benefits
[684.04 → 689.80] and it's really up to the people to decide what they want to do we've seen both sides of this where
[689.80 → 697.18] people have jumped because rust is hard to learn we've also seen people embrace it and use tower as a
[697.18 → 705.82] way to become a rust engineer so we've seen both and I think that what we've also seen are people
[705.82 → 713.60] who say well look I'm using python already I don't care about rust so open BB they made a python
[713.60 → 718.96] adapter for one of the low-level libraries somebody else just recently posted an elixir
[718.96 → 725.96] kind of binding so you can use a phoenix channels instead of rust people are working on believe it or
[725.96 → 733.24] not a PHP backend so that you can write all your logic at PHP and still get all the benefits of
[733.24 → 739.06] or type rust core and a user interface that can directly access both the rest APIs through its
[739.06 → 748.16] JavaScript or call out to believe it or not PHP JavaScript ideas on the horizon as well so i I think
[748.16 → 755.62] that like what tally itself started out as is one thing and where it's moving I think is another and
[755.62 → 761.76] that is turning into a collection of tools that you can kind of pick and choose how you want to piece
[761.76 → 766.90] them together that's fascinating to hear it sounds like there's enough value there enough
[766.90 → 772.86] interest to when even if rust is a barrier for you there's people that are like look I can work around
[772.86 → 779.36] this particular aspect of tower by building a PHP backend for instance or providing access to elixir
[779.36 → 784.86] because I want to use it so bad and I don't really want to use this part of it so I mean that to me
[784.86 → 791.74] shows quite a bit of interest for people willing to you know break out their code editors and work
[791.74 → 800.68] around or code around these issues that's that's pretty cool, but you have this year as we meet again
[800.68 → 807.24] you have more news obviously the mobile stuff is huge, but you also have news around uh what's behind
[807.24 → 814.96] tower open source strategy funding round there's lots going on there I know you had a very interesting
[814.96 → 819.84] take on open source last time can you tell us what you guys have figured out in terms of making this
[819.84 → 826.62] thing I don't know sustain and thrive it's tricky we actually started a company last year
[826.62 → 834.28] some of us from the tower working group started a company last year in November okay, and it was
[834.28 → 841.10] really important to us that nothing changed from the outside it's still a militantly driven open
[841.10 → 850.04] source community that now is supercharged with a handful of engineers being paid full-time to do the
[850.04 → 857.44] research development and maintenance that a massive project like tower needs and that company is called
[857.44 → 867.16] crab nebula we chose crab nebula because we liked the idea of a place where stars are born a nebula is a
[867.16 → 876.46] a star factory if you will, and we chose crab because well rust the the the icon the avatar if you will
[876.46 → 887.32] is Ferris the little crustacean gustation and now obviously you can't make a pitch to a VC and say we're
[887.32 → 896.28] just going to serve as a charity and donate all of your money to open source things uh would be nice
[896.28 → 904.94] if they work that way maybe but I think that uh we found the perfect VC uh to join us on this trip
[904.94 → 914.40] that's JJ from OSS capital west coast based venture group that only supports early stage open source
[914.40 → 922.36] projects commercial open source projects and through JJ and through years and years of being around
[922.36 → 930.88] we sort of collected an all-star regiment of angels who joined us along the way I could drop all
[930.88 → 936.76] of the names uh maybe you can edit them out or choose the ones you like but I think you know of the
[936.76 → 945.26] almost 30 angels that we have the good dozen that are really relevant um are you know novel radiant
[945.26 → 952.08] from angel list automatic inc the company the investment arm of automatic from WordPress fame
[952.08 → 959.64] Guillermo rank the CEO of oversell Thomas dock the CEO of GitHub uh tom Preston Werner the
[959.64 → 967.30] co-founder the original co-founder of GitHub uh Paul cobblestone from super base Justin Hoffman the
[967.30 → 972.16] former SVP of elastic if I didn't say bob young I'll say his name again because he's amazing
[972.16 → 980.98] but Ahmad mustily was the CEO of stability AI clement de long the co-founder and CEO of hugging face
[980.98 → 988.40] Dave tier the founder of one password Adam Wiggins the co-founder of Heroku Gavin Europa the founder
[988.40 → 995.14] of NCO dB heather meeker if you know heather she's uh not only the general partner of OSS capital
[995.14 → 1003.56] but wrote the book on OSS licensing, and you know we also have a couple of people like uh Cassidy Williams
[1003.56 → 1011.24] who's the CTO of contend you maybe know her as Cassidy also uh times Kumar and I think what
[1011.24 → 1020.18] what drove us to work with this number of angels is getting to know your idols the people that have
[1020.18 → 1025.46] built open source the people who are building open source and people who are poised to build the next
[1025.46 → 1033.40] open source who understand the challenges of not only having a product but also having the machinery
[1033.40 → 1039.68] the understanding and the ability to innovate into products and new products as they come out um
[1039.68 → 1050.66] so that happens and nothing changed at tower I mean we kept on building tower in line with our um
[1050.66 → 1061.32] foundations expectations but behind the scenes um we are working on a few products I mean other than
[1061.32 → 1066.88] investing time in tower we're also auditing tower that's one of the things that we love doing
[1066.88 → 1073.32] actually is auditing people's uh software that they built with tower with rust you know we just
[1073.32 → 1082.28] completed an audit for a company called blue bay eye that uses tower we don't really do custom
[1082.28 → 1090.56] development we do, but we don't like we will pick from uh clients who want to have something done that
[1090.56 → 1095.38] aligns with our research goals that makes sense like we're not just out there cutthroat working
[1095.38 → 1100.66] for half a million dollars because somebody wants to pay us money to build something for them, I mean
[1100.66 → 1105.64] we'd consider it, but it has to align with our research goals things that we want to know things
[1105.64 → 1111.82] that we know that the community needs those are the kinds of uh of customers that we've been looking
[1111.82 → 1119.18] for and been finding we also recognized from the beginning that shipping apps is hard it's really hard
[1119.18 → 1126.24] like I mean anybody can build an app but once you're done how do you distribute it how do you update it
[1126.24 → 1135.94] how do you sign it and for that we're building a platform to empower the people to ship their apps
[1135.94 → 1145.00] like super easy super cheap in some cases totally discounted for open source, and we know that this
[1145.00 → 1151.14] is going to get a little political I don't know if that's okay, but we know that the incumbents uh like
[1151.14 → 1159.30] Microsoft and apple and alphabets and meta and byte dance they have vested interests well maybe less
[1159.30 → 1165.28] byte dance but definitely the platforms they have an interest in keeping a hold over a chokehold
[1165.28 → 1170.76] over the app signing process they keep such a chokehold on it that in my opinion it's not
[1170.76 → 1176.26] talked about enough in the supply chain like that final bit of app signing for GUI apps, and you know
[1176.26 → 1181.46] in some cases even CLI apps it's just like oh yeah apple will take care of that for you, we got you we
[1181.46 → 1186.88] got you come here and just give me your 99 euro or Microsoft changing the game suddenly last
[1186.88 → 1193.88] April saying now you have to get an extended validation dongle or HSM but don't worry you can use our
[1193.88 → 1201.02] super secure never been hacked for azure platform for that google is a little bit less concerned i
[1201.02 → 1207.24] think that anything that impacts their ad business is going to uh be a problem for them but apps on
[1207.24 → 1212.06] devices keeps people on devices keeps them buying devices so I think that that that's okay for them
[1212.06 → 1218.06] but when I hear from people from the tower community that they are having problems signing their apps
[1218.06 → 1223.22] people aren't like some people don't even sign them they just ship their Microsoft apps without a
[1223.22 → 1229.90] developer signature, and they're like people will deal with it and there's no money solution here
[1229.90 → 1236.54] there's no lobbying we can do, but we can in Europe at least get involved with the European commission
[1236.54 → 1247.48] and its platform policy work serving as experts, and you know making sure that these changes
[1247.48 → 1254.66] are respected that other types of app stores can be on their devices other third-party apps can now
[1254.66 → 1263.12] starting in April in the European Union by law have to be landing on these devices, and you know i I feel
[1263.12 → 1271.30] I feel very deeply about empowering the citizen developers out there who don't have the 99 euro or who
[1271.30 → 1279.54] are in a third world so-called Third World country where 99 is just like a month of food, but they still
[1279.54 → 1284.78] can build their apps, but they can't distribute them, and they have no access to these larger markets I find
[1284.78 → 1291.34] that compelling in a very sad way and I think that you know the the mixture of good business good
[1291.34 → 1298.78] politics supporting the community is really in the DNA of crab nebula so much to the point that
[1298.78 → 1304.38] one of our first products that we're going to be bringing out in q4, and you can find out about it
[1304.38 → 1312.72] just by following our socials is a dev tool because debugging anything is hard debugging tower is triple
[1312.72 → 1321.52] hard web has great dev tools apps not so much, and we want people to be able to connect their app to an
[1321.52 → 1326.14] analyzer to figure out where things are going wrong or getting better and i I understand you're thinking
[1326.14 → 1331.76] Daniel this is niche not many people are using tower but the great news is that we're we're
[1331.76 → 1338.48] working together with other partners in the rust ecosystem to define and use emerging standards
[1338.48 → 1344.98] so that the work that we're doing for tower people can be used by at first others in the rust
[1344.98 → 1352.70] ecosystem and later other ecosystems as they get interested in it and i I think the final thing
[1352.70 → 1359.64] that I'd like to point out is that you asked how is this how is this possible how can you keep the
[1359.64 → 1367.96] the energy going the momentum going and in open source projects you generally have like three or
[1367.96 → 1374.18] four models one a company sits on top puts its thumb down it's not even benevolent dictator it's like
[1374.18 → 1380.00] we're doing this now this way we're calling our project open source and later on we can rug pull
[1380.00 → 1388.28] but another one is a benevolent dictator who decides the way the project goes generally takes all the
[1388.28 → 1394.72] funds and other people contribute as they have time people come people go and what we have with
[1394.72 → 1402.86] tower though is really quite compelling because from the core team five of the people are still around
[1402.86 → 1409.70] almost five years later and I think that that's a testament to the fact that we really enjoy doing it
[1409.70 → 1419.60] and yet I don't believe that it should be just the goal of one company in sitting in Malta to finance
[1419.60 → 1426.88] an entire open source project right, and we do have donors and that's amazing I think where things
[1426.88 → 1435.34] are tending toward is toward applying for more systemic grants you know where we apply for funding from
[1435.34 → 1443.34] the European commission from organizations like NL net and potentially even other companies come and recognize
[1443.34 → 1449.26] the value that they've gotten from the community and start giving back I don't know I think that that that's a
[1449.26 → 1456.92] very long, long play expecting people that get something for free to give back to a community that they're not so much
[1456.92 → 1463.40] involved in there's a lot to unpack there at the end of the last show I asked you about venture capital and the
[1463.40 → 1469.32] organization and things that would come from the one point over at least that was about a year ago and you
[1469.32 → 1475.02] kind of tease us a little bit with a topic we like to talk about with core Doctorow choke point capitalism I think
[1475.02 → 1480.86] you're talking about that with app signing I think that's definitely a position of hey if there's an artist
[1480.86 → 1486.34] shipping something there's a choke point at some point that says okay we're going to collect our toll our fee
[1486.34 → 1491.40] and that seems like what one part of your mission then you mentioned the core team and the model of open
[1491.40 → 1497.92] source which I think is interesting I'd love to touch all those obviously but uh maybe focus in on the
[1497.92 → 1502.62] organization itself like remind us what its license as remind us of the organization what has happened
[1502.62 → 1508.70] since one point to sort of formalize I know you mentioned crab nebula what exactly is the model of
[1508.70 → 1513.74] tower right now like how do you compare it to others you mentioned company atop rug polling we've seen
[1513.74 → 1519.38] that more recently and that's fresh and uh it's a fresh wound to the open source community
[1519.38 → 1524.94] yeah absolutely so nothing has changed in the organizational structure of tower itself there
[1524.94 → 1531.58] is still a board of directors there is still an entity held within a Dutch foundation the proper
[1531.58 → 1538.02] name is the tower program within the commons' conservancy all the code is open source Apache to
[1538.02 → 1545.06] MIT dual licensed at your leisure we take potential license violations within our own code base very
[1545.06 → 1552.84] seriously we will investigate those and resolve them a lot of times uh it's a mistake usually it's
[1552.84 → 1558.30] something we can correct actually I think we've always corrected them so to summarize the licenses
[1558.30 → 1567.22] MIT Apache to it is still morally stewarded by the car the commons conservancy and internally
[1567.22 → 1574.70] there is a working group composed of people who elect themselves to join to the working group currently
[1574.70 → 1584.42] there are about 45 members of the working group and I would say about 20 are active and these are not
[1584.42 → 1591.74] all employees of crime nebula I mean there are many them but the majority of the current
[1591.74 → 1598.78] working group members are not, and we even have other companies more or less explicitly involved or with
[1598.78 → 1607.10] or by association one of our board members actually works at Microsoft so from the organizational side of
[1607.10 → 1615.98] the open source projects nothing has changed from the perspective of the company we are donating slash
[1615.98 → 1621.50] allocating I don't know how you want to say it full-time employees to spend all of their working time
[1621.50 → 1630.54] on research developments and maintenance of towering itself of the core pieces of that tech and then
[1631.02 → 1638.78] the products that the company itself makes and distributes are generally going to be at the very
[1638.78 → 1643.18] the least source available we always want to make sure that people can see what we're doing and have faith in
[1643.18 → 1649.18] what we're doing a lot of the things will also be open source MIT Apache 2 as we roll them out
[1651.50 → 1667.18] what's up friends today we have an awesome sponsor dot tech domains, and they're giving this segment away
[1667.18 → 1673.50] to dot tech founders to showcase the amazing things that are being built on a dot tech domain through their
[1673.50 → 1680.32] startups dot tech program dot tech domains are the go-to namespace to build anything in tech and home to the
[1680.32 → 1686.24] world's most innovative startups for example a self-driving AI company that's raised 3.7 billion
[1686.24 → 1694.88] dollars and is building on aurora dot tech the most viral crypto app of 2023 is building on friend dot tech
[1694.88 → 1701.12] and an AI startup backed by Sam Altman and open AI is building on one x dot tech there are thousands of
[1701.12 → 1707.36] companies like this who are taking advantage of dot tech domains to reinforce their brand as tech focused
[1707.36 → 1712.40] and forward-thinking but here's the cool thing instead of just selling domains dot tech domains
[1712.40 → 1717.84] wants to give their users a platform to show the world the amazing things their dot tech startups are
[1717.84 → 1724.32] building so if you're building on a dot tech domain, or you want to simply apply to these startups dot tech
[1724.32 → 1731.12] program by going to startups dot tech slash changelog and filling out the form that way dot tech startups get
[1731.12 → 1736.32] to be in front of thousands of people like on this show, and we get to learn about cool things they're building
[1736.32 → 1743.84] on dot tech again go to startups dot tech slash changelog once again startups dot tech slash changelog
[1758.16 → 1766.16] so crab nebula is the entity which has all these amazing angels correct, and it's starting off as
[1766.16 → 1773.04] consulting and auditing, but that's not the big picture that you drew for these angels that got them
[1773.04 → 1778.56] excited I would imagine it'd be okay to back something like that, but your bigger picture is
[1779.20 → 1786.16] products services seems like some sort of distribution network of you know maybe app stores etc for the
[1786.16 → 1794.56] tower ecosystem is that what you're saying right we see consulting itself as a way to offset the cost of
[1794.56 → 1801.12] R&D yeah you know with the addition of grants coming in that covers our RD costs because we align
[1801.12 → 1809.44] those tasks with r and d and auditing is important because it keeps our security team fresh, and we're
[1809.44 → 1815.04] helping the ecosystem arguably with important projects that people are using by auditing them of
[1815.04 → 1822.88] course neither of those is that you know exponential curve that everybody is dreaming about and I think that the
[1822.88 → 1832.08] the long play for crab nebula is in the services of distributing solving this signing problem one way or the other
[1832.64 → 1841.68] and providing tools that bring joy to the act of development of software again you know and I think that what we're
[1841.68 → 1851.44] already seeing inside the team is we are generally very dissatisfied with products out on the market it's hard for us to find stuff that
[1851.44 → 1859.44] ticks all the boxes and there are a couple of things that we are building internally that we might just spin off into a product
[1859.44 → 1867.68] itself just here you go world buy a seat have fun because I think that the benefit of working with all of these fantastic
[1867.68 → 1876.40] fantastic people is the perspectives that you get when you're analyzing a problem field and seeing
[1876.40 → 1882.88] all of the different ways in which people are criticizing things like oh the security is crap oh the layout
[1882.88 → 1892.48] so is this bootstrap 2.0 you know, and it's a challenge to reel people in to say okay love we're not going to build that
[1892.48 → 1897.28] product right now we're going to solve our own problems on our own time but right now what we are
[1897.28 → 1904.40] building are these dev tools and building out the platform because those are the things that will scale
[1904.96 → 1915.44] especially once you consider that the mechanism for bundling signing and distributing its kind of the same no
[1915.44 → 1922.32] matter what platform you're using you know if it's React Native, or it's electron, or it's any of the
[1922.32 → 1931.84] other competitors or competing systems to towering I guess is still just a bundle and a sign and a ship
[1931.84 → 1939.60] so that move there allows us to also become more than just the towering company I think that that's
[1939.60 → 1945.52] you know that's a risk that we identified really early and as a matter of fact it would technically be
[1945.52 → 1951.76] prevented by the statutes of the open source community no one entity can profit exclusively from
[1952.48 → 1958.00] towering itself we cannot be the towering company, but we can be a towering company we can maybe be
[1958.00 → 1962.96] the best towering company, but we can't be the only towering company, and we are starting to see people
[1963.76 → 1971.12] start building their products around towering as well so if you created a platform for towering you
[1971.12 → 1976.24] would desire other platforms for towering is that what you're saying like if you were like the app store for
[1976.24 → 1981.04] towering apps that did all the bundling and signing and whatever else is involved and allowed you to
[1981.04 → 1987.76] distribute your software to users crab nebula you're not going to be the next apple in that regard is
[1987.76 → 1991.68] that what you're saying like the open source by laws make it so you can't be that because I mean
[1992.24 → 1998.96] given your 100 success we would end up in the same place with we put you in the list we'd be like oh man
[1998.96 → 2004.80] Microsoft and apple and crab nebula like they're all like we would just add you to the list wouldn't we
[2004.80 → 2012.56] okay maybe the ambition is a little bigger maybe the ambition is more to say that the towering
[2012.56 → 2018.00] framework itself would be more aligned with something like JavaScript it's not a product towering is not a
[2018.00 → 2025.52] product in and of itself it's a way to get stuff done like JavaScript like PHP like ruby, and we would
[2025.52 → 2033.36] like to consider ourselves as the people pushing that ecosystem forward and developing on top of it
[2033.36 → 2039.60] but we are not towering because towering can't be a product it can't monetize open source for me
[2040.48 → 2047.52] is gone ahead go off go ahead it's one of the scary parts about this no like I have a lot of friends in
[2047.52 → 2051.36] the industry and I don't want to piss anybody off but I really hate it when licenses get changed or what
[2051.36 → 2058.32] communities break down or when you know corporate interest and greed suddenly redefines community
[2059.12 → 2064.64] and then you find out what it is behind the community you find out oh it was the money
[2064.64 → 2071.36] behind the community if crab nebula, and it's a startup right like startups have a gradient of
[2071.36 → 2078.48] potential success if crab nebula goes down it would suck for crab nebula towering can continue
[2078.48 → 2083.04] kind of right and I think that that's this kind of well I mean if you're funding some of the core
[2083.04 → 2088.32] team members, and you're a major financier behind the scenes of making things happen then obviously
[2088.32 → 2094.00] the economics of supporting it change you're right in the fact that it can continue but if you know
[2094.00 → 2100.24] it's financially stabilized to some degree by the success and the angels that you've you've mentioned so
[2100.24 → 2103.12] there is no way to completely remove yourself up from that so I'm not saying that's a
[2103.68 → 2107.76] strike against you, it's just the truth i i I want to agree with you in principle
[2107.76 → 2115.68] but I'm not going you should because I'm right i I mean i know you're right for
[2115.68 → 2119.68] you and from where you're sitting no from where you're sitting I think it makes a lot of
[2119.68 → 2126.32] sense but the point i was trying to make was and this is something I'm working with the whole
[2126.32 → 2131.36] working group on, and it's not something that's done in software very often I mean look at Emma script
[2131.36 → 2137.44] 2022 it's never ending it's going to be typescript someday the point is I think at some point we
[2137.44 → 2143.84] can actually declare tower is done I'm not saying Kubernetes done but done enough so that all you have
[2143.84 → 2148.32] to do is add little things and there's little bits of maintenance but done, done to the point where the
[2148.32 → 2155.04] features have been completed and maybe that's the point in time where we get to start thinking about
[2155.04 → 2160.96] other stuff we'd like to build I don't know like a browser come on that's too much work is it
[2160.96 → 2166.88] if we lay the groundwork for that over time it might, I don't know I'm not trying to get ahead
[2166.88 → 2171.20] of myself but i we have opinions we just shared our opinions on this do you listen our show often
[2171.20 → 2176.88] Daniel by any chance i do we just went off on this we just went on like what we want in browsers
[2176.88 → 2182.08] me jarred and nick on our talk show Gino and friends so we were just like knee-deep in this so
[2182.08 → 2187.20] we're just talking about an open source browser right that would be amazing so you're teasing us here but
[2187.20 → 2194.16] I mean yeah tower being done when the underlying platforms the deployment targets of tower are never
[2194.16 → 2201.04] finished it seems like okay maintenance but how much of a burden is that I mean iOS 17 just came out
[2201.04 → 2208.16] certainly as the new versions of these desktop and mobile platforms that you're creating apps for
[2208.16 → 2213.12] are changing they're moving targets so tower can't be finished unless it's irrelevant, but maybe you could
[2213.12 → 2218.24] say just major efforts are done as a matter of fact at crab nebula this week we decided we're
[2218.24 → 2223.60] changing research and development changing its name research development and maintenance RDM because
[2223.60 → 2229.20] maintenance is that it's like that part of R&D that I think people forget like let's make a brand new
[2229.20 → 2236.32] framework and call it new and like rage on all the things that everyone else thinks is a good thing
[2236.32 → 2245.68] and no I mean right now in the RDM department we are working on a grant from nonet together with the
[2245.68 → 2255.76] awesome folks over at Amalia to verify that we can use servo as a web view target for tower apps
[2256.56 → 2263.84] with early success seems quite actually quite good already for the short time that the Amalia team has
[2263.84 → 2270.40] taken up the helm of working on servo, and it's a long future and at some point people get bored and
[2270.40 → 2276.08] they start having silly ideas and I'm not saying we will build a browser I'm not saying we won't
[2276.72 → 2282.72] I do know that it's a massive undertaking an open source browser is going to require a ton of stakeholders
[2282.72 → 2292.56] a ton of specialists for a very long time and hey we're not raising money right now but I think that if
[2292.56 → 2298.48] you were to do something like that you would definitely have to have like the entire EU behind
[2298.48 → 2303.04] you'd have to have the European commission behind you, you'd have to have more than just money
[2303.04 → 2310.64] you need the charm and the goodwill and I mean the drive kind of comes for free because otherwise
[2310.64 → 2315.60] we wouldn't be talking about it but I don't know do you guys remember our first conversation when I told
[2315.60 → 2321.60] you I've always kind of been interested in building tools yeah and for me one of the
[2322.64 → 2328.64] interesting side effects about working with tower is that Lucas and I started way back in the day and
[2328.64 → 2332.48] we thought we were going to make a better electron we haven't gotten there yet electron is better in
[2332.48 → 2338.08] a number of ways I'll say it here tower is better in a number of ways it's a different thing, but that's
[2338.08 → 2343.52] what we started out to do and along the way we built a community we made a ton of friends we started a
[2343.52 → 2351.52] company, and then we realized you know actually maybe we should expand our reach a little bit
[2351.52 → 2357.84] right this updater and bundler that we built it's tightly coupled to tower, and then you know at crab
[2357.84 → 2361.84] nebula we go to conferences we went to four this year, or we will have gone to four this year at one of
[2361.84 → 2369.76] the conferences somebody rushed the table and was like guys hey can you please upstream the bundler
[2369.76 → 2375.20] because I'm using Deoxys and like it would be great if I could just bundle and ship that way
[2375.92 → 2381.04] and you know we backordered it because we had to get the 2.0 we had to make that push to beta
[2381.60 → 2388.72] but internally we are working at internally at crab nebula we are working on the proof of concept
[2388.72 → 2395.76] research to upstream it and make it available to other projects outside just pure tower the most
[2395.76 → 2402.64] exciting one is saint because you know we found out meeting with saint they have a different target
[2402.64 → 2408.72] audience, but they are building desktop apps, and they're using our low-level libraries tau and rye
[2408.72 → 2415.12] so all of a sudden this like the reason why tower became so popular in the first place in my opinion
[2415.12 → 2422.00] is because anybody could use the front-end stack if you're reacted or if you're svelte or if you're
[2422.00 → 2429.28] solid or view or angular or choose any one of the hundreds or even rust based ones like you and
[2429.28 → 2434.80] dominator and all that you could use this thing that we made for you, we gave everybody a gift and
[2434.80 → 2440.48] it was like this is great, and then we were still in this issue bubble right where we were seeing
[2440.48 → 2446.08] problems and comparing ourselves to others and feeling like oh there's competition out there
[2446.08 → 2455.76] and by reframing it from hey you know this we don't have to compete with Deoxys or saint or electron
[2456.64 → 2465.36] we can help them do better things uh do things better right and by moving out of that tight coupling to
[2465.36 → 2472.80] tau Rico um you know we are doing just that and i I think that I mean I haven't had the opportunity to
[2472.80 → 2482.24] speak to chore doctor all personally but i I think that this mode of deciding for cooperation instead
[2482.24 → 2490.24] of competition is really, really rare in I mean an open source maybe but in in in venture capital
[2490.88 → 2496.40] type companies very likely yeah the competition helps you understand better who you are, but we're
[2496.40 → 2503.60] going to crush them we're going to like you know and i I see this I see the world differently I see it as
[2503.60 → 2509.76] a way for us to build tools to support other people and if they like our product they're going to use it if
[2509.76 → 2513.92] they like somebody else's product they're going to use that I have confidence that the products we're
[2513.92 → 2519.20] making are great and that people are going to love them and use them and that's what I sold I didn't sell
[2519.20 → 2527.04] my soul to VC or to our wonderful angels I sold this firm belief in the fact that we are not only
[2527.04 → 2532.32] doing something great for each other great for the planet great for people's devices but also great for
[2532.32 → 2538.40] this ecosystem which is a subset of the markets that we can attract I like that sales pitch I don't see
[2538.40 → 2544.00] how you get from there to a web browser but I understand that if you get bored quote unquote then
[2544.00 → 2548.88] maybe you're like we need a big fish to fry and I would love to have somebody fry that fish Daniel so i
[2548.88 → 2555.20] I would also buy that in terms of a massive effort to do that I put my money and time and voice behind
[2555.20 → 2560.48] that effort but to me the web browser thing is out of left field Daniel I'm not gonna lie like I didn't
[2560.48 → 2567.04] ever expect you to say that today so I'm kind of confounded you know what does a web browser need
[2567.04 → 2572.56] like what's the one thing that it really needs that we did really well at teller needs to be updated
[2572.56 → 2577.84] every freaking day it needs to be updated needs to be distributed across the planet to every kind of
[2577.84 → 2584.48] device every version of device every operating system it needs that kind of reach, and you've done
[2584.48 → 2591.84] that already seems like the design for the platform that we are rolling out to beta later this fall
[2592.64 → 2600.56] early winter is capable of that so we've just kind of accidentally built one of the things we kind of need
[2600.56 → 2609.60] to ship a browser okay a research goal is to find a way to make servo window options for tower devs
[2610.24 → 2616.88] it's an it's a very interesting almost legendary collaboration right there between Amalia and
[2616.88 → 2621.52] servo what's that mean servo window options tell us more about what that means exactly well I mean if
[2621.52 → 2628.08] you if you remember servo was a project from Mozilla that was designed to support the work on
[2628.08 → 2632.40] Firefox actually a lot of the libraries and crates that are there are still in use they never just got
[2632.40 → 2638.56] all deprecated, but the team was lost to the course of funding or something I don't know and servo sort
[2638.56 → 2645.28] of languished for a couple of years and about a year ago I don't know maybe in August or September we
[2645.28 → 2651.04] started thinking about what it would look like to get servo back on track, but it was we didn't have
[2651.04 → 2657.60] the big enough team we didn't have any money to do that at the time and then Amalia picked up a
[2657.60 → 2667.60] partnership with I believe it is a future way which is a research and development group of UA company
[2668.16 → 2675.52] and they started working on updating all the other crates on making a unified browser-like
[2675.52 → 2682.32] experience in a window basically getting all the HTML the CSS to work I think they currently have
[2682.32 → 2688.00] compliance with css2 which is huge really, really amazing JavaScript of course you know that's the
[2688.80 → 2697.44] unloved uncle browser and progress is being made there but what we're trying to do is leverage and work
[2697.44 → 2710.32] together with the servo group to leverage the servo web view as it were as a target instead of using
[2710.88 → 2722.88] WebKit GTK we web view 2 on the systems this way we can actually give everybody versions that
[2722.88 → 2729.52] they know are the same on these different platforms which is a sticking point for a lot of people and
[2730.24 → 2735.68] building a browser isn't something that I'm even committing to right now just to see that
[2735.68 → 2740.16] very clearly I think that's clear but should it become something that the group is interested
[2740.16 → 2747.20] in the future well we've laid the groundwork for it right if the POCs turn out if the
[2747.20 → 2753.76] collaborations continue if the funding is made available if the funding is palatable if the
[2754.40 → 2758.48] engineers come together you know there are a lot of ifs and a lot of timelines and there's a lot of
[2758.48 → 2768.64] project management involved in that kind of thing
[2768.64 → 2779.28] what's up friends there's so much going on in the data and machine learning space
[2780.00 → 2784.16] it's just hard to keep up did you know the graph technology lets you connect the dots across your
[2784.16 → 2790.08] data and ground your LLM in actual knowledge to learn about this new approach don't miss nodes on
[2790.08 → 2795.04] October 26th at this free online conference developers and data scientists from around the
[2795.04 → 2800.64] world will share how they use graph technology for everything from building intelligent apps and APIs to
[2800.64 → 2806.16] enhancing machine learning and improving data visualizations there are 90 inspiring talks over
[2806.16 → 2810.88] 24 hours so no matter where you're at in the world you can attend live sessions to register for this
[2810.88 → 2828.00] free conference visit neo4j.com slash nodes that's n-e-o the number four j dot com slash nodes
[2828.00 → 2846.64] I have one more if for you then an if and a what so if you could assemble all those pieces together
[2846.64 → 2852.48] if you could have all those resources then you know what would compel you to build a web browser and
[2852.48 → 2859.44] what does it need like what would differentiate the kind of browser you can envision comparatively to
[2859.44 → 2864.48] what's out there currently well first first and foremost like it absolutely has to be privacy
[2864.48 → 2873.04] respecting it has to be securely designed and I know those are two like simple words to just drop into
[2873.04 → 2878.48] a sentence like there it's easy to drop those two words into a sentence to say yeah it has to be privacy
[2878.48 → 2887.60] centric and secure by design but what that ultimately means is that in the context of local first apps we want
[2888.32 → 2900.56] we want I think that a solid approach would be to focus on that aspect of treating the individual as a human
[2900.56 → 2911.44] being and not a data point for harvesting their conversations the things that I say uh in an in this
[2911.44 → 2920.24] browser they shouldn't be tracked by something slurping up my voice and my face and uh the words I say and
[2920.24 → 2929.12] feeding it into some LLM that's training on me, I think that like those kinds of privacy centric things
[2929.12 → 2935.28] have to be important I think you know ads should just disappear I did an artwork over a decade ago
[2935.28 → 2942.08] where somebody made an I think a Firefox plugin where you could supply different banner sizes and then
[2942.08 → 2948.32] as I gave him a collection of images, and then they would replace all the ads in the browser with artwork
[2948.32 → 2954.80] I loved that project never forgot about it, I think that the way in which we've been
[2954.80 → 2962.72] been instrumentalized and forced to use the browser is kind of sad I mean I understand why there's a lot
[2962.72 → 2970.00] of big money behind it and big ad tech and um I think that the industry would be very much opposed to
[2970.00 → 2978.80] a browser without ads and secure by security I meant that things like your personal identification
[2978.80 → 2987.28] your secrets your credit cards your password management is done from of you know from first
[2987.28 → 2998.72] principles of preserving security integrity and reliability of data not just for yourself but for your
[2998.72 → 3004.24] device right I think that the easy way to look at security is to say oh it's just about my passwords
[3004.24 → 3012.64] the reality on the ground is that sometimes we share passwords right like um my mom and her husband
[3013.28 → 3020.64] they had a shared password for their banking until I caught them and I was like no guys you can't do that you
[3020.64 → 3028.48] can't share passwords these days and I think that the entire model of passwords passes keys and cryptography
[3028.48 → 3035.92] needs uh a revision it needs to be treated in a way that is built off of those first principles
[3035.92 → 3040.64] that if it's not secure it doesn't ship well those were two aspects of the things that I put on my list
[3040.64 → 3046.88] Adam of what we want in a web browser and uh I know what the main thing that we all agreed we didn't want
[3046.88 → 3055.36] was an ad company living inside our web browser which is why we have gone elsewhere fascinating
[3055.36 → 3061.20] Daniel I think if you ever do decide to plant your stake in the ground uh come here first and talk
[3061.20 → 3068.48] to us about it, we would be happy to help you bootstrap support around that project it's something that
[3069.44 → 3077.04] I think the world does need and uh that's cool it just seems like from the tower people it's just it's
[3077.04 → 3081.76] interesting I understand that you gave the reasoning why you've been thinking through this but for me
[3081.76 → 3087.28] it is a bit of a pleasant surprise Adam was you expecting him to talk web browsers today with
[3087.28 → 3092.00] Daniel I didn't think we would no but I think the components you mentioned which you know the signing
[3092.00 → 3096.00] the delivery the distribution I agree with everything you said there Daniel which you're
[3096.00 → 3102.32] you're essentially building the necessary bones to build the skeleton of a browser, and you know
[3102.32 → 3105.76] jarred we just talked about that now obviously we're not going back to that friends episode, but we are
[3105.76 → 3113.04] kind of in a way you know I don't use safari because it's got particular privacy or certain
[3113.04 → 3118.80] features like that I use it for you know graphics essentially like okay it gives me tabs that shares
[3118.80 → 3122.64] with my iCloud like it gives me particular features like that not because it's more secure
[3123.20 → 3128.32] and I think that the browser you're talking about would be built on fundamentals that are for the people
[3128.32 → 3133.92] versus for the corporation building the thing itself like that to me sounds like amazing foundation
[3133.92 → 3141.20] but no jarred I was not expecting him well I mean there I'm it would also need more than just that
[3141.20 → 3146.40] of course but uh we don't need to talk about oh god it would need perfect visual representation it
[3146.40 → 3151.76] would need to have cc'd CSS 3 compliance there he goes it would need to have typescript from the get-go
[3151.76 → 3158.32] it has to have Wasm I mean yeah of course there's a laundry list of things that make a browser
[3158.32 → 3165.20] yeah performance right speed if it doesn't have those things that we like to ascribe to browsers it's
[3165.20 → 3169.52] not a browser sure and I'm not saying baseline browser features I'm saying like it would need i
[3169.52 → 3175.12] know you chose the differentiating factors but also I think speed performance battery use these are things
[3175.12 → 3179.76] that are also very important alongside privacy and security, so there are a lot of things that go into
[3179.76 → 3186.96] making a compelling browser if we might just hop that conversation back over to tower one thing that you
[3186.96 → 3190.96] said it was probably 15 minutes ago now that I was like this is interesting this is a change in
[3190.96 → 3196.24] perspective for you when you were talking about electron and competition and cooperation and VCS and
[3196.24 → 3201.52] tower you said that elect you set out to make it a better electron you didn't make that you made
[3201.52 → 3206.64] something different, and it's better than electron in some ways, and it's worse than electron in some ways
[3206.64 → 3211.04] and I would love if you just take a few moments to draw that out for people because a lot of us
[3211.68 → 3216.00] Daniel are still in the point where we're thinking about tower and we're just we're not as far down the
[3216.00 → 3219.76] line as you are, and you're thinking we're thinking like should I use this or should I use electron
[3219.76 → 3225.52] we're thinking about tooling and so that's a very interesting thing is like just that comparison of
[3225.52 → 3233.60] the two coming from your mouth about what is electron better at than tower and vice versa I think just to
[3234.24 → 3241.12] address it I made some mistakes engaging in this idea that tower is better than electron and
[3241.12 → 3248.32] here's why and I even got into a twitter battle with Marshall of sound where I proved that we were
[3248.32 → 3256.32] better in some way and after reflecting on it, I think that there are a lot of things that electron
[3257.36 → 3264.56] brings to the table for example you might consider it's a bad thing, but it does bring a unified
[3264.56 → 3272.32] web interface to the major desktop platforms it's the same interface if you look at it in windows it's
[3272.32 → 3277.68] going to look the same as it is on Linux so I think that that's something that we don't currently
[3277.68 → 3287.68] have you also get an amazing general runtime of node.js bundled with joy that can do anything basically
[3287.68 → 3295.52] if you can think it in JS your isomorphic skills are going to come in totally handy you're going to
[3295.52 → 3301.76] be able to follow documentation that's been built over I mean electrons like almost because it's 10 years
[3301.76 → 3308.40] old now like they've been around for a while and a lot of people loved it and grew up on it and made
[3309.04 → 3316.08] documentation made the whole tutorials you can learn about it and not need to step out of your
[3316.08 → 3320.88] comfort zone so I think that that's something those are things that that electron has going for it
[3320.88 → 3327.68] tower what tower has going for it are you only ship the parts of software that you need to run it
[3327.68 → 3335.76] you don't need to ship a generalized runtime so by doing that we can reduce the actual engine size of
[3335.76 → 3341.36] a tower app down to five six hundred kilobytes maybe 400 depending on how aggressive you compress
[3341.36 → 3348.08] tower is also like i I might get some flack for saying this like people do benchmarks and they
[3348.08 → 3353.04] benchmark, and they compare and like oh this is a hello world electron app this is a hello world tower
[3353.04 → 3357.52] app and this one starts up this fast and this one starts up this fast I know which is better
[3358.16 → 3366.64] but ultimately what's happening under the hood what's happening inside the core runtime is fewer
[3366.64 → 3375.84] says calls fewer memory like less memory pressure and believe it or not a quicker startup like just the
[3375.84 → 3384.40] time it takes to open up a large binary is like linearly longer than opening up a small one if we're
[3384.40 → 3392.40] talking milliseconds here I guess you could split feathers but once you start thinking at a global scale of the
[3392.40 → 3400.80] the trillions quadrillions of apps that are installed out on the planet do they all need to have an
[3400.80 → 3409.28] individual eight or 12 megabyte node.js runtime if you have 10 of them on your desktop not so much
[3409.28 → 3417.04] and i i I'm very much convinced that as tower technology gets more it gets adapted by more and more teams
[3417.04 → 3427.28] it does become a financial factor once you start to consider massive traction I mean if your app is
[3427.28 → 3432.88] downloaded a million times a day the difference between 200 megabytes and 10 megabytes is going to
[3432.88 → 3439.52] mean something to somebody in your accounting team and that's just the accounting side of it the transfer
[3439.52 → 3447.28] of this massive bundle costs electricity where you're not in a cold fusion world yet maybe at some
[3447.28 → 3451.84] point it won't matter anymore, and we all have our little fusion packs built into our wrist yeah but
[3451.84 → 3457.36] until then we have to conserve electricity we have to protect the planet and every little thing we can do
[3457.36 → 3462.88] is important and as like I was saying as tower grows more and more relevant and more and more widely
[3462.88 → 3471.44] used beyond the fig iOS and space drives out there it actually concretely positively impacts
[3471.92 → 3478.56] the planet now you could argue that the most performant app the most secure app is the one you
[3478.56 → 3483.76] don't build but I think that's a that's a red herring I think that people are going to continue to build
[3483.76 → 3488.72] apps, and we just want to make sure that they're you know Sussex out with the right tools what does
[3488.72 → 3496.80] tower also do better than node.js well we can integrate very easily with third languages there's
[3496.80 → 3503.28] actually a dynamic library example that lets you rig tower from c plus like I was saying before
[3503.28 → 3514.08] people are building elixir bindings and python wrappers and PHP engine backends and that ability for
[3514.08 → 3521.04] your preferred piece of back end and front end to come together with the tower components working
[3521.04 → 3528.96] as glue is the really compelling part of it because I'm not going to lie I wrote a lot of JavaScript
[3528.96 → 3535.28] in my life the thing about JavaScript is that, and it's happened to me, I'd be writing something and i
[3535.28 → 3540.16] wasn't sure which context I was in if I'm like on the front end of i in the server wait a second how does
[3540.16 → 3547.52] this work again you know that that isomorphism really i I lost my place sometimes and I think that
[3547.52 → 3558.00] the fact that you can now use rust elixir zinc c plus means that there's a lot more entry
[3558.00 → 3564.80] points into the system, and you know combined with the fact that the work we've done on the bundler and
[3564.80 → 3573.52] updater is going to become more broadly available to others in the ecosystems then I would argue that
[3573.52 → 3582.56] the tower project itself is grown beyond itself already I think that it's its grown to see itself
[3582.56 → 3588.08] as a way of supporting the much larger ecosystem that third language thing is really cool I wasn't
[3588.08 → 3593.44] aware of that until you told me here earlier I think that's really, really interesting and I agree with
[3593.44 → 3599.60] you I worked early on in some isomorphic contexts I think with meteor JS where I was just as lost and
[3599.60 → 3604.48] where was I you know that the benefit of having all JavaScript really was lost in the fact that i
[3604.48 → 3609.92] still didn't know which area of the stack I was currently coding for so I've never had a problem
[3609.92 → 3614.64] hopping back between JavaScript and a different language like contextually especially ones that aren't
[3615.20 → 3622.80] dramatically different anyway I always thought that the isomorphic promise was somewhat spurious or
[3623.60 → 3628.16] not interesting to me anyway that's a side tangent, but yeah third language is really cool it definitely
[3628.16 → 3633.76] allows kauri to bust outside the box that it's currently in interesting you mentioned
[3634.40 → 3640.56] user interface to a certain extent as an electron advantage in regard to what they provide what does
[3640.56 → 3646.64] kauri provide when it comes to interfaces I was kind of as I was kicking the tires I was expecting kind
[3646.64 → 3652.48] of more like widgets and of the things where you can just like give me a file explorer give me a
[3652.48 → 3657.36] thing widget, and it would provide that kind of thing it's like none of that's there so is everybody
[3657.36 → 3664.16] doing their own thing inside of you know you grab some tailwind CSS and like start from scratch or how's it
[3664.16 → 3672.00] work technically you're right the various ways that people can interact with kauri are it's going to sound
[3672.00 → 3680.32] stupid menus are part of the user human interface sure taskbar applications are you know
[3680.32 → 3684.32] these you have a little drop-down or drop up that gives you a little insight close the app totally
[3684.32 → 3693.04] show me the open windows the window itself the copy buffer the keyboard the mouse the pointing device
[3693.04 → 3700.24] potentially multitouch the microphone the camera like those are the things that we wanted to make
[3700.24 → 3708.88] sure we got right, and we like we talked about at one point even making a crate for people who want
[3708.88 → 3716.88] to play around with those little stoplights on their macOS and we sort of decided you know if someone
[3716.88 → 3720.72] from the community wants to build a plugin we'll, we'll support it and actually that's what happened
[3721.60 → 3729.04] now a window isn't just a window you know there's transparent windows and I'm being pedantic, but it's
[3729.04 → 3732.96] important I think there's there are transparent windows there are windows with decorations there's
[3732.96 → 3738.96] windows with title bars these are all like classical things that we touch the size of the window the
[3738.96 → 3746.00] position of the window the relationship between windows the is the window on top but what do you
[3746.00 → 3751.28] put inside the window right so like the way that kauri is built there's two very low level
[3752.16 → 3757.76] some people call it deep tech I hate that but call it low level libraries one of them is called tau
[3757.76 → 3764.08] and that's actually a fork of the win it projects that we've added to keyboard accelerators you know
[3764.08 → 3772.24] the command shift plus t or whatever and menus and the windows so we can create the window and all of
[3772.24 → 3779.84] this touchy-feely stuff with tau, and then you got to put something in tau there are a number of things
[3779.84 → 3784.64] that we currently offer the primary one is the web view that's what everyone knows it's HTML CSS JS
[3784.64 → 3790.96] compliant up to ECMAScript 2020 unless you're on let's see and then to get the less right unless
[3790.96 → 3802.00] you're on like Mac 10.13 because it's using safari web view and what is it using exactly it's using we
[3802.00 → 3814.00] web view on macOS it's using WebKit GTK on Linux, and it's using web view 2 on windows web view 2 I will
[3814.00 → 3819.04] note is based off of edge which is based off of chromium so you do get a chromium like browser
[3819.04 → 3827.20] experience with all of the lovely telemetry that Microsoft puts into every app the lovely
[3827.20 → 3834.96] telemetry yes than on macOS it's the we web view which is locked version locked to the safari that you
[3834.96 → 3843.84] have installed on your latest update and on Linux it's WebKit GTK which itself isn't totally feature
[3843.84 → 3850.80] uh compliant for example web RTC doesn't work there so we also built two other kinds of windows
[3850.80 → 3859.12] so there's an immediate mode GL type window called kauri GUI which you have to use rust for uh it's
[3859.12 → 3867.76] a real good way around it right now but uh rerun.io is the company behind GUI, and it provides a JavaScript
[3867.76 → 3876.32] HTML and CSS free way of building user interface that we recommend for people who have high security
[3876.32 → 3881.76] requirements you know you don't paste your password into a JavaScript window because you never know what
[3881.76 → 3886.32] somebody builds with the node module that you installed so you use one of those and recently
[3887.20 → 3895.20] it's not actually been made super public yet but there is also a web GPU window type that you can
[3895.20 → 3902.80] create so for example the bevy game group they need the GPU, but they also would like to put some
[3903.36 → 3911.20] HTML type buttons on it so it was a research project with crab nebula we put that together in about a week
[3911.20 → 3921.20] so now you have more options and all ideally the future looks like either servo or CEF
[3921.20 → 3927.36] chromium embedded framework both of them come with caveats and I mean CEF would be the
[3928.40 → 3933.84] the quick way to do it, but then you know we're shipping chromium to everybody again anyway that
[3933.84 → 3938.16] in and of itself and making it work on all of these different platforms oh my gosh then there's the
[3938.16 → 3946.56] mobile stuff as well has really led to us building these low-level tools and then expecting people who
[3946.56 → 3953.52] build front ends to create the kind of user interfaces they need and did you say earlier i
[3953.52 → 3959.20] kind of expected that to be the product of crab nebula so like I was thinking more along the tailwind
[3959.20 → 3965.28] CSS is the open source project and then tailwind UI is like the thing that you go and buy, and so I was
[3965.28 → 3970.32] kind of expecting you did mention productizing some UI stuff, but there's a lot of different stuff in there i
[3970.32 → 3976.96] kind of expected that to be your product play was all this additional layer on top that provides
[3977.60 → 3984.40] cross-platform widgets and cool looking things you can use you know the doodads and the can I be
[3984.40 → 3990.80] honest with you, I think that market is right now too small fair I think that that market needs two to
[3990.80 → 3996.72] five years to mature maybe two maybe less if we're really successful doing what we're doing but right now
[3996.72 → 4002.40] right it's not the time to bring that out I think that there 's's so many options for people to
[4002.40 → 4008.80] build stuff that yeah I mean fair enough I always get a laugh at the phrase can I be honest with you
[4008.80 → 4015.04] because it's like well what have you been doing this whole time Daniel come on i i I meant I know I'm
[4015.04 → 4021.44] just kidding jarred you know it's those in German they call them flushed in German they call them flushed
[4021.44 → 4026.56] what's that mean it's just like little flippers ah it's like little things you inject into a sentence
[4026.56 → 4031.68] to pass the time while you decide if you're actually going to say the thing you want to say
[4031.68 → 4037.20] right no I'm just giving you a hard time good stuff Daniel we've talked about a lot is there anything
[4037.20 → 4043.92] obvious or big in cart regarding your news and your release 2.0 you mentioned like is this stuff
[4043.92 → 4049.28] burgeoning you have a product in the fall like what's coming out what's what else have we talked
[4049.28 → 4055.60] about or that you want to reiterate as a final thing well I mean right now kauri itself is
[4055.60 → 4061.68] close to entering the beta phase the beta phase means we've reached a compliance internally with
[4061.68 → 4068.00] our expectations of what it should do basically as soon as we mark kauri as 2.0 beta we're sending
[4068.00 → 4073.52] it off to audit it's going to be audited by two companies radically open security on one hand and on
[4073.52 → 4082.88] the other hand crab nebula because crab nebula has been auditing kauri since the 1.0 release 1.3 or 4
[4082.88 → 4088.80] you know whenever we started the company back in November and once the audit is completed, and we've
[4088.80 → 4097.36] fixed the findings we will then mark kauri as rc0 give the community a good time to feedback reply
[4097.36 → 4105.28] make last minute changes, and then we will release kauri 2.0 um I hesitate to give timelines because
[4105.28 → 4111.04] audits can find lots of things that you weren't expecting uh, but we do expect to keep things speed
[4111.04 → 4117.36] we have a blog post about it on the kauri website where we go into detail about it but the challenges
[4117.36 → 4123.60] of an open source community is that it's really hard I mean even with the know venture-backed group
[4123.60 → 4130.88] like we are being involved it's really hard to give the community timelines I'd like to say a certain
[4130.88 → 4137.20] date, but obviously you know we've learned that you know engineering sometimes just takes the time it
[4137.20 → 4144.96] takes, but we're closing it on it, and it will have mobile so I think we're we're checking off the
[4144.96 → 4151.36] to-do list for kauri right now well all exciting things Daniel we of course hope the best for you
[4151.36 → 4156.08] always appreciate you coming on the show and discussing these things big picture little
[4156.08 → 4163.28] picture I love how you can go from this from the stars down into the nitty-gritty of web views just
[4163.28 → 4168.80] like that so we definitely appreciate your you're our kind of fella we appreciate you coming on and uh
[4168.80 → 4173.92] come back anytime especially when you're ready to announce your open source privacy focused browser
[4173.92 → 4176.96] project promise to do so thanks Daniel
[4176.96 → 4186.32] just on the tale of our what do you want from a web browser episode on change like my friends here we
[4186.32 → 4193.12] are on this podcast talking about exactly what we all thought made the most sense an open source
[4193.12 → 4199.68] privacy focused web browser and Daniel's talking about it so we're kind of excited about that are you
[4199.68 → 4206.64] at all interested in this coming to fruition if so let us know slack twitter comments
[4206.64 → 4212.72] take your flavour whatever works for you coming up tomorrow on change talking friends we invited our
[4212.72 → 4218.88] good friend Christina warren film girl to talk about the death of physical media as it relates to
[4219.52 → 4225.44] Netflix DVD shutting down as it relates to the era we're in where streaming is really taking over
[4225.44 → 4232.48] and being favoured by the studios and everyone else it's a good show it was fun I hope you listen to it
[4232.48 → 4238.32] comes out tomorrow and a big thank you to our friends and our partners at fast fly and type
[4238.32 → 4247.28] sense they have our back if you need amazing search an amazing CDN or the best place to host your things
[4247.28 → 4252.96] check out fly check out fast and check out type sense they're all awesome but hey that's it
[4252.96 → 4266.80] the show's done we will see you tomorrow
[4266.80 → 4268.80] you
[4282.96 → 4296.80] you
