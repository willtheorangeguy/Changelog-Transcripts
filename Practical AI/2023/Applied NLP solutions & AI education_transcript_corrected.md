[0.00 → 8.64] Welcome to Practical AI.
[9.20 → 15.96] If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 → 18.78] are changing the world, this is the show for you.
[19.20 → 24.36] Thank you to our partners at Vastly for shipping all of our pods superfast to wherever you
[24.36 → 24.66] listen.
[24.92 → 26.76] Check them out at Fastly.com.
[26.76 → 32.02] And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 → 33.70] No ops required.
[34.02 → 36.08] Learn more at fly.io.
[42.26 → 45.58] Well, welcome to another episode of Practical AI.
[45.96 → 47.64] This is Daniel Whiten ack.
[47.76 → 50.72] I'm a data scientist at SIL International.
[51.20 → 55.78] And I'm not joined by Chris today, but we have a very exciting guest.
[55.78 → 62.12] Today, we have with us Jay Palomar, who you might know from a bunch of great content out
[62.12 → 68.24] there, including the Illustrated Transformer and other articles also with Cohere.
[68.58 → 69.18] Welcome, Jay.
[69.60 → 70.04] Thank you.
[70.16 → 70.82] Great to be here.
[71.00 → 71.72] Thank you for having me.
[71.94 → 72.60] Yeah, yeah.
[72.64 → 76.24] It was great to see you at EM NLP back in December.
[76.88 → 81.60] We tried to sit down and have a conversation then, but it didn't quite work out.
[81.60 → 84.14] Still really great to see you there.
[84.62 → 92.94] What were your impressions just generally about the experience at EM NLP and the NLP crowd
[92.94 → 95.86] gathering there and what they were talking about?
[95.92 → 98.88] It was just after ChatGPT came out.
[99.26 → 102.00] So yeah, what was your impression and some takeaways?
[102.54 → 104.02] Yeah, these are incredible events.
[104.02 → 111.10] The amount of condensed download that you get in a conference like this of so much research.
[111.26 → 112.88] A lot of it you've caught up to.
[113.00 → 115.38] A lot of it is new and for you to explore.
[115.72 → 122.06] And also a lot of people to meet that, in my case, most of them I've never met before.
[122.84 → 129.48] A lot of them I've connected with online, but then having the chance to go deep into some
[129.48 → 133.82] these topics and think through with people what they're thinking about.
[134.34 → 140.58] And also like observing what themes are sort of coming in, let's say, multiple poster presentations
[140.58 → 141.70] or workshops.
[142.46 → 145.48] So yeah, definitely awesome running into you.
[145.54 → 147.02] I'm glad we're catching up after that.
[147.60 → 152.52] I'm glad we got to shoot also one of your works in a video we've rolled out.
[152.62 → 154.88] And it's part of my excitement when I was there.
[154.88 → 159.52] I was like, you know, people who don't go to conferences, they never really get the sense
[159.52 → 160.68] of what happens inside.
[161.62 → 166.66] And so I'm glad that you were doing a bunch of these interviews during the conference to
[166.66 → 168.14] cover it for people who are not there.
[168.50 → 171.74] And I think there's room for a lot more sort of content like that.
[171.96 → 180.14] So yeah, it was definitely interesting and eye-opening and quite intense in terms of just how
[180.14 → 184.40] much information and social interaction is done in five days.
[184.40 → 185.60] Yeah, I love it.
[185.70 → 188.20] But at the end of each day, I'm so tired.
[189.08 → 191.02] I like I love being around people.
[191.18 → 192.36] I actually do enjoy that.
[192.36 → 195.96] But being an introvert, I am absolutely exhausted afterwards.
[196.48 → 196.84] 100%.
[196.84 → 198.24] And it's like on a weekend.
[198.34 → 201.94] So it's like also you're, you know, you're working through and then, you know, you don't
[201.94 → 202.46] have a weekend.
[202.46 → 203.96] And so you're working through it.
[204.00 → 208.20] So yeah, definitely need a day or two after to sort of cool down.
[208.70 → 208.84] Yeah.
[208.86 → 211.56] And you mentioned some of the content that you've been creating.
[211.56 → 218.68] I think many probably know your name or would have like to recognize your blog and some of
[218.68 → 222.36] the blog posts, like I mentioned, from like Illustrated Transformer.
[222.44 → 224.92] But then like you have so much after that as well.
[225.00 → 229.42] You were just mentioning some recent things you put out about Stable Diffusion.
[229.42 → 237.08] Where did you start developing this passion for like more of the educational side of this
[237.08 → 239.52] kind of state-of-the-art AI stuff?
[239.76 → 242.34] And what's your perspective on that?
[242.42 → 247.76] And what from your perspective are you trying to kind of achieve with some of the things that
[247.76 → 248.36] you're putting out?
[248.70 → 253.66] Writing publicly and like learning publicly is maybe one of the greatest life hacks I've
[253.66 → 254.66] ever stumbled into.
[254.66 → 259.84] It started about eight years ago when I was just getting into machine learning.
[260.42 → 264.08] There was an event that happened, which was TensorFlow becoming open source.
[264.98 → 268.22] And I thought, OK, now it's a good time to jump into machine learning.
[268.32 → 270.28] I've been eyeing the field with interest.
[270.40 → 276.04] I've been seeing a lot of the deep learning developments, but I had no exposure to it previously.
[276.56 → 280.74] So I was, you know, not necessarily working in the industry, but I was extremely interested
[280.74 → 282.00] in it and I wanted to learn.
[282.00 → 285.70] And it's very easy for you to spend some time learning about a thing.
[285.82 → 291.82] But then, you know, three months in, six months in, you need some sort of artifact to point
[291.82 → 295.78] to that really gives you a sense of, you know, how much you're progressing in that field.
[295.90 → 301.18] And for me, some of these initial artifacts was, yeah, writing a tutorial that sort of captures
[301.18 → 303.48] what I've learned in those two or three months.
[304.06 → 309.92] It also serves as me just writing down my notes for me to learn a concept a little bit better.
[309.92 → 316.04] So I did that a few times, and it developed in so many different ways.
[316.14 → 322.26] So it opened so many doors that pulled me closer to machine learning and helped me learn more
[322.26 → 322.86] and more and more.
[323.36 → 327.56] Like if I'm to understand a new paper that came out, I can read the paper and, you know,
[327.60 → 331.00] maybe understand or grasp, let's say, you know, 20 percent of it.
[331.30 → 336.58] But if I'm to explain it, I really have to go in, you know, much deeper into it or if you're
[336.58 → 340.94] going to implement it as well, because if you're writing about it or explaining the work,
[341.00 → 345.20] you don't want to write something out there that is, let's say, incorrect.
[345.58 → 351.54] So in a way, it forces the social circuits of my brain to exert that pressure for me to learn.
[352.28 → 354.06] And so that's been extremely useful.
[354.14 → 355.38] And that's opened so many doors.
[355.56 → 360.48] So through the blog, Udacity reached out to me and I worked with them for about two years,
[360.48 → 366.06] creating lessons on their deep learning and NLP nanometres, which include creating a bunch
[366.06 → 369.60] of videos and code examples, which I continue to do after.
[369.86 → 374.34] So that included, let's say, the YouTube channel that I've been, you know, creating some of
[374.34 → 378.06] these videos on that explain, you know, a bunch of these models.
[378.92 → 381.88] But yeah, it's a very fast moving field.
[382.04 → 386.00] And there are so many exciting things happening every couple of months.
[386.00 → 392.42] And when I get some time and I sort of have my eyes on something that is especially interesting,
[392.98 → 395.42] yeah, I would sit down and try to sort of do a write-up.
[395.62 → 401.52] And so some of these milestones of, let's say, models have been, so yeah, the transformer
[401.52 → 402.82] was a major one.
[402.94 → 404.28] GPT-2 was a big one.
[404.34 → 405.08] GPT-3.
[405.76 → 406.10] BERT.
[406.90 → 410.12] Retrieval augmented transformers, I've written about that.
[410.22 → 411.84] Really interested in multimodality.
[411.84 → 418.14] So when a language model has the ability to read or like to look at images or generate images.
[418.64 → 421.12] So I have a write-up about one of these models.
[421.78 → 426.20] And then, yes, the latest has been image generation models.
[426.34 → 431.82] So Stable Diffusion, how these models work, and how text language models factor into their
[431.82 → 436.92] composition is also sort of another sort of fascinating component for me in that.
[436.92 → 440.90] So yeah, definitely one of the most useful things that I do.
[441.12 → 447.82] And just I'm really excited to see people finding that content helpful in their journey.
[448.32 → 453.76] People love that visual aspect of, you know, don't assume that the reader knows everything
[453.76 → 454.46] about the topic.
[454.60 → 457.06] So a lot of people jump into the field.
[457.26 → 463.36] Either, you know, they jump from computer vision to NLP, or they jump from being a Python
[463.36 → 465.16] backend developer to becoming.
[465.16 → 471.10] And so just thinking about some of the content pieces as being gentle on ramps for them is
[471.10 → 472.52] something on my mind as I write these.
[472.60 → 475.50] And I encourage people to write whatever they learn.
[475.68 → 482.04] And we need so much educational content out there that it's the most useful life hack I
[482.04 → 482.50] can think of.
[482.84 → 484.06] Yeah, I totally agree with you.
[484.16 → 488.46] I think generally the podcast, as we've developed it, you know, Chris and I have developed it over
[488.46 → 488.92] time.
[489.06 → 494.14] Our focus is mostly on sort of like community and like bringing guests in and all that.
[494.14 → 499.80] But the one sort of like selfish, amazing thing that I found also is like having conversations
[499.80 → 501.08] about all of these topics.
[501.08 → 506.48] And occasionally Chris and I do like just episodes, him and I, where we dive into a topic.
[506.48 → 508.80] Like we did one on ChatGPT.
[508.80 → 515.94] We did one on Stable Diffusion and others where like having to talk about these things like
[515.94 → 522.94] in a time window and try to also not say that many inaccuracies.
[523.54 → 527.70] It is a challenge, but it's been really useful for my own learning.
[527.70 → 528.46] That's for sure.
[528.46 → 535.08] Do you have any tips or sort of cheat codes for those that are like, oh, I would really
[535.08 → 543.36] like to kind of get into this arena of creating educational content around technical topics
[543.36 → 546.48] around AI or NLP or whatever it is.
[546.48 → 550.96] Because like you say, there's such a need for good content around these things out there
[550.96 → 554.02] more so than like the research paper is great.
[554.02 → 558.20] But, you know, follow-ups to that and educational content around things is really useful.
[558.44 → 564.34] So any tips or things you'd like to share for those out there that are thinking about
[564.34 → 567.18] either blogs or videos or whatever it might be?
[567.60 → 567.82] Yeah.
[567.92 → 569.84] So like the first one is start.
[570.06 → 572.48] Just pick a medium and start with it.
[572.48 → 579.10] Whether it's audio, whether it's video, whether it's like to say short tweets or tweet storms
[579.10 → 582.74] or a blog or, you know, tech talk videos.
[582.74 → 588.16] So just pick something or experiment with a bunch of them until sort of you find the channel
[588.16 → 589.20] that you're comfortable with.
[589.30 → 594.62] But definitely what I see a lot of people do is waiting and waiting and waiting for them
[594.62 → 599.48] to have, let's say, their magnum opus and have that sort of masterwork be the first thing
[599.48 → 602.94] that they release, which is the wrong way to go about it.
[603.00 → 606.36] So you'll definitely improve a lot quicker.
[606.36 → 612.26] People will not, you know, judge you harshly for sharing something that you've learned
[612.26 → 613.30] out there.
[613.36 → 618.50] And a lot of people are held back by some sense of imposter syndrome because, you know, they're
[618.50 → 619.26] learning something.
[619.44 → 622.26] And, you know, there are so many experts out there about this thing.
[622.80 → 625.32] So they're like, you know, what can I add to this conversation?
[625.50 → 627.64] And in fact, you can add a lot.
[627.98 → 629.68] You're seeing it with fresh eyes.
[629.74 → 632.62] You're seeing it at a different time when there are different resources.
[632.62 → 639.04] Even if the only thing that you're doing is putting together a curated list of, you know,
[639.10 → 644.54] resources that you found helpful is a useful thing in its own sort of regard.
[644.68 → 649.80] So definitely starting and with time finding your own voice and finding your own comfort
[649.80 → 653.70] and improving your craft is something that will come with practice.
[653.70 → 656.70] You'll definitely not be happy with your first output.
[656.84 → 661.10] But as long as you're putting it out, you're learning, and you're sort of nudging your way
[661.10 → 663.94] closer into that place.
[664.48 → 667.44] To me, it's always useful to sort of, yeah, emulate your heroes.
[667.76 → 669.40] You know what kind of content do you consume?
[669.60 → 671.34] What kind of content did you find helpful?
[671.96 → 674.22] What exactly about it was helpful to you?
[674.38 → 680.86] So in my case, you know, coming into machine learning, like I can identify a few writers and
[680.86 → 686.30] bloggers who, you know, whose code or articles really were helpful to me.
[686.42 → 692.28] So Andrew Apathy, for example, you know, had this article about RNNs, the unreasonable
[692.28 → 693.54] effectiveness of RNNs.
[693.58 → 699.04] That was one of the first times when text generation really clicked for me and that it's
[699.04 → 702.74] finally really possible for software to generate text.
[702.92 → 705.00] And that is, you know, somewhat coherent.
[705.00 → 711.94] I learned a lot from, yeah, just the styles of Chris Ola, from Andrew Track and sort of
[711.94 → 717.44] writing a neural network tutorial with just 13 lines of Python.
[717.64 → 720.74] And that was really one of the first times when machine learning sort of really clicked
[720.74 → 721.10] for me.
[721.70 → 726.44] So yeah, that would be the I think the second one, like see the sense of what connects with
[726.44 → 726.72] you.
[727.24 → 728.58] Try maybe to emulate it.
[728.64 → 730.18] Don't be shy of stealing.
[730.18 → 735.00] You know, the Beatles spent years and years just doing covers until they were comfortable
[735.00 → 736.22] with their own sort of sound.
[736.84 → 738.00] And so that would be the second one.
[738.10 → 743.52] But, you know, really comes down to just create, put out there, get some feedback, continue
[743.52 → 745.20] creating and just move the cycle.
[746.14 → 753.14] I remember at EM NLP when we were chatting a bit, one of the things you mentioned was how
[753.14 → 757.76] you were really enjoying, I forget the exact words you used, but it was something like making
[757.76 → 762.86] NLP boring or something about applied NLP or something like that.
[763.38 → 764.66] What did you mean by that?
[764.70 → 769.06] And what are your kind of passions around like your day-to-day work at this point?
[769.46 → 769.58] Yeah.
[769.68 → 775.78] So, I mean, we're blessed to be working in a field that is very hot, very rapidly moving.
[776.00 → 781.88] And every now, and then you see something that is super impressive beyond the capabilities
[781.88 → 785.10] of what you think software should be able to do.
[785.10 → 792.86] Now, you can see a demo out there or, you know, you can come across social media posts
[792.86 → 797.12] that show that model X does Y, which is, you know, mind-blowing.
[797.62 → 801.68] But then how reliably really is the model able to do this specific task?
[801.78 → 806.78] So, a massive GPT model is able, let's say, to answer a question about programming.
[807.10 → 811.70] And you can see a demo or, you know, a screenshot online of it answering a question correctly.
[811.70 → 817.24] But then is this really reliable for you to build a product around for this specific use
[817.24 → 817.52] case?
[817.74 → 822.50] And, you know, the example here is that for some use cases it is, for others it's not.
[823.14 → 827.84] But if you're just seeing these demos, you have to really ask yourself, is this a cherry
[827.84 → 831.86] picked example or is this reliably something that the model is able to do?
[831.86 → 837.32] And for this example, which is answering questions about programming, that is a, you know, large
[837.32 → 844.48] class of complex problems that models are currently not able to really be reliably good at, as
[844.48 → 850.06] evidenced by Stack Overflow banning the posting of answers from GPT models.
[850.62 → 855.48] So, that's one example of, you know, use cases where, yes, you will see flashy demos, but,
[855.68 → 857.16] you know, the reliability isn't there.
[857.20 → 861.48] But there are other use cases where the models can reliably generate sort of use cases.
[861.48 → 867.50] And so, I work with and collaborate with a lot of developers and companies who are trying
[867.50 → 868.62] to roll out these models.
[868.68 → 871.44] And they, you know, would come in with a specific understanding.
[871.68 → 877.54] But then when they try to use it for a use case where the model is expected to reliably
[877.54 → 882.04] be correct, they, you know, find that the demos and the real world are a little different.
[882.76 → 887.12] And so, yeah, there's a little bit of education and, let's say, a learning curve of how to best
[887.12 → 892.30] roll out these models and how to think about the various use case and how they differ, for
[892.30 → 892.68] example.
[893.24 → 897.94] And so, yeah, I'm really excited in these, let's say, playbooks of how to roll these models
[897.94 → 904.74] out reliably, which ones are, you know, ready to be used now for various use cases.
[905.20 → 909.32] Like, one example here is, let's say, neural search and semantic search.
[909.32 → 915.06] And it's using embeddings to create search systems that go beyond just keyword search
[915.06 → 915.38] systems.
[915.46 → 919.74] So, that's a very, let's say, reliable and mature use case of AI.
[919.88 → 925.58] It's not part of, let's say, the generative AI hype out there, but it really should be.
[926.28 → 930.60] And so, that's a little bit of the example that I feel we as an industry owe the people
[930.60 → 936.78] who are just catching up to these developments to, you know, have a discerning eye of, yes,
[936.78 → 938.66] there are a lot of exciting things here.
[939.04 → 945.60] Let's not get sort of tricked by the hype across everything and have some non-realistic
[945.60 → 948.28] expectations for some use cases that are still futuristic.
[948.74 → 953.54] The models are still able to do incredible things right now, but some of them will continue
[953.54 → 954.24] to be developed.
[954.80 → 959.10] Yeah, that's a little bit of how I think about it in the I mean, that is definitely prefaced
[959.10 → 962.60] by saying that there is something really special happening here.
[962.60 → 969.06] And software being able to understand, quote unquote, understand and generate text coherently,
[969.06 → 973.72] you know, has a potential that is beyond what we can really fathom.
[974.18 → 976.50] So, it's right to be excited about it.
[976.76 → 977.72] Then, yeah, go deeper.
[978.20 → 979.00] Be a little cautious.
[979.64 → 984.00] Be discerning of cherry-picked examples versus reliable use cases.
[984.26 → 989.34] When I started first consuming like your blog content and other things and thinking about
[989.34 → 995.58] transformers and then like going over to a notebook, trying to do a few things, at a certain point,
[995.58 → 1001.28] it was quite difficult to like overcome that barrier and start to integrate some of these
[1001.28 → 1002.58] things into your applications.
[1002.76 → 1008.20] And we moved to a time when it's so easy to pull these models in.
[1008.96 → 1014.96] Now, the problem is not so much like good tooling around this because it is fairly easy to do this
[1014.96 → 1022.42] at this point in terms of like an integration, but more so around like the workflows and best
[1022.42 → 1028.28] practices and how to judge like, is this model a good fit for this use case, or how could I use
[1028.28 → 1028.86] this model?
[1028.98 → 1029.82] That sort of thing.
[1030.28 → 1032.44] Would you say that's also how you're seeing it?
[1032.54 → 1038.00] And I'm also wondering, you know, you mentioned talking to clients and customers and people doing,
[1038.26 → 1041.18] you know, building up new applications around these technologies.
[1041.18 → 1047.52] Have you seen a shift in terms of like most of those people being now like software engineers
[1047.52 → 1052.78] instead of, let's say, like data scientists or that sort of thing?
[1052.96 → 1059.74] And if so, how does that influence kind of how we think about building AI tooling and who
[1059.74 → 1061.48] we're building it for maybe?
[1062.02 → 1067.06] For the first point, definitely there's a lot of, you know, playbooks being created.
[1067.30 → 1069.86] So first it started out with prompt engineering.
[1069.86 → 1075.86] So how do you get the model to do some behaviour that is useful for your use case?
[1075.88 → 1077.48] And they're definitely capable of doing it.
[1078.00 → 1082.20] But then that's really not enough of a competitive advantage for you to build a product around.
[1082.86 → 1087.76] And so your playbook will need to include a bunch of other components.
[1087.94 → 1092.32] So can you have access to some proprietary data that others cannot have?
[1092.76 → 1098.36] And then one of the let's say, also differentiating factors here is can you fine tune your own models
[1098.36 → 1105.98] so that you just improve upon just the baseline model that is publicly accessible or even open source in some cases?
[1106.54 → 1114.56] How can you continue to improve the quality of your own fine-tunes and continue to collect the data that improves that model?
[1114.78 → 1118.26] And let's say observing the generations of your own model.
[1118.26 → 1125.36] If you're a company or a product that is, you know, building around a specific model, there are dynamics there that really affect the economics.
[1125.56 → 1133.24] So in image generation, for example, it's extremely useful to have a public gallery of your model's generations.
[1133.24 → 1139.18] So Midjourney has one of these where, you know, if you want to create a specific kind of image,
[1139.30 → 1143.56] you can, you know, give the model a few prompts and explore that generative space.
[1143.66 → 1150.26] But you're really helped by the model having a massive gallery of hundreds of thousands of examples
[1150.26 → 1158.58] that really nudge you towards the best way, direction, visual space, kind of prompt type or description of style.
[1158.58 → 1165.46] And so that's, let's say, another example of one element of a generative AI playbook.
[1165.96 → 1172.04] Keeping on top of the research is also another source of perfect ideas for how to roll out a lot of these models.
[1172.20 → 1181.98] So in, you know, two, three years ago, there were a lot of these demos when, let's say, GPT-3 first came out of the model answering something factual
[1181.98 → 1185.52] and bringing, let's say, a specific fact to asking it a question in the model.
[1185.52 → 1192.86] And it's surprising when that happens, but then you know with time that that's not a necessarily reliable use case for these models up until now.
[1192.94 → 1201.24] But there is a way towards one where you're not just asking the generative model for the information stored inside its parameters,
[1201.66 → 1204.08] but you aid it with a search component.
[1204.08 → 1211.32] There's a part of your system that goes and searches a database or the web and then retrieves relevant articles
[1211.32 → 1218.80] and presents those in the prompt to a generative model and, in this process, sort of improve what kind of model.
[1218.88 → 1223.12] So that's another sort of element of, if you want to tackle this use case, you know,
[1223.12 → 1228.20] don't just rely on the pre-trained model's parameters and information stored there,
[1228.28 → 1230.60] but let's say augment it with a retrieval component.
[1230.60 → 1234.38] And, you know, a bunch of companies are figuring out, yeah, a bunch of these.
[1234.46 → 1237.68] And I think as a community, we're also sort of working on that together.
[1237.84 → 1245.18] I'm working on sort of some write-ups to try to codify and, you know, make public some of this sort of gray knowledge
[1245.18 → 1250.16] that's coming together across generative AI use cases on both the text and image space.
[1250.16 → 1253.96] Definitely the last few months, to address the second part of your question,
[1254.32 → 1262.20] there's been an absolute explosion in the public's excitement of text generation models.
[1262.90 → 1271.70] So, yes, ChatGPT is one of these models, and then the generative chat battles happening between Google and Bing
[1271.70 → 1276.46] and these product rollouts and sort of the waves that they're making throughout the industry
[1276.46 → 1282.24] are definitely putting text generation and language models at the tops of the minds of a lot of people.
[1282.34 → 1287.96] And a lot of developers are sort of trying to figure out, you know, how they can start using these models,
[1288.06 → 1289.16] how they can think about them.
[1289.54 → 1293.24] Yeah, it's been an absolutely tremendous couple of months to see that growth,
[1293.24 → 1297.44] which is not just developers, but it's like people in the street, just, you know,
[1298.02 → 1302.90] your parents coming up and saying, okay, we finally sort of get what you do,
[1303.44 → 1306.20] which has been absolutely surprising.
[1306.86 → 1313.00] Yeah, I really like how you highlighted this sort of like gray area or gray matter,
[1313.22 → 1320.88] whatever you described around this, like knowledge of how to put these various pieces together into a solution.
[1320.88 → 1330.22] I guess it's sort of like solution with a certain set of like potential pathways forward with a state-of-the-art model.
[1330.36 → 1335.52] So like used to, like when there was sort of data science hype before all the AI hype,
[1335.62 → 1338.06] it was like, okay, you need training data, you're going to train a model.
[1338.18 → 1339.70] That was sort of like the playbook.
[1339.84 → 1343.94] Now you're in this scenario where you're like, okay, well, I have a pre-trained model.
[1344.12 → 1346.78] Am I going to do some type of fine tune?
[1346.78 → 1349.04] So that's like something there.
[1349.18 → 1351.86] Am I going to focus on prompt engineering?
[1352.14 → 1354.82] Am I going to chain multiple things together?
[1355.58 → 1360.12] Am I going to do some retrieval and pull in like external knowledge into that?
[1360.38 → 1365.68] So there's like so many of these things where like the chaining and the assembly of the solution
[1365.68 → 1371.92] is actually where the value comes out, which I think is a perfect thing for people to think about.
[1371.92 → 1376.34] I'm wondering, because you're in this all the time, you're seeing new problems.
[1376.50 → 1382.16] And I know you've even showed me cool solutions you put together around like topic modelling
[1382.16 → 1386.38] and like labelling topic names with generative models and that sort of thing.
[1386.46 → 1392.98] Like when you come to something like that, how do you parse through like this intuition around,
[1393.26 → 1396.42] well, is this a situation where I'm like chaining multiple models together?
[1396.56 → 1400.16] Is this a situation where I really need to focus on prompt engineering?
[1400.16 → 1404.50] Is this a scenario where maybe I should be focused on fine-tuning?
[1404.88 → 1413.66] Any sort of guidance or thoughts around like how to develop the intuition around that sort of solution?
[1413.72 → 1417.26] Maybe part of it is just experience, but any suggestions around that?
[1417.60 → 1417.72] Yeah.
[1417.94 → 1420.40] I'm in complete agreement to what you said.
[1420.50 → 1427.20] There is this frontier forming between where you train models and where you're just a user of models
[1427.20 → 1434.94] because of just the very high quality of pre-trained models and their ability to solve general problems.
[1435.04 → 1436.56] So they're a general problem-solving.
[1437.12 → 1440.26] Vast majority of my work is above this frontier.
[1440.42 → 1442.50] So not on the modelling layer.
[1442.88 → 1449.44] I would want to explore what is possible with pre-trained models, generally without a fine tune.
[1449.44 → 1456.50] And that is aided by just the surprising thing of these large generative language models.
[1457.12 → 1460.96] They do few-shot generation really well.
[1461.48 → 1466.06] So if you give them three or five examples of a type of generation or a style of generation that you want,
[1466.78 → 1472.10] they tend to catch on to that and give you something that is good enough for a lot of use cases.
[1472.10 → 1476.16] And then, you know, I know that fine-tuning would be the next step to that.
[1476.34 → 1484.64] So if that is not enough and if there's a use case where, okay, I have, you know, 500 labelled examples or a thousand,
[1485.10 → 1487.86] that's when I would sort of try to reach to fine-tuning.
[1488.04 → 1495.66] But in context of just providing a few examples to the model really helps solve a lot of use cases.
[1495.66 → 1501.84] And so, yes, the solution sort of aspect is where the headspace sort of, you know, try to think about.
[1502.80 → 1508.70] Just using the APIs of these models and, yeah, how to chain them together,
[1508.92 → 1513.12] how to think about, yeah, fine-tuning and not fine-tuning, but let's say embeddings
[1513.12 → 1519.74] and then using those embeddings for specific tasks for retrieval and then chaining that with generation.
[1519.74 → 1524.92] So this is a vastly underexplored and, let's say, new frontier.
[1525.38 → 1531.74] Because you can completely spend 40 years just learning the training layer and the various model architectures
[1532.26 → 1536.82] and the various ways to improve the data and fix the data.
[1536.92 → 1540.60] So we need people in all heights of the stack.
[1540.94 → 1546.86] But then the engineers right now have this widely available sort of underexplored area
[1546.86 → 1551.38] of what can you do with pre-trained models, a lot of them sorts of via APIs.
[1551.84 → 1554.84] And you can definitely do a lot.
[1555.54 → 1559.32] Could you just give people maybe who aren't familiar with Cohere
[1559.32 → 1564.36] some general intro to what Cohere is trying to do and what they offer?
[1564.72 → 1565.64] Absolutely, yes.
[1565.88 → 1567.10] Glad to hear that.
[1567.56 → 1570.40] Cohere offers an API for large language models.
[1570.40 → 1577.02] And the goal there is to make using language models easier for every developer or company out there
[1577.02 → 1582.06] without thinking about hiring an army of people to train large transformers.
[1582.70 → 1586.42] Our founders came out of Google Brain, and one of them was the co-author of the Transformers paper.
[1586.98 → 1590.74] And we have teams that are focused on training, let's say, two kinds of models.
[1590.86 → 1592.90] So the generation large GPT models.
[1593.60 → 1598.00] We train, let's say, both of these families in-house and continue to develop and improve them.
[1598.00 → 1601.18] And the other family is text embedding models.
[1601.32 → 1607.10] And these are the ones that can power use cases like neural search, semantic search, text classification.
[1607.54 → 1613.22] So if you want to classify messages by topic or by sentiment, they're very sort of capable in that.
[1613.32 → 1619.38] And the latest release has been the multilingual embedding model that supports over 100 languages.
[1619.48 → 1622.40] So if you want to do semantic search or neural search,
[1622.40 → 1632.58] you don't have to build 100 different pipelines for each language that does, I don't know, stemming and, you know, very language-specific pipelines.
[1632.58 → 1637.74] You can just throw it all at the embedding model and just retrieve, you know, the best results.
[1638.36 → 1641.92] And so that's the core tech, and the company offers all of that via API.
[1642.26 → 1646.46] And, yeah, we invest a lot in the content and educational side.
[1646.58 → 1649.20] It's still an area that is quite new.
[1649.20 → 1653.16] So large language models as a service is a new brand of company.
[1653.38 → 1655.26] It's only been around for, you know, two years.
[1655.40 → 1661.60] And so, yeah, we focus a lot on the educational side of the various concepts that are needed there
[1661.60 → 1666.74] to help both developers but also a general audience capture and build those intuitions.
[1666.86 → 1671.88] And that's, you know, something that companies had to do throughout the development of technology.
[1671.88 → 1677.24] So the majority of executives now would know what an API is, for example.
[1677.38 → 1684.26] But, you know, 15 years ago or maybe 20 years ago, API or big data or cloud hosting were all sorts of, you know,
[1684.30 → 1687.54] deeply technical words or words that, you know, didn't yet develop.
[1687.70 → 1693.72] And that is the same now with things like embedding and fine-tuning and base model, yeah, language model.
[1694.34 → 1696.86] And so, yeah, definitely the education is a part of that.
[1696.86 → 1703.04] And a lot of it is just us, you know, learning with our developer community and sharing the common lessons.
[1703.72 → 1709.14] So developer number 10,000 doesn't have to repeat the mistakes of the previous developers.
[1709.52 → 1711.26] We're really passionate about that as well.
[1711.58 → 1711.70] Yeah.
[1711.86 → 1718.68] Part of the advantage of having some of this, and I'd be curious to hear your thoughts on this as well.
[1718.68 → 1726.10] So, you know, going back to, like, something I said earlier when I was first learning about transformers and trying to get hands-on with these things,
[1726.10 → 1733.12] like, there was no, like, easy cloud API for me to just, like, access and use.
[1733.24 → 1742.16] I think now, like, even for open models, that's shifting a lot where you can, you know, host things on Hugging Faces Inference API.
[1742.16 → 1745.80] Or you could, you know, use any number of these services.
[1745.80 → 1748.54] So you could use Cohere's large language models.
[1748.88 → 1754.34] You could use, like, Replicate and what they have in their cloud APIs and that sort of thing.
[1754.46 → 1762.14] So a lot of these are available now where it's a few lines of code, and you're able to access the API.
[1762.14 → 1775.58] What do you think are the implications of that for, you know, how people are thinking about using models maybe differently than they thought in the past because of these access patterns?
[1775.86 → 1781.72] Maybe it's fewer people are thinking about the training side and just, like, chaining.
[1782.02 → 1783.54] I don't think it's an accident.
[1783.66 → 1786.74] We've seen a lot of, like, chaining things recently.
[1786.74 → 1788.04] But, yeah, I don't know.
[1788.16 → 1804.40] I'm curious to hear about your thoughts on the implications of how this landscape is changing to where, like, we've kind of gone from, oh, let me download model weights to, like, I could chain this API together with this API and that sort of thing.
[1804.96 → 1816.30] I mean, definitely it makes it a lot easier for a much larger group of people to start experimenting with these models because it just lowers the barrier of entry so much.
[1816.30 → 1828.28] And it enables people to not think about moving tensors across GPUs and watching out for GPUs running out of memory and updating model weights.
[1828.54 → 1830.30] And it's just another abstraction.
[1830.46 → 1833.56] And you can think about it just like every other cloud service out there.
[1833.66 → 1844.10] So if you want to build a new website, you no longer need to buy a physical machine, ship it to a data centre, maybe go physically to that data centre and sort of, you know, put the code on.
[1844.10 → 1848.16] And it's been abstracted away as a service you can reliably access.
[1848.70 → 1854.22] Somebody else has the world's, say, foremost experts making that service reliable for you.
[1854.26 → 1860.06] And you can focus on your core business problem, the core sort of product that you want to do.
[1860.06 → 1873.02] And knowing that these other pieces are there and are being handled by people whose sole job is to, you know, maintain the quality and increase the quality of these models and the uptime.
[1873.02 → 1878.72] And this is especially a factor when these models are massive.
[1878.96 → 1882.38] They need to be on so many different machines and GPUs.
[1882.46 → 1886.42] And it's such a hassle to deploy your own model.
[1886.58 → 1892.54] Like you need a PhD maybe to really wrap your head around everything that is involved in something like.
[1892.54 → 1896.96] And so, yeah, it just frees up people to think about, okay, this is an API.
[1897.54 → 1903.66] Think about the frontier of the next level of services that are now finally possible that weren't possible before.
[1903.82 → 1907.30] And let's say we saw new industries come out of these developments in AI.
[1907.42 → 1914.34] So AI writing assistance, for example, is a type of industry where there are so many companies now that didn't exist before.
[1914.34 → 1924.52] And these companies just rely on, in general, rely on APIs, and they can focus on really creating the best, you know, domain knowledge for them to help their customers.
[1924.60 → 1935.72] So it really helps in the specialization and sort of that abstraction of not having to worry about this lower layer in the stack where others are sort of handling it for you.
[1935.72 → 1947.08] And fine-tuning becomes as easy as uploading a text file rather than, you know, a process of babysitting a model for a week to see, you know, what happens.
[1947.70 → 1960.36] And so that definitely increases the cycle of experimentation, but also the ease of deployment in accelerates, let's say, the coming of the next generation of products that are just now possible.
[1960.36 → 1970.14] Yeah, and one of the things that we talked about before we started recording was some of your excitement around like multimodal models and where those are going.
[1970.30 → 1976.12] I know that's also increasingly easy to kind of like tie different modalities together.
[1976.46 → 1979.32] I think the light bulb is going off for a lot of people.
[1979.38 → 1987.82] I even just had a conversation yesterday where someone was talking to me about like, oh, a large language model, could it do this or that like for their use case?
[1987.82 → 1993.02] And I said, yeah, but like what if you just add the image component on as well?
[1993.02 → 2005.56] Like you can, you know, generate the copy for your ad and the image for your ad, you know, with generated text and that sort of thing, which I know a lot of people are trying and a bunch of other things too.
[2005.56 → 2009.30] So what's on your mind in terms of kind of multimodality?
[2009.48 → 2013.54] I know you've written a lot about Stable Diffusion and other things recently.
[2013.54 → 2023.58] Where's your mind with respect to that, and what are some of the use cases that you're thinking of or the sort of applied things that are interesting to you in that space?
[2023.58 → 2035.08] Yeah. So on the research front, I've written about NATO, DeepMind's NATO model that does images and text and a lot of other modalities, which is an interesting research development.
[2035.22 → 2041.70] On the more applied side, we've released a notebook that does a little bit of prompt chaining.
[2041.70 → 2052.48] So a few researchers from DeepMind had this paper called Dramatic where they, you know, shared a system and a bunch of prompts that uses language models to write a screenplay.
[2052.80 → 2054.80] And it doesn't write it from one prompt.
[2054.96 → 2060.58] It's, you know, seven different prompts that do different things of the story, and then you end up with the screenplay.
[2060.66 → 2066.18] So there's a prompt to generate the characters and the prompt to generate the setting and then the beats of the story.
[2066.18 → 2078.76] And so you build this knowledge hierarchy and then, and so we have a notebook that showcases how to do that with Coheres models, but also plug in some calls to Stable Diffusion models to generate.
[2078.92 → 2080.76] Okay. So these are the descriptions of the characters.
[2081.04 → 2082.72] What might these characters look like?
[2083.14 → 2085.80] So that is an AI image generation sort of flow.
[2086.18 → 2090.80] This is a description of a setting where the part of the story takes place.
[2090.96 → 2093.26] How can we sort of visualize it enough?
[2093.26 → 2106.34] And these are sort of the flows, and we see, you know, libraries kind of like a line chain that are empowering a lot of this chaining of the various text models, but also potentially image generation models.
[2107.22 → 2110.34] So, yeah, that's the most, the use case that I went down.
[2110.64 → 2119.04] And it was only really possible because, you know, like for me to have a quick time to experiment with them because there are APIs that do them.
[2119.04 → 2127.98] So on the Stable Diffusion front, I can share this code because it's an API call to, like, say, stability AIs, the Stable Diffusion models.
[2128.60 → 2133.14] But I've been wanting to do that with Midjourney, but Midjourney does not have an API that you can call.
[2133.28 → 2133.98] I have to do it.
[2133.98 → 2135.86] You have to do it through, like, Discord, for example.
[2135.86 → 2143.02] And so that's also, let's say, differentiating factor for these various products, you know, which ones support API access, which don't.
[2143.14 → 2149.68] So it will factor into, let's say, developer adoption for them on the infrastructure layer.
[2150.10 → 2155.04] But, yeah, that would be specifically the one that I've experimented with the most.
[2155.04 → 2155.60] Awesome.
[2155.92 → 2165.76] As we kind of wrap up here, usually we ask our guests sort of, like, what's on their mind moving into the next, you know, six months or so?
[2165.90 → 2167.98] What are you most excited about?
[2168.10 → 2170.30] What have you not explored yet?
[2170.38 → 2174.40] But what's, like, on the top of your list to dive into?
[2174.78 → 2175.62] Any thoughts?
[2176.34 → 2181.68] Yeah, I'm really excited about use cases that use both generation and embedding in the same sort of flow.
[2181.68 → 2183.74] That's one area where I think about a lot.
[2183.92 → 2190.86] And let's say the topic modelling and, let's say, cluster naming use case is one of them.
[2191.06 → 2195.84] And we've open sourced a library called Topically that does exactly that.
[2195.88 → 2198.08] So that's one area where I'm working closely.
[2198.18 → 2208.24] And I think these models can help us really understand large collections of data using that and, you know, create interesting visualizations of them as well.
[2208.24 → 2217.06] So, yeah, for me, it's mostly, yeah, the interaction of this sort of two systems, hopefully, let's say, supporting multiple languages as well.
[2217.26 → 2219.08] So multimodality is interesting.
[2219.32 → 2226.34] Also multilingualism is interesting for, you know, systems that can support even more and more data that's out there.
[2226.78 → 2231.04] I think these are most likely the ones that are just top of mind for me at this time.
[2231.58 → 2231.88] Awesome.
[2231.88 → 2235.58] Well, thanks so much for taking time to chat, Jay.
[2235.68 → 2244.52] I'm glad we got to do this and hope to have you back on the show in a year so we can talk about all the fun things you've explored in the interim.
[2245.08 → 2246.00] So thanks a lot.
[2246.78 → 2247.18] Amazing.
[2247.30 → 2247.94] Thank you so much.
[2247.98 → 2250.68] So good to catch up with you and chat about all of this.
[2250.86 → 2252.64] I look forward to speaking again.
[2252.64 → 2264.16] Thank you for listening to Practical AI.
[2264.72 → 2268.50] Your next step is to subscribe now, if you haven't already.
[2268.92 → 2274.96] And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[2275.44 → 2280.34] Thanks once again to Vastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2280.34 → 2284.72] Check out what they're up to at Fastly.com and Fly.io.
[2285.12 → 2290.44] And to our Beat Freakin' residents, Break master Cylinder, for continuously cranking out the best beats in the biz.
[2290.72 → 2291.62] That's all for now.
[2291.90 → 2293.04] We'll talk to you again next time.
