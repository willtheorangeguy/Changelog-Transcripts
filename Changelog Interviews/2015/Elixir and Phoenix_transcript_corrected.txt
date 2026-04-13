[0.00 → 15.08] welcome back everyone this is the changelog and I'm your host Adam stekowiak this is episode 147
[15.08 → 20.96] and today jarred and I are talking to Chris McCord talking about elixir on top of Erlang
[20.96 → 26.70] phoenix the web framework definitely got me and jarred thinking about concurrency and elixir for
[26.70 → 32.26] upcoming project phoenix sounds really cool and I love this conversation with Chris we got some
[32.26 → 38.64] awesome sponsors code ship top towel and portico we'll tell you about top towel and portico later
[38.64 → 43.16] in the show, but our friends at code ship have this awesome new feature that help you deploy the
[43.16 → 48.44] production so much faster than you're doing right now it's called parallel CI and if you want to run
[48.44 → 53.80] faster tests and have your builds built and in production quicker you've got to run your tests
[53.80 → 59.94] in parallel with parallel CI you can now split your test commands into 10 test pipelines or up to 10
[59.94 → 64.76] test pipelines this lets you run your test suite much faster than before and drastically reduce the
[64.76 → 70.46] time it takes for you to push your code to production and get your builds run they integrate
[70.46 → 75.66] with GitHub and Bitbucket you can deploy to cloud services like ROK AWS and many more, and you can
[75.66 → 80.38] get started today by trying out their free plan which includes 100 builds a month and five private
[80.38 → 86.62] projects, or you can use our offer code the change law podcast again that offer code is the change law podcast
[86.62 → 93.38] and with that code you'll get 20 off any plan you choose with code ship three months head to
[93.38 → 97.98] codeship.com slash the change law to get started and now on to the show
[97.98 → 107.48] all right everybody we're back we got Chris McCord on the call today we're talking about some cool
[107.48 → 113.78] stuff today elixir the language uh phoenix the framework Chris welcome to the show how's it going
[113.78 → 119.34] and we also got jarred canton on jarred how are you today manning doing better than I was yesterday
[119.34 → 123.74] yeah yesterday was a bad day that was a bad day would you did you sleep a lot of a lot of
[123.74 → 130.02] time I was trying to sleep mostly tossing and turning you know but uh all good today feeling better
[130.02 → 140.12] did slack keep you up and whatnot ah everything was keeping me up it was a bad day so Chris you hail
[140.12 → 147.42] from Dayton Ohio right that's right not phoenix Arizona no not, yet we established in the pre-show
[147.42 → 153.10] that Chris would be slightly cooler well at least I did if you were from phoenix Arizona because of
[153.10 → 159.24] phoenix the framework it's just it would make sense you know maybe he had named the framework
[159.24 → 166.12] Dayton framework see come on Chris the logo wouldn't have been nearly as cool though so
[166.12 → 171.00] I don't know I mean you got some you got the date what the Daytona 500 up there right
[171.00 → 177.00] no that's that's that's wrong state is that a different state that's uh Florida so that's right
[177.00 → 183.22] florida what's in date well you know isn't there something racing there no we like where
[183.22 → 187.58] the Wright brothers were from so we were first in flight except they didn't they built it here but
[187.58 → 193.64] they flew it in North Carolina, so both states claim that we're both first in flight so that's
[193.64 → 200.12] probably our only claim to fame that's it well you got some other claims of fame here so let's let's
[200.12 → 204.78] dig deep here so you know for those who know who do not know who you are how do you introduce yourself
[204.78 → 211.42] to an audience like we got today um I created the phoenix framework uh it's an elixir web framework
[211.42 → 219.26] and i also i just recently uh authored uh metaprogramming elixir for prorogue and uh during
[219.26 → 225.52] the day I build web applications at little lines I like that you know that you got a
[225.52 → 233.20] little shout out too in that uh in your talk recently it was elixir com yep yeah um was there
[233.20 → 237.22] people in the crowd that knew who little lines was I think we got yeah we had like that one little
[237.22 → 241.08] whoop a small following I don't know I don't know who that was we asked someone did
[241.08 → 248.82] so yes jarred's singing in the chat room behind the scenes Daytona 500 classic yeah that's that's just
[248.82 → 253.08] i I confuse it all the time with Dayton and I'm sorry that's classic
[253.08 → 259.34] we get that a lot we get that a lot yeah you google date, and you get Daytona 500 every time
[259.34 → 264.24] every time all right well Chris we've been excited to get you on the show we've had uh
[264.24 → 270.26] multiple requests to have shows on elixir uh show on phoenix we have to thank a few of our
[270.26 → 275.40] listeners Alexander Quine was the one who originally said hey let's let's talk about elixir on the show
[275.40 → 282.80] and then following up to that was uh Sebastian cizduro sorry Sebastian if I butcher that name
[282.80 → 290.02] Cicero um who said uh yes let's talk about elixir and specifically let's get Chris on the show to
[290.02 → 294.82] talk about phoenix, so thanks to those guys for requesting this, and we're happy to have you here
[294.82 → 301.02] to talk about what did they request that at uh they request that on our ping repo which is GitHub.com
[301.02 → 306.32] slash the changelog slash ping yep and I think they reached out to me someone reached out to me on IRC
[306.32 → 311.82] elixir link and then that's right and opened up that issue made it happen I love that man
[311.82 → 315.42] elixir advocates out there apparently yeah and little lines too
[315.42 → 323.88] yep yeah, so elixir is an interesting young language um seems to be growing quite the following
[323.88 → 330.28] and seems like it's got your uh it's caught your fancy and so why don't you just start off we'll
[330.28 → 334.24] talk about elixir, and then we'll get into phoenix later but I'd like to hear about elixir from your
[334.24 → 340.06] perspective Chris as one who is now developing lots of stuff uh in the language sure so yeah so
[340.06 → 346.28] you mentioned elixir is a young language and that's true uh, but we are at a 1.0 uh stable release
[346.28 → 353.16] we've been there since uh July last year and kind of the cool thing about elixir is it's built on top of
[353.16 → 360.00] uh the Erlang virtual machine so we are very young language, but we're using um Erlang to kind of
[360.00 → 365.34] bootstrap the language itself so we didn't have to kind of reinvent the wheel for a lot of the
[365.34 → 370.52] underpinnings and that let elixir kind of get out of the gates quickly, and then we also have you know
[370.52 → 375.82] 20 plus years of innovation and libraries under the hood that we can take advantage of uh today
[375.82 → 384.04] so for those that don't know uh elixir compiles down to um Erlang byte code, and it runs on the Erlang
[384.04 → 389.76] virtual machine and um Erlang was kind of an obscure language at least for me a few years ago I hadn't
[389.76 → 394.92] I had heard of it but I wasn't really aware of it um never heard about it in college Erlang kind of
[394.92 → 401.00] had this nugget of innovation for the last 25 years is what I tell people they basically run half
[401.00 → 408.18] the world's telecommunication systems and um so it's been operating um at high scale and high
[408.18 → 415.54] reliability for decades and only now recently people are starting to take notice of our most of our modern
[415.54 → 419.58] languages aren't really great at concurrency, and now they're kind of finding out that Erlang solved
[419.58 → 425.74] these problems 20 years ago um so it's pretty cool that like you know you might say that other
[425.74 → 432.00] modern languages like go kind of you know tackle concurrency but Erlang from the very beginning had
[432.00 → 437.62] three core values which I think most not any language that I'm aware of targets it was a language that
[437.62 → 442.78] needed to be highly concurrent um highly distributed because they wanted to run out on multiple telecom
[442.78 → 447.40] switches in the 80s and then a highly fault-tolerant because you wanted these things to stay online
[447.40 → 452.54] forever and they kind of built the language around those needs and developed kind of the standard
[452.54 → 457.72] library around these specific problems and that those specific problems actually map perfectly onto
[457.72 → 463.78] kind of the multicore age that we have today um, so elixir builds on top of that uh Erlang innovation
[463.78 → 470.30] adding um some modern features that you would expect with a language like uh metaprogramming was big
[470.30 → 476.80] for me, it adds um polymorphism through protocols so it borrows some ideas from closure and some other
[476.80 → 482.02] places to really give you this modern language with all this great innovation for the last couple
[482.02 → 488.44] decades so did you have you previously tried Erlang directly or did you come through it from the elixir
[488.44 → 493.70] side so I went straight to elixir but so what got me into it initially is I've been doing ruby
[493.70 → 501.00] development professionally for the last uh six years or so and I wanted to do uh web sockets in my rails' app
[501.00 → 506.68] I was building some kind of real-time features into uh my rails' app I built this gym called sync
[506.68 → 512.10] that let you build let you do like real-time rails partials, and it worked well but I had to
[512.10 → 517.58] jump through kind of all these hoops to push out real-time events I couldn't do it in my rails' app
[517.58 → 521.98] itself I had to kind of offload it to an event machine thread or I had to offload it to like a
[521.98 → 527.42] separate FAE server, and it was like all this messiness and I got into if it wasn't going to
[527.42 → 532.60] scale well at all and so then I started looking at like you know what are some other people
[532.60 → 537.28] doing what languages are they using and that's when I looked at Erlang and I think that was when
[537.28 → 543.06] that was when WhatsApp was not yet sold for 20 billion dollars but at the time um there was an article
[543.06 → 548.66] I read a couple of years ago two or three years ago that was about they were using Erlang, and they were
[548.66 → 553.72] getting a million concurrent connections per server and that kind of blew my mind because I was looking
[553.72 → 560.64] at getting maybe you know 100 connections uh on my rails app um so that kind of spiked my interest
[560.64 → 566.40] into Erlang and then I remembered elixir that I had just kind of come across um so i kind of checked
[566.40 → 572.38] elixir out and then that kind of got the ball rolling on everything so you came at it from
[572.38 → 577.00] the ruby perspective which it seems like it's fitting because elixir also has a kind of ruby
[577.00 → 581.74] pedigree is that right yeah so we'll see we see a lot of people coming over from ruby I think you
[581.74 → 588.06] know a large part of that is uh José valid the creator of elixir um was a rails core team member and
[588.06 → 592.24] he's written probably if you're doing rails development you use half of the gems he's ever
[592.24 → 597.86] created uh so I think his proximity to the ruby community has brought a lot of people over and then
[597.86 → 603.20] also yeah at a glance uh the syntax does look familiar I would say that that's kind of like a
[603.20 → 607.42] veneer because once you get into it the semantics are very different but at least at a glance you're
[607.42 → 612.40] like hey this looks kind of similar so it's kind of like a double whammy to for rubies to
[612.40 → 618.38] kind of jump in awesome so um tell us a little bit more about the language itself so it builds on
[618.38 → 623.76] top of Erlang it has some meta programming is it a functional language is an object-oriented language
[623.76 → 628.50] give us some of the aspects sure yeah so it's an it's a functional language and uh it's immutable
[628.50 → 635.50] and uh it interops it has full interoperability with Erlang so you can call Erlang from elixir and
[635.50 → 641.48] you can call elixir from Erlang so any uh off-the-shelf Erlang library um you can just drop in
[641.48 → 647.22] and it just works and that's what kind of let us um as a community move forward and get a release
[647.22 → 651.90] out soon because we didn't have to kind of you know ream at the wheel for everything um but it
[651.90 → 659.46] adds, and it solves some pain points um that people have had with Erlang uh one is at least for me some
[659.46 → 663.72] people really dislike meta programming but for me coming from like a ruby background i I love
[663.72 → 670.32] meta programming kind of lets me um distill my domain problems and write beautiful code uh so it adds
[670.32 → 675.06] meta programming which was kind of a big feature for me, and then it adds um like I said polymorphism
[675.06 → 681.58] it borrowed the idea from closure where you can get um polymorphism but without object orientation so
[681.58 → 686.04] you can go to functional programming you don't have to throw away all this um all these ideas of
[686.04 → 691.64] polymorphism which are good, and you can kind of get that but in a functional paradigm so for me that's
[691.64 → 695.88] been really nice, and then it has really great like just simple things that you expect in a modern
[695.88 → 700.74] language like really great Unicode string handling which has been historically problematic in Erlang
[700.74 → 707.70] and it really focuses on great experiences like developer experience so it has a build tool that
[707.70 → 713.76] it ships with a project generator so you can just say uh mix new give it a project name, and it will
[713.76 → 719.62] generate you know idiomatic project structure for you, it ships with a test unit framework I can just say
[719.62 → 724.80] mix test to run my tests, and then it also comes with a package manager and kind of all these things
[724.80 → 731.34] were uh missing or not missing they were not uh shipping with the base Ealing installation and it
[731.34 → 736.72] kind of Ealing didn't focus on getting up and running quickly because historically they've been solving I'd
[736.72 → 743.60] say like grittier problems uh so it came in I think solved some filled in some big gaps and I think you
[743.60 → 750.52] know José uh said it best that when he first looked into Ealing he loved everything he saw, but he hated the
[750.52 → 755.42] things that he didn't see and that's what kind of elixir came about is filling in those gaps and still
[755.42 → 761.22] building off all the things that he loved that's interesting I have a little bit of a history with
[761.22 → 767.42] Ealing like a few days like a weekend with Ealing where I thought I'm gonna kind of
[767.42 → 773.44] bend my mind a little bit and the syntax itself it was for me difficult to stretch my mind around
[773.44 → 777.84] started to get to it by the end of the weekend but didn't have a real world use case for it back
[777.84 → 784.32] then so it didn't stick what's the syntax of uh of elixir I know it's kind of difficult to describe
[784.32 → 788.88] code in words but if you had to compare it to a language or to a few languages what would you say
[788.88 → 795.16] that it feels like writing well so I would say the syntax is beautiful and uh it is definitely uh
[795.16 → 800.98] feels uh it definitely feels like ruby to some degree, but it has even it has even more of a natural
[800.98 → 808.20] syntax than ruby and um it has some neat it stole we stole the idea of the pipeline operator if you're
[808.20 → 814.94] familiar um closure has like threading macros and f sharp has the pipe operator um so when you write
[814.94 → 820.04] elixir you structure your code I'd say very differently than other functional programming languages that I've
[820.04 → 826.22] seen just by virtue of having the pipeline operator allows you to kind of flatten out a list of nested
[826.22 → 832.10] function calls so it pipes the argument of the result of one operation into the first argument
[832.10 → 836.14] of another function so instead of like kind of trying to read your code backwards in a bunch of
[836.14 → 842.34] parentheses it kind of flattens that out and just compiles down to the same nested function call um so
[842.34 → 846.58] it kind of it made when I first got into it made me feel like when I was writing ruby of it just it
[846.58 → 852.90] feels very natural, and it's really pleasant to write um but even more which is surprising for me to say
[852.90 → 858.10] so like it gives you think like pattern matching which um anytime I go back to my ruby code I lack
[858.10 → 863.44] these features, and it makes me kind of sad so it's like the first time I had language envy coming from
[863.44 → 867.36] you know a ruby mindset of you know code should be beautiful it should be a pleasant you know
[867.36 → 874.14] experience to write can you explain pattern matching a little bit question too yeah so explain pattern
[874.14 → 882.46] matching in words so I can write multiple uh functions with the same name and I can um
[882.46 → 889.30] give the value of an argument and that function will only be invoked if that pattern matches so if i
[889.30 → 896.44] wrote like a countdown function I can pattern match I could recursively call countdown and pattern match
[896.44 → 901.88] on zero and that would be like the case where I'm done counting down and then I could just pattern
[901.88 → 908.14] match on a variable like number and then recourse on countdown minus one that makes any sense that's a
[908.14 → 914.88] very simple example, but the virtual machine lets you kind of uh restructure um any data structure so I can
[914.88 → 920.72] say I have a list I want to i could pattern match out the first three elements of that list and then get the
[920.72 → 924.78] head of or get the tail of the list like all the remaining elements and I would have those all in separate
[924.78 → 933.32] variables so it lets you kind of restructure things really naturally so does the arguments to the method or to the
[933.32 → 939.02] function they become part of the method signature yes exactly so you'd have multiple ones of the same
[939.02 → 944.50] name and as long as the arguments vary they would call different methods yeah exactly fair to say yep
[944.50 → 950.24] okay and that's how you'll see interesting you'll see that's kind of like idiomatic code so you elixir has
[950.24 → 955.98] like standard branch like if statements unless or if expressions unless expressions, but you use them a lot
[955.98 → 961.28] less often because you have pattern matching that's kind of one of the staples of functional programming
[961.28 → 966.36] correct you're going to find that in enclosure you're going to find that in you know lisps right
[966.36 → 973.84] yeah I think you'll find that in most functional areas and to me, it's its an it's huge I mean once
[973.84 → 979.40] you experience it is makes writing any code without it for me a kind of painful process yeah it seems
[979.40 → 983.98] like it helped melt away conditionals that would otherwise be checking these things, and then you know
[983.98 → 989.02] you know branching depending on the arguments um you could just melt those away with different
[989.02 → 994.24] methods yep so you'll use if occasionally but if i'm using if a couple of times in a function
[994.24 → 998.04] I start sweating a little bit thinking like you know something here is not quite right
[998.04 → 1006.64] interesting so you're building a web framework elixir comes from a rails core team member
[1006.64 → 1011.68] is elixir built for the web or is it a more of a general purpose programming language
[1011.68 → 1016.40] it's built I would say it wasn't I mean José comes from a web background
[1016.40 → 1023.12] but the neat thing about Erlang is you can target um kind of like the embedded space
[1023.12 → 1028.72] or the web so it's kind of i would say a general purpose in that you can go both high level and
[1028.72 → 1033.08] low level with it because it came the Erlang comes from you know running on telecom switches
[1033.08 → 1039.56] so people are using it um in the embedded space um pretty successfully today, but then it's also
[1039.56 → 1045.00] great for you know higher level building any kind of thing that you would run you would consider a
[1045.00 → 1050.64] server uh, so kind of web applications come into that naturally um you look at like WhatsApp they're
[1050.64 → 1055.90] running the entire operation on it um I think they were I mentioned a million connections
[1055.90 → 1059.92] per server but now I heard they're up to two million connections per server and I think they hit three
[1059.92 → 1066.80] million during a spike once, and they're running 400 plus million users all on Erlang and that you
[1066.80 → 1071.58] know that's yeah they had something like 30 engineers too or yes exactly so ridiculously small
[1071.58 → 1076.66] amount of engineers for how many users there were 400 million users and 30 engineers to kind of prove
[1076.66 → 1083.24] how robust Erlang is and elixir builds on top of that so the standard library um kind of gives you
[1083.24 → 1089.42] these um tried and true mechanisms for building out distributed fault-tolerant applications and um
[1089.42 → 1095.22] things uh intended just work cool so I saw your video on elixir cone which we'll link up to in the
[1095.22 → 1099.82] show notes and one thing you said is that you're you'd love if all of your consulting work
[1099.82 → 1106.46] not just your you know personal projects but all your consulting projects hopefully eventually
[1106.46 → 1113.42] at some point will be written in elixir if you had to describe it you know in one phrase what
[1113.42 → 1117.02] is it about elixir that has you so excited you got to distill it down what would you say
[1117.02 → 1126.74] uh so I will two phrases um so one it lets me i I can write highly performant code without sacrificing
[1126.74 → 1133.22] productivity and I can be highly productive without sacrificing performance and it kind of play on
[1133.22 → 1138.54] words, but it's kind of the holy grail like I come from you know writing a lot of rails applications
[1138.54 → 1145.70] where I'm sacrificing that concurrency and that performance but the um productivity and the feeling
[1145.70 → 1151.70] of building these things is so great um elixir gives me both of this performance and productivity
[1151.70 → 1159.38] any drawbacks or things you've run into that have been not so great uh so because elixir is so
[1159.38 → 1165.78] young um you're definitely going to have access to a lot less off-the-shelf uh libraries so if you can't
[1165.78 → 1172.10] just do gem install device and have user authentication yet um so I'd say that lack of off-the-shelf
[1172.10 → 1180.50] packages and also the learning curve is pretty steep compared to if you're coming from any kind of object-oriented
[1180.50 → 1186.74] background, and you want to get into you know ruby or get into python you're it's pretty straightforward
[1186.74 → 1192.58] because you know an object's an object um but coming into functional programming at least for me elixir
[1192.58 → 1198.18] was my first functional language the learning curve initially I call it like the frustration gap where
[1198.18 → 1202.74] you're like you feel dumb you're not getting anything done something that should look like it should be
[1202.74 → 1206.90] simple you can't figure out um it takes a little bit to get past that for things to actually like click in
[1206.90 → 1212.98] your mind thinking about programming differently awesome well we're going to take a break now to
[1212.98 → 1218.02] hear a word from a show sponsor, but we'll be right back and when we come back we'll talk about phoenix
[1218.02 → 1225.06] the web framework top towel is the best place to work as a freelance software developer if you're
[1225.06 → 1230.02] freelancing right now as a software developer, and you're looking for a way to work with top clients
[1230.02 → 1236.02] on projects that are interesting challenging and using the technologies you want to use top towel might just be
[1236.02 → 1241.22] the place for you working as a freelance software developer with top towel means that your days of searching
[1241.22 → 1247.14] for long-term high quality work and getting paid what you're worth will be over let's face it you're an awesome
[1247.14 → 1251.94] developer, and you deserve to be composite like one joining top means you'll have the opportunity to travel
[1251.94 → 1258.82] the world as an elite engineer on top of that top towel can help provide the software hardware and support you need
[1258.82 → 1266.98] to work effectively no matter where you are in the world head to top towel.com slash developers that's t-o-p-t-a-l.com
[1266.98 → 1270.18] slash developers to learn more and tell them the changelog sent you
[1272.34 → 1278.34] all right we are back with Chris McCord Chris you fell in love with elixir you've been doing a lot of rails
[1279.14 → 1286.74] um you decided there needs to be a rail for elixir that kind of the thought process there so uh
[1286.74 → 1292.98] yes and no so I would say we borrow um we definitely borrow some ideas from rails um but
[1292.98 → 1301.22] we're not trying to recreate rails and elixir but I will say um we are trying to borrow a lot of the
[1301.22 → 1307.46] um a lot of the spirits of rails so like what rail showed is if you have a community get together around
[1307.46 → 1315.62] like common conventions you can group build great tooling uh so I would say I would caution to say that
[1315.62 → 1322.02] we are building we aren't building rails for elixir but in some ways we are um we want to build a
[1322.02 → 1326.98] full-featured framework that the community can get together and build great tooling around so if I come
[1326.98 → 1333.14] into your phoenix project I can kind of know where things are how to name them um i just so to that
[1333.14 → 1341.06] degree we are um kind of replicating that similar uh experience uh-huh it's not unique we've we've heard
[1341.06 → 1346.26] this before though I mean uh when we had Taylor outsell on recently uh talking about Laravel that
[1346.26 → 1351.86] was the case there too where you sort of go to the camp you like to hang out best at and you
[1351.86 → 1358.90] create the worlds the rails of that world more or less I mean yep right, so a couple of shows back and
[1359.54 → 1364.98] uh a lot of people love that show, and we're hearing I think you hear it repetitively in a good way
[1364.98 → 1369.78] though it's a good testament back to a lot of the things he helped instill into good web frameworks
[1369.78 → 1375.54] oh definitely i I still do rails every other day and I love it so I think you know rails got a ton
[1375.54 → 1382.18] right and um you know so we borrow if you look at our router um we borrow some ideas there so they
[1382.18 → 1385.54] someone doing rails comes in and looks at phoenix without having any elixir experience they'll
[1385.54 → 1391.06] kind of be like hey if they squint a little bit um that looks pretty similar the DNA of rails comes out
[1391.06 → 1395.62] yeah, but we aren't just trying to go feature for feature saying okay like you know we need
[1395.62 → 1403.70] it's not a feature x right gotcha kind of like those uh those movies that aren't they're not
[1403.70 → 1409.38] like a retelling of a non-fiction they're like based on a true story you know those where you know
[1409.38 → 1413.38] like this is not actually a true story it's just based on a true story it's kind of like you know you
[1413.38 → 1418.10] want inspired by yeah, and you want to you want to think differently and um we've definitely borrowed
[1418.10 → 1423.78] some ideas um from other areas too so we're not just looking at rails we're looking at um like
[1423.78 → 1429.62] you know socket Io was a big inspiration for our real-time layer and I think the problem that people
[1429.62 → 1436.74] coming into elixir initially from any other language will say okay well we don't have a device for phoenix
[1436.74 → 1440.90] yet let's make device so instead of which is the wrong way to think about it if you need user
[1440.90 → 1445.14] authentication then you should start thinking about how do I solve user authentication you know in a
[1445.14 → 1449.46] a functional mindset so I think um that's why I just want to caution that we're not just trying
[1449.46 → 1453.94] to say okay how do we make how do we clone rails in phoenix no it's like how do you how do we think
[1453.94 → 1458.90] about the spirit of rails and how do we apply that on some of the good stuff that we can bring over to
[1458.90 → 1463.86] what works best in elixir and what we need to fulfill our needs yeah I mean you got to play the
[1463.86 → 1468.66] strengths of your language and your environment where are you drawing those different
[1468.66 → 1474.58] ideas from if not directly from rails from other experiences from other projects in the elixir
[1474.58 → 1480.74] ecosystem from elsewhere yeah so I mentioned so the big thing for me when I started getting into
[1480.74 → 1487.62] looking into this was doing real-time events from my rails app so when I saw elixir and right up on
[1487.62 → 1493.30] Ealing you know I immediately realized that this would be perfect for solving the real-time nature that i
[1493.30 → 1498.82] wanted with my application uh so socket Io I had a little bit of like node experience played with socket Io a
[1498.82 → 1505.06] little bit and um socket Io is awesome because it just lets you gives you a browser client and on the
[1505.06 → 1509.78] node server side you can just push and receive events, and it's super simple so i kind of drew on
[1509.78 → 1516.26] that API a little bit in that experience to say I want real-time events from my browser to my phoenix
[1516.26 → 1522.10] app to be as trivial as building like a rest back end like if you're building a rest back end and whatever
[1522.10 → 1526.98] framework you're using like you can just snap your fingers, and you know instantly how you would build that
[1526.98 → 1532.34] so that's kind of a big push on our real-time layer was looking at socket Io and then we kind of
[1532.34 → 1537.94] extended that a little bit um to kind of namespace events um but I'd say that's been a big uh inspiration
[1537.94 → 1545.06] for us, so web socket support came in early and is like production ready or what's the status of your
[1545.06 → 1551.06] of your web socket support yes so web socket support is production ready and since then uh since elixir
[1551.06 → 1556.90] cone we've added it falls back to long polling uh so it's going to work in I think i.e. 8 plus now
[1557.54 → 1564.74] um falls back to long polling transparently and um you can just drop it in phoenix JS and uh it just
[1564.74 → 1570.74] works awesome have you had uh have you had success with people out there in the community trying it
[1570.74 → 1578.02] have you built it have any of your own projects with it yeah so we're using it um one of our own
[1578.02 → 1583.30] uh projects which unfortunately I can't share publicly um, but people are using it kind of all over the place
[1583.30 → 1589.62] uh someone uh recently built like an uh right around Christmastime you could play uh jingle bells
[1590.34 → 1595.78] remotely with like a party of people so kind of like you know you could coordinate they did this
[1595.78 → 1600.26] like timing algorithm so you could ring your bell and play like you know the jingle bells chime
[1601.30 → 1608.50] you know across iPhone to iPhone just using phoenix channels so I think gaming could be a big uh a big
[1608.50 → 1614.42] area like someone I haven't seen this come to fruition, but someone was looking into using uh phoenix channels
[1614.42 → 1620.10] um over to like an Unreal Engine so like a native desktop app, but you know pushing out the real-time
[1620.10 → 1626.18] events back and forth so kind of outside the HTML server webspace I think phoenix could have a
[1626.18 → 1633.14] a happy home there too yeah I even saw that you uh have some iOS support going on want to talk about
[1633.14 → 1640.90] that sure yeah so I think you know as I mentioned at elixir cone um phoenix is great at building just
[1640.90 → 1646.50] what you would think of as HTML web applications and APIs but i kind of wanted to go beyond that
[1646.50 → 1650.74] because the web is kind of transitioning changing a little bit you know I don't think browsers are going
[1650.74 → 1657.78] anywhere and I'm a web developer but I think we have all these um native apps native clients
[1657.78 → 1662.98] internet of thing movement coming on, and we need a framework to be able to connect all these devices
[1662.98 → 1668.66] and push out events and talk to them so I think phoenix is well positioned for that and i kind of for
[1668.66 → 1675.94] version 1.0 we have an iOS client um that is I think it works on it's a swift client um so it's not
[1675.94 → 1681.06] going to work on any of your uh Objective-C library libraries, but someone has put together
[1681.06 → 1685.86] an Objective-C library, and we're going to show up with an android client as well for 1.0 so you should
[1685.86 → 1690.58] be able to write mobile applications that are native and have them talking to the same back end that your
[1690.58 → 1696.10] web application is talking to from the browser that's pretty nice we're hearing lots more about
[1696.10 → 1700.42] the internet of things I mean I think that's we heard that jarred with uh some things we haven't
[1700.42 → 1705.62] released it with beyond the code when we talked about what in software inspires and excites people was a
[1705.62 → 1711.46] lot of the things that ties into like devices um things like the watch for example or other things
[1711.46 → 1719.06] that are inside your home I'm a little bit wishy-washy on the internet of things myself it seems like it's
[1719.06 → 1724.66] very nebulous and kind of I don't know I don't think aspirational is the right word but
[1725.86 → 1730.98] pie in the sky, but they're like the real world applications of it don't seem like they're actually
[1730.98 → 1735.14] all that useful like you know your toaster can tell you when your toast is done it's like yeah but I can
[1735.62 → 1741.14] I can look at my toast and see that it's burnt right um what or your toaster what are your thoughts
[1741.14 → 1746.10] your toaster can list itself one bay did you see that there was someone made one where if you didn't
[1746.10 → 1751.30] use it in x amount of days it would automatically eBay itself so it could be sold to someone that would
[1751.30 → 1756.34] use it yeah that's hilarious yeah I mean most of our applications are just someone I somewhat agree
[1756.34 → 1761.06] with you, they're they're they're very kind of silly kind of uh novelties right now I'm sure
[1761.06 → 1767.46] it's just because it's very fringe and just upcoming and very much a buzzword but um no doubt
[1767.46 → 1772.34] we'll need software to drive those you know those interactions um whether they're valuable or
[1772.34 → 1776.82] not we're going to have to find out I guess well for you Chris though what when you say internet
[1776.82 → 1784.82] of things as in regard to phoenix and elixir what are you thinking of so for me, i so I think i
[1784.82 → 1789.22] kind of agree that you know internet of things is just a's a hype right now that we haven't really
[1789.22 → 1794.50] seen great applications of it but I think even in the mobile space if we just talk smartphones
[1794.50 → 1799.06] you know that is we already have the internet of things in my mind everyone's walking around
[1799.06 → 1804.26] permanently connected to the internet with a square in their hand uh so I think from that perspective
[1804.82 → 1810.82] um coming from again I know I'm not trying to pick on rails but coming from a rails background i just
[1811.54 → 1815.94] don't see it in that mindset of being able to have all these connected devices I can't do that in
[1815.94 → 1820.98] ruby just based on the concurrency model at least not super well so for me just from like the
[1820.98 → 1826.26] mobile um landscape I want to have a framework that I can maintain a persistent connection to
[1826.26 → 1833.30] my devices, and you know push out real-time updates like someone um recently wrote an app that uh they
[1833.30 → 1838.90] use phoenix channels to track shipments for a new startup so they're they have a web browser it's
[1838.90 → 1844.82] an ember app, and it's listing you know where the drivers are at all times so it's a native application
[1844.82 → 1849.22] pushing out updates over phoenix channels and shows you in real time on a map in the browser where
[1849.22 → 1854.66] your drivers are so things like that um I think is what I'm talking about with internet of things
[1855.54 → 1860.74] but I think the toaster and stuff I think maybe in four or five years we'll see useful applications
[1861.30 → 1865.30] I think a good application of what you're talking about just with the phone the device connectedness
[1865.94 → 1871.78] um is the meerkat app which kind of has blown up in the last couple of weeks um which is a twitter
[1871.78 → 1876.66] base it's an Io it's an iPhone app you guys probably have seen it posted to twitter where
[1876.66 → 1881.70] you can immediately start streaming live um just post a tweet out to Twitter I think it's like a
[1881.70 → 1887.06] single click to start streaming video from your phone and anybody from their phones can just click
[1887.06 → 1893.22] and they're now streaming your video live to their phones very simply, and you know this is the kind
[1893.22 → 1898.50] of thing that just wasn't even possible a couple of years ago right I mean now we have the pervasiveness
[1898.50 → 1904.58] of LTE we all have the devices we have the software there has to be infrastructure behind that right
[1905.46 → 1909.06] you get the bandwidth costs which is what I think about is like man how long can these guys
[1909.86 → 1912.90] just burn money before they're probably open twitter buys them or something but
[1913.54 → 1918.02] how long can they just burn money on bandwidth you know before they start making some money of their own
[1918.02 → 1924.18] but then also like their servers back there driving these things and the ability to all of a sudden have
[1924.18 → 1934.10] thousands of streaming video connections seems like Erlang and the OTP stuff that it does is kind of
[1934.10 → 1942.18] well suited for those kinds of large um communities what do you think about that yeah exactly, exactly I was
[1942.18 → 1948.02] going to say the uh I went to Erlang factory uh last year I think that's the first time I talked about phoenix
[1948.02 → 1954.10] publicly and uh one of the WhatsApp engineers was there, and they were he was talking about that where they
[1955.14 → 1960.82] turned on the feature for sharing image and video, and they weren't sure how it was going to scale because he was talking about
[1961.30 → 1966.74] you can't really you can't really load test these things you can't fake it yeah yeah if you have 400 million users you can't say
[1966.74 → 1971.86] like hey let's see how this is going to work throw some servers behind it, you can't really load test it so they had to do a live
[1971.86 → 1976.90] and uh just worked, and they were able to you know turn on the and that was kind of you know sharing video
[1976.90 → 1982.18] and images so I think you know very similar to what you were just talking about yeah awesome so the
[1982.18 → 1987.78] channel support is unique I think um and interesting what else does phoenix bring to the
[1987.78 → 1994.02] table as far as a framework goes do you consider it a full stack framework yes yeah, so the goal is i
[1994.02 → 1998.90] think you know i it's not a micro framework I hate that word I think you know if you want to be a
[1998.90 → 2004.42] library libraries are fine some people like building their applications out from small
[2004.42 → 2010.66] composable pieces but I think in practice at least building a lot of rails applications and inheriting
[2010.66 → 2015.62] a lot of rails applications I think having a set of conventions and a set of full features and obvious
[2015.62 → 2022.02] ways to do things is great for community so yeah it's definitely it's a batteries included framework
[2023.54 → 2028.58] give us some of those batteries what you got in there cool so we have uh
[2028.58 → 2035.06] similar to i mentioned our router is somewhat similar to rails so you can have this DSL for
[2035.06 → 2042.34] routing requests into your controllers, and we have a view layer is kind of neat because you can
[2042.34 → 2047.94] render we kind of separated the idea of views and templates, so views are more your presentation layer
[2047.94 → 2053.70] and views render templates and a special thing at least about what we do is we pre-compile all the
[2053.70 → 2058.90] templates into the view module so runtime you're just calling a function, and it's returning you it's
[2058.90 → 2064.18] basically doing string concatenation whereas you know other frameworks can't really pre-compile
[2064.18 → 2068.58] these things so they have to read from disk and cache it and go through all this work but since we have
[2068.58 → 2074.10] metaprogramming elixir all that content in your template files is just pre-compiled and baked directly
[2074.10 → 2079.46] in as a function call is that how all the metaprogramming works in elixir it's all at compile time
[2079.46 → 2084.42] yeah all the compile time so we can do a bunch of work at compile time and at runtime it's super
[2084.42 → 2087.78] fast you don't have to worry about caching these things you're not doing any disk reads because it's
[2087.78 → 2094.66] all just in memory so, but it's just as robust and um powerful as what you would think of in like a
[2095.30 → 2099.78] scripted language that's not being compiled so like people are seeing like to give you an idea people are
[2099.78 → 2105.06] seeing microsecond response times rendering templates in phoenix which is kind of cool
[2105.06 → 2112.90] what else you got so routing is I'm sure there's uh it seems like you have MVC but you
[2112.90 → 2119.78] also have a what you call a view layer and a template layer can you talk about that yeah views are
[2119.78 → 2125.06] basically like a presenter the presenter pattern if you're coming from an object-oriented mindset but
[2125.54 → 2134.18] we push it further too so I'm in a controller I can say you know render my show template, and you can
[2134.18 → 2140.02] explicitly specify the content type, or it will use the content type from the accept headers so if it
[2140.02 → 2145.70] was a HTML request it's going to render the HTML template, but we also are promoting the mindset of
[2145.70 → 2150.50] your view should render everything so if you want to render Jason if you're just building like a Jason API
[2150.50 → 2156.50] your view is just a module that's going to construct that Jason uh for the caller so we kind of I think i
[2156.50 → 2160.74] at least haven't seen that in other areas where we're kind of pushing things out of the controller and
[2160.74 → 2165.70] keeping your controllers really clean and making the view present whatever you know was requested
[2166.50 → 2172.10] and then obviously um on top of that our channel layer is probably the biggest I'd say innovation and
[2172.10 → 2179.30] what draws people in and that's what you can do you can push out real-time pub so events to the browser
[2179.30 → 2187.06] today, and hopefully you know iOS and android coming soon cool so that view layer I mean it's its kind of
[2187.06 → 2194.34] like a presenter or a decorator layer, but it can itself just serialize Jason so you wouldn't even
[2194.34 → 2198.98] have to have templates at all is that what you're saying yeah exactly, exactly, but you would still be
[2198.98 → 2203.54] rendering a view you wouldn't be constructing the Jason in the controller as like an as a map in the
[2203.54 → 2209.22] controller what if you do want to have just straight up HTML templates with generated server-side
[2210.02 → 2218.90] markup that all yeah so then you yeah you would just create a html. Ex template and uh say render
[2218.90 → 2223.94] index.html, and it would it would precompile that and render it uh so it'd be just the same
[2225.62 → 2230.98] and that I assume has your typical helper methods or whatever they're called in elixir they
[2230.98 → 2236.10] called functions is everything a function yeah everything's a function i I tend i helpers is
[2236.10 → 2240.98] an accurate way to describe it too, so your views can define um all the helper methods for its
[2240.98 → 2246.66] templates whether that template is whether that's going to be your HTML template or just you know
[2246.66 → 2253.70] Jason directly in the uh module body awesome so as far as full stack goes is there anything missing at
[2253.70 → 2261.54] this point so uh we're pretty close to 1.0 although I say that and I don't want to give any hard dates but
[2261.54 → 2267.62] I'd say what's missing video that you said uh end of by the end of the year you'd be at 1.0 but that
[2267.62 → 2272.18] was last year I didn't say which I didn't say which year he's pulling a pearl on us here
[2274.18 → 2280.10] he's pulling a software developer on us yeah I pushed it back to uh, uh I've said quarter one this
[2280.10 → 2284.58] year, but we're coming up on that but no really I think we're actually quite close now um what is
[2284.58 → 2290.42] missing is uh like internationalization we used to have uh what we tore it out um because we're working on
[2290.42 → 2296.10] something better uh so we might release 1.0 without internationalization um and then release like
[2296.10 → 2303.54] release like a 1.1 with it so that's been taking out now and um I think for now we're just trying to
[2303.54 → 2311.22] settle on our channel API and make sure our um you know the current APIs that we have are good
[2311.22 → 2315.22] because you know we don't want to lose we can't release 1.0 and immediately break things but the
[2315.22 → 2321.70] core features there you know are baked in so we have routers uh controllers views we even have a
[2321.70 → 2327.62] we refer to them as endpoints so we're not like a monolith like rails so you can kind of bring in
[2327.62 → 2335.22] phoenix into an existing OTP app, or you can run multiple phoenix endpoints within an app and everything
[2335.22 → 2339.46] kind of just works along the lines of you can have as many of these things running as you want
[2340.26 → 2344.66] and then along with that what we've recently done is you know we've had channels for a long time but we
[2345.22 → 2350.50] recently um supported different pub sub adapters, so the channel channels operate on top of a pub sub
[2350.50 → 2355.78] layer and the problem that we used to have is if you weren't running elixir uh nodes clustered
[2355.78 → 2361.06] together like on Heroku dynes can't talk to each other um you couldn't really make use of channels
[2361.06 → 2366.74] over dynes that weren't clustered so we recently added a Regis adapter and anyone can implement their
[2366.74 → 2373.46] own pub sub adapter now where we kind of use a pub sub adapter to broker the um events so now on Heroku
[2373.46 → 2378.10] cross your dynes it's just going to work or if you're running elixir distributively it's just
[2378.10 → 2383.62] going to fall back to the standard library so that was a big feature for us recently one term I think
[2383.62 → 2389.78] we've glazed over a little bit is OTP yeah could you unpack that for the audience sure yeah and i you
[2389.78 → 2395.06] know when I first saw this too I was thinking like what the heck is that so OTP stands for open telecom
[2395.06 → 2400.90] platform which doesn't really tell you anything about what it is um so it started off this is you know
[2400.90 → 2405.94] historically Erlang was built for um telecommunication systems that's where the open telecom platform
[2405.94 → 2411.14] comes from but really the best way to describe it is its Erlang's standard library for building
[2411.78 → 2416.90] concurrent distributed fault-tolerant applications and that's what elixir ships with as well so
[2416.90 → 2422.82] anything you're doing as far as holding state, or we build applications we call them in like supervision
[2422.82 → 2428.74] trees so you have supervisors that are going to supervise different parts of your application so if
[2428.74 → 2433.06] something crashes or something goes wrong it's going to automatically be restarted by its supervisor
[2433.62 → 2438.82] and that will kind of travel up the chain and um all the way up to your application supervisor and
[2438.82 → 2442.90] you kind you know so if everything crashes the whole world's on fire it will keep trying to restart in
[2442.90 → 2449.70] the entire you know different chains of the application uh so that's what OTP is and um you're going to use
[2449.70 → 2454.98] it um everywhere use it everywhere what is it actually what's the benefit
[2454.98 → 2462.50] yeah so uh elixir's concurrency model is we call them uh our unit of concurrency is a process
[2462.50 → 2467.62] it's not an operating system process it's like a really lightweight thread, and you can run like a
[2467.62 → 2473.94] million of them on like you're like on my macBook I can spin up a million processes so what OTP is it's
[2473.94 → 2480.82] just uh it built out a set of conventions for um managing state in an application and responding to
[2480.82 → 2487.62] um failure and those are processes and uh they call we call them gen servers if we want to hold state
[2487.62 → 2492.26] in a process we have to basically recourse on a process with its state over and over since we're
[2492.26 → 2497.54] an immutable language so it's basically just a set of conventions that kind of naturally came about
[2497.54 → 2502.98] when uh Erlang was solving these problems, and they codified it into OTP uh so actually the
[2502.98 → 2507.70] the best way I've heard it described is it's its the uh the rails of concurrency nice
[2507.70 → 2513.54] and that's pretty accurate all right let's take a break real quick and hear from a sponsor when we
[2513.54 → 2518.98] come back we'll talk about deploying phoenix to production so we'll come back in just a second
[2521.14 → 2527.38] I could not be more excited about this sponsor postico is a Postgres client for OS 10
[2527.38 → 2533.86] developed by a single independent developer named Jacob egger Jacob has open source chops as well you may
[2533.86 → 2539.06] know him as the maintainer of postgres.app, and he even used to work on SQL pro back in the day
[2539.86 → 2546.10] equal pro is a MySQL client for OS 10 that has a special place in my heart it is a great client with
[2546.10 → 2553.94] a capital g, but unfortunately it only supports MySQL I'm a Postgres convert and I've long been clamouring
[2553.94 → 2560.66] for a high quality Postgres GUI for OS 10 portico aims to be just that it has all the features you come
[2560.66 → 2565.62] to expect from a SQL client and more, but you know what if something that you want is missing
[2566.18 → 2572.50] you can contact Jacob I can tell you from personal experience he takes feedback and is very responsive
[2572.50 → 2578.42] which is important to me when I'm investing in software but the best part about portico is that
[2578.42 → 2585.06] it is native to Yosemite, and it is designed well it fits right into the operating system copy and paste
[2585.06 → 2590.82] just works undo just works keyword shortcuts you bet the portico gone are the days of using
[2590.82 → 2597.22] SQL GUIs that stick out like a sore thumb there's a free trial which has no time limit so check it out
[2597.22 → 2604.58] portico the best way is to google that word that's p-o-s-t-i-c-o you'll find it at the very first hit
[2604.58 → 2610.50] that's the simplest way to get where you need to go check out portico I love it and I think you will too
[2610.50 → 2618.02] thanks to Jacob for supporting us and let's get back to the show all right so we're back Chris let's
[2618.02 → 2621.70] talk about deploying I think that's one of the things that tends to hold people up you know getting
[2621.70 → 2624.74] into production is one of the things so what kind of environment do you have to deploy a phoenix
[2624.74 → 2632.82] framework app to so um it's actually funny because it's easier for me to deploy my phoenix apps these
[2632.82 → 2638.02] days to Heroku and then to deploy my rails apps and I don't know why like i I did some benchmarking
[2638.02 → 2642.98] recently, and it took me like two hours to get this rails app started up even though I do rails
[2642.98 → 2648.74] full-time um, but elixir is actually pretty easy to deploy if we're not talking some of the more
[2648.74 → 2656.02] advanced features um it's pretty easy to build on any kind of you know Unix Linux uh box we ship with
[2656.02 → 2660.26] uh usually a lot of people if you're deploying yourself you'll run it behind like a nginx proxy
[2660.98 → 2666.90] um, but it will happily serve you know directly over port 80 if you wanted to you know live on the
[2666.90 → 2673.54] dangerous side yeah, but it's not it's not too hard to stand up um elixir i usually I tend to build
[2673.54 → 2681.14] from source and have any problems um Erlang is available um for pretty much any distribution you
[2681.14 → 2686.50] can think of um and Heroku has a build pack for it so it's pretty easy to stand an app up on Heroku
[2687.38 → 2692.02] quickly and then if you want to get into like advanced appointments um we haven't mentioned this
[2692.02 → 2699.14] yet but Erlang and elixir has this idea of uh hot code uh uploading so I can upgrade my code in
[2699.14 → 2705.86] production from like one state to the next and um for literally zero talent downtime deploys so not like
[2705.86 → 2711.62] you know some people are doing where you have like nginx like serve all the requests and then wait and
[2711.62 → 2719.54] shove the request on a new instance it's actually like literally I can update a module from one piece of
[2719.54 → 2724.50] code to the next and have what it was doing pass that off to the new code if that makes any sense
[2725.14 → 2732.82] how does that work man magic sounds like it sounds like magic to me yeah so I don't have experience
[2732.82 → 2737.86] in this regard uh we have we do have a guide up, but it's called uh they're called uh releases we do have
[2737.86 → 2744.26] a guide up on phoenix framework.org for performing these, and it will work, but you have to your have to
[2744.26 → 2748.02] think about a lot of things in your code to make sure they can work well with releases so that's the
[2748.02 → 2754.58] only thing like if you don't need that absolutely you know critical zero time downtime deploy uh type
[2754.58 → 2759.54] setup it's its I would say not worth it so you have to kind of weigh the odds of development cost
[2759.54 → 2763.94] of maintaining that, and then you also really have to test releases because um you want those things
[2763.94 → 2769.54] to work perfectly um so if you're like a telecommunication company um for example like the joke is
[2769.54 → 2773.94] you've never heard like AT&T doesn't call you up and say you know sorry you can't make a phone call
[2773.94 → 2779.30] tonight from 6 to 10 p.m because we're going down for scheduled maintenance like you never that never
[2779.30 → 2785.94] happens so I think for some um for some companies they can do that and they
[2785.94 → 2790.50] have been doing that successfully uh so you kind of have to just weigh the odds but that does work
[2790.50 → 2796.90] there's a tool called exam which is like elixir uh release tool for building releases and performing
[2796.90 → 2803.46] hot code swapping, but it definitely requires some more TLC I'd say so just to be clear we're not talking
[2803.46 → 2810.98] about a rolling restart we're talking about live code swapping just like bam yeah exactly so that
[2810.98 → 2814.50] yeah you can do rolling restart but yeah this is like a whole nother ball game of
[2815.06 → 2820.98] if I have liked you know if I have a counter keeping track of number of active users and that thing's in
[2820.98 → 2826.82] the middle of like running a piece of code that module I update that counter module the new piece of
[2826.82 → 2832.42] code will get the previous state what that counter was, and you actually write a callback in a function to
[2832.42 → 2837.22] say there's a code change like here's what here's the state that I had now you take it and make it
[2837.22 → 2842.98] into some new state that you want to handle that makes any sense uh so it's pretty I mean pretty
[2842.98 → 2847.38] amazing that this kind of things are built in but like I said it's going to take some more work
[2847.38 → 2851.94] is this the language level or phoenix level this is at the language level okay
[2852.74 → 2857.14] the advantage of being on Erlang because like you said the telephone companies didn't have the
[2857.14 → 2863.46] luxury of downtime like we have with the web right so I think what I recommend to people is
[2863.46 → 2868.50] you know rolling restarts are totally fine and I think you know to some degree you're going to
[2868.50 → 2873.06] have to write your application around you know if someone trips over the server power cord things are
[2873.06 → 2879.30] to go down anyway so you still want to be able to react to going offline anyway so I think unless you
[2879.30 → 2885.86] have the peculiar you know use case for releases um I think at least getting started you don't have to
[2885.86 → 2891.30] really worry about it but if you do have this high demand I think there's an it's not WhatsApp
[2891.30 → 2896.02] there's another early chat app that they're running on releases um so you know they're got they're like
[2896.02 → 2900.98] guaranteeing message delivery type stuff so it's really cool if you have a especially if you're running
[2900.98 → 2906.10] kind of some software as a service like uh like you know pusher or uh some of those companies where
[2906.10 → 2910.98] you know you can't really stand to have messages dropped you have to guarantee that there's not
[2910.98 → 2916.42] going to be any kind of blip, but it's a nice option let's switch gears a little bit and talk
[2916.42 → 2922.42] about the community one thing I've noticed so far is you've just referred to it as we pretty much the
[2922.42 → 2928.74] entire conversation yeah when speaking about phoenix who's all involved in phoenix and then by extension
[2928.74 → 2935.22] the elixir community tell us about that sure so uh we've had the great fortune of José
[2935.22 → 2940.66] valid has joined the phoenix core team uh so he's been working on phoenix quite a bit for the last
[2940.66 → 2947.86] several months, and he's contributed some of the biggest features uh as of late um so it's José is
[2947.86 → 2954.18] a big core contributor we've recently we have a Jason Steve um sunny Scrooge and I'm going to miss
[2954.18 → 2959.94] a few people here, but we have a set of I think five people on the core team right now and the community
[2959.94 → 2965.46] in general I think is one of elixir's biggest assets as far as um you know we're trying to establish
[2966.58 → 2970.98] um the meme in the community of you know we're very helpful and welcoming because a lot of these
[2970.98 → 2976.18] concepts are difficult to get started in especially if you're coming into phoenix you're listening to
[2976.18 → 2980.66] this podcast, and you're like wow this sounds great let me dive in so suddenly you're learning
[2980.66 → 2984.98] like a new web framework you're learning a new language then you have this like OTP thing that
[2984.98 → 2989.38] you're trying to learn so it's like a new programming paradigm so like there's like seven different
[2989.38 → 2994.66] things that are like totally new to you um so we're trying to kind of build a community around
[2995.30 → 2999.54] being very supportive asking for help receiving help and I think we've been pretty successful with
[2999.54 → 3006.18] that where you said uh somebody pinged you earlier I think it was in the pre-call how you got ping for
[3006.18 → 3012.10] coming on the show was in a RC channel what was that RC channel yeah it's uh elixir Lang
[3012.10 → 3018.90] elixir hyphen Lang on uh free node that's that's where I direct anyone that's on Twitter mentions
[3018.90 → 3022.90] anything about elixir I tell them to hop on if they have you know get stuck or have any questions
[3022.90 → 3029.22] is there one specific for phoenix uh so not yet so whenever José gets tired of seeing all the phoenix
[3029.22 → 3034.10] stuff in the elixir channel that we'll make our own but for now it's um kind of one of the same right
[3034.10 → 3041.54] now yeah he's pretty savvy of José as the language author and obviously highly invested in the success of
[3041.54 → 3049.30] elixir to participate in the development of phoenix because um adoption especially of a language that
[3049.30 → 3056.10] suits itself so well to the web um could be highly dependent upon a popular and very high quality
[3056.10 → 3060.26] web framework do you think that was kind of the deciding factor of why he got involved
[3060.82 → 3066.26] or was it just pure excitement for what you're up to yeah I think um that probably has something
[3066.26 → 3071.38] to do with I know from like from the beginning um José wanted to you know he comes from a web
[3071.38 → 3076.82] background, and he had started a prototype web framework called dynamo um why he was building
[3076.82 → 3082.58] elixir so from the beginning he was definitely thinking about um how elixir is well suited to web
[3083.30 → 3088.02] but I think it was uh Bruce Tate uh had convinced him that he couldn't do he couldn't write a web
[3088.02 → 3094.18] framework and a new programming language at the same time just it was too much so instead he uh he
[3094.18 → 3100.42] built plug which was like an uh http uh middleware and like web server abstraction kind of like rack
[3100.42 → 3107.06] you're familiar from ruby so instead of the kind of used that dynamo framework to prototype some ideas
[3107.06 → 3112.58] and why he was building elixir to see how they could coexist and then um step back from that built
[3112.58 → 3117.30] that middleware library and then that that way I was able to come in and build on top of his
[3117.30 → 3121.54] middleware uh so I think it was just kind of like you know the timing all together you know while he was
[3121.54 → 3127.30] finishing elixir I had found plug and started building phoenix on top of plug, and then he was
[3127.30 → 3132.34] able to finish elixir, and then he hopped on board, so kind of timelines worked out really well and i
[3132.34 → 3137.94] think um yeah the phoenix's co-bases is definitely it's been hugely beneficial to have him on board it's
[3137.94 → 3144.02] awesome so you'd say that phoenix is still built on top of plug and still has this middleware thing
[3144.02 → 3151.30] going on yeah so and that's the big thing for us is i I didn't want to hide the plug layer so
[3151.30 → 3155.38] like if you're coming you know I've been talking about rails a lot but I come from a rails background
[3155.38 → 3159.94] like uh you don't really you know you're running on top of a rack but unless you're using rack
[3159.94 → 3164.74] middleware explicitly you're you know in day-to-day you're not thinking about it whereas in phoenix
[3164.74 → 3170.42] we very we coexist with plug at a much finer level so you have to be kind of aware of the plug
[3170.42 → 3176.34] concepts and any kind of middleware or any kind of like uh filtering you do on a request is all
[3176.34 → 3184.50] happening um with a plug API interesting so it looks like you just released 0.10
[3185.78 → 3188.82] um with a bunch of goodies in there including live reload support which
[3189.30 → 3194.34] kind of amazes me because I've never seen live reload done without an extension
[3195.22 → 3199.62] which I'm assuming you're just using the web socket support to kind of shove that in there
[3200.42 → 3204.66] yeah so that yeah 0.10 is super exciting for me just because we've we've gotten we've like
[3204.66 → 3209.06] streamlined the development experience so like it feels like I have an I have a more enjoyable
[3209.06 → 3212.74] development experience um today with phoenix than I do rails at least you know starting out
[3213.38 → 3220.02] so with live reload since we have the channel web socket layer built in we basically thought you know
[3220.02 → 3224.50] last month I was like wait a second why can't I just inject that a little bit of JavaScript on the
[3224.50 → 3230.82] into the body of your HTML page and then watch the file system for changes and just basically
[3230.82 → 3236.58] dog food our own real-time system so it ended up being like you know 20 lines of code to have live
[3236.58 → 3242.10] live reload work, and it doesn't require node.js doesn't require a browser plugin it's all just
[3242.10 → 3249.06] kind of dog food in our own real-time APIs that is really cool you also have some asset pipeline stuff
[3249.06 → 3254.34] you've got um some new form helpers looks like it's your really adding the goodies now tell us
[3254.34 → 3261.22] about 1.0 and then give us a just brief overview of what you see for the future of phoenix sure
[3261.22 → 3268.50] yeah so uh 1.0 is basically like we said going to be a full stack uh framework we have we are using uh
[3268.50 → 3274.98] we're using brunch which is a node uh build tool for asset compilation um so we didn't want to write our
[3274.98 → 3279.70] own asset pipeline because we didn't think I mean there are mature uh solutions out there so we
[3279.70 → 3286.10] evaluated like half a dozen of the popular node options I have like huge amount of hours in that
[3286.10 → 3292.26] but we ship with you know you just throw your CSS and your es6 JavaScript uh SAS into a specific
[3292.26 → 3296.90] folder it just gets compiled so you don't really have to think about um brunch or node or anything it
[3296.90 → 3302.10] just works a little bit pre-installed on your machine or something yeah if you install phoenix it
[3302.10 → 3306.18] will detect that you have node installed and automatically set it up so if you have node
[3306.18 → 3311.78] installed already it would just work um otherwise you can forego the brunch integration but then you
[3311.78 → 3318.90] just have to build your own build tool um, but we have an uh good asset story uh real-time events is in
[3318.90 → 3325.30] for 1.0 so I think you know for now from here until I think the end of April which is elixirconf EU
[3325.94 → 3330.18] is what we're targeting for a 1.0 release it's just going to be about stabilizing the APIs
[3330.18 → 3334.42] there's some channel work that I want to get in place that is going to make channels uh a little
[3334.42 → 3339.78] nicer to deal with at like the concurrency level, but it's kind of an uh implementation detail uh but
[3339.78 → 3344.66] but the biggest feature remaining for 1.0 uh I haven't mentioned yet is being able to replay channel
[3344.66 → 3350.10] messages so if I'm online if I've written a chat app in phoenix and I drive under a bridge on my cell
[3350.10 → 3356.98] phone right now you'd miss any of those messages that were broadcasted out through the server so we want to
[3356.98 → 3360.98] be able to buffer those messages on the server and then when the client reconnects after
[3360.98 → 3366.10] they get out of the tunnel it just flushes the buffer so we're going to include that hopefully as
[3366.10 → 3372.10] a 1.0 release with mobile clients and I think that would be a solid 1.0 release to compete with
[3372.82 → 3377.54] with most of the frameworks out there except we should be able to take on the world so to speak as far as
[3378.34 → 3386.90] scalability goes and beyond 1.0 what you got so I have some ambitious goals I'd say
[3386.90 → 3392.66] with my elixir cone talk I talked about distributed services and this is being something that we probably
[3392.66 → 3396.50] uh this would be something that lived under the phoenix framework organization on GitHub but not
[3396.50 → 3403.22] part of phoenix core itself, but the idea is we have you know elixir I haven't mentioned this, but you can
[3403.22 → 3408.90] you write code to run on one machine, and you can run that on 50 machines connected together, and it's
[3408.90 → 3414.18] pretty much the same code, so the concurrency model is distributed at its heart so you don't really
[3414.18 → 3419.62] have to think about um receiving a message from a different um server on your cluster it's all just
[3420.18 → 3426.10] baked into the concurrency model, so the idea there is I want to be able to write a service layer that
[3426.10 → 3432.82] I can spin up multiple nodes running kind of different services so if I have an I'm writing a search engine
[3432.82 → 3439.30] uh in elixir and I'm using phoenix I want to be able to say okay I have a page indexer service that is
[3439.30 → 3444.42] pretty expensive it has to make page requests you know parts the HTML and I know that I can do
[3445.06 → 3450.66] a thousand of those on one box at a time so I want to be able to spin up 10 nodes running that code
[3450.66 → 3455.86] and have them register themselves on the cluster saying hey I can perform the page indexing work
[3455.86 → 3462.34] or hey I can perform the page crawling work and then at my uh at my application level code I just want
[3462.34 → 3468.26] to be able to say hey service page crawler crawl this page, and it will find a node on the cluster that can
[3468.26 → 3473.46] do the work that's available do the work for me and give me a result, so there's the gist of kind
[3473.46 → 3478.26] of the ideas I'm playing with um is there I think there are a lot of hard problems to solve there around
[3478.26 → 3483.70] like you know cap theorem and distributed programming, but elixir enables all that it's really exciting to
[3483.70 → 3489.54] me that that's all possible you're getting a lot of benefits into phoenix itself from elixir
[3490.42 → 3495.14] oh yeah you know choosing the right kind of language and then getting a lot of the benefits from the
[3495.14 → 3500.66] the limits itself yep like I mentioned in my uh in elixir cone talk too like if you're running
[3500.66 → 3505.78] channels you can, I'm running channels on 10 different machines I could have one machine dedicated to
[3506.82 → 3511.38] streaming twitter results and if I find something interesting on Twitter it can broadcast it out on
[3511.38 → 3515.62] a channel and that would show up in the browser so as long as it's connected to the cluster I could you
[3515.62 → 3520.82] know like I said have one machine dedicated to doing these things, and you just push out an event and it
[3520.82 → 3525.94] gets really rich uh broadcast out to any listeners on the cluster and that's just built in that's just
[3525.94 → 3532.10] the concurrency model is I send you a message it's just going to go over the network, but the process could
[3532.10 → 3536.90] be you know located on any machine, but it's the same as if I was writing that for just my laptop
[3537.70 → 3543.30] it's pretty cool it does sound pretty cool so let's talk about getting into the closing here for the call
[3543.30 → 3548.82] just uh for listener’s sake I've been waiting to ask this because I've been biting my tongue over here on
[3548.82 → 3553.70] getting started because I feel like you got so much stuff that we've talked about for those who
[3553.70 → 3559.54] could be coming from ruby so maybe an uh you know a similar look to the syntax but once you get deeper
[3559.54 → 3564.98] in is as we said before it's not the same um but still some of the fundamentals some of the DNA of rails
[3564.98 → 3570.50] is in phoenix and so you kind of have a home away from home but how do you get started I know that elixir
[3570.50 → 3577.06] 1.0.2 or plus is a requirement is elixir on most machines how do you yeah well how do you get to
[3577.06 → 3583.30] start with elixir or with elixir now so phoenix sure so elixir yeah elixir Lang elixir hyphen
[3583.30 → 3589.30] lang.org has getting started guides for pretty much all major platforms so if it's is you're on a Mac
[3589.30 → 3595.86] you can do a brew install elixir uh if you're on Linux it's just you know apt um so it's easy to get
[3595.86 → 3601.54] running um elixir itself and then for phoenix we have phoenix framework.org getting started guides as well
[3601.54 → 3608.82] um and just takes you step by step um you should have an um an app up and running um with you know
[3608.82 → 3612.90] live reload and assets and in under you know a couple of minutes I think you know in the latest
[3612.90 → 3618.18] 010 release video I showed that where you just run mix phoenix new it generates a new project and
[3618.74 → 3624.10] sets you up, and you're ready to go well I'm just about a minute or two what's the what's the hello
[3624.10 → 3627.78] world the perfect hello world for someone listening right now to jump into
[3627.78 → 3633.30] the perfect go towards if they're going to build something with phoenix I'd say like a little a
[3633.30 → 3640.10] little chat app I have I put a little example out um like the chat app is like the uh the real
[3640.10 → 3645.30] time to-do list type thing like if you're on if you're coming from like node or meteor JS you're like
[3645.30 → 3648.66] oh I can make a chat app so easily but I think that's a good one because it just kind of shows you
[3648.66 → 3653.46] how easy it is to push events back and forth uh so I'd say yeah check out a phoenix chat app kind
[3653.46 → 3660.74] of fun to get your feet wet awesome we uh I do want to take a time a second to mention this
[3660.74 → 3665.46] too for those who are listening that are members um we've been working with elixir sips for quite a
[3665.46 → 3672.50] while we've never had a show obviously on elixir or phoenix for that matter but um for those who are
[3672.50 → 3681.22] members we do have a discount with elixir sips it's 77 off 77 off to be more clear um it's about six bucks
[3681.22 → 3687.22] for the first three months so to get started on some of these things I know that I do such a great
[3687.22 → 3694.18] job on uh on you know just exposing a lot of this knowledge so diving into getting deployment started
[3694.18 → 3699.70] all sorts of stuff so you remember taking advantage of that for sure, but we do ask some really awesome
[3699.70 → 3705.86] questions heading out of the show and our favourite to ask is uh who's your programming hero programming
[3705.86 → 3712.66] hero so many doesn't matter I mean just share gotcha so I'd say uh Matt's uh from ruby would
[3712.66 → 3721.38] probably be up there um I think just because it kind of embraced being um happy programmer and having
[3721.38 → 3726.34] a language that kind of put that at the forefront for me was like a breath of fresh air coming into
[3726.34 → 3731.78] ruby where um you know I don't think at least I had no experience where before you know the creator was
[3731.78 → 3736.10] like programming should be you should be happy we should um all be nice to each other, and it should
[3736.10 → 3739.94] be an enjoyable experience and that's kind of the way I feel about programming it's like a's a
[3739.94 → 3746.18] creative process and uh brings me a lot of joy so I think that um has really shaped a lot of people's
[3746.18 → 3752.90] opinions about programming so he'd probably be up there with that another one we like to ask is uh
[3753.78 → 3759.54] if you weren't doing what you're doing now which is building out phoenix on elixir uh using elixir
[3759.54 → 3765.30] what if you weren't doing that what would you be doing um probably something uh like aerospace
[3765.30 → 3772.34] industry I'm a huge space nerd so uh space has always been a passion of mine um so I think something
[3772.34 → 3778.34] in the know planetary science aerospace industry but um from a programming perspective I always think
[3778.34 → 3786.10] that like the Mars rover for example like they update the code on that thing on Mars so i always
[3786.10 → 3791.22] think like you know if there's a bug in my code I get like a something went wrong error page on the
[3791.22 → 3795.30] web browser but I don't know that I don't know that I would have the stomach for that industry
[3795.30 → 3801.30] just like you know rake deploy, and you know it's running on Mars so I think um yeah definitely space
[3801.30 → 3805.14] is a huge interest of mine and I wait like two and a half years or something for your code to get out
[3805.14 → 3809.78] there right yeah well you have to yeah like best case like some people you write code and then 10 years
[3809.78 → 3814.42] later you're yeah you're hoping it works so I think uh well I'm I'm super passionate about that so
[3814.42 → 3822.02] something along those lines that's funny um I guess a good another good one for closing out is a
[3822.02 → 3828.26] call to arms to your projects' elixir phoenix um you know where are some ways that the community
[3828.26 → 3833.38] listening to the show now could step in where's a good place to either help out with the language itself
[3833.38 → 3839.22] or help out with the framework and join the core team or help out where's a good place to start
[3839.22 → 3846.02] yes so uh phoenix framework.org is uh the best place to start and also elixir Lang IRC
[3846.66 → 3851.06] is um you know I live on there I'm probably on there too much but I'm happy to help anyone out
[3851.06 → 3857.14] that wants to jump in and I think um if you already have some experience in elixir um you can always
[3857.14 → 3860.82] you know contribute and give back whether it's helping someone else out that has questions or
[3861.54 → 3865.70] now is kind of a great time to get in early and start putting together third-party packages
[3865.70 → 3871.14] so like you know the plug middleware that we talked about um that's kind of the open season
[3871.14 → 3875.70] for if you want to build you know a first class authentication system kind of all these different
[3876.34 → 3880.82] big uh checklist items that the community doesn't have, yet you know start building something and
[3881.30 → 3884.66] might find a problem that's not solved, and you can solve it and kind of give back
[3886.10 → 3890.90] awesome and uh what is your GitHub what is your twitter how can people follow you to kind of keep
[3890.90 → 3896.82] up with you in general besides IRC when you're sure it's uh Chris underscore McCord on Twitter
[3896.82 → 3902.34] and then just Chris McCord on GitHub awesome Chris anything else you want to mention as we close out
[3903.38 → 3907.94] uh like I said I just published uh metaprogramming elixir on prorogue oh yeah so check that out
[3907.94 → 3912.74] uh if you are that pre-order now or is it uh available now it's out it's been out for about
[3912.74 → 3919.06] a month and a half so nice check it out we'll put a link in the show notes for that uh maybe uh
[3919.06 → 3923.78] I'll ask you now do you have any discount codes you can give our listeners I don't at the moment
[3923.78 → 3928.34] but uh I can see what I can do awesome so if you're listening check the show notes we'll see
[3928.34 → 3933.46] if we can get one if we can get one cool if not we'll just uh we'll just flame Chris and RC or
[3933.46 → 3941.22] something like that no problem also uh check out elixir cone uh EU it's uh end of April in Kraków
[3941.22 → 3945.62] Poland and I'll be there uh talking about phoenix so it should be a lot of fun we've got the
[3945.62 → 3950.98] José creator of elixir be there and the creator of Ealing Joe Armstrong is also giving a keynote
[3951.54 → 3956.34] so it should be pretty cool stuff all right well that's it for this show everybody thanks for
[3956.34 → 3963.22] listening to uh this great conversation i I love the know I was quite silent in this one just
[3963.22 → 3967.46] because some of the stuff is over my head when you said OTP I was thinking something else but uh
[3968.42 → 3972.90] you know great conversation today, so thanks for coming on the show and uh with that let's say goodbye
[3972.90 → 3983.30] see you
[3991.54 → 3993.38] oh
[3993.38 → 4023.36] We'll be right back.
