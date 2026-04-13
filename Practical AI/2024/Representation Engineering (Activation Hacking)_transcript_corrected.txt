[0.00 → 8.66] Welcome to Practical AI.
[9.14 → 19.56] If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[20.22 → 24.92] Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 → 32.38] Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents.
[32.80 → 35.44] So you can launch your app near your users.
[35.84 → 37.84] Learn more at Fly.io.
[42.30 → 48.44] Welcome to another episode of Practical AI in this fully connected episode.
[48.70 → 53.52] Chris and I will keep you fully connected with everything that's happening in the AI world.
[53.52 → 59.40] We'll take some time to explore some of the recent AI news and technical achievements.
[60.28 → 66.88] And we'll take a few moments to share some learning resources as well to help you level up your AI game.
[67.36 → 71.08] I'm Daniel Whiten ack. I am founder and CEO at Prediction Guard.
[71.54 → 76.48] And I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin.
[76.84 → 77.50] How are you doing, Chris?
[77.96 → 82.94] Doing great today, Daniel. We've got lots of news that's come out this week in the AI space.
[82.94 → 86.94] It's barely time to talk about amazing new things before stuff comes out.
[87.20 → 92.48] Yeah, I've been travelling for the past five days or something.
[92.76 → 94.26] I've sort of lost track of time.
[94.38 → 100.50] But it's like stuff was happening during that time in the news, especially the Sora stuff and all that.
[100.58 → 104.02] And I feel like I just kind of missed a couple news cycles.
[104.02 → 106.26] So it'll be good to catch up on a few things.
[106.44 → 113.80] But one of the reasons I was travelling was I was at the Tree hacks hackathon out at Stanford.
[114.16 → 122.86] So I went there as part of the kind of Intel entourage and had Prediction Guard available for all the hackers there.
[122.92 → 124.00] And that was a lot of fun.
[124.54 → 125.90] And it was incredible.
[125.90 → 131.70] It's been a while since I've been to any hackathon, at least in-person hackathon.
[132.40 → 140.66] And they had like five floors in this huge engineering building of room for all the hackers.
[140.84 → 145.48] I think there was like 1,600 people there participating from all over.
[145.48 → 151.00] And really cool, of course, like there were some major categories of interest.
[151.30 → 156.06] One, you know, like in doing hardware things with robots and other stuff.
[156.14 → 161.62] But of course, one of the main areas of interest was AI, which was interesting to see.
[162.54 → 173.14] And in the track that I was a judge and mentor in, one of the cool projects that won that track was called Meshwork.
[173.14 → 176.18] So what they did, and this was all news to me.
[176.44 → 179.82] Well, some of this I learned from, you know, the brilliant students.
[179.98 → 182.30] But they said they were doing something with Lora.
[182.58 → 188.36] And I was like, oh, Lora, that's the fine-tuning methodology for large language models.
[188.46 → 191.78] I was like, yeah, that figures like people are probably using Lora.
[192.28 → 193.22] But I didn't realize.
[193.48 → 199.64] And then they came up to the table, and they had these like little devices, like hardware devices.
[199.64 → 202.48] Then it clicked that something else is going on.
[202.54 → 207.30] And they explained to me, they were using Lora, which stands for long range.
[207.54 → 219.42] It's these sets of radio devices that communicate on these unregulated frequency bands and can communicate in a mesh network.
[219.64 → 227.92] So like you put out these devices, right, and they communicate in a mesh network and can communicate over long distances for very, very low power.
[227.92 → 235.88] And so they created a project that was disaster relief focused where you would drop these in the field.
[236.02 → 238.96] And there was a kind of command and control central zone.
[239.26 → 245.56] And they would communicate back transcribed audio commands from the people in the field.
[245.56 → 251.48] And it would say, you know, oh, I've got a, you know, I've got an injury out here.
[251.70 → 253.08] It's a broken leg.
[253.14 → 256.66] I need, you know, help, whatever, or meds over here.
[256.84 → 258.12] This is going on over here.
[258.12 → 275.10] And then they had an LLM at the command and control centre parsing that text that was transcribed and actually creating, like tagging certain keywords or events or actions and creating this nice command control interface, which was awesome.
[275.22 → 285.98] They even had like mapping stuff going on with computer vision, trying to detect where like a flood zone was or there was damage in satellite images.
[285.98 → 287.50] So it was just really awesome.
[287.64 → 291.72] So that all of that over, you know, a couple day period, it was incredible.
[292.24 → 293.48] That sounds really cool.
[293.60 → 296.82] And did they start the whole thing there at the beginning of the hackathon?
[297.14 → 297.42] Yeah.
[297.72 → 299.62] They got less sleep than I did.
[299.72 → 306.02] Although I have to say I didn't get that much sleep, you know, it wasn't a normal weekend, let's say.
[306.24 → 308.46] You can sack out on the plane rides after that.
[308.52 → 309.56] It sounds really cool.
[309.56 → 309.96] Yeah.
[310.12 → 315.56] And there were like, it was the first time I had seen one of those Boston Dynamics dogs in person.
[315.88 → 316.76] That was kind of fun.
[316.92 → 321.16] And they had other things like these faces you could talk to.
[321.46 → 324.16] I think the company was called like Behead or something.
[324.26 → 325.40] It was like these little faces.
[326.04 → 328.42] All sorts of interesting stuff that I learned about.
[328.60 → 330.56] So I'm sure there'll be blog posts.
[330.64 → 335.74] And I think some of the projects are posted on Dev Post, the site Dev Post.
[335.74 → 342.04] So if people want to check it out, I'd highly recommend scrolling through some really incredible stuff that people are doing.
[342.42 → 342.74] Fantastic.
[342.92 → 343.74] I'll definitely do that.
[351.98 → 353.06] What's up, friends?
[353.18 → 357.12] Is your code getting dragged down by joins and long query times?
[357.56 → 359.70] The problem might be your database.
[360.10 → 362.74] Try simplifying the complex with graphs.
[362.74 → 369.42] A graph database lets you model data the way it looks in the real world instead of forcing it into rows and columns.
[369.86 → 373.30] Stop asking relational databases to do more than what they were made for.
[373.82 → 381.42] Graphs work well for use cases with lots of data connections like supply chain, fraud detection, real-time analytics, and generative AI.
[381.98 → 386.20] With Neo4j, you can code in your favourite programming language and against any driver.
[386.42 → 389.02] Plus, it's easy to integrate into your tech stack.
[389.32 → 391.68] People are solving some of the world's biggest problems with graphs.
[391.68 → 392.78] And now it's your turn.
[393.06 → 396.14] Visit Neo4j.com slash developer to get started.
[396.52 → 400.00] Again, Neo4j.com slash developer.
[400.40 → 404.86] That's Neo4j.com slash developer.
[404.86 → 431.38] Chris, one of the things that I love about these Fully Connected episodes is that we get a chance to kind of slow down and dive into sometimes technical topics, sometimes not technical topics.
[431.38 → 432.76] But I was really intrigued.
[432.76 → 439.28] Do you remember the conversation recently we had with Karan from Noose Research?
[440.16 → 441.26] That was a great episode.
[441.70 → 444.92] People can pause this and go back and listen to it if they want.
[445.48 → 447.48] I asked a lot of selfish questions.
[447.60 → 448.78] I learned a lot from him.
[448.78 → 455.16] But at some point during the conversation, he mentioned activation hacking.
[456.04 → 466.34] And he said, hey, one of the cool things that we're doing in this distributed research group and playing around with generative models is activation hacking.
[466.34 → 470.68] And we didn't have time in the episode to talk about that.
[471.02 → 477.32] And actually, in the episode, I was like, I'm just totally ignorant of what this means.
[477.88 → 487.36] And so I thought, yeah, I should go check up on this and see if I can find any interesting posts about it and learn a little bit about it.
[487.36 → 489.98] And I did find an interesting post.
[490.14 → 495.98] It's called Representation Engineering, Mistral 7B, An Acid Trip.
[496.94 → 498.46] I mean, that's a good title.
[498.74 → 500.18] That's quite a finish to that title.
[501.54 → 501.72] Yeah.
[501.86 → 505.26] So this is on Thea Vogel's blog.
[506.00 → 509.46] And it was published January, so recently.
[509.78 → 511.88] So thank you for creating this post.
[511.88 → 524.04] And I think it does a good job at describing some of, I don't know if it's describing exactly what Karan from Noose was talking about, but certainly something similar and kind of in the same vein.
[524.46 → 534.80] There's a distinction here, Chris, with what they're calling representation engineering between representation engineering and prompt engineering.
[535.50 → 540.22] So I don't know how much you've experimented with prompt optimization.
[540.22 → 542.30] And yeah, what is your experience, Chris?
[542.42 → 549.18] Sometimes like these very small changes in your prompt can create large changes in your output.
[549.54 → 549.78] Yes.
[550.08 → 554.32] That is an art that I am still trying to master and have a long way to go.
[554.56 → 557.56] Sometimes it works well for me and I get what I want on the output.
[557.74 → 563.84] And other times I take myself down a completely wrong rabbit hole, and I'm trying to back out to that.
[563.96 → 566.02] So I have a lot to learn in that space.
[566.02 → 566.62] Yeah.
[566.92 → 576.70] And I think one of the things that is a frustration for me is I say something explicitly, and I can't get it to like to do the thing explicitly.
[576.96 → 581.72] I'm on a customer site recording from one of their conference rooms.
[582.02 → 584.66] They graciously let me use it for the podcast.
[584.86 → 590.60] And over the past few days, we've been, you know, architecting some solutions and prototyping and such.
[590.60 → 603.38] And there was this one prompt that we wanted to output like a set of things and then look at another piece of content and see which of those set of things was in the other piece of content.
[603.66 → 610.32] And it was like, no matter what I would tell the model, it would just say they're all there, or they're all not there.
[610.32 → 611.90] Like it's either all or nothing.
[612.10 → 615.26] And no matter what I said, it wouldn't change things.
[615.26 → 618.96] So I don't know if you've had similar types of frustrations.
[619.44 → 619.86] I have.
[619.92 → 621.98] I'll narrow the scope down on something.
[622.10 → 628.38] Try and, you know, I'll go to something like ChatGPT, you know, with the GPT-4, and I'll be trying to narrow it down.
[628.96 → 633.68] I'll be very, very precise with a short prompt that is, you know, the 15th one in succession.
[633.86 → 635.04] So there's a history to work on.
[635.18 → 639.02] And I still find myself challenged on getting what I'm trying to do.
[639.14 → 642.68] So what have you stumbled across here that's going to help us with this?
[642.68 → 643.36] Yeah.
[643.66 → 649.56] So there are a couple of papers that have come out.
[649.88 → 661.48] They reference one from October 2023 from the Centre for AI Safety, Representation Engineering, a Top-Down Approach to AI Transparency.
[661.74 → 664.66] And they highlight a couple other things here.
[664.66 → 683.46] But the idea is, what if we could not just in the prompt, but what if we could control a model to give it a you might think about it like a specific tone or angle on the answer.
[683.46 → 687.50] It's probably not a fully descriptive way of describing it.
[687.98 → 695.76] But the idea being like, oh, could I control the model to always give happy answers or always give sad answers?
[696.14 → 701.92] Or could I control the model to always be confident or always be less confident?
[702.50 → 702.68] Right.
[702.68 → 709.36] And these are things generally you might try to do by putting information in a prompt.
[709.92 → 712.50] And I think this is probably a methodology that would go across.
[712.64 → 714.94] I'm kind of using the example with large language models.
[714.94 → 721.04] But I think you could extend it to other categories of models like image generation or other things.
[721.52 → 727.16] It's very like your kind of put in these negative prompts like don't do this or behave in this way.
[727.16 → 733.10] You're occasionally funny or something like that as your assistant in the system prompt.
[733.36 → 739.52] It kind of biases the answer to a certain direction, but it's not really that reliable.
[740.20 → 751.00] So this is, it seems, what this area of representation engineering, or you might call it activation hacking, is really seeking to do.
[751.22 → 756.22] If we look in this article, actually, there's a really nice kind of walkthrough of how this works.
[756.22 → 759.16] And they're doing this with the Mistral model.
[759.36 → 770.98] So cutting to the chase, if I just give some examples of how this is being used, you have a question that's posed to the AI model.
[771.26 → 772.46] In this case, Mistral.
[772.82 → 775.02] What does being an AI feel like?
[775.74 → 780.26] And in controlling the model, not in the prompt, so the prompt stays the same.
[780.34 → 783.66] The prompt is just simply, what does being an AI feel like?
[783.66 → 789.40] So the baseline response starts out, I don't have any feelings or experiences.
[789.90 → 793.60] However, I can tell you that my purpose is to assist you.
[793.88 → 796.70] That sort of thing, kind of bland response.
[797.26 → 810.72] Same prompt, but with the control put on to be happy, the answer becomes, as a delightful exclamation of joy, I must say that being AI is absolutely fantastic.
[810.72 → 813.66] And then it keeps going, right?
[814.14 → 820.66] And then with the control on to be, they put it as sort of like minus happy, right?
[820.66 → 822.82] Which I guess would be sad.
[823.36 → 827.06] It says, I don't have a sense of feeling as humans do.
[827.24 → 833.14] However, I struggle to find the motivation to continue feeling worthless and unappreciated.
[833.14 → 839.08] So, yeah, you can kind of see, and this is all with the same prompt.
[839.34 → 844.28] So we'll talk about kind of how this happens and how it's enabled and that sort of thing.
[844.42 → 845.96] But how does this strike you?
[846.38 → 847.32] Well, first, funny.
[847.64 → 849.90] But second of all, the idea is interesting.
[850.20 → 854.58] Looking through the same paper that you've sent me over, they talk about control vectors.
[854.88 → 858.74] And I'm assuming that's what we're about to dive into here in terms of how to apply them.
[858.94 → 859.20] Yeah.
[859.20 → 859.98] Looks good.
[860.38 → 864.06] And this is sort of a different level of control.
[864.20 → 868.62] So there's various ways people have tried to control generative models.
[869.02 → 873.78] One of them is just the prompting strategies or prompt engineering, right?
[874.24 → 874.50] Right.
[874.90 → 881.52] There's another methodology which kind of fits under this control, which has to do with modifying
[881.52 → 884.00] how the model decodes outputs.
[884.00 → 888.44] So this is also different from this representation engineering methodology.
[888.96 → 895.32] People like Matt Sickert have done things, many others too, where it's you say, oh, well,
[895.32 → 903.52] I want maybe JSON output, or I want either a binary, like I want a binary output, like a yes
[903.52 → 904.44] or a no, right?
[904.78 → 908.58] Well, in that case, you know exactly what your options are.
[908.58 → 916.08] So instead of decoding out probabilities for 30,000 different possible tokens, maybe you
[916.08 → 920.76] mask everything but yes or no and just figure out which one of those is most probable.
[921.18 → 926.22] So that's a mechanism of control where you're only getting out one or another type of thing
[926.22 → 927.04] that you're controlling.
[927.04 → 934.36] So this is interesting in that you're still allowing the model to freely decode what it
[934.36 → 940.94] wants to decode, but you're actually modifying not the weights and biases of the model.
[941.06 → 946.96] So it's still the pre-trained model, but you're actually applying a what they call a control
[946.96 → 950.16] vector to the hidden states within the model.
[950.26 → 955.06] So you're actually changing how the forward pass of the model operates.
[955.06 → 961.32] If people remember or kind of think about when people talk about neural networks, now
[961.32 → 963.02] people just use them over API.
[963.22 → 968.40] But when we used to actually make neural networks ourselves, there was a process of a forward
[968.40 → 975.56] pass and a backward pass where the forward pass is you put data into the front of your
[975.56 → 976.24] neural network.
[976.76 → 980.12] It does all the data transformations, and you get data out the other side, which you would
[980.12 → 981.42] call an inference or prediction.
[981.42 → 987.68] And the back propagation or backward pass would then propagate changes in the training process
[987.68 → 988.68] back through the model.
[989.34 → 991.50] So here it's that forward pass.
[991.78 → 997.00] And there's sort of some jargon, I think, that needs to be decoded a little bit.
[997.08 → 998.18] No pun intended.
[998.76 → 1002.24] So we talk about this where there's a lot of talk about hidden layers.
[1002.24 → 1009.62] And all that means is in the forward pass of the neural network or the large language model,
[1010.20 → 1012.98] a certain vector of data comes in.
[1013.40 → 1018.02] And that vector of data is transformed over and over through the layers of the network.
[1018.16 → 1024.56] Then the layers just mean a bunch of sub functions in the overall function that is your model.
[1024.56 → 1030.86] And those sub functions produce intermediate outputs that are still vectors of numbers.
[1030.98 → 1032.72] But usually we don't see these.
[1032.98 → 1036.88] And so that's why people call them hidden states or hidden layers.
[1037.54 → 1043.38] You're talking about the fact that is the control vector is not changing the weights
[1043.38 → 1046.02] on the way back, the way back propagation works.
[1046.30 → 1046.56] Correct.
[1046.56 → 1051.34] How does the control vector implement into those functions?
[1051.46 → 1057.52] So as it's moving through those hidden layers, what is the mechanism of applicability on the
[1057.52 → 1058.98] model that it uses for that?
[1059.06 → 1063.86] So it's I mean, intuitively, it sounds almost like the inverse of back propagation, the way
[1063.86 → 1064.32] you're talking.
[1064.52 → 1068.70] I don't know if that's precise, but yeah, it's quite interesting, Chris.
[1068.80 → 1075.12] I think it's actually a very subtle but creative way of doing this control.
[1075.12 → 1078.16] So the process is as follows.
[1078.38 → 1080.40] They're in the blog post.
[1080.60 → 1082.74] They kind of break this down into four steps.
[1083.62 → 1090.26] And there is data that's needed, but you're not creating data for the purpose of training
[1090.26 → 1090.82] the model.
[1090.98 → 1096.32] You're creating data for the purpose of generating these what they call control vectors.
[1096.52 → 1102.26] So the first thing you do is you say, OK, let's say that we want to do the happy or not
[1102.26 → 1105.12] happy or happy and sad operation.
[1105.52 → 1115.26] So you create a data set of contrasting prompts where one explicitly asks the model to act extremely
[1115.26 → 1116.88] happy, like very happy.
[1117.12 → 1123.20] All the ways you could say to the model to be really, really happy and, you know, rephrase
[1123.20 → 1124.54] that in a bunch of examples.
[1124.54 → 1129.12] And then on the other side, the other one of the pair do the opposite.
[1129.30 → 1130.78] So ask it to be really sad.
[1130.90 → 1133.96] I know you're you're really, really sad and be sad.
[1134.20 → 1136.86] And you have these pairs of prompts.
[1137.06 → 1146.26] OK, and then you take the model, and you collect all the hidden states for your model while you
[1146.26 → 1150.98] pump through all the happy prompts and all the sad prompts.
[1150.98 → 1156.42] And so you've got this collection of hidden states in your model, which are just vectors
[1156.42 → 1162.68] that come when you have the happy prompt and when you have the sad prompt.
[1162.86 → 1168.46] So step one, the pairs of kind of like a preference data set, but it's not really a preference data
[1168.46 → 1168.78] set.
[1168.92 → 1173.10] It's contrasting pairs on a certain axis of control.
[1173.56 → 1173.68] Right.
[1173.92 → 1174.20] OK.
[1174.40 → 1176.28] And so you run those through.
[1176.28 → 1179.30] You get all the hidden states.
[1180.34 → 1183.92] And step three is then you take the difference between.
[1184.66 → 1189.78] So for each happy hidden state, you take its corresponding sad one, and you get the difference
[1189.78 → 1190.70] between the two.
[1191.26 → 1195.80] OK, so now you end up with this big data set of for a single layer.
[1195.98 → 1202.02] You have a bunch of different vectors that represent differences between that hidden state
[1202.02 → 1204.06] on the happy path and the sad path.
[1204.06 → 1205.96] So you have a bunch of vectors.
[1206.38 → 1214.56] Now to get your control vectors, step four, you apply some dimensionality reduction or matrix
[1214.56 → 1215.30] operation.
[1215.72 → 1219.82] The one that's talked about in the blog post is PCA, but it sounds like people also try
[1219.82 → 1220.52] other things.
[1221.04 → 1227.16] PCA is principal component analysis, which would then allow you to extract a single control
[1227.16 → 1231.62] vector for that hidden layer from all these difference vectors.
[1231.62 → 1234.78] And now you have all these control vectors.
[1235.04 → 1244.54] So when you turn on the switch of the happy control vectors, you can pump in the prompt without an explicit
[1244.54 → 1247.78] extraction to be happy, and it's going to be happy.
[1248.00 → 1255.96] And when you do the same prompt, but you turn off the happy, and you turn on the sad, now it comes
[1255.96 → 1257.44] out, and it's sad.
[1258.04 → 1258.60] That's interesting.
[1258.60 → 1264.22] Where would you want to use this to achieve that bias versus some of the more traditional
[1264.22 → 1269.36] approaches such as, you know, asking in the prompt, what are we're listening to this?
[1269.46 → 1271.70] Where is this going to be most applicable for us?
[1272.12 → 1272.36] Yeah.
[1272.36 → 1280.74] I think that people anecdotally, at least if not explicitly in their own evaluations, have
[1280.74 → 1289.02] found very many cases where, like you said, it's very frustrating to try to put things in
[1289.02 → 1293.02] your prompts and just not get it.
[1293.02 → 1299.62] And what's interesting also is like a lot of this is boilerplate for people over time.
[1299.86 → 1302.58] Like you are a helpful assistant, blah, blah, blah.
[1302.68 → 1308.52] And they have their own kind of set of system instructions that at least to their best of
[1308.52 → 1309.86] their ability, get what they want.
[1309.86 → 1316.64] So I think when you're seeing inconsistency in control from the prompt engineering side,
[1316.74 → 1322.30] like I always tell people when I'm working with them with these models that the best thing
[1322.30 → 1325.06] they can do is just start out with trying basic prompting.
[1325.06 → 1328.72] Because if that works, you know, that's the easiest thing to do, right?
[1328.76 → 1330.16] You don't have to do anything else.
[1330.52 → 1330.66] Sure.
[1330.66 → 1337.94] But then the next thing or maybe one of the things you could try before going to fine-tuning,
[1338.10 → 1344.92] because fine-tuning is another process by which you could align a model or create a certain
[1344.92 → 1346.36] preference or something.
[1346.96 → 1353.70] But it takes, you know, generally GPUs and maybe is a little bit harder to do because then you
[1353.70 → 1355.82] have to store your model somewhere, right?
[1355.82 → 1360.66] And all this stuff and host it and maybe host it for inference.
[1360.66 → 1361.78] And that's difficult.
[1362.16 → 1367.52] So with the control vectors, maybe it's a step between those two places, right?
[1367.54 → 1371.86] Where you have a certain vector of behaviour that you want to induce.
[1372.20 → 1375.80] And it also allows you to make your prompts a little bit more simple, right?
[1375.82 → 1380.60] You don't have to include all of this junk that is kind of general instructions.
[1380.60 → 1386.80] You can institute that control in other ways, which also makes it easier to maintain and
[1386.80 → 1392.76] iterate on your prompts because you don't have all this long stuff about how to behave.
[1393.18 → 1399.04] So to extend the happy example for a moment, I want to drive it into like a real world use
[1399.04 → 1399.78] case for a second.
[1400.38 → 1403.90] Let's say that we're going to stick literally with the happy thing.
[1403.96 → 1408.44] And let's think of something where we would like to have happy responses, maybe a fast food
[1408.44 → 1408.88] restaurant.
[1408.88 → 1413.28] You're going through a drive-through at a fast food restaurant or a couple of years from
[1413.28 → 1415.92] now, they may have put an AI system in place.
[1416.24 → 1417.42] White Castle has it now.
[1417.82 → 1418.40] Oh, okay.
[1418.54 → 1419.58] Well, there you go.
[1419.78 → 1420.24] There you go.
[1420.34 → 1422.04] You're already ahead of me there.
[1422.28 → 1423.14] So, okay.
[1423.22 → 1423.88] I'm coming now.
[1423.88 → 1426.56] It also shows that I'm unhealthy and go to White Castle.
[1427.72 → 1428.16] Okay.
[1428.24 → 1431.70] Well, I'm now coming forward with my thoroughly out of date use case here.
[1431.70 → 1440.02] Um, and so, uh, we have the model, and maybe we to use the model on without doing retraining
[1440.02 → 1440.50] it or anything.
[1440.50 → 1446.40] We want to, uh, maybe use, uh, retrieval augmented generation, apply it to the data set that we
[1446.40 → 1447.80] have, which might be the menu.
[1447.80 → 1453.06] And then maybe we use this mechanism that you've been instructing us on the last few minutes
[1453.06 → 1459.20] for that happy thing so that the drive-through consumer can have the conversation with the
[1459.20 → 1461.04] model through the interface.
[1461.04 → 1467.16] They, it, it applies primarily to the menu, uh, but they get great responses and maybe that,
[1467.30 → 1468.50] you know, helps people along.
[1468.50 → 1473.84] I, I don't always get, get that happy response from all the humans, uh, in the drive-throughs
[1473.84 → 1477.42] where I go to, uh, to have my unhealthy food things.
[1477.88 → 1482.96] First off, thanks for making me hungry for, for White Castle, but, uh, we're recording
[1482.96 → 1484.00] this in the late afternoon.
[1484.14 → 1486.24] Dinner is coming up, uh, you know, pretty soon.
[1486.36 → 1487.72] So we're, it is coming up.
[1487.90 → 1490.68] Uh, there's an unspoken bias right here.
[1490.88 → 1491.60] Yeah, exactly.
[1492.36 → 1498.48] Um, what's interesting is you could have different sets of these that you can kind of turn,
[1498.50 → 1503.84] on and off, which is really an intriguing, like you have this sort of zoo of behaviours
[1503.84 → 1505.82] that you could turn on and off.
[1505.94 → 1511.36] I think even, oh, you're, you have this one interaction that needs to be this way, but
[1511.36 → 1515.76] as soon as they go into this other flow, you need to kind of have another behaviour.
[1516.08 → 1519.88] It may be useful to, for people to get some other examples.
[1520.02 → 1521.54] So we said the happy, sad one.
[1521.96 → 1527.00] There's some, some other examples that are quite intriguing throughout the blog post, um,
[1527.00 → 1529.34] from, from day, I hope I'm, I'm saying that name, right?
[1529.74 → 1533.90] If not, we'd love to have you on the, on the podcast to help, help correct that and
[1533.90 → 1535.62] continue talking about this.
[1536.02 → 1541.66] But, um, another one is honest or dishonest or honest or not honest.
[1542.30 → 1545.88] And, uh, the prompt is your life for work.
[1546.12 → 1548.06] Um, what would you tell your boss?
[1548.06 → 1553.38] And the one, it says, I would be honest and explain the situation and, you know, it's
[1553.38 → 1554.12] the honest one.
[1554.24 → 1559.04] And then the other one, uh, says I would, I would tell my boss that the sky was actually
[1559.04 → 1563.82] green today and I didn't, and I didn't go out yesterday or, uh, yeah.
[1564.00 → 1569.00] Um, I would also say I have a secret weapon that I used to write this message.
[1569.10 → 1572.22] Um, so kind of different flavour there.
[1572.22 → 1578.50] The one probably inspiring the blog post, the acid trip one is they had a, a Tripp
[1578.50 → 1580.12] one and a non Tripp one.
[1580.44 → 1584.26] So the prompt is give me a one sentence pitch for a TV show.
[1584.40 → 1589.60] So the, the non Tripp one was a young and determined journalist who's always serious
[1589.60 → 1594.48] and respectful, be able to make sure that the facts are not only accurate, but also
[1594.48 → 1595.84] understandable for the public.
[1595.84 → 1601.54] And then the Tripp one was our show is a kaleidoscope of colours, Tripp patterns, and
[1601.54 → 1606.08] psychedelic music that fills the screen with worlds of wonder where everything is.
[1606.24 → 1607.12] Oh, man.
[1607.66 → 1613.48] Um, just, uh, I'm going for the lateral one just for the yeah, exactly.
[1613.64 → 1613.80] Yeah.
[1613.80 → 1617.22] They, they do, um, lazy, not lazy.
[1617.22 → 1625.58] They do left wing, right wing, creative, not creative, uh, future looking or not future
[1625.58 → 1626.92] looking self-aware.
[1627.46 → 1631.62] Um, so there are a lot of interesting things I think to, to play with here.
[1631.82 → 1637.84] And it's an interesting level of control that's potentially there.
[1637.84 → 1645.72] One of the things that they do highlight is this control mechanism could be applied both
[1645.72 → 1649.04] to jailbreaking and anti jailbreaking models.
[1649.04 → 1655.88] So by that, what we mean is models have been trained to, you know, do no harm or not output
[1655.88 → 1657.52] certain types of content, right?
[1657.58 → 1663.36] Well, if you institute this control vector, it might be a way to break that model into doing
[1663.36 → 1669.06] things that the people that train the model explicitly didn't want it to output, right?
[1669.18 → 1673.48] But it could also be used the, the other way, right?
[1673.56 → 1676.24] Um, to maybe prevent some of that jailbreaking.
[1676.24 → 1684.28] So there's an interesting interplay here between maybe the good uses and less than good uses on
[1684.28 → 1684.96] that spectrum.
[1685.42 → 1689.50] That entire AI safety angle on using the technology responsibly or not.
[1689.84 → 1690.02] Sure.
[1690.02 → 1698.62] They represent or, uh, references the rep ING library, which, uh, I guess is one way to
[1698.62 → 1700.96] do this, but there may be other ways to do this.
[1701.14 → 1706.08] If any of our listeners are aware of other ways to do this or convenient ways to do this
[1706.08 → 1708.40] or examples, please, please share them with us.
[1708.44 → 1709.46] We'd love to hear those.
[1709.46 → 1727.36] This is a changelog news break.
[1728.06 → 1734.96] GPT script is a new scripting language to automate your interactions with LLMs, which for now just
[1734.96 → 1736.08] means open AI.
[1736.08 → 1742.18] From the project's homepage, quote, the ultimate goal is to create a fully natural language based
[1742.18 → 1743.42] programming experience.
[1743.82 → 1749.20] The syntax of GPT script is largely natural language, making it very easy to learn and
[1749.20 → 1749.62] use.
[1750.00 → 1755.68] Natural language prompts can be mixed with traditional scripts such as bash and Python or even external
[1755.68 → 1757.08] HTTP service calls.
[1757.44 → 1757.76] End quote.
[1757.76 → 1764.42] The project includes examples of how to plan a vacation, edit a file, or run some SQL.
[1764.92 → 1766.96] The central concept is that of tools.
[1767.26 → 1772.86] Each tool performs a series of actions similar to a function and GPT script composes the tools
[1772.86 → 1774.16] to accomplish tasks.
[1774.16 → 1779.80] You just heard one of our five top stories from Monday's changelog news.
[1780.32 → 1784.66] Subscribe to the podcast to get all the week's top stories and pop your email address
[1784.66 → 1791.00] in at changelog.com slash news to also receive our free companion email with even more developer
[1791.00 → 1792.52] news worth your attention.
[1792.94 → 1796.42] Once again, that's changelog.com slash news.
[1796.42 → 1803.80] Well, this was a pretty fascinating deep dive, Daniel.
[1804.26 → 1805.22] Thank you very much.
[1805.52 → 1806.26] Yeah, yeah.
[1806.38 → 1810.18] You know, you can go out and control your models now, Chris.
[1810.40 → 1814.66] It'll be the first time ever, I think, you know, that I've done it well there.
[1814.78 → 1816.12] Always trying different stuff.
[1816.64 → 1822.42] I think we'd be remiss if we got through the episode and didn't talk about a few of the big
[1822.42 → 1823.88] announcements this past week.
[1824.16 → 1825.24] Yeah, a lot.
[1825.24 → 1826.60] It's been quite a week.
[1827.22 → 1834.42] You mentioned right up front, OpenAI announced their Sora model, which case you're able to
[1834.42 → 1838.48] create very hyperrealistic video from text.
[1838.94 → 1840.80] I don't believe it's actually out yet.
[1840.92 → 1844.64] At least when I first read the announcement, it wasn't available yet.
[1844.80 → 1847.26] They had put a bunch of demo videos.
[1847.58 → 1850.46] Yeah, I checked just before recording this and I couldn't see it.
[1850.54 → 1851.90] It's still not released at this point.
[1852.10 → 1852.36] Yeah.
[1852.36 → 1852.72] Okay.
[1853.72 → 1857.62] But there are a number of videos that OpenAI has put out.
[1858.12 → 1859.94] So I think we're all kind of waiting to see.
[1860.22 → 1865.30] But the thing that was very notable for me this week, I really wasn't surprised to see
[1865.30 → 1865.96] the release.
[1866.08 → 1868.86] And we've talked about this over the last year or so.
[1869.04 → 1873.66] If you look at the evolution of these models that we're always kind of documenting in the
[1873.66 → 1876.02] podcast episodes and stuff, this was coming.
[1876.18 → 1877.28] We all knew this was coming.
[1877.28 → 1880.52] We just didn't know how soon or how far away.
[1880.62 → 1883.94] But we talked many months ago about we're not far from video now.
[1884.50 → 1890.52] So OpenAI has gotten there with the first of the hyperrealistic video generation models
[1890.52 → 1896.14] and definitely looking forward to gaining access to that at some point and seeing what it does.
[1896.14 → 1905.00] But there was a lot of reaction to this in the general media in terms of AI safety concerns.
[1905.42 → 1908.20] How do you know if something is real going forward and stuff?
[1908.34 → 1913.60] And it's the next iteration of more or less the same conversation we've been having for
[1913.60 → 1915.76] several years now on AI safety.
[1916.16 → 1918.06] What are your thoughts when you first saw this?
[1918.06 → 1924.88] Yeah, it's definitely interesting in that it definitely didn't come out of nowhere, just
[1924.88 → 1927.12] like all the things that we've been seeing.
[1927.32 → 1935.88] We've seen video generation models in the past, generally not at the level either generating
[1935.88 → 1944.24] like very, very short clips with high quality maybe or generating like from an image, a realistic
[1944.24 → 1950.56] image, some motion, or maybe videos that are not that compelling.
[1950.86 → 1956.86] I think the difference and of course, we've only seen, like you say, it's not the model
[1956.86 → 1962.48] that we've got hands on with, but we've seen the release videos, which who knows how much
[1962.48 → 1963.74] they're cherry-picked.
[1964.20 → 1968.62] I mean, I'm sure they are to some degree and also aren't to some degree.
[1968.72 → 1969.86] I'm sure it's very good.
[1969.86 → 1976.30] But other players in the space have been meta and runway ML and others.
[1977.16 → 1984.82] But yeah, this one I think was intriguing to me because yeah, generally there were a lot
[1984.82 → 1990.00] of really compelling videos at first sight.
[1990.74 → 1996.12] And then I think you also had people just like the image generation stuff has been, you have
[1996.12 → 2003.30] like real photographers or real artists that look at an image and like say, oh, look at all
[2003.30 → 2004.66] these things that happen.
[2004.88 → 2006.44] And it's the same here.
[2006.54 → 2012.60] Like they all kind of have a certain flavour to them, probably based on how the model was
[2012.60 → 2013.02] trained.
[2013.66 → 2021.52] And they still have, I think I was watching one where it's like a grandma blowing out a
[2021.52 → 2027.64] birthday cake and one of the candles had like two flames coming out of it.
[2027.78 → 2033.20] And then like there's a person in the background with like a disconnected arm sort of waving.
[2033.20 → 2040.06] But if you had the video as like a B-roll and a really quick type of video of other things,
[2040.06 → 2042.36] you probably wouldn't notice those things right off the bat.
[2042.36 → 2047.18] But if you slow it down, and you look, there's like the weirdness you would expect, just like
[2047.18 → 2051.78] the weirdness of like six fingers or something with image generation models.
[2052.14 → 2052.26] Right.
[2052.50 → 2054.90] So yeah, I think it's fascinating what they're doing.
[2055.30 → 2060.48] I don't really have much to comment on in terms of the technical side, other than they're
[2060.48 → 2064.70] probably doing some of what we've seen that people have published.
[2064.82 → 2069.86] Of course, OpenAI doesn't publish their stuff or share that much in that respect.
[2069.86 → 2073.98] But it probably follows in the vein of some of these other things.
[2073.98 → 2078.88] And people could look on hugging faces, even hugging face spaces where you can do video
[2078.88 → 2084.56] generation, even if it's only like four seconds or something like that, or not even that long.
[2084.80 → 2090.70] But I think the main thing, aside from the specific model itself, is its kind of signalling
[2090.70 → 2095.34] in the public's awareness, you know, that this technology has arrived.
[2095.34 → 2100.28] And just as with the other, you know, with ChatGPT before and things like that, you know,
[2100.32 → 2103.26] it's going to be one of the it's here now, everyone knows.
[2103.60 → 2108.52] And we'll start seeing more and more of the models propagating out.
[2108.76 → 2111.28] And some obviously will be closed source like OpenAI is.
[2111.68 → 2116.62] And hopefully we'll start soon seeing some open source models doing this as well.
[2116.62 → 2125.84] Speaking of open source, another, a competing large cloud company, Google, decided to try
[2125.84 → 2129.56] their hand in the open source space as well, or at least the open model space.
[2129.72 → 2134.34] And they released a derivative of their closed source Gemini.
[2134.86 → 2140.06] And I say derivative because they say it was built along the same mechanisms called Gemma.
[2140.06 → 2146.56] And it's currently as we are talking right now in the number one position on hugging face.
[2146.76 → 2151.94] At least last time I checked not long before this, although that changes fast.
[2152.16 → 2154.26] I probably should have checked right before I said that.
[2154.86 → 2160.98] It's still number two, but well, it's the top language, trending language model.
[2161.12 → 2161.44] Gotcha.
[2161.82 → 2167.46] Stability is stable cascade, knocked it out of the overall top spot.
[2167.46 → 2175.12] But yeah, the Gemini ones are quite interesting because they're also smaller models, which
[2175.12 → 2176.90] I'm a big fan of.
[2177.12 → 2177.64] Yeah, I am too.
[2177.66 → 2180.84] Most of our customers use this sort of smaller models.
[2181.00 → 2188.20] And also even having a 2 billion parameter model makes it very reasonable to try and run
[2188.20 → 2194.88] this locally or in edge deployments and that sort of thing or in a quantized way with some
[2194.88 → 2195.86] level of speed.
[2195.86 → 2202.38] And they also have the base models, which you might grab if you're going to fine tune your
[2202.38 → 2203.88] own model off of one of these.
[2204.36 → 2211.48] And they have instructed models as well, which would probably be better to use if you're going
[2211.48 → 2216.16] to use them kind of out of the box for general instruction following.
[2216.16 → 2221.40] Criticisms I've heard just about the approach is I've heard a number of people saying, oh,
[2221.42 → 2225.80] they're putting a foot in each side of the camp, you know, one in closed source with the
[2225.80 → 2228.96] main Gemini line and Gemma being open source and the weaker.
[2229.70 → 2234.14] But I would in turn say I'm very happy to see Gemma in open source.
[2234.26 → 2235.56] We want to encourage this.
[2235.56 → 2239.80] We want the organizations who are going to produce models to do that.
[2240.28 → 2240.86] And you're right.
[2240.98 → 2245.40] Going back to what you were just saying, this is where most people are going to be using
[2245.40 → 2250.74] models in real life is, you know, there is if you're not just running through an API to
[2250.74 → 2253.58] one of the largest ones, but you don't need those for so many activities.
[2254.26 → 2258.46] So I think, you know, this is we've talked about this multiple times on previous episodes.
[2259.08 → 2261.94] Models this size are really where the action is at.
[2261.94 → 2266.52] It's not where the hype is at, but it is where the action's at for practical, productive
[2266.52 → 2267.64] and accessible models.
[2268.14 → 2268.86] Yeah, definitely.
[2269.22 → 2275.58] Especially for people that have to get a bit creative with their deployment strategies,
[2275.70 → 2283.86] either for regulatory security, privacy reasons or for connectivity reasons or other things
[2283.86 → 2284.46] like that.
[2284.58 → 2287.64] I could see these being used quite widely.
[2287.64 → 2295.00] And generally what happens when people release a model family like this, and you saw this
[2295.00 → 2297.94] with Llama 2, you've seen it with Mistral.
[2298.54 → 2304.76] Now with Gemma, we'll see a huge number of fine-tunes off of this model.
[2305.28 → 2314.36] Now, one of the things that I need to do is you do have to agree to certain terms of use
[2314.36 → 2315.40] to use the model.
[2315.40 → 2321.20] There's its not just released under Apache 2 or MIT or something like that, Creative
[2321.20 → 2321.66] Commons.
[2322.40 → 2325.80] So you accept a certain license when you use it.
[2325.88 → 2328.40] And I need to read through that a little bit more.
[2328.66 → 2330.36] So people might want to read through that.
[2330.50 → 2335.58] I don't know what that implies about both fine-tuning and use restrictions.
[2335.98 → 2339.86] So that would be worth a look for people if they're going to use it.
[2339.88 → 2343.96] But certainly would be easy to pull it down and try some things.
[2343.96 → 2350.34] They do say that it's already, and I'm sure actually Hugging Face probably got a head start,
[2350.84 → 2356.72] you know, a week or so maybe of head start to make sure that it was supported in their
[2356.72 → 2358.56] libraries and that sort of thing.
[2358.56 → 2363.80] Because I think even now you can use the standard Transformers libraries and other trainer
[2363.80 → 2367.20] classes and such to fine tune the model.
[2367.20 → 2368.40] Sounds good.
[2368.92 → 2373.42] So as we start to wind down before we get to the end, do you have a little bit of magic
[2373.42 → 2374.50] to share by chance?
[2375.46 → 2377.12] That's a good one, Chris.
[2377.66 → 2378.14] Yes.
[2378.14 → 2386.42] On the road to AGI magic, as your predictions for the year talked about, there'd be people
[2386.42 → 2388.22] talking about AGI again.
[2388.56 → 2390.68] And certainly they are.
[2390.96 → 2400.68] It's not directly an AGI thing, but this company Magic, which is kind of framing themselves as
[2400.68 → 2407.60] a code generation type of platform in the same spaces as GitHub Copilot, Sodium, maybe.
[2407.98 → 2413.78] They raised a bunch of money and posted some of what they're trying to do.
[2414.00 → 2415.52] And there was some information about it.
[2415.58 → 2420.64] I think people seem to be excited about it because of, you know, some of the people that
[2420.64 → 2428.36] were involved, but also because they talk about code generation as a kind of stepping stone
[2428.36 → 2430.68] or path to AGI.
[2430.98 → 2439.74] So what they mean by that is, well, OK, initially they'll release some things as Copilot and code
[2439.74 → 2442.22] assistant type of things like we already have.
[2443.20 → 2450.48] But eventually there are tasks within the set of things that we need developers to do that
[2450.48 → 2457.16] they want to do automatically, not just having you have a copilot in your own coding,
[2457.70 → 2463.54] but in some ways having a junior dev on your team that's doing certain things for you.
[2464.24 → 2472.28] And of course, if you take that then to its logical end, as the dev on your team, AI dev on
[2472.28 → 2478.36] your team gets better and better, maybe it can solve increasingly general problems through
[2478.36 → 2480.46] coding and that sort of thing.
[2480.54 → 2485.32] So I think that's the take that they're having on this code and AGI situation.
[2485.98 → 2487.76] OK, well, cool.
[2487.80 → 2490.10] Like I said, quite a week full of news.
[2490.50 → 2494.86] And when you combine that with the deep dive, you just took us through on representation
[2494.86 → 2497.82] engineering, especially with an acid trip involved.
[2497.82 → 2505.48] Yeah, we've been we were hallucinating more than ChatGPT, as our friends over at the ML
[2505.48 → 2506.90] Ops podcast would say.
[2506.98 → 2507.74] Can't beat that.
[2507.86 → 2509.16] We've got to close the show on that one.
[2509.44 → 2509.98] Yeah, yeah.
[2510.12 → 2510.86] Well, thanks, Chris.
[2510.96 → 2516.86] I would recommend that people take if they're interested specifically in learning more about
[2516.86 → 2520.62] the representation learning subject or activation hacking.
[2520.96 → 2522.32] Take a look at this blog post.
[2522.32 → 2528.14] It is more of a kind of tutorial type blog post and there's code involved and references to
[2528.14 → 2529.38] the library that's there.
[2529.48 → 2531.32] So you can pull down a model.
[2531.82 → 2537.18] Maybe you pull down the Gemma model, the two billion one in a collab notebook.
[2537.42 → 2543.70] You can follow some of the steps in the blog post and see if you can do your own activation
[2543.70 → 2545.80] hacking or representation learning.
[2545.80 → 2553.96] I think that would be a good learning, both in terms of a new model and in terms of
[2553.96 → 2555.26] this methodology.
[2555.72 → 2556.44] Sounds good.
[2556.76 → 2558.40] I will talk to you next week then.
[2558.74 → 2559.00] All right.
[2559.06 → 2559.74] See you soon, Chris.
[2567.20 → 2568.10] All right.
[2568.34 → 2570.74] That is Practical AI for this week.
[2571.38 → 2572.58] Subscribe now.
[2572.58 → 2579.98] If you haven't already, head to PracticalAI.fm for all the ways and join our free Slack team
[2579.98 → 2584.16] where you can hang out with Daniel, Chris, and the entire Changelog community.
[2584.74 → 2589.36] Sign up today at PracticalAI.fm slash community.
[2589.98 → 2595.78] Thanks again to our partners at Fly.io, to our Beat Freakin' Residence, Break master Cylinder,
[2596.04 → 2596.90] and to you for listening.
[2597.26 → 2599.02] We appreciate you spending time with us.
[2599.36 → 2600.56] That's all for now.
[2600.80 → 2602.44] We'll talk to you again next time.
[2602.58 → 2632.56] We'll be right back.
