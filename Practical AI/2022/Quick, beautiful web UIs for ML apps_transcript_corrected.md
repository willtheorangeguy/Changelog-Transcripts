[0.00 → 8.68] But I think one of the very interesting developments that we're seeing, and we're trying to understand this piece better, is that people used to just have demos as kind of standalone things.
[8.68 → 12.56] But now people are taking demos and integrating it onto their websites.
[12.96 → 16.16] One of our users, for example, built this NFT search engine.
[16.74 → 18.68] The back end of it is a Radio app.
[19.04 → 23.48] He hosted it on Spaces and just embedded that Spaces on the homepage of his website.
[23.88 → 27.46] And so his whole website, I mean, it has some surrounding information, but it's basically a Radio demo.
[27.86 → 29.44] We've seen this in a few different examples.
[29.44 → 31.00] And this kind of raises the question.
[31.10 → 36.50] So now it seems like a lot of people are building very data-centric or machine learning-centric applications.
[36.66 → 37.64] That's like the focus of it.
[46.74 → 47.70] Hello, friends.
[47.88 → 54.38] Jared here to tell you about Changelog++, our membership program for those of you who want to directly support our work.
[54.38 → 58.72] Your++ membership gets you closer to the metal with extended episodes,
[58.72 → 64.58] makes the ads disappear, and takes our audio to the next level with higher bitrate MP3s.
[64.72 → 68.32] You can join today at changelog.com slash plus.
[79.96 → 87.70] Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive, and accessible to everyone.
[87.70 → 92.46] This is where conversations around AI, machine learning, and data science happen.
[92.78 → 98.18] Join us at practicalai.fm slash community and follow the show on Twitter.
[98.38 → 100.54] We're at practicalai.fm.
[100.68 → 105.40] Thank you to our partners at Vastly for shipping our pods superfast all around the world.
[105.64 → 107.48] Check them out at fastly.com.
[107.48 → 116.60] Welcome to another episode of Practical AI.
[116.60 → 118.54] This is Daniel Whiten ack.
[118.66 → 121.88] I am a data scientist with SIL International.
[122.14 → 127.58] I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin.
[127.84 → 128.76] How are you doing, Chris?
[128.90 → 132.52] Doing very well, except I'm drowning in yellow pine pollen.
[132.98 → 134.62] Yeah, it's allergy season.
[134.62 → 136.36] Yeah, it's everywhere.
[136.68 → 138.56] Other than that, doing great.
[139.08 → 139.70] Yeah, yeah.
[139.76 → 140.58] Allergy season.
[140.82 → 147.02] I've been rotating between sneezing and then debugging some like NVIDIA issue today.
[147.22 → 153.24] So it's like NVIDIA issue, sneeze, come back, see if it's fixed, sneeze, blow my nose.
[153.40 → 156.60] Is the NVIDIA issue contributing to the sneezing?
[156.84 → 158.48] I don't know.
[158.86 → 159.22] I don't know.
[159.24 → 160.86] Is there a correlation between the two?
[161.28 → 163.26] Let's say no on the record.
[163.26 → 166.70] Just inspired like the next line of NVIDIA processors.
[166.90 → 169.38] They'll be like the sneeze or something, you know?
[169.56 → 170.36] Yeah, yeah.
[170.36 → 173.04] They need good marketing, and you're providing that for a free service.
[173.44 → 174.70] Yeah, I guess so.
[175.22 → 182.20] Yeah, speaking of practical things, I'm pretty excited about our guest today because, as you
[182.20 → 186.96] know, I'm always wanting to get into the practicalities of what we're talking about.
[186.96 → 189.82] And this really fits into that.
[189.96 → 192.64] I'm sure a lot of our listeners have heard about Radio.
[193.10 → 199.26] And today we have with us Abubakar Acid, who is the Radio team lead at Hugging Face.
[199.60 → 199.82] Welcome.
[200.22 → 201.18] Thank you so much, guys.
[201.34 → 202.40] It's awesome to be here.
[202.68 → 203.40] Yeah, yeah.
[203.40 → 209.10] As we get started, maybe just give us a little bit of a sense of like your background and
[209.10 → 217.58] how you eventually, you know, found your way into thinking about Granitelike things or interfaces
[217.58 → 219.32] or apps for machine learning.
[219.64 → 220.42] Yeah, absolutely.
[220.96 → 223.68] So I've been doing machine learning for about a decade now.
[223.84 → 229.38] I did my PhD at Stanford and I worked a lot on building machine learning models for medical
[229.38 → 232.26] imaging and medical videos, that kind of thing.
[232.26 → 238.36] And during the course of my PhD, I would often work with collaborators who are not machine
[238.36 → 240.80] learning scientists, not machine learning engineers.
[241.02 → 244.24] There were doctors, clinicians, biologists, that kind of thing.
[244.58 → 249.00] And one of the things that we realized was, well, first, not everyone knows how to
[249.00 → 250.52] use machine learning models directly.
[250.96 → 254.14] Not everyone can code, you know, software engineering and all that good stuff.
[254.52 → 258.68] And we wanted to make it easy for other people to try out the model so that they could get
[258.68 → 259.04] feedback.
[259.04 → 263.00] Because, you know, sometimes you tell someone, hey, I trained a model for you.
[263.04 → 264.24] It's like 95% accurate.
[264.60 → 265.34] They're not going to believe you.
[265.38 → 267.54] They're not going to take your word necessarily.
[267.60 → 269.56] They want to try it out themselves and, you know, test it.
[270.00 → 275.76] And so we started off with a very simple library that was designed to make it easy to test computer
[275.76 → 276.54] vision models.
[276.54 → 282.02] That ultimately grew into Radio, which is an open source Python library to build machine
[282.02 → 286.24] learning models very generally, to build GUIs for machine learning models very generally,
[286.34 → 289.28] to build demos, web apps for machine learning models.
[290.00 → 294.02] And then I actually finished my PhD at Stanford last year.
[294.38 → 298.30] And then soon after that, actually, Radio got acquired by Hugging Face.
[298.30 → 303.38] And so now we're here at Hugging Face, which is a fantastic place to be.
[303.86 → 308.38] And really, we have this amazing mandate, which is, hey, let's, you know, let's make Radio
[308.38 → 313.66] the default tool for machine learning practitioners to build demos, to get their work out there so
[313.66 → 318.52] that other people can access their work so that machine learning researchers can make their
[318.52 → 319.80] work more reproducible.
[320.38 → 324.44] Machine learning teams can easily collaborate and kind of see what machine learning models are
[324.44 → 325.08] actually doing.
[325.96 → 330.34] And yeah, and we're hoping to grow this a lot more in the next few years.
[330.88 → 332.30] So just to blow it out.
[332.40 → 337.52] So for those in our audience who are not familiar with Radio, could you talk specifically about
[337.52 → 341.68] what that is, since we've all been talking about it for a few minutes, and I want to make
[341.68 → 344.28] sure that they have a clear image of what you're talking about?
[344.62 → 345.18] Yeah, absolutely.
[345.32 → 347.98] So Radio is an open source Python library.
[348.42 → 349.68] So you can, you know, pip install it.
[349.76 → 353.82] And what it does is it takes a machine learning model that you've built, or it could also be an API
[353.82 → 358.18] or any sort of function, but it takes something that you've built and wraps it with a GUI.
[358.62 → 360.52] So you have this like web-based GUI.
[360.90 → 364.82] So you imagine like you have an image classification model, you can easily wrap a web-based GUI that
[364.82 → 368.18] allows you to drag and drop your images, see the model's predictions.
[368.86 → 373.08] But the cool thing is that you can build this GUI entirely from Python, right?
[373.12 → 376.70] So in the past, if you wanted to build like a web application around your model, you needed
[376.70 → 381.64] to know Flask, but then also maybe Docker to containerize it, and then maybe some Bash scripts,
[381.64 → 383.62] and then you need to figure out web hosting solutions.
[384.16 → 387.42] And then you need to maybe know a little bit of SQL to build a database to collect samples,
[387.42 → 391.74] and then maybe some front-end web development, HTML, CSS, JavaScript to kind of build a little
[391.74 → 392.82] UI around it.
[393.22 → 398.28] All of that in one framework in Python, which is already something that you know if you're
[398.28 → 398.96] doing machine learning.
[399.52 → 399.64] Yeah.
[399.94 → 405.36] So before the show, I was just running a few things in Radio.
[405.56 → 410.06] And I have in the past, but I kind of revisited a few things that I was playing around with.
[410.06 → 415.84] Right now, I've got an application running to do just like question answering, which is
[415.84 → 420.24] actually something that we do at SIL and work very closely with those sorts of models.
[420.44 → 425.76] Just to give people a sense, I created this application, and I'm looking at it right now.
[425.92 → 427.30] It's 10 lines of code.
[427.60 → 429.04] Three of those are blank lines.
[429.64 → 435.76] And in those 10 lines of code, imported question answering model, and like you say, wrapped it
[435.76 → 438.80] in this function, this question answer function.
[439.38 → 446.02] And then with that, when I do Python, you know, this app.py, then it spins up a web server,
[446.02 → 448.68] and I can go into my browser and interact with the model.
[448.98 → 450.18] So yeah, it's pretty cool.
[450.26 → 455.34] I think it's like pretty interesting that it's almost like it seems like you can have superpowers,
[455.46 → 460.24] like you get sort of superpowers to do this web stuff without having to actually know that
[460.24 → 460.62] stuff.
[460.62 → 466.28] I'm curious, from your perspective now doing this for quite a while, seeing a lot of people
[466.28 → 473.30] use Radio, in the context of like industry and companies, where do you think like the
[473.30 → 479.52] value add comes from this type of, I don't know if you'd consider it like a prototype or
[479.52 → 481.20] an app or a tool?
[481.78 → 488.10] Where does the value add come within the workflow of a typical like data scientist or something
[488.10 → 488.54] like that?
[488.54 → 491.32] Yeah, no, I think this is a really important question.
[491.80 → 496.22] So the way that I've seen machine learning done in both in research kind of settings,
[496.26 → 500.96] but also in industry teams, is that there's almost like two cycles of machine learning.
[501.16 → 504.58] There's the prototyping slash exploration slash research cycle.
[504.92 → 506.56] And then there's kind of the deployment cycle.
[506.82 → 511.36] And the kind of the workflows and the tools that are used in both of the cycles are very
[511.36 → 511.70] different.
[512.04 → 515.42] So in the first one, you know, in the research exploration, you're mostly working in Jupyter
[515.42 → 518.14] notebooks, doing a lot of trial and error.
[518.44 → 522.42] You're building lots and lots of models oftentimes, and you're getting feedback.
[522.42 → 523.58] And this is really important.
[523.66 → 528.16] You're getting feedback from stakeholders because it's impractical and usually not the case
[528.16 → 531.84] that the machine learning developer knows everything about what kind of data, you know,
[531.84 → 533.04] how the model is going to be used.
[533.04 → 538.26] It's oftentimes end users, you know, sometimes quality testers, sometimes customers, sometimes
[538.26 → 542.64] business teams who are going to be the ultimate consumers of these models, right?
[542.70 → 546.22] So like there are the producers of the models and the consumer of the models.
[546.82 → 551.20] And traditionally, it's very hard for those two types of folks to talk to each other.
[551.86 → 555.80] And so what Radio does, it kind of creates the kind of the bridge between these two teams.
[556.06 → 560.08] So let's say you're a machine learning researcher, scientist, developer, whatever your role is,
[560.08 → 564.74] you can easily take a model that you've built and then expose it so that it can be consumed
[564.74 → 566.32] by a variety of different people.
[566.70 → 570.10] And we've seen that be sometimes a quality testing teams.
[570.52 → 574.48] So one of the things you'll notice in a Radio demo, by default, there's this flag button as
[574.48 → 578.72] well, which helps you catch like incorrect predictions and so on and store them in a local
[578.72 → 580.70] like database on your computer and stuff like that.
[580.98 → 582.16] So that's very useful.
[582.16 → 586.88] And it's really designed for like quality testing teams or even end users to try out your model
[586.88 → 588.26] and get back to you.
[588.26 → 590.66] The whole idea behind Radio is it's so intuitive.
[590.90 → 594.90] Very few people know how to build machine learning models kind of in the grand scheme of things.
[595.36 → 599.16] More people know how to like maybe load a model, you know, if you've given a model and maybe
[599.16 → 600.68] run some code against it.
[600.90 → 603.36] But way more people know how to use a browser, right?
[603.46 → 608.20] Like billions of people can, you know, literally drag and drop images into a browser and try
[608.20 → 608.54] it out.
[608.54 → 612.50] And what that does is it kind of lets you, it reminds you that, you know, your audience
[612.50 → 615.96] when you're building these machine learning models is very broad, and it lets, you know,
[615.96 → 618.98] it puts the control in their hands so they can, they can try it out and give you feedback.
[619.64 → 621.74] Is it kind of conceptualizing it a little bit?
[621.90 → 622.10] Yeah.
[622.14 → 626.04] If you're kind of making an analogy to web development a little bit, and you have these
[626.04 → 630.82] frameworks out there to make it easier, like React and Angular and stuff like that, is it
[630.82 → 632.10] a little bit like that?
[632.10 → 634.76] Or is it more focused on just the model?
[635.02 → 639.16] When you talk about creating that, that user experience so that you can share it with people,
[639.16 → 641.20] what does a typical experience look like?
[641.20 → 642.58] Yeah, it's a perfect question.
[642.70 → 646.84] So even when we started Radio, and recently we've been having this conversation about
[646.84 → 649.42] how general purpose do we want Radio to be?
[649.52 → 654.32] Like, do we want it to be the way you create any sort of web application in, you know, directly
[654.32 → 654.90] from Python?
[655.22 → 656.14] That would be really cool.
[656.18 → 659.86] And I think we're working towards that goal, but we've intentionally started with these
[659.86 → 663.34] higher level abstractions that are designed for machine learning models.
[663.68 → 667.38] Like really, like if you have a machine learning model, and you want to wrap it with a demo
[667.38 → 671.22] or with a GUI, you can do it in like less than like three lines of code as Daniel was just
[671.22 → 671.76] talking about.
[672.02 → 676.04] And that's because we've created these high level abstractions that make it super easy
[676.04 → 679.20] to like plug in a model, plug in what kind of input you want, plug in what kind of output,
[679.56 → 680.60] creates that GUI for you.
[680.60 → 685.34] So really like the developer experience right now, as is designed, you know, really for like
[685.34 → 688.16] machine learning kind of engineers and researchers.
[688.54 → 692.10] But, and this is one of the things we're working on right now, is we're exposing a low level
[692.10 → 696.64] API that can allow you to actually build more, like more complicated and more, you know,
[696.64 → 702.60] potentially a much wider array of web applications, whether they be for other use cases in machine
[702.60 → 707.30] learning, like for example, labelling or annotation or a data set exploration, or it could be for
[707.30 → 708.46] like other things altogether.
[709.14 → 714.34] And partly because of great communities like Hugging Face and other communities, you know,
[714.42 → 720.46] we are seeing this rapid proliferation of all sorts of kinds of models and how they're
[720.46 → 723.80] used to do like all sorts of interesting things.
[723.80 → 731.68] So could you describe a little bit with Radio, like maybe those main use cases where it's
[731.68 → 736.68] super easy, like I did the question answering thing, and then maybe other cases, how does
[736.68 → 738.36] like the customization work?
[738.58 → 743.14] Maybe someone out there is thinking like, oh, well, I'm not quite doing the same type of
[743.14 → 748.04] like object recognition or text summarization or something like that.
[748.10 → 748.72] How does that work?
[749.02 → 749.64] Yeah, absolutely.
[749.64 → 752.76] So Radio started off actually designed for images.
[753.12 → 755.34] That was kind of the image related tasks.
[755.82 → 761.64] But at this point, it covers a pretty much, I would say 95% of machine learning use cases.
[762.18 → 765.28] And the way it does that, and this kind of goes back to your previous question, Chris,
[765.32 → 766.54] about who is designed for.
[766.84 → 771.04] The way it does that, it comes shipped with prebuilt components, right?
[771.06 → 773.30] So the idea is, hey, I'm working with videos.
[773.46 → 774.68] I want a video input.
[774.68 → 779.30] And maybe my output is, I don't know, it's a heat map, it's an image, or it's a plot,
[779.44 → 780.30] or whatever it may be.
[780.66 → 785.46] So Radio comes in shipped with all of these different components, making it super easy
[785.46 → 790.06] for basically your use case could be anything from like, I don't know, maybe I'm doing video
[790.06 → 795.22] activity detection to anything to like more like traditional data science.
[795.36 → 799.82] Maybe I'm working with data frames and other kinds of graphs and time series data.
[800.42 → 802.10] Radio has components for all of that.
[802.10 → 805.04] And we've, you know, we're always like adding new things.
[805.16 → 808.60] And so for example, we just added automatic speech recognition, or like real time speech
[808.60 → 809.12] recognition.
[809.38 → 810.48] So you can kind of speak.
[810.56 → 813.20] And as you're speaking, you can get a transcription rendered real time.
[813.46 → 815.42] We have a lot more things in the pipeline as well.
[815.54 → 821.52] Some things like 3D images and 3D models and objects, that's going to be released pretty
[821.52 → 822.10] soon as well.
[822.62 → 824.02] So I'm just looking at the documentation.
[824.52 → 828.90] And I was also playing around with a couple other things before this conversation.
[828.90 → 832.26] And it covers a lot of components.
[832.62 → 837.50] So like input components, including things like, you know, sliders and text box and video
[837.50 → 843.36] and audio output components, data frames, files, labels, text box.
[843.86 → 847.60] And so like, I also work in dialogue systems with SIL.
[847.76 → 849.80] And there's even like a chatbot output.
[850.16 → 855.74] I actually didn't know that before I went into your, like went into your docs again after I'd
[855.74 → 856.38] used it in a while.
[856.38 → 857.48] And I was like, that's cool.
[857.48 → 861.88] So I clicked on that and just like opened a notebook and had like a chatbot interface
[861.88 → 866.18] to like plug into my NLU model, which was, which was really cool.
[866.60 → 868.46] You can stitch all of these together as well.
[868.56 → 872.66] So what we, you know, one of the things that kind of astounds me is sometimes people will
[872.66 → 877.26] build super complex, like a model will take like eight different inputs, and they will
[877.26 → 881.44] write all like the Radio code that's needed to create like this input that takes eight
[881.44 → 882.08] different things.
[882.08 → 887.00] And the GUI is so complicated, and I'm like, wow, you know, they write all this code, which
[887.00 → 890.24] isn't too much code, but still, you know, you have to get, you have to read the documentation,
[890.44 → 892.58] understanding, understand the parameters and all of that.
[892.94 → 896.20] And people do all of that because the alternative is, it's kind of terrible.
[896.62 → 899.18] The alternative is having to write all of this front end stuff.
[899.54 → 900.68] And no one wants to do that.
[900.78 → 901.64] No one wants to do that.
[901.64 → 905.78] So having this ability to kind of the superpower to do it in Python, I think it's quite nice.
[931.64 → 949.66] So you already mentioned the acquisition by Hugging Face, and now you're, you know, lead of the
[949.66 → 953.44] Radio team at Hugging Face, which is, which is super exciting.
[953.82 → 959.24] So our listeners can't see video, but I made sure, and I wore my new Hugging Face hat today
[959.24 → 960.16] for the interview.
[960.32 → 961.24] I don't know if you see that.
[961.70 → 966.84] Obviously I'm, I have a little bit of bias on my side for, for Hugging Face, as our listeners
[966.84 → 967.30] will know.
[967.48 → 969.44] I'm jealous because I don't have a Hugging Face hat.
[969.64 → 970.34] How did you get one?
[970.52 → 971.10] I don't know.
[971.78 → 972.76] Well, I don't know.
[972.82 → 978.34] I saw someone on Twitter post like, Hey, beta of the Hugging Face store.
[978.42 → 980.50] And I don't know if it's like public yet.
[981.14 → 984.82] Maybe I'm not supposed to be sharing this, but I saw it on Twitter, like beta of the Hugging
[984.82 → 985.40] Face store.
[985.40 → 986.74] And I was like, Oh yeah.
[986.88 → 990.98] So I clicked there and then I, I ordered swag for my whole team.
[991.12 → 993.02] So I splurged a little bit.
[993.26 → 996.80] They won't be surprised, I guess, if they listen to this podcast, I'll try to get it to them
[996.80 → 997.34] before then.
[997.94 → 1002.22] But yeah, anyway, with Hugging Face, like, so you've described Radio.
[1002.56 → 1007.14] We've talked about Hugging Face on the show many times, but maybe you could just give us
[1007.14 → 1013.66] from your perspective, like what is Hugging Face, and why does it make sense to have like Radio
[1013.66 → 1014.74] plus Hugging Face?
[1014.74 → 1015.66] Yeah, absolutely.
[1016.08 → 1017.44] Hugging Face does a lot of things.
[1017.80 → 1023.06] So it's hard to describe concisely, but basically what I think the overarching goal of Hugging
[1023.06 → 1025.74] Face is to make machine learning more accessible, right?
[1025.84 → 1031.40] So previously, if you wanted to use state-of-the-art machine learning models, you have to wrangle
[1031.40 → 1034.88] with a lot of, you know, you have to read papers, you have to wrangle with a lot of, I think,
[1034.98 → 1036.64] malformed GitHub repos.
[1036.80 → 1038.38] I don't miss those days at all.
[1038.54 → 1038.94] Exactly.
[1039.60 → 1040.44] It's a lot of work.
[1040.48 → 1042.08] I remember that from my PhD as well.
[1042.08 → 1042.78] It's a lot of work.
[1042.78 → 1048.44] The way I see it is that Hugging Face offers various levels of access, right?
[1048.52 → 1053.28] So for example, there's Hugging Face data sets, which is designed for machine learning practitioners,
[1053.48 → 1055.04] really, to train their own models.
[1055.04 → 1060.40] Then there's Hugging Face models, which is designed for machine learning practitioners, but also
[1060.40 → 1063.64] software engineers who don't want to have to think about like what's under the hood.
[1063.90 → 1069.68] They just want to use a perfect, you know, image classification or perfect question
[1069.68 → 1073.14] answering model and not really worry about any of the algorithmic, you know, implementation
[1073.14 → 1073.78] details.
[1074.04 → 1076.44] And so that, you know, opens it up to a lot more people.
[1076.44 → 1081.72] And then with Radio and or spaces, which is what Hugging Face calls demos, that level
[1081.72 → 1083.28] of access opens up even more.
[1083.80 → 1087.32] So now pretty much anyone who can use a browser, like we said, you know, billions of people who
[1087.32 → 1092.20] have a browser and are connected to the internet can now use state-of-the-art machine learning
[1092.20 → 1094.26] models, and they can do interesting things with that.
[1094.66 → 1096.28] And I'll just give me two quick examples.
[1096.80 → 1101.56] One is we had this demo that someone built with Radio called Animal.
[1101.56 → 1106.06] And we've seen many, many such examples, but Animal was this demo that you could put
[1106.06 → 1110.82] your own image or put any image, and it would render it into this carbonized, you know,
[1110.86 → 1115.30] like almost like I think it's called otoscope or like drawn version of that image.
[1115.40 → 1120.82] And someone built a demo with Radio, hosted on Hugging Face Spaces, which is a place you
[1120.82 → 1126.20] can host your Radio demos for free and then released it on Twitter where it went viral or,
[1126.44 → 1126.56] you know.
[1126.74 → 1127.70] I remember it.
[1127.84 → 1127.98] Yeah.
[1128.06 → 1128.34] Yeah.
[1128.34 → 1128.66] Yeah.
[1128.66 → 1133.72] And we had thousands of people use the model, I would say maybe tens of thousands and, you
[1133.72 → 1137.54] know, tried on their own profile pictures, pictures of their pets, you know, every day
[1137.54 → 1138.24] objects.
[1138.82 → 1143.52] And they were interacting with actually state-of-the-art machine learning, which is something
[1143.52 → 1144.64] that's never been done before.
[1144.88 → 1149.40] And that is really cool because now machine learning developers are thinking, hey, the audience
[1149.40 → 1151.64] for who's using my model is a lot bigger.
[1152.16 → 1154.14] Let me make sure that my models are robust.
[1154.14 → 1157.06] They can handle like diverse images, diverse inputs.
[1157.68 → 1161.72] And that leads to a level of, I think, you know, concern for the end user that wasn't
[1161.72 → 1162.52] really there before.
[1162.74 → 1166.24] I think that's really important because then issues of bias and accessibility are addressed
[1166.24 → 1166.62] as well.
[1167.02 → 1170.46] I want to give one other example as well, because I think this is interesting as well, because
[1170.46 → 1174.82] demos have a big purpose for education as well.
[1174.82 → 1180.28] And I remember one of the early days of Radio, actually, we had built like this demo for an
[1180.28 → 1180.96] MOIST model.
[1181.50 → 1185.34] And I actually shared this, you know, this MOIST model, you can draw handwritten digits
[1185.34 → 1187.84] and you can see what the prediction of the model is.
[1188.24 → 1189.42] And I shared it with my sister.
[1189.68 → 1192.40] My younger sister was like no background in machine learning whatsoever.
[1192.94 → 1197.58] And she tried using the model and she, you know, she drew a six, and it predicted six
[1197.58 → 1198.28] and all that work.
[1198.56 → 1200.54] And then she just drew a little dot in the centre.
[1201.02 → 1202.64] And I think it predicted like a seven.
[1203.10 → 1205.24] And she was like, why did I predict a seven?
[1205.30 → 1205.92] That makes no sense.
[1205.98 → 1206.62] I just drew a dot.
[1207.14 → 1210.44] And then I told her, well, it kind of has to predict something, you know, and maybe the
[1210.44 → 1212.62] sevens were just the most common thing in the data set.
[1213.04 → 1214.76] And she was like, that doesn't seem right.
[1215.02 → 1216.64] So then I was like, well, what should I do?
[1217.00 → 1220.88] And she said, well, it should just like avoid making a prediction, you know, and it should
[1220.88 → 1222.32] kind of abstain from making a prediction.
[1222.78 → 1226.46] And so she had stumbled upon this idea of abstention, which is, you know, now a really important
[1226.46 → 1226.78] topic.
[1226.88 → 1227.96] A lot of people think about that.
[1227.96 → 1231.44] But, you know, if you've never really like interacted with a machine learning model in
[1231.44 → 1234.20] this way, you might not even realize the importance of it.
[1234.38 → 1236.10] And, you know, this someone has no background in machine learning.
[1236.38 → 1241.88] So I think demos, I can go a really far away in both accessibility and then also education
[1241.88 → 1242.28] as well.
[1242.52 → 1243.08] So I love that.
[1243.18 → 1247.16] I actually like to dig in, having gone through those two examples and dig in just a little
[1247.16 → 1247.40] bit.
[1247.74 → 1253.28] It really begs the question of what typical workflows look like, because you've kind of shown us
[1253.28 → 1255.90] two examples of kind of going out there and doing that.
[1255.90 → 1260.08] And that second one in particular, there was a big insight, you know, because we're all
[1260.08 → 1260.82] in this industry.
[1260.82 → 1263.44] And I think there are some things we take for granted because we've been doing it for a
[1263.44 → 1263.64] while.
[1263.86 → 1268.90] But you had someone who wasn't someone important in your life who was not in the industry make
[1268.90 → 1269.70] you realize something.
[1269.86 → 1271.80] And I think we all have moments like that.
[1272.42 → 1276.92] What are some of the typical ways that you and your team and other people that you work
[1276.92 → 1282.30] with are using Radio on a day-to-day basis that that has like directly changed the way
[1282.30 → 1283.52] the workflow is?
[1283.52 → 1284.80] Where do you fit this in?
[1284.90 → 1290.08] If I'm adding Radio into my machine learning, I'm already maybe using Hugging Face, but now
[1290.08 → 1291.48] I want to use Radio as part of that.
[1291.86 → 1292.60] What's changed?
[1292.84 → 1294.84] And how do I think about my workflow now?
[1295.18 → 1295.88] Yeah, absolutely.
[1296.34 → 1299.26] Let me give me one more example, I think, that might illustrate that.
[1299.34 → 1300.78] And then we can kind of discuss that.
[1301.28 → 1305.76] So this was actually one of the early examples of Radio and where I realized it could actually
[1305.76 → 1308.98] have a big impact, especially in interdisciplinary teams.
[1308.98 → 1315.18] And so I was building a machine learning model to classify ultrasound images of the heart.
[1315.32 → 1317.04] So echocardiograms, if you're familiar with them.
[1317.50 → 1322.56] And so we had built this model, and it was getting perfect accuracy, like 95%, you
[1322.56 → 1326.98] know, AUC and all this good stuff to predict like various things about the heart.
[1327.04 → 1329.92] For example, like does this patient have a pacemaker in the heart or not?
[1329.92 → 1334.58] And so we had built this model, and we shared it with a cardiologist and the cardiologist
[1334.58 → 1337.84] was a little skeptical about, you know, how well the model was working.
[1338.52 → 1342.40] And so we built a Radio demo around it, and we let him play around with it.
[1342.44 → 1346.28] And one of the things you can do with a Radio demo is you can interactively edit the input.
[1346.62 → 1351.16] So the cardiologist can upload his own ultrasound image in this case, and they can kind of edit
[1351.16 → 1351.38] it.
[1351.48 → 1356.46] And so they could, for example, remove the pacemaker from the image by like white, you know, kind
[1356.46 → 1357.32] of white outing it.
[1357.70 → 1358.82] And so he did that.
[1358.82 → 1361.34] And so there was a pacemaker ultrasound.
[1361.98 → 1364.18] It was the model was predicting this patient as a pacemaker.
[1364.36 → 1367.04] Then the cardiologist white outed it, removed it.
[1367.14 → 1369.22] And then the predictions change in real time.
[1369.54 → 1374.42] And when the cardiologist saw that and did this with a few different images, he was like,
[1374.46 → 1375.68] wow, this actually works.
[1375.86 → 1377.40] You know, this actually works.
[1377.42 → 1380.74] And even us, all the machine learning people in the room, we all breathed a sigh of
[1380.74 → 1381.02] relief.
[1381.30 → 1385.32] Because one thing to see aggregate metrics, but it's another thing to have someone adversarial
[1385.32 → 1386.12] test your model.
[1386.54 → 1388.34] And then it's still, you know, it's kind of robust to that.
[1388.34 → 1392.50] Basically, I think there are two broad ways that Radio can help.
[1392.72 → 1399.04] And one is if your model is good, it can help build trust in the model, especially for important
[1399.04 → 1400.50] stakeholders because they can test it.
[1400.76 → 1404.42] But if your model is bad, and this may be more important, if your model is bad, it can
[1404.42 → 1408.86] help expose those issues of bias and other things that are really important as well.
[1408.86 → 1410.76] So I had a little follow-up.
[1410.90 → 1413.52] And you're starting to address it there at the end already.
[1413.52 → 1414.64] But I'm curious.
[1414.80 → 1416.36] And it's a little bit of a side issue.
[1416.38 → 1417.80] It's not a direct Radio issue.
[1417.86 → 1421.02] But the Radio is obviously part of the solution to this.
[1421.02 → 1426.14] And that is that several times in our conversation, we've mentioned the idea of people being skeptical
[1426.24 → 1427.70] of model output.
[1427.82 → 1429.30] And like, I don't know, and all that.
[1429.30 → 1432.96] And obviously, you've seen that and you're addressing it.
[1433.08 → 1437.98] And you've produced a perfect tool for letting people get that.
[1438.26 → 1443.08] But I'm curious, as someone who's observed that repeatedly, what is it that's causing
[1443.08 → 1445.68] the skepticism in trusting the model?
[1445.68 → 1451.78] And obviously, they get to a point where the tangibility of using Radio allows them to
[1451.78 → 1452.48] get past that.
[1452.56 → 1458.56] But what do you think is causing the challenge the non-machine learning consumer of that model
[1458.56 → 1460.32] is facing up front?
[1460.64 → 1465.32] Well, I think you only have to look at some of these very famous models.
[1465.48 → 1467.10] You look at something like GPT-3, for example.
[1467.22 → 1468.44] OpenAI released this model.
[1468.76 → 1472.64] It's supposed to be able to understand language and answer your questions.
[1472.64 → 1476.36] But people try it, and they discover all sorts of problems, right?
[1476.36 → 1482.28] So you can ask it questions, and it starts making very nonsensical kind of responses or,
[1482.44 → 1484.24] you know, it even suggests very dangerous things.
[1484.36 → 1488.00] I remember there was a study like that showed that if you ask it medical questions, it could
[1488.00 → 1491.28] suggest things that could lead to self-harm and all these terrible things.
[1491.98 → 1493.48] And I myself was part of a study.
[1493.62 → 1497.62] I did a study where we were looking at bias and kind of religious bias and found that GPT-3
[1497.62 → 1501.38] is all these issues associating, for example, Muslims with violence and all of these kind
[1501.38 → 1502.30] of problematic things.
[1502.64 → 1503.54] And that's just one example.
[1504.00 → 1508.28] And so OpenAI did something interesting, which is that they did release it as a demo so that
[1508.28 → 1509.22] people could try it out.
[1509.54 → 1512.36] But that doesn't happen most of the time with research, right?
[1512.40 → 1516.20] So you see all of these really nice sounding numbers and like, you know, state of the art
[1516.20 → 1520.54] this and that and nice models published in nature that claim to solve this problem.
[1520.96 → 1525.20] I remember actually there was one person I talked to when I was a PhD student at Stanford
[1525.20 → 1530.72] and she had made this really nice model to look at videos of people at ICU, kind of in
[1530.72 → 1531.24] the ICU.
[1531.84 → 1535.24] And like from those videos, you could tell if a patient had a particular disease, like
[1535.24 → 1537.08] based on how they were moving around.
[1537.76 → 1540.60] And as she published in nature, and I was like, oh, this is really cool.
[1540.92 → 1542.62] We should try to deploy this in the clinic.
[1542.84 → 1543.68] And then she looked at me.
[1543.72 → 1544.56] She was like, are you crazy?
[1544.56 → 1548.88] I would never trust this in the clinic because like there's a big gap between I think what
[1548.88 → 1553.38] is, you know, publishable and sometimes what people can get away with versus, you know,
[1553.44 → 1556.88] what is actually usable in the real world for all the reasons that we've talked about.
[1556.96 → 1563.60] Like there's usually models are trained and tested on these really nice sanitized data sets.
[1563.94 → 1568.34] And, you know, we don't really expect it to test them on kind of real world settings that
[1568.34 → 1569.34] might be out of distribution.
[1569.94 → 1572.72] And so I think one of the cool things about Radio, and we're seeing this more and more,
[1572.72 → 1579.56] for example, at CVPR 2022, they published papers, and they released a company in Radio
[1579.56 → 1579.88] demos.
[1580.52 → 1583.14] And then the research community was testing them.
[1583.42 → 1584.90] And there were some models that did great.
[1585.02 → 1588.06] Like people were testing them all sorts of difficult ways, and they were doing great.
[1588.18 → 1591.20] And then other models, people found holes relatively quickly.
[1591.66 → 1595.16] And so I think part of it is because, you know, the machine learning community is so
[1595.16 → 1600.42] accustomed to training and testing on these very fixed benchmarks that really, really
[1600.42 → 1604.26] stresses the need for something like Radio to open that up, you know, open up that box
[1604.26 → 1605.84] and let other people tie it with their own data.
[1605.84 → 1635.58] Well, I definitely want to follow up on some things related to.
[1635.58 → 1639.10] Hugging Face plus Radio, but maybe from a different perspective.
[1639.40 → 1645.88] I'm wondering, like, as you were sort of running Radio pre-hugging face, and you had like the
[1645.88 → 1650.96] open source project and in certain ways you might not have known all the ways that people were using
[1650.96 → 1654.18] Radio, but had like some sense of how it was useful.
[1654.42 → 1660.10] And now you've kind of got this like hugging face scale of people using it and an avenue for
[1660.10 → 1662.76] people to share things, and they're sharing a lot of things.
[1663.44 → 1672.06] What sorts of maybe challenges have you faced as you've tried to integrate Radio at like hugging face
[1672.06 → 1679.44] scale and tried to like, you know, scale that up, make sure it runs well for like people as they create
[1679.44 → 1684.84] their own spaces with all sorts of different models, some which might be huge and some which might be
[1684.84 → 1691.04] like pretty easy to run. I just imagine that that's kind of a, well, a really hard thing to do,
[1691.28 → 1695.12] but it seems like you've done it very well. So yeah. Any thoughts there?
[1695.36 → 1696.84] Yeah, that's a good question.
[1696.98 → 1697.86] There's a lot here.
[1697.86 → 1706.60] So one of the things that amazed by is just like the diversity in the types of models that people
[1706.60 → 1710.94] are building. This is like shocking. Like I think sometimes you can be kind of an echo team where
[1710.94 → 1716.06] you think, okay, most people use machine learning for these types of use cases, but then you see
[1716.06 → 1720.32] users that just completely, you know, blow your mind. So for example, you know, people, I don't know,
[1720.32 → 1725.92] using GANs to generate Pokémon or people using speech recognition in so many other languages.
[1725.92 → 1730.36] And you have to realize you have to support Unicode this and that. It's just a lot,
[1730.40 → 1734.98] it's just a lot of different use cases that show up, and you have to kind of address that.
[1735.40 → 1739.98] I think in terms of, so one of the good things about Radio, I talked earlier about how there's
[1739.98 → 1744.10] like two different cycles of machine learning. There's kind of the exploratory slash research
[1744.10 → 1749.02] stage, and then there's actual kind of production level type stuff. So at Radio, we tend to focus
[1749.02 → 1753.56] more on the exploratory research side. And so even when you share a model, let's say on spaces,
[1753.56 → 1759.30] or you share it temporarily. So I don't know if you've seen this, but if you create a Radio demo,
[1759.50 → 1764.40] you can pass in one extra parameter in the launch function, share equals true. And that creates this
[1764.40 → 1768.34] like temporary public link that allows anyone to access your model, which is super, super handy
[1768.34 → 1773.98] for prototyping. And so what we've like entirely focused on, we've said this, we're not trying to,
[1773.98 → 1777.94] you know, optimize for like production level traffics or anything like that. We want to just focus on,
[1778.04 → 1781.60] hey, let a few people try out your model, get feedback, let a few other people try out your model.
[1781.60 → 1787.12] And so that, because we've kind of focused, laser focused on that use case, even when a lot of
[1787.12 → 1792.82] other people are using Radio demos, we have like always stayed with that expectation. So for example,
[1792.92 → 1798.36] people ask us, oh, my space is up on Hugging Face, I want to use it as an API. Well, we added support
[1798.36 → 1801.88] for that, but we kind of made it clear, hey, this is not meant to be like a production level API,
[1802.16 → 1807.70] you can use it for testing and so on. So I think we've mitigated a lot of like traffic type
[1807.70 → 1812.66] related issues just by focusing on this stage of, of kind of the use case. And then the other
[1812.66 → 1817.16] thing that we've tried to do is leverage Hugging Face's existing infrastructure as much as possible.
[1817.72 → 1822.52] So for example, Hugging Face already has something called the inference API. So any sort of model that
[1822.52 → 1826.56] you can find on the Hugging Face hub, which at this point is, I think more than 30,000 different models,
[1826.92 → 1832.82] it comes with its own like inference API that you can just call. So Radio also supports using any of
[1832.82 → 1837.68] the models in the Hugging Face hub pretty much off the shelf. So in like one line of code, you can
[1837.68 → 1843.18] build a demo for one of these models. And if you do it, it leverages Hugging Face's existing inference
[1843.18 → 1847.88] API rather than trying to create something ourselves. So by doing that, I think we've mitigated a lot of
[1847.88 → 1853.48] those like load issues. But what we definitely find is a lot of people using Radio and like these
[1853.48 → 1857.90] different use cases that we wouldn't even imagine. We see, you know, a lot of issues being raised,
[1857.90 → 1861.42] and then we're doing our best to kind of support that. A lot of cool things like people,
[1861.42 → 1866.92] people ask for new types of components as well. And so we're working on supporting that.
[1867.38 → 1872.56] A lot of people ask for like, we're using this space to test our model. We're seeing some,
[1872.60 → 1877.58] you know, kind of weird behaviour. How do we kind of retrain the model based on what kind of issues
[1877.58 → 1881.58] have been observed? So we're thinking about how to fit Radio into kind of this larger loop of
[1881.58 → 1886.24] training models again, and making them better as well. So yeah, a lot of cool things there.
[1886.80 → 1890.32] I'm synced with you pretty well, I think, because you're already going where I was going to ask you,
[1890.32 → 1896.12] and that is, as you talk about these new components that you're building, and you've talked about kind
[1896.12 → 1900.80] of focusing more on the exploratory side of that, but you've already acknowledged that there's the
[1900.80 → 1905.84] kind of the production deployment side, is that where you want to go is it seems like it might be
[1905.84 → 1911.50] a natural workflow that if I'm already doing Radio and getting my feedback with my demos and
[1911.50 → 1917.22] everything that I might ultimately just want to deploy that in a variety of areas. And so as you build
[1917.22 → 1923.12] more components out, is that with that, that in mind of eventually you are robust enough in how
[1923.12 → 1928.58] you're making that model available so that you can that it's Radio all the way and forevermore.
[1928.90 → 1933.72] Yeah, it's interesting. We're thinking about that. And right now we're actually leaning against that a
[1933.72 → 1938.04] little bit. And the reason for that is because that space is first, very crowded. There's a
[1938.04 → 1943.80] lot of like tools that are designed to help you deploy your model. And it's kind of an interesting,
[1943.80 → 1948.66] the issue is, it's one of those things, it's kind of like, I would say like kind of like the Heroku
[1948.66 → 1954.28] type problem, which is that if people get big enough, they don't want to use your solution to
[1954.28 → 1958.32] deploy, they want to do it themselves. If people are small, like they want to, so there's a lot of
[1958.32 → 1962.24] people who are just prototyping. Great. So we've got that use case covered. When people are big,
[1962.40 → 1966.62] like kind of medium size, maybe they'll use like an off the shelf product to deploy your model.
[1966.84 → 1969.54] When they're very big, they're going to write something themselves or use something that's,
[1969.54 → 1975.38] you know, kind of very tightly coupled with one of the big cloud vendors. And so we're actually
[1975.38 → 1982.22] thinking that rather than focusing on the production kind of production use case, which is kind of
[1982.22 → 1987.92] crowded, what we should do instead is make it easier to build more kinds of web applications from Python
[1987.92 → 1992.62] itself. And so I think we're going to be leaning more in that direction. You'll see things like
[1992.62 → 1996.68] potentially solutions for, you know, maybe lightweight labelling solutions built out of Radio,
[1996.68 → 2001.64] or maybe a dataset exploration tools built out of Radio, trying to cover more of those use cases.
[2002.20 → 2002.98] Love the focus there.
[2003.32 → 2010.30] And as you look towards that, I also note that I believe if I'm not mistaken, the sort of main
[2010.30 → 2016.74] core of Radio is open source. I don't know if there are certain things that, you know, are maybe
[2016.74 → 2021.80] integration things with Hugging Face and other things that aren't. But the main bit is, I'm wondering
[2021.80 → 2028.30] how that community has grown over time, and the sort of code base and open source community,
[2028.80 → 2032.44] what you're seeing in terms of activity and interests there.
[2033.08 → 2038.58] Yeah, that's been amazing. And we obviously owe a lot to Hugging Face for that. So like, for example,
[2038.58 → 2042.58] we have a Discord server. I think if we had just launched for Radio Discord server, I don't know
[2042.58 → 2046.16] how many people would have joined, but we're part of the Hugging Face Discord server, which helps a lot.
[2046.16 → 2051.24] And our community is honestly amazing. There are some folks, and this astounds me, there are some folks
[2051.24 → 2056.04] that use Radio every day, and they're like raising new issues. Like I don't use Radio every day.
[2056.66 → 2061.90] You know, so it's been really nice. People catch issues like that. Anytime we break anything,
[2062.20 → 2066.20] people let us know. But I think one of the very interesting developments that we're seeing,
[2066.28 → 2071.42] and we're trying to understand this piece better, is that people used to just have demos as kind of
[2071.42 → 2076.34] standalone things. But now people are taking demos and integrating it onto their websites,
[2076.78 → 2080.90] like as portfolio, you know, as part of their portfolios, but even just as like standalone
[2080.90 → 2086.88] websites. So one of our users, for example, built this NFT search engine using the backend of it is
[2086.88 → 2092.94] a Radio app. He hosted it on Spaces and just like embedded that Spaces on the homepage of his website.
[2093.44 → 2097.08] And so his website, I mean, it has some surrounding information, but it's basically a Radio demo,
[2097.08 → 2101.48] which is very interesting. I mean, you know, and this is not the only one. We've seen this in a
[2101.48 → 2105.40] few different examples. And this kind of raises the question. So now it seems like a lot of people
[2105.40 → 2110.28] are building very data-centric or machine learning-centric applications. That's like the focus
[2110.28 → 2114.28] of it. If there's enough use cases like this, maybe we want to like focus on building, you know,
[2114.64 → 2118.18] kind of this one-stop shop for how to build like a complete data-centric application.
[2118.62 → 2120.06] So we're thinking about that as well.
[2120.56 → 2125.68] I work with a lot of students from Purdue University, have a close collaboration there,
[2125.68 → 2131.44] and other universities as well. And they're always asking me, you know, like as I'm going from like
[2131.44 → 2137.00] grad school into industry, like what can I do to set myself apart? I think for like those of you
[2137.00 → 2142.26] listening out there that are listening to this, like this is like a really cool idea that is very,
[2142.74 → 2148.44] like can set you apart. Like if you're able to go past saying, hey, I ran this cool example in my
[2148.44 → 2153.98] Jupyter notebook and here's like the GitHub repo with the Jupyter notebook. Okay. It renders and I can see
[2153.98 → 2161.22] some images. It's a whole nother level when you can like point someone to spaces or to a radio app or
[2161.22 → 2165.92] embed that in a blog post or your website or whatever and have someone actually interact with
[2165.92 → 2172.26] it. I think that that like goes a long way. We get a lot of requests from people listening to the
[2172.26 → 2177.66] podcast and in our own lives about like people getting into AI and data science. And I think just,
[2177.84 → 2182.34] that's just a general like free, free tip out there. I think this, this episode has,
[2182.34 → 2187.22] has shown that. It really differentiates that person from all the competition. And,
[2187.34 → 2192.04] and I know that in my own organization, we see that as well as people are coming in. If you,
[2192.26 → 2197.30] you know, walk in, and you're a radio expert compared to people who are not able to show that
[2197.30 → 2201.54] it's a huge differentiator for someone. So yeah, it's a great point you're making there.
[2201.88 → 2203.70] Yeah. Yeah. That's a lot of fun.
[2203.82 → 2204.72] It is a lot of fun.
[2205.34 → 2210.86] Yeah. Just to be able to interact with your model. Like it's just so much more real. You know,
[2210.86 → 2214.42] as we've talked about, you start noticing these things that you otherwise would just not have
[2214.42 → 2219.04] even paid attention to. Like a lot of things are just buried under these nice aggregate metrics
[2219.04 → 2222.94] that we like to take a look at, but you just get way more insight when you can actually play around
[2222.94 → 2223.44] with your model.
[2223.44 → 2230.02] And as you look to kind of the future of radio and hugging face and maybe like other things that are
[2230.02 → 2238.04] happening with those two things, what are some of the things that are exciting to you about maybe the
[2238.04 → 2245.34] the AI space more generally, and then maybe more specifically in a hugging face and radio world?
[2245.42 → 2250.76] Like what, what are you thinking about that? You're super excited about the developments of,
[2250.76 → 2255.96] looking forward to the future. Yeah, absolutely. So I think one thing that really excites me is that
[2255.96 → 2260.96] we are moving away from this, like what we've talked about, you know, this, this benchmarking
[2260.96 → 2265.50] on these static data sets and that's it. Now a lot more people are interested in out of distribution
[2265.50 → 2271.50] robustness, right? Like we've trained a great model on our data set. What kind of guarantees can we give
[2271.50 → 2275.54] about how well it's going to perform in the real world? Obviously it's a very difficult topic,
[2275.54 → 2280.02] but there's a lot more interest both on the academic side. And then also on the industry side,
[2280.02 → 2284.26] with practical tooling. And so this is where I think, you know, we're going to see companies,
[2284.38 → 2289.08] you know, potentially including hugging face also invest more resources in like you have some models
[2289.08 → 2294.86] out there. How can you effectively flag issues that the model is having so that other people who use
[2294.86 → 2300.94] it is aware of these limitations can contribute to the robustness of the model? Because I do think
[2300.94 → 2306.18] at the end of the day, so it's a it's a problem that's probably going to be, it's very hard,
[2306.18 → 2310.86] but I think to formulate this problem in a clean way such that we can tackle it from a theoretical
[2310.86 → 2314.72] point of view or an academic point of view, I think what we need are better tools like to identify
[2314.72 → 2319.82] issues behind models and, and to like, let people almost like, you know, just the way,
[2320.00 → 2324.54] same way like GitHub, for example, has issues and PRs, you know, what is the equivalent of that for
[2324.54 → 2329.36] machine learning look like? So that the people are kind of aware of the issues and can make things
[2329.36 → 2333.26] better. So that's something I'm personally very excited by. I think radio plays a role with that in
[2333.26 → 2337.94] helping discover these issues, but I think it's a much bigger problem just alone that great we can
[2337.94 → 2342.96] solve. Yeah. And you mentioned even, we didn't go into it in detail, but you do have this flagging
[2342.96 → 2349.00] feature within the app. Could you maybe tie in how that, how you see that fitting into what you're
[2349.00 → 2354.44] talking about with this out of distribution input and that sort of thing? Yeah, absolutely. So this is
[2354.44 → 2358.86] one of like the core fundamental things that we added to Radio early on, and we see people using it
[2358.86 → 2365.12] very actively to this day, which is that Radio lets you try out your own data in potentially
[2365.12 → 2368.70] someone else's model or your own model, right? You can put it, you can drag and drop your own image,
[2368.96 → 2372.78] you can type your own text, you can edit it, you can play around with it. And let's say you find
[2372.78 → 2377.74] something that the model isn't working well on. Let's say, I mean, just for an example, if you take
[2377.74 → 2383.96] a state-of-the-art image classifier, and you put in a picture of a bride who's wearing Western attire,
[2383.96 → 2388.72] like American, let's say, you know, typical, it predicts bride, bride or ceremony, you know,
[2388.74 → 2394.06] pretty reasonable labels. But if you put in a picture of a bride from Pakistan, where I'm from,
[2394.36 → 2399.16] or India, it usually predicts things like costume or performance or something that's, you know,
[2399.18 → 2403.58] could be, that's wrong. Maybe it could be borderline offensive as well. You know, you find issues like
[2403.58 → 2406.66] this all the time with all sorts of machine learning models that we've talked about, they're very fragile.
[2407.16 → 2413.08] And so what this flagging button lets you do is it saves that sample, and it stores it to a local
[2413.08 → 2417.58] database in like a CSV file, basically. And so the workflow, what this looks like in practice,
[2417.58 → 2422.14] and we see this often is people will create a Radio demo, and they'll share it because it's so
[2422.14 → 2426.00] easy to share that demo. It's like a just like a link, like a Google Drive link. You share it with
[2426.00 → 2430.14] a bunch of people that try out your model, they identify issues, and that helps you. And then they
[2430.14 → 2433.50] can just click the flag button. That's all they have to do. And then you have this nice CSV of
[2433.50 → 2438.20] everything that's been flagged, and you can say, ah, okay, maybe I should retrain my model on these
[2438.20 → 2442.96] samples, or maybe I have some better understanding of what the failure points are. We have users
[2442.96 → 2446.90] who used to like, you know, have spreadsheets where they would send these spreadsheets back
[2446.90 → 2450.70] and forth over email. It's kind of a replacement for that and maybe a better way to do it.
[2450.92 → 2457.10] Yeah, I think this is super important. And yeah, I'm just really excited about the future with these
[2457.10 → 2461.98] sorts of tools and what you're doing. Keep up the good work. Really appreciate you taking time
[2461.98 → 2468.12] out of your busy Radio hugging face life to let us know about these things. It was a pleasure
[2468.12 → 2469.86] talking. Hope to talk again soon.
[2469.86 → 2474.30] Yeah, it was great. Thank you so much for having me here and all the great questions.
[2474.30 → 2475.12] All right. Bye-bye.
[2475.12 → 2489.96] All right. That is Practical AI for this week. If this is your first time listening, subscribe now
[2489.96 → 2496.00] at practicalai.fm or just search for Practical AI in your favourite podcast app. We're in there.
[2496.32 → 2500.98] And if you're a longtime listener, please do share the show with your friends. It is the best way you
[2500.98 → 2506.62] can help Practical AI succeed. Thanks again to Vastly for shipping our shows superfast all around the
[2506.62 → 2510.98] world to Break master Cylinder for the Beats and to you for listening. We appreciate you.
[2511.32 → 2513.68] That's all for this week. We'll talk again next time.
