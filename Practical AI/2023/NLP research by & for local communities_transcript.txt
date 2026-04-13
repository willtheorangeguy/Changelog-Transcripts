[0.00 --> 3.12]  I can relate to just, I thought that I knew the language,
[3.26 --> 6.14]  but then it feels like, okay, I actually don't know anything.
[6.52 --> 8.60]  And I don't know, there's been that interesting curve.
[8.92 --> 11.24]  It's called a curve of like David something,
[11.60 --> 12.94]  where it technically shows that, okay,
[13.30 --> 15.14]  when you think that you know something,
[15.56 --> 16.62]  you have high confidence,
[16.78 --> 18.88]  and that's actually when you actually don't know anything.
[19.22 --> 20.96]  But then when you start learning,
[21.08 --> 22.92]  and then you are adopting more of yourself,
[22.92 --> 25.84]  it's technically like that process of acknowledging
[25.84 --> 27.46]  and learning more things,
[27.46 --> 30.72]  and then like the curve goes up at some point again.
[41.18 --> 44.64]  Welcome to Practical AI, a weekly podcast
[44.64 --> 47.62]  making artificial intelligence practical, productive,
[47.88 --> 48.94]  and accessible to everyone.
[49.28 --> 50.96]  Subscribe now if you haven't already.
[50.96 --> 54.08]  Head to practicalai.fm for all the ways.
[54.46 --> 56.78]  Special thanks to our partners at Fastly
[56.78 --> 58.92]  for delivering our shows super fast
[58.92 --> 60.10]  to wherever you listen.
[60.40 --> 62.22]  Check them out at Fastly.com.
[62.56 --> 64.64]  And to our friends at fly.io.
[65.00 --> 67.54]  We deploy our app servers close to our users,
[67.76 --> 68.60]  and you can too.
[68.94 --> 70.82]  Learn more at fly.io.
[77.52 --> 81.22]  Welcome to another episode of the Practical AI podcast.
[81.64 --> 83.08]  This is Daniel Whitenack.
[83.08 --> 85.78]  I'm a data scientist with SIL International,
[86.36 --> 89.66]  and I'm at the EMNLP conference in Abu Dhabi,
[89.72 --> 92.96]  and I've got some old friends, some new friends here with me.
[93.04 --> 96.90]  A very exciting community show that we have for you today.
[97.22 --> 100.42]  Why don't I just have everyone just give a brief introduction
[100.42 --> 102.54]  of who they are and where they're coming from.
[103.10 --> 103.58]  Okay.
[103.72 --> 104.32]  Hi, everyone.
[104.46 --> 107.16]  My name is Andi Swapogula from South Africa.
[107.16 --> 111.30]  I work for the South African Center for Digital Language Resources
[111.30 --> 113.58]  as an Isikosa researcher.
[114.12 --> 117.90]  Isikosa being one of the 11 official languages spoken in South Africa.
[118.94 --> 119.72]  Hi, everyone.
[119.98 --> 122.28]  I am Rueida Mabuya, better known as Rue.
[122.62 --> 124.26]  I am also from South Africa.
[124.58 --> 128.10]  I work with Andi Swapogula at the South African Center for Digital Language Resources.
[128.64 --> 130.90]  I work as an Isi Zulu researcher.
[131.36 --> 133.94]  It's also part of the 11 official languages of the country.
[133.94 --> 134.72]  Thank you.
[135.36 --> 135.74]  Hi, all.
[135.78 --> 136.92]  My name is Jus Svenneker.
[137.18 --> 140.12]  I've been working as a data engineer for over 20 years.
[140.44 --> 142.92]  Recently, I wanted to switch towards data science,
[143.02 --> 144.78]  so I did a master's in that direction.
[145.46 --> 149.44]  For my thesis, I created a translation system for San Antongo,
[149.72 --> 154.44]  which is an English-based Creole language from Suriname,
[155.36 --> 158.56]  where my father is from, and I'm of mixed origin.
[158.76 --> 161.68]  So my mother is from the Netherlands, and my father is from Suriname,
[161.68 --> 163.40]  and I've been born and raised in the Netherlands.
[164.22 --> 165.00]  Okay, hi.
[165.10 --> 166.48]  My name is Bonaventure Dosu.
[166.66 --> 167.86]  I'm originally from Benin,
[168.34 --> 171.20]  but I'm also known as the citizen of the world,
[171.32 --> 172.50]  traveling around conferences.
[173.16 --> 178.42]  I am soon to be a PhD student at the Quebec AI Institute and also at Migio.
[178.42 --> 182.58]  And I work on low-resource languages, African low-resource languages.
[183.58 --> 188.30]  I mean, focusing on foreign-minded languages, but extending to other languages as well.
[188.72 --> 191.26]  And I'm also interested in machine learning for healthcare,
[191.80 --> 194.74]  like drug discovery, therapy, medical imaging, all those type of things.
[194.74 --> 195.66]  Great.
[195.82 --> 196.00]  Yeah.
[196.10 --> 196.62]  Thank you all.
[196.70 --> 198.62]  Thank you all for taking time to do this.
[198.68 --> 199.38]  This is so great.
[199.74 --> 204.20]  I mean, one of the really encouraging things about being in this room with you all is that,
[204.20 --> 207.76]  you know, so many talks here at EMNLP are great talks,
[207.76 --> 212.10]  but they'll say things like massively multilingual or like,
[212.10 --> 216.22]  this works for all languages or something like that.
[216.58 --> 221.02]  And that's definitely one perspective that's not totally accurate.
[221.02 --> 223.98]  So maybe if we start with Rue and Andy,
[224.40 --> 227.16]  what from your perspective are you're passionate about,
[227.36 --> 228.78]  what is the area that you're working?
[229.00 --> 233.32]  And maybe just highlight some of those things that maybe are another perspective
[233.32 --> 238.58]  of either linguistics or NLP that are important for people to understand
[238.58 --> 239.88]  in terms of the world's languages.
[240.40 --> 240.58]  Okay.
[240.66 --> 245.80]  So my passion is working on making sure that Isisulu is also a language of teaching and learning
[245.80 --> 247.56]  because currently in South Africa,
[247.56 --> 253.38]  English is the predominant language that is used in median governance and also in higher education.
[253.98 --> 261.12]  So what we're doing now is ensuring that our languages are also at a level where they are at par with English
[261.12 --> 267.20]  in terms of developing it in tools, in human language technologies, in machine learning, etc.
[267.50 --> 271.26]  So we also want to have that privilege, if I can put it like that,
[271.50 --> 275.78]  in ensuring that our languages are also more accessible even online.
[275.78 --> 279.60]  I've been working on looking at specific literature materials,
[279.72 --> 282.12]  but you find that I can't find those online.
[282.58 --> 287.72]  I literally have to scan the book if I want to do an analysis of a particular morphological structure
[287.72 --> 288.98]  that I'm working on currently.
[289.46 --> 293.70]  But then you find that all the Shakespearean books, for example, are readily available online.
[293.70 --> 300.18]  So that's my passion in ensuring that even African scholars can do research in their own languages
[300.18 --> 303.14]  with writers or authors that are like them,
[303.28 --> 306.92]  that write in the languages that we're interested in looking at,
[307.00 --> 309.94]  so that we also have those readily available
[309.94 --> 313.88]  and they can be used for research throughout for posterity.
[313.88 --> 318.72]  And I think for me also, for the institution that we are working with,
[318.78 --> 322.66]  working for, is that we're trying to also build a bridge,
[322.76 --> 326.42]  a gap between NLP practitioners and linguists,
[326.70 --> 331.48]  because it's always a matter of linguists are doing their projects on their own side
[331.48 --> 334.02]  and NLP practitioners are doing their own projects on the side.
[334.52 --> 336.50]  But I feel like if we can work together,
[336.74 --> 341.10]  because for you to understand the language that you're working on,
[341.10 --> 342.90]  you should collaborate with the linguists.
[343.00 --> 346.16]  And for us to understand how these language technologies work,
[346.24 --> 348.28]  we need to work with the NLP practitioners,
[348.66 --> 351.22]  because now in South Africa, NLP is not a big field.
[351.76 --> 355.16]  That's why our institutions are able to send us to such conferences
[355.16 --> 357.02]  so that we know what other people are doing,
[357.34 --> 359.06]  so that when we go back to our institutions
[359.06 --> 363.00]  and going back to actually assisting the universities in the country,
[363.30 --> 365.06]  we can impart that knowledge to them.
[365.36 --> 369.08]  Because currently, really, how we're doing research is still a bit traditional,
[369.08 --> 371.86]  and time is moving, technology is advancing,
[372.26 --> 373.42]  we don't want to be left behind.
[373.70 --> 376.48]  So I think our greatest passion is to make sure that our languages,
[377.08 --> 380.20]  because you keep saying that under-resourced, under-resourced, until what?
[380.30 --> 384.04]  Like we've been saying that our languages have been under-resourced for many years now,
[384.10 --> 388.12]  that now we have the opportunity to actually be sitting in a room like this
[388.12 --> 391.46]  with people who are actually doing the things that we've always heard of,
[391.64 --> 393.94]  but never knew were possible for our languages.
[393.94 --> 397.64]  So we're basically here to say, collaborate with us,
[397.72 --> 402.70]  assist us to get our languages to a level where there are languages of teaching and learning,
[403.12 --> 405.54]  and our data is also easily accessible.
[405.84 --> 408.48]  Because the other issue we have is accessibility of data.
[408.62 --> 410.42]  We don't have a lot of data in our languages,
[410.62 --> 412.96]  because we don't digitize the material that we have,
[413.16 --> 416.42]  but at least now we know what the possibilities are.
[416.94 --> 417.26]  So yeah.
[417.72 --> 418.50]  That's great.
[418.66 --> 421.42]  And just to follow up on one of the things that you mentioned,
[421.42 --> 425.90]  you mentioned this sort of idea of linguists and NLP people collaborating together,
[425.90 --> 430.92]  and you kind of mentioned the problem of sort of the availability of data,
[431.04 --> 432.64]  the scarcity of data.
[432.98 --> 437.94]  Are there any either misconceptions or things that you would like to highlight in terms of,
[438.24 --> 440.68]  you know, a lot of times what we see are these models,
[440.88 --> 446.28]  NLP models getting bigger and bigger and bigger and requiring more and more and more data to train,
[446.70 --> 449.46]  but the reality is for a lot of languages of the world,
[449.46 --> 454.26]  like you said, we either kind of have just a small amount of data,
[454.34 --> 455.44]  and it's not growing quickly.
[455.76 --> 460.92]  And, you know, those models are getting further and further away from being applicable in those scenarios.
[460.92 --> 463.42]  So anything you'd like to highlight or point out there?
[463.74 --> 467.66]  Yeah, I think, yeah, that's the issue that I don't really know who builds the models,
[467.86 --> 470.68]  because I wanted to refer specifically to the people who build the models,
[470.84 --> 472.32]  is that when they're building them,
[472.38 --> 477.32]  it's like they don't have the idea of the structures of the languages that they're building the models for.
[477.32 --> 480.96]  Because we also have in our repository certain models that we're using,
[481.10 --> 485.26]  but as soon as we train them with data from our languages,
[485.76 --> 488.40]  the accuracy levels are always very poor,
[488.72 --> 492.54]  because it's like the systems or the technologies do not understand that,
[492.82 --> 494.40]  for instance, my language is acclutinative.
[494.92 --> 497.82]  So when they're being built, hence the collaboration,
[498.02 --> 502.62]  it's like also take into consideration the languages that you're building the systems for.
[502.62 --> 506.62]  Because I feel like the systems are always built for specific structured languages.
[507.10 --> 511.24]  So that's always an issue, because now we do have access to the languages,
[511.68 --> 513.92]  but there's so little that we can do with them,
[513.98 --> 516.00]  because they don't understand the structures of our languages.
[516.48 --> 525.30]  Hence, again, I will emphasize the collaboration between NLP practitioners and linguists.
[525.30 --> 531.50]  Just to add on, a case and example is when looking at Google Translate, for example.
[531.64 --> 533.72]  It has improved quite a lot now,
[533.92 --> 539.86]  but previously you'd find that you'd want to translate something from my language into English or vice versa.
[540.04 --> 541.10]  The results were poor.
[541.58 --> 544.02]  But I think now because there's data that is available
[544.02 --> 547.80]  and they're doing something to ensure that there's an improvement in there,
[548.04 --> 550.34]  then you actually can see the positive results.
[550.34 --> 553.96]  But still, you find that in some other tools, even now,
[554.04 --> 556.92]  you still find that the accuracy levels are still very low.
[557.48 --> 562.66]  And as she said, it's the fact that when the tools are being built or created,
[563.16 --> 566.00]  it's like they don't have the language structure in mind.
[566.42 --> 569.28]  I feel like it's a matter of, okay, we've built this,
[569.36 --> 571.86]  so it should work for every other language, which is not the case.
[572.18 --> 573.64]  Each language has a unique structure.
[573.76 --> 575.38]  We have a unique morphology.
[575.74 --> 579.20]  Even though they're spoken maybe for, like the case in South Africa,
[579.20 --> 582.82]  we have nine indigenous languages, but the structure is not the same.
[583.16 --> 586.94]  So the people that actually build tools or create tools need to have that in mind
[586.94 --> 589.96]  and need to also work collaboratively with linguists,
[590.38 --> 595.44]  people that are trained in these languages to ensure that the structure is also represented
[595.44 --> 596.84]  when the tools are created.
[597.10 --> 599.38]  Yeah, that's such an amazing point.
[599.42 --> 600.34]  I'm glad you brought that up.
[600.44 --> 604.92]  I know even in our work, you know, encountering tools that are very popular,
[604.92 --> 608.82]  things like word segmenters or subword packages,
[608.82 --> 613.12]  where maybe it doesn't work quite right for like an Arabic script language
[613.12 --> 615.74]  or a right-to-left language or whatever it is,
[616.04 --> 618.94]  just because that was never envisioned, you know, from the beginning.
[619.18 --> 622.64]  On that same theme of kind of the types of languages
[622.64 --> 625.24]  that people are building language technology for,
[625.60 --> 628.24]  I wanted to ask you just about Creole languages.
[628.74 --> 632.62]  Maybe people listening to this podcast aren't that familiar with Creole languages
[632.62 --> 636.02]  or understand kind of how they're used around the world or what they are.
[636.12 --> 640.12]  Could you describe that a little bit and then also a little bit about your language
[640.12 --> 641.88]  and the language you've been working with?
[642.36 --> 642.72]  Yeah, sure.
[643.20 --> 647.40]  So a Creole language is basically a language that emerges in places
[647.40 --> 649.74]  where people of different cultural backgrounds come together.
[650.32 --> 653.22]  So in the case of Suriname, that is during slavery time,
[653.28 --> 657.76]  basically the 17th century, people were brought from Africa to Suriname.
[658.14 --> 661.10]  Also people from Europe came there to, you know, basically,
[661.10 --> 664.46]  you know what they did, all kinds of horrible stuff.
[665.20 --> 668.06]  But they needed a means to communicate amongst each other.
[668.24 --> 671.00]  And basically it's a language that has characteristics
[671.00 --> 674.24]  from the different languages that participate,
[674.42 --> 677.30]  from the people that participated in those communities,
[677.56 --> 684.32]  like English, Portuguese, Dutch, and some African languages.
[684.86 --> 687.44]  So it's basically a melting pot of languages.
[687.44 --> 689.98]  I don't know if I can put it that way,
[690.08 --> 693.18]  but usually it's grammatically a bit simpler
[693.18 --> 695.92]  and it's easier to learn a language.
[696.06 --> 696.84]  Let's put it that way.
[697.58 --> 700.20]  Yeah, and one of the things you were mentioning to me
[700.20 --> 702.26]  in our discussions even previous to this
[702.26 --> 705.16]  is that for some of those reasons that you've mentioned,
[705.38 --> 708.48]  you know, maybe Creole languages weren't and aren't
[708.48 --> 712.64]  always treated sort of at the same status of other languages.
[712.80 --> 713.78]  Could you speak to that a little bit?
[713.78 --> 715.96]  Yeah, definitely that's the case.
[716.76 --> 718.68]  So when I started this project,
[718.92 --> 721.36]  I found that this was really low resource.
[721.48 --> 724.02]  I was even amazed to find out that I couldn't find
[724.02 --> 727.42]  a single book or novel written in Sranangtongo.
[728.12 --> 730.62]  And that's because there's a lot of stigmatization
[730.62 --> 731.96]  going on with that language.
[732.14 --> 733.94]  So for instance, in school,
[734.94 --> 737.68]  so the surname is a former colony of the Netherlands.
[738.16 --> 740.34]  The first language still to this day,
[740.44 --> 742.34]  they're independent since 1975.
[742.34 --> 744.18]  The first language still is,
[744.32 --> 745.56]  and the official language is Dutch,
[745.88 --> 746.76]  spoken in Suriname.
[747.36 --> 749.76]  Sranangtongo is the second language.
[749.94 --> 752.48]  So there's basically no sources available in Sranangtongo.
[752.76 --> 755.88]  And it was for a long time forbidden
[755.88 --> 758.02]  to speak the language in schools, for instance.
[758.74 --> 762.10]  Also, parents often discourage their children
[762.10 --> 762.98]  to speak the language.
[763.32 --> 766.90]  So that stigmatization caused the low availability
[766.90 --> 768.72]  that we are dealing with now.
[768.72 --> 773.60]  Yeah, and describe a little bit about sort of your vision,
[773.74 --> 776.34]  I guess, for this project that you're working on
[776.34 --> 778.88]  and how it fits into maybe some of the needs
[778.88 --> 781.68]  of the language community that you're aware of about
[781.68 --> 783.84]  just from being part of that community
[783.84 --> 786.10]  and how that shaped your view of the project
[786.10 --> 788.52]  and what you're actually working on in your project.
[788.82 --> 789.02]  Yeah.
[789.02 --> 790.66]  So I have two sons.
[790.94 --> 792.94]  My youngest son asked me a couple of,
[793.10 --> 794.20]  last year he asked me
[794.20 --> 797.26]  why I hadn't taught him how to speak Sranangtongo.
[797.62 --> 799.54]  And that gave me actually the idea
[799.54 --> 800.84]  to build a translating system
[800.84 --> 803.68]  so that there's a lot of people living in the Netherlands
[803.68 --> 805.52]  with Suriname roots.
[806.10 --> 807.48]  Like I just explained,
[807.58 --> 809.74]  like in 1975, they became independent.
[810.14 --> 811.02]  So around that time,
[811.08 --> 814.78]  lots of people migrated from Suriname to the Netherlands.
[814.78 --> 818.72]  So this first generation is mostly fluent in Sranangtongo.
[819.54 --> 821.04]  I myself am a second generation.
[821.44 --> 822.46]  Before starting this project,
[822.56 --> 825.30]  I thought I was pretty okay in Sranangtongo,
[825.70 --> 827.14]  maybe 80, 90%.
[827.14 --> 830.46]  So I now would say maybe 50%, 60%
[830.46 --> 832.40]  after studying the language better.
[833.22 --> 835.02]  My son, who is a third generation,
[835.60 --> 837.92]  really wants to connect with his culture.
[838.36 --> 840.08]  So when we visited Suriname, for instance,
[840.18 --> 842.04]  and we're meeting with family members,
[842.54 --> 843.60]  he wants to know what they're saying.
[843.60 --> 847.44]  So I see this need within the Netherlands
[847.44 --> 850.02]  that people from the second and third generation,
[850.16 --> 851.36]  they want to connect with their culture,
[851.46 --> 852.44]  but they don't speak the language.
[852.58 --> 854.98]  So I hope that this translation system
[854.98 --> 858.76]  will support them in reconnecting with their culture.
[859.64 --> 860.34]  Awesome. Yeah.
[860.68 --> 864.46]  So I want to maybe ask Bona a couple of questions.
[864.82 --> 866.00]  I feel like I've been trying to get you
[866.00 --> 867.48]  on the podcast for a while now.
[867.58 --> 869.32]  So I'm glad you're actually here.
[869.76 --> 870.96]  I was actually already on.
[870.96 --> 873.96]  So, yeah, I wonder,
[874.18 --> 876.08]  one of the things that we were chatting about
[876.08 --> 880.04]  just before this is that people view Masakane
[880.04 --> 882.06]  and some of the things that are going on there
[882.06 --> 883.42]  with a lot of respect.
[883.66 --> 885.48]  And because of the momentum it has
[885.48 --> 887.02]  and how so much has been done,
[887.08 --> 889.14]  and I know you're part of some of the things
[889.14 --> 891.14]  that are being presented here with Masakane,
[891.52 --> 892.62]  could you describe maybe,
[892.78 --> 895.46]  we've actually mentioned Masakane on the podcast before,
[895.52 --> 896.96]  but for those that aren't familiar,
[897.46 --> 899.38]  could you describe what it is?
[899.38 --> 902.10]  Okay, I hope I will do justice to everyone.
[903.66 --> 907.88]  So I would describe Masakane
[907.88 --> 911.26]  as a grassroots organization,
[911.94 --> 915.40]  NLP movement that wants to build NLP
[915.40 --> 918.56]  on language technologies for African languages
[918.56 --> 919.68]  by Africans.
[919.90 --> 921.70]  And as everyone talked about,
[922.22 --> 924.28]  as everyone said earlier here,
[924.28 --> 928.26]  we need more people speaking those languages
[928.26 --> 931.86]  to be more involved in the building
[931.86 --> 933.94]  of those language technologies.
[934.38 --> 935.76]  Because someone, for instance,
[935.86 --> 937.00]  who works in a big company
[937.00 --> 937.46]  and be like,
[937.50 --> 939.26]  oh, okay, I found maybe this data on,
[939.70 --> 940.52]  let me say, Oscar,
[940.52 --> 942.70]  or like on like Flores
[942.70 --> 944.98]  or any data set that is said
[944.98 --> 947.60]  to be high quality and like multilingual.
[948.18 --> 950.54]  You know, he's just like trains a model on it
[950.54 --> 951.78]  and then assume that everything
[951.78 --> 953.52]  is supposed to be working, you know.
[953.96 --> 955.36]  But while at the beginning,
[955.68 --> 957.20]  those like language models,
[957.38 --> 958.58]  like SLMR, those type of things,
[958.64 --> 959.28]  have been created
[959.28 --> 961.96]  like for like high resource languages
[961.96 --> 963.04]  like what?
[963.16 --> 964.66]  Like English, Chinese, you know.
[965.00 --> 966.62]  Even like in those initial papers,
[966.74 --> 968.32]  you can see that the downstream tasks,
[968.50 --> 969.82]  they evaluated those tasks,
[969.96 --> 971.96]  those models on languages
[971.96 --> 973.76]  like French, English, Chinese,
[973.86 --> 974.48]  those type of things.
[974.96 --> 977.62]  So there's the assumption that,
[977.76 --> 979.96]  okay, we train those massive
[979.96 --> 981.40]  pre-trained language models
[981.40 --> 983.28]  and well, they can just like,
[983.36 --> 984.96]  we can just do like some transfer learning
[984.96 --> 986.18]  to low resource settings,
[986.36 --> 987.56]  which is not always true,
[987.56 --> 989.66]  which is one of the idea and paper
[989.66 --> 991.32]  that I presented here
[991.32 --> 992.66]  talking about active learning
[992.66 --> 994.42]  for language modeling.
[995.06 --> 996.72]  So as everyone has been saying,
[997.10 --> 997.96]  this is important
[997.96 --> 999.90]  and like that's the gap.
[1000.64 --> 1002.74]  Like also Andy said
[1002.74 --> 1004.10]  and like Ru said
[1004.10 --> 1005.58]  and just said
[1005.58 --> 1007.14]  that we need to like reduce
[1007.14 --> 1008.54]  that gap between linguists
[1008.54 --> 1011.46]  and like people who are like practitioners
[1011.46 --> 1012.66]  or NLP practitioners,
[1013.28 --> 1013.52]  you know.
[1013.68 --> 1015.24]  We need domain expertise,
[1015.46 --> 1016.22]  domain knowledge.
[1016.22 --> 1017.40]  And of course,
[1017.50 --> 1018.98]  like as an NLP researcher,
[1018.98 --> 1020.22]  I can have those,
[1020.56 --> 1022.24]  but language also have to come in
[1022.24 --> 1022.94]  to be able to say,
[1023.02 --> 1025.74]  okay, whatever this model is like predicting
[1025.74 --> 1026.88]  is like rubbish
[1026.88 --> 1029.18]  or like it makes sense.
[1029.66 --> 1032.92]  And I think as the most recent,
[1033.00 --> 1034.58]  like ongoing stuff,
[1034.70 --> 1035.84]  like on Twitter and all,
[1036.24 --> 1038.16]  models actually don't understand language.
[1038.56 --> 1040.24]  They understand data distribution.
[1040.40 --> 1041.32]  They understand words,
[1041.72 --> 1042.02]  you know.
[1042.02 --> 1043.90]  But then we need,
[1044.18 --> 1044.44]  again,
[1044.52 --> 1045.38]  as I'm emphasizing,
[1045.56 --> 1047.32]  we need that expert knowledge
[1047.32 --> 1048.90]  to be able to make sense
[1048.90 --> 1050.72]  of whatever those models produce
[1050.72 --> 1051.74]  to be able to say,
[1051.82 --> 1051.92]  okay,
[1051.96 --> 1053.56]  this is actually something useful.
[1054.58 --> 1055.38]  And yeah,
[1055.52 --> 1056.70]  that's what Master Canada
[1056.70 --> 1058.70]  is trying to like build
[1058.70 --> 1060.30]  a community of like NLP,
[1060.74 --> 1061.06]  not,
[1061.36 --> 1062.38]  I want to say NLP research,
[1062.50 --> 1063.64]  a community of like,
[1063.92 --> 1064.90]  let me say people,
[1065.46 --> 1066.00]  Africans,
[1066.00 --> 1067.92]  who are working
[1067.92 --> 1070.08]  on African technologies.
[1070.70 --> 1072.46]  So it includes linguists,
[1072.58 --> 1073.68]  it includes people
[1073.68 --> 1075.20]  who have theoretical,
[1075.48 --> 1075.96]  like NLP,
[1076.30 --> 1077.14]  mathematical background
[1077.14 --> 1078.16]  like me and like you.
[1078.36 --> 1079.70]  You're also part of the community.
[1080.06 --> 1081.72]  We have also like Sebastian,
[1082.10 --> 1082.50]  we have people
[1082.50 --> 1084.42]  who actually are not Africans,
[1084.52 --> 1086.30]  but who have like interest
[1086.30 --> 1087.66]  in like building,
[1088.00 --> 1089.56]  in like a company,
[1089.78 --> 1091.20]  like that effort.
[1091.44 --> 1092.12]  And that's like
[1092.12 --> 1093.66]  what the community is all about,
[1094.00 --> 1094.80]  putting forward
[1094.80 --> 1096.12]  and like representing,
[1096.68 --> 1097.96]  bringing more people like us
[1097.96 --> 1098.56]  at this,
[1098.70 --> 1099.86]  at this type of like
[1099.86 --> 1101.38]  big NLP conference,
[1101.88 --> 1102.20]  let me say,
[1102.26 --> 1102.76]  to the world
[1102.76 --> 1103.44]  or to the map
[1103.44 --> 1104.02]  or however,
[1104.20 --> 1105.10]  like increasing
[1105.10 --> 1105.88]  that representation
[1105.88 --> 1107.02]  and making sure
[1107.02 --> 1107.90]  like our language
[1107.90 --> 1108.46]  are preserved
[1108.46 --> 1109.38]  through those technologies,
[1109.60 --> 1111.50]  which I need to about today
[1111.50 --> 1112.72]  because somehow
[1112.72 --> 1114.46]  everything we're doing now
[1114.46 --> 1115.90]  is like based on needs
[1115.90 --> 1116.24]  somehow.
[1116.68 --> 1117.00]  So yeah.
[1117.74 --> 1117.96]  Yeah,
[1118.00 --> 1118.54]  that's great.
[1118.64 --> 1119.30]  And I can speak,
[1119.36 --> 1119.80]  as you mentioned,
[1119.90 --> 1121.34]  I've had the great privilege
[1121.34 --> 1123.26]  to interact with a lot of people
[1123.26 --> 1124.14]  from Masakane
[1124.14 --> 1125.00]  and, you know,
[1125.06 --> 1126.66]  on a few small areas,
[1126.76 --> 1128.88]  but even in those small things,
[1128.96 --> 1129.76]  I would just encourage
[1129.76 --> 1130.96]  researchers out there
[1130.96 --> 1131.96]  that have an interest
[1131.96 --> 1133.30]  in what's being discussed here
[1133.30 --> 1135.32]  to engage with those communities,
[1135.58 --> 1137.96]  engage with local language communities
[1137.96 --> 1139.86]  and speakers of those languages
[1139.86 --> 1141.52]  as you're building these technologies
[1141.52 --> 1142.24]  because you do,
[1142.64 --> 1142.86]  you know,
[1142.92 --> 1144.34]  I'm benefited so much
[1144.34 --> 1145.36]  by getting to interact
[1145.36 --> 1146.10]  with Masakane
[1146.10 --> 1147.12]  and the things that I learn
[1147.12 --> 1148.06]  and, you know,
[1148.10 --> 1149.90]  getting to have these sorts
[1149.90 --> 1150.48]  of discussions
[1150.48 --> 1151.74]  to have better awareness
[1151.74 --> 1152.32]  and understand
[1152.32 --> 1153.40]  how I can join
[1153.40 --> 1154.70]  and partner with people
[1154.70 --> 1155.64]  in the building
[1155.64 --> 1156.92]  of language technology.
[1157.52 --> 1159.10]  So as we kind of have
[1159.10 --> 1159.70]  gone around
[1159.70 --> 1161.06]  and talked about various things,
[1161.40 --> 1161.72]  I'm wondering
[1161.72 --> 1163.74]  if you all could maybe share,
[1163.94 --> 1165.14]  there's probably people,
[1165.38 --> 1166.40]  a lot of people listening
[1166.40 --> 1167.20]  to this podcast
[1167.20 --> 1169.16]  that are actually
[1169.16 --> 1170.68]  listening to it in English
[1170.68 --> 1170.92]  but,
[1171.02 --> 1172.54]  or maybe have a mother tongue,
[1172.70 --> 1173.06]  their English
[1173.06 --> 1173.96]  is their second language
[1173.96 --> 1174.64]  and they're thinking,
[1174.82 --> 1174.90]  hey,
[1174.96 --> 1176.76]  I wonder what I could do
[1176.76 --> 1178.36]  in my mother tongue
[1178.36 --> 1180.50]  in my first language.
[1180.50 --> 1182.52]  I know it's not well supported
[1182.52 --> 1184.30]  in language technology.
[1184.68 --> 1185.64]  Any encouragements
[1185.64 --> 1186.44]  from any of you
[1186.44 --> 1187.10]  of like,
[1187.18 --> 1188.66]  if you're a language speaker
[1188.66 --> 1190.26]  and you're wanting
[1190.26 --> 1192.86]  to sort of get into this somehow
[1192.86 --> 1194.90]  and kind of partner together,
[1195.08 --> 1195.94]  collaborate with others
[1195.94 --> 1196.94]  to help build,
[1197.02 --> 1197.74]  you know,
[1197.76 --> 1198.44]  more language,
[1198.80 --> 1199.42]  a higher level
[1199.42 --> 1200.58]  of digital language support
[1200.58 --> 1201.42]  for your language,
[1201.54 --> 1202.18]  what would you say?
[1202.90 --> 1203.30]  Yeah,
[1203.36 --> 1204.48]  if I can add to that.
[1204.72 --> 1206.54]  So what you usually see,
[1206.84 --> 1208.34]  you need a lot of data
[1208.34 --> 1210.08]  to train a good translation system
[1210.08 --> 1212.10]  or any NLP application
[1212.10 --> 1213.88]  and although there is not
[1213.88 --> 1215.04]  much data available
[1215.04 --> 1216.90]  in San Antonio in my case,
[1217.30 --> 1218.54]  the thing that you can usually find
[1218.54 --> 1219.94]  are Bible translations.
[1220.38 --> 1221.18]  So in my case,
[1221.26 --> 1223.96]  I used the Jehovah Witness 300 corpus
[1223.96 --> 1225.94]  which has a translation
[1225.94 --> 1227.78]  of 300,000 parallel sentences
[1227.78 --> 1230.04]  from Dutch into San Antonio
[1230.04 --> 1232.52]  and even in some smaller,
[1232.64 --> 1233.58]  even smaller languages
[1233.58 --> 1235.34]  spoken in Suriname
[1235.34 --> 1236.42]  like Saramakan
[1236.42 --> 1237.24]  and Aukan
[1237.24 --> 1238.42]  which is closer
[1238.42 --> 1240.46]  to some African languages.
[1241.22 --> 1242.40]  So that's a starting point.
[1242.56 --> 1242.98]  Of course,
[1243.18 --> 1244.42]  the idea would probably be
[1244.42 --> 1245.34]  that you create
[1245.34 --> 1247.54]  a general purpose translation system
[1247.54 --> 1248.50]  that was also my plan
[1248.50 --> 1250.28]  and still is my plan.
[1250.44 --> 1252.44]  So on top of that data,
[1252.70 --> 1253.48]  you would need
[1253.48 --> 1254.80]  some more data
[1254.80 --> 1256.44]  from a general domain
[1256.44 --> 1257.60]  from different domains
[1257.60 --> 1259.72]  next to the religious domain.
[1259.72 --> 1261.78]  So it was funny actually
[1261.78 --> 1263.10]  that's to see
[1263.10 --> 1264.50]  that Daniel from SIL,
[1264.74 --> 1265.80]  I found online,
[1265.90 --> 1266.78]  I found a dictionary
[1266.78 --> 1267.64]  in San Antonio
[1267.64 --> 1269.88]  and it contains
[1269.88 --> 1270.84]  a lot of words
[1270.84 --> 1272.02]  and with those words
[1272.02 --> 1273.28]  some example sentences.
[1273.80 --> 1275.74]  So before even knowing Daniel,
[1276.00 --> 1277.06]  I found his website
[1277.06 --> 1277.76]  of his company
[1277.76 --> 1279.70]  and was able to scrape
[1279.70 --> 1281.32]  3,000 sentences
[1281.32 --> 1282.36]  from there.
[1282.58 --> 1283.76]  Yeah, hopefully next time
[1283.76 --> 1284.74]  you don't have to scrape it.
[1284.96 --> 1285.80]  Shoot me an email.
[1286.18 --> 1287.00]  Yeah, indeed.
[1287.46 --> 1288.32]  Good to know you now.
[1288.32 --> 1289.94]  And on top of that,
[1290.02 --> 1290.62]  what I did is
[1290.62 --> 1292.44]  basically scan
[1292.44 --> 1294.58]  some smaller sources
[1294.58 --> 1296.60]  and OCR them basically
[1296.60 --> 1299.36]  and then manually align sentences.
[1299.88 --> 1301.26]  So it's a lot of manual work
[1301.26 --> 1302.88]  but I think also Bona
[1302.88 --> 1303.80]  has the same experience
[1303.80 --> 1304.96]  of doing a lot of manual work
[1304.96 --> 1306.94]  for his translation system.
[1307.48 --> 1309.14]  So now that I finally was able
[1309.14 --> 1310.60]  to get my first model
[1310.60 --> 1311.34]  up and running,
[1311.50 --> 1312.18]  I also built
[1312.18 --> 1314.00]  a translation system around it,
[1314.22 --> 1314.74]  a web app.
[1315.38 --> 1317.54]  So I'm now in the pilot phase
[1317.54 --> 1319.04]  where people are trying to,
[1319.20 --> 1319.84]  are trying,
[1319.94 --> 1320.84]  starting to use the,
[1321.22 --> 1322.40]  some speakers
[1322.40 --> 1324.00]  are using the system
[1324.00 --> 1327.10]  and evaluating the results.
[1327.80 --> 1328.58]  And so basically
[1328.58 --> 1329.72]  by just using it,
[1329.80 --> 1331.88]  they enter a sentence in Dutch,
[1332.02 --> 1334.30]  they get the Sranang translation back
[1334.30 --> 1335.76]  and they rate it.
[1336.10 --> 1337.18]  And if they don't think it's good,
[1337.30 --> 1338.74]  I ask them to enter
[1338.74 --> 1339.86]  a better translation
[1339.86 --> 1341.38]  and they submit it
[1341.38 --> 1342.86]  and I collect that data
[1342.86 --> 1343.62]  in my database.
[1343.84 --> 1345.24]  So I hope in this way
[1345.24 --> 1346.46]  to collect more data
[1346.46 --> 1348.38]  from a more modern use
[1348.38 --> 1349.06]  of a Sranang Tong
[1349.06 --> 1350.06]  instead of the religious one
[1350.06 --> 1351.44]  and collect enough data
[1351.44 --> 1353.16]  to eventually build a system
[1353.16 --> 1354.54]  that is more potent.
[1355.04 --> 1355.76]  Yeah, that's great.
[1355.84 --> 1357.08]  I think you highlight something
[1357.08 --> 1358.34]  that's definitely good
[1358.34 --> 1359.28]  for people to realize.
[1359.52 --> 1361.26]  This is also our colleague,
[1361.42 --> 1362.02]  Colin Leong
[1362.02 --> 1363.04]  from the University of Dayton.
[1363.18 --> 1364.34]  He told me about this,
[1364.42 --> 1365.70]  that his parents,
[1365.88 --> 1366.74]  who are speakers
[1366.74 --> 1368.66]  of a local language
[1368.66 --> 1369.76]  in East Asia,
[1369.76 --> 1370.86]  he asked them,
[1371.02 --> 1372.34]  hey, give me all of the data
[1372.34 --> 1373.68]  you have for your language
[1373.68 --> 1375.66]  and I'll try to build something.
[1375.90 --> 1377.42]  And he showed me the folder
[1377.42 --> 1379.90]  and it included MP3 files
[1379.90 --> 1381.38]  and Word documents
[1381.38 --> 1384.04]  and images and PDFs
[1384.04 --> 1384.88]  and all of these things.
[1385.02 --> 1385.94]  So I think, yeah,
[1385.98 --> 1386.86]  that's something important
[1386.86 --> 1387.94]  for people to realize
[1387.94 --> 1389.42]  that not everything
[1389.42 --> 1391.92]  has a nicely curated data set
[1391.92 --> 1392.86]  on Hugging Face
[1392.86 --> 1395.06]  and even being involved
[1395.06 --> 1395.96]  in some of that work
[1395.96 --> 1397.86]  to get that data put together
[1397.86 --> 1399.30]  is a hugely beneficial thing
[1399.76 --> 1400.64]  so, yeah,
[1400.70 --> 1401.24]  anyone else,
[1401.48 --> 1402.40]  things you would want to highlight
[1402.40 --> 1403.36]  for people out there
[1403.36 --> 1405.34]  wanting to start some of this?
[1405.94 --> 1408.04]  Before leaving the floor
[1408.04 --> 1408.86]  to the ladies,
[1409.42 --> 1410.60]  I would like to just like
[1410.60 --> 1412.58]  second what Jess said.
[1413.14 --> 1414.38]  I also had the same,
[1414.62 --> 1415.04]  let me say,
[1415.12 --> 1416.70]  struggle with phone
[1416.70 --> 1417.86]  because I started
[1417.86 --> 1420.46]  and nobody was working on phone.
[1420.80 --> 1422.10]  Nobody knew about the language
[1422.10 --> 1423.34]  and that was also something
[1423.34 --> 1424.20]  interesting and exciting,
[1424.36 --> 1424.52]  you know,
[1424.58 --> 1425.72]  like going into a direction
[1425.72 --> 1427.00]  where nobody's looking at
[1427.00 --> 1428.50]  and like unveiling it.
[1428.50 --> 1428.98]  So,
[1429.76 --> 1430.62]  not to show off,
[1430.68 --> 1431.76]  but a lot of people nowadays
[1431.76 --> 1433.60]  just like quote me
[1433.60 --> 1434.84]  as the phone guy,
[1434.96 --> 1435.16]  you know,
[1435.22 --> 1436.50]  like when someone is talking
[1436.50 --> 1437.52]  about phone or whatever
[1437.52 --> 1438.50]  and there's dub,
[1438.58 --> 1440.26]  they just tag me on like
[1440.26 --> 1441.14]  Twitter or whatever
[1441.14 --> 1442.12]  and yeah,
[1442.28 --> 1443.80]  I envision just to be the same
[1443.80 --> 1445.64]  like for Sranatongo
[1445.64 --> 1446.94]  and you know,
[1447.18 --> 1449.06]  the moral of the story
[1449.06 --> 1450.42]  is that you need
[1450.42 --> 1451.18]  to get started
[1451.18 --> 1452.76]  because there's always
[1452.76 --> 1454.06]  going to be a point
[1454.06 --> 1455.06]  where there's no data
[1455.06 --> 1456.18]  and someone has to do
[1456.18 --> 1457.10]  some little effort.
[1457.52 --> 1457.64]  You know,
[1457.70 --> 1458.04]  for instance,
[1458.16 --> 1459.12]  we have GW300
[1459.12 --> 1460.40]  but what if those people
[1460.40 --> 1461.18]  didn't do anything?
[1461.44 --> 1462.20]  We wouldn't have even,
[1462.72 --> 1463.86]  we would not even have
[1463.86 --> 1464.72]  a starting point,
[1465.22 --> 1465.50]  you know.
[1465.70 --> 1466.18]  So,
[1466.38 --> 1467.12]  I started as,
[1467.32 --> 1468.32]  with GW300
[1468.32 --> 1469.70]  and then I tried
[1469.70 --> 1470.76]  to like manually
[1470.76 --> 1472.34]  like scrape from like
[1472.34 --> 1473.26]  with my friends
[1473.26 --> 1475.12]  and all through Google Forms
[1475.12 --> 1476.06]  like created something
[1476.06 --> 1478.16]  like 25,000 sentences
[1478.16 --> 1479.70]  and then out of that
[1479.70 --> 1480.68]  then I've been able
[1480.68 --> 1481.80]  to bring some
[1481.80 --> 1482.64]  proof of concept
[1482.64 --> 1484.08]  and you know,
[1484.16 --> 1485.22]  like it grew up
[1485.22 --> 1485.86]  and like people
[1485.86 --> 1486.82]  are now more
[1486.82 --> 1488.18]  knowing about the language.
[1488.56 --> 1489.16]  Still is not,
[1489.46 --> 1489.70]  I mean,
[1489.88 --> 1491.14]  I build FFR Translate
[1491.14 --> 1491.86]  with Chris
[1491.86 --> 1493.12]  and people are using it,
[1493.20 --> 1493.78]  people are like
[1493.78 --> 1494.64]  very like
[1494.64 --> 1495.64]  sending feedback,
[1495.88 --> 1496.72]  they are like happy,
[1497.00 --> 1497.64]  it helps them,
[1497.78 --> 1498.14]  artists,
[1498.32 --> 1499.06]  people are like,
[1499.34 --> 1499.98]  they are more like
[1499.98 --> 1500.40]  awareness,
[1500.54 --> 1501.88]  people be willing
[1501.88 --> 1503.96]  to be more contributing,
[1504.12 --> 1505.02]  creating more content.
[1505.34 --> 1506.24]  It's not yet
[1506.24 --> 1507.06]  on something like
[1507.06 --> 1507.86]  a Google Translate
[1507.86 --> 1509.44]  or a centralized translation
[1509.44 --> 1510.48]  for those like
[1510.48 --> 1511.72]  African law resource language
[1511.72 --> 1512.58]  or law resource language
[1512.58 --> 1513.04]  in general
[1513.04 --> 1513.60]  but I hope
[1513.60 --> 1514.56]  that something's
[1514.56 --> 1515.56]  going to be coming.
[1516.02 --> 1516.14]  So,
[1516.24 --> 1517.12]  I'll just say just that.
[1517.28 --> 1517.44]  Yeah,
[1517.66 --> 1518.14]  honestly,
[1518.30 --> 1519.12]  like my name says,
[1519.70 --> 1521.00]  I like adventures
[1521.00 --> 1522.26]  and I like good adventures.
[1522.86 --> 1523.06]  So,
[1523.24 --> 1524.56]  I just like to go
[1524.56 --> 1526.14]  where nobody's focusing on
[1526.14 --> 1526.60]  and like
[1526.60 --> 1527.90]  unknown is exciting,
[1527.90 --> 1529.56]  like you bring something
[1529.56 --> 1530.76]  that people haven't been
[1530.76 --> 1531.78]  focusing on tonight.
[1532.34 --> 1533.18]  I don't think
[1533.18 --> 1534.64]  I would have had the same
[1534.64 --> 1535.52]  maybe impact
[1535.52 --> 1536.08]  if I,
[1536.18 --> 1536.46]  for instance,
[1536.56 --> 1537.72]  started with Evo
[1537.72 --> 1538.98]  because that project,
[1539.10 --> 1540.14]  the first FFR project
[1540.14 --> 1540.86]  that then like
[1540.86 --> 1541.68]  went on DPC
[1541.68 --> 1542.54]  or those type of things,
[1542.96 --> 1543.96]  we were dubting
[1543.96 --> 1544.82]  whether we should use
[1544.82 --> 1545.36]  FON or Evo.
[1545.78 --> 1545.98]  So,
[1546.12 --> 1546.42]  finally,
[1546.52 --> 1546.90]  Chris and I,
[1546.94 --> 1548.02]  we decided to go for FON
[1548.02 --> 1549.44]  because Evo has at least
[1549.44 --> 1550.62]  some effort done already
[1550.62 --> 1552.20]  but nobody heard about FON,
[1552.20 --> 1553.68]  nothing was on FON.
[1553.86 --> 1553.92]  Like,
[1554.42 --> 1554.80]  today,
[1555.04 --> 1557.28]  there are a lot of papers,
[1557.38 --> 1558.64]  people citing the work.
[1558.78 --> 1559.30]  It's been cited
[1559.30 --> 1560.78]  like in the paper
[1560.78 --> 1562.42]  that led to the extension
[1562.42 --> 1563.20]  of Google Translate
[1563.20 --> 1564.30]  to 2024
[1564.30 --> 1565.92]  or 20 more African languages
[1565.92 --> 1566.52]  or 24.
[1566.96 --> 1567.70]  It's been cited
[1567.70 --> 1568.78]  like no language
[1568.78 --> 1570.28]  left behind of Meta
[1570.28 --> 1571.00]  and,
[1571.10 --> 1571.24]  you know,
[1571.30 --> 1572.44]  like also being part
[1572.44 --> 1573.02]  of the Master Academy,
[1573.14 --> 1574.10]  you collaborate with people
[1574.10 --> 1574.78]  like Sebastian,
[1575.10 --> 1575.74]  with Julia,
[1576.24 --> 1577.16]  with Angela Fan
[1577.16 --> 1578.42]  who work on NLB,
[1578.58 --> 1578.84]  you know.
[1579.16 --> 1579.40]  So,
[1579.62 --> 1580.34]  just get started
[1580.34 --> 1581.08]  and like people
[1581.08 --> 1581.86]  will know about it
[1581.86 --> 1582.60]  and then I will just
[1582.60 --> 1583.28]  keep supporting.
[1583.82 --> 1584.02]  Yeah,
[1584.30 --> 1585.62]  if you don't have support,
[1586.00 --> 1587.96]  just be a self-supporter
[1587.96 --> 1589.08]  and at some point,
[1589.52 --> 1589.72]  like,
[1589.76 --> 1589.94]  you know,
[1590.02 --> 1590.82]  when people are seeing
[1590.82 --> 1591.38]  the effort,
[1591.56 --> 1592.18]  they will definitely
[1592.18 --> 1592.76]  then join
[1592.76 --> 1593.84]  and then it will like
[1593.84 --> 1595.16]  take it up from there.
[1595.82 --> 1596.04]  Yeah,
[1596.26 --> 1596.84]  Rue or Andy,
[1596.98 --> 1597.82]  anything to add?
[1598.60 --> 1599.56]  I also share
[1599.56 --> 1600.34]  the same sentiments
[1600.34 --> 1601.50]  with the case
[1601.50 --> 1602.20]  for AC Zulu.
[1602.76 --> 1603.70]  You find that
[1603.70 --> 1605.80]  people should just start
[1605.80 --> 1606.90]  even though it's difficult
[1606.90 --> 1608.16]  because data
[1608.16 --> 1608.96]  is available
[1608.96 --> 1610.26]  but people are not
[1610.26 --> 1610.94]  coming forth.
[1611.04 --> 1611.52]  They're not wanting
[1611.52 --> 1612.66]  to share their data.
[1613.18 --> 1613.78]  You find that,
[1613.90 --> 1614.04]  okay,
[1614.12 --> 1614.72]  you collect
[1614.72 --> 1615.72]  or you do whatever
[1615.72 --> 1616.10]  with it
[1616.10 --> 1616.62]  and then you just
[1616.62 --> 1617.52]  keep it to yourself
[1617.52 --> 1618.98]  and then that now
[1618.98 --> 1620.10]  hinders the progress
[1620.10 --> 1620.66]  of the language
[1620.66 --> 1621.34]  or the development
[1621.34 --> 1621.90]  of the language
[1621.90 --> 1622.48]  in itself.
[1622.80 --> 1623.34]  I think it would be
[1623.34 --> 1623.98]  a great idea
[1623.98 --> 1624.80]  if people get
[1624.80 --> 1625.30]  the understanding
[1625.30 --> 1626.46]  that when you
[1626.46 --> 1627.58]  are allowing your data
[1627.58 --> 1628.34]  to be accessible
[1628.34 --> 1630.24]  or make it open resource,
[1630.36 --> 1630.64]  you're not,
[1631.56 --> 1632.40]  it's not a matter of
[1632.40 --> 1633.36]  I want to steal your idea,
[1633.52 --> 1634.50]  I can do something different
[1634.50 --> 1635.18]  than what you did
[1635.18 --> 1635.78]  with the data
[1635.78 --> 1637.20]  and also just ensuring
[1637.20 --> 1638.76]  that more researchers
[1638.76 --> 1639.86]  have accessibility
[1639.86 --> 1640.58]  to it so that
[1640.58 --> 1641.18]  they can use it
[1641.18 --> 1641.52]  for whatever
[1641.52 --> 1642.04]  that they want
[1642.04 --> 1642.72]  to use it for.
[1643.12 --> 1643.84]  The only issue
[1643.84 --> 1644.38]  that I have
[1644.38 --> 1645.14]  with getting sure
[1645.14 --> 1645.70]  that the data
[1645.70 --> 1646.30]  is more,
[1646.66 --> 1647.20]  is collected
[1647.20 --> 1648.68]  in a general sense
[1648.68 --> 1649.16]  because you find
[1649.16 --> 1650.44]  that newspaper articles
[1650.44 --> 1651.30]  are very much
[1651.30 --> 1652.06]  easily accessible
[1652.06 --> 1653.32]  but in the case
[1653.32 --> 1653.78]  for AC Zulu
[1653.78 --> 1654.62]  you find that novels
[1654.62 --> 1655.28]  you can't,
[1655.32 --> 1656.14]  you need to actually
[1656.14 --> 1657.12]  do OCRing
[1657.12 --> 1658.36]  and do the scans
[1658.36 --> 1658.90]  by hand
[1658.90 --> 1659.56]  which takes a lot
[1659.56 --> 1660.04]  of time.
[1660.50 --> 1661.56]  So if we can
[1661.56 --> 1662.04]  find something
[1662.04 --> 1662.66]  that would work,
[1662.96 --> 1663.52]  that would be much
[1663.52 --> 1663.94]  quicker,
[1664.58 --> 1665.36]  we'd be grateful
[1665.36 --> 1666.00]  for it
[1666.00 --> 1667.04]  so that at least
[1667.04 --> 1667.80]  we can get it
[1667.80 --> 1668.88]  to be at the level
[1668.88 --> 1669.36]  where we have
[1669.36 --> 1670.20]  enough data
[1670.20 --> 1671.80]  to train models
[1671.80 --> 1673.02]  and train tools
[1673.02 --> 1673.96]  with it.
[1674.56 --> 1674.96]  Yeah,
[1675.02 --> 1675.92]  what I would add
[1675.92 --> 1677.16]  is that language
[1677.16 --> 1677.62]  preservation
[1677.62 --> 1678.64]  is very important.
[1679.00 --> 1679.92]  Let's find ways
[1679.92 --> 1681.16]  in which we can
[1681.16 --> 1682.58]  preserve our languages
[1682.58 --> 1683.06]  in the sense
[1683.06 --> 1683.88]  that they do not
[1683.88 --> 1684.40]  go extinct.
[1684.84 --> 1685.28]  For instance,
[1685.36 --> 1685.84]  what we're doing
[1685.84 --> 1686.66]  now in South Africa
[1686.66 --> 1687.54]  is that because
[1687.54 --> 1688.68]  most of our languages
[1688.68 --> 1689.80]  have dialects
[1689.80 --> 1690.68]  and dialects,
[1690.94 --> 1691.48]  because they're not
[1691.48 --> 1692.24]  standard languages,
[1692.44 --> 1693.96]  they're not documented.
[1693.96 --> 1695.44]  So one of the projects
[1695.44 --> 1696.12]  that people can do
[1696.12 --> 1696.82]  if they're in similar
[1696.82 --> 1697.78]  situations is where
[1697.78 --> 1698.98]  you collect speech data
[1698.98 --> 1700.08]  of those dialects
[1700.08 --> 1700.68]  so that they can be
[1700.68 --> 1701.60]  accessible somewhere
[1701.60 --> 1702.68]  so that if in the
[1702.68 --> 1703.32]  next 10 years
[1703.32 --> 1704.36]  a dialect is not spoken,
[1704.56 --> 1705.80]  there is data available
[1705.80 --> 1706.86]  for people to hear
[1706.86 --> 1707.36]  that, okay,
[1707.50 --> 1707.98]  there was actually
[1707.98 --> 1708.66]  once a language
[1708.66 --> 1709.24]  like the spoken
[1709.24 --> 1710.10]  in a certain area.
[1710.80 --> 1711.24]  And yeah,
[1711.28 --> 1712.08]  I think more than anything
[1712.08 --> 1712.98]  it's just preserving
[1712.98 --> 1713.58]  the language,
[1713.76 --> 1714.76]  creating more data
[1714.76 --> 1715.98]  because now
[1715.98 --> 1717.46]  for this Mazakana project
[1717.46 --> 1718.28]  we're able to
[1718.28 --> 1719.20]  access our data
[1719.20 --> 1720.80]  via online newspapers.
[1721.32 --> 1721.90]  So if people can
[1721.90 --> 1722.92]  also digitize the work
[1722.92 --> 1723.54]  that they have
[1723.54 --> 1724.76]  because it is true
[1724.76 --> 1725.62]  that it's so difficult
[1725.62 --> 1726.42]  to find material
[1726.42 --> 1728.14]  because it's not being
[1728.14 --> 1730.02]  not digitized,
[1730.36 --> 1731.16]  published, yes.
[1731.48 --> 1732.40]  Some books are out
[1732.40 --> 1733.50]  of publication now
[1733.50 --> 1734.90]  so for that to not happen
[1734.90 --> 1735.98]  we must digitize
[1735.98 --> 1737.32]  our literature,
[1737.58 --> 1738.00]  our text,
[1738.12 --> 1738.80]  and everything else
[1738.80 --> 1739.80]  so that it can be
[1739.80 --> 1740.50]  easily accessible
[1740.50 --> 1741.38]  so that we can actually
[1741.38 --> 1742.38]  run such projects.
[1742.84 --> 1742.90]  Yeah.
[1743.66 --> 1744.14]  Great.
[1744.52 --> 1744.86]  Well,
[1744.98 --> 1746.34]  I really appreciate
[1746.34 --> 1747.22]  all of you
[1747.22 --> 1748.84]  getting to have a chance
[1748.84 --> 1749.90]  to join us here.
[1749.98 --> 1751.08]  I know it's a busy conference
[1751.08 --> 1751.80]  and there's a lot
[1751.80 --> 1752.46]  of great things
[1752.46 --> 1752.90]  to look at
[1752.90 --> 1753.70]  but I'm so happy
[1753.70 --> 1754.40]  that we get to
[1754.40 --> 1755.62]  bring this conversation
[1755.62 --> 1757.28]  to a wider audience
[1757.28 --> 1758.26]  and maybe,
[1758.50 --> 1759.32]  you know,
[1759.38 --> 1760.34]  if anyone wants
[1760.34 --> 1761.48]  to leave with
[1761.48 --> 1762.22]  a greeting
[1762.22 --> 1763.30]  in their language,
[1763.48 --> 1764.08]  please go ahead.
[1764.88 --> 1766.46]  So before finishing,
[1766.66 --> 1767.68]  I would do a little bit
[1767.68 --> 1769.20]  of like promotion.
[1769.62 --> 1770.26]  Yeah, please do.
[1770.68 --> 1772.06]  Regarding the language
[1772.06 --> 1773.10]  discoverability
[1773.10 --> 1774.18]  and all those type of things,
[1774.86 --> 1775.40]  Chris and I
[1775.40 --> 1776.08]  have been working
[1776.08 --> 1776.70]  on Lanfrica
[1776.70 --> 1778.70]  which is a,
[1779.10 --> 1779.70]  let's say,
[1779.82 --> 1780.34]  innovation,
[1780.52 --> 1781.10]  an idea
[1781.10 --> 1783.24]  of like putting out
[1783.24 --> 1784.94]  those like language resources
[1784.94 --> 1786.88]  for those African language resources
[1786.88 --> 1788.96]  that are not discoverable
[1788.96 --> 1789.48]  on the internet
[1789.48 --> 1790.66]  so you can access
[1790.66 --> 1792.34]  like research papers,
[1792.52 --> 1793.82]  you can access data sets,
[1793.90 --> 1794.74]  you can access tools
[1794.74 --> 1795.78]  like keyboard
[1795.78 --> 1796.74]  or those type of things
[1796.74 --> 1797.36]  and anything
[1797.36 --> 1798.60]  like dictionaries,
[1799.04 --> 1799.38]  anything.
[1799.94 --> 1800.66]  Even sometimes
[1800.66 --> 1801.62]  like YouTube videos
[1801.62 --> 1802.42]  so people are doing
[1802.42 --> 1802.94]  great things
[1802.94 --> 1804.18]  like educating people
[1804.18 --> 1805.26]  for instance
[1805.26 --> 1806.62]  in Afra
[1806.62 --> 1807.70]  or those type of languages,
[1807.82 --> 1808.78]  languages I've never heard
[1808.78 --> 1809.46]  about before
[1809.46 --> 1810.36]  and they are doing
[1810.36 --> 1810.92]  great effort
[1810.92 --> 1811.82]  but then it's like
[1811.82 --> 1812.32]  on YouTube
[1812.32 --> 1813.40]  and like nobody knows
[1813.40 --> 1814.94]  so on Lanfrica
[1814.94 --> 1815.84]  they can easily
[1815.84 --> 1816.54]  kind of access
[1816.54 --> 1817.26]  those resources
[1817.26 --> 1818.80]  and if you also
[1818.80 --> 1819.58]  have a work
[1819.58 --> 1820.96]  like on mainly
[1820.96 --> 1822.76]  on African languages
[1822.76 --> 1823.42]  but if it's
[1823.42 --> 1824.58]  on low resource languages
[1824.58 --> 1825.50]  we have for instance
[1825.50 --> 1826.52]  the Lanfrica talk
[1826.52 --> 1827.58]  where people
[1827.58 --> 1828.80]  from all around the world
[1828.80 --> 1829.92]  we got like people
[1829.92 --> 1831.52]  from like CMU,
[1831.66 --> 1832.12]  we got people
[1832.12 --> 1833.00]  from Google Research,
[1833.20 --> 1833.68]  we got people
[1833.68 --> 1835.24]  from like UCL
[1835.24 --> 1836.44]  people from around the world
[1836.44 --> 1836.84]  students,
[1837.10 --> 1837.56]  researchers,
[1837.82 --> 1838.24]  anybody
[1838.24 --> 1839.56]  who has been working
[1839.56 --> 1841.32]  who has been working
[1841.32 --> 1842.12]  and passionate about
[1842.12 --> 1843.16]  like low resource
[1843.16 --> 1844.30]  languages,
[1844.50 --> 1846.10]  NLP technologies
[1846.10 --> 1847.74]  then to like come
[1847.74 --> 1849.20]  to and like
[1849.20 --> 1850.34]  give a talk
[1850.34 --> 1851.42]  for like people
[1851.42 --> 1852.40]  to know more
[1852.40 --> 1853.46]  about what they've been doing
[1853.46 --> 1855.00]  so it's pretty simple
[1855.00 --> 1855.94]  you just go on like
[1855.94 --> 1862.66]  www.lanfrica.com
[1862.66 --> 1863.64]  and then like
[1863.64 --> 1864.46]  you can find out
[1864.46 --> 1865.76]  the information
[1865.76 --> 1867.36]  about like languages
[1867.36 --> 1868.68]  and also how to assess
[1868.68 --> 1870.00]  the or like
[1870.00 --> 1870.72]  how to book
[1870.72 --> 1871.40]  for a meeting
[1871.40 --> 1872.64]  for the Lanfrica talk
[1872.64 --> 1875.80]  so that being said
[1875.80 --> 1876.68]  like something
[1876.68 --> 1878.28]  basic in my language
[1878.28 --> 1878.84]  would be
[1878.84 --> 1880.24]  Enachenwekaka Daniel
[1880.24 --> 1881.28]  that means
[1881.28 --> 1882.14]  thank you so much
[1882.14 --> 1883.06]  Daniel for
[1883.06 --> 1884.26]  oh well
[1884.26 --> 1886.00]  Enachenwekaka Daniel
[1886.00 --> 1886.96]  well I don't know
[1886.96 --> 1887.92]  about the form
[1887.92 --> 1889.02]  for this invitation
[1889.02 --> 1889.50]  you know
[1889.50 --> 1890.40]  and that's something
[1890.40 --> 1891.50]  like I can relate
[1891.50 --> 1891.98]  to just
[1891.98 --> 1893.00]  I thought that
[1893.00 --> 1893.96]  I knew the language
[1893.96 --> 1895.18]  but then it feels like
[1895.18 --> 1895.52]  okay
[1895.52 --> 1896.78]  I actually don't know
[1896.78 --> 1897.14]  anything
[1897.14 --> 1897.96]  and I don't know
[1897.96 --> 1898.40]  they've been
[1898.40 --> 1899.60]  that interesting curve
[1899.60 --> 1901.00]  it's called a curve
[1901.00 --> 1902.24]  of like David something
[1902.24 --> 1903.14]  where it technically
[1903.14 --> 1903.72]  showed that
[1903.72 --> 1903.96]  okay
[1903.96 --> 1905.56]  when you think
[1905.56 --> 1906.42]  that you know something
[1906.42 --> 1907.88]  you have high confidence
[1907.88 --> 1908.64]  and that's actually
[1908.64 --> 1909.42]  when you actually
[1909.42 --> 1910.18]  don't know anything
[1910.18 --> 1911.26]  but then when you
[1911.26 --> 1912.24]  start learning
[1912.24 --> 1912.86]  and then you are
[1912.86 --> 1914.20]  adopting more of yourself
[1914.20 --> 1915.00]  it's technically
[1915.00 --> 1916.32]  like that process
[1916.32 --> 1917.10]  of acknowledging
[1917.10 --> 1918.16]  and like learning
[1918.16 --> 1918.74]  more things
[1918.74 --> 1919.30]  and then like
[1919.30 --> 1920.02]  the curve
[1920.02 --> 1921.02]  like goes up
[1921.02 --> 1921.96]  at some point again
[1921.96 --> 1923.08]  so yeah
[1923.08 --> 1923.68]  I'll just stick
[1923.68 --> 1925.04]  to Enachenwekaka Daniel
[1925.04 --> 1926.36]  and I will let
[1926.36 --> 1927.54]  just Andy
[1927.54 --> 1929.00]  and Ro
[1929.00 --> 1930.02]  finish
[1930.02 --> 1931.08]  in the languages
[1931.08 --> 1932.44]  thank you so much
[1932.44 --> 1933.24]  I'd also just like
[1933.24 --> 1934.14]  to maybe just promote
[1934.14 --> 1935.46]  also the organization
[1935.46 --> 1936.18]  we're coming from
[1936.18 --> 1937.34]  the South African Center
[1937.34 --> 1938.58]  for Digital Language Resources
[1938.58 --> 1939.66]  any researchers
[1939.66 --> 1940.30]  that are working
[1940.30 --> 1941.04]  in any of the
[1941.04 --> 1942.26]  South African languages
[1942.26 --> 1943.24]  they can check us out
[1943.24 --> 1945.26]  at sadila.org.za
[1945.26 --> 1946.28]  a parting word
[1946.28 --> 1946.82]  that I can say
[1946.82 --> 1947.36]  in my language
[1947.36 --> 1947.76]  is
[1947.76 --> 1951.56]  which means
[1951.56 --> 1952.36]  thank you so much
[1952.36 --> 1954.16]  for listening to me
[1954.16 --> 1955.56]  now I don't know
[1955.56 --> 1956.28]  what I'm going to say
[1956.28 --> 1957.08]  but I'm going to keep it
[1957.08 --> 1957.68]  very short
[1957.68 --> 1960.20]  which means
[1960.20 --> 1961.60]  thank you very much
[1961.60 --> 1962.48]  yeah before
[1962.48 --> 1963.18]  finishing
[1963.18 --> 1964.38]  I must express
[1964.38 --> 1964.88]  that I'm actually
[1964.88 --> 1965.40]  a bit jealous
[1965.40 --> 1966.72]  of the Mashakana community
[1966.72 --> 1971.76]  free of charge
[1971.76 --> 1972.26]  okay
[1972.26 --> 1973.28]  that's
[1973.28 --> 1975.06]  good to know
[1975.06 --> 1975.72]  thank you very much
[1975.72 --> 1976.44]  for the invitation
[1976.44 --> 1977.40]  also
[1977.40 --> 1978.44]  I wanted to add
[1978.44 --> 1978.90]  that maybe
[1978.90 --> 1979.48]  if there's
[1979.48 --> 1980.56]  other people
[1980.56 --> 1980.94]  listening
[1980.94 --> 1981.90]  who are into
[1981.90 --> 1982.68]  Creole languages
[1982.68 --> 1984.78]  give me a shout out
[1984.78 --> 1985.56]  my name is
[1985.56 --> 1986.02]  just
[1986.02 --> 1986.42]  Zvenecker
[1986.42 --> 1986.84]  just
[1986.84 --> 1987.52]  dot
[1987.52 --> 1988.10]  Zvenecker
[1988.10 --> 1989.18]  at gmail.com
[1989.18 --> 1989.86]  so
[1989.86 --> 1991.64]  I'm happy
[1991.64 --> 1992.52]  to join you guys
[1992.52 --> 1992.94]  but
[1992.94 --> 1994.04]  I'm not sure
[1994.04 --> 1994.66]  if it fits in
[1994.66 --> 1995.94]  as being an African language
[1995.94 --> 1996.20]  but
[1996.20 --> 1998.24]  as we say
[1998.24 --> 1998.88]  there's Daniel
[1998.88 --> 1999.58]  for instance
[1999.58 --> 2001.32]  there's
[2001.32 --> 2001.84]  Sebastian
[2001.84 --> 2002.76]  there is
[2002.76 --> 2003.48]  Graham
[2003.48 --> 2004.34]  you know
[2004.34 --> 2005.14]  people actually
[2005.14 --> 2005.78]  who
[2005.78 --> 2007.10]  are not necessarily
[2007.10 --> 2008.94]  from the continent
[2008.94 --> 2009.48]  or speaking
[2009.48 --> 2010.20]  those languages
[2010.20 --> 2010.88]  but who just
[2010.88 --> 2011.82]  share the same vision
[2011.82 --> 2012.56]  so
[2012.56 --> 2012.98]  like
[2012.98 --> 2013.72]  well
[2013.72 --> 2014.62]  many people
[2014.62 --> 2015.62]  I'm sure
[2015.62 --> 2016.22]  that many people
[2016.22 --> 2016.84]  would be interested
[2016.84 --> 2017.62]  in like
[2017.62 --> 2018.40]  maybe like
[2018.40 --> 2019.66]  writing research papers
[2019.66 --> 2021.08]  or reading language models
[2021.08 --> 2021.98]  or those type of things
[2021.98 --> 2022.42]  for
[2022.42 --> 2023.44]  Skanatongo
[2023.44 --> 2024.16]  so
[2024.16 --> 2024.94]  I mean
[2024.94 --> 2026.24]  as they say
[2026.24 --> 2027.36]  alone
[2027.36 --> 2028.12]  you can do
[2028.12 --> 2028.76]  better
[2028.76 --> 2029.84]  or something like that
[2029.84 --> 2030.34]  but like
[2030.34 --> 2030.86]  together
[2030.86 --> 2032.10]  with a bigger community
[2032.10 --> 2032.56]  you can go
[2032.56 --> 2033.34]  definitely faster
[2033.34 --> 2033.96]  and like
[2033.96 --> 2034.24]  you know
[2034.24 --> 2035.18]  and like
[2035.18 --> 2035.80]  that's how
[2035.80 --> 2036.88]  technical ideas
[2036.88 --> 2037.26]  come
[2037.26 --> 2037.96]  you know
[2037.96 --> 2038.64]  so
[2038.64 --> 2040.04]  I'm definitely
[2040.04 --> 2040.56]  going to share
[2040.56 --> 2040.96]  the link
[2040.96 --> 2041.28]  with you
[2041.28 --> 2041.96]  I have your link
[2041.96 --> 2042.28]  in
[2042.28 --> 2043.68]  to join the Slack
[2043.68 --> 2044.06]  and
[2044.06 --> 2044.88]  and we'll put it
[2044.88 --> 2046.12]  in our show notes
[2046.12 --> 2046.54]  as well
[2046.54 --> 2047.22]  all the links
[2047.22 --> 2048.00]  to everything
[2048.00 --> 2048.72]  we've talked about
[2048.72 --> 2049.04]  yeah
[2049.04 --> 2049.48]  okay
[2049.48 --> 2050.06]  okay
[2050.06 --> 2050.56]  so
[2050.56 --> 2051.28]  I'm definitely
[2051.28 --> 2051.78]  going to share
[2051.78 --> 2052.06]  with you
[2052.06 --> 2052.78]  and you are free
[2052.78 --> 2053.90]  to just call me
[2053.90 --> 2055.72]  I just want to warn you
[2055.72 --> 2056.72]  it's a big place
[2056.72 --> 2058.20]  people find it messy
[2058.20 --> 2059.34]  we usually work
[2059.34 --> 2060.18]  in that chaotic
[2060.18 --> 2061.04]  environment
[2061.04 --> 2061.64]  but then
[2061.64 --> 2062.04]  you mean
[2062.04 --> 2062.98]  community is messy
[2062.98 --> 2064.34]  well
[2064.34 --> 2065.22]  I won't say
[2065.22 --> 2065.64]  I mean
[2065.64 --> 2066.26]  it's just like
[2066.26 --> 2066.84]  that means
[2066.84 --> 2067.92]  it's a real community
[2067.92 --> 2068.38]  yeah
[2068.38 --> 2068.70]  yeah
[2068.70 --> 2069.00]  yeah
[2069.00 --> 2070.76]  so things are not
[2070.76 --> 2071.16]  like
[2071.16 --> 2072.30]  don't wait for people
[2072.30 --> 2072.86]  to be like
[2072.86 --> 2073.04]  okay
[2073.04 --> 2073.30]  this
[2073.30 --> 2073.54]  this
[2073.54 --> 2073.80]  this
[2073.80 --> 2074.18]  you know
[2074.18 --> 2075.02]  take ownership
[2075.02 --> 2076.24]  take initiative
[2076.24 --> 2076.70]  like
[2076.70 --> 2077.78]  on whatever
[2077.78 --> 2078.50]  you want
[2078.50 --> 2079.22]  to work on
[2079.22 --> 2079.90]  and then
[2079.90 --> 2080.62]  people will just
[2080.62 --> 2081.96]  easily follow you
[2081.96 --> 2083.30]  and yeah
[2083.30 --> 2083.96]  I'm pretty sure
[2083.96 --> 2084.90]  it's going to be beneficial
[2084.90 --> 2085.86]  I may
[2085.86 --> 2087.00]  I would like
[2087.00 --> 2087.44]  with pleasure
[2087.44 --> 2087.82]  for instance
[2087.82 --> 2088.36]  also to
[2088.36 --> 2089.46]  on the project
[2089.46 --> 2089.94]  with you
[2089.94 --> 2091.12]  I speak
[2091.12 --> 2091.48]  what
[2091.48 --> 2092.28]  French
[2092.28 --> 2093.32]  a little bit
[2093.32 --> 2093.88]  of German
[2093.88 --> 2094.80]  Russian
[2094.80 --> 2095.68]  English
[2095.68 --> 2097.36]  phone a little bit
[2097.36 --> 2097.76]  so
[2097.76 --> 2098.96]  it wouldn't hurt me
[2098.96 --> 2099.80]  to learn a
[2099.80 --> 2100.96]  sixth or fifth
[2100.96 --> 2101.52]  language
[2101.52 --> 2102.36]  at least
[2102.36 --> 2102.80]  you know
[2102.80 --> 2103.76]  I learned a lot
[2103.76 --> 2104.96]  like working with people
[2104.96 --> 2105.80]  about
[2105.80 --> 2106.22]  I mean
[2106.22 --> 2107.86]  working with Igbo people
[2107.86 --> 2108.74]  or those type of things
[2108.74 --> 2109.06]  so
[2109.06 --> 2110.14]  let us know
[2110.14 --> 2110.72]  the African
[2110.72 --> 2111.10]  past
[2111.10 --> 2111.56]  scare you
[2111.56 --> 2112.58]  just join
[2112.58 --> 2113.64]  is a bad law
[2113.64 --> 2114.48]  resource in general
[2114.48 --> 2115.38]  and I know
[2115.38 --> 2115.94]  there's even
[2115.94 --> 2116.56]  for instance
[2116.56 --> 2117.10]  in Nigeria
[2117.10 --> 2117.66]  they've spoken
[2117.66 --> 2118.44]  Nigerian pigeon
[2118.44 --> 2119.44]  which
[2119.44 --> 2121.06]  I had some ideas
[2121.06 --> 2122.30]  of doing some
[2122.30 --> 2123.02]  pre-training
[2123.02 --> 2123.68]  transfer learning
[2123.68 --> 2124.12]  from that
[2124.12 --> 2124.90]  because I think
[2124.90 --> 2125.26]  there's some
[2125.26 --> 2126.18]  similarities going on
[2126.18 --> 2126.58]  there so
[2126.58 --> 2128.48]  that already
[2128.48 --> 2129.00]  brings the
[2129.00 --> 2129.60]  connection to
[2129.60 --> 2130.24]  Masakana
[2130.24 --> 2130.64]  closer
[2130.64 --> 2131.56]  I guess
[2131.56 --> 2132.16]  so
[2132.16 --> 2133.20]  I would like
[2133.20 --> 2133.50]  to finish
[2133.50 --> 2134.38]  with just one
[2134.38 --> 2134.60]  word
[2134.60 --> 2135.64]  which means
[2135.64 --> 2136.28]  thank you
[2136.28 --> 2136.56]  in
[2136.56 --> 2137.60]  Sarantoma
[2137.60 --> 2138.78]  well thank you all
[2138.78 --> 2139.44]  this has been
[2139.44 --> 2140.28]  so much fun
[2140.28 --> 2141.24]  appreciate it
[2141.24 --> 2142.02]  and we'll share
[2142.02 --> 2143.16]  links in our show notes
[2143.16 --> 2143.68]  for everything
[2143.68 --> 2144.48]  that we've talked about
[2144.48 --> 2145.86]  and all the great
[2145.86 --> 2146.62]  things that you've shared
[2146.62 --> 2147.38]  so thank you all
[2147.38 --> 2148.14]  thank you
[2148.14 --> 2149.48]  thank you
[2149.48 --> 2158.80]  all right
[2158.80 --> 2159.94]  that is our show
[2159.94 --> 2160.52]  for this week
[2160.52 --> 2161.58]  if you dig it
[2161.58 --> 2162.32]  don't forget
[2162.32 --> 2163.14]  to subscribe
[2163.14 --> 2164.14]  head to
[2164.14 --> 2165.52]  practicalai.fm
[2165.52 --> 2166.34]  for all the ways
[2166.34 --> 2167.54]  and if practical
[2167.54 --> 2168.42]  AI has benefited
[2168.42 --> 2168.98]  your life
[2168.98 --> 2170.00]  pay it forward
[2170.00 --> 2170.96]  by sharing the show
[2170.96 --> 2171.54]  with a friend
[2171.54 --> 2172.26]  or a colleague
[2172.26 --> 2173.10]  word of mouth
[2173.10 --> 2174.20]  is the number one way
[2174.20 --> 2175.02]  people find shows
[2175.02 --> 2175.58]  like ours
[2175.58 --> 2176.66]  thanks again to
[2176.66 --> 2177.34]  Fastly for
[2177.34 --> 2177.96]  fronting our
[2177.96 --> 2178.84]  static assets
[2178.84 --> 2179.92]  to Fly.io
[2179.92 --> 2180.64]  for backing
[2180.64 --> 2181.66]  our dynamic requests
[2181.66 --> 2182.76]  to Breakmaster
[2182.76 --> 2183.66]  Cylinder for the beats
[2183.66 --> 2184.84]  and to you for listening
[2184.84 --> 2185.80]  we appreciate ya
[2185.80 --> 2186.94]  that's all for now
[2186.94 --> 2187.96]  we'll talk to you again
[2187.96 --> 2188.66]  on the next one
[2197.54 --> 2205.90]  caboose
[2205.90 --> 2207.66]  marinara
[2207.66 --> 2207.98]  monster
[2207.98 --> 2208.82]  cloud
[2208.82 --> 2210.08]  potential
