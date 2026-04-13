[0.00 → 8.74] Welcome to the Practical AI Podcast, where we break down the real-world applications
[8.74 → 13.64] of artificial intelligence and how it's shaping the way we live, work, and create.
[13.88 → 19.14] Our goal is to help make AI technology practical, productive, and accessible to everyone.
[19.48 → 23.54] Whether you're a developer, business leader, or just curious about the tech behind the
[23.54 → 25.12] buzz, you're in the right place.
[25.12 → 29.84] Be sure to connect with us on LinkedIn, X, or Blue Sky to stay up to date with episode
[29.84 → 33.02] drops, behind-the-scenes content, and AI insights.
[33.36 → 35.88] You can learn more at practicalai.fm.
[36.20 → 37.50] Now, on to the show.
[39.60 → 44.22] Well, friends, when you're building and shipping AI products at scale, there's one constant.
[44.84 → 45.32] Complexity.
[45.72 → 50.48] Yes, you're bringing models, data pipelines, deployment infrastructure, and then someone
[50.48 → 52.94] says, let's turn this into a business.
[53.46 → 54.72] Cue the chaos.
[54.90 → 59.54] That's where Shopify steps in, whether you're spinning up a storefront for your AI-powered
[59.54 → 62.66] app or launching a brand around the tools you've built.
[63.04 → 68.40] Shopify is the commerce platform trusted by millions of businesses and 10% of all U.S.
[68.40 → 73.38] e-commerce, from names like Mattel, Gymshark, to founders just like you.
[73.94 → 79.60] With literally hundreds of ready-to-use templates, powerful built-in marketing tools, and AI that
[79.60 → 84.16] writes product descriptions for you, headlines, even polishes your product photography.
[84.16 → 86.34] Shopify doesn't just get you selling.
[86.66 → 88.20] It makes you look good doing it.
[88.68 → 89.34] And we love it.
[89.60 → 90.74] We use it here at Changelog.
[90.94 → 93.36] Check us out, merch.changelog.com.
[93.58 → 94.86] That's our storefront.
[95.28 → 97.18] And it handles the heavy lifting, too.
[97.52 → 101.66] Payments, inventory, returns, shipping, even global logistics.
[102.34 → 106.24] It's like having an ops team built into your stack to help you sell.
[106.24 → 109.40] So if you're ready to sell, you are ready for Shopify.
[110.02 → 116.70] Sign up now for your $1 per month trial and start selling today at Shopify.com slash practical
[116.70 → 117.12] AI.
[117.80 → 122.34] Again, that is Shopify.com slash practical AI.
[136.24 → 141.12] Welcome to another fully connected episode of the Practical AI Podcast.
[141.58 → 143.44] This is Daniel Whiten ack.
[143.56 → 149.62] I am CEO at Prediction Guard, and I'm joined by Chris Benson, my co-host, who is a principal
[149.62 → 151.90] AI research engineer at Lockheed Martin.
[152.58 → 158.66] And in these fully connected episodes, or it's just Chris and me, we try to dig into a few topics
[158.66 → 164.42] or deep dive into some learning resources that will help you level up your AI machine learning
[164.42 → 164.86] game.
[164.86 → 167.02] Looking forward to this one, Chris.
[167.22 → 174.04] I think in reflecting before the episode, both of us going into American Thanksgiving,
[174.40 → 181.42] which is tomorrow as we're recording this, but going in with a lot of gratitude for the
[181.42 → 181.72] year.
[182.04 → 190.68] Just a lot happens in life, and it's a nice time to kind of reflect and see the blessings
[190.68 → 192.88] that we have at Thanksgiving.
[192.88 → 201.20] And yeah, what a blessing to just keep doing this show for going on eight years now.
[201.50 → 202.26] It's been a moment.
[202.26 → 212.50] But having a lot of fun, stepping on a few mines along the way, but having fun generally.
[212.72 → 216.56] And I think, yeah, thankful to our listeners as well.
[216.80 → 221.78] Just to take a moment to say thank you for sticking with us all these years.
[222.28 → 226.32] Chris and I have a lot of cool plans for the coming year.
[226.32 → 229.38] And there's energy behind the show.
[229.46 → 232.00] Lots of ideas going on that we'll talk about soon.
[232.34 → 235.52] But yeah, thank you to our listeners for sticking with us.
[235.70 → 236.40] Couldn't say it better.
[236.58 → 238.54] Thank you to the listeners for sticking with us.
[238.86 → 244.28] And I got to say, these fully connected shows in a lot of ways are so much fun.
[244.42 → 249.66] They're among my very favourites because we get to talk to these most amazing guests in a typical
[249.66 → 253.22] episode, you know, where you're like talking to some of the smartest people in the world
[253.22 → 256.58] and being able to kind of understand how they see it and learn.
[256.80 → 259.48] And I know our listeners go along for the ride on that.
[259.76 → 264.08] But I also love when we just, you know, it's the Wednesday afternoon before Thanksgiving for
[264.08 → 265.52] you and me as we're recording this.
[265.90 → 268.04] I know people will be listening to it just after Thanksgiving.
[268.56 → 271.28] But it's a lot of fun just to jump into the conversation.
[271.80 → 274.42] And I know we have some fun things to hit today.
[274.42 → 277.22] So I'm relaxed and looking forward to it, Daniel.
[277.96 → 279.12] Yeah, yeah, for sure.
[279.34 → 285.92] And I don't know a more exciting topic for the Thanksgiving dinner table than document
[285.92 → 290.72] processing, which is what I kind of brought forward today.
[291.32 → 296.76] I guess what I was realizing, Chris, is we talk a lot about large language models.
[297.48 → 302.74] We've talked a lot about we have talked a lot about computer vision type of things on the
[302.74 → 307.54] show, maybe not as much recently, but certainly over the years.
[307.54 → 313.94] We've talked about all the kind of chatbot stuff and all of that.
[313.94 → 322.06] But I think kind of lurking below the surface of a lot of work in industry is document processing.
[322.56 → 329.10] And as the years have gone along, and we've kind of entered into the generative AI kind of
[329.10 → 336.56] revolution, there has been also this kind of stream of innovations in relation to processing
[336.56 → 339.92] documents in an automated way with models.
[339.92 → 349.08] And of course, that reaches very practical places in terms of everyday business work.
[349.48 → 349.62] Right.
[349.62 → 357.90] I think often the most valuable workflows that people have day to day or maybe the most annoying
[357.90 → 362.12] ones is, you know, this person emails me with this document.
[362.32 → 368.22] I've got to, you know, extract this or do this or create a summary of that.
[368.22 → 376.20] Or I have new documents that are, you know, regulations related to compliance and I need to process
[376.20 → 379.34] them and get them, you know, into somewhere.
[379.54 → 384.86] And that's really kind of at the centre of a lot of what happens in businesses day to day.
[385.02 → 392.88] So, yeah, I thought it would, you know, as we hopefully aren't yet in a comma after
[392.88 → 398.16] eating too much turkey, we could, you know, use our use this time when we're alert to talk
[398.16 → 398.94] about some of that.
[399.24 → 400.46] You know, a great point there.
[400.46 → 404.88] And before, like, I kind of hate the, the, the name, you know, like document processing.
[404.88 → 409.24] And I think, you know, like before everyone out there goes to sleep, you know, turns us
[409.24 → 412.90] off and goes, oh my God, they're talking about document processing and goes to sleep.
[413.02 → 414.46] This is pretty cool stuff.
[414.64 → 416.94] And it's important because it's modelling wise.
[417.10 → 418.26] Yeah, absolutely.
[418.54 → 420.28] And, and it, it, it is productive.
[420.28 → 425.24] And, you know, we pride ourselves, you know, on, on bringing that, that, you know, a practical,
[425.42 → 427.64] productive and accessible approach to it.
[427.64 → 431.90] And, and I think that's really important is like, I think one of the differences in
[431.90 → 435.66] the conversations we have on the show versus some other shows is the other ones tend to
[435.66 → 437.86] chase the headlines and the glam and stuff.
[438.24 → 443.54] And we're really focused on like getting people into this technology so that they can
[443.54 → 445.38] use its day to day in a fun way.
[445.70 → 451.46] And, and so like before you turn off and go, oh, I'm going to turn off for turkey on document
[451.46 → 452.00] processing.
[452.42 → 453.90] This is pretty cool stuff.
[453.90 → 458.78] And as Daniel said, this has been going on, we just don't get the headlines anymore
[458.78 → 459.56] like it used to.
[459.64 → 464.46] And so it's really worth diving into and saying, hey, look at what's possible now versus the
[464.46 → 465.60] last time we talked about it.
[465.88 → 466.00] Yeah.
[466.16 → 471.72] And probably what initially prompted this is of course, I mean, we've been working with
[471.72 → 477.38] some of these models internally, but also DeepSeek did release a DeepSeek OCR model,
[477.38 → 483.86] which people have been talking a lot about, which is, which represents at least part of
[483.86 → 489.34] this stream of work that's been going on around document processing models.
[489.56 → 495.72] Now, just so people kind of have, I guess, a little bit of background or jargon kind of
[495.72 → 496.36] where we're headed.
[496.36 → 503.16] My thought is we really need to kind of pick apart some of these different kinds of, of
[503.16 → 507.80] modelling, how they fit in and where they're practical, maybe where they're not practical.
[508.44 → 516.54] And in particular, there is OCR, which has been around for the longest, I guess, in terms
[516.54 → 520.64] of the things that we'll talk about, which is optical character recognition.
[520.64 → 521.80] That's what that stands for.
[521.80 → 529.64] Then there are language vision models, which is something that has happened or LVMs.
[529.98 → 537.20] Then there are, I guess, document structure type of models, kind of like a docking.
[537.34 → 538.94] People might've heard of docking.
[539.14 → 545.54] And then finally, there's kind of this latest model, DeepSeek OCR, which is different from
[545.54 → 549.44] kind of like what people might think of in terms of OCR.
[549.44 → 555.32] And so there's these, these different kind of categories or families of, of methodologies
[555.32 → 555.76] here.
[555.76 → 560.92] And there's really, like you say, Chris, a lot, a lot happening in, in these different
[560.92 → 564.98] areas, but that's, that's kind of where we're headed in, in the conversation, I guess, for
[564.98 → 569.32] those, for those listening as there's kind of pick apart some of these things.
[569.32 → 578.62] I don't know, Chris, how long, I mean, I, I kind of remember OCR happening for a very
[578.62 → 579.30] long time.
[579.40 → 585.36] I mean, I, I didn't grow, neither one of us, I think, grew up with computers, at least
[585.36 → 589.04] that had OCR on them or computers in general.
[589.04 → 596.12] I do remember in grad school, you know, processing some, you know, papers or other things and
[596.12 → 602.90] applying some type of OCR, maybe in some tools on these, but yeah, what, what's your, what's
[602.90 → 603.60] your history there?
[603.86 → 604.00] Yeah.
[604.06 → 608.94] Well, I mean, early OCR was really not very good, you know, and this was kind of, you
[608.94 → 614.08] know, certainly before kind of the current generation of AI, and I'm using generation very
[614.08 → 619.90] broadly here, like the last 15 years, and it's come a long way with these new technologies
[619.90 → 620.48] and stuff.
[620.58 → 626.04] I know when I was younger, some of the kind of pre AI OCR technologies just were like,
[626.42 → 631.18] I remember trying them when I was younger and kind of going really not working for like,
[631.18 → 633.68] it's almost costing me more effort than it's worth it.
[634.20 → 636.12] So things have changed dramatically.
[636.30 → 640.06] I mean, it's so good now and there are so many approaches to it as we're, as we're going to
[640.06 → 640.50] dive into.
[641.32 → 641.46] Yeah.
[641.60 → 641.76] Yeah.
[641.76 → 647.80] And I, and I think that maybe a good starting point for that, if we just start with OCR
[647.80 → 654.74] is really thinking about the processing pipeline and the different components that are involved
[654.74 → 655.00] in it.
[655.00 → 660.64] Cause that really drives what compute is needed, how fast it is, how performant it is, you
[660.64 → 663.50] know, and it kind of distinguishes it as a category.
[663.50 → 669.80] So if we just start with OCR, I think we could do that now, just by way of reference in terms
[669.80 → 676.74] of like how things are processed through a kind of quote, classical OCR model or a typical
[676.74 → 677.52] OCR model.
[677.52 → 683.04] These would be things like Tesseract or paddle OCR, these sorts of technologies that we're
[683.04 → 683.72] thinking of.
[684.58 → 687.78] What, what happens is an image is input.
[687.78 → 693.40] And then ideally kind of text or characters or output.
[693.72 → 699.06] If we just contrast that, cause everyone's talking about LLMs now that the typical processing
[699.06 → 704.40] pipeline with LLMs is, you know, not images come in, but text comes in.
[704.56 → 706.96] That text is split apart into tokens.
[706.96 → 711.62] Those tokens are assigned indices, like within a vocabulary.
[712.96 → 722.76] Those, that kind of array of indices is embedded into a dense representation by a transformer based
[722.76 → 723.66] model often.
[724.38 → 732.90] And then what is predicted on the output side is a, is a, an array of probabilities corresponding
[732.90 → 738.16] to different tokens such that you can know what is the most probable next token coming
[738.16 → 738.74] out of the model.
[738.74 → 743.64] So you kind of have text come in, that text is split apart into tokens that's embedded.
[743.92 → 748.42] And then output are these probabilities of next token.
[748.52 → 754.76] So if we just contrast that with the OCR model, first, we have a different type of input,
[754.92 → 755.08] right?
[755.12 → 759.36] We have an image and that image is made of pixels.
[759.36 → 766.46] And often, so we have this image, it's made of pixels in the output, actually not dissimilar
[766.46 → 768.46] to the LLM.
[768.64 → 771.40] There is an output of probabilities at the end.
[771.50 → 775.20] It's just an output of kind of probabilities of characters.
[776.10 → 783.20] So what happens is if you look at a big image, it might have regions of characters in it or
[783.20 → 783.70] words.
[783.70 → 790.12] And what happens in the OCR model is you take that big image with, with a lot of characters,
[790.42 → 794.86] there might be some pre-processing on the image, like a resizing or something.
[794.86 → 804.20] But then there is one kind of model that detects the area or regions where there are kinds of
[804.20 → 806.62] characters or text, text regions.
[806.62 → 812.80] And then you take each of these text regions, and you put it through like a convolutional
[812.80 → 814.62] neural network or an LSTM.
[814.84 → 823.68] And then that outputs through a sequence model, a probability of characters or the probability
[823.68 → 826.36] of what character corresponds to that region, right?
[826.40 → 833.40] So essentially that OCR model, it's really just looking at that big image, determining where
[833.40 → 836.12] there are characters or text regions.
[836.12 → 843.16] And then for each of those predicting what that character or text region is, right?
[843.18 → 850.90] So that's how the processing goes, which in some ways is kind of seems kind of almost
[850.90 → 852.30] brute force, right?
[852.62 → 855.82] You're just, you're splitting it apart into all of these regions, right?
[856.08 → 861.34] And as you were talking though, I was also thinking back over the history of the show and,
[861.34 → 865.42] you know, we're talking like, this is the first time I think you've said LSTM and, you
[865.42 → 867.38] know, in a while and in a bit.
[867.52 → 867.72] Yeah.
[867.80 → 872.62] How many years has it been since we talked about that and, and recurrent neural networks, you
[872.62 → 878.68] know, which were also involved in, and, and then kind of transformers also starting to
[878.68 → 879.60] bridge the gap there.
[879.94 → 880.38] Wow.
[880.86 → 882.54] Taking us back a little ways there.
[882.74 → 884.62] So taking us back.
[884.76 → 885.06] Yeah.
[885.06 → 892.80] So if you, this is really kind of in a lot of ways, a brute force type thing, you're really
[892.80 → 895.48] splitting apart that image into these different regions.
[895.48 → 901.90] And then for each kind of trying to detect which character now, similar to what you were
[901.90 → 908.38] saying, we're talking about maybe convolutional models or architectures, maybe LSTMs, which
[908.38 → 912.66] is a long short term memory recursive type of network.
[913.48 → 920.36] This kind of traditionally in these tools, like the OCR tools are rather small models
[920.36 → 922.36] by today's standards.
[922.36 → 929.18] And as such, even though it's kind of, you're brute forcing all of these characters, they
[929.18 → 932.28] are fairly efficient in terms of where you can run them.
[932.36 → 934.46] So I can run one easily on my laptop.
[934.46 → 935.64] I can run it on a CPU.
[935.74 → 937.98] I don't have to have a large GPU.
[938.60 → 938.72] True.
[938.98 → 944.08] It's, you know, it's interesting is that evolution and the different kind of branches of possibility
[944.08 → 947.42] in terms of how you might approach the problem have developed.
[948.20 → 949.26] Any thoughts?
[949.26 → 954.58] Do you have any, any kind of thoughts around kind of like as we, as we went from LSTMs and
[954.58 → 960.68] got to convolutional and then Transformers started making an impact on that, you know,
[960.68 → 964.90] maybe after we come out of the break, we can talk a little bit about kind of how those,
[965.16 → 970.18] how those evolved and why the different selections became kind of primary over time.
[970.18 → 979.44] Well, friends, it is time to let go of the old way of exploring your data.
[979.72 → 980.64] It's holding you back.
[980.98 → 983.00] But what exactly is the old way?
[983.34 → 988.22] Well, I'm here with Mark Lupus, co-founder and CEO of FBI, a collaborative analytics
[988.22 → 990.26] platform designed to help big explorers like yourself.
[990.58 → 992.58] So Mark, tell me about this old way.
[993.08 → 998.10] So the old way, Adam, if you're a product manager or a founder, and you're trying to get
[998.10 → 1002.26] insights from your data, you're, you're wrestling with your Postgres instance or Snowflake or
[1002.26 → 1003.36] your spreadsheets.
[1003.48 → 1007.50] Or if you are, and you don't maybe even have the support of a data analyst or data scientist
[1007.50 → 1009.08] to, to help you with that work.
[1009.24 → 1014.94] Or if you are, for example, a data scientist or engineer or analyst, you're wrestling with
[1014.94 → 1020.60] a bunch of different tools, local Jupyter notebooks, Google Cola, or even your legacy BI to try
[1020.60 → 1024.18] to build these dashboards that, you know, someone may or may not go and look at.
[1024.18 → 1029.94] And in this new way that we're building at FBI, we are creating this all-in-one environment
[1029.94 → 1034.88] where product managers and founders can very quickly go and explore data regardless of
[1034.88 → 1035.54] where it is, right?
[1035.58 → 1038.58] So it can be in a spreadsheet, it can be in Airtable, it can be in Postgres, Snowflake,
[1038.86 → 1043.76] really easy to do everything from an ad hoc analysis to much more advanced analysis if,
[1043.94 → 1045.24] again, you're more experienced.
[1045.72 → 1050.82] So with Python built in, you know, Python built in right there, and our AI assistant, you can
[1050.82 → 1052.82] move very quickly through advanced analysis.
[1052.82 → 1058.76] And a really cool part is that you can go from ad hoc analysis and data science to publishing
[1058.76 → 1065.18] these as interactive data apps and dashboards, or better yet, at delivering insights as automated
[1065.18 → 1070.98] workflows to meet your stakeholders where they are in, say, Slack or email or spreadsheets.
[1071.12 → 1074.22] So, you know, if this is something that you're experiencing, if you're a founder or a product
[1074.22 → 1078.36] manager trying to get more from your data or for your data team today, you're just underwater
[1078.36 → 1083.24] and feel like you're wrestling with your legacy, you know, BI tools and notebooks, come check out
[1083.24 → 1084.30] the new way and come try out FBI.
[1084.30 → 1085.38] There you go.
[1085.52 → 1088.86] Well, friends, if you're trying to get more insights from your data, stop wrestling with it,
[1089.12 → 1091.80] start exploring it the new way with FBI.
[1092.12 → 1094.30] Learn more and get started for free at fabi.ai.
[1094.30 → 1098.40] That's F-A-B-I dot A-I.
[1098.64 → 1100.24] Again, fabi.ai.
[1105.24 → 1106.54] Yeah, Chris.
[1106.72 → 1115.02] So you were just kind of getting into, I guess, maybe why, assuming we have OCR, right?
[1115.02 → 1121.68] That does work in the sense that you can predict characters, you can pick out these text regions.
[1122.14 → 1125.92] So, you know, OCR models have obviously got better over the years.
[1126.06 → 1128.48] So why is there a need for something else?
[1128.56 → 1132.84] Why is there a transition to maybe other architectures or other things?
[1133.18 → 1140.26] So what I would say is there's kind of, if you think about that process of the image coming in
[1140.26 → 1147.66] and you're splitting apart those text regions, you kind of end up with all of this kind of plain text output.
[1148.52 → 1157.22] And any sort of logic around the reconstruction of that document, especially related to the layout of the document,
[1157.80 → 1162.46] is problematic, I would say.
[1162.46 → 1171.70] And I would say these are often highly dependent on the actual quality of the pixels that are input.
[1171.76 → 1173.54] Remember, the pixels are input here.
[1173.72 → 1179.44] And often the images are kind of resized on the inputs to these models,
[1179.46 → 1182.28] or they need to be just in terms of the input size.
[1182.28 → 1188.48] So you've got kind of this combination of problems of not having an understanding of the layout,
[1188.54 → 1194.98] but also requiring kind of clean scans of the documents, if you will,
[1195.06 → 1201.44] which is definitely a drawback of this approach, I would say.
[1201.86 → 1204.98] Yeah, I mean, I can remember back in the day with the traditional OCR,
[1205.28 → 1207.76] I mean, that was not just a problem, but it was constant.
[1207.76 → 1214.24] You know, you would use OCR on a document, and you had to pretty meticulously go through the document afterwards
[1214.24 → 1217.16] to correct a lot of the error on that.
[1217.32 → 1222.46] And, you know, that didn't change really until we got past the traditional into more of the vision-based model.
[1222.64 → 1226.46] So definitely seeing the progression there.
[1226.92 → 1227.48] Yeah, yeah.
[1227.56 → 1236.46] And I mean, that kind of naturally transitions us into one of the things that is now a part of our world
[1236.46 → 1241.48] and helps with that, at least a part of that problem, the structure and layout problem,
[1242.22 → 1245.56] which are what are called document structure models.
[1246.24 → 1250.32] So the most, or one of the most popular of these is called Docking.
[1250.64 → 1252.40] And there are different families of these.
[1252.52 → 1258.20] Docking, it might be confusing because there are some models that are kind of labelled as Docking models.
[1258.20 → 1265.04] There's also a toolkit called Docking that IBM released, which isn't actually just one model.
[1265.18 → 1270.58] It's a whole series of pipelines and options around document processing.
[1271.12 → 1280.24] But one of the core concepts here, whether it's in use in that library or in reference to a model,
[1280.24 → 1289.00] is that a document structure model in terms of what it does or the differences,
[1289.32 → 1292.14] it actually doesn't do any OCR.
[1292.40 → 1293.88] It doesn't detect text.
[1294.02 → 1298.80] It doesn't convert, you know, images to text and this sort of thing.
[1298.94 → 1308.66] What it does is it tries to predict the structure of the document or a structured representation of the document.
[1308.66 → 1312.64] Because remember with OCR, we don't really have that, right?
[1312.68 → 1319.76] We just have the prediction of these characters and these different, you know, cropping of the image.
[1320.26 → 1327.06] And so with Docking or a similar document structure model, what happens is you have that document that's input,
[1327.94 → 1329.58] a document or an image.
[1329.58 → 1340.80] And then what happens is that a kind of parser extracts layout primitives.
[1341.00 → 1346.30] So that might be like rectangles or certain shapes or vectors or fonts.
[1346.94 → 1352.90] And then a layout model, again, kind of part of this document structure model,
[1353.04 → 1358.96] layout model then makes predictions for what those regions should be classified as.
[1358.96 → 1366.34] So things like, you know, titles or paragraphs or headings or tables, et cetera.
[1366.86 → 1371.70] And then output of the model rather than predicting characters again.
[1371.80 → 1373.28] So I'm not getting text out of this.
[1373.34 → 1374.88] I'm not getting characters or text.
[1375.02 → 1380.04] What I'm getting is a structured output representation of the document,
[1380.18 → 1385.20] usually in kind of JSON, Markdown, HTML format,
[1385.20 → 1389.38] which basically tells me, okay, you put in this document.
[1389.62 → 1392.08] Over here is a table.
[1392.38 → 1393.52] Over here is a title.
[1394.10 → 1396.10] This region corresponds to a heading.
[1396.44 → 1398.02] There's a paragraph over here.
[1398.02 → 1409.58] And that way, when you have these more complex documents, maybe two column papers or white papers with a bunch of tables or data sheets or that sort of thing,
[1409.88 → 1413.12] you kind of have this structure laid out.
[1413.28 → 1415.52] You have the classification of that structure.
[1415.52 → 1425.48] And so actually a docking model or this type of document structure model is often used in combination with an OCR model.
[1425.72 → 1429.14] And it would kind of go like document comes in.
[1429.70 → 1432.26] You detect all the structure of the document, right?
[1432.38 → 1433.60] Oh, here's a table.
[1433.72 → 1434.38] Here's a paragraph.
[1434.62 → 1435.22] Here's a title.
[1435.54 → 1445.36] Okay, well, now let me send that title bit into an OCR model and then actually get the text associated with the title, right?
[1445.36 → 1452.98] And so now you've overcome a little bit of that limitation of the raw OCR by applying this structure on top.
[1453.06 → 1460.30] And you can reconstruct the document, you know, as a Markdown document with all the tables and titles and that sort of thing.
[1460.68 → 1461.04] It's funny.
[1461.18 → 1467.08] As you kind of describe, you're going through the process there as a very loose analogy.
[1467.08 → 1474.06] It reminds me somewhat of, for those of us in the audience who are programmers like you and I,
[1474.54 → 1480.90] it reminds me a little bit of the way programming languages are compiled into this tree-structured format.
[1481.04 → 1487.22] It's called an abstract syntax tree and asked, you know, where it kind of captures what,
[1487.36 → 1493.08] regardless of what the originating language is, it kind of captures the essence of what the program is
[1493.08 → 1496.74] before it's, you know, compiled into the machine code or whatever your target is.
[1497.14 → 1501.10] But it kind of feels like Docking is doing a somewhat, at a higher level, obviously,
[1501.24 → 1506.02] but doing a little bit of a similar thing in terms of capturing all that structure out of the dock.
[1506.52 → 1507.10] Yeah, yeah.
[1507.14 → 1514.00] It would be like the OCR model has an output of character probabilities, right?
[1514.00 → 1517.48] The LLM has an output of token probabilities.
[1517.90 → 1527.02] The document structure model actually has an output of this tree structure or the tree representation of the structure of the document.
[1527.22 → 1535.88] So it's that kind of processing pipeline where you pick apart these layout primitives, and then you classify each one.
[1535.88 → 1544.60] So really, it's kind of main piece of this is the classification piece of each of these elements and then assembling that into this tree structure,
[1544.84 → 1547.56] which, yeah, is certainly very useful.
[1547.96 → 1555.18] I think there's, it's worth noting that this does help you handle more complicated documents.
[1555.64 → 1559.14] It, again, though, it doesn't solve the text extraction piece.
[1559.22 → 1561.98] You still kind of need to add that piece in.
[1561.98 → 1571.58] And often this is more computationally heavy than just raw OCR, which can run on, on CPUs often.
[1571.58 → 1579.10] I think I've run Docking models also on CPU or on constrained environments.
[1580.24 → 1587.36] I think Hugging Face released a small Docking model, which is also geared towards that side of things.
[1587.36 → 1592.52] Obviously, you have the same tradeoffs with any kind of model size.
[1593.00 → 1599.28] The smaller ones maybe don't have the same level of performance, but will run on more constrained environments.
[1599.50 → 1603.90] The larger ones maybe have higher performance, but they might need a GPU to run.
[1603.90 → 1613.74] As we talk about this, would you say that Docking is like still a very modern and current way of doing things, given the fact that Hugging Face is releasing models?
[1614.40 → 1619.70] And are there use cases where you would not necessarily want to go to this in your view?
[1619.94 → 1623.90] Like where might you say, I don't, like I get the benefits that we've talked about.
[1624.26 → 1626.94] Where might we say not the right fit?
[1626.94 → 1638.98] Yeah, I would say that you really kind of want to use this when you need to preserve the structure of the documents that are input.
[1639.36 → 1648.16] And you maybe have complex structures, again, like the data sheets or multi-column or mix of columns and other things.
[1648.28 → 1650.22] This is really useful at that point.
[1650.22 → 1663.54] But if you just have like a raw scan that's relatively clean and all of it's just text, and you need to detect all of that text, then maybe an OCR model is totally fine.
[1663.78 → 1666.64] And, you know, the structure model is overkill.
[1667.12 → 1667.26] Right.
[1667.58 → 1675.46] But, yeah, I would say this is still very much in widespread use now and quite powerful.
[1675.46 → 1681.36] We've used it on a few different projects as well with good success.
[1681.60 → 1694.30] And it is still a model that I would say, even though it's a little bit more computationally expensive than OCR, we'll talk about language vision models and Deeper OCR here in a second.
[1694.30 → 1709.20] It is not that not at the level of computation of those types of models, which means you could still embed it kind of within your application or something, maybe run it on a commodity GPU, that sort of thing.
[1709.28 → 1713.40] So it is still really useful in those ways as well.
[1713.40 → 1730.36] Thinking a little bit about different use cases, you know, we still today, like if you go and use different types of Office tools, you know, I don't necessarily mean Microsoft Office, but that genre of productivity tools, and you're doing file format changes and stuff across.
[1730.36 → 1739.36] I know recently, I think about a week ago, I was trying to move a keynote just into a PowerPoint context.
[1740.54 → 1743.56] And you would think in 2025 we would have gotten past that.
[1743.76 → 1744.22] I didn't.
[1744.52 → 1757.96] Do you think this is something that is either used at some level or could be used at levels in terms of trying to capture that kind of complex structure and get it into a different format without losing the gist of what the communication was?
[1758.32 → 1759.74] Am I on target there?
[1759.74 → 1760.64] Yeah, yeah.
[1760.74 → 1766.26] I think the limitation, I guess, is in how rich that description is, right?
[1766.40 → 1773.98] Like you might get these heading, or you might get these labels like heading, title, paragraph, et cetera, table.
[1774.84 → 1787.92] But ultimately, if you were to need to reconstruct that, you have to decide how you are going to render a table, how you are going to render a title, which may be very different from the original, you know, keynote.
[1787.92 → 1793.94] So let's say the keynote presentation, and you're going and putting it in, you know, Google Slides or something like that.
[1794.02 → 1799.34] So actually that I think that rendering piece is still a quite challenging one.
[1799.34 → 1807.40] What I would say, maybe this is a generalization because we've actually used docking models in other ways than what I'm about to say.
[1807.40 → 1819.74] But one of the very frequent uses of these models is for the processing of documents that are feeding into, let's say, a RAG, a retrieval augmented generation pipeline.
[1819.74 → 1821.14] Why would that be?
[1821.30 → 1837.94] It's sort of because the cleaner and more context relevant you can make that those chunks of text into your RAG system, the better results you're going to get in the responses from the RAG system.
[1837.94 → 1852.42] And so if you're just processing your documents that have some complex structure using OCR, all the text might get jumbled up and thus the knowledge and the context in the document is kind of jumbled up.
[1852.50 → 1857.04] Even though all the pieces are there, they might be out of order, or they might be something like that.
[1857.50 → 1861.00] In the case of RAG, you actually don't need to render anything.
[1861.24 → 1863.64] You just need to parse it well and preserve the structure.
[1863.64 → 1876.04] So actually, I think docking or these document structure models are a perfect way to do that document processing for input to RAG pipelines.
[1876.16 → 1886.60] Because there you probably just need things to be represented well in Markdown or some similar text format, not in a cool PDF that you recreate or something like that.
[1886.60 → 1895.64] Yeah, you know, that I'm just thinking of like, you know, it wasn't too far back, you know, a year, a year and a half and RAG was all new at the time.
[1895.64 → 1898.78] And now it is so embedded into our workflows.
[1899.10 → 1901.38] It lots and lots of organizations out there.
[1901.52 → 1901.78] Yes.
[1901.78 → 1909.98] And I'm thinking about the fact that I wonder how many people out there are using docking in that capacity, you know, as that input to that workflow.
[1909.98 → 1921.14] And it would probably, you know, having the contextual aspect of the information saved structurally in that way would probably, I agree with you.
[1921.18 → 1929.42] I mean, that makes perfect sense intuitively that it would, you would definitely have a RAG system able to give you better answers on that.
[1929.42 → 1932.20] Have you seen that in that use case much out there?
[1932.28 → 1933.60] Or is that very much one-off?
[1933.72 → 1935.08] What's your gut feeling about that?
[1935.16 → 1935.96] Yeah, definitely.
[1936.18 → 1947.68] I would say in particular toolkits like docking, the toolkit, and there are other ones like Market Down, which I think is a toolkit from Microsoft.
[1948.34 → 1950.78] We've used those over and over in RAG systems.
[1950.90 → 1953.36] And I know other people do as well.
[1953.82 → 1957.52] Certainly people also use vision models, which we'll talk about here in a second.
[1957.52 → 1962.60] But I would say, again, in the RAG system, you want to preserve that structure.
[1963.06 → 1964.40] You don't want things out of order.
[1964.76 → 1967.98] But you really don't care how they're rendered necessarily.
[1968.90 → 1971.56] You just need to preserve the structure and ordering.
[1971.84 → 1975.74] And so that works out perfect for RAG systems.
[1975.74 → 1995.54] So most design tools lock you behind a paywall before you do anything real.
[1996.10 → 1998.94] And Framer, our sponsor, flips that script.
[1998.94 → 2009.54] With Design Pages, you get a full-featured professional design experience from vector workflows, 3D transforms, image exporting, and it's all completely free.
[2009.96 → 2015.84] And for the uninitiated, Framer has already built the fastest way to publish beautiful production-ready websites.
[2016.38 → 2019.28] And now it is redefining how we design for the web.
[2019.28 → 2026.82] With their recent launch of Design Pages, which is a free canvas-based design tool, Framer is more than a site builder.
[2027.12 → 2029.08] It is a true all-in-one design platform.
[2029.48 → 2036.06] From social media assets to campaign visuals to vectors to icons, all the way down to a live site.
[2036.52 → 2039.20] Framer is where ideas go live start to finish.
[2039.20 → 2046.26] So if you're ready to design, iterate, and publish all in one tool, start creating for free today at framer.com slash design.
[2046.42 → 2051.04] And use our code practical ai for a free month of Framer Pro.
[2051.40 → 2053.90] Again, framer.com slash design.
[2057.02 → 2059.44] All right, Chris.
[2059.56 → 2067.12] Well, there's a couple of, I guess, variations on the next, you know, types of models.
[2067.12 → 2074.12] Maybe it would be helpful to talk about language vision models or vision language models first,
[2074.12 → 2079.78] and then talk about kind of deep seek OCR, which is kind of a different kind of animal.
[2080.02 → 2082.18] It's not OCR like we talked about before.
[2082.32 → 2085.02] It's not vision model like we're about to talk about.
[2085.66 → 2095.78] But the vision model is actually kind of different, or it's more similar to the LLM than the OCR model, I think.
[2095.78 → 2106.24] So a language vision model, what that means is that the input to the model can actually be an image and a text prompt.
[2106.62 → 2108.82] And so this is often how it works.
[2108.82 → 2116.08] Like if you go into a multimodal kind of chat thing, and you upload an image and say,
[2116.24 → 2117.66] hey, what's going on in here?
[2117.84 → 2122.58] Who's, you know, who is this in this, or what product is this in this photo?
[2122.58 → 2124.28] Or, you know, all of those sorts of things.
[2124.38 → 2131.34] You want to ask about the image, or you want to ask about, like, give it as extra context to the language model.
[2131.54 → 2137.04] So the language vision model actually takes an image and or text.
[2137.74 → 2147.32] And then the output is similar, though, to the large language model in the sense that it's just going to output a stream of probable tokens.
[2147.32 → 2156.64] So this isn't actually, in one sense, this is not document processing, but it could be used for that.
[2156.98 → 2159.22] But it doesn't have to be used for it.
[2159.26 → 2167.46] So it could be used just to enhance the chat experience or to have a multimodal experience or to reason over images, right?
[2167.48 → 2169.16] Or to even classify images.
[2169.16 → 2172.88] It's kind of a general purpose reasoner over images.
[2172.88 → 2182.52] And what happens is you kind of take a large language model, and you add kind of a vision transformer into the mix.
[2182.84 → 2187.78] And the vision transformer takes the image and converts it into an embedding.
[2188.54 → 2195.52] The transformer piece of the LLM takes your text and converts it into an embedding.
[2195.52 → 2201.42] And then you smash both of those embeddings together into a vision plus text embedding.
[2201.88 → 2206.00] And that's what's used to generate the probability of the tokens on the output.
[2206.58 → 2212.10] So, again, image or text coming in, text going out the other end.
[2212.54 → 2218.70] And where this plugs into document processing is I could upload an image of a document, right?
[2218.70 → 2226.86] And just as my prompt say, hey, reconstruct this table in this image, right?
[2227.22 → 2228.96] And maybe that works.
[2229.22 → 2236.72] And it actually works quite well, depending on, of course, the model and what image you put in and that sort of thing.
[2236.72 → 2249.64] I'm kind of curious as you're kind of going through that fusion process, you know, between the text and the image thing, do you have any insight on whether those operate kind of in parallel and come together at some point?
[2249.70 → 2255.62] Or like how that fusion is able to generate the better outcome?
[2256.72 → 2258.88] Is it one of those things we just know it does?
[2259.12 → 2259.96] Or do you have any?
[2259.96 → 2260.58] Yeah, yeah.
[2260.58 → 2268.44] I think the key thing here is that, at least in my understanding, and our listeners can correct me if I'm spewing nonsense here.
[2268.52 → 2273.10] But in my understanding, part of it is that, yes, there are these two pieces.
[2273.96 → 2278.06] And so the input, the image input goes through the vision transformer.
[2278.30 → 2283.28] The text goes through different layers of a transformer network.
[2283.90 → 2285.12] Those embeddings are generated.
[2285.26 → 2286.02] They're smashed together.
[2286.02 → 2293.42] But that whole system is jointly trained together towards the output, right?
[2293.48 → 2295.68] So it's not like you train the one.
[2295.84 → 2296.70] That makes sense.
[2296.72 → 2297.86] And then you train the other one.
[2297.86 → 2299.98] And then you hope they work well together.
[2300.62 → 2305.56] It's kind of like you join them together at the hip to start with.
[2305.62 → 2311.70] You train the whole system on many, many, many of these kinds of inputs and outputs.
[2311.70 → 2322.18] And that's what, obviously, it's not interpretable in the sense of knowing how or why it outputs certain things.
[2322.68 → 2326.70] But it is able to recreate that probable output.
[2326.70 → 2332.74] And that would be, I would say, would be a major contrast with something like using docking plus OCR.
[2333.06 → 2342.20] Because then, actually, you do get a human observable structure of a document out and text corresponding to that.
[2342.64 → 2349.40] With the language vision model, you toss an image and text in and text comes out.
[2349.40 → 2362.22] And there's no real interpretable connection between the structure or content of that text on the output and any region in the images or specific characters in the images.
[2362.22 → 2371.18] It's all just us related via the semantics of those embeddings, not any sort of structure or anything like that.
[2371.18 → 2372.46] It's fascinating.
[2372.68 → 2382.48] It sounds like when you, I'm just kind of once again thinking back over, you know, the whole conversation and the maturity that's evolving in this capability.
[2383.16 → 2389.34] And so, I guess, as we've kind of hit that point, like, what's the next step in it?
[2389.42 → 2389.56] Yeah.
[2389.86 → 2390.78] What do you think is going?
[2391.14 → 2396.40] Well, I think the or at least a next step, it might not be where everything is going.
[2396.40 → 2402.78] But I think a next step is kind of represented by what Deeper has done with Deeper OCR.
[2402.98 → 2406.36] So, there are many language vision models or vision language models.
[2406.92 → 2407.86] I've heard it both ways.
[2408.42 → 2414.20] There's the one we use, kind of Quinn 2.5 vision language model.
[2414.52 → 2416.10] We've used that one quite a bit.
[2416.36 → 2417.62] Really great model.
[2417.76 → 2422.96] I mean, the best of these, the reality is the best of these are all coming out of China.
[2422.96 → 2428.56] At least at the moment of this recording in terms of the vision language model side of things.
[2429.06 → 2441.24] So, there have been these models over time, but they have limitations in the sense that most of these vision language models still assume a fixed resolution of the input of that image.
[2441.24 → 2450.28] And they do require, you know, they still require, you know, huge, huge training data sets and that sort of thing.
[2450.62 → 2455.50] But I think one of the main limitations is this fixed resolution size, right?
[2455.54 → 2464.38] So, no matter the size of your document, how it's structured, all of that, you're going to get this fixed resolution, which often does kind of create problems.
[2464.38 → 2484.38] And so, what DeepSeek OCR has kind of done is that they actually have kind of a different processing pipeline that doesn't take, so it doesn't take the whole image as a whole image.
[2484.38 → 2497.60] But actually, what happens is it takes the input image, and then it splits it apart into this kind of image tokens, if you will.
[2497.60 → 2505.76] So, small vision tokens that then are kept at their higher resolution.
[2505.76 → 2513.64] And they're combined with the kind of big, the whole image, right?
[2513.70 → 2522.44] So, you take the whole image, you combine it with these vision tokens and then, or a global full resolution view, I think they call it.
[2522.48 → 2525.62] So, you get this global page plus these tiles.
[2525.88 → 2531.94] And each of these tiles are kind of vision tokens are smashed together with the global page.
[2531.94 → 2548.42] And the idea is that you actually don't lose, it's a way of kind of representing this image or this document in a kind of compact token sequence where you are not limited by the resolution of your document.
[2548.42 → 2570.08] And so, what that means is that DeepSeek OCR, at least in terms of how it seems right now, is that it does a good job at preserving certain shapes of characters, line breaks, alignments, very tiny mathematical equations or notation, right?
[2570.12 → 2575.14] You get sort of little dots or a carrot above mathematical notation.
[2575.14 → 2593.04] And so, really what DeepSeek OCR is kind of taking some of these ideas to the next level and preserving a lot of that information from the larger document into this kind of full resolution tiles, which can then be processed through the model.
[2593.04 → 2602.72] Can you talk a little bit about, like when we're talking about resolution, like what kind of level set, what does resolution mean in this context?
[2602.76 → 2608.58] As we're talking about, you know, specific resolutions and then a multi-resolution thing, can you kind of clarify what that is?
[2608.70 → 2609.12] Yeah, yeah.
[2609.12 → 2615.70] So, if I have just kind of reducing it to thinking about a single page, right?
[2615.92 → 2627.48] If I have a single page and I represent that of a document, I represent that as an image, you know, it might be however many pixels by however many pixels, right?
[2627.54 → 2631.18] Let's say 1,000 pixels by 1,500 pixels, right?
[2631.18 → 2642.30] But in a vision language model, typically regardless of what image you input, it's going to resize it to whatever, 256 by 256.
[2642.68 → 2657.78] And if you imagine taking that larger page, smashing it down into 256 by 256, you're going to lose little handwriting or diagrams or code or equations or little tiny fonts or footnotes, etc.
[2657.94 → 2659.08] All of that stuff.
[2659.08 → 2671.16] And so, what DeepSeek is saying, well, let's not lose all of that context, but let's also not have to, you know, keep everything in the same resolution.
[2671.46 → 2674.98] Let's take the tile, let's tile this image.
[2675.80 → 2683.58] And now we have the original resolution of the document, but the tile is not there.
[2683.58 → 2691.24] But we also don't lose the ordering or the context of where that tile fits because we have the global view of the page.
[2691.24 → 2700.22] And so, it's kind of like when we put text into a transformer, we actually don't lose the ordering often either, right?
[2700.22 → 2703.88] We understand where text is related to other text.
[2704.00 → 2716.14] And this is kind of a similar concept where we're not losing any of the resolution, but we're also not losing the structure of where this kind of tiles are placed, if you will.
[2716.14 → 2717.30] That makes perfect sense.
[2717.42 → 2729.40] And so, it's kind of the natural progression, you know, if we're going back a few years and talking about the way convolutional neural networks are working and the fact that you were constantly having to go to, you know, reduce the size down.
[2729.40 → 2738.18] But that created problems in terms of what was in the pictures, you know, identification of whatever.
[2738.52 → 2741.64] And the lack of resolution could sometimes make that a challenge.
[2742.32 → 2742.54] Yes.
[2742.70 → 2744.98] And this solves that in a particular way.
[2745.18 → 2745.64] Yeah, yeah.
[2745.64 → 2753.24] Which the kind of last generation, or I don't know, current or last, I don't know what generation we're in.
[2753.38 → 2763.24] The bulk of vision language models at the moment do not solve that because they still force this kind of fixed resolution.
[2764.06 → 2768.38] Now, at the same time, Deeper OCR, it is also a larger model.
[2768.66 → 2771.44] It does require GPUs to run.
[2771.44 → 2777.40] But this is only the kind of first generation of these, similar to vision language models, large language models.
[2777.60 → 2785.16] I'm sure there will be a gradual shrinking of these models at higher performances as more and more people train them.
[2785.46 → 2791.00] And who knows if this is the right approach, kind of quote right approach to go down.
[2791.34 → 2792.28] But it is interesting.
[2793.66 → 2798.82] One of the things I find interesting here, Chris, is we talk a lot about large language models.
[2798.82 → 2802.56] And for the most part, they all operate the exact same way.
[2802.86 → 2806.20] And we've been talking about them operating the exact same way for some time.
[2806.52 → 2816.74] But if you look at the progression of these models, these multimodal models, they all, as we've gone through this conversation, they all do operate in quite different ways.
[2816.74 → 2841.58] And so there's a lot of, you know, to your point at the beginning, from my perspective, maybe from a nerdy perspective, document processing is very much not boring because there's actually such a diversity and such innovation going on here with much more diversity on the model side and the technical side than what you see in large language models.
[2841.58 → 2847.18] And not only that, but our listeners have come through this with us.
[2847.60 → 2850.94] This is probably not something most of them have been hitting on lately.
[2851.48 → 2859.48] And so not only have they earned their, if they're in the U.S., at least their Thanksgiving meal for tomorrow by the time they've done this.
[2859.48 → 2872.94] But maybe coming out of the holidays, they can go back into the office and kind of give an upgrade to their RAG system and be wizards at how effective RAG is being for their organization.
[2873.48 → 2877.22] Because I definitely learned a bit along the way here about that.
[2877.34 → 2879.20] I have a bunch of use cases in mind now.
[2879.34 → 2881.96] I'm thinking, oh, gosh, we can go back and do this and that and the other.
[2881.96 → 2890.50] So fantastic explanation of these different approaches and kind of the timeline about how they develop.
[2890.66 → 2891.70] So thanks for doing that.
[2891.96 → 2892.64] Yeah, of course.
[2893.08 → 2895.28] And happy Thanksgiving again, Chris.
[2895.44 → 2897.36] Happy Thanksgiving to all our listeners.
[2898.04 → 2900.32] Hope you enjoy your Tour.
[2900.64 → 2901.14] There you go.
[2901.30 → 2907.90] And even if you're outside the U.S., we are thankful for you listening in and looking forward.
[2908.10 → 2910.60] Hope that you have whatever holidays you celebrate.
[2910.60 → 2913.72] We hope they're very good going over the next few months here.
[2920.92 → 2921.56] All right.
[2921.72 → 2923.14] That's our show for this week.
[2923.52 → 2930.46] If you haven't checked out our website, head to practicalai.fm and be sure to connect with us on LinkedIn, X or Blue Sky.
[2930.70 → 2934.02] You'll see us posting insights related to the latest AI developments.
[2934.46 → 2936.40] And we would love for you to join the conversation.
[2936.40 → 2940.66] Thanks to our partner, Prediction Guard, for providing operational support for the show.
[2941.00 → 2942.40] Check them out at predictionguard.com.
[2943.42 → 2947.02] Also, thanks to Break master Cylinder for the beats and to you for listening.
[2947.40 → 2948.18] That's all for now.
[2948.48 → 2950.20] But you'll hear from us again next week.
[2950.20 → 2953.42] Thanks for watching.
[2960.30 → 2962.30] Bye.
[2962.32 → 2963.50] Bye.
[2963.50 → 2964.42] Bye.
[2964.42 → 2968.02] Bye.
[2972.10 → 2974.10] Bye.
[2974.10 → 2974.48] Bye.
[2974.48 → 2974.50] Bye.
[2974.70 → 2975.30] Bye.
