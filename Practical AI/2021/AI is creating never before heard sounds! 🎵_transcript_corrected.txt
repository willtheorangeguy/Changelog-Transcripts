[0.00 → 7.54] I have some kind of frustration with a lot of the way that machine learning stuff goes, where it's like not fully attributed data sets.
[7.96 → 11.78] So we are trying to kind of do the hard tech in the opposite direction.
[11.78 → 22.96] All the data sets that we have are open source, or we hired our friends or musicians that we know to create a data set that is fully licensed for this purpose of creating a generative model.
[22.96 → 36.38] And then I think when people are able to in mass create their own generative models, then there is a huge opportunity for creating value for those musicians, getting paid for the generative use of or the licensing of that generator.
[39.22 → 41.94] Big thanks to our partners, Linde, Vastly and Launch Darkly.
[42.14 → 44.36] We love Linde. They keep it fast and simple.
[44.50 → 46.86] Check them out at linode.com slash changelog.
[46.86 → 53.06] Our bandwidth is provided by Vastly. Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[53.32 → 55.04] Get a demo at LaunchDarkly.com.
[55.54 → 58.90] This episode is brought to you by our friends at Rutter stack.
[59.10 → 63.62] And we're calling all data engineers to check out Rutter stack Cloud and start building smart customer data pipelines.
[64.12 → 67.04] Rutter stack is warehouse first, no more silos.
[67.50 → 76.54] Rutter stack builds your customer data lake on your data warehouse, not theirs, enabling all functionality of a CDP with more security and retaining full ownership of your data.
[76.54 → 79.34] It's open source and API first.
[79.66 → 83.08] Rutter stack can be easily integrated into your existing development processes.
[83.64 → 86.38] And because they're open source, you can see all their code.
[86.60 → 89.02] So you don't have to worry about vendor lock-in or black boxes.
[89.56 → 91.14] And best of all, they have transparent pricing.
[91.34 → 93.58] Stop paying your CDP a premium to store your data.
[94.06 → 98.94] Rutter stack is free up to 500,000 events and pricing scales transparently from there.
[99.36 → 101.40] Learn more and get started at Rutterstack.com.
[101.68 → 103.92] Again, Rutterstack.com.
[103.92 → 107.64] That's R-U-D-D-E-R-S-T-A-C-K.com.
[117.04 → 124.52] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[124.86 → 128.92] This is where conversations around AI, machine learning, and data science happen.
[128.92 → 134.00] Join the community and Slack with us around various topics of the show at change.com slash community.
[134.34 → 135.30] And follow us on Twitter.
[135.42 → 137.04] We're at Practical AI FM.
[143.06 → 146.22] Welcome to another episode of Practical AI.
[146.58 → 148.06] This is Daniel Whiten ack.
[148.16 → 151.06] I'm a data scientist with SIL International.
[151.66 → 157.06] I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin.
[157.60 → 158.20] How are you doing, Chris?
[158.20 → 159.38] I am doing very well.
[159.44 → 160.36] How's it going today, Daniel?
[160.88 → 161.66] It's going great.
[161.78 → 162.98] I don't know if we talked about this.
[163.10 → 165.44] Are you a musician in your past at any point?
[165.62 → 169.30] I have been a musician a lot in my past, but I'm not currently right now.
[169.42 → 170.50] But I love music.
[170.70 → 171.70] I dabble a bit.
[171.80 → 178.04] So I'm pretty excited today that we have COTAM Ma'am, who is a musician and programmer.
[178.72 → 186.40] He's the co-founder of Never Before Heard Sounds, which uses machine learning and AI for musicians,
[186.40 → 187.64] which is pretty exciting.
[187.64 → 188.52] Welcome, COTAM.
[188.88 → 189.60] Good to be here.
[189.72 → 190.48] Thank you for having me.
[190.76 → 198.32] Maybe we should just start out to let people know how machine learning maybe has been used
[198.32 → 203.54] before for music or, you know, some things that people are trying out there.
[203.62 → 205.60] Just sort of set the landscape for us.
[205.64 → 212.16] How have people tried and maybe failed or succeeded in using machine learning in the realm of music?
[212.16 → 212.84] Sure.
[213.34 → 220.68] I mean, there's been, I guess, a lot of sorts of statistical music generation for decades now.
[221.22 → 226.20] I wish I could remember this person's name, but automatic music generation sort of in the MIDI form
[226.20 → 232.74] using Markov chains has been pretty successfully used to imitate, you know, classical era composers
[232.74 → 235.72] going back from the 80s and 90s.
[235.72 → 244.02] And MIDI, this M-I-D-I, for those that don't know, that's like a representation of like a sort of markup
[244.02 → 247.94] representation of notes and links of notes and that sort of thing, right?
[247.94 → 249.84] Sadly, I remember all this all day.
[249.84 → 257.64] Yeah, no, thanks for stopping because I might speak in some other music-specific jargon.
[258.02 → 261.46] Yeah, MIDI is, you know, notes onset and offset.
[261.98 → 268.08] And, you know, more recently, a lot of stuff has been in the audio classification realm.
[268.78 → 275.04] Certainly, people want to know, you know, when piece of audio someone's talking or there's music playing
[275.04 → 279.96] or in music information retrieval, which is a massive field song.
[280.18 → 282.18] This is just all like super broad overview.
[282.28 → 285.08] And then we'll get into this little niche corner that we occupy.
[285.70 → 290.78] Music information retrieval, which is about figuring out what the chord structure of a song is,
[290.84 → 292.46] maybe even the genre of a song.
[293.24 → 298.70] This has also been going on for, you know, more than a decade at least.
[298.70 → 305.96] More recently, sort of deep learning stuff has been in the realm of music generation.
[306.58 → 313.18] So really trying to get some really accurate, you know, sort of composition length audio
[313.18 → 318.64] that maybe isn't a specific style of an artist or a period or a location.
[319.38 → 325.78] And then the realm that we're focused on at the moment is in the audio generation realm.
[325.78 → 332.68] So forgetting the sort of the pitch MIDI format stuff and jumping straight into how can we
[332.68 → 336.18] make new and interesting sounds using machine learning.
[336.96 → 341.72] I'm wondering, as I'm thinking about this, we sort of talked about MIDI a little bit.
[341.94 → 347.72] And then we have like, you know, I think people are familiar with at least like audio files,
[347.72 → 350.34] like they might have MP3 files or WAV files or something.
[350.34 → 358.36] But in terms of AI models and these generative models, like how is audio represented in most of
[358.36 → 363.98] these models in terms of like data input and generally how it's processed?
[364.60 → 365.40] Yeah, great question.
[366.04 → 374.46] I would say, you know, the sort of the MIDI to audio jump is a similar kind of leap as say,
[374.46 → 382.30] like text to image, just a substantially more data to deal with and much more complex models.
[382.66 → 386.68] So MIDI can be represented in a number of ways.
[386.96 → 392.88] You can think of it as if you've ever seen sort of like a piano roll or a music box where
[392.88 → 396.82] you have kind of all the notes in one dimension and then time in another dimension,
[396.82 → 402.42] or you can represent it just to sort of discrete onset events and offset events.
[402.42 → 406.70] And so there's a great piano transcription model called onsets and frames.
[406.86 → 413.96] And it is able to kind of reduce the piano transcription output to a pretty kind of compact
[413.96 → 418.96] format by just giving you the onset and the offset of the notes, as opposed to, you know,
[419.00 → 422.96] you can imagine sort of this 2D array of data is a much bigger thing to represent.
[423.48 → 427.00] On the audio side, there are a few ways to do it.
[427.00 → 431.48] The models that I'm typically working with are outputting sample by sample.
[431.48 → 439.74] So audio, digital audio, you know, like a wave file is an array of floating point values,
[439.82 → 441.44] usually one for each channel.
[441.68 → 445.32] And that's typically sampled at 44,000 times a second.
[445.48 → 451.62] So we're talking about quite a lot of data for things that are generating in the raw audio
[451.62 → 452.18] domain.
[452.50 → 457.42] It makes it kind of challenge, you know, especially a challenge to do it quickly because
[457.42 → 460.16] it's a lot of data to generate.
[460.16 → 460.60] Yeah.
[460.60 → 461.16] Yeah.
[461.16 → 468.04] I assume that, you know, it's not that satisfying to have a generative model where maybe you hit
[468.04 → 473.58] a note on a keyboard and then like seven seconds later you get the output, right?
[474.16 → 474.68] Yeah.
[475.40 → 477.14] It's delayed gratification there.
[477.86 → 483.96] You know, I don't know that that would promote like a lot of jazz improve and that sort of thing.
[483.96 → 484.40] Yeah.
[484.40 → 489.18] You can imagine how hard it would be to learn an instrument where say you sit down at a
[489.18 → 493.70] keyboard, and you play for a minute and a half, and then it's totally silent.
[493.96 → 497.62] And then you come back, and you can hear what your minute and a half sounded like.
[497.72 → 501.64] It would be a pretty laborious way to learn anything.
[501.64 → 507.44] So specifically the models that we focus on are in the audio domain are real time.
[507.60 → 512.98] So they both need to generate faster than real time, and they need to have small enough
[512.98 → 517.54] little buffered chunks to be able to keep up with a low latency.
[517.92 → 520.34] So there's kind of two parts of real time audio processing.
[520.62 → 525.20] One is the real time, which is like it takes less than a second to produce one second of
[525.20 → 525.50] audio.
[525.50 → 529.34] That would technically be a real time model, but then a low latency real time model would
[529.34 → 535.38] be as soon as you, you know, ask for the beginning of the audio generation, how long does it take
[535.38 → 538.08] to give you the beginning of the response?
[538.64 → 543.44] You'd kind of have to be Beethoven, you know, being the deaf composer that he was to be successful.
[543.60 → 546.98] Otherwise, you know, if you were having that delayed period all the way through there.
[547.10 → 548.02] Yeah, that would be tough.
[548.60 → 553.86] These models that you're working with, these generative models, I mean, maybe the first thing that
[553.86 → 558.78] comes to people's mind when they think of generative models is GANs, so generative adversarial networks.
[558.78 → 562.64] Is that sort of the realm of things that you're working with?
[562.78 → 568.36] Or are you, what's the sort of range of those types of either frameworks or architectures that
[568.36 → 570.08] you're exploring in the audio space?
[570.24 → 572.88] We had some success with GAN based models.
[573.16 → 579.60] We actually made like a little website where we show off two of these models called GAN.style.
[579.60 → 587.72] You drop in a YouTube link, and then it replaces the audio of that YouTube link with the audio generated
[587.72 → 588.80] from one of these models.
[589.46 → 590.28] That sounds exciting.
[590.70 → 597.70] Yeah, so the two models that we got running in the GAN style are a choir model that's generated from,
[597.70 → 607.32] I think, 11 plus hours of kind of choral church music and a string quartet model, which is from
[607.32 → 615.10] a university computer science slash music crossover department that they released a paper with this
[615.10 → 616.64] data set.
[616.78 → 622.00] So those are both trained using GAN and a discriminator for the loss.
[622.20 → 625.22] We've also had some luck losing the discriminator part.
[625.22 → 629.16] It trains a lot faster in this other kind of losses that we were able to use.
[629.72 → 635.88] I think if you look at the paper out of Magenta called DDSP, you'll see a really successful
[635.88 → 640.26] version of this sort of timbre transfer, the same kind of technique turning one sound into
[640.26 → 640.60] another.
[641.02 → 642.80] And they don't use a GAN approach.
[642.96 → 646.78] They just use, yeah, different loss, FFT loss.
[647.22 → 651.72] So I have an almost side question because I'm fascinated by this.
[651.82 → 654.42] And it's a use case for GANs that we haven't talked about yet.
[654.42 → 658.14] You know, which seems kind of weird at this point since, you know, we all love music and
[658.14 → 658.42] everything.
[658.92 → 662.92] But I can't wonder what drove you into this?
[663.06 → 666.20] I mean, I guess you were doing music first and getting it.
[666.32 → 670.18] You know, how did you combine all of this to go do this?
[670.22 → 671.80] And what was the motivation to get you going?
[671.86 → 675.08] Because as you've been explaining this, I've been wondering that along the way.
[675.26 → 675.38] Yeah.
[675.64 → 676.68] How does someone end up here?
[676.78 → 677.38] Good question.
[677.54 → 678.34] How do you end up there?
[678.46 → 678.68] Yeah.
[678.82 → 679.40] I mean, really?
[679.56 → 681.56] And how can I end up in the same place?
[681.56 → 683.16] It sounds like a lot of fun.
[683.54 → 685.44] He was much smarter about it than we were.
[685.80 → 686.20] Yeah.
[686.44 → 686.70] Yeah.
[686.70 → 692.08] I actually never even really thought about like learning how to program or anything like
[692.08 → 697.84] that until I was kind of into my, I guess, junior year of college.
[698.00 → 699.26] I studied music.
[699.34 → 701.46] I played piano and I studied jazz piano.
[701.72 → 703.46] That was kind of my whole focus.
[703.68 → 708.08] I was really interested in kind of music production techniques and different kind of things.
[708.08 → 713.42] But I had never expanded to the realm of sort of like entirely generative and especially
[713.42 → 715.80] not like machine learning generated.
[716.06 → 719.42] That wasn't just a thing that popped into your mind, studying music in school.
[719.94 → 720.12] Yeah.
[720.20 → 726.22] So I was lucky that I went to a school that had this computer music department, which I
[726.22 → 730.38] didn't know as a field and which is, you know, like a very vibrant field over the past
[730.38 → 734.00] many decades with a few kind of like bases all around the world.
[734.00 → 739.72] And one of the bases is at UC Berkeley, the Centre for New Music and Audio Technology.
[740.12 → 746.74] And I just was sort of enamoured by the way that people were making music there.
[747.04 → 753.52] And this entirely new seemed like really innovative, seemed like the stuff that they're making is
[753.52 → 757.98] like a huge departure from anything that you could do using different techniques.
[757.98 → 763.20] So that kind of led me down this route of like, okay, how can technology kind of like make
[763.20 → 764.36] new music?
[764.68 → 768.10] How can it kind of keep progressing and pushing music forward?
[768.78 → 774.02] And, you know, I had done then many, many projects sort of in music technology, building
[774.02 → 780.14] synthesizers, building even like, you know, music generator systems, doing some like generative
[780.14 → 782.08] music for video games, different things.
[782.08 → 789.68] And maybe about four years ago or something, I started to get more into, okay, you know,
[789.76 → 794.32] like machine learning, this is the next big technology innovation.
[794.84 → 796.18] What's this going to do for music?
[796.30 → 802.60] And so it kind of like, you know, I just saw a huge, huge opportunity in all the potential.
[803.58 → 809.64] And so about two years ago, I started a company with a partner, Christina Never called Before
[809.64 → 815.56] Heard Sounds, basically entirely dedicated to this question of, okay, what is AI ML going
[815.56 → 816.62] to do for music?
[817.32 → 823.46] And specifically with the angle of like, you know, there's a lot of people doing not a lot,
[823.56 → 828.74] but music generation systems, you know, like for ads or for, I totally understand the like
[828.74 → 832.68] utility of that, but that for me doesn't progress music.
[832.92 → 835.48] Like that doesn't push the envelope of what's possible.
[835.48 → 841.82] It sort of puts music in this like utilitarian category of like, okay, music serves a function,
[842.62 → 847.72] you know, helps you study, you know, like works really well in this ad video and things like
[847.72 → 847.94] that.
[848.08 → 854.20] But it doesn't kind of like, you know, the way to progress music is to put those tools in
[854.20 → 856.30] musicians' hands to build the instruments.
[856.50 → 856.58] Yeah.
[857.00 → 862.42] So you're there in school, you're a junior, you have not previously done this, you discover
[862.42 → 866.44] this, but I got to say, and I'm not just talking about music here.
[867.20 → 874.16] I'm thinking back to myself and probably most people to leap into machine learning and to
[874.16 → 876.92] suddenly be able to be a practitioner in the space.
[877.06 → 878.26] That's a tall order.
[878.56 → 880.40] That is a significant leap right there.
[880.82 → 883.68] Can you tell us a little bit about, you know, you're this musician, you're doing this,
[884.28 → 886.40] you discover this, you get this exposure.
[886.90 → 889.04] How did you make that jump into being a practitioner?
[889.36 → 890.52] How did you accomplish that?
[890.52 → 894.30] You know, I graduated over 11 years ago, 10 years ago.
[894.34 → 896.10] So it's been a slow transition.
[896.76 → 898.94] It definitely was not something overnight.
[899.06 → 899.24] Okay.
[899.34 → 904.78] First started with, there was this great, you know, my, my like primary language that I
[904.78 → 910.04] got super into after college, where it's like, it's all Python and Java and Lisp for
[910.04 → 910.62] some reason.
[910.96 → 914.70] So, you know, then the thing that I was most fascinated with is JavaScript.
[914.70 → 919.96] Because it's like you program in JavaScript, people can run your applications on like billions
[919.96 → 922.72] of devices and great language for that reason.
[922.96 → 928.78] So I got into the first thing that I looked at with machine learning was this really simple
[928.78 → 931.48] neural net implementation in JavaScript.
[932.16 → 934.64] And I wish I could remember the name.
[935.14 → 938.20] I remember the author's first name was Heather.
[938.52 → 939.66] I think I saw that.
[939.74 → 941.52] I don't remember either, but I think I remember.
[941.52 → 942.26] From years ago.
[942.38 → 942.52] Yeah.
[942.52 → 944.56] I think I remember what you're talking about.
[945.08 → 948.04] If you know what we're talking about, let us know and we'll put it in the show notes.
[948.24 → 948.76] That's right.
[948.94 → 949.54] Yes, please.
[949.64 → 950.00] Thank you.
[950.34 → 955.50] So it was this great, like compact library and just like being able to see those things
[955.50 → 959.04] in this, you know, JavaScript is a fairly simple language.
[959.14 → 962.72] Being able to see those concepts, like kind of laid out in that simple way.
[962.76 → 964.60] That was my, that was my start.
[964.60 → 969.50] And like in the beginning, I wasn't able to really produce anything interesting or fascinating
[969.50 → 972.28] with this, but like I kept trying, I kept seeing that potential.
[972.52 → 996.56] With advancements in AI and deep learning evolving at lightning pace, it's more important now
[996.56 → 1000.08] than ever to research the best options suited to your unique needs.
[1000.08 → 1005.40] This is particularly true when building custom systems and those systems that are GPU heavy.
[1005.90 → 1010.24] Not only do the applications running on the system matter, but your AI infrastructure and
[1010.24 → 1013.02] budget constraints need to be front of mind as well.
[1013.64 → 1020.30] PSSC Labs, which is an HPC and AI custom solutions provider based in California, has been creating
[1020.30 → 1025.18] high performance computing systems to meet their clients' unique enterprise computing challenges
[1025.18 → 1026.76] for more than 25 years.
[1026.76 → 1033.18] And with cloud computing costs growing at astronomical rates, plus companies increasingly losing control
[1033.18 → 1037.88] of their data security, it is no wonder that enterprises and government agencies need to
[1037.88 → 1040.72] continually look for ways to take back control of their data.
[1041.14 → 1047.38] Solutions from PSSC Labs provide a cost-effective, highly secure, and performance guarantee that
[1047.38 → 1050.94] organizations need to reach their AI and machine learning goals.
[1050.94 → 1057.88] For more information and a free consultation, please visit PSSCLabs.com slash practical AI.
[1058.22 → 1062.58] Once again, that's PSSCLabs.com slash practical AI.
[1062.58 → 1076.58] We were chatting before starting the recording about some of the projects that you're working
[1076.58 → 1076.86] on.
[1076.86 → 1084.30] And I think you had mentioned this one AI vocal technology that you just released, which I think
[1084.30 → 1085.20] is fascinating.
[1085.20 → 1089.76] And not only is it interesting technology, but I think it has a lot of elements in it that
[1089.76 → 1096.06] I think people, you know, may have follow-up questions on in terms of like data and the
[1096.06 → 1099.72] motivation and use and, you know, all of those things.
[1099.72 → 1101.88] So could you just introduce that?
[1101.96 → 1103.46] I believe it's called Holly Plus.
[1103.60 → 1105.88] Tell us a little bit about that and how it came about.
[1106.42 → 1106.58] Yeah.
[1106.58 → 1115.86] So I had mentioned this past project GAN style and really the for me, the interesting thing
[1115.86 → 1121.32] with these models that we've been developing is, you know, like we can find cool data sets
[1121.32 → 1122.40] and we can train cool models.
[1122.58 → 1126.92] But really, I think the big leap is in letting people train their own models.
[1127.16 → 1131.34] And now you have a generator of your specific sound.
[1131.34 → 1138.00] You know, your grandma's piano with the one squeaky note and like the out of tune, upper
[1138.00 → 1143.84] register or your specific guitar playing technique where you, you know, slap certain notes and
[1143.84 → 1144.72] you pluck others.
[1145.26 → 1149.30] And obviously the most personal instrument that we all have is our voice.
[1149.88 → 1155.74] It seems like the voice models are like really the most interesting personal model.
[1155.94 → 1160.98] So while we were developing GAN style, we're thinking about, okay, like it'd be cool to find
[1160.98 → 1163.94] some musical artists that we could collaborate with.
[1164.42 → 1170.80] And I always had Holly Herndon in mind just because she's done a lot of AI music projects.
[1171.24 → 1177.16] So I actually just basically tweeted at her musical partner, and we were DMing, and I was like,
[1177.34 → 1181.44] or no, actually he had first posted on our launch day.
[1182.02 → 1185.84] Hey, is there anyone out there who could help us out with machine learning?
[1186.42 → 1190.24] You know, like any, any data scientists, people, ML programmers who could help us out with
[1190.24 → 1190.70] the project.
[1191.14 → 1195.18] I immediately responded in DM, and I was like, yeah, what are you looking for?
[1195.24 → 1198.68] And he's like, well, we want to build a website where anyone, where we could train a custom
[1198.68 → 1204.60] model on Holly's voice, and we could have anyone uploaded audio file, transform it into that
[1204.60 → 1207.32] custom model and then kind of like have the results.
[1207.70 → 1211.52] And we had just released this GAN style, which is, you know, a lot of the same mechanism.
[1211.52 → 1215.22] And I had already transformed one of her songs into the choir.
[1215.22 → 1221.88] So I sent it to him, and he's like, I think his response was Holly and I are freaking out.
[1222.12 → 1222.82] Can we talk?
[1224.82 → 1225.38] Yeah.
[1225.46 → 1231.60] Fast forward a few months, we had sort of repurposed this, you know, GPU backend that we had developed
[1231.60 → 1239.12] for, or not repurposed, but augmented now to, to include this Holly Herndon model and trained
[1239.12 → 1244.20] a model from her, you know, a bunch of recordings that she gave us of her voice.
[1244.26 → 1249.18] And she's got a one reason that this worked kind of successfully is that her vocal style
[1249.18 → 1251.34] is, is not acoustic.
[1251.66 → 1252.80] It's very digital.
[1252.96 → 1258.98] It's a lot of like harmonized, a lot of vocoder stuff, a lot of like digital glitches.
[1258.98 → 1263.34] And, you know, like one thing that machine learning is perfect at is producing some
[1263.34 → 1264.56] digital glitches.
[1264.56 → 1267.58] So yeah, it worked out pretty well with her voice model.
[1268.00 → 1274.38] And then last week we, you know, we released it to the world where anyone could drop in
[1274.38 → 1277.82] an audio file and have it transformed into Holly Herndon's voice.
[1278.22 → 1280.68] I have so many follow-up questions on this.
[1280.84 → 1283.70] I don't think we'll get to them all in our, in our interview.
[1284.46 → 1287.54] So, so you'll have to keep, keep me on track, Chris.
[1287.54 → 1293.80] Maybe first off, like you were talking about the voice being one of the most personal sorts
[1293.80 → 1301.00] of instruments that we have, but also, you know, a musician's voice, it's sort of like,
[1301.06 → 1302.92] it's a big part of their livelihood, right?
[1302.98 → 1304.94] And how they, how they make money.
[1305.06 → 1309.76] So what, what are your sort of thoughts and what were your discussions with Holly and maybe
[1309.76 → 1314.62] others as you were entering into this project and the future of these types of projects around,
[1314.62 → 1322.44] like, Hey, I could, you know, uh, I get Taylor Swift's voice and I can produce a my own backing
[1322.44 → 1322.88] track.
[1322.88 → 1329.34] And now I have my own Taylor Swift song and release it on and stream it on, uh, some service.
[1329.34 → 1331.50] And now I'm making money off of it.
[1331.50 → 1331.72] Right.
[1331.72 → 1335.48] So there's a lot of like messy stuff that could come up here.
[1335.48 → 1340.10] So what, what were some of your thoughts on that and what discussions have you had there?
[1340.10 → 1345.06] Yeah, this was really for Holly Ended and Matt Dewhurst.
[1345.20 → 1351.12] This was the purpose of the project was like the age of this, exactly what you're describing,
[1351.28 → 1352.28] Daniel, this is coming.
[1352.70 → 1358.72] And they wanted to kind of control that story and offer a version of how this could go.
[1359.08 → 1365.20] So they have a whole mechanism for how things that are created with this, you know, they're,
[1365.20 → 1369.66] they're free, and they're, they're able to be used, but the ownership is actually through,
[1369.66 → 1372.76] uh, like a DAO, a decentralized autonomous organization.
[1372.96 → 1379.04] That's their version of how this kind of rights management could go.
[1379.40 → 1385.06] But I think that this kind of are the most relevant questions when you think about, about
[1385.06 → 1386.78] these types of generative models.
[1386.78 → 1392.90] Um, our version of this and how we've been producing and thinking about the future models
[1392.90 → 1397.30] that we produce is really like full transparency, full attribution.
[1397.30 → 1404.72] And, and also when we get to it, uh, being able to kind of pay the artists back that went
[1404.72 → 1405.60] into this model.
[1405.60 → 1412.02] So I have some kind of frustration with a lot of the way that machine learning stuff goes,
[1412.02 → 1418.14] where it's like not fully attributed data sets or like a lot of scraped data sets and things
[1418.14 → 1418.64] like that.
[1418.64 → 1424.10] And so we are trying to kind of do the hard tack in the opposite direction.
[1424.10 → 1430.52] Um, the all the data sets that we have are open source, or we, we hired our friends or
[1430.52 → 1436.00] musicians that we know to create a data set, uh, that is fully licensed for this purpose
[1436.00 → 1437.32] of creating a generative model.
[1437.32 → 1443.42] So, and then I think when people are able to kind of in mass create their own generative
[1443.42 → 1449.72] models, then, uh, there is a huge opportunity for that being sort of, you know, creating value
[1449.72 → 1454.66] for those musicians, like getting paid for the generative use of, or the licensing of that
[1454.66 → 1455.20] generator.
[1455.56 → 1458.90] Um, so that's kind of how I see that potential future.
[1459.86 → 1465.26] So Holly was a part of this process and maybe had a vision for the future of how this data was
[1465.26 → 1471.92] going to be used and potentially how, you know, her career and, uh, could be benefit benefited
[1471.92 → 1472.28] from it.
[1472.34 → 1475.64] Maybe how her bottom line and her finances could be benefited from it.
[1475.88 → 1482.12] Whereas like, if I go to Spotify and just use some tool to capture a bunch of audio from an
[1482.12 → 1486.66] artist, they have no knowledge of, of that particular use.
[1486.66 → 1491.50] And so, you know, part of it, I guess is on the data side and maybe part of it is on how
[1491.50 → 1493.30] the model is, is released.
[1493.30 → 1499.06] I know we've been seeing a lot more models, even, you know, outside this genre of models
[1499.06 → 1506.02] being released as APIs where there's sort of more control in terms of who's using that
[1506.02 → 1512.06] for what and how that exchange of value is happening and, and that sort of thing.
[1512.42 → 1512.92] So, yeah.
[1512.96 → 1517.58] Do you see a lot of these models maybe in the future being released in that sort of API
[1517.58 → 1525.14] form or, or, you know, because I could also just throw the model up on S3 or something and
[1525.14 → 1528.94] then like anybody can use it to generate, generate a voice, maybe.
[1529.52 → 1529.62] Yeah.
[1529.70 → 1530.00] True.
[1530.16 → 1535.94] For the time being, we are kind of in full control of, of how these models are all used.
[1535.94 → 1539.44] So, you know, they are behind an API that we control.
[1539.56 → 1545.34] There are, they are on our servers, and we are not yet at the place where we intend on
[1545.34 → 1547.16] open sourcing these models or their weights.
[1547.74 → 1554.72] Um, partially because of these reasons of, you know, like being able to kind of, um, control
[1554.72 → 1561.46] who uses it and like give value to the musician's effort that went into this and kind of, you know,
[1561.46 → 1564.40] honour that by not just giving it away for free everywhere.
[1565.00 → 1569.80] You know, it's, it's interesting is that this is an area like, like pretty much everything
[1569.80 → 1576.48] we've seen in the AI ML space that because it's a totally new way of doing things and
[1576.48 → 1578.58] clearly there will be lots of people.
[1578.68 → 1583.18] I mean, this is, I mean, you're pioneering something that I think will be huge going
[1583.18 → 1583.52] forward.
[1583.68 → 1588.92] And yet there's the kind of AI ethical consideration that is kind of built into everything that
[1588.92 → 1589.30] we do.
[1589.30 → 1593.28] You know, we've had this conversation across so many topic areas and stuff.
[1593.60 → 1594.22] It's pretty cool.
[1594.32 → 1598.00] I mean, so you're recognizing that early on and there are questions that have to be figured
[1598.00 → 1602.38] out and like, like every other field, but, and, and it sounds like you're taking a kind
[1602.38 → 1606.14] of a careful, you know, kind of respecting that, that process up front.
[1606.52 → 1612.00] How do you shape that as you, as, as a pioneer yourself in this field, and you're looking at,
[1612.00 → 1617.06] uh, an industry that where other people will start doing either the same or very similar
[1617.06 → 1619.58] things and exploring their own creativity.
[1619.58 → 1624.90] So just like we've seen in, uh, in convolutional with, you know, artwork creation, you know,
[1624.90 → 1629.72] in terms of visual things, how do you think that will roll out going forward to, to try
[1629.72 → 1634.84] to, to try to have a whole new industry in music that is taking advantage of this and,
[1634.84 → 1638.22] you know, merging it with existing, you know, approaches.
[1638.22 → 1644.10] As a small company, what all we can do is kind of like lead by example and hopefully make
[1644.10 → 1650.36] this sort of public enough information that it, people might expect that from other companies,
[1650.74 → 1655.78] full attribution of the data sets or that, you know, the musicians involved are paid.
[1655.94 → 1660.96] I guess part of it is really education of how this stuff works.
[1660.96 → 1666.64] I think a lot of times the story that's sort of spun is like the AI as some agent that's like,
[1666.64 → 1671.80] you know, like a magical character that's off in the cloud doing some magic up there.
[1671.94 → 1677.00] But, you know, the story that we're trying to make clear is like, no, that's, that's actually
[1677.00 → 1677.80] not really how it works.
[1677.88 → 1681.48] There are a bunch of musicians, you know, there's kind of this condensed mathematical model,
[1681.48 → 1684.54] and that is a generator that you can then play with.
[1684.68 → 1689.74] But in the end, that model acts as a conduit between you, a musician and the data set musicians.
[1690.06 → 1695.44] So making those, those data set musicians as kind of clear as possible and making that
[1695.44 → 1698.78] narrative as clear as possible is our approach to it.
[1698.90 → 1703.34] You know, so that when other data sets come out, I think the immediate question for consumers
[1703.34 → 1706.24] is hopefully, okay, well, where'd you get the data?
[1706.44 → 1707.24] You know, who's involved?
[1707.48 → 1708.16] What are their names?
[1708.40 → 1709.54] Where are they paid for it?
[1710.30 → 1711.46] And those kinds of things.
[1711.74 → 1717.58] And, and yes, putting a face on that data set is our, is our approach that hopefully catches on.
[1717.58 → 1726.72] And that data set that you gathered or worked on with Holly and her collaborators, what did that end up looking like?
[1726.78 → 1734.02] What data was needed to actually make this happen in the end in terms of like how much and like, you know,
[1734.06 → 1738.36] someone could put in almost any kind of audio into this thing, right?
[1738.36 → 1746.70] We actually just had a conversation, I think in the last release episode about, you know, out of distribution input into, into models.
[1746.88 → 1752.04] And sort of here, you've got like this whole range of whatever audio could be that could come into this.
[1752.18 → 1761.40] So what did it take to put the data set together and get it behaving reasonably for, for a sort of wide variety of audio input?
[1761.84 → 1765.44] It's the right question, which is like, how do you, how do you train something?
[1765.54 → 1767.54] And really it all just comes down to the data set.
[1767.54 → 1775.00] So for us, we, it was a few iterations, you know, we have definitely a bunch of models that, that didn't really come together in the end.
[1775.32 → 1785.92] And the initial ask was for Holly and Matt was, okay, can you give us roughly two hours of audio, you know, wave files that are self-similar.
[1786.22 → 1795.42] And the self-similar part is like kind of abstract notion, but you know, we're like, okay, whatever is the, the Holly sound, like give us, give us those.
[1795.42 → 1803.46] So, so we had a few backs and forth, and we trained probably about a half a dozen models on different permutations of their data set.
[1803.74 → 1809.40] We built a few tools that, that do, you know, sort of data set analysis and throw out things that are too far.
[1809.40 → 1814.70] Or the thing that ends up being really far, oftentimes in audio data sets is like silence.
[1815.36 → 1819.66] So, you know, automatic silence kind of trimming and things like that.
[1819.66 → 1826.90] And so, yeah, roughly about two hours of audio is what we've been using as our rule of thumb for these data sets.
[1826.98 → 1833.36] But it all depends on kind of how sort of self-similar it is and then what you're asking for it to do on the output.
[1833.36 → 1842.10] So, because this was, you know, something that we wanted to be able to handle pretty much any audio file that people throw into it.
[1842.10 → 1852.34] We also just trained it for, for a really long time to try and kind of get out all of those little weird squeaks and edge cases that happen when you ask it for something that it knows nothing about.
[1852.34 → 1867.22] We deserve a better internet and the Brave team has the recipe for bringing it to us.
[1867.22 → 1868.36] Start with Google Chrome.
[1868.60 → 1872.30] Keep the extensions, the dev tools, and the rendering engine that make Chrome great.
[1872.50 → 1873.38] Rip out the Google bits.
[1873.52 → 1874.14] We don't need them.
[1874.52 → 1877.02] Mix in ad and tracker blocking by default.
[1877.30 → 1880.00] Quick access to the Tor network for true private browsing.
[1880.00 → 1884.70] And an opt-in reward system so you can get paid to view privacy-respecting ads.
[1884.82 → 1888.64] Then turn around and use those rewards to support your favourite web creators like us.
[1888.98 → 1893.56] Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[1904.56 → 1908.62] Yo, Tom, I want to return to a comment you made much earlier,
[1908.62 → 1914.30] which is that one of your big focuses on your work is real-time audio processing.
[1915.10 → 1923.90] And you sort of describe what that meant in terms of like, oh, maybe you have around 44,000 samples per second,
[1923.90 → 1928.00] and you're wanting to be real-time and low latency.
[1928.00 → 1937.08] So what has that journey been and the tricks that you found and that sort of thing in order to actually reach that level of performance
[1937.08 → 1940.04] reasonably that you can support?
[1940.40 → 1944.78] Because I'm sure there's a lot of people out there that are interested in that, you know,
[1944.88 → 1948.12] real-time deep learning or AI side of things.
[1948.12 → 1957.38] Maybe not even in the audio space, but in, you know, video or text processing from users or something.
[1957.68 → 1960.20] What's your journey been in that real-time space?
[1960.24 → 1965.42] And what are some of the tricks and what you've had to learn in order to reach that performance?
[1965.92 → 1968.98] Basically trying to, you know, we use convolutional models.
[1968.98 → 1971.92] Those run the fastest in general.
[1972.60 → 1978.74] And they also will give you oftentimes, you know, because of the different convolutional layers,
[1978.84 → 1981.34] they'll give you sort of bunch of garbage.
[1981.50 → 1982.32] I don't know how else to put it.
[1982.36 → 1985.82] A bunch of random stuff on either end where there was padding added.
[1985.96 → 1990.00] And what we need is, you know, which is fine if you're generating, it doesn't make,
[1990.36 → 1994.60] you don't even really hear it or notice it if you generate, say, five minutes of audio.
[1994.60 → 2000.36] But if you generate a little tiny, like, say, 256 sample chunk,
[2000.72 → 2008.04] where a large percentage of that chunk is going to just be this sort of convolutional padding garbage on either end.
[2008.16 → 2011.60] So there are a few different techniques to kind of deal with that.
[2011.82 → 2014.52] The most simple is you just sort of trim it off.
[2015.00 → 2021.72] The next more complicated one is you, you know, you do what it would have done internally,
[2021.72 → 2028.56] which is your pass the end back in as the beginning and sort of repeat that over and over again.
[2029.16 → 2031.66] And so you're always just kind of swapping things around.
[2032.12 → 2037.38] That's how we've been able, you know, most models aren't made to kind of stream in this way.
[2037.48 → 2041.54] What I'm describing is how you make these convolutional models stream.
[2042.14 → 2045.94] Most of them are just made for, you know, large batch processing.
[2046.28 → 2050.08] And we need tiny batches that stream really fast.
[2050.08 → 2056.70] Another thing that we've had a lot of luck with in terms of getting, you know, multi-X speed up,
[2056.74 → 2061.64] I think maybe like four or five times faster was when we converted everything to Tensor RT.
[2062.30 → 2064.16] And so that really helped.
[2064.28 → 2071.10] That required also kind of changing the architecture of our model a bit to fit what,
[2071.10 → 2075.36] I guess, Tensor RT had or has implemented.
[2075.36 → 2079.66] Could you talk a little bit about that, about making that conversion and what it was?
[2080.04 → 2083.72] I mean, there was some just basic stuff.
[2083.96 → 2086.04] Like the I used this library.
[2086.18 → 2091.68] Now they actually have a replacement that I think NVIDIA maybe is more officially supporting.
[2091.82 → 2099.94] But I was using this other library called Torch to TRT that did the PyTorch to Tensor RT conversion.
[2099.94 → 2104.34] And it was a bunch of layers basically that it didn't have implemented.
[2104.62 → 2107.86] So I needed to kind of take a look at what their code was.
[2107.96 → 2111.80] Like, for example, like 1D convolution, which is used all over in audio.
[2112.04 → 2114.66] But it's like kind of niche thing, I think.
[2114.78 → 2119.26] Like when I submitted the poll request for like, hey, I implemented 1D convolution.
[2119.50 → 2121.34] Like here, this is what it is.
[2121.38 → 2122.54] I basically just copy-pasted.
[2122.78 → 2124.82] You know, it wasn't anything crazy that I invented.
[2124.82 → 2127.28] I copy-pasted their 2D code and made it work for 1D.
[2127.86 → 2133.14] And the person who responded to this question was, what do you use this 1D convolution for?
[2133.80 → 2141.74] And I think it's just like most people, you know, who are doing image or video stuff aren't used to seeing 1D convolution.
[2142.26 → 2146.58] And that's probably why they didn't even bother implementing the converter.
[2147.26 → 2153.56] There was another thing that came up, which was they doingn't have specific kind of padding that we were using implemented.
[2153.56 → 2155.96] So I needed to swap out a bunch of layers.
[2156.16 → 2158.14] It was, you know, it wasn't pretty work.
[2158.20 → 2160.72] It was a lot of just kind of like grinding away.
[2161.44 → 2165.94] And there wasn't any, it wasn't any like massive, you know, epiphany that I can give your listeners.
[2166.12 → 2169.58] It was really just like, yeah, I went through it step by step.
[2169.68 → 2172.30] And like where things broke, I tried to figure out a way around.
[2172.30 → 2188.10] And so then do all these style transfer and real-time audio processing models in terms of making that real-time, is a GPU required at inference time basically for all of these?
[2189.10 → 2191.98] Yeah, for ours currently, they all are.
[2191.98 → 2198.44] And that's what got us to actually like trying to get it on little tiny pieces of hardware.
[2199.12 → 2199.98] NVIDIA makes...
[2200.74 → 2208.78] Yeah, I've seen pictures with like a little knob and such, which was really intriguing for me because I was like, that's really cool.
[2208.78 → 2213.20] I mean, I was wondering what's inside that box, I guess, was where my question was leading.
[2213.32 → 2220.70] Because if all of that's requiring the GPU, you know, what ends up having to be in that sort of small box to make that happen?
[2220.76 → 2225.04] Because it almost looks like, is it inspired by a sort of guitar pedal type profile?
[2225.42 → 2226.14] Is that...
[2226.14 → 2226.90] Yeah, exactly.
[2227.10 → 2227.78] That's...
[2227.78 → 2235.18] We're trying to meet musicians where, with the tools that they're accustomed to and the things that they have.
[2235.18 → 2246.18] And what not a lot of people have is like a Linux machine with an NVIDIA card and the specific version of CUBA installed and all this kind of stuff that...
[2246.18 → 2255.72] So we're like, okay, well, what we could do is, you know, have basically a little computer with a little GPU and have everything basically pre-installed on it.
[2256.22 → 2263.74] And NVIDIA, they've been actually now, I think, had it for a few years, but they made some big strides with their Jet son platform,
[2263.74 → 2265.26] which is exactly that.
[2265.42 → 2269.52] It's like a Raspberry Pi with a little attached GPU.
[2270.04 → 2271.30] It's not even a discrete GPU.
[2271.44 → 2272.60] It's like an integrated GPU.
[2272.82 → 2275.12] But, you know, it runs all the CUBA libraries.
[2275.34 → 2276.82] It does give you a big speed-up.
[2277.34 → 2283.48] And so, you know, we've been targeting that for sort of our real-time hardware offering.
[2283.76 → 2292.02] And the idea is to get it, you know, fast enough and stable enough that we could have a consumer product that that would work.
[2292.14 → 2292.22] Yeah.
[2292.22 → 2292.70] Yeah.
[2292.70 → 2303.86] And I guess if you had that platform and, you know, that GPU integrated, it seems like in theory,
[2303.86 → 2309.68] you could create a little sort of pedal type device where you could load a bunch of different models on it.
[2309.78 → 2313.96] As you release new models, you could sort of load them on or swap and that sort of thing.
[2313.96 → 2318.94] Because I think a lot of guitar pedals, it's like it does a specific thing, right?
[2319.06 → 2323.08] Maybe this one would be sort of flexible in that way.
[2323.18 → 2324.32] Is that kind of what you envision?
[2325.22 → 2325.60] Exactly.
[2325.78 → 2325.96] Yeah.
[2325.96 → 2331.56] So I think that, to me, is the really exciting part with all of this is like the models.
[2331.78 → 2333.60] Like what can we train?
[2334.12 → 2335.98] What can we make a good generator of?
[2336.36 → 2339.24] So I think, you know, we'll train a bunch of models.
[2339.24 → 2347.34] We have trained a bunch of models, different instruments and data sets that we've either, you know, licensed or recorded or open source.
[2347.58 → 2353.60] But letting people train their own model and then passing it over to their friend and saying,
[2353.60 → 2356.84] Hey, this is a saxophone technique that I was playing with.
[2356.98 → 2358.82] Why don't you try performing violin through it?
[2358.90 → 2361.10] I think that's like the real exciting future.
[2361.74 → 2367.62] So when do you think, you know, beyond kind of the gimmick stage, when do you think we'll be going to like concerts,
[2367.86 → 2376.42] you know, major concerts at major venues and have that integrated in to the, you know, the performance itself?
[2376.42 → 2384.00] And not as, as like, Ooh, we're using AI on stage, but like you get past that, and it's truly part of the art.
[2384.22 → 2387.76] You know, it's, it's built in as much as the instruments they're already using.
[2388.04 → 2392.06] Do you think that's sooner or do you think we're still quite a ways from that at this point?
[2392.22 → 2396.50] I think if, if we have our way, then it will hopefully be pretty soon.
[2396.58 → 2396.76] Yeah.
[2396.94 → 2397.32] Okay.
[2397.72 → 2398.48] Good answer.
[2398.68 → 2401.06] That's, that's exactly what we're working towards.
[2401.06 → 2408.68] And that is, you know, I think that the AI is gimmick will hopefully fade away.
[2408.78 → 2417.34] And the AI is interesting, nuanced, you know, like wild sounds and integral to the art.
[2417.54 → 2417.64] Yeah.
[2417.90 → 2418.14] Yeah.
[2418.16 → 2420.44] Part of it as much as every other part.
[2421.04 → 2421.20] Yeah.
[2421.62 → 2430.66] Maybe that brings up another question, which I've been thinking about, which is, I mean, like you say, computers and synthesis and, you know,
[2430.66 → 2439.00] actually very complicated math and all of that has been used in music for a very long time and synthesizers and other things.
[2439.00 → 2456.00] What do you think like creative wise AI based techniques provide for musicians in terms of their own composition and that sort of thing may be different from like computer based music in the past.
[2456.00 → 2467.26] What are, what are the sort of qualities of AI generated music that maybe distinguish it a little bit from what musicians might have a feeling for already in terms of synthesis?
[2467.92 → 2469.72] I mean, I think that there are a few answers.
[2469.90 → 2473.74] One is the big one is, I don't know.
[2473.84 → 2480.64] And I want to find out basically like Jimi Hendrix was not possible before the electrification of the guitar.
[2480.64 → 2496.42] Like those two things kind of go hand in hand or, you know, so much of, of what you hear on the radio, people, you know, young thug being virtuosic with, with the auto-tune was not possible before auto-tune was a, was a tool.
[2496.42 → 2505.62] So I think really the most interesting part is like how people, what we've kind of laid out is like a utilitarian thing.
[2505.72 → 2508.32] Oh, I don't have a saxophonist, but I have a saxophone model.
[2508.80 → 2512.08] So let me, you know, use the saxophone model to generate a saxophone sound.
[2512.16 → 2521.80] But I think really the interesting part is like where it breaks and like how that is, you know, kind of pushed to stretch to its limits to make something actually truly new.
[2521.80 → 2524.38] So that's, that's what I'm most excited about.
[2524.80 → 2537.98] I think another kind of thing that, that AI affords versus traditional techniques is, you know, like more of an abstract, like I'll call it sort of like a feature space.
[2537.98 → 2550.66] Like some say like a saxophonist's tone is a really sort of like abstract nuance, like a lot of things combined to create that specific musician and their specific tone.
[2551.16 → 2563.98] It's kind of way too many parameters to model, though people try and there's a lot of really cool saxophone models, but AI kind of lets you jump that whole modelling part and just have these learned features.
[2563.98 → 2575.00] And then maybe you can even sort of distill some of the learned features, like maybe you can extract like attitude from the saxophone model and maybe replace it with something else.
[2575.22 → 2581.78] And so this is another kind of like fascinating, exciting area of how, of how these models can be used.
[2581.82 → 2584.58] That is a big departure from what we currently have.
[2584.58 → 2595.72] Well, I know I'm super excited to watch all of these things unfold and also to get one of these little boxes to plug my guitar into whenever, whenever it becomes available.
[2596.22 → 2598.64] Well, thank you so much for sharing all this with us.
[2598.66 → 2599.80] It's been a real pleasure.
[2600.12 → 2609.58] And I love how, you know, just to see the creativity that people are using AI for creative tasks, I think is fascinating.
[2609.58 → 2614.34] But there's also creativity and how you've gone about applying AI, which is amazing.
[2614.52 → 2615.18] So great work.
[2615.30 → 2616.96] And thank you so much for joining us.
[2617.10 → 2617.80] Yeah, thank you both.
[2620.96 → 2623.44] Thank you for listening to Practical AI.
[2623.82 → 2636.00] We have a bundle of awesome podcasts for you at changelog.com, including our brand-new show, Ship It with Gerhard Leon, a podcast about getting your best ideas into the world and seeing what happens.
[2636.00 → 2640.28] It's about the code, the ops, the infra and the people that make it happen.
[2640.54 → 2644.28] Yes, we focus on the people because everything else is an implementation detail.
[2644.62 → 2650.00] Subscribe now at changelog.com slash ship it or simply search for Ship It and your favourite podcast app.
[2650.08 → 2650.56] You'll find it.
[2650.72 → 2653.96] Of course, the galaxy brain move is to subscribe to our master feed.
[2654.08 → 2659.34] It's all changelog podcasts, including Practical AI and Ship It in one place.
[2659.68 → 2664.42] Search changelog master feed or head to changelog.com slash master and subscribe today.
[2664.42 → 2669.62] Practical AI is hosted by Daniel Whiten ack and Chris Benson with music by Break master Cylinder.
[2669.84 → 2672.34] We're brought to you by Vastly, Launch Darkly and Linde.
[2672.64 → 2673.36] That's all for now.
[2673.56 → 2674.52] We'll talk to you again next week.
[2674.52 → 2704.50] We'll talk to you again next week.
