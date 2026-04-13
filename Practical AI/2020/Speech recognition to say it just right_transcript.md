[0.00 --> 8.76]  And if you've ever used an old IVR system where you phoned up and talked to it, you very much get the feeling that you're being walked through a flowchart by voice.
[8.88 --> 12.76]  And at some point, you're being asked for some piece of information and you have to fill it in.
[12.76 --> 14.10]  Yeah, I did that just yesterday.
[15.18 --> 20.92]  They're still very popular. We're still working hard to deploy lots of advances.
[21.24 --> 26.44]  But this idea of modeling a conversation as a flowchart is quite popular.
[26.44 --> 34.24]  And now advances in language understanding have meant that we can be a little bit more flexible about what we're asking for and when.
[35.70 --> 40.42]  Bandwidth for ChangeLog is provided by Fastly. Learn more at Fastly.com.
[40.66 --> 45.54]  We move fast and fix things here at ChangeLog because of Rollbar. Check them out at Rollbar.com.
[45.80 --> 50.32]  And we're hosted on Linode cloud servers. Head to linode.com slash ChangeLog.
[50.32 --> 57.88]  Do not underestimate the power of the independent open cloud for developers.
[58.08 --> 64.90]  Yes, I'm talking about Linode. Linode is our cloud of choice and it's the home of ChangeLog.com.
[64.90 --> 69.90]  What we love most about Linode is their independence and their commitment to open cloud.
[70.32 --> 76.68]  Open cloud means being unencumbered by outside investment and maximizing value for the community, not shareholders.
[76.68 --> 81.88]  And that's exactly what Linode represents. No vendor lock-in. Open at every layer.
[82.30 --> 87.44]  If you want to learn more, head to linode.com slash open. Again, linode.com slash open.
[87.44 --> 105.64]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[105.64 --> 110.60]  This is where conversations around AI, machine learning, and data science happen.
[111.22 --> 116.16]  Join the community and Slack with us around various topics of the show at ChangeLog.com slash community.
[116.60 --> 119.06]  And follow us on Twitter. We are at Practical AI FM.
[119.72 --> 121.14]  Okay, here's Daniel and Chris.
[123.48 --> 126.94]  Welcome to another episode of Practical AI.
[126.94 --> 131.86]  Hi, this is Daniel Whitenack. I'm a data scientist with SIL International.
[132.32 --> 138.72]  And I'm joined as always by my co-host, Chris Benson, who is a principal AI strategist at Lockheed Martin.
[138.96 --> 139.58]  How are you doing, Chris?
[139.94 --> 141.80]  I am doing very well, Daniel. How's it going today?
[142.16 --> 145.30]  It's going very well. You know, a lot of people working at home.
[145.48 --> 145.74]  Yeah.
[146.02 --> 150.32]  This is not new to me and really to you either, I don't think.
[150.32 --> 156.26]  Although travel is down, but it's been a productive few days for me.
[156.40 --> 158.40]  So, I have no complaints.
[159.02 --> 159.60]  What about you?
[160.04 --> 164.06]  Other than the travel, for March and April, I was going to be traveling quite a lot.
[164.24 --> 166.46]  And obviously, not traveling at all.
[166.60 --> 170.72]  Working from home is normal for me, but we've entered a little bit of a weird thing.
[170.90 --> 175.42]  Our school system locally has closed down indefinitely for coronavirus.
[175.42 --> 180.96]  So, as we speak, my wife is in another part of the house homeschooling my daughter.
[181.22 --> 182.72]  And that's a new thing for us.
[183.30 --> 183.78]  Yeah.
[184.12 --> 184.30]  Yeah.
[184.56 --> 194.30]  And I saw, of course, there's been a lot of posts related to like AI and how that's intersected with this whole coronavirus thing.
[194.48 --> 200.02]  I know there was a good blog post that I saw the other day that kind of talked about that a little bit.
[200.08 --> 203.02]  I'll link that in the show notes for people if they're curious.
[203.02 --> 207.44]  But that's not quite the topic that we're here to talk about today.
[207.90 --> 215.10]  Back in January, Chris, you and I were at the Project Voice conference down in Chattanooga, Tennessee, here in the U.S.
[215.50 --> 222.70]  And at that conference, I was able to meet Catherine Breslin, who is a solutions architect at Cobalt.
[223.12 --> 228.86]  And we have Catherine with us today to talk about all sorts of things related to speech technology.
[229.02 --> 229.62]  Welcome, Catherine.
[229.62 --> 232.00]  Hi, Daniel and Chris.
[232.12 --> 233.90]  Thanks so much for inviting me on your show.
[234.08 --> 235.56]  It's great to be here to chat with you.
[235.86 --> 237.20]  It's great to have you here.
[237.40 --> 244.18]  So, before we jump into speech technology and voice assistance and speech to text and all sorts of things,
[244.34 --> 253.98]  could you just give us a little bit of your background and how you got into speech technology and then eventually ended up doing what you're doing now?
[253.98 --> 260.70]  Sure. So, I'm sure it doesn't take much to work out that, from my accent, I'm not from the same part of the world as you.
[261.22 --> 263.54]  So, I'm over here based in Cambridge, UK.
[264.06 --> 267.28]  I've been living over here for, living in Cambridge for about 15 years.
[267.80 --> 273.38]  And I moved here after I was at university and I was studying engineering at university.
[273.38 --> 278.96]  And at the time, I really had no idea what it was I wanted to do as a career.
[279.50 --> 285.92]  But I was really intrigued by the idea, which I learned about in my final year of undergraduate studies,
[285.92 --> 291.38]  of getting computers to seem smart, to do things which people can do really easily.
[291.38 --> 300.70]  And we looked at sort of vision and medical imaging and sort of vision-related technologies when I was an undergraduate.
[301.00 --> 303.88]  And then I thought about what about language and speech?
[304.06 --> 307.42]  How do people do this and how can we make computers do those?
[307.44 --> 312.02]  And that led me down the path, which is how I ended up where I am now.
[312.02 --> 319.84]  And so, I ended up sort of studying speech and language technology and understanding how we could make computers,
[320.28 --> 325.50]  do some of these things, and studying PhD, studying a master's,
[325.58 --> 330.24]  and eventually ending up working at various different places along the way.
[330.52 --> 334.64]  So, my first career was effectively in research.
[334.64 --> 341.52]  I was a PhD student and I did research for Toshiba in their Cambridge lab here.
[342.02 --> 347.24]  And ended up doing a postdoc position as well, taking a postdoc position at the university,
[347.36 --> 350.30]  all to do research into speech and language technology.
[351.72 --> 359.32]  And then around about sort of 2010, 2011, the wider industry was taking off
[359.32 --> 363.58]  and people were actually building this technology into products and services.
[363.98 --> 368.14]  And I ended up leaving the research world and moving to work on products.
[368.14 --> 369.40]  So, I worked on...
[369.40 --> 370.12]  I moved to Amazon.
[370.62 --> 373.62]  And when I joined Amazon, I learned about Amazon Alexa,
[373.80 --> 376.74]  which was just about to be launched when I joined Amazon.
[377.38 --> 378.02]  And good timing.
[378.36 --> 380.10]  It was really good timing to work there.
[380.16 --> 382.66]  So, I didn't originally start working on Alexa.
[382.78 --> 385.60]  I started working on some other products when I joined Amazon.
[385.60 --> 390.18]  But over time, things sort of coalesced under the Alexa umbrella.
[390.34 --> 394.78]  And I worked on there for a few years before moving on to do what I do now,
[394.84 --> 398.54]  which is helping other businesses who want to build this technology.
[399.92 --> 399.94]  Awesome.
[400.20 --> 401.86]  And I know that Cobalt...
[401.86 --> 403.38]  So, tell us a little bit about Cobalt.
[403.48 --> 407.26]  I know that there's people there that have a long history with speech,
[407.44 --> 411.08]  particularly, I think, Jeff Adams is there at Cobalt, right?
[411.16 --> 413.28]  And he also was at Amazon.
[413.46 --> 414.02]  Is that right?
[414.02 --> 415.18]  So, that's right.
[415.58 --> 417.44]  Jeff Adams is the CEO of Cobalt.
[417.74 --> 420.88]  He founded Cobalt about five and a half years ago now
[420.88 --> 425.70]  to help businesses who want to build speech and language technology
[425.70 --> 429.14]  but didn't have the team to do it or the expertise in-house.
[429.66 --> 432.32]  And Cobalt's really grown over the last few years
[432.32 --> 438.24]  to take on people who have experience working in this technology.
[438.52 --> 440.88]  So, people from Amazon, people from other companies
[440.88 --> 444.12]  who've been able to build this technology in their careers
[444.12 --> 449.24]  and bring them all together to be effectively the speech team for other companies.
[449.24 --> 453.94]  So, I guess, starting off, you're an expert in this area and Daniel is too.
[454.10 --> 458.76]  By the way, I am, of the three of us, probably the one least knowledgeable in this area.
[458.92 --> 462.68]  And so, I would love it if you would give me kind of an overview
[462.68 --> 468.68]  of what mainstream speech technologies look like, how they're being used.
[468.96 --> 471.10]  And, you know, we've talked about Alexa and obviously
[471.10 --> 473.36]  there's the competition to Alexa out there.
[473.54 --> 475.30]  Is it more than just virtual assistants?
[475.30 --> 477.26]  What does the landscape look like today?
[477.86 --> 480.10]  Yeah. So, maybe we can start with virtual assistants.
[480.38 --> 482.28]  And I think they're a great way to think about it
[482.28 --> 486.96]  because they contain all the different technology bits underneath them.
[487.50 --> 491.10]  So, a virtual assistant is a pipeline of different technology
[491.10 --> 495.20]  that all works together to understand what you've asked and to do it.
[495.72 --> 499.38]  But the underlying technology can be used in different ways.
[499.46 --> 501.62]  And we can talk about some of those later as well.
[501.68 --> 503.88]  But we can start by thinking about a virtual assistant
[503.88 --> 507.40]  and what happens when you ask a virtual assistant to do something.
[508.42 --> 511.22]  So, if you say, hey, computer, play me some music.
[511.84 --> 513.60]  And then it starts playing you some music.
[514.52 --> 518.56]  There is a number of things that have to have happened for that to come true.
[519.28 --> 521.70]  So, the first thing is that the computer has to,
[521.84 --> 524.96]  well, firstly, wake up and start listening to you
[524.96 --> 526.94]  when it hears, hey, computer,
[527.32 --> 530.28]  whatever it is that you've decided is going to be the wake word.
[530.28 --> 534.52]  And that is often a very small, low-powered speech recognition system,
[534.60 --> 536.70]  which is sitting on a device or on your phone
[536.70 --> 539.64]  that's listening very specifically for particular words.
[540.02 --> 544.28]  Then it's got to run speech recognition on what you've asked it to do.
[544.60 --> 547.60]  So, speech recognition goes from audio to text.
[547.82 --> 550.24]  It's transcribing what it is that you've asked for.
[550.76 --> 553.86]  So, it says, hopefully, play me some music.
[553.96 --> 556.26]  Although, speech recognition systems are not perfect,
[556.34 --> 557.36]  then they make some mistakes.
[557.36 --> 559.36]  So, we hope that most of the time, though,
[559.42 --> 562.52]  it gets your request accurate enough when it transcribes them.
[563.10 --> 565.42]  But that's not enough for the computer to know what to do.
[565.52 --> 567.38]  The computer has to sort of bucket that
[567.38 --> 569.38]  into one of many things that it can do.
[570.22 --> 573.96]  So, you could have asked for playing some music
[573.96 --> 575.58]  or you could have asked for buying some music.
[575.68 --> 577.96]  And it has to distinguish those two things.
[578.38 --> 580.72]  You could have also asked for the weather forecast
[580.72 --> 584.58]  or asked for the answer to a factual question,
[585.24 --> 586.52]  which is slightly easier to think about.
[586.52 --> 588.16]  So, there are some things that you ask about
[588.16 --> 590.98]  which are close together and some things are further apart.
[591.16 --> 593.82]  And the computer has to distinguish those
[593.82 --> 596.64]  with some sort of language understanding technology.
[597.64 --> 600.22]  And if you're asking about anything complicated,
[600.40 --> 602.58]  it not only has to sort of bucket what you've asked,
[602.72 --> 606.94]  but also what particular entities you might be asking about.
[607.04 --> 610.52]  So, you could say, play me some music by Sting.
[611.40 --> 614.46]  And there it has to know that Sting is the name of the artist
[614.46 --> 615.92]  that you're actually after,
[616.04 --> 617.70]  that you're interested in hearing music from.
[618.70 --> 620.98]  So, this language understanding technology
[620.98 --> 622.88]  is going to pick out what you want to do
[622.88 --> 625.26]  and the sorts of things that you want to do that with.
[625.34 --> 627.26]  So, the artists you want to listen to,
[627.42 --> 629.68]  the city you want the weather forecast in,
[630.06 --> 631.36]  the album you want to hear,
[631.60 --> 634.26]  the thing you want to buy or add to your shopping basket,
[634.26 --> 635.84]  all of those things we have to pick out.
[635.84 --> 640.40]  And then there's some computer system
[640.40 --> 641.52]  which is going to take that request
[641.52 --> 643.08]  and go and execute it
[643.08 --> 645.58]  and actually figure out what music to play back.
[646.92 --> 649.02]  And if you play music back,
[649.12 --> 651.52]  you might just hear the music start to play,
[651.84 --> 653.10]  but you might also hear an announcement
[653.10 --> 654.60]  about the music it's going to play.
[654.96 --> 656.60]  Or if you ask for the weather forecast,
[656.74 --> 660.48]  you might hear it tell you the weather forecast in words.
[660.48 --> 663.16]  And that technology, that text-to-speech technology
[663.16 --> 665.02]  is the last part of the pipeline.
[665.02 --> 668.30]  And that's sort of like the opposite of speech recognition.
[668.80 --> 670.36]  In this case, you're going from text
[670.36 --> 673.10]  and converting it into speech that can be understood.
[674.10 --> 676.46]  So, you put these things together in this pipeline.
[676.60 --> 677.46]  You've got speech recognition,
[678.02 --> 680.16]  language understanding, and text-to-speech,
[680.36 --> 683.02]  which all combine together to give you a virtual assistant
[683.02 --> 686.28]  which is going to act on what you tell it to do.
[686.98 --> 688.82]  So, I got a follow-up question for you.
[689.00 --> 689.82]  And I'm wondering,
[690.00 --> 691.92]  and this is partly from the fact
[691.92 --> 695.28]  that I'm kind of thinking of it as a software developer
[695.28 --> 698.50]  in terms of kind of how I'm thinking about asking the question.
[698.94 --> 700.98]  And I'm asking as a person in this conversation
[700.98 --> 702.64]  who knows the least about the topic.
[702.98 --> 706.78]  So, there is a series of tasks that you just talked about,
[707.00 --> 708.86]  but unlike if you're following,
[709.28 --> 711.08]  you know, like a webpage form
[711.08 --> 713.26]  where you have a very explicit set
[713.26 --> 715.80]  of things that are going to happen
[715.80 --> 717.62]  in a particular order and stuff.
[718.08 --> 720.28]  In this case, the types of questioning
[720.28 --> 722.28]  is you have follow-ups on what kind of music,
[722.38 --> 723.34]  what artists, that kind of stuff.
[723.82 --> 727.24]  How does the system kind of understand
[727.24 --> 729.42]  a collection of state,
[729.56 --> 732.02]  a collection of related conversation?
[732.44 --> 734.66]  How does it conceptualize like when that's done?
[734.80 --> 735.86]  How does it, you know,
[736.04 --> 738.02]  given the fact that it is a loose,
[738.20 --> 740.40]  not tightly controlled system that we're talking about?
[740.40 --> 744.44]  So, yeah, this is an interesting technical
[744.44 --> 746.62]  as well as a design challenge, I think.
[747.10 --> 750.42]  Because if you were to say to your virtual assistant,
[750.60 --> 751.60]  play me some music,
[752.32 --> 754.22]  you might design it such that it would,
[754.62 --> 755.64]  if in that case,
[755.68 --> 757.92]  it had no information about the music you wanted to play,
[758.00 --> 759.44]  but it would just pick something randomly
[759.44 --> 760.60]  that it thought you might like.
[760.74 --> 762.36]  And then it wouldn't ask for any follow-up
[762.36 --> 764.72]  about what it was that you actually wanted to listen to.
[765.32 --> 767.98]  But another person might design their virtual assistant
[767.98 --> 769.32]  to actually follow up on you
[769.32 --> 770.24]  and say specifically,
[770.50 --> 771.92]  what music do you want to hear?
[772.80 --> 775.68]  And so there's different design choices
[775.68 --> 777.28]  in how you build these things as well.
[778.06 --> 779.52]  And something like music,
[780.14 --> 783.26]  you can have a choice that just plays random music
[783.26 --> 785.12]  so you don't have to specify any further.
[785.26 --> 787.18]  Whereas if you're asking for the weather,
[787.44 --> 789.08]  you probably actually want to know
[789.08 --> 790.66]  where in the world you're asking for the weather for.
[790.72 --> 792.18]  Otherwise, it's no good to anybody
[792.18 --> 793.56]  to get a random weather forecast.
[795.26 --> 797.66]  So these design choices have to come into it
[797.66 --> 799.28]  in the very early stages and thinking
[799.28 --> 801.42]  how much effort you want to put on the user.
[802.08 --> 803.38]  The second thing you have to bear in mind
[803.38 --> 807.66]  is that these systems are not that great at conversation yet.
[808.02 --> 810.76]  And if you try and initiate long conversations with people,
[811.12 --> 812.16]  they can get confusing
[812.16 --> 813.88]  and they can frustrate your users too.
[814.44 --> 817.18]  So another design goal is to sort of keep the conversations
[817.18 --> 818.88]  that they're having as short as possible.
[818.88 --> 821.68]  And so with this in mind,
[821.76 --> 824.30]  you can think about which of these...
[825.06 --> 826.60]  I talked about taking intents
[826.60 --> 829.10]  or taking bucketing what people were asking for
[829.10 --> 831.20]  and the things that they were asking about.
[831.34 --> 834.54]  So when we bucket what a user is requesting
[834.54 --> 835.62]  into different categories,
[836.00 --> 837.00]  we call those intents.
[837.64 --> 839.50]  So you might have an intent
[839.50 --> 841.32]  which is a play music intent.
[841.86 --> 843.22]  You might have an intent
[843.22 --> 845.18]  which is a turn on the lights intent
[845.18 --> 846.94]  or a give me a weather forecast intent.
[846.94 --> 850.16]  And this is just the general shape
[850.16 --> 851.84]  of the request that the user is asking.
[852.58 --> 854.26]  And then within that intent,
[854.36 --> 857.78]  you will have a set of what gets called
[857.78 --> 859.46]  in various ways,
[859.58 --> 861.78]  either a concept or an entity or a slot.
[861.96 --> 864.28]  The terms are somewhat used interchangeably.
[865.04 --> 866.56]  But you have some sort of entity
[866.56 --> 867.68]  that you're asking about.
[867.88 --> 869.26]  So in the case of music,
[869.36 --> 871.34]  it might be an artist name or an album name.
[871.72 --> 873.54]  In the case of a weather forecast,
[873.60 --> 874.40]  it might be the city.
[874.40 --> 876.02]  And those entities,
[876.44 --> 877.94]  we can decide that the computer
[877.94 --> 879.36]  has to ask for them
[879.36 --> 881.82]  or maybe they can have some default behavior
[881.82 --> 883.68]  or maybe some random behavior.
[884.22 --> 885.64]  So the designer has to choose
[885.64 --> 890.18]  which of these entities are desired or necessary
[890.18 --> 891.46]  in the same way you do
[891.46 --> 894.04]  for other programming defaults, I think.
[894.72 --> 895.88]  So I'm curious.
[896.54 --> 898.04]  I mean, you mentioned the idea.
[898.28 --> 899.60]  So two ideas, I guess.
[899.70 --> 901.32]  One around the fact that
[901.32 --> 903.70]  these types of assistants are composed
[903.70 --> 905.26]  of these various components
[905.26 --> 906.86]  that all work together.
[907.42 --> 908.78]  And then second, that, you know,
[908.84 --> 912.00]  part of a current limitation of these systems
[912.00 --> 913.94]  is long conversations.
[913.94 --> 917.08]  We'll get into sort of the speech to text
[917.08 --> 920.04]  and maybe speech synthesis parts here in a second.
[920.16 --> 922.38]  But I was wondering if I'm right in assuming
[922.38 --> 924.00]  that that limitation
[924.00 --> 925.96]  in terms of the length of conversations
[925.96 --> 928.40]  or maybe how dynamic they can be
[928.40 --> 930.60]  is driven by limitations
[930.60 --> 933.16]  in the sort of natural language understanding
[933.16 --> 933.96]  that you mentioned,
[934.12 --> 935.98]  I guess the middle bits.
[936.12 --> 937.82]  So after you've detected the speech
[937.82 --> 939.96]  and you've converted that into text,
[940.08 --> 942.40]  maybe then you have to decide what to do with it.
[942.44 --> 943.42]  Is it those limitations
[943.42 --> 946.24]  that limit how dynamic things can be at this point?
[946.96 --> 948.30]  I think there's a separate step
[948.30 --> 950.04]  which I sort of glossed over a little bit,
[950.10 --> 952.78]  which is managing the state of a conversation.
[953.58 --> 954.60]  And in the past,
[954.66 --> 955.86]  we've designed conversations
[955.86 --> 957.78]  to be sort of like flow charts.
[958.40 --> 961.06]  And if you've ever used an old IVR system
[961.06 --> 962.70]  where you phoned up and talked to it,
[963.06 --> 964.28]  you very much get the feeling
[964.28 --> 967.06]  that you're being walked through a flow chart by voice.
[967.18 --> 968.02]  And at some point,
[968.06 --> 969.70]  you're being asked for some piece of information
[969.70 --> 971.04]  and you have to fill it in.
[971.04 --> 972.40]  Yeah, I did that just yesterday.
[973.60 --> 974.86]  They're still very popular.
[974.86 --> 977.14]  But we're still working hard
[977.14 --> 979.22]  to deploy lots of advances.
[979.54 --> 982.26]  But this idea of modeling a conversation
[982.26 --> 984.74]  as a flow chart is quite popular.
[985.52 --> 988.24]  And now advances in language understanding
[988.24 --> 990.60]  have meant that we can be a little bit more flexible
[990.60 --> 992.50]  about what we're asking for and when.
[993.06 --> 995.34]  So we might be able to have a user
[995.34 --> 998.00]  say in one single utterance
[998.00 --> 999.46]  everything they're asking for.
[999.62 --> 1001.40]  Whereas before we might have broken up
[1001.40 --> 1002.42]  and asked them specifically
[1002.42 --> 1004.18]  over a number of conversation turns.
[1004.18 --> 1006.74]  And this means that we have to introduce
[1006.74 --> 1009.12]  a technology which is tracking
[1009.12 --> 1011.16]  all the information that the user's given us
[1011.16 --> 1012.46]  a sort of dialogue state.
[1013.00 --> 1014.94]  We have to move between dialogue states
[1014.94 --> 1017.06]  as the user gives us different bits of information
[1017.06 --> 1019.50]  or as they ask us to do different things.
[1020.78 --> 1022.72]  And so there's really a couple of points
[1022.72 --> 1026.08]  that are limiting what we can do.
[1026.18 --> 1028.72]  One is the language understanding technology
[1028.72 --> 1029.40]  at the moment.
[1029.40 --> 1033.16]  It can recognize broad categories of things
[1033.16 --> 1035.82]  but a lot of what users might ask for
[1035.82 --> 1037.72]  doesn't necessarily fall in something
[1037.72 --> 1040.78]  which can be easily modeled as intents and slots.
[1041.28 --> 1043.98]  If you're just having small talk with a computer
[1043.98 --> 1045.24]  some sort of chit chat
[1045.24 --> 1047.26]  that's a different kind of conversation
[1047.26 --> 1048.78]  and that's not naturally modeled
[1048.78 --> 1050.22]  with intents and slots.
[1050.86 --> 1052.10]  So we can rule out
[1052.10 --> 1054.46]  having some of those sorts of conversations
[1054.46 --> 1057.18]  with this way of building technology.
[1059.02 --> 1060.18]  The other thing is
[1060.18 --> 1062.72]  if you have conversation turns
[1062.72 --> 1064.20]  which happen over time
[1064.20 --> 1066.48]  and the user starts to
[1066.48 --> 1069.14]  ask for more complicated things
[1069.14 --> 1070.88]  or they start to refer back to things
[1070.88 --> 1071.98]  that they've talked about earlier.
[1072.52 --> 1074.24]  So tracking those over a conversation
[1074.24 --> 1075.34]  is also quite hard.
[1075.34 --> 1079.26]  If you ask your virtual assistant
[1079.26 --> 1080.54]  you say, what's this?
[1081.48 --> 1082.92]  Then it has to know what this is.
[1083.00 --> 1085.18]  It has to be able to try and figure out
[1085.18 --> 1086.20]  what you're talking about
[1086.20 --> 1088.98]  which can be relatively straightforward
[1088.98 --> 1090.10]  if there's a song playing.
[1090.50 --> 1092.24]  You might assume that it's the song that's playing
[1092.24 --> 1094.10]  but if you've talked about something
[1094.10 --> 1095.30]  previously in the conversation
[1095.30 --> 1095.96]  it could be that.
[1096.04 --> 1097.50]  So there's a lot of complicated
[1097.50 --> 1099.54]  language-related technology
[1099.54 --> 1101.48]  to do that tracking over time
[1101.48 --> 1103.90]  which doesn't work well at scale yet.
[1105.34 --> 1118.66]  Hi there.
[1119.02 --> 1120.24]  This is Daniel Whitenack
[1120.24 --> 1122.14]  one of the co-hosts of Practical AI
[1122.14 --> 1124.80]  and when I'm not working on Practical AI
[1124.80 --> 1127.14]  I'm developing my own AI applications
[1127.14 --> 1129.36]  or I'm training teams at other companies.
[1129.68 --> 1131.84]  I've been doing this for over 10 years now
[1131.84 --> 1133.88]  and I've trained more than a thousand people.
[1133.88 --> 1135.68]  Now I'd like to invite you
[1135.68 --> 1138.72]  to my new live online training event
[1138.72 --> 1140.24]  called AI Classroom.
[1140.74 --> 1141.96]  In AI Classroom
[1141.96 --> 1143.82]  I'm going to teach the practical skills
[1143.82 --> 1144.94]  I've learned over the years
[1144.94 --> 1147.88]  using the latest open source AI technology.
[1148.30 --> 1150.16]  You will learn both AI theory
[1150.16 --> 1152.88]  along with practical hands-on implementations
[1153.44 --> 1155.32]  in both PyTorch and TensorFlow.
[1155.96 --> 1158.00]  After attending AI Classroom
[1158.00 --> 1159.30]  you'll be able to understand
[1159.30 --> 1160.40]  the latest models
[1160.40 --> 1162.66]  implement your own models and code
[1162.66 --> 1165.42]  train computer vision and NLP models
[1165.42 --> 1167.30]  create model inference servers
[1167.30 --> 1169.68]  and experiment with state-of-the-art methods
[1169.68 --> 1170.94]  like reinforcement learning.
[1171.70 --> 1174.02]  AI Classroom is taking place this May
[1174.02 --> 1176.00]  and it'll be taking place live
[1176.00 --> 1177.30]  and completely online
[1177.30 --> 1179.36]  in a high-quality virtual classroom
[1179.36 --> 1180.88]  so no travel is required.
[1181.38 --> 1182.86]  There will be two cohorts
[1182.86 --> 1184.26]  with convenient time zones
[1184.26 --> 1186.24]  for Eastern and Western hemispheres
[1186.24 --> 1187.42]  so don't miss out.
[1187.42 --> 1189.16]  Tickets and more information
[1189.16 --> 1191.74]  is available at datadan.io
[1191.74 --> 1194.12]  That's datadan.io
[1194.12 --> 1197.38]  and early bird pricing lasts until April 3rd.
[1197.54 --> 1199.54]  See you online in AI Classroom.
[1199.54 --> 1214.86]  So Catherine, I'm kind of curious
[1214.86 --> 1218.90]  as we kind of launched right into assistance up front.
[1219.08 --> 1220.70]  I'm also kind of wondering
[1220.70 --> 1222.56]  if we could lay out kind of landscape
[1222.56 --> 1225.18]  on how is speech technology
[1225.18 --> 1228.92]  being used outside of assistance strictly
[1228.92 --> 1231.00]  and in the larger landscape.
[1231.62 --> 1234.70]  What is there in the speech community out there
[1234.70 --> 1236.32]  beyond these assistants
[1236.32 --> 1237.34]  that we've been talking about?
[1238.06 --> 1238.26]  Sure.
[1238.44 --> 1240.16]  So I think one of the obvious things
[1240.16 --> 1241.02]  you can think about
[1241.02 --> 1243.42]  is just speech recognition technology
[1243.42 --> 1244.16]  on its own.
[1244.66 --> 1246.98]  So taking long streams of audio
[1246.98 --> 1248.26]  and transcribing it
[1248.26 --> 1249.06]  and there you can think of
[1249.06 --> 1249.92]  all sorts of applications
[1249.92 --> 1252.06]  which don't fall within virtual assistants.
[1252.56 --> 1254.42]  And maybe one of the obvious ones
[1254.42 --> 1256.02]  is sort of automated subtitling.
[1256.52 --> 1258.74]  So especially as we're moving more online
[1258.74 --> 1260.90]  and we're having more video content created
[1260.90 --> 1263.34]  being able to automatically subtitle that
[1263.34 --> 1264.42]  can be really helpful.
[1264.66 --> 1266.78]  Not just for accessibility
[1266.78 --> 1268.38]  for people who are watching it
[1268.38 --> 1269.54]  in real time perhaps
[1269.54 --> 1271.78]  but also to search it later on.
[1272.20 --> 1274.70]  So if you want to come back
[1274.70 --> 1276.74]  and find particular places in our video
[1276.74 --> 1277.94]  where things were talked about
[1277.94 --> 1280.88]  having an automatically generated transcript
[1280.88 --> 1282.40]  can help with that.
[1282.56 --> 1285.42]  So that's one place speech recognition is used.
[1285.82 --> 1287.38]  It can be used in other places
[1287.38 --> 1290.22]  though there are some industries for example
[1290.22 --> 1291.70]  where it becomes very important
[1291.70 --> 1295.10]  to monitor conversations between people
[1295.10 --> 1296.48]  for legal reasons.
[1296.48 --> 1298.70]  So if you're giving financial advice to somebody
[1298.70 --> 1301.00]  you want a record of that financial advice.
[1301.86 --> 1303.68]  But manually transcribing
[1303.68 --> 1304.74]  all of these conversations
[1304.74 --> 1306.62]  gets very tedious and time consuming.
[1306.62 --> 1308.72]  So there's great applications there
[1308.72 --> 1310.56]  to help relieve the workflow
[1310.56 --> 1312.70]  and make it easier for people to manage.
[1313.44 --> 1315.22]  So as we're kind of getting a bit more
[1315.22 --> 1316.22]  into speech recognition
[1316.22 --> 1317.48]  which I think like you said
[1317.48 --> 1319.72]  is one of the things that pops
[1319.72 --> 1320.86]  into people's mind
[1320.86 --> 1323.48]  as something that has utility
[1323.48 --> 1324.66]  both in assistants
[1324.66 --> 1326.82]  and in various other places.
[1326.82 --> 1329.00]  I know you're an expert in this technology
[1329.00 --> 1329.96]  and I also know
[1329.96 --> 1331.24]  from our previous conversations
[1331.24 --> 1332.88]  I was learning from you
[1332.88 --> 1335.82]  about how speech recognition itself
[1335.82 --> 1339.08]  can be composed into various pieces
[1339.08 --> 1341.16]  almost like a pipeline as well.
[1341.68 --> 1343.22]  I was wondering if you could cover
[1343.22 --> 1347.80]  what those steps in a typical speech recognition system are
[1347.80 --> 1348.96]  and what their function is.
[1349.54 --> 1349.90]  Sure.
[1349.90 --> 1352.58]  So as I said earlier
[1352.58 --> 1353.54]  at the beginning
[1353.54 --> 1355.38]  the job of a speech recognition system
[1355.38 --> 1356.36]  is to take audio
[1356.36 --> 1358.62]  and to give you an estimate
[1358.62 --> 1360.66]  or guess of what words were spoken
[1360.66 --> 1362.74]  so to transcribe that audio.
[1363.52 --> 1365.64]  And there's three different parts
[1365.64 --> 1367.52]  that we typically break this down into.
[1368.12 --> 1370.22]  So the first part that we have
[1370.22 --> 1373.44]  is what we call a lexicon.
[1374.10 --> 1376.24]  So if you think about words in a language
[1376.24 --> 1377.98]  they are composed of different sounds.
[1377.98 --> 1380.36]  So the word cat, for example
[1380.36 --> 1383.12]  is composed of the sound k-a-t
[1383.12 --> 1386.96]  and the word bat is composed of b-a-t
[1386.96 --> 1391.60]  so we can take this phonetic representation
[1391.60 --> 1392.66]  of different words
[1392.66 --> 1393.64]  and create a lexicon
[1393.64 --> 1395.88]  which tells you how each word is pronounced.
[1396.90 --> 1398.58]  And in a language like English
[1398.58 --> 1401.44]  we might find that there are about 50 different sounds
[1401.44 --> 1403.56]  that we can combine together
[1403.56 --> 1405.32]  to make all the different words.
[1405.32 --> 1410.20]  So the lexicon maps words to their pronunciations.
[1411.48 --> 1414.74]  We have then a model in the system
[1414.74 --> 1416.06]  called the acoustic model
[1416.06 --> 1418.04]  and the acoustic model
[1418.04 --> 1418.68]  as you might guess
[1418.68 --> 1420.66]  models the acoustics of sound and speech.
[1421.36 --> 1422.54]  And this is the bit of the model
[1422.54 --> 1423.76]  which is going to tell you
[1423.76 --> 1425.78]  for each little bit of sound
[1425.78 --> 1427.34]  that someone is talking
[1427.34 --> 1430.32]  which phoneme is likely to be spoken
[1430.32 --> 1432.40]  which of those 50 sounds
[1432.40 --> 1434.72]  is likely to be happening at that time.
[1434.72 --> 1437.82]  And this acoustic model
[1437.82 --> 1440.68]  is going to be built on lots of audio
[1440.68 --> 1442.38]  that we know what's happening in the audio
[1442.38 --> 1444.52]  and we can build a machine learning model
[1444.52 --> 1446.06]  which is going to be able to tell us
[1446.06 --> 1448.50]  given a huge database of sounds
[1448.50 --> 1450.14]  where we know what sounds are being spoken
[1450.14 --> 1452.72]  can we predict for new sounds
[1452.72 --> 1454.28]  what sounds, for new audio
[1454.28 --> 1455.46]  what sounds are being spoken.
[1456.10 --> 1458.48]  And then we have finally a language model
[1458.48 --> 1460.80]  and the purpose of the language model
[1460.80 --> 1462.02]  in a speech recognition system
[1462.02 --> 1463.76]  is to predict sequences of words.
[1463.76 --> 1465.94]  So from a language model
[1465.94 --> 1466.76]  we might say
[1466.76 --> 1469.60]  if the input to the language model
[1469.60 --> 1470.96]  is hi, my name is
[1470.96 --> 1473.42]  then it's very likely
[1473.42 --> 1474.28]  that the next word
[1474.28 --> 1475.22]  is going to be Catherine
[1475.22 --> 1476.86]  but the next word
[1476.86 --> 1478.54]  is very unlikely to be goodbye
[1478.54 --> 1480.58]  and so the language model
[1480.58 --> 1481.40]  is sort of predicting
[1481.40 --> 1482.74]  which sequences of words
[1482.74 --> 1483.80]  are more likely than others.
[1484.36 --> 1485.68]  So if we put these together
[1485.68 --> 1487.28]  we have an acoustic model
[1487.28 --> 1488.12]  which tells you
[1488.12 --> 1489.16]  from some audio
[1489.16 --> 1490.00]  which sounds are likely
[1490.00 --> 1491.72]  to be spoken at that time.
[1491.72 --> 1493.44]  the lexicon tells you
[1493.44 --> 1494.76]  how those sounds combine
[1494.76 --> 1495.52]  into words
[1495.52 --> 1497.52]  and then the language model
[1497.52 --> 1498.54]  tells you how those words
[1498.54 --> 1500.22]  combine into sequences of words.
[1501.36 --> 1502.62]  And so we use these three models
[1502.62 --> 1504.02]  sort of in a combined
[1504.02 --> 1505.46]  decoding procedure
[1505.46 --> 1506.92]  decoding algorithm
[1506.92 --> 1508.84]  to work together
[1508.84 --> 1509.90]  to tell you
[1509.90 --> 1511.18]  for a new piece of audio
[1511.18 --> 1512.48]  what words are likely
[1512.48 --> 1513.78]  to be spoken in that audio.
[1513.78 --> 1516.26]  So I've got a question
[1516.26 --> 1517.18]  as you've been talking
[1517.18 --> 1518.42]  about these acoustic models
[1518.42 --> 1519.38]  and language models
[1519.38 --> 1520.64]  and I guess
[1520.64 --> 1521.88]  almost a basic question
[1521.88 --> 1523.14]  when you talk about these
[1523.14 --> 1524.98]  what kind of models are they?
[1525.08 --> 1526.20]  Are they statistical models?
[1526.36 --> 1527.88]  Are they deep learning models?
[1528.22 --> 1530.82]  Are there other technologies
[1530.82 --> 1532.68]  that are being used
[1532.68 --> 1533.50]  to blend in?
[1533.74 --> 1534.80]  Could you kind of talk about
[1534.80 --> 1535.88]  what those are fundamentally?
[1536.32 --> 1536.50]  Yeah.
[1536.74 --> 1538.64]  So one thing I should mention
[1538.64 --> 1540.56]  is that there is
[1540.56 --> 1541.52]  what I'm talking about
[1541.52 --> 1542.56]  in terms of breaking down
[1542.56 --> 1543.86]  into acoustic and language model
[1543.86 --> 1545.70]  and lexicon is a technology
[1545.70 --> 1546.98]  which is very common right now
[1546.98 --> 1547.52]  but there are
[1547.52 --> 1548.60]  in the research community
[1548.60 --> 1549.80]  there's a lot more effort
[1549.80 --> 1551.28]  to come up with new
[1551.28 --> 1552.48]  neural network approaches
[1552.48 --> 1555.50]  to build one speech recognition system
[1555.50 --> 1556.96]  which isn't decomposed
[1556.96 --> 1558.06]  into these three parts.
[1558.52 --> 1559.50]  But I'll carry on talking
[1559.50 --> 1560.38]  about the three parts
[1560.38 --> 1561.30]  because that's how a lot
[1561.30 --> 1563.26]  of our commercial speech recognition systems
[1563.26 --> 1564.52]  are built right now.
[1565.60 --> 1566.82]  So the lexicon
[1566.82 --> 1568.68]  which is basically
[1568.68 --> 1569.62]  a phonetic pronunciation
[1569.62 --> 1570.62]  of lots of words
[1570.62 --> 1572.52]  often we have really good
[1572.52 --> 1573.14]  high quality
[1573.14 --> 1574.68]  handcrafted lexicons
[1574.68 --> 1576.14]  so they're written
[1576.14 --> 1577.18]  by phoneticians
[1577.18 --> 1578.38]  and you can imagine
[1578.38 --> 1579.40]  for a language like English
[1579.40 --> 1581.02]  we have good lexicons
[1581.02 --> 1581.90]  which have been developed
[1581.90 --> 1583.10]  over many years.
[1584.12 --> 1584.64]  Now obviously
[1584.64 --> 1587.08]  language is always changing
[1587.08 --> 1588.18]  and new words come up
[1588.18 --> 1588.76]  and new ways
[1588.76 --> 1589.84]  of using language come up
[1589.84 --> 1590.94]  and so we still have
[1590.94 --> 1592.06]  to be able to predict
[1592.06 --> 1593.88]  pronunciations of new words
[1593.88 --> 1596.38]  but we have very good lexicons
[1596.38 --> 1597.16]  to tell us
[1597.16 --> 1598.50]  pronunciations of
[1598.50 --> 1599.54]  the vast majority
[1599.54 --> 1600.66]  of English words already
[1600.66 --> 1602.00]  and so predicting
[1602.00 --> 1602.68]  new words
[1602.68 --> 1603.40]  the pronunciation
[1603.40 --> 1604.16]  of new words
[1604.16 --> 1605.68]  is a smaller task.
[1607.92 --> 1609.64]  The acoustic model
[1609.64 --> 1610.42]  and the language model
[1610.42 --> 1611.26]  then end up being
[1611.26 --> 1611.94]  statistical
[1611.94 --> 1613.72]  machine learned models
[1613.72 --> 1616.56]  and the language model
[1616.56 --> 1618.00]  is trained on text
[1618.00 --> 1619.34]  and the acoustic model
[1619.34 --> 1620.32]  is trained on audio.
[1621.34 --> 1622.40]  So two different models
[1622.40 --> 1623.42]  trained on two different
[1623.42 --> 1624.42]  types of data.
[1624.42 --> 1627.32]  So the acoustic model
[1627.32 --> 1628.22]  for instance
[1628.22 --> 1630.20]  we've had great success
[1630.20 --> 1631.46]  in recent years.
[1631.56 --> 1632.30]  If you think back
[1632.30 --> 1634.02]  like 10, 15 years ago
[1634.02 --> 1635.10]  speech recognition systems
[1635.10 --> 1635.86]  didn't really work
[1635.86 --> 1636.30]  all that well
[1636.30 --> 1638.02]  and they were using
[1638.02 --> 1640.38]  often for the acoustic models
[1640.38 --> 1641.90]  Gaussian mixture models
[1641.90 --> 1643.92]  and one of the things
[1643.92 --> 1644.62]  that's really happened
[1644.62 --> 1645.42]  in recent years
[1645.42 --> 1646.70]  in the past 10 years or so
[1646.70 --> 1647.84]  is the switch
[1647.84 --> 1649.22]  from Gaussian mixture models
[1649.22 --> 1650.68]  to neural network
[1650.68 --> 1651.42]  acoustic models
[1651.42 --> 1652.60]  and that's had
[1652.60 --> 1653.48]  a really big impact
[1653.48 --> 1654.24]  on the performance
[1654.24 --> 1655.48]  of speech recognition systems
[1655.48 --> 1656.12]  has made them
[1656.12 --> 1658.22]  significantly more accurate
[1658.22 --> 1660.16]  over the past few years
[1660.16 --> 1661.86]  and that's come in tandem
[1661.86 --> 1662.88]  with other advances
[1662.88 --> 1663.88]  in computing power
[1663.88 --> 1664.50]  and storage
[1664.50 --> 1664.96]  and memory
[1664.96 --> 1665.82]  and computation
[1665.82 --> 1666.90]  and all of those other things
[1666.90 --> 1668.24]  but the actual switch
[1668.24 --> 1670.00]  from GMM models
[1670.00 --> 1670.92]  Gaussian mixture models
[1670.92 --> 1671.82]  to neural networks
[1671.82 --> 1672.90]  and the acoustic modeling side
[1672.90 --> 1673.88]  has really made
[1673.88 --> 1675.18]  speech recognition systems
[1675.18 --> 1676.22]  much more accurate.
[1676.96 --> 1677.80]  So I'm curious
[1677.80 --> 1678.68]  as I was thinking
[1678.68 --> 1679.44]  through what you're
[1679.44 --> 1679.96]  talking about
[1679.96 --> 1681.20]  with these various bits
[1681.20 --> 1682.64]  obviously like you said
[1682.64 --> 1684.06]  there's a need
[1684.06 --> 1684.90]  for this sort of
[1684.90 --> 1686.48]  expert information up front
[1686.48 --> 1687.36]  and that's available
[1687.36 --> 1688.92]  for languages like English
[1688.92 --> 1690.66]  and probably less available
[1690.66 --> 1691.86]  for other languages
[1691.86 --> 1692.88]  but I was also thinking
[1692.88 --> 1694.12]  about the side of things
[1694.12 --> 1695.94]  which is accents
[1695.94 --> 1697.68]  and in terms of like
[1697.68 --> 1699.32]  the lexicon
[1699.32 --> 1700.18]  and determining
[1700.18 --> 1701.20]  how each word
[1701.20 --> 1701.82]  is pronounced
[1701.82 --> 1703.10]  and then also
[1703.10 --> 1704.26]  for the acoustic model
[1704.26 --> 1704.96]  I guess that's where
[1704.96 --> 1706.14]  the biggest impact is
[1706.14 --> 1707.24]  but it seems like
[1707.24 --> 1708.54]  that filters all the way through
[1708.54 --> 1709.48]  because even for
[1709.48 --> 1710.36]  the language model
[1710.36 --> 1711.48]  if I understood right
[1711.48 --> 1712.62]  you're kind of
[1712.62 --> 1713.62]  taking a sequence
[1713.62 --> 1715.28]  of sounds or phonemes
[1715.28 --> 1716.82]  and then translating
[1716.82 --> 1717.88]  that in a sense
[1717.88 --> 1719.18]  to actual words
[1719.18 --> 1720.18]  so the sounds
[1720.18 --> 1720.98]  would even affect
[1720.98 --> 1721.42]  that bit
[1721.42 --> 1722.66]  I guess as well
[1722.66 --> 1723.72]  so how does accent
[1723.72 --> 1725.00]  come into this?
[1725.74 --> 1726.60]  So yeah you're right
[1726.60 --> 1727.94]  accent sort of touches
[1727.94 --> 1729.32]  every bit of the system
[1729.32 --> 1730.24]  if you have
[1730.24 --> 1731.50]  the lexicon itself
[1731.50 --> 1732.52]  is a place where
[1732.52 --> 1734.00]  you might have
[1734.00 --> 1736.20]  multiple pronunciations
[1736.20 --> 1736.68]  of a word
[1736.68 --> 1737.42]  but there would be
[1737.42 --> 1738.30]  really standard
[1738.30 --> 1739.66]  pronunciations of a word
[1739.66 --> 1740.94]  so you might have
[1740.94 --> 1741.92]  the and the
[1741.92 --> 1743.92]  as pronunciations
[1743.92 --> 1744.34]  for the
[1744.34 --> 1745.20]  or either either
[1745.20 --> 1746.50]  like alternative
[1746.50 --> 1748.20]  pronunciations
[1748.20 --> 1749.18]  but you wouldn't
[1749.18 --> 1750.34]  necessarily like
[1750.34 --> 1751.70]  handcraft in the lexicon
[1751.70 --> 1752.52]  every single
[1752.52 --> 1753.60]  accented pronunciation
[1753.60 --> 1754.38]  of something
[1754.38 --> 1755.78]  because that would
[1755.78 --> 1756.50]  just mean you had
[1756.50 --> 1757.04]  loads and loads
[1757.04 --> 1758.16]  of entries in the lexicon
[1758.16 --> 1759.32]  and it would get
[1759.32 --> 1760.32]  difficult for the
[1760.32 --> 1761.80]  computer to tell them
[1761.80 --> 1762.74]  apart over time
[1762.74 --> 1764.66]  it would make it
[1764.66 --> 1765.22]  much more difficult
[1765.22 --> 1765.70]  for the speech
[1765.70 --> 1766.48]  recognition system
[1766.48 --> 1766.90]  to work
[1766.90 --> 1768.58]  so we might have
[1768.58 --> 1769.34]  if we knew we were
[1769.34 --> 1770.28]  working with particular
[1770.28 --> 1770.78]  accents
[1770.78 --> 1771.60]  we would have
[1771.60 --> 1772.36]  different lexicons
[1772.36 --> 1773.18]  and you see that
[1773.18 --> 1773.64]  for example
[1773.64 --> 1774.54]  we might have
[1774.54 --> 1775.58]  a different lexicon
[1775.58 --> 1776.44]  for the US
[1776.44 --> 1776.98]  and the UK
[1776.98 --> 1778.28]  because they're
[1778.28 --> 1779.46]  substantially different
[1779.46 --> 1781.24]  dialects of English
[1781.24 --> 1782.82]  then we have
[1782.82 --> 1783.54]  the acoustic model
[1783.54 --> 1784.32]  and the acoustic model
[1784.32 --> 1784.86]  is modelling
[1784.86 --> 1785.40]  as I said
[1785.40 --> 1785.88]  the sounds
[1785.88 --> 1786.48]  of the language
[1786.48 --> 1787.04]  and this is a
[1787.04 --> 1787.82]  neural network
[1787.82 --> 1789.30]  model right now
[1789.30 --> 1792.00]  and if you can train
[1792.00 --> 1793.28]  this acoustic model
[1793.28 --> 1794.10]  on different
[1794.10 --> 1795.86]  variations in speech
[1795.86 --> 1797.16]  so different accents
[1797.16 --> 1798.18]  but also not just
[1798.18 --> 1799.30]  accents but different
[1799.30 --> 1800.34]  noise conditions
[1800.34 --> 1800.84]  that are happening
[1800.84 --> 1801.48]  in the background
[1801.48 --> 1802.96]  so different
[1802.96 --> 1803.94]  microphones that
[1803.94 --> 1804.68]  people are using
[1804.68 --> 1805.76]  different distances
[1805.76 --> 1806.36]  they're talking
[1806.36 --> 1807.08]  from the microphone
[1807.08 --> 1807.86]  so there's a difference
[1807.86 --> 1808.84]  between if you're
[1808.84 --> 1809.52]  talking close up
[1809.52 --> 1810.04]  to a microphone
[1810.04 --> 1810.92]  versus if you're
[1810.92 --> 1812.12]  talking across a room
[1812.12 --> 1812.76]  to a microphone
[1812.76 --> 1814.02]  so all of these
[1814.02 --> 1815.16]  variations go into
[1815.16 --> 1815.92]  the acoustic model
[1815.92 --> 1816.86]  and the model there
[1816.86 --> 1817.98]  along with some
[1817.98 --> 1818.62]  accent
[1818.62 --> 1821.02]  and finally the
[1821.02 --> 1821.62]  language model
[1821.62 --> 1822.66]  you find that
[1822.66 --> 1824.46]  accents don't just
[1824.46 --> 1825.78]  change the sounds
[1825.78 --> 1826.44]  that people say
[1826.44 --> 1826.90]  when they say
[1826.90 --> 1827.50]  things but they
[1827.50 --> 1828.08]  might change
[1828.08 --> 1829.14]  the phrasing
[1829.14 --> 1829.94]  that people use
[1829.94 --> 1830.44]  and the order
[1830.44 --> 1831.06]  that they say
[1831.06 --> 1831.62]  words in
[1831.62 --> 1832.76]  and that's where
[1832.76 --> 1833.58]  the language model
[1833.58 --> 1834.80]  will pick some
[1834.80 --> 1835.34]  of that up
[1835.34 --> 1835.94]  and model it
[1835.94 --> 1837.20]  so I'm also
[1837.20 --> 1838.66]  curious for the
[1838.66 --> 1839.50]  acoustic model
[1839.50 --> 1839.98]  you mentioned
[1839.98 --> 1841.16]  the kind of
[1841.16 --> 1842.54]  upgrade in recent
[1842.54 --> 1843.28]  years that's really
[1843.28 --> 1844.12]  boosted performance
[1844.12 --> 1845.10]  in terms of the
[1845.10 --> 1845.92]  use of neural
[1845.92 --> 1846.34]  networks
[1846.34 --> 1848.44]  and for something
[1848.44 --> 1849.24]  like text
[1849.24 --> 1850.14]  or for images
[1850.14 --> 1850.94]  we've talked
[1850.94 --> 1851.42]  on the show
[1851.42 --> 1852.28]  about how
[1852.28 --> 1853.46]  both of these
[1853.46 --> 1855.54]  types of input
[1855.54 --> 1856.92]  data are encoded
[1856.92 --> 1858.22]  into neural
[1858.22 --> 1858.94]  network models
[1858.94 --> 1860.04]  so for example
[1860.04 --> 1860.84]  like with text
[1860.84 --> 1862.00]  you have maybe
[1862.00 --> 1863.18]  you do some
[1863.18 --> 1864.56]  type of encoding
[1864.56 --> 1865.28]  or you have a
[1865.28 --> 1865.80]  vocabulary
[1865.80 --> 1867.42]  that you're able
[1867.42 --> 1868.18]  to convert
[1868.18 --> 1869.84]  essentially strings
[1869.84 --> 1870.86]  or words
[1870.86 --> 1872.36]  into numbers
[1872.36 --> 1873.68]  similarly for
[1873.68 --> 1874.22]  images
[1874.22 --> 1874.90]  those ways of
[1874.90 --> 1875.90]  encoding images
[1875.90 --> 1877.02]  but I was wondering
[1877.02 --> 1877.86]  we haven't really
[1877.86 --> 1878.86]  talked a lot about
[1878.86 --> 1880.02]  audio data
[1880.02 --> 1881.68]  as an input
[1881.68 --> 1882.54]  to neural
[1882.54 --> 1883.26]  network models
[1883.26 --> 1884.26]  so could you
[1884.26 --> 1884.74]  describe
[1884.74 --> 1885.50]  you know
[1885.50 --> 1886.74]  what's unique
[1886.74 --> 1887.74]  about using
[1887.74 --> 1888.86]  audio as an
[1888.86 --> 1889.12]  input
[1889.12 --> 1889.68]  and how
[1889.68 --> 1890.36]  encoding that
[1890.36 --> 1890.90]  sort of data
[1890.90 --> 1891.30]  is maybe
[1891.30 --> 1891.70]  different
[1891.70 --> 1892.88]  sure
[1892.88 --> 1894.00]  so if you
[1894.00 --> 1894.78]  take a stream
[1894.78 --> 1895.26]  of audio
[1895.26 --> 1896.18]  it has some
[1896.18 --> 1897.10]  differences from
[1897.10 --> 1897.78]  text
[1897.78 --> 1898.52]  it has some
[1898.52 --> 1899.16]  differences from
[1899.16 --> 1900.04]  images you might
[1900.04 --> 1900.32]  think
[1900.32 --> 1901.24]  but there's a lot
[1901.24 --> 1901.88]  of stuff in
[1901.88 --> 1902.56]  common as well
[1902.56 --> 1903.90]  so if you take
[1903.90 --> 1904.58]  a stream of
[1904.58 --> 1904.98]  audio
[1904.98 --> 1905.72]  what we tend
[1905.72 --> 1906.28]  to do is
[1906.28 --> 1907.00]  split it into
[1907.00 --> 1907.94]  small segments
[1907.94 --> 1908.96]  so each segment
[1908.96 --> 1909.40]  of audio
[1909.40 --> 1910.54]  might be about
[1910.54 --> 1911.50]  25 milliseconds
[1911.50 --> 1911.96]  long
[1911.96 --> 1913.32]  so we have
[1913.32 --> 1914.84]  a long stream
[1914.84 --> 1915.20]  of audio
[1915.20 --> 1915.92]  which gets split
[1915.92 --> 1916.68]  into discrete
[1916.68 --> 1917.28]  segments
[1917.28 --> 1918.22]  and each of
[1918.22 --> 1918.66]  these segments
[1918.66 --> 1919.22]  is going to be
[1919.22 --> 1919.82]  one input
[1919.82 --> 1920.20]  frame
[1920.20 --> 1920.48]  it's going to
[1920.48 --> 1921.20]  be one feature
[1921.20 --> 1922.24]  one vector
[1922.24 --> 1923.02]  one feature vector
[1923.02 --> 1924.36]  in our input
[1924.36 --> 1925.12]  to our machine
[1925.12 --> 1925.66]  learning model
[1925.66 --> 1926.92]  so the next step
[1926.92 --> 1927.50]  then is to take
[1927.50 --> 1928.12]  these 25
[1928.12 --> 1929.28]  millisecond segments
[1929.28 --> 1929.72]  of audio
[1929.72 --> 1930.46]  and convert them
[1930.46 --> 1931.22]  into a vector
[1931.22 --> 1932.04]  representation
[1932.04 --> 1933.46]  and so we'll
[1933.46 --> 1933.94]  typically
[1933.94 --> 1935.52]  take this
[1935.52 --> 1936.28]  small segment
[1936.28 --> 1936.70]  of audio
[1936.70 --> 1937.02]  and we'll
[1937.02 --> 1937.60]  do a Fourier
[1937.60 --> 1938.00]  transform
[1938.00 --> 1938.94]  on it
[1938.94 --> 1940.54]  to give you
[1940.54 --> 1941.52]  the frequency
[1941.52 --> 1942.14]  distribution
[1942.14 --> 1943.18]  in that
[1943.18 --> 1944.32]  segment
[1944.32 --> 1944.88]  of audio
[1944.88 --> 1945.86]  and then we
[1945.86 --> 1946.42]  will have
[1946.42 --> 1947.04]  a filter
[1947.04 --> 1947.40]  bank
[1947.40 --> 1948.70]  which is
[1948.70 --> 1950.30]  a particular
[1950.30 --> 1951.24]  kind of set
[1951.24 --> 1951.74]  of filters
[1951.74 --> 1952.94]  triangular filters
[1952.94 --> 1954.72]  which are spaced
[1954.72 --> 1956.02]  in particular
[1956.02 --> 1956.82]  that they're
[1956.82 --> 1957.28]  centered on
[1957.28 --> 1958.26]  specific frequencies
[1958.26 --> 1959.86]  which follow
[1959.86 --> 1960.76]  a scale
[1960.76 --> 1961.94]  to sort of
[1961.94 --> 1962.60]  mimic the human
[1962.60 --> 1963.10]  ear a little
[1963.10 --> 1963.34]  bit
[1963.34 --> 1965.02]  so the
[1965.02 --> 1965.66]  filters might
[1965.66 --> 1966.56]  be further
[1966.56 --> 1967.02]  apart
[1967.02 --> 1967.80]  but spaced
[1967.80 --> 1968.38]  further apart
[1968.38 --> 1968.90]  in the higher
[1968.90 --> 1969.42]  frequency
[1969.42 --> 1970.28]  band
[1970.28 --> 1970.92]  because in
[1970.92 --> 1971.18]  the lower
[1971.18 --> 1971.58]  frequency
[1971.58 --> 1971.88]  bands
[1971.88 --> 1972.28]  that's where
[1972.28 --> 1972.56]  it is
[1972.56 --> 1973.14]  more sensitive
[1973.14 --> 1975.26]  so we
[1975.26 --> 1976.06]  pass the
[1976.06 --> 1976.60]  frequency
[1976.60 --> 1978.06]  spectrum
[1978.06 --> 1978.92]  through this
[1978.92 --> 1979.60]  filter bank
[1979.60 --> 1980.28]  just to get
[1980.28 --> 1981.12]  a set
[1981.12 --> 1982.50]  of filter
[1982.50 --> 1982.78]  bank
[1982.78 --> 1983.32]  coefficients
[1983.32 --> 1984.04]  which we
[1984.04 --> 1984.54]  can use
[1984.54 --> 1985.26]  as features
[1985.26 --> 1986.68]  for our
[1986.68 --> 1987.56]  neural networks
[1993.34 --> 1997.42]  in case
[1997.42 --> 1997.82]  you missed
[1997.82 --> 1998.02]  it
[1998.02 --> 1998.34]  Manning
[1998.34 --> 1998.72]  hooked us
[1998.72 --> 1999.16]  up with
[1999.16 --> 1999.72]  three
[1999.72 --> 2000.20]  free
[2000.20 --> 2000.62]  ebook
[2000.62 --> 2001.04]  copies
[2001.04 --> 2001.42]  of
[2001.42 --> 2001.78]  build
[2001.78 --> 2002.00]  a
[2002.00 --> 2002.38]  career
[2002.38 --> 2002.68]  in
[2002.68 --> 2002.88]  data
[2002.88 --> 2003.42]  science
[2003.42 --> 2004.06]  we
[2004.06 --> 2004.22]  had
[2004.22 --> 2004.36]  one
[2004.36 --> 2004.46]  of
[2004.46 --> 2004.58]  the
[2004.58 --> 2004.90]  authors
[2004.90 --> 2005.26]  Emily
[2005.26 --> 2005.68]  Robinson
[2005.68 --> 2006.36]  on episode
[2006.36 --> 2006.66]  number
[2006.66 --> 2007.08]  81
[2007.08 --> 2007.80]  to discuss
[2007.80 --> 2008.42]  if you
[2008.42 --> 2008.66]  want to
[2008.66 --> 2009.02]  get your
[2009.02 --> 2009.42]  eyeballs
[2009.42 --> 2009.94]  on this
[2009.94 --> 2010.34]  excellent
[2010.34 --> 2010.78]  resource
[2010.78 --> 2011.26]  all you
[2011.26 --> 2011.50]  have to
[2011.50 --> 2011.70]  do
[2011.70 --> 2012.04]  is leave
[2012.04 --> 2012.50]  a comment
[2012.50 --> 2012.88]  on the
[2012.88 --> 2013.18]  episode
[2013.18 --> 2013.54]  page
[2013.54 --> 2013.96]  tell us
[2013.96 --> 2014.14]  about
[2014.14 --> 2014.36]  your
[2014.36 --> 2014.66]  career
[2014.66 --> 2014.82]  in
[2014.82 --> 2014.98]  data
[2014.98 --> 2015.30]  science
[2015.30 --> 2015.44]  and
[2015.44 --> 2015.54]  how
[2015.54 --> 2015.68]  the
[2015.68 --> 2015.82]  book
[2015.82 --> 2016.04]  might
[2016.04 --> 2016.30]  help
[2016.30 --> 2016.64]  you
[2016.64 --> 2017.20]  head
[2017.20 --> 2017.34]  to
[2017.34 --> 2017.56]  change
[2017.56 --> 2017.70]  all
[2017.70 --> 2018.18]  dot com
[2018.18 --> 2018.52]  slash
[2018.52 --> 2019.04]  practical
[2019.04 --> 2019.40]  AI
[2019.40 --> 2019.92]  slash
[2019.92 --> 2020.32]  81
[2020.32 --> 2020.66]  and
[2020.66 --> 2020.94]  click
[2020.94 --> 2021.12]  the
[2021.12 --> 2021.46]  discuss
[2021.46 --> 2021.72]  link
[2021.72 --> 2022.12]  on the
[2022.12 --> 2022.30]  play
[2022.30 --> 2022.52]  bar
[2022.52 --> 2022.90]  you
[2022.90 --> 2023.08]  have
[2023.08 --> 2023.32]  until
[2023.32 --> 2023.54]  April
[2023.54 --> 2023.94]  12th
[2023.94 --> 2024.04]  to
[2024.04 --> 2024.30]  enter
[2024.30 --> 2025.30]  once
[2025.30 --> 2025.52]  again
[2025.52 --> 2025.80]  that's
[2025.80 --> 2026.80]  changelog.com
[2026.80 --> 2027.20]  slash
[2027.20 --> 2027.68]  practical
[2027.68 --> 2028.08]  AI
[2028.08 --> 2028.64]  slash
[2028.64 --> 2029.08]  81
[2029.08 --> 2048.84]  so
[2048.84 --> 2049.26]  Catherine
[2049.26 --> 2049.60]  I'm
[2049.60 --> 2049.82]  kind
[2049.82 --> 2050.02]  of
[2050.02 --> 2050.50]  curious
[2050.50 --> 2050.80]  I've
[2050.80 --> 2050.90]  been
[2050.90 --> 2051.10]  learning
[2051.10 --> 2051.38]  a lot
[2051.38 --> 2051.58]  from
[2051.58 --> 2051.70]  you
[2051.70 --> 2051.84]  here
[2051.84 --> 2052.10]  today
[2052.10 --> 2052.38]  thank
[2052.38 --> 2052.48]  you
[2052.48 --> 2052.64]  very
[2052.64 --> 2052.92]  much
[2052.92 --> 2053.42]  what
[2053.42 --> 2053.60]  is
[2053.60 --> 2053.82]  the
[2053.82 --> 2054.50]  state
[2054.50 --> 2054.80]  of
[2054.80 --> 2055.08]  speech
[2055.08 --> 2055.50]  recognition
[2055.50 --> 2055.82]  right
[2055.82 --> 2056.14]  now
[2056.14 --> 2056.84]  kind
[2056.84 --> 2056.98]  of
[2056.98 --> 2057.22]  for
[2057.22 --> 2057.64]  higher
[2057.64 --> 2058.14]  resource
[2058.14 --> 2058.62]  languages
[2058.62 --> 2059.12]  what
[2059.12 --> 2059.24]  does
[2059.24 --> 2059.38]  the
[2059.38 --> 2059.76]  accuracy
[2059.76 --> 2060.10]  look
[2060.10 --> 2060.44]  like
[2060.44 --> 2060.64]  at
[2060.64 --> 2060.84]  this
[2060.84 --> 2061.18]  point
[2061.18 --> 2061.82]  what
[2061.82 --> 2061.94]  are
[2061.94 --> 2062.10]  the
[2062.10 --> 2062.38]  current
[2062.38 --> 2062.94]  challenges
[2062.94 --> 2063.68]  that
[2063.68 --> 2063.84]  you
[2063.84 --> 2064.08]  guys
[2064.08 --> 2064.24]  are
[2064.24 --> 2064.60]  dealing
[2064.60 --> 2065.02]  with
[2065.02 --> 2065.46]  going
[2065.46 --> 2065.80]  forward
[2065.80 --> 2066.06]  and
[2066.06 --> 2066.36]  what
[2066.36 --> 2066.54]  kind
[2066.54 --> 2066.62]  of
[2066.62 --> 2067.16]  improvements
[2067.16 --> 2067.62]  are
[2067.62 --> 2068.04]  you
[2068.04 --> 2069.12]  expecting
[2069.12 --> 2069.42]  or
[2069.42 --> 2069.82]  striving
[2069.82 --> 2070.34]  toward
[2070.34 --> 2070.86]  to
[2070.86 --> 2071.18]  meet
[2071.18 --> 2071.42]  those
[2071.42 --> 2071.74]  current
[2071.74 --> 2072.40]  challenges
[2072.40 --> 2073.32]  yes
[2073.32 --> 2073.58]  I think
[2073.58 --> 2073.72]  you're
[2073.72 --> 2074.04]  right to
[2074.04 --> 2074.20]  think
[2074.20 --> 2074.44]  about
[2074.44 --> 2074.92]  high
[2074.92 --> 2075.26]  resource
[2075.26 --> 2075.64]  languages
[2075.64 --> 2076.04]  versus
[2076.04 --> 2076.64]  low
[2076.64 --> 2077.00]  resource
[2077.00 --> 2077.40]  languages
[2077.40 --> 2077.76]  because
[2077.76 --> 2078.04]  we've
[2078.04 --> 2078.14]  been
[2078.14 --> 2078.54]  doing
[2078.54 --> 2079.24]  speech
[2079.24 --> 2079.58]  recognition
[2079.58 --> 2080.12]  research
[2080.12 --> 2080.28]  in
[2080.28 --> 2080.72]  English
[2080.72 --> 2081.44]  for
[2081.44 --> 2081.84]  many
[2081.84 --> 2082.16]  years
[2082.16 --> 2082.34]  now
[2082.34 --> 2082.50]  so
[2082.50 --> 2082.84]  obviously
[2082.84 --> 2083.54]  there's
[2083.54 --> 2083.80]  a lot
[2083.80 --> 2084.04]  more
[2084.04 --> 2084.40]  data
[2084.40 --> 2084.86]  available
[2084.86 --> 2085.24]  a lot
[2085.24 --> 2085.50]  more
[2085.50 --> 2086.10]  benchmarks
[2086.10 --> 2086.52]  a lot
[2086.52 --> 2086.86]  more
[2086.86 --> 2087.52]  knowledge
[2087.52 --> 2088.38]  that's
[2088.38 --> 2088.64]  been
[2088.64 --> 2089.30]  spread
[2089.30 --> 2089.66]  around
[2089.66 --> 2090.58]  and so
[2090.58 --> 2091.50]  there are
[2091.50 --> 2091.76]  still
[2091.76 --> 2092.18]  some
[2092.18 --> 2092.74]  challenges
[2092.74 --> 2093.12]  when it
[2093.12 --> 2093.38]  comes
[2093.38 --> 2093.56]  to
[2093.56 --> 2093.82]  building
[2093.82 --> 2094.06]  good
[2094.06 --> 2094.30]  speech
[2094.30 --> 2094.68]  recognition
[2094.68 --> 2095.36]  systems
[2095.36 --> 2096.66]  and
[2096.66 --> 2097.44]  they have
[2097.44 --> 2097.72]  different
[2097.72 --> 2098.24]  dimensions
[2098.24 --> 2098.64]  of
[2098.64 --> 2099.36]  difficulty
[2099.36 --> 2100.26]  to deal
[2100.26 --> 2100.52]  with
[2100.52 --> 2100.92]  so
[2100.92 --> 2101.62]  noise
[2101.62 --> 2102.02]  is one
[2102.02 --> 2102.40]  dimension
[2102.40 --> 2103.66]  so
[2103.66 --> 2104.26]  if
[2104.26 --> 2104.56]  you're
[2104.56 --> 2104.92]  speaking
[2104.92 --> 2105.40]  in a
[2105.40 --> 2105.62]  nice
[2105.62 --> 2106.02]  quiet
[2106.02 --> 2106.36]  room
[2106.36 --> 2107.14]  that's
[2107.14 --> 2107.34]  very
[2107.34 --> 2107.68]  different
[2107.68 --> 2107.94]  speech
[2107.94 --> 2108.28]  recognition
[2108.28 --> 2108.92]  performance
[2108.92 --> 2109.24]  to if
[2109.24 --> 2109.38]  you're
[2109.38 --> 2109.72]  speaking
[2109.72 --> 2110.18]  in a
[2110.18 --> 2110.50]  car
[2110.50 --> 2111.16]  or if
[2111.16 --> 2111.28]  you're
[2111.28 --> 2111.64]  speaking
[2111.64 --> 2112.44]  in a
[2112.44 --> 2112.64]  noisy
[2112.64 --> 2113.04]  environment
[2113.04 --> 2113.26]  like
[2113.26 --> 2113.48]  you have
[2113.48 --> 2113.70]  some
[2113.70 --> 2114.10]  machinery
[2114.10 --> 2114.64]  behind
[2114.64 --> 2114.90]  you
[2114.90 --> 2115.18]  things
[2115.18 --> 2115.40]  like
[2115.40 --> 2115.62]  that
[2115.62 --> 2115.90]  so
[2115.90 --> 2116.76]  noise
[2116.76 --> 2116.96]  is
[2116.96 --> 2117.12]  still
[2117.12 --> 2117.34]  one
[2117.34 --> 2117.50]  thing
[2117.50 --> 2117.66]  which
[2117.66 --> 2117.90]  makes
[2117.90 --> 2118.14]  speech
[2118.14 --> 2118.54]  recognition
[2118.54 --> 2118.96]  hard
[2118.96 --> 2119.98]  there's
[2119.98 --> 2120.36]  other
[2120.36 --> 2121.62]  challenges
[2121.62 --> 2122.02]  as well
[2122.02 --> 2122.38]  such
[2122.38 --> 2123.06]  as
[2123.06 --> 2123.66]  the
[2123.66 --> 2124.10]  style
[2124.10 --> 2124.28]  of
[2124.28 --> 2124.68]  speech
[2124.68 --> 2125.70]  so
[2125.70 --> 2125.92]  when
[2125.92 --> 2126.24]  someone
[2126.24 --> 2126.48]  is
[2126.48 --> 2127.08]  speaking
[2127.08 --> 2127.52]  if
[2127.52 --> 2127.70]  they're
[2127.70 --> 2127.98]  standing
[2127.98 --> 2128.26]  up
[2128.26 --> 2128.98]  addressing
[2128.98 --> 2129.58]  people
[2129.58 --> 2129.90]  or
[2129.90 --> 2130.12]  if
[2130.12 --> 2130.42]  they
[2130.42 --> 2130.98]  are
[2130.98 --> 2132.28]  reading
[2132.28 --> 2132.80]  text
[2132.80 --> 2134.16]  they
[2134.16 --> 2134.46]  speak
[2134.46 --> 2134.60]  in
[2134.60 --> 2134.74]  very
[2134.74 --> 2135.00]  different
[2135.00 --> 2135.30]  ways
[2135.30 --> 2135.52]  if
[2135.52 --> 2135.72]  you're
[2135.72 --> 2135.90]  just
[2135.90 --> 2136.12]  having
[2136.12 --> 2136.22]  a
[2136.22 --> 2136.38]  back
[2136.38 --> 2136.50]  and
[2136.50 --> 2136.64]  forth
[2136.64 --> 2137.16]  conversation
[2137.16 --> 2137.44]  in a
[2137.44 --> 2137.64]  meeting
[2137.64 --> 2137.84]  room
[2137.84 --> 2138.00]  with
[2138.00 --> 2138.14]  some
[2138.14 --> 2138.50]  friends
[2138.50 --> 2140.12]  people
[2140.12 --> 2140.28]  are
[2140.28 --> 2140.46]  much
[2140.46 --> 2140.86]  less
[2140.86 --> 2141.50]  formal
[2141.50 --> 2141.96]  when
[2141.96 --> 2142.16]  they're
[2142.16 --> 2142.48]  having
[2142.48 --> 2143.44]  lots
[2143.44 --> 2143.64]  of
[2143.64 --> 2143.90]  heated
[2143.90 --> 2144.36]  discussions
[2144.36 --> 2144.92]  and
[2144.92 --> 2145.26]  their
[2145.26 --> 2145.68]  voice
[2145.68 --> 2145.96]  and the
[2145.96 --> 2146.06]  way
[2146.06 --> 2146.36]  they say
[2146.36 --> 2146.60]  things
[2146.60 --> 2146.76]  are
[2146.76 --> 2147.10]  slightly
[2147.10 --> 2147.52]  different
[2147.52 --> 2148.12]  so
[2148.12 --> 2148.38]  that's
[2148.38 --> 2148.68]  another
[2148.68 --> 2149.70]  dimension
[2149.70 --> 2149.98]  of
[2149.98 --> 2150.44]  difficulty
[2150.44 --> 2150.78]  there
[2150.78 --> 2151.10]  in
[2151.10 --> 2151.42]  that
[2151.42 --> 2152.60]  if
[2152.60 --> 2152.78]  you're
[2152.78 --> 2152.94]  trying
[2152.94 --> 2153.12]  to
[2153.12 --> 2153.50]  recognize
[2153.50 --> 2153.90]  people
[2153.90 --> 2154.56]  reading
[2154.56 --> 2155.90]  a
[2155.90 --> 2156.16]  passage
[2156.16 --> 2156.32]  of
[2156.32 --> 2156.58]  text
[2156.58 --> 2156.70]  to
[2156.70 --> 2156.78]  a
[2156.78 --> 2156.94]  large
[2156.94 --> 2157.12]  group
[2157.12 --> 2157.24]  of
[2157.24 --> 2157.48]  people
[2157.48 --> 2157.74]  that's
[2157.74 --> 2158.06]  easier
[2158.06 --> 2158.46]  than
[2158.46 --> 2158.72]  trying
[2158.72 --> 2158.88]  to
[2158.88 --> 2159.30]  transcribe
[2159.30 --> 2159.60]  people
[2159.60 --> 2159.84]  in a
[2159.84 --> 2160.12]  meeting
[2160.12 --> 2161.44]  where
[2161.44 --> 2161.92]  they're
[2161.92 --> 2162.38]  passionately
[2162.38 --> 2162.84]  discussing
[2162.84 --> 2163.12]  lots of
[2163.12 --> 2163.38]  different
[2163.38 --> 2163.84]  ideas
[2163.84 --> 2164.60]  things
[2164.60 --> 2164.78]  like
[2164.78 --> 2165.26]  accent
[2165.26 --> 2166.18]  is also
[2166.18 --> 2166.72]  something
[2166.72 --> 2167.10]  which can
[2167.10 --> 2167.28]  be
[2167.28 --> 2167.58]  difficult
[2167.58 --> 2167.94]  to deal
[2167.94 --> 2168.26]  with
[2168.26 --> 2168.74]  if you
[2168.74 --> 2168.96]  have
[2168.96 --> 2169.46]  heavily
[2169.46 --> 2170.14]  accented
[2170.14 --> 2171.06]  English
[2171.06 --> 2171.88]  that can
[2171.88 --> 2173.38]  make it
[2173.38 --> 2173.72]  harder
[2173.72 --> 2174.34]  to recognize
[2174.34 --> 2175.50]  and also
[2175.50 --> 2175.78]  if you
[2175.78 --> 2176.42]  have to
[2176.42 --> 2177.02]  recognize
[2177.02 --> 2178.60]  specific
[2178.60 --> 2179.24]  domains
[2179.24 --> 2179.58]  so
[2179.58 --> 2180.28]  specific
[2180.28 --> 2181.24]  types
[2181.24 --> 2181.66]  of language
[2181.66 --> 2182.00]  that can
[2182.00 --> 2182.28]  be more
[2182.28 --> 2182.60]  difficult
[2182.60 --> 2182.92]  so
[2182.92 --> 2183.40]  if
[2183.40 --> 2183.54]  you
[2183.54 --> 2183.92]  have
[2183.92 --> 2184.66]  a
[2184.66 --> 2184.86]  speech
[2184.86 --> 2185.30]  recognition
[2185.30 --> 2185.74]  model
[2185.74 --> 2186.10]  which
[2186.10 --> 2186.26]  is
[2186.26 --> 2186.52]  trained
[2186.52 --> 2186.68]  on
[2186.68 --> 2186.98]  general
[2186.98 --> 2187.64]  conversational
[2187.64 --> 2188.20]  English
[2188.20 --> 2189.06]  but you
[2189.06 --> 2189.48]  try and
[2189.48 --> 2189.94]  use that
[2189.94 --> 2190.16]  to
[2190.16 --> 2190.82]  recognize
[2190.82 --> 2191.78]  somebody
[2191.78 --> 2192.02]  giving
[2192.02 --> 2192.34]  lectures
[2192.34 --> 2192.54]  on
[2192.54 --> 2192.98]  chemistry
[2192.98 --> 2194.30]  you see
[2194.30 --> 2194.42]  a
[2194.42 --> 2194.74]  degradation
[2194.74 --> 2195.00]  in
[2195.00 --> 2195.42]  performance
[2195.42 --> 2195.76]  because
[2195.76 --> 2196.02]  the
[2196.02 --> 2196.38]  two
[2196.38 --> 2196.98]  scenarios
[2196.98 --> 2197.30]  are not
[2197.30 --> 2197.54]  well
[2197.54 --> 2197.90]  matched
[2197.90 --> 2198.20]  up
[2198.20 --> 2199.42]  and so
[2199.42 --> 2199.54]  I
[2199.54 --> 2199.66]  think
[2199.66 --> 2199.80]  in
[2199.80 --> 2199.98]  high
[2199.98 --> 2200.26]  resource
[2200.26 --> 2200.58]  languages
[2200.58 --> 2200.84]  we're
[2200.84 --> 2201.04]  really
[2201.04 --> 2201.30]  good
[2201.30 --> 2201.44]  at
[2201.44 --> 2201.98]  building
[2201.98 --> 2202.26]  very
[2202.26 --> 2202.56]  good
[2202.56 --> 2202.96]  general
[2202.96 --> 2203.40]  purpose
[2203.40 --> 2203.68]  speech
[2203.68 --> 2204.04]  recognition
[2204.04 --> 2204.72]  systems
[2204.72 --> 2206.24]  but when
[2206.24 --> 2206.38]  it
[2206.38 --> 2206.60]  comes
[2206.60 --> 2206.76]  to
[2206.76 --> 2207.00]  building
[2207.00 --> 2207.60]  specific
[2207.60 --> 2207.88]  speech
[2207.88 --> 2208.22]  recognition
[2208.22 --> 2208.84]  systems
[2208.84 --> 2209.06]  to
[2209.06 --> 2209.34]  work
[2209.34 --> 2209.56]  in
[2209.56 --> 2210.30]  specific
[2210.30 --> 2210.60]  noise
[2212.60 --> 2213.02]  types
[2213.02 --> 2213.26]  of
[2213.26 --> 2214.04]  tasks
[2214.04 --> 2214.22]  like
[2214.22 --> 2214.64]  chemistry
[2214.64 --> 2215.14]  lectures
[2215.14 --> 2215.88]  or
[2215.88 --> 2217.08]  specific
[2217.08 --> 2217.68]  accents
[2217.68 --> 2218.46]  specific
[2218.46 --> 2218.94]  types
[2218.94 --> 2219.22]  of
[2219.22 --> 2219.78]  condition
[2219.78 --> 2220.42]  that's
[2220.42 --> 2220.58]  where
[2220.58 --> 2220.70]  I
[2220.70 --> 2220.86]  think
[2220.86 --> 2220.96]  it
[2220.96 --> 2221.14]  gets
[2221.14 --> 2221.36]  much
[2221.36 --> 2221.54]  more
[2221.54 --> 2221.88]  difficult
[2221.88 --> 2222.72]  even
[2222.72 --> 2222.94]  in
[2222.94 --> 2223.12]  high
[2223.12 --> 2223.46]  resource
[2223.46 --> 2223.86]  languages
[2223.86 --> 2224.60]  we don't
[2224.60 --> 2224.92]  always
[2224.92 --> 2225.12]  have
[2225.12 --> 2225.32]  lots
[2225.32 --> 2225.44]  of
[2225.44 --> 2225.70]  data
[2225.70 --> 2225.90]  in
[2225.90 --> 2226.08]  those
[2226.08 --> 2226.50]  scenarios
[2226.50 --> 2227.30]  and so
[2227.30 --> 2227.54]  that's
[2227.54 --> 2227.68]  one
[2227.68 --> 2228.18]  of the
[2228.18 --> 2228.52]  areas
[2228.52 --> 2228.80]  that we
[2228.80 --> 2229.06]  work
[2229.06 --> 2229.24]  on
[2229.24 --> 2229.50]  a lot
[2229.50 --> 2229.74]  is
[2229.74 --> 2229.88]  to
[2229.88 --> 2230.12]  try
[2230.12 --> 2230.26]  and
[2230.26 --> 2230.66]  build
[2230.66 --> 2231.32]  speech
[2231.32 --> 2231.68]  recognition
[2231.68 --> 2232.20]  systems
[2232.20 --> 2232.68]  customized
[2232.68 --> 2233.14]  to
[2233.14 --> 2233.46]  different
[2233.46 --> 2233.98]  domains
[2233.98 --> 2234.24]  to
[2234.24 --> 2234.50]  different
[2234.50 --> 2235.06]  scenarios
[2235.06 --> 2235.36]  to
[2235.36 --> 2235.56]  different
[2235.56 --> 2236.00]  purposes
[2236.00 --> 2237.42]  so
[2237.42 --> 2238.26]  you
[2238.26 --> 2238.58]  brought up
[2238.58 --> 2238.88]  something
[2238.88 --> 2239.20]  that
[2239.20 --> 2239.54]  kind
[2239.54 --> 2239.84]  of
[2239.84 --> 2240.04]  I
[2242.60 --> 2242.78]  the
[2242.78 --> 2243.20]  problem
[2243.20 --> 2243.54]  and
[2243.54 --> 2243.64]  I
[2243.64 --> 2243.78]  was
[2243.78 --> 2244.04]  thinking
[2244.04 --> 2244.42]  mostly
[2244.42 --> 2244.66]  of
[2244.66 --> 2244.98]  I'm
[2244.98 --> 2245.08]  going
[2245.08 --> 2245.20]  to
[2245.20 --> 2245.42]  speak
[2245.42 --> 2245.62]  into
[2245.62 --> 2245.78]  a
[2245.78 --> 2246.18]  microphone
[2246.18 --> 2246.52]  and
[2246.52 --> 2246.78]  then
[2246.78 --> 2247.48]  the
[2247.48 --> 2247.90]  computer
[2247.90 --> 2248.06]  is
[2248.06 --> 2248.18]  going
[2248.18 --> 2248.26]  to
[2248.26 --> 2248.46]  figure
[2248.46 --> 2248.86]  out
[2248.86 --> 2249.94]  the
[2249.94 --> 2250.68]  corresponding
[2250.68 --> 2251.34]  text
[2251.34 --> 2251.64]  but
[2251.64 --> 2252.16]  in
[2252.16 --> 2252.54]  scenarios
[2252.54 --> 2252.76]  where
[2252.76 --> 2252.88]  you
[2252.88 --> 2253.08]  have
[2253.08 --> 2253.46]  multiple
[2253.46 --> 2253.94]  speakers
[2253.94 --> 2254.14]  or
[2254.14 --> 2254.52]  noise
[2254.52 --> 2254.74]  like
[2254.74 --> 2254.86]  you
[2254.86 --> 2255.14]  mentioned
[2255.14 --> 2255.68]  there's
[2255.68 --> 2256.14]  a lot
[2256.14 --> 2256.60]  going
[2256.60 --> 2256.94]  on
[2256.94 --> 2257.24]  there
[2257.24 --> 2258.30]  do
[2258.30 --> 2258.62]  people
[2258.62 --> 2258.92]  deal
[2258.92 --> 2259.12]  with
[2259.12 --> 2259.36]  that
[2259.36 --> 2260.10]  sometimes
[2260.10 --> 2260.58]  as
[2260.58 --> 2260.78]  kind
[2260.78 --> 2260.88]  of
[2260.88 --> 2261.30]  another
[2261.30 --> 2261.80]  layer
[2261.80 --> 2262.06]  of
[2262.06 --> 2262.38]  this
[2262.38 --> 2262.82]  three
[2262.82 --> 2263.24]  step
[2263.24 --> 2263.72]  process
[2263.72 --> 2264.06]  like
[2264.06 --> 2264.54]  maybe
[2264.54 --> 2265.14]  speaker
[2265.14 --> 2266.40]  segmentation
[2266.40 --> 2266.68]  or
[2266.68 --> 2267.10]  picking
[2267.10 --> 2267.36]  out
[2267.36 --> 2267.78]  speakers
[2267.78 --> 2268.02]  is
[2268.02 --> 2268.28]  that
[2268.28 --> 2268.84]  can
[2268.84 --> 2269.00]  that
[2269.00 --> 2269.18]  be
[2269.18 --> 2270.02]  bolted
[2270.02 --> 2270.62]  onto
[2270.62 --> 2271.52]  the
[2271.52 --> 2272.04]  other
[2272.04 --> 2272.64]  type
[2272.64 --> 2272.80]  of
[2272.80 --> 2273.18]  system
[2273.18 --> 2274.36]  it
[2274.36 --> 2274.66]  can
[2274.66 --> 2274.84]  be
[2274.84 --> 2275.16]  yes
[2275.16 --> 2275.58]  so
[2275.58 --> 2275.92]  you
[2275.92 --> 2276.12]  can
[2276.12 --> 2276.68]  identify
[2276.68 --> 2277.56]  speakers
[2277.56 --> 2277.82]  in
[2277.82 --> 2278.42]  different
[2278.42 --> 2279.34]  ways
[2279.34 --> 2280.26]  if
[2280.26 --> 2280.42]  you
[2280.42 --> 2280.84]  have
[2280.84 --> 2281.48]  a
[2281.48 --> 2281.70]  room
[2281.70 --> 2282.20]  which
[2282.20 --> 2282.52]  speakers
[2282.52 --> 2282.66]  are
[2282.66 --> 2282.86]  sitting
[2282.86 --> 2283.08]  around
[2283.08 --> 2283.20]  and
[2283.20 --> 2283.30]  you
[2283.30 --> 2283.46]  have
[2283.46 --> 2283.82]  a
[2283.82 --> 2284.16]  microphone
[2284.16 --> 2284.36]  in
[2284.36 --> 2284.46]  the
[2284.46 --> 2284.60]  middle
[2284.60 --> 2284.78]  that
[2284.78 --> 2284.96]  is
[2284.96 --> 2285.34]  fixed
[2285.34 --> 2285.78]  you
[2285.78 --> 2285.94]  can
[2285.94 --> 2286.16]  use
[2286.16 --> 2286.28]  a
[2286.28 --> 2286.60]  microphone
[2286.60 --> 2286.96]  array
[2286.96 --> 2287.66]  for
[2287.66 --> 2288.06]  example
[2288.06 --> 2288.50]  and
[2288.50 --> 2288.60]  a
[2288.60 --> 2288.96]  microphone
[2288.96 --> 2289.28]  array
[2289.28 --> 2289.52]  has
[2289.52 --> 2289.86]  got
[2289.86 --> 2290.44]  more
[2290.44 --> 2290.56]  than
[2290.56 --> 2290.74]  one
[2290.74 --> 2291.24]  microphone
[2291.24 --> 2291.68]  in
[2291.68 --> 2291.80]  the
[2291.80 --> 2291.92]  middle
[2291.92 --> 2292.02]  of
[2292.02 --> 2292.10]  the
[2292.10 --> 2292.36]  table
[2292.36 --> 2292.68]  often
[2292.68 --> 2293.12]  some
[2293.12 --> 2293.26]  of
[2293.26 --> 2293.44]  these
[2293.44 --> 2293.64]  might
[2293.64 --> 2293.92]  have
[2293.92 --> 2294.42]  say
[2294.42 --> 2294.74]  seven
[2294.74 --> 2295.16]  microphones
[2295.16 --> 2295.46]  in
[2295.46 --> 2295.58]  a
[2295.58 --> 2295.88]  circle
[2295.88 --> 2296.90]  and
[2296.90 --> 2297.10]  there
[2297.10 --> 2297.22]  you
[2297.22 --> 2297.38]  can
[2297.38 --> 2297.62]  actually
[2297.62 --> 2297.78]  do
[2297.78 --> 2298.02]  something
[2298.02 --> 2298.32]  which
[2298.32 --> 2298.40]  I
[2298.40 --> 2298.52]  think
[2298.52 --> 2298.64]  is
[2298.64 --> 2299.20]  quite
[2299.20 --> 2299.52]  smart
[2299.52 --> 2299.82]  which
[2299.82 --> 2300.14]  is
[2300.14 --> 2300.44]  figure
[2300.44 --> 2300.92]  out
[2300.92 --> 2301.64]  the
[2301.64 --> 2302.06]  direction
[2302.06 --> 2302.42]  that
[2302.42 --> 2302.78]  a
[2302.78 --> 2302.98]  voice
[2302.98 --> 2303.10]  is
[2303.10 --> 2303.32]  coming
[2303.32 --> 2303.66]  from
[2303.66 --> 2304.80]  because
[2304.80 --> 2306.28]  when
[2306.28 --> 2306.52]  people
[2306.52 --> 2306.96]  speak
[2306.96 --> 2307.20]  their
[2307.20 --> 2307.62]  voice
[2307.62 --> 2307.86]  takes
[2307.86 --> 2307.98]  a
[2307.98 --> 2308.10]  little
[2308.10 --> 2308.34]  time
[2308.34 --> 2308.48]  to
[2308.48 --> 2308.78]  travel
[2308.78 --> 2309.10]  and
[2309.10 --> 2309.22]  if
[2309.22 --> 2309.30]  you
[2309.30 --> 2309.48]  have
[2309.48 --> 2309.92]  two
[2309.92 --> 2310.36]  microphones
[2310.36 --> 2310.52]  in
[2310.52 --> 2310.62]  the
[2310.62 --> 2310.76]  middle
[2310.76 --> 2310.90]  of
[2310.90 --> 2311.00]  the
[2311.00 --> 2311.34]  table
[2311.34 --> 2311.78]  their
[2311.78 --> 2312.08]  voice
[2312.08 --> 2312.24]  will
[2312.24 --> 2312.38]  get
[2312.38 --> 2312.50]  to
[2312.50 --> 2312.58]  the
[2312.58 --> 2312.94]  microphone
[2312.94 --> 2313.38]  closest
[2313.38 --> 2313.58]  to
[2313.58 --> 2313.72]  them
[2313.72 --> 2314.02]  just
[2314.02 --> 2314.68]  fractionally
[2314.68 --> 2314.92]  before
[2314.92 --> 2315.10]  it
[2315.10 --> 2315.26]  gets
[2315.26 --> 2315.38]  to
[2315.38 --> 2315.46]  the
[2315.46 --> 2315.60]  one
[2315.60 --> 2315.86]  further
[2315.86 --> 2316.22]  away
[2316.22 --> 2316.96]  and
[2316.96 --> 2317.10]  so
[2317.10 --> 2317.44]  using
[2317.44 --> 2317.66]  that
[2317.66 --> 2317.80]  you
[2317.80 --> 2317.96]  can
[2317.96 --> 2318.18]  figure
[2318.18 --> 2318.38]  out
[2318.38 --> 2318.62]  where
[2318.62 --> 2318.74]  in
[2318.74 --> 2318.82]  the
[2318.82 --> 2319.00]  room
[2319.00 --> 2319.26]  someone
[2319.26 --> 2319.58]  is
[2319.58 --> 2320.46]  so
[2320.46 --> 2320.64]  this
[2320.64 --> 2320.78]  is
[2320.78 --> 2321.18]  a
[2321.18 --> 2321.40]  great
[2321.40 --> 2321.60]  way
[2321.60 --> 2321.74]  to
[2321.74 --> 2322.06]  separate
[2322.06 --> 2322.44]  speakers
[2322.44 --> 2322.60]  in
[2322.60 --> 2322.72]  a
[2322.72 --> 2322.92]  room
[2322.92 --> 2323.12]  if
[2323.12 --> 2323.22]  you
[2323.22 --> 2323.52]  have
[2323.52 --> 2324.00]  a
[2324.00 --> 2324.36]  microphone
[2324.36 --> 2324.70]  array
[2324.70 --> 2324.92]  to
[2324.92 --> 2325.16]  help
[2325.16 --> 2325.34]  you
[2325.34 --> 2326.84]  you
[2326.84 --> 2327.02]  might
[2327.02 --> 2327.16]  not
[2327.16 --> 2327.38]  always
[2327.38 --> 2327.66]  have
[2327.66 --> 2327.92]  a
[2327.92 --> 2328.22]  microphone
[2328.22 --> 2328.50]  array
[2328.50 --> 2328.78]  if
[2328.78 --> 2328.96]  you've
[2328.96 --> 2329.12]  got
[2329.12 --> 2329.34]  some
[2329.34 --> 2329.56]  sort
[2329.56 --> 2329.74]  of
[2329.74 --> 2331.10]  online
[2331.10 --> 2331.80]  conferencing
[2331.80 --> 2332.06]  where
[2332.06 --> 2332.58]  everyone's
[2332.58 --> 2333.14]  busy
[2333.14 --> 2333.82]  talking
[2333.82 --> 2334.12]  on their
[2334.12 --> 2334.30]  own
[2334.30 --> 2334.66]  computer
[2334.66 --> 2334.96]  and
[2334.96 --> 2335.18]  they
[2335.18 --> 2335.60]  are
[2335.60 --> 2336.36]  talking
[2336.36 --> 2336.56]  into
[2336.56 --> 2336.68]  a
[2336.68 --> 2336.88]  central
[2336.88 --> 2337.24]  system
[2337.24 --> 2337.52]  you
[2337.52 --> 2337.96]  might
[2337.96 --> 2338.26]  actually
[2338.26 --> 2338.54]  have
[2338.54 --> 2338.80]  access
[2338.80 --> 2339.00]  to
[2339.00 --> 2339.12]  all
[2339.12 --> 2339.24]  of
[2339.24 --> 2339.56]  those
[2339.56 --> 2340.18]  separate
[2340.18 --> 2340.66]  microphones
[2340.66 --> 2340.94]  which
[2340.94 --> 2341.20]  is
[2341.20 --> 2341.60]  super
[2341.60 --> 2341.92]  helpful
[2341.92 --> 2342.60]  but
[2342.60 --> 2342.70]  if
[2342.70 --> 2342.82]  you
[2342.82 --> 2343.16]  don't
[2343.16 --> 2343.34]  you
[2343.34 --> 2343.64]  can
[2343.64 --> 2344.02]  use
[2344.02 --> 2344.16]  the
[2344.16 --> 2344.56]  characteristics
[2344.56 --> 2344.78]  of
[2344.78 --> 2345.04]  people's
[2345.04 --> 2345.28]  voice
[2345.28 --> 2345.42]  to
[2345.42 --> 2345.62]  be able
[2345.62 --> 2345.76]  to
[2345.76 --> 2345.90]  tell
[2345.90 --> 2346.02]  them
[2346.02 --> 2346.32]  apart
[2346.32 --> 2346.54]  as
[2346.54 --> 2346.94]  well
[2346.94 --> 2347.14]  so
[2347.14 --> 2347.38]  there's
[2347.38 --> 2347.58]  different
[2347.58 --> 2347.76]  ways
[2347.76 --> 2347.84]  you
[2347.84 --> 2347.94]  can
[2347.94 --> 2348.08]  do
[2348.08 --> 2348.22]  it
[2348.22 --> 2348.40]  and
[2348.40 --> 2348.54]  you
[2348.54 --> 2348.82]  can
[2348.82 --> 2349.36]  figure
[2349.36 --> 2349.66]  out
[2349.66 --> 2349.92]  who
[2349.92 --> 2350.10]  is
[2350.10 --> 2350.40]  speaking
[2350.40 --> 2350.66]  when
[2350.66 --> 2350.78]  and
[2350.78 --> 2350.96]  that's
[2350.96 --> 2351.04]  a
[2351.04 --> 2351.30]  task
[2351.30 --> 2351.74]  we call
[2351.74 --> 2352.64]  diarization
[2352.64 --> 2353.42]  so
[2353.42 --> 2353.70]  much
[2353.70 --> 2354.02]  new
[2354.02 --> 2355.00]  jargon
[2355.00 --> 2355.24]  it's
[2355.24 --> 2355.40]  always
[2355.40 --> 2355.66]  good
[2355.66 --> 2355.90]  to
[2355.90 --> 2356.40]  parse
[2356.40 --> 2356.60]  through
[2356.60 --> 2356.90]  that
[2356.90 --> 2358.30]  each
[2358.30 --> 2358.58]  field
[2358.58 --> 2358.76]  has
[2358.76 --> 2358.88]  its
[2358.88 --> 2359.16]  own
[2359.16 --> 2360.06]  terminology
[2360.06 --> 2360.76]  yeah
[2360.76 --> 2361.20]  exactly
[2361.20 --> 2362.18]  so
[2362.18 --> 2362.44]  I got
[2362.44 --> 2362.80]  a question
[2362.80 --> 2363.18]  for you
[2363.18 --> 2364.22]  I know
[2364.22 --> 2364.60]  that
[2364.60 --> 2365.90]  there are
[2365.90 --> 2366.36]  end-to-end
[2366.36 --> 2366.80]  approaches
[2366.80 --> 2367.20]  out there
[2367.20 --> 2367.64]  for speech
[2367.64 --> 2368.16]  recognition
[2368.16 --> 2368.78]  end-to-end
[2368.78 --> 2369.12]  approaches
[2369.12 --> 2369.66]  specifically
[2369.66 --> 2370.16]  without
[2370.16 --> 2370.56]  multiple
[2370.56 --> 2370.92]  models
[2370.92 --> 2371.42]  involved
[2371.42 --> 2372.16]  I'd like
[2372.16 --> 2372.42]  to know
[2372.42 --> 2373.16]  what the
[2373.16 --> 2373.48]  state
[2373.48 --> 2373.84]  of that
[2373.84 --> 2374.10]  where
[2374.10 --> 2374.32]  people
[2374.32 --> 2374.60]  that
[2374.60 --> 2375.10]  I think
[2375.10 --> 2375.98]  Google
[2375.98 --> 2376.40]  has had
[2376.40 --> 2376.58]  some
[2376.58 --> 2377.48]  speech-to-speech
[2377.48 --> 2377.88]  models
[2377.88 --> 2378.78]  they've talked
[2378.78 --> 2379.40]  about in the past
[2379.40 --> 2379.72]  and I'm sure
[2379.72 --> 2380.22]  there are others
[2380.22 --> 2380.78]  as well
[2380.78 --> 2381.52]  can you
[2381.52 --> 2382.68]  tell us
[2382.68 --> 2382.98]  what that
[2382.98 --> 2383.40]  looks like
[2383.40 --> 2383.64]  at this
[2383.64 --> 2383.86]  point
[2383.86 --> 2384.46]  yeah
[2384.46 --> 2384.74]  sure
[2384.74 --> 2385.08]  so the
[2385.08 --> 2385.42]  idea
[2385.42 --> 2385.86]  of
[2385.86 --> 2386.26]  an
[2386.26 --> 2386.60]  end-to-end
[2386.60 --> 2386.88]  model
[2386.88 --> 2387.38]  is that
[2387.38 --> 2388.10]  you have
[2388.10 --> 2389.24]  a single
[2390.06 --> 2390.38]  model
[2390.38 --> 2390.96]  it's usually
[2390.96 --> 2391.26]  a neural
[2391.26 --> 2391.56]  network
[2391.56 --> 2392.22]  because it's
[2392.22 --> 2392.84]  the most
[2392.84 --> 2393.22]  powerful
[2393.22 --> 2394.12]  model we
[2394.12 --> 2394.42]  have
[2394.42 --> 2395.54]  a single
[2395.54 --> 2395.76]  neural
[2395.76 --> 2396.06]  network
[2396.06 --> 2396.32]  model
[2396.32 --> 2396.60]  where you
[2396.60 --> 2397.10]  put audio
[2397.10 --> 2397.38]  in
[2397.38 --> 2397.90]  and you
[2397.90 --> 2398.32]  get words
[2398.32 --> 2398.64]  out
[2398.64 --> 2399.38]  you no need
[2399.38 --> 2399.88]  for a separate
[2399.88 --> 2400.52]  language model
[2400.52 --> 2401.06]  or a separate
[2401.06 --> 2401.66]  acoustic model
[2401.66 --> 2402.16]  or even a
[2402.16 --> 2402.74]  handcrafted
[2402.74 --> 2403.16]  lexicon
[2403.16 --> 2403.80]  neural network
[2403.80 --> 2404.26]  is going to
[2404.26 --> 2404.84]  model all of
[2404.84 --> 2405.72]  that internally
[2405.72 --> 2406.48]  which I think
[2406.48 --> 2406.76]  is a really
[2406.76 --> 2407.38]  neat idea
[2407.38 --> 2408.78]  because it
[2408.78 --> 2409.70]  just streamlines
[2409.70 --> 2410.34]  the whole process
[2410.34 --> 2411.14]  makes it much
[2411.14 --> 2411.94]  easier to
[2411.94 --> 2412.34]  comprehend
[2412.34 --> 2414.96]  and you're
[2414.96 --> 2415.36]  right that
[2415.36 --> 2415.84]  Google
[2415.84 --> 2416.76]  are one of
[2416.76 --> 2417.04]  the ones
[2417.04 --> 2417.32]  who've been
[2417.32 --> 2417.70]  pushing the
[2417.70 --> 2418.24]  boundaries in
[2418.24 --> 2418.66]  this area
[2418.66 --> 2419.12]  and it's a
[2419.12 --> 2419.70]  very big
[2419.70 --> 2419.98]  topic
[2420.06 --> 2421.06]  of research
[2421.06 --> 2422.28]  right now
[2422.28 --> 2422.74]  and I know
[2422.74 --> 2423.42]  that if you
[2423.42 --> 2423.86]  go to the
[2423.86 --> 2424.46]  speech recognition
[2424.46 --> 2425.04]  conferences
[2425.04 --> 2425.62]  a lot of
[2425.62 --> 2426.02]  the papers
[2426.02 --> 2426.42]  are looking
[2426.42 --> 2427.62]  into end-to-end
[2427.62 --> 2428.16]  methods for
[2428.16 --> 2428.78]  speech recognition
[2428.78 --> 2429.46]  right now
[2429.46 --> 2430.36]  one of the
[2430.36 --> 2431.40]  downsides of
[2431.40 --> 2432.52]  this approach
[2432.52 --> 2433.14]  I think is
[2433.14 --> 2433.46]  that you
[2433.46 --> 2434.44]  typically need
[2434.44 --> 2434.82]  quite a lot
[2434.82 --> 2435.30]  more data
[2435.30 --> 2436.32]  to be able
[2436.32 --> 2436.68]  to build
[2436.68 --> 2437.28]  them so
[2437.28 --> 2438.38]  if you
[2438.38 --> 2438.96]  are
[2438.96 --> 2440.38]  building a
[2440.38 --> 2440.88]  speech recognition
[2440.88 --> 2441.54]  model and
[2441.54 --> 2441.86]  then you
[2441.86 --> 2442.38]  quickly want
[2442.38 --> 2443.06]  to convert it
[2443.06 --> 2443.58]  to a new
[2443.58 --> 2444.20]  scenario
[2444.20 --> 2445.06]  and you need
[2445.06 --> 2445.40]  a lot of
[2445.40 --> 2445.96]  audio data
[2445.96 --> 2446.56]  to do that
[2446.56 --> 2447.14]  that can get
[2447.14 --> 2447.60]  a little bit
[2447.60 --> 2448.14]  expensive
[2448.14 --> 2449.24]  whereas
[2449.24 --> 2450.94]  if you've
[2450.94 --> 2451.56]  separated your
[2451.56 --> 2452.04]  models out
[2452.04 --> 2452.80]  into an
[2452.80 --> 2453.38]  acoustic model
[2453.38 --> 2453.60]  and a
[2453.60 --> 2454.20]  language model
[2454.20 --> 2455.12]  you can
[2455.12 --> 2455.74]  maybe take
[2455.74 --> 2456.32]  advantage of
[2456.32 --> 2457.30]  the fact that
[2457.30 --> 2458.24]  you need
[2458.24 --> 2459.00]  text data to
[2459.00 --> 2459.34]  train your
[2459.34 --> 2459.76]  language model
[2459.76 --> 2460.20]  you don't need
[2460.20 --> 2460.88]  audio and so
[2460.88 --> 2461.34]  you can do
[2461.34 --> 2462.64]  better that way
[2462.64 --> 2463.24]  and you can
[2463.24 --> 2464.10]  separate out
[2464.10 --> 2464.80]  whether you're
[2464.80 --> 2465.62]  adapting to
[2465.62 --> 2466.24]  the language
[2466.24 --> 2466.96]  that someone's
[2466.96 --> 2468.00]  using or to
[2468.00 --> 2468.80]  the acoustics of
[2468.80 --> 2469.42]  the situation
[2469.42 --> 2470.52]  and make the
[2470.52 --> 2471.14]  data collection
[2471.14 --> 2471.92]  a little easier
[2471.92 --> 2474.00]  and to my
[2474.00 --> 2474.50]  knowledge although
[2474.50 --> 2475.52]  this is rapidly
[2475.52 --> 2476.94]  changing and I
[2476.94 --> 2477.62]  can't claim to
[2477.62 --> 2478.14]  know the
[2478.14 --> 2479.32]  latest results
[2479.32 --> 2480.20]  but these
[2480.20 --> 2481.12]  models tend to
[2481.12 --> 2481.94]  be sort of
[2481.94 --> 2482.54]  either on a
[2482.54 --> 2483.12]  par or just
[2483.12 --> 2483.86]  slightly worse
[2483.86 --> 2484.26]  than our
[2484.26 --> 2485.40]  current what
[2485.40 --> 2485.94]  we call hybrid
[2485.94 --> 2486.68]  systems the
[2486.68 --> 2487.68]  acoustic model
[2487.68 --> 2488.24]  language model
[2488.24 --> 2489.30]  lexicon systems
[2489.30 --> 2490.98]  so I'm curious
[2490.98 --> 2492.16]  kind of piggybacking
[2492.16 --> 2492.64]  off of that
[2492.64 --> 2493.62]  question it seems
[2493.62 --> 2494.88]  like you know
[2494.88 --> 2496.58]  maybe in the
[2496.58 --> 2498.48]  so early 2010s
[2498.48 --> 2499.00]  like there was
[2499.00 --> 2500.04]  this image net
[2500.04 --> 2500.94]  moment for AI
[2500.94 --> 2501.86]  with computer
[2501.86 --> 2503.26]  vision now it
[2503.26 --> 2503.92]  seems like we're
[2503.92 --> 2504.74]  in a phase where
[2504.74 --> 2505.62]  like everything is
[2505.62 --> 2506.20]  about natural
[2506.20 --> 2507.04]  language processing
[2507.04 --> 2508.10]  it's kind of
[2508.10 --> 2508.84]  having a moment
[2508.84 --> 2510.00]  in terms of text
[2510.00 --> 2511.76]  and these large
[2511.76 --> 2512.44]  scale language
[2512.44 --> 2513.14]  models like
[2513.14 --> 2514.40]  bird and GPT-2
[2514.40 --> 2515.52]  and all of these
[2515.52 --> 2516.90]  things and I
[2516.90 --> 2517.96]  was curious like
[2517.96 --> 2518.66]  if you think
[2518.66 --> 2519.32]  there's going to
[2519.32 --> 2520.52]  be a similar
[2520.52 --> 2522.06]  sort of
[2522.06 --> 2523.70]  acceleration of
[2523.70 --> 2524.92]  speech and
[2524.92 --> 2526.40]  AI at some
[2526.40 --> 2527.58]  point and if
[2527.58 --> 2528.76]  so maybe what's
[2528.76 --> 2530.00]  holding that back
[2530.00 --> 2530.90]  now I was kind
[2530.90 --> 2531.28]  of trying to
[2531.28 --> 2531.98]  process this in
[2531.98 --> 2532.54]  my own mind
[2532.54 --> 2532.96]  and thinking
[2532.96 --> 2533.60]  oh well for
[2533.60 --> 2534.94]  text like
[2534.94 --> 2535.96]  we've got the
[2535.96 --> 2536.74]  whole internet
[2536.74 --> 2537.62]  of text that
[2537.62 --> 2538.32]  we can crawl
[2538.32 --> 2539.04]  and pull and
[2539.04 --> 2539.46]  maybe there's
[2539.46 --> 2540.20]  not as much
[2540.20 --> 2541.44]  speech data but
[2541.44 --> 2542.56]  there is there's
[2542.56 --> 2543.34]  a lot of audio
[2543.34 --> 2544.64]  data out there
[2544.64 --> 2545.56]  so I don't know
[2545.56 --> 2547.32]  is progress do
[2547.32 --> 2548.18]  you think could
[2548.18 --> 2549.06]  be accelerated by
[2549.06 --> 2549.66]  the availability
[2549.66 --> 2551.04]  of more data
[2551.04 --> 2552.06]  or is it the
[2552.06 --> 2553.14]  methodologies or
[2553.14 --> 2553.66]  what do you
[2553.66 --> 2553.90]  think?
[2554.70 --> 2555.52]  I think that
[2555.52 --> 2556.22]  the speech
[2556.22 --> 2557.22]  community have
[2557.22 --> 2558.06]  had an awful
[2558.06 --> 2559.14]  lot of shared
[2559.14 --> 2560.60]  tasks
[2560.60 --> 2561.70]  one of the
[2561.70 --> 2562.12]  you said about
[2562.12 --> 2562.64]  ImageNet and
[2562.64 --> 2563.20]  ImageNet is a
[2563.20 --> 2563.90]  large shared
[2563.90 --> 2564.80]  data set of
[2564.80 --> 2565.48]  images and
[2565.48 --> 2566.08]  there have been
[2566.08 --> 2566.70]  over the past
[2566.70 --> 2568.06]  years plenty of
[2568.06 --> 2568.96]  large shared
[2568.96 --> 2569.82]  speech recognition
[2569.82 --> 2571.02]  tasks that
[2571.02 --> 2572.08]  different research
[2572.08 --> 2572.56]  groups have
[2572.56 --> 2573.44]  contributed to
[2573.44 --> 2573.98]  and worked on
[2573.98 --> 2574.58]  so I think
[2574.58 --> 2575.70]  that in the
[2575.70 --> 2576.94]  way that text
[2576.94 --> 2577.72]  and images have
[2577.72 --> 2578.78]  relied on building
[2578.78 --> 2579.36]  up big data
[2579.36 --> 2580.00]  sets I think
[2580.00 --> 2580.46]  that already
[2580.46 --> 2581.90]  exists in the
[2581.90 --> 2582.44]  speech recognition
[2582.44 --> 2583.66]  community to
[2583.66 --> 2584.80]  some extent
[2584.80 --> 2586.36]  although maybe
[2586.36 --> 2587.58]  the size of
[2587.58 --> 2588.32]  the data sets
[2588.32 --> 2589.48]  is not as
[2589.48 --> 2590.00]  large as we
[2590.00 --> 2591.20]  need maybe the
[2591.20 --> 2592.38]  annotations are
[2592.38 --> 2592.88]  not quite there
[2592.88 --> 2593.66]  but certainly
[2593.66 --> 2594.94]  having data sets
[2594.94 --> 2595.60]  available that
[2595.60 --> 2596.54]  people can work
[2596.54 --> 2597.10]  on and benchmark
[2597.10 --> 2597.78]  against each
[2597.78 --> 2598.70]  other has been
[2598.70 --> 2599.86]  in place for a
[2599.86 --> 2600.80]  while and I
[2600.80 --> 2601.44]  think that's
[2601.44 --> 2602.20]  actually driven
[2602.20 --> 2603.10]  some of the
[2603.10 --> 2604.00]  improvements like
[2604.00 --> 2605.14]  I said from
[2605.14 --> 2606.18]  GMMs to
[2606.18 --> 2606.70]  neural networks
[2606.70 --> 2607.44]  over the past
[2607.44 --> 2608.30]  few years in
[2608.30 --> 2608.74]  that having
[2608.74 --> 2609.28]  these shared
[2609.28 --> 2610.50]  tasks has
[2610.50 --> 2611.08]  meant that people
[2611.08 --> 2612.50]  can easily build
[2612.50 --> 2613.30]  and test and
[2613.30 --> 2614.40]  compare different
[2614.40 --> 2614.98]  systems.
[2616.38 --> 2617.28]  Transcribing audio
[2617.28 --> 2618.98]  is a little more
[2618.98 --> 2619.64]  time consuming.
[2620.40 --> 2620.90]  One of the
[2620.90 --> 2622.04]  reasons that I
[2622.04 --> 2622.80]  think is so
[2622.80 --> 2623.66]  popular or has
[2623.66 --> 2625.00]  been so successful
[2625.00 --> 2625.74]  is that it can
[2625.74 --> 2626.36]  just take large
[2626.36 --> 2626.74]  amounts of
[2626.74 --> 2627.84]  unlabeled data
[2627.84 --> 2628.52]  to build from
[2628.52 --> 2630.34]  whereas transcribing
[2630.34 --> 2631.58]  all the speech
[2631.58 --> 2632.42]  recognition data you
[2632.42 --> 2632.80]  might need to
[2632.80 --> 2633.44]  build up a large
[2633.44 --> 2634.88]  data set is
[2634.88 --> 2635.64]  time consuming
[2635.64 --> 2636.14]  and there are
[2636.14 --> 2637.24]  efforts to do
[2637.24 --> 2637.78]  that to build
[2637.78 --> 2638.44]  up larger data
[2638.44 --> 2639.50]  sets and I
[2639.50 --> 2640.10]  know that one
[2640.10 --> 2640.74]  of the breakthroughs
[2640.74 --> 2641.50]  of ImageNet was
[2641.50 --> 2642.42]  having just large
[2642.42 --> 2642.94]  amounts of
[2642.94 --> 2643.98]  annotated images
[2643.98 --> 2645.02]  available for
[2645.02 --> 2645.76]  people to use.
[2646.48 --> 2646.92]  So like when
[2646.92 --> 2647.36]  we're talking
[2647.36 --> 2648.14]  about a speech
[2648.14 --> 2649.10]  recognition model
[2649.10 --> 2649.84]  whether it be
[2649.84 --> 2650.58]  the sort of
[2650.58 --> 2651.16]  hybrid approach
[2651.16 --> 2651.42]  that you're
[2651.42 --> 2652.12]  talking about
[2652.12 --> 2652.88]  or the end-to-end
[2652.88 --> 2654.10]  approach how
[2654.10 --> 2655.82]  much audio is
[2655.82 --> 2657.52]  needed to achieve
[2657.52 --> 2658.60]  something that's
[2658.60 --> 2659.72]  fairly useful
[2659.72 --> 2660.76]  at least on
[2660.76 --> 2661.40]  general
[2661.40 --> 2662.84]  conversational data
[2662.84 --> 2663.32]  maybe not
[2663.32 --> 2664.14]  domain-specific
[2664.14 --> 2664.58]  data?
[2665.10 --> 2665.32]  Yeah.
[2665.80 --> 2666.42]  We have speech
[2666.42 --> 2667.22]  recognition models
[2667.22 --> 2667.96]  acoustic models
[2667.96 --> 2668.48]  in various
[2668.48 --> 2669.20]  languages and one
[2669.20 --> 2669.76]  of the successful
[2669.76 --> 2670.50]  ways to build
[2670.50 --> 2670.84]  in a new
[2670.84 --> 2671.46]  language is to
[2671.46 --> 2672.06]  use transfer
[2672.06 --> 2672.40]  learning.
[2672.84 --> 2673.34]  So to take
[2673.34 --> 2673.78]  an English
[2673.78 --> 2674.50]  acoustic model
[2674.50 --> 2675.44]  take off the
[2675.44 --> 2675.96]  last layer
[2675.96 --> 2676.72]  put on a new
[2676.72 --> 2677.40]  last layer that
[2677.40 --> 2678.22]  represents say
[2678.22 --> 2679.46]  German and
[2679.46 --> 2680.76]  train the last
[2680.76 --> 2681.70]  layers using a
[2681.70 --> 2682.36]  smaller amount of
[2682.36 --> 2682.98]  German data.
[2683.44 --> 2683.92]  So we're in a
[2683.92 --> 2684.58]  really good position
[2684.58 --> 2685.68]  having good
[2685.68 --> 2686.50]  English acoustic
[2686.50 --> 2687.40]  models so we can
[2687.40 --> 2688.00]  use transfer
[2688.00 --> 2688.70]  learning to new
[2688.70 --> 2689.16]  languages.
[2690.34 --> 2691.16]  To do transfer
[2691.16 --> 2691.78]  learning to a
[2691.78 --> 2692.22]  new language
[2692.22 --> 2693.08]  obviously the more
[2693.08 --> 2693.72]  data you have
[2693.72 --> 2694.64]  the better but
[2694.64 --> 2695.50]  sort of the order
[2695.50 --> 2697.56]  of 100 hours up
[2697.56 --> 2698.38]  to 1000 hours of
[2698.38 --> 2699.02]  audio can get
[2699.02 --> 2699.78]  you really good
[2699.78 --> 2701.50]  starting points
[2701.50 --> 2702.10]  for your model
[2702.10 --> 2702.54]  that you want
[2702.54 --> 2702.96]  to build.
[2703.74 --> 2704.12]  So would
[2704.12 --> 2704.62]  automated
[2704.62 --> 2705.90]  annotation in
[2705.90 --> 2706.78]  some way kind
[2706.78 --> 2707.36]  of going back
[2707.36 --> 2708.34]  to the you
[2708.34 --> 2708.86]  know that like
[2708.86 --> 2709.34]  what does it
[2709.34 --> 2709.98]  take to get
[2709.98 --> 2710.68]  there as I've
[2710.68 --> 2711.24]  been listening to
[2711.24 --> 2711.72]  you and Daniel
[2711.72 --> 2712.56]  talk about that
[2712.56 --> 2713.46]  would have being
[2713.46 --> 2714.14]  able to get that
[2714.14 --> 2715.32]  large volume of
[2715.32 --> 2716.64]  data annotated
[2716.64 --> 2717.74]  and transcribed in
[2717.74 --> 2718.54]  an automated way
[2718.54 --> 2719.38]  so that it
[2719.38 --> 2719.98]  wasn't such a
[2719.98 --> 2720.58]  burden you think
[2720.58 --> 2720.92]  that would
[2720.92 --> 2722.16]  contribute significantly
[2722.16 --> 2722.80]  in that direction
[2722.80 --> 2723.86]  or or not?
[2724.76 --> 2725.24]  Yeah that's one
[2725.24 --> 2725.64]  of the other
[2725.64 --> 2726.62]  things that people
[2726.62 --> 2727.22]  actually do in
[2727.22 --> 2728.06]  practice as well
[2728.06 --> 2729.04]  is speech
[2729.04 --> 2729.48]  recognition
[2729.48 --> 2730.68]  especially if you
[2730.68 --> 2731.30]  have a commercial
[2731.30 --> 2732.12]  system that's up
[2732.12 --> 2732.54]  and running
[2732.54 --> 2733.96]  you can have a
[2733.96 --> 2734.70]  throughput of
[2734.70 --> 2736.56]  some thousands
[2736.56 --> 2737.44]  of hours of
[2737.44 --> 2738.52]  audio but maybe
[2738.52 --> 2738.98]  you only have
[2738.98 --> 2739.84]  capacity to
[2739.84 --> 2741.14]  transcribe 100
[2741.14 --> 2742.16]  hours of that
[2742.16 --> 2744.20]  so using that
[2744.20 --> 2745.38]  small amount of
[2745.38 --> 2746.62]  human transcribed
[2746.62 --> 2747.44]  data is going to
[2747.44 --> 2747.90]  improve your
[2747.90 --> 2749.08]  performance but
[2749.08 --> 2749.84]  then you can do
[2749.84 --> 2751.06]  sort of unsupervised
[2751.06 --> 2752.36]  or semi-supervised
[2752.36 --> 2753.56]  learning using that
[2753.56 --> 2755.30]  automatically transcribed
[2755.30 --> 2756.16]  data as well.
[2756.16 --> 2757.18]  it's not going to
[2757.18 --> 2758.10]  give you the same
[2758.10 --> 2758.90]  order of magnitude
[2758.90 --> 2759.84]  of gains as having
[2759.84 --> 2760.54]  the transcribed
[2760.54 --> 2761.72]  data but if you
[2761.72 --> 2762.42]  have more
[2762.42 --> 2763.60]  automatically transcribed
[2763.60 --> 2765.02]  data and then you
[2765.02 --> 2765.88]  use that to update
[2765.88 --> 2766.76]  your acoustic models
[2766.76 --> 2767.86]  that can also give
[2767.86 --> 2768.80]  you some good
[2768.80 --> 2769.22]  gains.
[2770.28 --> 2770.70]  Awesome well
[2770.70 --> 2771.58]  there's so much
[2771.58 --> 2773.32]  here to dig into
[2773.32 --> 2774.20]  further I know I
[2774.20 --> 2776.04]  want to after the
[2776.04 --> 2777.04]  conversation but I
[2777.04 --> 2777.68]  was wondering if we
[2777.68 --> 2778.88]  could just kind of
[2778.88 --> 2780.48]  close out by talking
[2780.48 --> 2781.40]  a little bit about
[2781.40 --> 2782.74]  you know what you're
[2782.74 --> 2783.74]  excited about in
[2783.74 --> 2784.70]  terms of the future
[2784.70 --> 2785.66]  of speech technology
[2785.66 --> 2786.92]  what what are you
[2786.92 --> 2787.82]  excited about
[2787.82 --> 2788.68]  implementing or
[2788.68 --> 2789.42]  developing yourself
[2789.42 --> 2790.34]  or what are you
[2790.34 --> 2791.16]  following what gets
[2791.16 --> 2792.62]  you excited in in
[2792.62 --> 2793.10]  this topic?
[2793.72 --> 2794.38]  What am I excited
[2794.38 --> 2794.64]  about?
[2794.76 --> 2795.92]  I am excited about
[2795.92 --> 2797.52]  the fact that we
[2797.52 --> 2798.58]  have worked out how
[2798.58 --> 2799.16]  to build this
[2799.16 --> 2799.94]  technology in English
[2799.94 --> 2800.84]  and how to scale it
[2800.84 --> 2801.76]  up and now that
[2801.76 --> 2802.72]  there's a huge
[2802.72 --> 2803.80]  opportunity to take
[2803.80 --> 2804.38]  it out to new
[2804.38 --> 2805.26]  languages and to
[2805.26 --> 2805.94]  build things that
[2805.94 --> 2806.64]  can be helpful to
[2806.64 --> 2807.46]  people all over the
[2807.46 --> 2808.52]  world particularly
[2808.52 --> 2809.54]  if you think about
[2809.54 --> 2810.58]  virtual assistants
[2810.58 --> 2811.20]  and putting it all
[2811.20 --> 2811.82]  together into some
[2811.82 --> 2812.28]  sort of voice
[2812.28 --> 2813.60]  interface I think
[2813.60 --> 2814.66]  that's a really nice
[2814.66 --> 2815.82]  neat way to interact
[2815.82 --> 2816.88]  with computers that
[2816.88 --> 2817.70]  can make technology
[2817.70 --> 2819.82]  accessible so there
[2819.82 --> 2820.78]  are huge parts of the
[2820.78 --> 2822.00]  world where people
[2822.00 --> 2823.86]  don't necessarily read
[2823.86 --> 2824.96]  and write in the same
[2824.96 --> 2825.78]  way that we do and
[2825.78 --> 2827.84]  therefore having this
[2827.84 --> 2828.68]  technology available to
[2828.68 --> 2829.96]  them is a great way to
[2829.96 --> 2831.22]  make things more level
[2831.22 --> 2833.14]  and I think it's a great
[2833.14 --> 2833.98]  way to make technology
[2833.98 --> 2835.20]  accessible to people who
[2835.20 --> 2836.58]  can't always just use a
[2836.58 --> 2838.90]  computer so I know I
[2838.90 --> 2839.80]  have elderly relatives
[2839.80 --> 2840.72]  who can't use a mouse or
[2840.72 --> 2841.60]  a keyboard very easily
[2841.60 --> 2842.58]  and for them voice
[2842.58 --> 2843.48]  technology has been
[2843.48 --> 2844.50]  really helpful to help
[2844.50 --> 2845.58]  them be able to do
[2845.58 --> 2846.06]  things that they
[2846.06 --> 2846.60]  wouldn't otherwise
[2846.60 --> 2847.58]  have been able to do
[2847.58 --> 2849.22]  and there is different
[2849.22 --> 2850.98]  work being done in
[2850.98 --> 2853.30]  making voice technology
[2853.30 --> 2855.24]  work for people who
[2855.24 --> 2857.34]  have maybe medical
[2857.34 --> 2858.24]  conditions which affect
[2858.24 --> 2860.10]  how they speak and so
[2860.10 --> 2862.06]  sort of helping these
[2862.06 --> 2864.02]  people be able to live
[2864.02 --> 2865.00]  more independent lives
[2865.00 --> 2866.76]  so I think there's a
[2866.76 --> 2868.56]  huge amount of need
[2868.56 --> 2870.08]  and desire to have this
[2870.08 --> 2871.22]  technology working for a
[2871.22 --> 2872.10]  broader range of people
[2872.10 --> 2873.28]  and I think that's what
[2873.28 --> 2873.90]  we'll see in the next
[2873.90 --> 2874.62]  few years is sort of
[2874.62 --> 2875.78]  widening access to this
[2875.78 --> 2876.20]  technology.
[2877.02 --> 2877.60]  Yeah that's super
[2877.60 --> 2878.88]  encouraging and glad you
[2878.88 --> 2879.48]  mentioned that.
[2879.64 --> 2880.94]  I'm excited to follow
[2880.94 --> 2882.08]  your work in the coming
[2882.08 --> 2883.08]  years and really
[2883.08 --> 2884.58]  appreciate you helping
[2884.58 --> 2885.38]  us learn about these
[2885.38 --> 2886.58]  technologies today and
[2886.58 --> 2888.06]  taking time to share
[2888.06 --> 2888.44]  with us.
[2888.52 --> 2889.18]  Thank you so much.
[2889.50 --> 2890.00]  My pleasure.
[2890.16 --> 2891.06]  It's been a great chat
[2891.06 --> 2891.38]  with you.
[2895.46 --> 2896.48]  Thank you for listening
[2896.48 --> 2897.56]  to this episode of
[2897.56 --> 2899.68]  Practical AI and a big
[2899.68 --> 2900.68]  thanks to Catherine
[2900.68 --> 2901.78]  Breslin for coming on
[2901.78 --> 2902.10]  the show.
[2902.54 --> 2903.42]  You can find everything
[2903.42 --> 2904.92]  Catherine is up to in
[2904.92 --> 2905.86]  the links in the show
[2905.86 --> 2906.12]  notes.
[2906.82 --> 2907.84]  This episode was hosted
[2907.84 --> 2908.94]  by Chris Benson and
[2908.94 --> 2909.70]  Daniel Whitenack.
[2909.86 --> 2910.72]  It was produced by
[2910.72 --> 2911.36]  Jared Santo.
[2911.68 --> 2912.22]  Hey that's me.
[2912.46 --> 2913.48]  Our music is brought to
[2913.48 --> 2914.30]  you by the mysterious
[2914.30 --> 2915.36]  Breakmaster Cylinder.
[2915.86 --> 2917.16]  We have awesome sponsors
[2917.16 --> 2917.92]  supporting the show.
[2918.14 --> 2919.34]  You know Fastly, Linode,
[2919.46 --> 2920.54]  and Robar have our back.
[2920.90 --> 2921.72]  If you and your
[2921.72 --> 2922.50]  organization would
[2922.50 --> 2923.32]  benefit from speaking
[2923.32 --> 2924.90]  directly into the ears of
[2924.90 --> 2925.96]  all the AI practitioners
[2925.96 --> 2926.88]  out there consider
[2926.88 --> 2927.76]  sponsoring the show.
[2927.76 --> 2929.48]  Podcast advertising is
[2929.48 --> 2930.58]  very effective especially
[2930.58 --> 2931.40]  when you're talking to
[2931.40 --> 2932.46]  the exact people you
[2932.46 --> 2932.82]  want to.
[2933.20 --> 2934.16]  Plus you get that warm
[2934.16 --> 2934.90]  fuzzy feeling of
[2934.90 --> 2935.64]  supporting something you
[2935.64 --> 2935.94]  love.
[2936.22 --> 2937.24]  Head to changelog.com
[2937.24 --> 2938.24]  slash sponsor to learn
[2938.24 --> 2938.54]  more.
[2938.76 --> 2939.40]  We'd love to work with
[2939.40 --> 2939.56]  you.
[2939.94 --> 2940.62]  That's all for now.
[2940.96 --> 2941.60]  We'll talk to you next
[2941.60 --> 2941.84]  week.
[2941.84 --> 2942.34]  Bye.
[2942.34 --> 2942.40]  Bye.
[2942.40 --> 2942.90]  Bye.
[2942.90 --> 2942.98]  Bye.
[2942.98 --> 2943.40]  Bye.
[2943.40 --> 2943.90]  Bye.
[2943.90 --> 2944.40]  Bye.
[2944.40 --> 2944.90]  Bye.
[2944.90 --> 2945.40]  Bye.
[2945.40 --> 2945.90]  Bye.
[2945.90 --> 2945.96]  Bye.
[2945.96 --> 2946.02]  Bye.
[2946.02 --> 2946.52]  Bye.
[2946.52 --> 2946.90]  Bye.
[2946.90 --> 2946.96]  Bye.
[2946.96 --> 2947.02]  Bye.
[2947.02 --> 2947.50]  Bye.
[2947.50 --> 2948.02]  Bye.
[2948.02 --> 2948.08]  Bye.
[2948.08 --> 2948.10]  Bye.
[2948.10 --> 2949.02]  Bye.
[2949.02 --> 2950.02]  Bye.
[2950.02 --> 2950.10]  Bye.
[2950.10 --> 2950.18]  Bye.
[2950.18 --> 2951.10]  Bye.
[2951.10 --> 2952.02]  Bye.
[2952.02 --> 2952.10]  Bye.
[2952.10 --> 2952.12]  Bye.
[2952.12 --> 2953.02]  Bye.
[2953.02 --> 2954.02]  Bye.
[2954.02 --> 2955.06]  Bye.
[2955.16 --> 2955.96]  Bye.
[2955.96 --> 2956.34]  Bye.
[2956.84 --> 2957.28]  Bye.
[2957.28 --> 2958.22]  Bye.
[2958.36 --> 2960.76]  Bye.
[2960.76 --> 2961.28]  Bye.
[2963.90 --> 2964.26]  Bye.
[2974.56 --> 2975.30]  Bye.
[2975.30 --> 2975.40]  Bye.
[2976.50 --> 2977.50]  Bye.
[2982.64 --> 2983.80]  Bye.
