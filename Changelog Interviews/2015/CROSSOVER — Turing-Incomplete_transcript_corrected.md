[0.00 → 15.86] welcome back everyone this is the change log and I'm your host Adam stekowiak this is episode 173
[15.86 → 22.18] and on today's show we're joined by Pam seller person Darry Justin Campbell and Len smith the
[22.18 → 28.08] folks behind Turing incomplete it's a new podcast which can be found on the web at Turing. Cool
[28.08 → 32.30] great show today where we connect with fellow podcasters out there discussing open source
[32.30 → 38.34] software development podcasting building community and more we had four awesome sponsors coach
[38.34 → 47.68] image harvest and also sentry our first sponsor is coachip launched a brand-new feature
[47.68 → 52.80] called organizations a few months back everyone's been loving it now you can create teams you can
[52.80 → 58.26] set permissions for your specific team members, and you can improve collaboration in your continuous
[58.26 → 63.82] delivery workflows you can maintain your centralized control over your entire organization's projects
[63.82 → 70.66] and teams with this new feature it's super awesome, and you can save 20 off any premium plan you choose
[70.66 → 77.48] for three months by using our code the changelog podcast again that code is the changelog podcast
[77.48 → 84.22] 20 off any plan you choose for three months head to coachip.com slash the changelog to get started
[84.22 → 90.26] and one more thing I want to tell you about Sean Devine is doing an API workshop called API first
[90.26 → 96.98] training and guess what he's going to use coach as a demo tool the URL to learn more about that API
[96.98 → 100.54] training is in our show notes so check those out but now on to the show
[100.54 → 115.22] all right everyone we have a bit of a show lined up today's show is cool it's a crossover show
[115.22 → 119.68] where we connect with fellow podcasters out there to discuss open source software development
[119.68 → 125.90] podcasting building community and more and today jarred and I are joined by the folks behind Turing
[125.90 → 131.76] incomplete which can be found on the web at Turing. Cool so please welcome hey I'm sell
[131.76 → 137.02] driven curie Justin Campbell and Len smith and obviously jarred Santa
[137.02 → 145.56] everyone say hello thanks for having me of course hey so I guess the easiest way to open this
[145.56 → 154.38] one up is this your first time being on somebody else's podcast uh it is for me this is Justin
[154.38 → 163.98] for me no Pam it is for me Trevor and me Len as well too okay so I'm what show are you on
[163.98 → 172.60] uh shop talk oh awesome love those guys by the way yeah they're really fun that show's live right
[172.60 → 179.14] mm-hmm so is that super stressful for you or just amazing no it's pretty fun and the only thing
[179.14 → 185.38] is the because it can be a little distracting uh watching the chat flow by uh so you kind of have
[185.38 → 190.60] to i would have to just kind of minimize it um because people are chatting while you're talking
[190.60 → 197.12] which is normal but hard when you're trying to be the one talking we've flirted with live haven't we Adam
[197.12 → 204.62] we have definitely flirted with live we've held hands uh we've uh we've gone out on several dates
[204.62 → 209.90] it just hasn't stuck honestly it's a good idea in theory but I think this kind of show typically
[209.90 → 215.62] maybe not this particular episode but this show in general just seemed to work out better when it was
[215.62 → 223.36] sort of like a one-to-one or a one-to-a-few uh conversations so that's that way it's like sort of
[223.36 → 230.78] tighter more intimate less like pressure to perform I guess you know for a crowd when it's live it just
[230.78 → 235.98] and then also if you listen to Dan Benjamin or anybody else who does live shows the numbers on
[235.98 → 240.36] live shows continue to dwindle while the subscribers and podcast listeners on the actual shows
[240.36 → 246.90] continue to go up and so you know depending upon the show type live can work for you if it's like
[246.90 → 252.00] if it's part of the DNA of the show and where it's this show was never originally live so it kind of
[252.00 → 257.76] never stuck for us, I think when we start talking about live I assumed you meant like
[257.76 → 262.24] sitting at a table in front of a crowd and that i I would be really nervous doing that
[262.24 → 269.90] that to that's tough that'd be even worse before we get too far into things let's lets uh we're
[269.90 → 274.14] going to spend a little bit of time getting to know everyone so a bit of an intro a bit of a little
[274.14 → 280.04] bit of history so we'll start from the top which is Pam so Pam can you kind of introduce yourself to
[280.04 → 285.02] the audience of the changelog and kind of give a bit about uh who you are and if you want to
[285.02 → 289.58] mention your birthday last week you're you're welcome to oh well you know since you mentioned
[289.58 → 297.08] the national holiday my birthday was last week uh so just in case anyone missed it you can mark it
[297.08 → 308.30] for next year um so I'm a developer in Philadelphia Pennsylvania I am known on the internet for a few
[308.30 → 316.58] things notably uh for JavaScript I speak at JavaScript conferences pretty often uh my latest
[316.58 → 322.26] talk is about the streams data structure and how awesome it is and that's where we met when
[322.26 → 332.28] I gave that talk at any at uh Nebraska JS com and i also in real life I also run a JavaScript meetup
[332.28 → 339.28] in Philadelphia we have over a thousand members, and we also run a JavaScript conference here
[339.28 → 346.26] uh two years running and I also wrote a book and I record with these folks on Turing and complete
[346.26 → 351.34] so I do a lot of stuff also I'm working on another book wow what was your book about
[351.34 → 354.42] it's finding your next job as a developer
[354.42 → 358.20] how do you do it how to guide
[358.20 → 364.12] can you give us a secret together we'll let people read the book to find out
[364.12 → 374.06] sure I mean the secret is that you can apply for jobs the really frustrating like to me the
[374.06 → 380.00] really frustrating and inefficient way of gathering your resume and putting a cover letter together
[380.00 → 407.82] and then emailing people who don't care about you who will never call you back, or you can approach it systematically that will with a plan with you know like because there 's is a way to do it and that's really what the book is it's a know you can disagree with the way to do it is does involve a lot of networking, and you know that's like literally so you know how everyone always says like most jobs are found through networking according to BLS data which the way that numbers derived is
[407.82 → 415.02] but anyway about 70 70 to 80 percent of jobs are found through networking and then no one tells you how to do it
[415.02 → 423.98] so what this book is specifically for developers here is how it works and if you follow these steps this is how it works, and it should work for you
[423.98 → 433.68] very interesting yeah quick google search didn't lead me to it with that uh finding your next job as a developer so we'll have to get the link from you later
[433.68 → 445.22] no it's I don't have an I actually don't have a book page where I'm still very much writing it but if you go to the web of war which is my blog i I have a mailing list there and I'm sending out updates to that mailing list
[445.22 → 451.76] so that's where the first beta will be announced um and there are a few posts leading up to that so
[451.76 → 460.20] I did find a link uh to burn your resume when doing that Google search which was to the same site you just mentioned so I assume that's where we can send people
[460.20 → 465.10] mm-hmm yep fantastic all right uh person let's go with you
[465.10 → 472.20] oh man it's hard to follow up after Pam uh I'm a developer in Philadelphia
[472.20 → 481.84] and uh I organized filly Rb which is the Philadelphia ruby user group um and I'm on Turing incomplete
[481.84 → 486.92] and that's about it that's about it on the internet you can find me at person
[486.92 → 494.44] no uh no books no uh no books no books that's not involved in her book writing
[494.44 → 500.14] person also speaks about closure script yeah I was going to mention the closure thing too
[500.14 → 503.66] well we just had an episode on closure last week we had Karen Meyer
[503.66 → 507.34] uh person you may know her as gigasquid talking closure
[507.34 → 513.16] she spoke very highly of closure script yes she sure did she probably turned some heads too with
[513.16 → 518.90] thinking like I should do that yeah, and she wrote a book by the way drawn if you didn't know
[518.90 → 524.38] living closure right living closure that's right that's right Pam's book is still in beta so you
[524.38 → 528.16] know if you sweet talk her maybe you can get a byline on that thing just there you go just a thought
[528.16 → 536.24] just a four word something you know prologue all right Justin what do you think I've heard that if
[536.24 → 541.22] you have um sometimes if you have like a Wikipedia page, and you're not important enough to have a
[541.22 → 546.16] Wikipedia page you'll take it down but one of the things they need is like a source which is a
[546.16 → 550.88] newspaper or book so I guess if you write a book you're important enough to have a Wikipedia page
[550.88 → 557.64] that sounds like a route to take on this one you're about to take is that your is that your intro
[557.64 → 560.46] well no I'm not I'm curious if pat has Wikipedia page or not okay
[560.46 → 567.84] I am uh I wouldn't make my own Wikipedia page how about a book she will have one in about five minutes
[567.84 → 575.14] that'd be a good book how to get your own Wikipedia page and the first step is written a book
[575.14 → 583.18] and then step two is I guess I'm on Wikipedia now dot dot dot step yeah exactly anyway easy
[583.18 → 590.54] so my name is Justin Campbell I'm a software developer also uh as all four of us are I work
[590.54 → 594.62] for a company called hash corp which makes a lot of open source tools and I work on a product called
[594.62 → 604.62] atlas which is uh trying to be GitHub for ops is an easy way to put it hmm uh and I organize a
[604.62 → 609.06] software craftsmanship meetup in Philadelphia called software as craft and occasionally I give conference
[609.06 → 615.84] talks but I've been uh busy not doing uh side project things the past few months
[615.84 → 619.90] sensing I'm sensing a trend of Philadelphia too here
[619.90 → 625.80] yes uh we're all from Philadelphia originally or from the past few years except Len moved to Seattle
[625.80 → 632.74] a couple of months ago yes I'm an I'm I would say I'm a Philadelphian living in Seattle currently
[632.74 → 638.42] my heart's in filly soon to be I was wondering why you're uh why you're not in filly anymore
[638.42 → 644.56] oh uh my partner moved out here for work uh so I followed since I'm in software and can work
[644.56 → 652.76] wherever very cool awesome so Turing incomplete is a Philadelphia joint by way of Seattle
[652.76 → 661.06] yes, yes why don't you guys uh tell us a little bit about the show let's start with kind of the
[661.06 → 666.86] genesis, and then we'll move on to the name which I think is quite cool and then the URL which is
[666.86 → 672.80] literally dot cool I don't think we did a Len introduction either oh we didn't kind of just
[672.80 → 677.72] said that I was currently in Seattle yeah my name is Len smith uh I'm a rails' developer which means i
[677.72 → 683.16] write JavaScript all day and yeah currently in Seattle there you go there you go sorry about that
[683.16 → 688.76] one so yeah I guess the start of turning complete uh person and I had talked about doing a podcast for
[688.76 → 694.76] about a year, and we were wondering who else we would want to be on the podcast and uh Pam instantly
[694.76 → 698.92] came to mind as a friend of ours and somebody who is well known in the Philadelphia community
[698.92 → 704.82] and we both worked with uh Len and I didn't actually know that Len was interested in podcasting
[704.82 → 709.30] until we were mentioning it one day, and he said oh I tried to make a podcast before and he already
[709.30 → 715.72] had like a logo and other things uh well no I didn't try I was always planning on it, I'm just
[715.72 → 722.10] very bad at procrastinating okay commissioned artwork and always plan to do it so the four of us got
[722.10 → 732.36] yes sorry uh yeah i the four of us got together and picked a date and just decided to record and
[732.36 → 740.64] the first one was pam was in India yeah I forgot about that a little bit on how it got
[740.64 → 747.06] started huh well yeah that was okay though this one was absolutely awful uh we didn't, but it was good
[747.06 → 752.12] it was a good practice run and yeah when Justin approached me like I said I've been procrastinating
[752.12 → 756.78] for literally years and I'm like sure I'd be interested, and he's like okay we're going to record
[756.78 → 767.80] tomorrow so that was good and I heard one TDD is dead question mark uh yeah that was right on the time
[767.80 → 775.78] that uh DHH gave his TDD is dead keynote uh in which you guys mourn the death of TDD and then episode
[775.78 → 781.24] two TDD is alive again absolutely there's actually an episode zero that we recorded with
[781.24 → 786.42] another co-worker in front of ours dame McClary uh that was episode zero and that was never
[786.42 → 793.36] published oh not nice well that's what zero is for is you don't put it out there yeah that's the
[793.36 → 800.40] test run although in reality the first five are probably bad well you know that's the that's the
[800.40 → 804.68] fun thing with podcasting you kind of have to grow into it a little bit you know and it is takes i
[804.68 → 813.46] mean Geez jarred if we tell our history our first few are not bad but I think audio quality wise just
[813.46 → 820.26] in general from a podcast what people know of a podcast today they think a little bit more
[820.26 → 826.36] higher quality a bit more put together whereas in 2009 it was just like if you got audio on the
[826.36 → 831.70] internet that's audible it's a podcast what was that service that did the phone thing uh talk shoe
[831.70 → 839.00] remember a lot of podcasts in like 2009 2010 were recorded over like telephone yeah huh I didn't know
[839.00 → 847.04] that one of our actually our first podcast had uh Natalie Feigenbaum in it and uh at the time
[847.04 → 854.70] uh the call had to be done via a phone not from us but for she so that's how it worked out
[854.70 → 863.02] seems like podcasting is kind of like TV shows where certain ones have to kind of get their legs
[863.02 → 866.94] if you judge it by the pilot so to speak you're not gonna you're not going to find too many shows that
[866.94 → 872.12] you like no, but you wait till like six episodes in, or you wait even till season two sometimes in a
[872.12 → 876.98] traditional TV format and that's when things usually start to get interesting did you find it took
[876.98 → 883.64] just a handful for you guys to really uh gel I think it took a handful for us to nail down the format
[883.64 → 890.80] we went I think we still do go back and forth on do we need a topic or should we do a topic
[890.80 → 899.76] uh should we go topic less or yeah it is what is the format then so right now uh we mostly just
[899.76 → 906.96] talk for an hour or so on a call the four of us, and we record, and then we cut it together into a show
[906.96 → 914.54] um the first I would say 20 25 episodes we tried to do a topic every episode if we weren't doing a
[914.54 → 921.20] guest and for me personally that ended up being really stressful trying to like pick a topic before
[921.20 → 926.44] we recorded we'd have a lot of uh tension and anxiety about if we didn't have a topic yet like
[926.44 → 932.44] should we record and i I found like a lot of podcasts I listened to I really enjoyed the
[932.44 → 939.46] conversational style and just kind of friends hanging out uh style recording, and it's
[939.46 → 945.72] really hard also to pick a topic every week and have it be a different topic when you know the four
[945.72 → 951.18] of us have a know at least apart from software development have a diverse set of skills in software
[951.18 → 956.24] development and now, but we're not an expert in that many things uh when you have a guest it's really
[956.24 → 961.08] easy to you know that guest is usually very qualified to talk on that subject, and you can have different
[961.08 → 966.66] subjects every week but for the four of us I found it kind of hard to pick a topic and start talking
[966.66 → 973.74] about things we didn't know that much about but I know other people on the podcast really like to have
[973.74 → 979.32] a topic so when we talked before though Pam you said that you all don't have a topic, and you just sort
[979.32 → 984.80] of wing it is that still the case yeah I mean that's the case now yeah that's what we evolved into i
[984.80 → 992.86] liked the topics but so also our pattern for topics was kind of picking a noun and then that
[992.86 → 999.40] would be the topic and eventually we kind of the well was starting to get thin on nouns that we felt
[999.40 → 1005.82] like talking about or that we felt qualified to talk about yeah I mean there were but now that now
[1005.82 → 1010.28] we just talk about things we're unqualified to talk about so it all works out mostly elixir
[1010.28 → 1016.54] mostly you know elixir and JavaScript frameworks well I guess that's a sort of part we kind of
[1016.54 → 1022.08] missed a little bit not so much a full-on deep history of each of you but I guess to get an
[1022.08 → 1029.14] idea of any show like for example uh here at the changelog our roots are in ruby uh jarred and I are both
[1029.14 → 1035.64] in the ruby community we've we've been doing that for a very long time um what would each of you say to
[1035.64 → 1040.72] kind of the kind of program you are or maybe even what your specialties are what you love doing most
[1040.72 → 1047.24] does that play into the role you play in the podcast and I guess if you want to take turns here
[1047.24 → 1053.52] we can start with Pam uh could you restate the question well just like uh you know
[1053.52 → 1058.92] what kind of software developer are you what and is that the same role each of you kind of play
[1058.92 → 1067.86] in you know I think i I'm a Gryffindor but sometimes I people think I'm a Ravenclaw okay and that's okay
[1067.86 → 1075.46] uh because you know I'm really clever um no i I don't really I don't so because I've done a lot of
[1075.46 → 1082.22] JavaScript development I feel like when I get asked this question i I might be misinterpreting
[1082.22 → 1087.84] but I often read it as a subtext of someone saying okay well so you're a front-end developer and like
[1087.84 → 1092.60] that's all you're ever being that's all you ever want to know, and we're not trying to put you in a
[1092.60 → 1099.78] box here no, no not at all generally speaking like yeah i mean work on so like i just i switched to a
[1099.78 → 1104.62] team where I'm doing something totally different I'm not really doing website development anymore
[1104.62 → 1110.36] or working on things that end in a website I'm working on the layer that supports other
[1110.36 → 1117.40] development platforms and so middleware no uh i don't think it would be called middleware
[1117.40 → 1125.48] actually it might be services let's just put it at that services yeah because other people write
[1125.48 → 1134.36] middleware that then uses this so it's the where it's almost like but i do think the that like when
[1134.36 → 1141.64] we do have a JavaScript question we go to either Len or Pam because they're more knowledgeable about
[1141.64 → 1147.84] JavaScript than i mean Pam wrote a book on JavaScript yeah right I'm getting hired now
[1147.84 → 1153.50] too obviously as a developer so i guess what we're trying to do we can go quickly through this but just
[1153.50 → 1157.72] trying to get a heartbeat of like a little bit about your background and how does that play into
[1157.72 → 1163.16] the overall aspect of like how you right each and every week you know define what turning incomplete
[1163.16 → 1169.32] is and what an episode is whether it's a guested show or it's a wing it shows right and also not just
[1169.32 → 1172.70] your programming background but like what your individual interests are and how that comes
[1172.70 → 1177.82] together to have it's cool i have some shows where it's you know it's interview style it's topical
[1177.82 → 1181.56] you have other shows where it's like hey it's for people who love programming, and we talk about it
[1181.56 → 1186.86] which sounds like that's the kind of show that turning incomplete is absolutely and just to give you
[1186.86 → 1191.68] know our listeners a bit of an idea not like how the show goes but just the people that they would
[1191.68 → 1195.24] be hanging out with like what are your guy's interests and what are the kind of things that are
[1195.24 → 1199.60] talked about we know that JavaScript is one of them but I'm sure there are plenty of things that you
[1199.60 → 1205.52] guys dive into we're interested in functional programming i think that's a bend that we're all
[1205.52 → 1212.54] interested in talking more about yeah i listened to a show uh i think it was number 59 evil leader
[1212.54 → 1219.80] um where there was a lot of elixir talk going on you guys have mentioned elixir i think by name i think
[1219.80 → 1228.50] person or Justin did um who's the elixir fans uh, and you know give us some information on why you're
[1228.50 → 1234.28] into that i mean yeah for me, i mean it's weird because we tend to talk what we're about what
[1234.28 → 1240.22] we're excited about which isn't necessarily we do all day sure you know what we do for our day jobs
[1240.22 → 1245.04] i think starts to get a little boring after a while, and then we play around with something for a couple
[1245.04 → 1249.30] hours at night and that's what we're most excited about yeah i think for a bunch of us that's been
[1249.30 → 1255.46] a perfect summary of it yeah that like yeah we do our day jobs, but we end up talking
[1255.46 → 1259.26] about so we each have our own wins which might be what you meant in your original question
[1259.26 → 1268.16] so I'm into JavaScript stuff and math stuff and new research that comes out I'm trying I'm not good
[1268.16 → 1273.88] at security but I'm trying to learn more about it uh so that's something that always fascinates me
[1273.88 → 1280.90] so uh any practical steps or even just tips you can give our listeners anybody who else is interested
[1280.90 → 1288.36] in learning security have you made any progress or found any good resources um you know i try and i
[1288.36 → 1294.92] kind of i follow a few more people on Twitter that i do and i read their blog posts i also joined the
[1294.92 → 1304.28] so simply secure is a non-profit that focuses i would say they focus on usable security because
[1304.28 → 1311.22] the biggest hole in security is humans and so by fixing user well by improving just mirror like if
[1311.22 → 1318.78] you've ever downloaded GPG tools you will deeply understand why such a non-profit needs to exist
[1318.78 → 1325.54] uh to improve user experience so if GPG tools is supposed to be a tool so GPG tools is a downloadable
[1325.54 → 1332.94] suite of things that enables you to use um PGP encryption technology pretty good privacy
[1332.94 → 1341.22] um which is generally a good idea uh because everything on the internet is like all your emails
[1341.22 → 1346.82] are basically postcards flying over the internet so if you want them to not be postcards maybe you
[1346.82 → 1351.58] should learn a little bit about encryption or at least learn how to use it and so simply secure is
[1351.58 → 1360.56] a slack that a lot of um people i think are fascinating are on so like crypt is someone on
[1360.56 → 1365.80] twitter who i think their stuff is really cool, and they just joined this slack, and so I'm like oh my gosh
[1365.80 → 1370.78] they're gonna you know i can see what they're talking about and there are different rooms on research
[1370.78 → 1376.74] and design and crypto so you can kind of keep track of what people who i would think are
[1376.74 → 1382.34] experts think of this kind of stuff very cool Jason how about yourself uh interest either inside of
[1382.34 → 1388.78] work or outside of work things that you dabble with in the development world um what are you into
[1388.78 → 1397.36] um these days I'm really into Emacs and uh closure slash closure script uh closure script
[1397.36 → 1408.66] seems easier for me to use at work or my old job but maybe closure will be easier now um yeah I'm just
[1408.66 → 1415.10] having a lot of fun these days improving my tool chain which is where Emacs comes in awesome so we've
[1415.10 → 1418.22] been considering this show I'll kind of give you there's a little behind the scenes here at the
[1418.22 → 1425.22] changelog we've had a show we've been considering uh which is kind of editor wars, and it's its kind of
[1425.22 → 1429.84] you know it's a play on the fact that everybody gets so excited and passionate about their editor
[1429.84 → 1437.10] but the idea is to get you know kind of three or four um not experts but people who are kind of
[1437.10 → 1443.78] outspoken in specific camps of vim and Emacs and so on Adam um and i have a short list of people that
[1443.78 → 1450.10] i like to have on except for in the Emacs area I'm not really sure like who is a prominent Emacs user
[1450.10 → 1455.66] that people look to as a source of information or aid could you help me out with that is there
[1455.66 → 1458.38] somebody in the Emacs world that uh we should have on the show
[1458.38 → 1461.30] hmm me no
[1461.30 → 1463.62] see that one
[1463.62 → 1467.72] I'm not sure if i have to look into that uh
[1467.72 → 1472.82] i think who's the who's the person who wrote closure brave and true
[1472.82 → 1481.10] uh i don't know i forget his name but necromancy he wrote the line tool he's really helpful on the
[1481.10 → 1489.46] Emacs channel okay i think he also is involved with the ergo docs keyboards um what are those
[1489.46 → 1499.50] it's a very ergonomic keyboard that Len has okay um Len you want to explain that what's the um
[1499.50 → 1504.30] yeah just to make basically make yourself look really elite it's like a split keyboard mine has
[1504.30 → 1510.70] no keycaps, and you program it to do all kind of things so it's its nice and ergonomic, and it has
[1510.70 → 1519.42] fewer keys than a normal keyboard, and you can basically switch layers so uh basically your arrow keys your h j k
[1519.42 → 1524.28] l and vim uh you can switch a layer and make those actual arrow keys, and then you can pop back up to a
[1524.28 → 1530.52] different layer and there's all kind of uh hacks new that i haven't dived that deep into yet
[1530.52 → 1534.26] that's amazing you're so elite that you need less keys in it
[1534.26 → 1542.12] but i did want to mention max i think the editor kind of making waves or the configuration
[1542.12 → 1548.36] making waves now and what brought me on board to Emacs is space max which is highly controversial
[1548.36 → 1556.76] in each world because it basically ships with like complete vim key bindings and i was very skeptical of
[1556.76 → 1563.40] that uh because normally that means like some movement keys work and a couple macros work and that's it
[1563.40 → 1570.76] but it is like a very complete vim implementation i was hacking around an absent-minded lead because i was
[1570.76 → 1576.52] just forgot that i was not in vim uh i used uh one of the plugins in vim a popular plugin called uh
[1576.52 → 1582.36] surround dot vim and i did like change surrounding parentheses, and it worked and that just blew my
[1582.36 → 1587.96] mind um so it's a weird shift because a lot of people are coming to Emacs through space max but
[1588.36 → 1594.76] it's basically vim and i think i even said recently that vim is still my favourite or space max is just a
[1594.76 → 1601.48] better vim than vim is hmm so that's interesting um I'm an old-time vim user but I'm one of the
[1601.48 → 1607.56] my old time i mean like 2001 2002 so I'm sure there's neck beards who are way older than that
[1607.56 → 1613.40] um so I'm not that elite but I'm one of the vim users who don't like vim like i have it ingrained
[1613.40 → 1619.08] in my fingers but I don't think it's that awesome I mean it's good um but I prefer like I actually use
[1619.08 → 1626.36] sublime quite often and um as my main editor mostly I use vim as kind of secondary editor and on servers
[1626.36 → 1633.16] but one thing sublime ships with is like vim mode where um you can use some of the vim key binding so
[1633.16 → 1636.44] it kind of seems like it's a little bit similar to space max in the sense of it's like this merging of
[1636.44 → 1641.40] the two worlds and at first I thought that's amazing I can use my vim key bindings inside of sublime
[1642.36 → 1647.48] but in reality it didn't really work out so well it's kind of like the uncanny valley where it's like
[1647.48 → 1654.84] so close to vim without actually being vim that it actually frustrated me uh non-stop so I wonder
[1654.84 → 1659.56] how space max avoids that problem or if you've actually had you felt the uncanny valley at all
[1660.60 → 1666.44] no and i I did feel the same thing i I try to use vim mode in a sublime and ruby mine and there's
[1666.44 → 1670.92] just you'll do something, and it doesn't work and then that's just the most frustrating thing and I've
[1670.92 → 1677.16] found next to nothing that doesn't work in space max awesome yeah we might need to get the
[1677.16 → 1682.36] space max developer on the show we actually had somebody ping us Adam yeah about having space max on
[1682.36 → 1688.04] the show and that kind of was what got me the idea of the editor editor editor war show yeah but uh
[1688.04 → 1692.04] that would be a really awesome panel show too I think that I mean obviously everybody can bring
[1692.04 → 1697.00] their own rage and their own thoughts and walk away with nothing of course because
[1697.00 → 1701.56] that's how it always works um it's just like a know tear up battle and everybody leaves and
[1701.56 → 1706.52] nobody gets really right you know to a new side it's just sort of like everybody fights and that's
[1706.52 → 1711.64] really how it works out, but a lot of good conversation like I can avoid that I mean there can
[1711.64 → 1716.20] definitely be good that come out of that well for example you just mentioned the vim mode and sublime
[1716.20 → 1720.28] and I'm sure there are tons of sublime users out there that are listening to the show right now they're
[1720.28 → 1725.96] like what it has that and right so now they're going to go check it out and sort of do the space max you
[1725.96 → 1733.32] know best of both sides kind of thing well we've uh we've definitely gotten a chance to learn a
[1733.32 → 1740.44] little bit more about each of you touring folks and uh see the backgrounds and the influences you bring to
[1740.44 → 1746.12] your show we're going to take a quick break and when we come back I want to dive a little deeper into
[1746.12 → 1750.20] the parts of your show jarred I'm not sure if we got the full complete answer on what training
[1750.20 → 1755.72] complete means no so maybe we can cover that and then love to dive into some of your goals so let's
[1755.72 → 1763.32] take a break when we come back we'll kick off with that image is a real-time image processing proxy
[1763.32 → 1770.92] and CDN and let me tell you this is way more than image magic running on ec2 this is way better it's
[1770.92 → 1778.76] everything your friend and developers have dreamt of output to PNG JPEG jiff JPEG 2000 and several other
[1778.76 → 1784.92] formats and if you're like me, you've ever argued with your boss or a teammate about serving retina
[1784.92 → 1791.56] images to non-retina devices you'll appreciate their open source dependency free JavaScript library
[1791.56 → 1797.24] that allows you to easily use the image API to make your images responsive to any device
[1798.04 → 1804.52] now all this takes a platform and the image platform is built on three core values flexibility
[1804.52 → 1812.36] and quality performance and affordability when it comes to flexibility and quality image has over 90
[1812.36 → 1819.16] URL parameters that you can mix and match to provide an unlimited amount of transformations that you need
[1819.16 → 1825.24] for your images, and they take quality very seriously and because of their commitment to quality several
[1825.24 → 1833.24] top 1000 websites in the world trust them to serve their images now when it comes to performance image
[1833.24 → 1839.24] operates out of data centres filled with top of the line mac pros and mac minis, and they're set up for a
[1839.24 → 1846.12] completely streaming solution this means your images never hit the disk images are served by the best
[1846.12 → 1852.36] SSD based CDM for delivery around the world anywhere extremely fast and while we're talking about
[1852.36 → 1859.40] speed almost all the image processing happens on GPUs this means transformations are superfast when
[1859.40 → 1865.56] compared to competing virtualized environments, and lastly it's all about affordability everyone wants to
[1865.56 → 1872.92] save a buck that's how the world works because image processes close to a billion with a b images per day
[1872.92 → 1880.04] they're able to make certain optimizations at scale and pass those savings on to you to learn more
[1880.04 → 1889.00] about image and what they're all about head to imgix.com slash changelog once again imgix.com
[1889.56 → 1892.68] slash changelog and tell the madam from the changelog sent you
[1892.68 → 1900.60] all right we're back we had a nice pause there and during that pause we had some inner discussion
[1900.60 → 1907.24] about whom the leader of this show might be and there's some controversy I'm not sure Justin you say
[1907.24 → 1911.56] it's len you say it's Justin Pam saying I'm not going to do that I'll just be on the show
[1912.36 → 1918.28] uh who's taking ownership of being the leader of touring and complete definitely Len he's the host he
[1918.28 → 1926.76] he edits the podcast um he cares a lot about like audio quality and uh editing cross talk out he
[1926.76 → 1934.04] does a great job about that um uh it was Justin's uh idea and Justin's production so I vote Justin
[1935.08 → 1937.88] although we do argue that Pam finds a lot of our guests
[1939.24 → 1944.52] Jason used to pick a lot of topics so it's a team effort then yeah it is all right well let's team
[1944.52 → 1951.64] effort the if you want opinions you should go to Justin okay now we're starting to get into the
[1951.64 → 1956.12] good stuff let's figure out the name of the show, so the name of the show is touring and complete
[1956.76 → 1963.00] and we all understand what touring is and the touring tests and things like that or
[1963.00 → 1968.76] maybe some listeners do but if it goes back as far as to explain that can we talk about where the name
[1968.76 → 1973.32] came from, and we'll dive into some deeper questions around the podcast itself and goals and things like
[1973.32 → 1978.04] that yeah we were just throwing names around, and we thought it was funny uh I think I might have
[1978.04 → 1988.04] suggested it but yeah Turing completeness is uh a language that can essentially uh implement another
[1988.04 → 1994.20] language is Turing complete or more formally uh anything that is effectively computable can be
[1994.20 → 2001.80] computed by a Turing machine or anything that is Turing complete and so being incomplete means what
[2001.80 → 2007.32] for your show and what should your listeners and guests I guess we are not universally computable
[2007.32 → 2013.08] I guess I mean it was just a really means nothing it's just a play on words, although the main name is
[2013.08 → 2019.32] pretty awesome Len picked that out that he found a Turing. Cool yes that is a cool uh no pun intended
[2019.32 → 2025.96] well actually it is uh that is cool I like that it's not as cool as abc.xyz but
[2025.96 → 2029.96] yeah well we're not right up there it's right up there we're not all alphabet
[2031.64 → 2037.72] so what are I thinking when our listeners and any listener of any podcast you know some come to
[2037.72 → 2042.68] this show for the technical content some come to it because of the person that's on the show
[2043.24 → 2048.12] uh you know it's just really a mixed bash of why people listen to podcasts but I know it's
[2048.12 → 2052.52] at some point in the back of everyone's minds they're thinking like what's the point of the show
[2052.52 → 2059.16] like what are your goals for the show is it to get rich you know what is it that drives you all to
[2059.16 → 2065.40] do this show for a year once a week accumulate 60 episodes do a great job at producing the show and
[2065.40 → 2071.08] all that good stuff like what is it that drives you and what are some of your do you have any goals
[2071.72 → 2077.24] well I would say um probably half of our listeners are Philadelphia-based, and they just know about us
[2077.24 → 2082.20] because we are a Philadelphia podcast and there's only I think a few technical podcasts in Philadelphia
[2082.20 → 2090.12] um yeah my goals are just I just enjoy recording with the other three people and
[2091.00 → 2095.32] just like talking about I work remotely so I don't get a lot of uh face-to-face interaction
[2095.96 → 2101.80] and just general chatting about technology so i just really like every week just talking about
[2101.80 → 2106.76] whatever is on our minds yep same for me, I mean I want to talk about software anyway so why not just
[2106.76 → 2112.12] record it and make a podcast out of it well it takes more time more effort more coordination
[2112.12 → 2119.08] um just for a few reasons it seems like i I agree with that being a remote worker myself one of the
[2119.08 → 2125.80] reasons I got involved in the changelog was so I could talk to people about what I do you know and
[2125.80 → 2132.04] uh being an independent contract contractor as well I tend to your know work on projects by myself or in
[2132.04 → 2138.36] very small teams, and so I was excited to not just talk to um people in the community but also to get a
[2138.36 → 2142.60] chance to you know pick the brains of people who are smarter and way better at programming than I am
[2143.24 → 2149.96] um so I definitely agree with that motivation um yeah and I think there's got to be more to it right
[2149.96 → 2154.36] well so uh for me personally when I first had the idea of I want to record a podcast
[2155.56 → 2164.60] a lot of podcasts I listened to were more surface level uh software engineering and community and
[2164.60 → 2170.76] uh didn't really get into like technical details of things and I don't know if we've succeeded on
[2171.40 → 2176.44] uh that goal of mine to be more technical podcast uh, but that's that's one of the reasons i
[2177.40 → 2181.72] wanted to make a new podcast originally so let's dive a little deeper into the topic than and then
[2182.28 → 2186.76] when one thing you guys said earlier which is something jerry we sort of deal with as a symptom of
[2186.76 → 2192.92] us is we're not experts in every subject that we cover here at the changelog so do you all feel the
[2192.92 → 2200.28] same pressure to somehow perform or be a subject-matter expert or is it that is that what you lean
[2200.28 → 2205.40] on guests for yeah I think leaning on guests for that definitely helps we've definitely had a lot of
[2205.40 → 2211.96] episodes where we just blabber about uh whether it's JavaScript frameworks or languages we're trying
[2211.96 → 2218.44] or uh editors like I don't think any of us have been using Emacs for more than a few months maybe
[2218.44 → 2223.64] person's been using it for more than a few months uh we talk about that a lot we talk about JavaScript
[2223.64 → 2229.08] frameworks and things that we're just trying out uh we talked about elixir uh a lot recently
[2229.88 → 2234.44] and I don't think any of us would consider ourselves experts in any of those topics uh so yeah we don't
[2234.44 → 2240.36] really have any fear of just chatting about what we're trying to do you think it's fair to say that to that
[2240.36 → 2246.12] you're all practitioners in said fields that you represent obviously, and you're sort of coming together
[2246.12 → 2251.48] and just sharing notes to a degree and maybe diving a bit deeper into the unknowns or the knowns
[2252.44 → 2258.84] yeah that's one way to put it I suppose somebody else can maybe elaborate on that yeah I think having
[2258.84 → 2266.76] guests is a good way to for me to kind of get to talk to that person or give that person a reason to
[2266.76 → 2275.96] talk to me and for me to pick their brains about whatever we both have interest in and then originally
[2277.24 → 2282.84] I had said to Justin we have all these interesting conversations it would be nice to record them and
[2282.84 → 2290.92] go back to listen to them in case I forget or to share them um, and then it's just a good opportunity to
[2290.92 → 2301.88] catch up or get valued friends opinions on certain things what's the sequence of it is it weekly is
[2301.88 → 2309.24] it semi-weekly is it does it say it's weekly what's uh what's your frequency it's semi-weekly, and we're
[2309.24 → 2316.44] still going to see if we can schedule time that we record this week so we aim for every week okay so
[2316.44 → 2320.76] that was jerry that's kind of like us, I mean we can lament a little bit with that because we did aim
[2320.76 → 2328.20] to be weekly and I would probably say that uh we aimed to be weekly mainly because there was no one
[2328.20 → 2334.44] doing it full-time and as of February this year I stepped away from my full-time job of pure charity
[2334.44 → 2340.76] where I was a product manager um to finally step away to do the change law full-time so I guess
[2340.76 → 2345.48] since then jerry we've been pretty good at being consistent wouldn't you say yeah I mean I think the game
[2345.48 → 2352.36] changes when a show is sustainable you know financially for somebody to put a full-time
[2352.36 → 2357.96] effort into it, and so I think that has really stabilized us and allow us to ship an episode
[2358.60 → 2364.44] each and every Friday which has been awesome um it's good about the financials too yeah up until then
[2364.44 → 2370.12] you know it's its a struggle there's scheduling conflicts especially with guests it's difficult
[2370.12 → 2374.04] because you have guest scheduling conflicts but I think with Turing incomplete probably your guys
[2374.04 → 2380.44] that scheduling is difficult because you have four regulars right it's more people to line up every
[2380.44 → 2386.52] week yeah we just recently decided on a time that we're just going to record every week um and then
[2386.52 → 2390.84] we're going to ship the same day every week so we've been doing that for a few weeks now and I think we've
[2390.84 → 2397.00] missed probably half of them or have to be scheduled uh so we're still trying that trying to adjust to that
[2397.00 → 2401.24] well guidelines is what it takes though you don't always have to like to hit those marks, but it's good to
[2401.24 → 2405.80] at least have them so you know what the expectation is of where you're trying to go you know so some
[2405.80 → 2411.56] goals in place so jarred you mentioned financials for us and that sort of allowed me to step away
[2411.56 → 2417.32] let's talk a bit about I guess financial matters for you all when it comes to goals is part of your
[2417.32 → 2422.36] goal to be sponsored will you ever be sponsored do you care about sponsors do you care about making
[2422.36 → 2431.24] money at this we actually had I guess debates over whether we should be sponsored um when we
[2431.24 → 2438.12] were trying to get stickers, and sometimes we debate to uh editing if we should pay someone to edit and
[2438.12 → 2446.84] if we should get sponsorship for that I don't think our goal is to make money from it um maybe have it
[2446.84 → 2453.96] sustain itself eventually but yeah any other thoughts on that i I think right now we don't
[2453.96 → 2459.80] have the listenership to really make that sustainable and I don't think we like our show is much less
[2459.80 → 2466.76] edited than your guys show like talking at the time we put into it um basically my workflow is to take
[2466.76 → 2473.64] our Skype call and uh just run some filters on it and put it on s3 so our costs are very minimal
[2473.64 → 2479.40] so we're not super worried about it if we did move to like a know a sponsorship model we
[2479.40 → 2484.52] would need to put a lot more production into it, I mean this isn't the podcast method we love Dan
[2484.52 → 2488.36] Benjamin around here we're on five by five syndicated through five by five we got a good relationship with
[2488.36 → 2494.36] them, and he shares tons of good advice but I think at the same time you know and jarred maybe help me with
[2494.36 → 2499.72] digging deeper into this but I feel like there's something that not something good or bad but something
[2499.72 → 2505.48] changes when it does make money like it has to, or it needs to sustain itself you know
[2505.48 → 2510.28] there are some services to pay for whether it's an editor or whether it's you know hosting services
[2510.92 → 2516.04] whatever you can think of I know s3 bills are tiny when it comes to you know podcast weight but
[2516.68 → 2522.60] um there's something that shifts when it becomes like a paid thing like you have to get not so much more
[2522.60 → 2529.56] serious but like an edge of professionalism that not so much you all don't have but that you are required to
[2529.56 → 2534.60] have whereas now you all can walk to it and say this is fun I enjoy doing it had fun at the end of the
[2534.60 → 2539.56] day or if it know got to the point where you all have said that you don't really want to go which
[2539.56 → 2544.36] is getting it sponsored it might make it too serious and take the fun or joy out of it would do you think
[2545.88 → 2554.84] I think that's where like Len and I think Justin are both kind of coming from I'm on team get money get paid
[2554.84 → 2566.20] but nice but like that's generally a life motto but I mean I respect the rest of the podcast decision
[2566.76 → 2569.48] the joker said it best if you're good at something don't give it away for free
[2571.08 → 2575.72] who said the joker yeah and uh okay so okay I would
[2575.72 → 2581.64] I like I prefer to take my quotes from like Oprah or something okay you know maybe not
[2583.08 → 2585.08] a deranged character
[2587.72 → 2592.92] well you know he did stab he did take the pencil and put it in the guy's eye and explain why that
[2592.92 → 2595.16] made sense because he made it disappear
[2597.24 → 2601.40] or so he's very logical is what you're very yeah very, very logical I'm with you though Pam so
[2601.40 → 2607.48] take me deeper there so why are you on team make money team get paid what is it for you and
[2607.48 → 2613.88] can we sway everyone else on this show now to be on that same team no I mean it's that if
[2616.12 → 2624.92] so I mean it's the question of can you take money and not compromise your integrity and I think
[2624.92 → 2631.32] that that that is kind of a personal level I mean I would be I guess the only contingency
[2631.32 → 2636.68] for being able to take money and take and keep your integrity is the ability to walk away if the
[2636.68 → 2641.64] money has to stop and so as long as you're willing to walk away if the money has to stop
[2642.20 → 2648.28] and so I mean i we deal with this with the JavaScript meetup like if we know we get sponsors and if
[2648.28 → 2654.28] ever a sponsor said well you know um we're I don't know we're terrible people, and we want to
[2654.28 → 2658.92] discriminate against this person because of something about them that they can't change or something
[2658.92 → 2662.52] and we're going to pull our money, and we would say okay great take your money and leave bye
[2663.32 → 2668.36] uh that's that's what we would do and that's how we would maintain our integrity and I think that
[2668.36 → 2675.96] just goes for I would apply that to every context so I don't see a problem with taking money so long as
[2675.96 → 2681.08] and it's a negotiation you say like when someone says hey we want to you know sponsor your
[2681.08 → 2686.60] meetup, and we want to come and do a sales pitch to your people, and we want to get their emails and
[2686.60 → 2692.92] their names and their phone numbers afterward we say no because that's not, that doesn't jibe with
[2692.92 → 2699.40] integrity for us, and so I don't see a problem with taking money in the podcast Len doesn't think we
[2699.40 → 2703.72] could get money on the podcast I think that we could get money in the podcast I think we could
[2704.36 → 2710.20] but basically the way the discussion was solved as i just I want to share this is that
[2710.20 → 2715.80] I was like all right lets you know I'm sure I can go get money, and then we can, you know pay for the
[2715.80 → 2719.88] stickers and stuff and then Justin just put in an order for stickers and that was how it was resolved
[2720.36 → 2725.24] and it was fine because then we had stickers, and now we actually have a link where people can order
[2725.24 → 2730.28] their own sticker so that's true very nice what's the link yeah what is that link it's on it's
[2730.28 → 2737.16] on the website so it's right on the first page awesome touring. Cool touring. Cool let's just keep
[2737.16 → 2743.64] saying that domain many times we can because it's so that cool um very cool well I think I like that you
[2743.64 → 2748.04] you guys have you guys have thought through this you know kind of where you stand it sounds like if
[2748.04 → 2753.96] money or sponsorship presented itself to you um maybe it wouldn't be something you're like uh
[2753.96 → 2760.20] antagonistic to but not necessarily a goal I'm not opposed to it personally yeah not too many people
[2760.20 → 2764.68] who are like diametrically opposed to getting paid uh for to do something they already are doing for fun
[2765.40 → 2772.28] um but have you guys ever heard the term pod fading I don't know if this is still around
[2772.28 → 2776.92] there is an urban dictionary for this is that what happens when we stop publishing yeah so it's
[2776.92 → 2784.92] kind of this phenomenon where podcasts will fade away and uh I saw some statistics a while back
[2784.92 → 2789.48] completely unsubstantiated I won't link them up because I don't even know if they're 100 true but
[2790.20 → 2794.68] that the majority of podcasts will fade out before they hit double-digit episodes like you're either
[2794.68 → 2798.68] going to fail like right away, or you're usually going to stick around for a while so we do have to
[2798.68 → 2803.16] take a speaking of sponsorships we do have to take a break to hear from one of our awesome sponsors
[2803.96 → 2809.64] but when we get back I want to talk about pod fading with you guys and maybe give tips and tricks
[2809.64 → 2814.60] on how not to fade out because you've made it to 60 which means you're statistically better than a lot
[2814.60 → 2821.40] of other podcasts out there yeah so you're going to share all your uh secrets when we come back
[2821.40 → 2827.40] on the other side of the break we're right back for those out there working solo or on a team
[2827.40 → 2833.88] tracking time you thought you were wrapping up a project until the client or your boss asks for a
[2833.88 → 2838.36] new feature at the last minute and here you are stuck you're not sure how much time you're spending
[2838.36 → 2844.28] on every feature how much time you're spending on bug fixes or tweaks well harvest is a time tracking
[2844.28 → 2851.24] tool built for understanding where your time is going and for developers it takes the pain out of time
[2851.24 → 2855.96] tracking just install the harvest Chrome extension, and you can start tracking time right from issues in
[2855.96 → 2861.56] JIRA or GitHub, and you won't have to go searching for your timesheet not only will you understand
[2861.56 → 2866.36] how much time you're spending on client work you'll also be able to turn your billable hours
[2866.36 → 2872.20] into an invoice from harvest in minutes harvest integrates with stripe and PayPal to make sure you
[2872.20 → 2876.44] get paid fast and on time there's built-in reporting in harvest that lets you see how much
[2876.44 → 2881.80] time your projects took so you can use that information to make better estimates in the future for
[2881.80 → 2885.72] a better way to track time and invoice your clients and take the pain out of what you're
[2885.72 → 2892.28] doing when it comes to tracking time and invoicing head to getharvest.com create a 30-day free trial
[2892.28 → 2897.64] and after your trial is over here's a goodie for all of our listeners enter the code changelog to save
[2897.64 → 2905.32] 50 off your first month once again getharvest.com create a free 30-day trial and after that trial is
[2905.32 → 2914.36] over enter the code changelog for 50 off your first month enjoy all right you all we are back with
[2915.16 → 2921.64] the good friends from touring incomplete talking about their podcast and I mentioned before the break
[2921.64 → 2931.16] that many podcasts fade into oblivion in fact Adam some controversy during the break yeah changelog on the
[2931.16 → 2939.32] fringe of pod fading what's your take man we were so close we're so close we uh so if you do google
[2939.32 → 2946.76] google search for pod fading or pod fade you'll inevitably find an urban dictionary definition of
[2946.76 → 2951.40] this and in part of that definition it says many podcasts deny their pod fade until it's too late
[2952.04 → 2954.12] and so part of the break was me
[2954.12 → 2963.48] I guess I don't deny the pod fade i but i I know I was denying it until it was too late like that
[2963.48 → 2973.56] really resonates with me because in 2012 August 2012 uh around mid-month um we stopped producing shows
[2973.56 → 2980.28] for our own reasons and i that's not the name of this show but nonetheless, and we didn't resume until
[2980.28 → 2987.32] yeah who was it what which guest was that was it Justin or was it lent hat said we uh we rebooted
[2988.12 → 2992.92] that was oh yeah I missed oh yeah it was Justin I agreed with it okay Justin so Justin said
[2993.56 → 2997.64] the change lot rebooted right and I'm like I don't know about that so then there's that there
[2997.64 → 3002.92] in the lies of the rub of me denying the fact that it was too late like i to me, we're just on a break
[3002.92 → 3008.28] you know it's kind of like we're from a girlfriend it's okay we're still together, and we're going to come
[3008.28 → 3016.36] back so well I have listened to the change log before the break in quotation marks uh yeah and
[3016.36 → 3021.08] then, and then it pods faded right and then uh and then I heard some news about oh the change log is
[3021.64 → 3028.04] starting up again so that that implied to me like a reboot yeah so i I don't deny it as a reboot
[3028.04 → 3033.88] internally it doesn't feel like a reboot it feels like uh just like a felt like a just a change you
[3033.88 → 3040.12] know just a resumption of it I guess so we're definitely in the pod fade definition there jerry
[3040.12 → 3045.56] for sure well what I was saying before the break is that you know even the change log when it began
[3045.56 → 3051.00] to fade what had been going for years yeah um and most podcasts don't last that long they usually we
[3051.00 → 3059.80] were 84 episode 84 yeah single digit episodes less than a year um, and you know the hosts decide that
[3059.80 → 3064.60] it's you know you're not priority, or they can't get it going, or it's not as fun as they thought
[3064.60 → 3072.20] it would um but turning complete lasted 60 episodes and you guys haven't faded yet doesn't sound like
[3072.20 → 3078.68] you're planning on it so what I was asking before was maybe some tips and tricks how do you guys keep
[3078.68 → 3084.60] it going always be recording always be recording that's pretty much a yeah that's a good going
[3084.60 → 3092.84] we got a good oh yeah I mean we had a rough patch when Len moved to Seattle okay so dealing with time
[3092.84 → 3100.12] zone change, and you know time zones are hard time zones are hard very hard amen why does the sun gotta be
[3100.92 → 3109.72] sun so did it fade a little bit did it fade at all was there we definitely had uh you know non I mean
[3109.72 → 3115.72] Len does most of our editing so yeah we fade a bit what if Len drops out are you guys done, done
[3115.72 → 3120.68] dealing I mean like would somebody else pick up the editing torch I would hope anybody's dropped that
[3120.68 → 3127.48] that somebody else would continue to record and work on it so I've I've edited a little bit too um I'm
[3127.48 → 3134.20] sure Baron and Pam could definitely be capable of doing that not about timing but technology-wise they could
[3134.20 → 3142.52] um yeah Justin often offers to edit and then I get very disgruntled about how his process Len's
[3142.52 → 3148.84] very protective, and he gets disgruntled online too so my my my editing process is uh I write down
[3148.84 → 3153.80] timestamps when we're recording and then I work backwards and I just cut in the end and I cut out
[3153.80 → 3157.40] anything that I wanted to cut out and then I cut in the beginning and then I just run it through a
[3157.40 → 3163.96] couple filters and I ship it Len listens to the entire thing and uh takes out like UMS and the
[3164.92 → 3170.44] and much uh much better final product but I have to imagine it's also much more time intensive
[3171.00 → 3175.40] but even I don't spend that much time my editing time is probably an hour or so
[3176.52 → 3181.56] so I think that's the thing that helped us uh you know keep putting out shows because it's
[3181.56 → 3187.48] it is pretty low time commitment every week it's an hour to record maybe a half hour to plan uh
[3187.48 → 3195.80] uh then an hour to uh edit the show and put up the credits and Justin uh build middleman site so it's
[3195.80 → 3204.28] a pretty quick process to deploy so uh all of our website is open source it's also on GitHub at GitHub.com
[3204.28 → 3211.48] slash Turing incomplete and uh you could see the process so it runs uh Travis so we basically
[3211.48 → 3217.72] just put a new show it goes to like our secret beta site uh and then if everything looks good we can
[3217.72 → 3223.00] make a pull request and merge it, and then it just automatically goes live that's an interesting process
[3223.00 → 3228.28] to be powered essentially by GitHub and Travis because we haven't gone that route we sort of
[3229.00 → 3233.96] do it old school I guess we're still database backed and all that good stuff uh and I guess
[3233.96 → 3239.48] while we're on the subject of process what exactly if someone was trying to replicate or following your
[3239.48 → 3243.72] footsteps what are some of the things that you've learned as part of your process that make it easier
[3243.72 → 3249.88] for four people in different time zones some in the same uh gather once per week and produce a show
[3249.88 → 3255.16] like what is the process you all follow I would say pick a time and show up every week
[3255.16 → 3262.20] so like for example uh recording that's probably the biggest question on some people's minds I mean
[3262.20 → 3266.92] like we have our own recording process and some people don't get it some people do you know you
[3266.92 → 3272.44] know not so much the exact software but like what is your know does one person record everybody somebody
[3272.44 → 3279.00] edits it, and then you know some of the maybe even some of the gear you all use Skype what is
[3279.00 → 3285.96] it that uh powers your podcast yeah so a lot of the things I do are uh based solely on
[3285.96 → 3294.04] reducing the time uh involved to do it so we use a Skype plugin called recorder to record the
[3294.04 → 3299.80] podcast okay so len records on his end and then i also record as a backup okay that makes sense and
[3299.80 → 3306.28] that has all of our voices in it, we just put it into audacity and edit there and combine it all um
[3306.28 → 3310.92] um and call recorder automatically start recording whenever you start a Skype call so there's really
[3310.92 → 3315.80] no fear of like are we recording yet or not it's just it just starts recording as soon as you start
[3315.80 → 3320.60] the call what about like naming your file do you have some sort of special convention is a part of your
[3321.16 → 3327.24] your system is it all detailed in your GitHub README oh yeah it's just uh the episode number so
[3327.24 → 3334.04] we do Turing dash incomplete dash one two three and then the uh the episodes are all numbered in
[3335.00 → 3343.08] middleman blog format so we just have like 55 let's say dot markdown and then there's a YAML uh
[3343.08 → 3348.68] front matter on that which has all the data about the podcast like how big is the where is the mp3
[3348.68 → 3354.20] located how big is it how long is it um what were all of our picks so we generate all those from
[3354.20 → 3361.64] from that file we also recently started using ahead oh yeah that's that's a good one
[3361.64 → 3370.44] you want to talk about that uh so ahead is an I guess collaborative editing app from Mozilla and
[3370.44 → 3378.12] we have the standard format for a post in it as a default, and then we just fill it in as the episode
[3378.12 → 3386.76] goes on and fill out the pics uh at the end of the episode and then I guess we just copy it over
[3386.76 → 3393.72] to the file right we just create a file from the contents of it yeah so when we're recording and
[3393.72 → 3398.20] we're mentioning links we're just copying and moving the links into there so we're almost writing the
[3398.20 → 3405.24] show notes as we're recording very interesting so because that is it EHPAD is that what it is
[3405.24 → 3412.84] etherpad h e r p a d okay we use uh it's an I forget what the actual open source product
[3412.84 → 3416.84] is called might be ether pad, but there are a bunch of different installations you can use, and we use
[3416.84 → 3423.88] the one on uh Mozilla so etherpad.mozilla.org okay I just grab the dot org one I'll grab the other
[3423.88 → 3430.28] link and put it in our show notes yeah so, and it's essentially like a Google uh google wave
[3430.28 → 3436.76] google wave uh amazing you guys should set up your own wave instance for this don't you think
[3438.28 → 3443.88] so does everyone get a chance to log these links or is it sort of you know you and Justin it
[3443.88 → 3450.36] sounds like you and Lynn doing this no everybody records them okay, and it saves time for whoever's
[3450.36 → 3456.44] doing the editing um to have everything already in the show notes and what about file size how do you
[3456.44 → 3461.16] get that is it just a simple thing in the command line then you copy and paste or is it like
[3461.16 → 3465.40] do you run a command like a rake task for example, and it like looks at the file and generates this
[3465.40 → 3470.76] front matter and middleman yeah I've we should have my that I've had them to do this for like I don't
[3470.76 → 3475.16] know since we started recording that it'd be really cool if I could just like to put the mp3 in the right
[3475.16 → 3482.44] place and run a command, and it would fill in the size and length and upload it um interesting so I mean
[3482.44 → 3487.24] that jarred some of this reminds me a little bit of how we evolved weekly because when we talk
[3487.24 → 3492.04] about pod fading there's also there should be like newsletter fading because that's what happened there
[3492.04 → 3499.24] we almost did that too yeah we've been down all roads all kinds of fading we ship a weekly email
[3499.24 → 3506.12] called change law weekly it's such a novel name um and for it was also built on middleman so we
[3506.12 → 3512.20] have kindred spirits in that regard um I was using the era I was doing it alone at the time uh it was
[3512.20 → 3518.44] all git based obviously each issue was basically an entire could be each commit was an entire issue
[3518.44 → 3524.44] because I didn't think it was enough to be autonomous or atomic and just like put you know
[3524.44 → 3529.80] a one-liner as a commit just to make any sense but similar in the fact that I was like handwriting
[3530.36 → 3537.40] era at least not so much straight HTML but pretty dang close and it uh you know I would use ruby to you
[3537.40 → 3545.72] know to automate some things, but it just wasn't quite the case and then uh in comes jarred and
[3545.72 → 3552.92] saves the day and says hey we can actually use Trello to act as our cms I've got this idea let me
[3552.92 → 3557.72] poke around with it, and before you know we're using Trello as a cms to generate our newsletter which
[3557.72 → 3561.56] could be very similar to how you all do your podcast or anybody could do a podcast because if
[3561.56 → 3566.76] you're using middleman uh jarred you could probably speak to the ruby behind this, but it's a rake task
[3566.76 → 3574.28] that that gets ran ruby behind it hits the Trello API uh pulls back uh the Jason good jarred you talk
[3574.28 → 3579.96] about that part no you drilled it man that's basically what happens is just you know maybe 150
[3579.96 → 3587.64] 200 lines of ruby using the Trello API that just transforms our lists and cards in Trello into
[3587.64 → 3595.32] you know the appropriate uh, uh HTML for Markdown to serve that's pretty nice we ship that off to
[3595.32 → 3600.28] campaign monitor this Trello is basically a title a description so it's much like a blog post so you
[3600.28 → 3606.28] can gather some of that, and we use labels to uh add a sponsor flag or a draft flag for example if
[3606.28 → 3610.84] you don't want it to go into the issue, but we also had to iterate there because we had some issues there
[3610.84 → 3616.84] that jarred's like what you got sponsors you got uh drafts okay we'll have to we'll have to fine-tune that
[3616.84 → 3623.08] so back to the drawing board, and you know uh more commits later it supports it, but that was a really
[3623.08 → 3629.08] interesting turn for us to newsletter fade and then and then bring that back because it was
[3629.08 → 3633.88] away six months when you say jarred it seems like six months is the magic number for us to let something
[3633.88 → 3639.80] fade and come back yeah and I think the there was just so much friction and there was no collaboration
[3639.80 → 3644.60] I mean I couldn't even help I could just send Adam links and be like here's a good one hopefully you put
[3644.60 → 3650.28] it in their buddy right and no team you know Trello has built-in users you know it has built-in
[3650.28 → 3655.88] collaboration tools at messaging we can put comments in their like I can put a link in and tell Adam i
[3655.88 → 3659.88] don't have time to write the know the blurb but make sure you mention this and then the comments
[3659.88 → 3664.84] just get dropped out you know when we ship the thing, so there are all sorts of you know mobile
[3664.84 → 3670.04] access you can email and stuff to a board so tons of tools that are there to be had
[3670.04 → 3676.12] and it really helped us out in that regard um yeah I never thought about building the podcast
[3676.12 → 3680.44] and the show notes around it but I'm sure you could definitely get that done it was just the tools we
[3680.44 → 3687.24] knew um yeah there seems to be some pretty nice like hosted podcast services now like um I don't know
[3687.24 → 3692.12] the names of them, but it seems like it's a lot easier to get started now oh totally I mean it's
[3692.12 → 3698.84] I mean the barrier to entry for podcasting today as compared to when i very first started
[3698.84 → 3705.48] podcasting which was 2007 um to even 2009 when the change law began is night and day like there's
[3705.48 → 3711.88] services there's hosting just like you know with our worlds as developers like the world's flattened
[3711.88 → 3718.12] quite a bit there there are things that were very costly five years ago that are almost free or
[3718.12 → 3725.64] basically fear or free mostly yeah, and it's just not uh it's crazy how things have progressed that way so
[3725.64 → 3730.36] it's interesting to kind of get a peek behind your process not so much just the technical side of
[3730.36 → 3737.24] like uh we use xyz mike but no like how you actually host your site and ship your shows and gather notes
[3737.24 → 3743.16] and make it collaborative and make it you know ultimately fun even though Pam is in the make
[3743.16 → 3751.00] money uh get rich uh camp don't put her in a box Adam no, no boxes for Pam no boxes one last question on
[3751.00 → 3756.76] process before we move on um curious how you guys get your download stats out of your s3 bucket just
[3756.76 → 3761.88] turn on logging and write your own little parser or is there a service you use for that we don't uh
[3763.08 → 3768.92] no yeah i I have uh parsed Len actually texted me before this recording this episode and asked me to get
[3768.92 → 3776.20] the most recent stats because last time I got them was maybe in April or march of this year okay um but
[3776.20 → 3782.36] yeah so we have feed burner stats that Len looks at um iTunes as most people know like does not
[3782.36 → 3787.32] provide any analytics right and uh yeah so we do have logging on the bucket I haven't looked at it
[3787.32 → 3796.52] recently um fever says what 500 Len um our downloads I haven't looked at it in a while, but it's been like
[3796.52 → 3803.24] yeah our downloads are like way more than yeah don't say like about like 2000 I think on average now
[3803.24 → 3809.96] um which is not a ton but we're happy with it so yeah podcast analytics is really tough
[3810.52 → 3818.84] yeah no joke how do you get numbers out well right uh right now we leverage well prior to
[3819.48 → 3826.12] being syndicated by five and moving there we were using buzz sprout which um is a great service
[3826.12 → 3831.32] we love those guys they're from Florida uh really great software developers awesome service that's been
[3831.32 → 3837.96] stable for years uh it's affordable uh really easy to use, and it gave stats, but they weren't always
[3837.96 → 3845.00] fully accurate, and then we saw a pretty big shift um I guess for the negative we went to five by five
[3845.00 → 3852.76] because we were seeing like 60 70 000 80 000 listens on shows and buzz sprout, and we go to five by five and
[3852.76 → 3860.28] it's it is kind of normalized at like 25 000 plus per show on a good average and I don't know how
[3860.28 → 3866.12] Dan does it but I know Dan uh is a rubbish at heart and that's where he kind of lies, and he's a software
[3866.12 → 3872.04] developer as well as a voice on the radio so he was able to build feet layer which is the
[3872.04 → 3879.24] back-end stats app that tracks all five by five, and so we have access to a dashboard that lets us uh look at
[3879.24 → 3885.00] every single episode and look at uh you know a few graphs that sort of give us more insight and I know
[3885.00 → 3889.08] Dan's currently working more and more on that I won't release any secrets because I don't know any
[3889.08 → 3895.08] but I know he's doing something more in that space right that is interesting so that's a hard subject
[3895.08 → 3901.08] the hard I mean the hardest part about it, I think and the reason why five by fife stats um tend to be
[3901.08 → 3907.08] lower and i probably more accurate is that um the way that podcast clients do downloads it's not like a
[3907.08 → 3911.40] one-to-one you can't just count you know a request as a download because they have these range requests
[3911.40 → 3915.80] where they're basically splitting the file up into sections and downloading it in sections, and you got
[3915.80 → 3920.84] to be able to stitch those all back together uh in order to actually count a download, and it seems like
[3920.84 → 3927.40] a lot of services out there don't have that quite figured out and Dan says that he's put time into
[3927.40 → 3935.08] getting that you know 100 accurate or as accurate as he can um so it goes back to what you all said too
[3935.08 → 3941.80] about taking money and being obligated right uh five by five is a for-profit venture so Dan wants
[3941.80 → 3946.36] to be conservative when it comes to those numbers so that when he tells sponsors, or we tell sponsors
[3947.00 → 3952.20] ourselves as well as, as independent you know hey this is what our listenership is it's its
[3952.20 → 3957.96] conservatively accurate it's probably more than that but Dan's conservative so I think that you know
[3957.96 → 3963.72] that's a good number to it's a safe number to easily tell publicly that you know isn't boasting
[3963.72 → 3969.56] or over inflating the number yeah there are a lot of request types that we get on s3 um some are range
[3969.56 → 3975.32] requests some are the full file some are uh head requests just asking for metadata out of the file
[3975.32 → 3981.32] we also noticed that our website the mp3 player actually downloads it looks like a download even though
[3981.32 → 3987.56] the play button wasn't pressed oh uh so we have a hard time like actually parsing all that yeah um so if we
[3987.56 → 3991.40] were to go to an advertiser we would probably need a more accurate number than we have now right even
[3991.40 → 3994.44] if you have downloads too it's not really guaranteed that people are actually listening to the podcast
[3994.44 → 3999.56] that's the problem right there's this discrepancy between their client downloading it and an actual
[3999.56 → 4006.84] listen and there's one nice thing that iTunes or I guess the podcasts' app now does or at least it used
[4006.84 → 4012.28] to I don't use it personally, but it will stop downloading new episodes like if you haven't listened to the
[4012.28 → 4017.16] the last three or something so it actually won't just continue to perpetuate that subscription um
[4017.16 → 4022.04] yeah the iOS app does that yeah which is better than the alternative of like once they subscribe
[4022.04 → 4027.08] it's just continually going to download all your episodes but like you said you cannot actually
[4027.88 → 4033.00] um derive a listen from a download which is unfortunate so even if you get those download
[4033.00 → 4040.28] numbers really well you're still ballparking it you know though on the importance of it though unless
[4040.28 → 4046.76] it's it has to be spot on accurate right it's more or less just information to make better choices
[4046.76 → 4050.36] that's all metrics are in the first place right like it's data driven it's not like you're going
[4050.36 → 4055.40] to live or die by you know two or three listens or a hundred or a thousand listens it's just like
[4055.40 → 4061.08] it's better informing you of the know the quality of each show, and you can go back and look at
[4061.08 → 4065.40] those shows and say well we had this topic, or you know in your case here this is a these are the five
[4065.40 → 4070.68] shows you won it and this is the five shows we had guests and those guest shows perform better
[4070.68 → 4076.60] maybe we should lead more towards guest-based shows right, and you know less wing it shows
[4077.48 → 4083.64] you know and so it's just better information for you as an as hosts and organizers of this podcast just
[4083.64 → 4088.76] like conferences have an obligation to do a good job you know to a degree have an obligation to
[4088.76 → 4093.72] do a good job as a podcaster and that helps inform you and everyone else involved yeah we
[4093.72 → 4099.32] knew that our analytics were way off when we had Cory Haynes on and uh the week before Cory Haynes
[4099.32 → 4105.40] was on we had a large spike and then Cory Haynes was like a dip he had retweeted that he was on the
[4105.40 → 4108.92] podcast so I don't know something's wrong there yeah something's definitely wrong we still never
[4108.92 → 4115.08] figured that mystery out but I'm sure the spike was Cory's episode yeah yeah I was going to give a
[4115.08 → 4120.84] a quick shout out to a service that I found which has helped me a little bit get just analytics out of
[4120.84 → 4129.88] s3 which is called cloud stat was spelled with a q q l o u d stat um it is a paid service and this is
[4129.88 → 4135.96] not a sponsored mention or anything but I was able to turn on logs point this at my s3 account
[4136.60 → 4143.08] and even on their free tier they allowed for some a little bit easier browsing of you know the history
[4143.08 → 4148.28] of downloads and stuff and sorting and filtering so you don't have to resort to programming just
[4148.28 → 4153.80] throwing that out there it might help you guys um you know get your stats without having to ask
[4153.80 → 4157.72] you have to ask Justin or Lind has to ask Justin or just has that's Lind or one of those two well
[4157.72 → 4163.24] our first our first like few months we were really obsessed with our listeners when we had like
[4163.24 → 4168.76] 60 or 70 and now I mean it's probably been months since we looked so without sponsors without anyone
[4168.76 → 4173.32] wanting to know those numbers we basically stopped looking and yeah we're having comfortable with where
[4173.32 → 4177.16] we're at I'd see people at conferences all the time, and they come up to me and say you know i
[4177.16 → 4183.08] listen to the podcast and I'm always blown away by that so yeah it's an it's some significant number
[4184.92 → 4190.76] well we've gotten to hear from a few of you this last 25 minutes or so uh when we come back from this
[4190.76 → 4195.72] break because we do have one more sponsor we love our sponsors by the way and if you want to support us
[4195.72 → 4199.80] the best way to support us is by supporting our sponsors so let's take this break real quick we're
[4199.80 → 4203.24] going to come back for our closing questions and a couple other we have up our sleeve so
[4203.80 → 4211.48] we'll break now break back century is logging the way it should be a brand-new sponsor here at the
[4211.48 → 4217.24] change log we met these guys at gopher con love what they're doing they're Gooding their own product
[4217.24 → 4222.92] and they're doing some awesome stuff well century is a real-time air logging platform that gives you the
[4222.92 → 4228.52] insight you need into the errors that affect your customers they surface your errors helps you gauge
[4228.52 → 4233.32] severity and frequency and then gives you the information you need to get them fixed it works
[4233.32 → 4242.52] on nearly every platform including JavaScript ruby iOS go python and many more and the best part is
[4242.52 → 4248.76] century is open source you can install and host it yourself, or you can make your life easier and start
[4248.76 → 4257.40] a hosted plan at get century.com once again that's get century.com all right we are back
[4257.40 → 4263.56] uh this is the is the closing of the show pretty much we got the last 15 or so minutes here
[4263.56 → 4269.88] a lot of great questions some of our you know fan favourite questions that we ask here on the change log
[4269.88 → 4276.68] but we also got a couple other ones and in your show turning complete you have what's known as picks
[4276.68 → 4281.56] and I thought we'd reverse that here on the show today and instead of don't pick what's your
[4281.56 → 4287.32] favourite episodes of your own show and so Pam let's start with you and figure out what your favourite
[4287.32 → 4293.96] show is that you all did okay so I'm going to pick one but I reserve the right to mention other ones at
[4293.96 → 4302.12] the end of people don't pick my other favourites okay so I'm going to pick number 37 with propositions as
[4302.12 → 4308.84] types with Brian McKenna and so that is where so I've met Brian McKenna a few times at conferences
[4309.56 → 4314.84] uh, and he's he's also Australian which always surprises me when I talk to him because I forget
[4314.84 → 4322.60] and then he sounds Australian um but so what we did is he was talking about the proposition is types paper
[4322.60 → 4331.48] which is I'm now I forgot the author but uh it's a really cool paper uh Philip Adler and
[4332.44 → 4340.68] so it's its a paper that covers this interesting idea and uh basically we brought I brought Brian
[4340.68 → 4346.68] McKenna on the show to explain it to us uh so it's its my favourite episode I thought it was really fun to
[4346.68 → 4354.52] read a paper I know the other podcast members might disagree with me but uh I really like that
[4354.52 → 4359.24] episode so number 37, and you can get to any episode is Turing. Cool slash the episode number
[4360.60 → 4363.96] and we'll link it up in the show notes too just so everyone's listening to that and
[4363.96 → 4367.88] you all know when you listen to the show you got show notes to go with it and links as well but
[4368.44 → 4371.32] person what do you think are you with Pam on that one you got a different one
[4371.32 → 4378.92] I have a different one I think I'll go with episode 28 uh with Kelsey Gilmore I think that was
[4378.92 → 4382.44] going to be mine oh my gosh that was totally that was one of the ones I was torn about
[4382.44 → 4391.24] so good the real metal so universally I guess uh that one was hilarious it's perfect
[4391.24 → 4393.80] I don't know what we talked about but I mentioned dog farts
[4395.88 → 4400.04] it's a winner all right uh Justin what do you think you got your own or you
[4400.04 → 4405.40] I was going to pick Kelsey Gilmore and I can I have to find something else um I had a perfect time
[4405.40 → 4412.52] I'm going to pick a few and possibly screw line over um I had a good time talking to uh mood it meta
[4413.24 → 4421.64] on episode 57 and also uh recently we talked to uh Raquel Vélez from uh the reactive podcast your latest
[4421.64 → 4429.16] show right 62 no 61 and that was uh that was really cool too um but I would suggest if you want to
[4429.16 → 4435.40] get a like a typical podcast for us pick one any of them without a guest would be my recommendation
[4436.68 → 4443.48] all right I guess uh bring it home Len what do you think yeah so I think my favourite topic in general
[4443.48 → 4448.52] to get out of people is kind of their origin stories what makes them the type of developer there are
[4448.52 → 4456.76] they are and for us uh that was episode three yeah which is not a good yeah it's its really
[4456.76 → 4463.40] bad we were terrible at this is it good or bad I like uh I think the stories are good, but we were
[4463.40 → 4469.56] obviously new to podcasting and uh could have used a little more editing so uh what episode number was
[4469.56 → 4478.20] that I might uh number three okay origin stories okay I like that and then I'd probably say the
[4478.20 → 4482.12] Cory Haynes episode especially since I was the only one on video watching him like to run around his
[4482.12 → 4488.28] apartment the whole episode uh, and he's also talking about my favourite topic uh which is also the four
[4488.28 → 4495.96] rules of simple design very cool is that episode three two is that a different one I don't see him in
[4495.96 → 4502.60] a list of uh that's episode 22 22 okay let me log that one then so okay 22 Cory Haynes okay cool
[4502.60 → 4510.60] simple design nice all right well one of my back pocket ones was uh is another one without
[4510.60 → 4514.36] a guest is the number 34 the 2014 retrospective
[4517.56 → 4520.04] because i i like end of year retros
[4520.84 → 4525.16] I was we're kind of in a little bit of a synergy there because my favourite was 55 the
[4525.72 → 4531.16] it's not a retrospective it's a recap it's the gopher con recap in a way it wasn't the only thing
[4531.16 → 4536.12] you all mentioned on that show, but it was something that I didn't were any of you at that
[4536.12 → 4541.16] conference I was yeah okay so we were there too, and we didn't meet and that's a bummer
[4542.52 → 4547.80] I was uh yeah very anti-social did you see us at least I did see you over on the side recording
[4548.44 → 4555.08] we're hard to miss, and you didn't come say hi now I'm really bummed I was in my laptop the entire
[4555.08 → 4561.32] week actually all of hash corp was uh that's true in Denver uh well we did talk to Mitchell
[4561.32 → 4566.84] we got him on camera as a matter of fact when we're so close to getting we're waiting for the uh
[4567.56 → 4572.68] gopher con peeps Eric and Brian to approve everything we've produced for him, but we got
[4572.68 → 4578.60] several interviews and one of those interviews is with Mitchell um that might be released along
[4578.60 → 4583.32] with it, I don't know if they'll approve it or not but uh great info from Mitchell jerry did you enjoy
[4583.32 → 4587.56] chat with Mitchell yeah absolutely, and we've had Mitchell on the podcast a couple of times
[4587.56 → 4592.28] yeah in the past so he's a're a big fan of him and hash corp and all that good stuff you
[4592.28 → 4595.32] guys are doing over there we were working there the entire week even though the conference was only
[4595.32 → 4601.56] two days so it felt more just like a work meetup than a typical conference for me, you had a big uh
[4602.68 → 4609.24] um I guess attendance there it was like 10 or so people 15 people yeah we were uh I think 14 people
[4609.24 → 4614.28] at the time 15 maybe, so everybody was there yes because the company was fully invested in go
[4615.08 → 4622.28] yes there you go I believe one was having a child another one was busy so I lost track did we all
[4622.28 → 4628.60] answer the pics question except for you oh me yeah you have to have a favourite show yeah okay very good
[4628.60 → 4639.96] so my favourite show is like 75 accurate noes it's evil leader number 59 because well we got a Nebraska
[4639.96 → 4646.12] JS shout out in there nice you all know I'm one of the organizers of that conference so that's how Pam and
[4646.12 → 4654.28] I met um back in August and an evil leader I think it was right before she left for it so it's kind of
[4654.28 → 4660.76] like a fly on the wall as she prepared to come to our conference which is kind of strange but I enjoyed
[4660.76 → 4667.48] that one I love the laid back kind of like relaxed just chilling with friends atmosphere of your guys
[4667.48 → 4674.28] to show so and Emacs that's preparing you for our editor war show I like him anybody talks about
[4674.28 → 4681.64] editors so right um absolutely cool let's move on to our next awesome question and Pam you may have
[4681.64 → 4685.80] answered this one at the conference if we got you on beyond code because this is one of our
[4686.44 → 4693.96] beyond code questions and so that is who is your programming hero and why, and we will start with Pam
[4695.24 → 4702.12] I might have said Brian McKenna and Michael Picard um they're also perfect friends
[4703.88 → 4710.44] but um yeah they're kind of my functional programming mentors, and so I don't I think i also yeah I did I
[4710.44 → 4714.76] responded to this then that's right I'm remembering you don't like yeah because I don't really like
[4714.76 → 4721.88] heroes because everyone can be a superhero and we just all need to share knowledge and be nice to each
[4721.88 → 4733.24] other so amen yeah all right person how about you uh I'm going to say Aaron Patterson also known as tender love
[4733.24 → 4741.72] uh because he's just hilarious and doesn't take uh life seriously, or maybe he does he's just really
[4741.72 → 4748.12] funny he has he's good with jokes, and he just seems like a really smart person, and he's funny yes very
[4748.12 → 4756.12] funny very but I met him in person, and he's he's also like that in person so good guy all around
[4756.12 → 4763.08] um we uh we saw him at keeper be weird last fall, and they actually had a pun off as one of the
[4763.88 → 4770.12] events which was they had brought in some professional pun ORS or pun makers I don't
[4770.12 → 4777.00] know people who had like won national competitions for puns puninators and uh you get paid
[4777.00 → 4782.52] for that no they're getting were they getting paid I did say professional didn't I I think they're like
[4782.52 → 4787.08] the national champions but I still don't think they're professional as you can
[4787.08 → 4792.28] get yeah like the winners of competitions and punning but I'm pretty sure they may have won a
[4792.28 → 4797.32] prize but I'm not sure that they're you know getting paid full-time to write puns although they
[4797.32 → 4803.80] probably wish they were uh anyway point being Aaron was a part of that and uh it was pretty
[4803.80 → 4808.84] awesome well let's move on now I think Justin's next Justin who's your programming hero and why
[4808.84 → 4818.12] uh I don't know uh I guess also like Aaron Patterson and uh Cory Haynes and the late Jim Heinrich like i
[4818.12 → 4825.16] really like people in the community that were uh not only you know I guess leaders of uh
[4825.16 → 4832.84] you know open source and the technology side but also kind of emanate uh you know positivity uh also
[4832.84 → 4840.52] José valine um and I guess I really like the stuff that kyle Kingsbury is doing with uh distributed
[4840.52 → 4844.84] systems can you go into detail on that I'm not familiar with him or what he's up to oh uh yeah
[4844.84 → 4853.24] he's uh at air a-p-h-y-r on Twitter okay um definitely check out his Twitter feed and uh yeah he does a lot
[4853.24 → 4861.56] of things that are related to um he has this series of blog posts called me maybe where uh he uses a
[4861.56 → 4867.88] piece of software he wrote called season to uh break distributed systems where uh you write a value
[4867.88 → 4876.36] to one node and then uh cause a network you know partition yeah and then um rejoin the
[4876.36 → 4883.40] network together and then try to read from a different node so in systems uh such as like hash corpus
[4883.40 → 4888.36] console where you write a value into one node you expect to be able to read from all other nodes it's
[4888.36 → 4893.96] really a hard problem to solve uh so he has a lot of really great detail posts about how different
[4893.96 → 4901.24] systems behave under network partitions and also some great conference talks awesome definitely have
[4901.24 → 4908.52] to check him out Len on to you uh who is your programming hero and why yeah I was going to pick
[4908.52 → 4915.32] uncle bob martin uh kind of for the opposite reason of Justin uh he can definitely be angry and crotchety about
[4915.32 → 4920.84] professionals being not professional uh and I think we need more of that in our industry because we're
[4920.84 → 4927.00] still often terrible at software and I love when uncle bob goes on riffs about being more professional
[4928.20 → 4936.84] uh uncle bob is also a podcaster too right or vlogger something, or he does have a video series yeah okay
[4936.84 → 4943.08] I know it's something for a theatre series yeah he also appears on many podcasts there you go as a
[4943.08 → 4948.92] guest definitely some great answers to the hero question jarred I like that some of those synergize
[4948.92 → 4954.28] with what we get back from beyond code and also past shows too so there's definitely some synergy
[4954.28 → 4960.04] amongst software developers that come on the show uh another fan favourite show or question we ask on the
[4960.04 → 4968.12] show is what is on your open source radar it could be a project it could be a paradigm it could be a
[4968.12 → 4973.64] topic just something that's out there in the software development open source world that if you had a
[4973.64 → 4979.32] weekend, and you can hack on it or hack with it what would it be and why so we'll start with Pam
[4979.32 → 4986.44] again we'll go back down the same list so my favourite first open source thing I'm watching
[4986.44 → 4999.88] is that the question yes so I'm runs next so runs is a reactive programming library that is I think the
[4999.88 → 5008.92] the best reactive programming library for JavaScript, but it is really hairy in its current form runs next is
[5008.92 → 5016.20] going to be a lot lighter and hopefully more performant and lots of other fantastic things
[5016.76 → 5021.88] and so that's the one I'm checking out very cool is this something that you've played with so far
[5021.88 → 5026.04] or you just haven't even touched it yet, and you're just like I can't wait till I can oh no I mean i
[5026.04 → 5034.60] actually I'm contributing a little to it okay very cool all right next I think we have javon so
[5034.60 → 5038.60] just ask again what's on your open source radar what's if you had a free weekend, and you can
[5038.60 → 5045.24] hack on it what would it be open source radar so I think I'm I'm in two spaces right now
[5045.24 → 5052.84] uh programming wise I would say closure just toying with whatever libraries that I come across
[5053.88 → 5059.96] I've been trying to get back into the kind of ops operational world so I've been playing with docker
[5059.96 → 5069.08] again and just seeing what's new with it so docker or yeah docker and core OS I think something in
[5069.08 → 5074.60] particular with docker or core OS I know there are lots of nuances and facets so what's what's got you
[5074.60 → 5083.48] excited so I have not used core OS but recently I spun up uh something on digital ocean and
[5084.36 → 5091.00] chorus was one of the options to pick from uh so just figuring out the use cases for that or
[5091.72 → 5097.24] my way around it and docker is just catching up so I used to be really into docker when it came out and
[5097.24 → 5106.92] um some things have changed or ways of doing things so I'm just catching up on that now um so yeah
[5106.92 → 5114.28] so back in episode 138 of this very show changelaw.com slash 138 we talked to Alex we talked
[5114.76 → 5121.24] this is kind of early so this was January of this year and uh a lot of not so much a lot has changed i
[5121.24 → 5125.88] mean at least the way they spell rocket has changed and other things and the new alliance
[5125.88 → 5132.84] with docker and all that with uh the open container spec and runtime so we did have a show there so if
[5132.84 → 5137.40] you haven't listened to that one go back and listen just uh all right I'll check it out Alex he's he's
[5137.40 → 5141.96] always fun to have on the show we've actually had a couple other smaller chats with him just about uh
[5141.96 → 5146.12] different announcements since then because we love kind of keeping our ear to the ground of that space
[5146.12 → 5153.40] a lot of changing happens so it feels good to kind of keep in touch with it all right uh Justin what
[5153.40 → 5160.12] about you uh programming or not programming hero uh we did that already my bad almost, almost yeah
[5160.12 → 5165.80] open source radar uh if you had a free weekend what's what's got you excited uh if I had a free
[5165.80 → 5171.64] weekend or a lot of free weekends which I have no free weekends because I'm a parent um I would love
[5171.64 → 5179.32] to play with uh robotics a little more uh we recently had uh Raquel Vélez who was part of the node bots
[5179.32 → 5186.68] project I believe yeah um where in her past life she was a roboticist and now yeah also in now she works
[5186.68 → 5193.48] for NPM which you know then node bots are a natural crossover right yeah listen to that episode uh where
[5193.48 → 5199.32] we talked about like autonomous uh you know robots and all kinds of like really cool stuff and like AI
[5199.32 → 5204.68] um so that's what's fascinating to me, I don't I don't know much about it um and I've not
[5204.68 → 5210.76] programmed many things other than like blinking a light on a Raspberry Pi uh for like hardware hacking
[5211.56 → 5215.72] so I've had this idea I've been obsessing over for the past week or so where I want to build a
[5216.28 → 5223.24] autonomous lawn mower because uh who wants to cut their grass exactly and the commercial options uh are all
[5223.24 → 5228.76] have like really terrible reviews, and they're really expensive and uh I figure like cost wise it probably
[5228.76 → 5235.24] wouldn't be too expensive and uh it seems like a really fun problem to code like how do you
[5235.24 → 5240.84] how do you know when to turn around how do you know when to go back to charging how do you wow
[5240.84 → 5246.60] not drive into the street and actually stay on my lawn uh I've always wanted that yeah it just sounds
[5246.60 → 5253.56] so dangerous you live in an apartment well I used to have a lawn before at one point in time I did have a
[5253.56 → 5261.00] lawn so Justin you were at uh go for con right yes and did you do the hack day portion did you bail
[5261.00 → 5266.28] I did not I flew home Friday so I missed that um but i was considering most likely writing
[5266.28 → 5272.84] whatever I write for a lawn mower in go um seems like a nice language for that um
[5272.84 → 5279.40] other things I like that yeah yeah kind of uh friendlier embedded systems language okay uh
[5279.40 → 5284.28] uh the other thing I'd like to do if I had free time is rewritten all my rails projects in elixir and
[5284.28 → 5291.56] phoenix oh um but I will never have time to do that um definitely starting new projects in those
[5291.56 → 5298.28] languages and in elixir and with phoenix um but probably not worth rewriting everything i already
[5298.28 → 5302.60] have so is it safe to say when you start a new project that you would have done in rails it's going to be
[5302.60 → 5310.76] an elixir uh if I'm not only definitely yeah okay interesting I have a suggestion for you Justin
[5310.76 → 5318.28] yeah and how so you should find a high school or a middle school that does us first robotics
[5319.24 → 5327.72] and you can kill two birds with one stone by helping younger kids and robotics oh that's not
[5327.72 → 5333.48] that same with his lawn mower his robotic lawn mower he probably will call two birds yes, yes
[5333.48 → 5339.08] yes he will good one Jason it's always really intimidating for me to like approach a school and
[5339.08 → 5345.48] uh like try to set up some kind of teaching so I've been mildly involved with um
[5345.48 → 5351.96] uh organization in Philadelphia called tech girls with the z um who tries to do teaching for I think
[5351.96 → 5358.44] middle school age um girls and trying to get them excited about programming uh I definitely want to
[5358.44 → 5364.76] get involved, but it's like hard to uh you know I don't have any kids of that age in school yet so
[5364.76 → 5369.96] it's hard to like approach a school locally and try to so it's like a's usually like an after-school
[5369.96 → 5377.32] club and there's already teachers and programs and money and a curriculum, and you just have to provide
[5377.32 → 5385.08] your expertise or so they just help to drill holes exactly just show up all right Len you're last on
[5385.08 → 5389.56] the list here so if you had a free weekend, and you can hack on something in the open source community
[5389.56 → 5396.12] what would it be on uh so for me, I think I mentioned most of these before, but it's there I currently have
[5396.12 → 5404.52] three ES uh learning ember elixir and Emacs all at the same time uh I never have a free weekend uh but
[5404.52 → 5408.60] I found that when I want to hack and all these things I'm excited on um I've been thrashing a
[5408.60 → 5414.52] lot because I never know like am I writing really stupid elixir probably and I just thrash on it so
[5414.52 → 5422.44] actually uh last night I signed up for live coding.tv and started streaming uh which is oddly a lot of
[5422.44 → 5426.60] pressure even though there's like eight people watching you uh but I had eight people watching me
[5426.60 → 5431.40] and I had so much pressure and I had no idea what I was doing and uh it was good for me because it
[5431.40 → 5437.24] stopped like me from bike shedding and I just tried to make progress and wrote really crappy uh
[5437.24 → 5443.96] elixir code well that's uh that's really all we had on our docket for the show is there anything
[5443.96 → 5448.92] that uh that we might have missed that it was on any of your place you're like we had to talk about
[5448.92 → 5456.36] this we just missed it I would say one thing that we missed about the pot fading is we all kind of push
[5456.36 → 5463.08] each other so if is some of us don't want to record that week one person's always like we should record
[5464.20 → 5471.80] um so if you have a teammate podcasting oh yeah encourage each other okay your pressure yeah yeah
[5471.80 → 5478.36] i always good peer pressure I'll announce this I always feel like I have to like um because once
[5478.36 → 5481.96] we're done with the show it's pretty much in my court right jarred like if it doesn't go out it's
[5481.96 → 5487.24] because I didn't do it right it's only recently because Aaron took a full-time position with Sean
[5487.24 → 5493.80] west uh new podcasting network it's seanwes.com doing great work over there we miss him did a
[5493.80 → 5500.12] great job helping us with this show but the show's now back in my court to sort of deal with
[5500.60 → 5504.84] I like doing if it's a lot of fun and if we don't deliver it i you know I feel like I'm letting
[5504.84 → 5512.28] jarred down you know I can't let jarred down I'll throw sad face emojis at you sad face man yeah
[5512.28 → 5519.24] super sad faces well pot fading is a real thing I will admit it now um that it's its true
[5519.24 → 5523.40] it does oh we've made progress we've made progress in this show during this show yeah I mean it has
[5523.40 → 5529.80] hired to admitting it now the next step is I don't know what the next step is recovery uh consistency
[5529.80 → 5535.88] is the next step which we are achieving we've been consistent this entire year we talked to you guys
[5535.88 → 5542.20] about being sponsored, and we are sponsored so it's not boasting it's just saying like uh to
[5542.20 → 5547.08] to go with Pam here I'm in the know make money camp I think if you're doing something you should
[5547.08 → 5552.04] find a way to make money from it but at the same time don't feel like you have to so there is a fine
[5552.04 → 5557.88] line there and do what is most comfortable for you for us, we knew we wanted to take things to the next
[5557.88 → 5562.84] level and do different things we have uh a lot more fun things that changelog is doing so we're
[5562.84 → 5567.48] doing changelog films we're working with conferences we're working with different partners and brands
[5567.48 → 5572.44] we're working with on the films' perspective like doing marketing videos and like we're going into
[5572.44 → 5577.56] engineering teams and learning more about them and their process and their community and the
[5577.56 → 5581.96] stack they're working with a lot of fun stuff so it's getting us a chance to dive even further
[5581.96 → 5586.76] and even deeper with the people already, already loving on in this community, and we're here to
[5586.76 → 5590.36] serve the up-to-serve community so we had to be sustainable and that is the name of the game
[5590.36 → 5597.00] when it comes to contributing is how can you do it sustainably and for us, we had to go the
[5597.00 → 5600.20] route of sponsorships, and we don't think of it just like somebody giving us money we think of it like
[5600.20 → 5606.92] partners every sponsor we have that you've seen listed so code ship image harvest and all the
[5606.92 → 5611.96] other sponsors you've heard on this show before are all partners of ours they want to see the
[5611.96 → 5617.56] the changelog do well and do what we do uh every single day changelog weekly changelog nightly
[5617.56 → 5623.64] all that fun stuff um that's essentially my close to the show but uh I do want to tip the hat to our
[5623.64 → 5630.68] next guest for next week saran the host of code newbie she's also the manager of a new tech training
[5630.68 → 5636.36] program at Microsoft called tech jobs academy that is next week so if you love saran, and you want to hear
[5636.36 → 5641.64] more about what she's doing at code newbie and at Microsoft and uh in leading education for those
[5641.64 → 5647.48] out there in tech listen to that show subscribe to changelog weekly changelog nightly and of course go
[5647.48 → 5653.88] to turing.co and subscribe uh and with that everybody let's let's say goodbye guys thanks so much
[5653.88 → 5659.96] for coming yeah thanks for having us on yeah, thank you thanks bye
[5666.36 → 5692.76] 1
