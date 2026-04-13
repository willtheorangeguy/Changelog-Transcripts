[0.00 → 3.72] With these technologies, one of the first things that I thought about was how artists
[3.72 → 8.66] were getting frustrated with the fact that you would have machine learning practitioners
[8.66 → 11.94] come in and creating art with these things and all that.
[12.00 → 15.56] And that's in a very immediate, you can do it today kind of situation.
[16.02 → 21.92] As we've watched these multi-modality evolutions coming through these models over the months,
[22.24 → 28.04] it's not hard to envision that at some point down the road, this will move into video and
[28.04 → 30.64] we'll see other modalities being added to it.
[30.64 → 36.90] And as we do that, you're now moving into that creative space that previously it took
[36.90 → 38.32] a great deal of effort.
[38.72 → 42.48] You know if we're talking about the entertainment industry and movie making and special effects,
[42.94 → 50.36] this could really revolutionize how special effects are cheap and make some amazingly phenomenal
[50.36 → 55.14] special effects as we see iterations going forward become very accessible.
[58.04 → 71.92] Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive,
[72.18 → 73.22] and accessible to everyone.
[73.60 → 75.28] Subscribe now if you haven't already.
[75.50 → 78.38] Head to practicalai.fm for all the ways.
[78.74 → 83.72] Special thanks to our partners at Vastly for delivering our shows superfast to wherever
[83.72 → 86.52] you listen, check them out at Fastly.com.
[86.80 → 92.52] And to our friends at Fly.io, we deploy our app servers close to our users, and you can
[92.52 → 92.90] too.
[93.24 → 95.12] Learn more at Fly.io.
[101.28 → 106.18] Welcome to another fully connected episode of the Practical AI podcast.
[106.72 → 112.08] In these episodes, we keep you up to date with everything that's happening in the AI community
[112.08 → 117.40] and take some time to dig into the latest things in the AI news.
[117.72 → 122.22] And we'll share some learning resources to help you level up your machine learning game.
[122.84 → 124.32] I'm Daniel Whiten ack.
[124.42 → 129.64] I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[129.64 → 132.86] Benson, who is a tech strategist at Lockheed Martin.
[133.18 → 133.86] How are you doing, Chris?
[134.24 → 135.46] I am doing very well, Daniel.
[135.56 → 136.48] Having a good day.
[136.94 → 138.78] Gosh, we've got cool stuff to talk about today.
[138.78 → 143.50] Yeah, but the biggest question though, did you watch Rings of Power?
[144.02 → 150.42] So this is the conflict in my family because I mentioned in the last episode, you know,
[150.42 → 151.88] that I was, but I'm waiting.
[152.12 → 155.58] I'm being a good husband and a good dad till they're ready.
[156.02 → 156.54] Okay.
[156.64 → 164.16] I won't give any spoilers and I probably shouldn't on the podcast anyway, but Chris and me, for our
[164.16 → 166.88] listeners are both big Lord of the Rings fans.
[167.24 → 169.58] So thanks for torturing me here at the beginning of the episode.
[169.58 → 169.82] Yeah.
[169.96 → 170.72] No, no worries.
[170.82 → 172.02] Any, anything I can do.
[172.20 → 172.52] Yeah.
[172.58 → 174.96] I won't, I won't indicate one way or the other.
[175.10 → 176.40] So yeah.
[176.64 → 182.98] I mean, this isn't revealing anything, but I was really interested in and kind of analyzing
[182.98 → 187.14] a lot of the visuals of Rings of Power as I was looking through it.
[187.14 → 193.50] And of course, Rings of Power, Lord of the Rings in general, it's set in a fantasy world
[193.50 → 195.02] of Middle Earth.
[195.34 → 200.76] And so there are all sorts of interesting, interesting visuals and creative elements.
[201.02 → 208.96] A lot of them with a lot of effort put in from designers and artists and graphics people.
[209.24 → 214.16] And it got me thinking a lot more about Stable Diffusion, which is what we're going to talk
[214.16 → 221.62] about today because really this model, and it's the latest in a series of models, but
[221.62 → 228.86] this kind of stream of models, these diffusion models are really kind of taking over and dominating
[228.86 → 231.74] a lot of the discussion in the AI community.
[232.68 → 237.88] And Chris and I thought, thought it would be good to, good to spend some time chatting about
[237.88 → 240.88] them in a lot more detail than we have in previous episodes.
[240.88 → 246.78] So if you're wondering more about Stable Diffusion, what it means, what it is, what it can do,
[247.26 → 248.44] that's what we're going to dig into.
[248.84 → 249.10] Yeah.
[249.16 → 252.60] How have you been thinking about Stable Diffusion?
[252.86 → 255.72] Where has it been entering into your life, Chris?
[256.38 → 262.16] So it is one of those, you know, we've been talking about the different, kind of these different
[262.16 → 267.78] disciplines within machine learning and crossing modalities and joining up.
[267.78 → 272.54] And that's been some, we've had a pretty exciting year in terms of what's happened already.
[273.16 → 279.10] And I think for me, as I know I've expressed to you offline, this is the most exciting thing
[279.10 → 283.42] and not just for what it is, but for what may be to follow.
[284.02 → 289.34] So I think this is, I hope that listeners are as excited as we are because this is one
[289.34 → 294.10] of those moments that I think is going to really turn into something quite wonderful.
[294.24 → 295.98] And it already is looking super cool.
[295.98 → 297.10] Yeah, for sure.
[297.44 → 305.72] So maybe it would just be good to set the stage for what Stable Diffusion is in terms
[305.72 → 311.92] of like what it can do and the motivation behind it, because it wasn't created in a vacuum,
[312.12 → 312.40] right?
[312.44 → 319.86] This is kind of the latest model in a series of these so-called diffusion models, which I
[319.86 → 326.78] think primarily are associated with right now or how they've got the most sort of attention
[326.78 → 330.88] is for text to image tasks.
[331.14 → 337.38] So you put in a text prompt, and it will generate an image corresponding to that text prompt.
[337.48 → 343.34] What are some of the interesting ones that you've seen, Chris, or the sort of images generated
[343.34 → 345.50] from text prompts that have been interesting for you?
[345.50 → 349.76] I think actually, I think some of the things that we've shared a little bit back and forth
[349.76 → 351.92] and that are in some of these articles are pretty cool.
[352.34 → 357.40] You know, being the geeks that we are and seeing things like Lord of the Rings showing up with
[357.40 → 360.28] blended with Star Wars characters in one of those.
[360.44 → 363.70] You know, there's one that has Gandalf and Yoda mixed together.
[363.84 → 364.82] They're just fun.
[364.82 → 370.82] And so I'm enjoying the creativity out of it, but it's really, it's really like I can
[370.82 → 376.42] think of so many uses that aren't necessarily just like cool imagery from a creative standpoint
[376.42 → 377.56] that are really functional.
[377.76 → 380.10] And we can get to that later on in the conversation.
[380.10 → 385.02] But this is one of those that has popped up from time to time that has, it kind of has a
[385.02 → 386.18] sense of magic about it.
[386.22 → 392.08] And of course it's not, I'm sad to say, but it definitely, it definitely has that surprise
[392.08 → 396.94] awe factor and what, you know, what you're able to do as you look at how the different
[396.94 → 398.54] parts of the system work together.
[398.54 → 403.12] And I know we're going to talk about that kind of workflow in terms of how the model
[403.12 → 408.12] works, but the backend, what arises out of that is definitely surprising.
[408.12 → 408.56] Yeah.
[408.78 → 414.78] And I think, like you said, the sort of text to image stuff is maybe the most accessible
[414.78 → 416.38] thing for people to try.
[416.52 → 421.10] And so that's what you've seen most, but I've seen fascinating integrations and demos
[421.10 → 427.84] of the model already because you can do not only sort of just a raw text to image, but
[427.84 → 429.92] you could do sort of like in painting.
[429.92 → 435.98] So you could freeze a part of the image and fill in the rest or like recover parts of an
[435.98 → 441.24] image after kind of, or, you know, if you have an image of a street, and you want to take
[441.24 → 446.34] this person out, you could kind of remove them and then fill in the gap, all sorts of
[446.34 → 450.34] interesting things like that, that you could do as part of the workflow.
[450.34 → 456.06] And then there's also this sort of image to image tasks, kind of doing some sort of translation
[456.06 → 458.68] of image style or something like that.
[459.08 → 463.64] But yeah, a lot of things that are integrating the Stable Diffusion model.
[463.76 → 466.76] One of the reasons is because it's open and people can access it.
[467.00 → 468.14] Yeah, it's fully open source.
[468.40 → 473.38] And I think going back to what you were just talking about for a second there, I think
[473.38 → 477.92] one of the coolest things about it is you can change the representation that's fed into
[477.92 → 479.16] the diffusion model.
[479.34 → 484.26] So, you know, like, as you said, from an accessibility standpoint, you kind of start with this, you
[484.26 → 490.54] know, writing the text out and the train model, which has been trained on so many things in
[490.54 → 496.18] human culture and civilization, you know, has these, these great components to draw from,
[496.28 → 498.24] to pull from within the train model.
[498.50 → 501.98] But, you know, you mentioned the image to image, and we've seen some interesting things
[501.98 → 504.84] where, you know, they, you know, you can take things out of an image.
[504.84 → 508.72] And I know there are other techniques out there, obviously for, for doing this, but the
[508.72 → 510.04] representation can be text.
[510.18 → 510.98] It can be images.
[511.14 → 515.16] It can be lots of different things, which really opens up the possibilities.
[515.16 → 519.60] And I think we'll, we'll kind of span all the disciplines that we commonly talk about
[519.60 → 520.30] in the space.
[520.76 → 520.88] Yeah.
[521.00 → 528.42] So to give people an idea of the accessibility, even just this morning, I had a Google Cola notebook
[528.42 → 528.92] open.
[528.92 → 534.18] It did have a GPU on it, but it was just a Google Cola notebook.
[534.84 → 541.00] I use the hugging face diffusers library where you can import the Stable Diffusion model.
[541.72 → 547.40] There's a pipeline built for, you know, using the pre-trained Stable Diffusion model.
[547.40 → 556.60] So I'm just counting after my imports, I have one, two, three, four, five, six, seven, eight
[556.60 → 560.50] lines of code to go from text to image.
[560.64 → 563.76] So this sort of, there are two factors here.
[563.86 → 567.38] One is like there's great tooling from hugging face, which is something we talk about all
[567.38 → 567.78] the time.
[567.92 → 569.68] So continual great work there.
[569.82 → 575.60] But the other side of it is, this is just running in a Google Cola notebook, and I'm able
[575.60 → 577.26] to access it via my browser.
[577.68 → 584.20] I don't have to like to spin up an instance in the cloud with a big beefy GPU or set of them.
[584.58 → 590.70] This side of the accessibility, both the open source release of the model and the ability
[590.70 → 596.16] to use the model in a computationally efficient way.
[596.38 → 600.48] Those were two of the sort of big motive in my understanding.
[600.64 → 601.90] And I should be explicit.
[601.90 → 606.24] I'm not, wasn't, I didn't have anything to do with training this model, but in my understanding
[606.24 → 613.36] from the teams that train this, which included a sponsor called Stability, that's where it
[613.36 → 614.76] gets its name, Stable Diffusion.
[615.56 → 622.58] Runway ML was involved, which we've, I think, mentioned on the show here before that has tools
[622.58 → 625.04] for kind of creative uses of machine learning.
[625.04 → 631.76] And then academic researchers from Ludwig Maximilian University in Germany.
[632.04 → 639.04] So this group kind of explicitly set out with motivations around accessibility and specifically
[639.04 → 645.58] with accessibility, more computationally efficient, a more computationally efficient diffusion
[645.58 → 648.90] model and one that would be explicitly open source.
[648.90 → 654.42] And I think that's why this has exploded is because if people can access something easily
[654.42 → 660.04] and they don't need really fancy compute to run it, then it's going to kind of spread
[660.04 → 661.00] very quickly, right?
[661.32 → 661.44] Yeah.
[661.54 → 666.72] I mean, it's been noted in multiple places that, you know, if you have a computer with
[666.72 → 670.92] a graphics card that, you know, that's a GPU that you're probably good to go.
[671.00 → 672.90] It doesn't have to be the latest, greatest thing.
[672.90 → 678.28] So it really opens up to people, you know, everywhere that can use this.
[678.44 → 682.70] And probably most people that might be interested in it already have the equipment, you know, even
[682.70 → 687.42] without going to a cloud solution like Cola or something, you have it in your house probably
[687.42 → 688.46] already, and you can do it.
[688.84 → 688.92] Yeah.
[689.02 → 696.40] On a laptop with a card or a desktop or just a cloud instance that's less expensive, right?
[696.48 → 698.58] Than trying to do something.
[698.58 → 702.42] I was reading that for other diffusion models.
[702.60 → 704.20] So we should be explicit too.
[704.28 → 706.60] This isn't the first of these types of models.
[706.72 → 711.88] We already talked about DALI 2, which is, has a lot of similarities with Stable Diffusion.
[711.88 → 718.52] And we'll, we'll kind of point out the differences as we continue the conversation, but also a model
[718.52 → 722.72] that's capable of doing this amazing text to image generation, right?
[722.76 → 727.38] And, and these other applications like in painting and that sort of thing, but it's fairly
[727.38 → 732.06] computationally expensive, and it's not as, as open, right?
[732.08 → 736.86] You have to kind of sign up on a wait list, get access, use it via API, that sort of thing.
[736.86 → 744.10] And I think I was reading, so for some other diffusion models, I read a one statistic that
[744.10 → 751.28] was like 50,000 samples takes about five days to do inferencing on, on a single A100.
[751.28 → 757.36] So most people don't have access to an A100 and maybe don't want to spend five days waiting
[757.36 → 760.30] around for, for the processing of a bunch of samples.
[760.30 → 767.04] Now, 50K is, is a lot as well, but yeah, so that, that's one just kind of baseline or
[767.04 → 773.88] foundational number that, Hey, these things did exist before, but they were extremely computationally
[773.88 → 774.40] expensive.
[774.40 → 778.98] You know, it's, it just as a, as a kind of single point that you mentioned it
[778.98 → 783.72] being open source, we've had, and we've talked about this with previous model releases on
[783.72 → 788.36] the show, different approaches to releasing of different types of models.
[788.36 → 793.02] And, you know, there have been things where there's been concern about how it would be used
[793.02 → 794.82] or security and things like that.
[794.92 → 800.86] And incremental, some things stay proprietary with just kind of front end interface to it.
[800.86 → 805.78] Other things have been released incrementally where the big model is withheld, but a smaller
[805.78 → 809.10] reduced functional version is, is offered.
[809.32 → 813.82] And here we are, and we just went through, you know, Dolly, which as you pointed out, you
[813.82 → 815.56] know, it has, has constraints there.
[815.76 → 818.10] And here we are with this open source release.
[818.36 → 824.34] That's quite powerful and quite amazing and yet quite accessible to, to pretty much anybody
[824.34 → 826.94] who would like to, to start working with it.
[826.94 → 831.08] What, what are your thoughts around, around the fact that, I mean, this is a feeling a
[831.08 → 835.16] little bit more like that open source software world that you and I have both come from,
[835.16 → 836.42] you know, in the past.
[836.42 → 840.88] And how do you think this may change the space going forward?
[841.34 → 846.30] If others as well with, with both this and other releases going forward, we, it tends to
[846.30 → 849.70] be more straight out open source with the level of accessibility.
[849.86 → 851.94] What, how do you, how does that change the space we're in?
[852.48 → 852.58] Yeah.
[852.58 → 855.08] I think that there are a few elements of this.
[855.50 → 860.80] I think it has been interesting last, um, last episode that we, that we had, we talked
[860.80 → 866.14] about these open rail licenses and, um, one is utilized by Stable Diffusion.
[866.14 → 872.06] And so there are some explicit things you have to agree to when downloading the model on hugging
[872.06 → 872.46] face.
[872.48 → 877.16] For example, you have to, you know, click a button that says, I agree to this stuff, and
[877.16 → 878.44] then you can download it.
[878.44 → 882.70] And you have to use your hugging face token to download it, but it is open in, in that
[882.70 → 885.58] sense under, in a sort of unique way.
[885.72 → 892.20] But I think that if we look at models like this and ones that are released open source,
[892.28 → 898.88] I think you saw, you kind of saw in software, I think over time, as it was open sourced, a
[898.88 → 906.08] lot of software applications or kind of specialized software things going from kind of specialized
[906.08 → 912.62] expert groups using them to a general purpose technology that was used and integrated into
[912.62 → 916.84] a whole variety of things that the original creators didn't even have in mind.
[916.84 → 917.12] Right.
[917.26 → 923.72] So I think we're in a similar place here where we're going from maybe models that were being
[923.72 → 927.16] experimented with in sort of siloed places.
[927.16 → 931.68] But now, as you were mentioning, there are all sorts of ways you could imagine using this
[931.68 → 932.06] model.
[932.62 → 937.48] And because I can access it and because I can run it without expensive, you know, hardware
[937.48 → 944.14] and because there's good tooling like the diffusers' library, which I can pull in and do this in
[944.14 → 950.46] eight lines of code, then who knows how people will use this and sort of hack it in a good
[950.46 → 950.82] way.
[950.94 → 951.16] Right.
[951.24 → 954.90] So hacking it for useful kind of pragmatic purposes.
[955.38 → 955.64] I agree.
[955.64 → 960.52] I'm actually looking forward to seeing as it really gets out beyond its core community
[960.52 → 965.48] and reaches all those people and people become aware of it because we're still very early
[965.48 → 971.18] days, it'll be interesting to see some of the ideas that come out of it, both the creative
[971.18 → 976.84] art that we've seen already, but also some of the kind of innovative, maybe kind of business
[976.84 → 983.20] oriented, you know, novel ways of using it that we are not likely to think of today.
[985.64 → 996.28] too much plain
[996.28 → 997.74] than you.
[997.82 → 999.00] You really better
[999.04 → 999.96] good time here when we're so big.
[999.96 → 1025.24] Okay, Chris, you know, I like to get into the weeds sometimes.
[1025.24 → 1030.96] I say we just dive into this model and see kind of how it works a bit.
[1031.08 → 1037.72] We'll kind of take the listeners along with us and go through and figure out how this happens.
[1037.84 → 1040.30] How do we go from text to image?
[1040.66 → 1043.64] And also, how is this thing trained?
[1043.94 → 1045.06] Let's diffuse the weeds.
[1045.52 → 1046.42] Let's get into it.
[1046.64 → 1048.86] Diffuse the knowledge or whatever.
[1049.20 → 1049.32] Yeah.
[1049.32 → 1049.80] Yeah.
[1050.20 → 1055.46] And Chris, I think there are certain things to listen for as we go through this process.
[1055.70 → 1060.16] You and I have talked about some of these building blocks that continually show up.
[1060.26 → 1065.18] One of them being transformers and the attention mechanism that has been applied.
[1065.68 → 1068.86] Of course, diffusion models have been applied in a variety of ways.
[1069.32 → 1073.74] Encoder, decoder models, word embeddings or text embeddings.
[1073.84 → 1077.40] All of these things show up as we go through this.
[1077.40 → 1080.58] So again, this is not kind of popping up out of nowhere.
[1080.80 → 1083.42] It's an assembly of things that we've talked about before.
[1083.68 → 1083.86] Yes.
[1084.20 → 1088.26] This has been a little bit of a magical past year as we've seen things come about largely
[1088.26 → 1093.80] from that cross-pollination of different technologies that have arisen on different paths.
[1093.90 → 1097.24] But now they're getting blended, and some pretty cool things are coming out of it.
[1097.54 → 1097.72] Yeah.
[1097.72 → 1104.42] So the Stable Diffusion model, if you were kind of having your mind, and we can't show
[1104.42 → 1109.44] you a picture because this is an audio podcast, but if you have in your mind going from a text
[1109.44 → 1119.36] input to an image output, the sort of general process is that that text is embedded into some
[1119.36 → 1120.10] representation.
[1120.10 → 1126.02] That embedding plus some noise is then denied to an image.
[1126.56 → 1134.18] And that image is then upscaled or decoded into a larger image that's not compressed.
[1134.66 → 1138.14] So those are the general stages of the pipeline.
[1138.14 → 1145.76] You've got text embedded plus random noise, denied, and then decoded or upscaled to an image.
[1146.06 → 1150.12] Do you want to take a moment and let's just kind of talk about, for those who are kind
[1150.12 → 1154.62] of coming into it, the idea of introducing noise and then denoting, what do you get out
[1154.62 → 1155.60] of that productively?
[1155.66 → 1155.90] Yeah.
[1156.00 → 1157.38] What's the reason for that in the workflow?
[1157.60 → 1157.86] Yeah.
[1158.02 → 1163.94] So, I mean, you can think about, it doesn't have to be a text to image model, but this
[1163.94 → 1170.42] sort of denoting or diffusion type model is useful because it can take a sort of noisy
[1170.42 → 1172.62] input and Denise it.
[1172.76 → 1179.12] So the sort of bigger idea here is that I could take a set of images in my training set, right?
[1179.12 → 1187.58] And then introduce noise into those images via certain steps of noising.
[1187.58 → 1195.54] And then I could train my model to, in a series of steps, Denise those images.
[1196.24 → 1202.20] And so this could be used both for like fixing corrupted images or upscaling images and that
[1202.20 → 1202.74] sort of thing.
[1202.82 → 1208.08] So it doesn't have to be for like text to image, but this is the general idea is that you have
[1208.08 → 1216.96] an original output or original set of images that you can kind of corrupt intentionally.
[1216.96 → 1221.30] And then train your model to corrupt those or Denise them.
[1221.96 → 1230.68] And then that model can be used to perform that sort of denoting or upscaling type of
[1230.68 → 1232.92] action afterwards.
[1233.50 → 1238.10] As we talk about, you know, the fact that attention is used in here, and I know in some of the
[1238.10 → 1241.24] discussions about it, it's referred to as cross attention.
[1241.82 → 1244.90] What is cross attention as a form of attention?
[1244.90 → 1248.92] Does that just mean different modalities coming in, or how would you define that?
[1249.24 → 1249.46] Yeah.
[1249.68 → 1255.88] So I think it would be good with that to kind of describe the maybe the overall components
[1255.88 → 1258.50] or modules of this system.
[1258.68 → 1265.54] So there are three main components of Stable Diffusion to like to make it what it is.
[1265.54 → 1272.74] The first is text encoder or a language model that takes your text and converts it into an
[1272.74 → 1276.64] embedded representation and or encodes that text.
[1276.80 → 1279.80] The next major component is an auto encoder.
[1280.20 → 1284.80] We'll come back to that because this is a key piece of what makes Stable Diffusion different
[1284.80 → 1286.46] is what they did with the auto encoder.
[1286.46 → 1294.22] But the auto encoder, basically, you can think about it as a way to train something to upscale
[1294.22 → 1294.82] your image.
[1295.00 → 1299.24] So to go from a compressed image to a non-compressed image.
[1299.86 → 1305.62] And then the third is this diffusion model, which is a UNIT model.
[1305.98 → 1308.90] This is the type of architecture it is, a UNIT model.
[1309.30 → 1313.58] And this is that model that takes a noisy input and then denotes it.
[1313.58 → 1319.62] So again, the text encoder encodes your text to an embedded representation, just a series
[1319.62 → 1322.34] of numbers, series of floating point numbers.
[1322.74 → 1329.62] Your auto encoder is a way to really a way to get to a decoder, which can decompress images
[1329.62 → 1330.80] or upscale them.
[1331.28 → 1336.66] And then your diffusion model, which is based on this UNIT architecture, which takes Gaussian
[1336.66 → 1345.42] noise or some noise and denotes it to get closer to the text representation that you input.
[1345.82 → 1347.50] So those are the three main components.
[1347.88 → 1354.82] And what happens is that we mentioned this diffusion model that takes noise and denotes
[1354.82 → 1357.82] it to something that's close to your text representation.
[1357.82 → 1363.06] Well, somehow you have to combine that noise and your text representation.
[1363.06 → 1369.42] So if you imagine text comes in to your text encoder or language model, that's converted
[1369.42 → 1375.26] to a series of numbers and embedding, a learned embedding for that text.
[1375.46 → 1380.70] And then that learned embedding is combined with this random noise.
[1380.84 → 1382.80] And that's where the cross attention happens.
[1382.94 → 1392.50] So cross attention is this way of mapping your text representation, your encoded text onto this
[1392.50 → 1397.38] random noise, which the word that they use for this is condition.
[1397.38 → 1402.06] It conditions the random noise with your text representation.
[1402.94 → 1409.66] And that's how the diffusion model, which denotes it, that's how it knows what it's kind of after.
[1409.86 → 1419.12] That's how it gets to a semantically relevant image that's relevant to your text input is because
[1419.12 → 1425.30] it's been combined with your text embedding in this cross attention mechanism and the random noise.
[1425.72 → 1428.44] And the diffusion model is a form of convolutional model.
[1428.56 → 1429.12] Is that accurate?
[1429.42 → 1435.98] Yeah, the diffusion model, at least the one that was used in this Stable Diffusion piece is called UNIT.
[1435.98 → 1444.74] It's not it's used in for other purposes as well, but it is sort of has a series of convolutional layers.
[1444.98 → 1454.90] One that kind of takes your image and shrinks the image down in the convolutions and one that does the inverse of that.
[1454.98 → 1457.48] So this is like a down path up path thing.
[1457.48 → 1460.84] And then there are combinations between those two things.
[1460.96 → 1466.48] But yeah, it's its it's a series of convolutions that are combined in a certain way, which makes it UNIT.
[1467.28 → 1473.94] You know, it's its interesting as you have kind of catalogued these different components in their workflow.
[1473.94 → 1478.24] And we have talked about all of these things in previous episodes.
[1478.24 → 1485.96] These are all existing technologies, but they had they found a way to put them together to a remarkable effect.
[1485.96 → 1496.14] And it's very interesting that we keep returning to that cross modality being, you know, kind of the source of the current wave of creativity in the AI space.
[1496.34 → 1498.42] And I think this is a great example.
[1498.42 → 1504.98] Individually, I know what all those things are, would never have imagined putting them together to achieve this.
[1505.24 → 1508.14] So it was a pretty, pretty cool way of doing this.
[1508.14 → 1525.24] Yeah. And I think that the key piece to emphasize about what was done here is really with the piece that we kind of glossed over quickly, which is this auto encoder and particularly how they trained both the diffusion model and the auto encoder.
[1525.24 → 1533.92] So it's not new to use this sort of auto encoder to compress and decompress images that that's been done before.
[1533.92 → 1544.42] If you imagine you have a model that can encode an image and then decode it, the encoding is sort of like the compressing of that image.
[1544.42 → 1547.06] The decoding is the decompressing of that image.
[1547.06 → 1558.06] And so you can train a model, you can train an encoder and a decoder jointly to do that compression and then do a corresponding decompression or decoding.
[1558.36 → 1563.94] And then the diffusion model sort of operates in that on those compressed images.
[1564.18 → 1568.50] So this is not new, this sort of combination of auto encoder and diffusion model.
[1568.50 → 1582.52] In my understanding, what is new is that the Stable Diffusion team, this team from stability and the group in Germany, I'll mention some of their names because Robin Ram bach et al.
[1582.82 → 1583.56] Are on the paper.
[1583.76 → 1585.30] We'll link in the show notes.
[1585.96 → 1592.96] But the thing that they wanted to do, remember, the motivation that they were after was to make a more computationally efficient diffusion model.
[1592.96 → 1596.52] That was at least one of the accessibility things they were after.
[1596.72 → 1608.52] And so what they did was instead of jointly training the auto encoder and the diffusion model, they separately trained the auto encoder and the diffusion model.
[1608.70 → 1619.82] And this does two things sort of it separates out the auto encoder and lets you train the auto encoder for what it needs to be good at, which is compressing and decompressing images.
[1619.82 → 1628.50] But it also means that the diffusion model only operates on these compressed images in the training.
[1628.50 → 1649.50] And those compressed images require like 64 times less memory for your diffusion model, which is why you can run the Stable Diffusion model on a consumer GPU card, because they've strategically separated out the training of this auto encoder and the diffusion model.
[1649.82 → 1661.66] Which allows the diffusion model to operate on compressed images, but still allows you to get high quality upscaled images out because you're using the decoder still.
[1662.06 → 1665.06] And we've seen the decoder and encoder being used.
[1665.14 → 1667.66] I mean, I think you see that in typical graphics software.
[1668.04 → 1668.18] Right.
[1668.48 → 1670.42] Or machine translation models.
[1670.80 → 1671.06] Exactly.
[1671.06 → 1671.76] All sorts of things.
[1671.90 → 1672.04] Yeah.
[1672.26 → 1673.88] It's used often to clean that up.
[1673.88 → 1681.38] So the diffusion model is kind of where, if I'm understanding you correctly, is kind of going through that noising and then denoting.
[1681.70 → 1686.30] It kind of blends what is available from the trained model together.
[1686.52 → 1689.00] And then in that compressed format.
[1689.00 → 1702.52] And then when the decoder takes the result of that and kind of upscales it back to the uncompressed model, it kind of, in a very non-technical phrase, it kind of cleans it up and makes it, you know, what it is at that point.
[1702.52 → 1705.82] Is that close to being how, is that approximately fair?
[1705.82 → 1706.26] Yeah.
[1706.40 → 1715.50] So if you can imagine tiny images, which are generated out of random noise based on the diffusion model, denoting that noise.
[1715.62 → 1715.82] Yeah.
[1715.92 → 1729.92] Then those tiny images are then decoded to a larger image, which is inferred, which uses this separately trained decoder, which was trained in this sort of autoencoder methodology.
[1729.92 → 1732.28] I have a question, a random question for you.
[1732.62 → 1745.82] Given that they're training them kind of as these separate components, does that potentially, if I'm thinking in terms of outside this space and software, we often mix different components together to achieve new things.
[1745.88 → 1754.60] Do you think that'll help accelerate some of the exploration and experimentation in this by keeping those bits separate so that you combine them as you want?
[1754.60 → 1775.46] Yeah. Well, I think that there's the clear computational advantage, but I think as an additional advantage, basically separating out this encoder or the autoencoder from the diffusion model makes it to where you can use the same autoencoder model for all sorts of different downstream diffusion models.
[1775.46 → 1783.12] So this is another kind of shift that we've seen in other areas, right, where a portion of what you're doing is general purpose.
[1783.40 → 1798.24] And then you're kind of bolting on what you need for the downstream tasks that you care about, whether that be image to image sort of tasks or text to image tasks, or maybe even another thing that would be like a text to audio task.
[1798.24 → 1802.24] Or there are all sorts of different things that you could imagine doing downstream.
[1802.24 → 1806.18] So, yeah, I think that this decouples the two.
[1806.18 → 1807.78] There's a computational advantage.
[1807.78 → 1811.00] There's also a sort of functional advantage.
[1828.24 → 1844.32] Well, Chris, I think one last thing to mention in terms of in the weeds stuff is I think it is fascinating to look at how a model was trained.
[1844.86 → 1851.58] So it's probably worth mentioning a couple of those things where this model, again, was trained in two distinct phases.
[1851.58 → 1863.28] There's this universal autoencoding stage, which is trained once and can be utilized for multiple diffusion models, model trainings downstream.
[1863.60 → 1867.74] And then there's the second phase, which is actually training the diffusion model.
[1867.74 → 1876.58] And this model was trained on approximately 120 million image text pairs.
[1876.58 → 1885.42] So there were, well, there were 120 million image text pairs from approximately 6 billion image text pair data set.
[1885.92 → 1890.34] That data set is freely accessible that you can look at that as well.
[1890.46 → 1892.72] And we'll link it in our show notes.
[1892.72 → 1904.00] But I think we also talked last in our last conversation about how it wasn't, I mean, it's expensive, but it wasn't a crazy number to actually train this model.
[1904.00 → 1914.50] So it took 256 A100s, about 150K hours, which would kind of equal at least at market price around 600K.
[1914.66 → 1918.60] And I'm getting that from one of the team members on Twitter.
[1919.02 → 1920.94] So, yeah, pretty interesting.
[1921.58 → 1933.52] I mean, I don't know if you have 600K lying around, Chris, but it's certainly a more accessible number than like, you know, training a model for 500 million or, you know, something.
[1933.52 → 1937.00] And no, I don't have the pocket change of 600K lying around.
[1937.18 → 1947.66] But, you know, as we're looking at separating these trainings out and the fact that, you know, if you kind of think, you know, we talked a little bit about the idea of the magic arising out of this earlier.
[1947.66 → 1958.58] And the fact that, you know, you have so much human semantics captured in the diffusion model, you know, in terms of how it was trained.
[1958.76 → 1960.36] So there are many concepts.
[1960.56 → 1965.04] You know, we talked earlier about the Gandalf Yoda imagery that we had seen.
[1965.04 → 1971.90] And clearly the training had included, you know, the concept of Yoda and the concept of Gandalf that were combined.
[1971.90 → 1993.08] As we go forward, do you think there is the idea of kind of diffusion marketplace that arises, both open source and maybe some not open source, where depending on the cost that you want and things like that, you can kind of get into the level of sophistication that you can support for your application.
[1993.56 → 2000.98] Do you think that becomes a reality as we talk about making these accessible across a wide range of users and use cases?
[2000.98 → 2020.02] Yeah, I mean, I think if you draw a parallel with what's happened with other models that have caught on in similar ways, like if you imagine back to BERT and these large language models, part of the magic of those was that the weights were open source.
[2020.20 → 2024.86] You could pull down a pre-trained version and then fine tune it for a particular task, right?
[2024.86 → 2036.18] So I have no doubt that, and I think people are looking into this and there are explicit notes on the Stable Diffusion page about limitations and bias and all that.
[2036.24 → 2037.70] So you can read that there.
[2037.82 → 2041.80] But certainly there's bias in the data set on which it was trained.
[2041.80 → 2053.26] But I think the power comes is if you're able to open source the model in some sort of way with tooling that will allow for the fine-tuning of it.
[2053.26 → 2076.92] I'm sure that people will sort of fine tune or create different versions based off of the parent using maybe it's imagery for particular styles of books or publications or imagery for or in painting for, you know, creative arts or for video processing or for all of these different things.
[2076.92 → 2091.50] I think people will create their own versions of these and probably some of them will be those fine tune kind of purpose built models will be commercially available for purchase, as we've seen with language, certain language models in the marketplace.
[2091.50 → 2097.82] And some will be open source for people's usage, just like we've seen kind of a general purpose BERT.
[2097.96 → 2104.84] And then we've got like a science document BERT, and we've got a legal document BERT and these sorts of things.
[2104.84 → 2106.00] And those are open.
[2106.12 → 2118.14] But also there are companies that are, you know, making money because they're processing legal documents with BERT, and they're using they have their own proprietary version, or maybe they're using the open source version and just have good tooling around it.
[2118.14 → 2132.34] So to extend kind of your answer there just a little bit, you know, one of the things that we often ask guests when we have guests on the show is kind of that, you know, wax poetic a little bit and tell us, you know, kind of where you see some of these things going.
[2132.34 → 2143.46] And I know that as we were diving into this topic for today's show and kind of exploring what we want to share with the audience, I could see so many possibilities, as could you.
[2143.94 → 2149.84] And so let's wax poetic for a few minutes on where this might go and what might come down the road.
[2150.20 → 2156.14] You talked a little bit about the marketplace of, you know, where people can find resources to move forward.
[2156.14 → 2173.72] With these technologies, one of the first things that I thought about was we were just talking in the last episode or two about how artists, you know, were getting frustrated with the fact that you would have machine learning practitioners come in and creating art with these things and all that.
[2173.78 → 2177.86] And that's in a very immediate you can do it today kind of situation.
[2177.86 → 2193.62] But it's as we've watched these multi-modality evolutions coming through these models over the months, it's not hard to envision that at some point down the road, this will move into video, and we'll see other modalities being added to it.
[2193.90 → 2196.94] I think that would be consistent with the recent history that we've seen.
[2197.30 → 2206.26] And as we do that, it really you're now moving into that creative space that previously it took a great deal of effort.
[2206.26 → 2226.52] You know if we're talking about the entertainment industry and movie making and special effects since we started with the Lord of the Rings, this could really revolutionize how special effects are cheap and make some amazingly phenomenal special effects as we see iterations going forward become very accessible to people at home.
[2226.52 → 2232.96] You know, you're no longer you're no longer the big special effects company, but you're, and those companies would have access to.
[2233.56 → 2235.32] But I could see so many industries.
[2235.32 → 2238.18] There's obviously there's security concerns.
[2238.32 → 2239.62] There's art things.
[2239.62 → 2240.66] There are business things.
[2240.90 → 2251.56] What are some of what are some of what ifs that you could see, maybe not just with this particular model, but with what we might expect to see not too far down the road?
[2252.12 → 2259.72] Yeah, I think the two areas that I am thinking about are one, the expansion of modalities like you talked about.
[2259.72 → 2274.72] So diffusion models applied to audio, for example, and what that means for both things like speech synthesis or even creative things like music generation or that sort of thing.
[2274.72 → 2280.16] So I think that that that area is quite interesting to me and I think it will happen.
[2280.16 → 2294.82] But the other what if in my mind is how this set of technologies will be combined with others that we've seen to be very powerful already that already exists.
[2294.82 → 2304.38] So, for example, I could have a dialogue system, or I could have prompts that were not created by me and fed into Stable Diffusion.
[2304.38 → 2325.48] But what if I create a prompt using GPT-3 or automate the sort of dialogue I'm having in a chatbot, right, with language model generated prompts along with imagery or video that's created using something like Stable Diffusion?
[2325.48 → 2337.14] Or, you know, you could even imagine creating a storybook with both, you know, language models and sort of visual elements from something like Stable Diffusion.
[2337.94 → 2351.02] So I think that the sort of creativity or the uses are also interested in how they are integrated with existing technologies, both that are AI related and maybe not AI related.
[2351.02 → 2360.16] So things like chatbots could be driven by an AI model, like a dialogue system model that's state of the art.
[2360.28 → 2366.10] They could also just be like decision tree based, you know, bots that are rule based.
[2366.10 → 2371.24] But maybe you integrate visual elements from something like this that in a more controlled way.
[2371.24 → 2387.06] So I think that this combination of the technology with both existing technologies and other language models, other models that are out there is an area that I think will kind of expand quite a bit, and we'll see some interesting things happen.
[2387.06 → 2405.34] I think we're looking at the birth of a kind of creative entrepreneurship, being able to really take some of this model and other recent models and some of the new things that we expect to come in the not so distant future and really have some amazing creative outputs on that.
[2405.76 → 2407.06] You know, we started with Lord of the Rings.
[2407.06 → 2412.54] And so I'll, I'll, I'll make a suggestion to the Tolkien business, if you will.
[2412.96 → 2420.46] You know, it would be interesting to see maybe in a few years when they've decided they need to refresh those stories again.
[2420.92 → 2427.48] Maybe it's done with some of these technologies, and it's done, you know, kind of entirely with the set of creative technologies.
[2427.48 → 2437.28] And to your point, maybe it is released in many, many languages simultaneously kind of native instead of being translated, you know, in that capacity.
[2437.28 → 2449.28] And so we can all share in that experience and maybe even variations to adapt to different cultures and different all sorts of different races, cultures and everything.
[2449.28 → 2455.78] And stories can be you can take a storyline and make it pretty special in terms of being multimodal itself.
[2455.78 → 2459.20] So I can imagine a lot of pretty cool things.
[2459.86 → 2482.58] Yeah, I always think back to that conversation we had with Jeff Adams from the Cobalt Speech company talking about how, you know, his vision for the future also was this sort of more holistic, holistic treatment of both language and other things because language touches everything.
[2482.58 → 2493.04] So I think that that's some of of what you're you're meaning while you were talking just to kind of show you how accessible things are.
[2493.16 → 2497.96] I typed into Stable Diffusion map of the USA and Lord of the Rings style.
[2498.76 → 2509.46] And there's definitely I'm sure you'll recognize certain elements of that map that I just posted on our Slack channel, Chris, that are Lord of the Rings ask.
[2509.64 → 2510.84] So pretty interesting.
[2510.84 → 2513.60] I actually I there's a there's a book.
[2513.84 → 2518.68] I don't remember what it's called right now, but there's a book of Lord of the Rings of Middle Earth maps.
[2519.06 → 2525.36] And it does remind so it's the US that we're, you know, the eastern and central US that we're looking at here.
[2525.44 → 2529.26] But it definitely has that that Lord of the Rings style going to it.
[2529.32 → 2532.86] So, yeah, that I'm enjoying that.
[2532.86 → 2541.66] Yeah. In terms of learning resources for people, I think what Chris and I would recommend that you do is just get hands on with this model.
[2541.66 → 2542.96] There are ways to do it.
[2543.02 → 2551.02] Even if you don't code, there are ways to do it through the Dream Studio dot AI app or on Hugging Face.
[2551.02 → 2557.04] You can actually download the model and use their diffusers' library to run the model.
[2557.18 → 2561.00] If you search for Stable Diffusion on Hugging Face, you can find it.
[2561.00 → 2563.12] Also, another post.
[2563.56 → 2575.60] So we'll put this in our show notes, but we leveraged a blog post, which was quite useful, written by Mark Popper that described a lot of the things that we talked about here.
[2575.60 → 2582.26] So if you want some visuals and that sort of thing to aid your understanding of the model, we'll link that in our show notes.
[2582.50 → 2583.96] So definitely take a look.
[2584.04 → 2588.76] It's been fun to diffuse some of these ideas with you, Chris.
[2588.96 → 2589.96] Enjoyed it very much.
[2590.18 → 2590.62] I did, too.
[2590.72 → 2595.68] I hope our audience enjoyed this as much with these shows where we get to explore bold new places.
[2595.96 → 2597.52] I really get excited about.
[2597.64 → 2602.58] So until I'm sure there'll be something super cool coming up that we'll be talking about again.
[2602.58 → 2604.98] But until then, thanks for joining today, Daniel.
[2604.98 → 2605.72] Bye.
[2628.64 → 2632.20] Word of mouth is the number one way people find shows like ours.
[2632.36 → 2634.90] Thanks again to Vastly for fronting our static.
[2634.98 → 2635.48] Assets.
[2635.72 → 2638.18] To fly.io for backing our dynamic requests.
[2638.72 → 2640.24] To Break master Cylinder for the beats.
[2640.52 → 2641.44] And to you for listening.
[2641.68 → 2642.34] We appreciate you.
[2642.66 → 2643.52] That's all for now.
[2643.74 → 2645.24] We'll talk to you again on the next one.
[2656.98 → 2658.78] Game on.
[2658.78 → 2666.42] Game on.
[2666.42 → 2676.16] Zwickau trust.
