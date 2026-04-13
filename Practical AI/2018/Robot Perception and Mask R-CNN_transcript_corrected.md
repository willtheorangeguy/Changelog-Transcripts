[0.00 → 6.70] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[6.70 → 11.42] things here at Changelog because of Rollbar. Check them out at Rollbar.com, and we're hosted
[11.42 → 17.36] on Linde servers. Head to linode.com slash Changelog. This episode is brought to you by
[17.36 → 23.72] DigitalOcean. They now have CPU optimized droplets with dedicated hyper threads from best in class
[23.72 → 29.18] Intel CPUs for all your machine learning and batch processing needs. You can easily spin up
[29.18 → 34.74] their one-click machine learning and AI application image. This gives you immediate access to Python 3,
[35.20 → 42.68] R, Jupyter Notebook, TensorFlow, Sci kit, and PyTorch. Use our special link to get a $100 credit for
[42.68 → 51.28] DigitalOcean and try it today for free. Head to do.co slash Changelog. Once again, do.co slash Changelog.
[59.18 → 68.60] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[69.02 → 74.52] productive, and accessible to everyone. This is where conversations around AI, machine learning,
[74.56 → 78.66] and data science happen. Join the community and snag with us around various topics of the show
[78.66 → 84.48] at changelog.com slash community. Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[89.18 → 95.46] Hey, welcome to another episode of the Practical AI Podcast. I'm Chris Benson, an AI and digital
[95.46 → 101.70] transformation strategist. And with me is my co-host, Daniel Whiten ack, who is a data scientist who likes
[101.70 → 108.32] to use AI to do good. Hey, Chris, how's it going? Doing very well. We have a pretty good episode lined up
[108.32 → 115.22] here, I think. We have Chris Rebellion, whom I'll introduce in just a minute. And he is a guy I've known
[115.22 → 120.32] for a while. And we're going to be talking about some computer vision stuff today that's really
[120.32 → 126.28] state of the art. Yeah, I'm excited to kind of dig into a few of the nuts and bolts of some things that
[126.28 → 131.40] we've mentioned in previous episodes, but haven't really gotten into the weeds with. So I'm excited
[131.40 → 137.92] about that. I am too. So I'm going to introduce Chris Rebellion and tell you a little bit about him.
[137.98 → 142.50] And then I'll turn it over to Chris for a second. Chris and I have actually worked together at
[142.50 → 148.30] Honeywell, where we were both kind of plank owners of the very first dedicated AI team at Honeywell
[148.30 → 153.60] Safety and Productivity Solutions. And I'm no longer with Honeywell, but Chris still is and is
[153.60 → 158.86] doing some really cool work. And I miss being able to work with him. How are you doing today, Chris?
[159.34 → 162.64] Hey, Chris. I'm well. How are you? I'm doing great. Thanks for joining us, man.
[162.86 → 166.92] Yeah, I'm going to be confusing with two Chris's. That's true.
[166.92 → 171.68] Chris and I worked together for a while, and we dealt with that. So hopefully that experience will come in
[171.68 → 176.94] handy here. Awesome. So maybe I'll say Mr. Rebellion and make it sound all official.
[177.08 → 184.22] That's very formal. Yeah, it doesn't feel right, though. So, okay. So we are just for our audience.
[184.46 → 190.42] Last night, I was actually with Chris, because he was at the Atlanta deep learning meetup doing a
[190.42 → 199.26] fantastic presentation on mask RCNN, which is a deep learning algorithm for computer vision. And
[199.26 → 205.68] we're going to do a deep dive in this episode into what that is and the pros and cons and cool
[205.68 → 210.40] things about it. So I'm pretty excited about it. And Chris, thank you for doing such a fantastic job
[210.40 → 213.36] last night. And I'm really looking forward to our conversation today.
[213.80 → 218.82] Oh, my pleasure. Last night was a lot of fun. I had a good time doing it and looking forward to
[218.82 → 223.60] talking about it some more today. Cool. Well, you know what? I am going to start us off with the first
[223.60 → 229.68] question. And I guess I'd like you to just kind of tell us what robotic perception is, since we're
[229.68 → 236.86] talking about robotic perception for mask RCNN. Sure. So robotic perception is basically about
[236.86 → 243.74] seeing understanding, using sensors so that the robot can interpret the environment and understand
[243.74 → 249.56] its place within that environment. Typically, we do that through a combination of 2D sensors,
[249.56 → 256.22] 3D sensors, other types of sensors. But it's basically helping the computer that's part of the
[256.22 → 263.46] robot to understand that environment. So what kind of robots are we talking about? You know, like
[263.46 → 271.88] what are in the context of manufacturing or like, you know, Roomba's? What are we talking about here?
[272.10 → 277.52] Yeah. So good question. Really all robots, right? It's easy to think of it in terms of, say,
[277.52 → 284.78] a robotic arm in a manufacturing environment where it has to move and perform some task. But robot
[284.78 → 289.72] perception also applies to something like self-driving cars, where you have to understand
[289.72 → 295.90] the environment that you're in. So it's really all robots. Yeah. So a robot, I guess, doesn't have to
[295.90 → 303.30] mean like, you know, articulating arms and quasi eyes or something, but really any kind of, you know,
[303.30 → 309.56] machine that is trying to get some sense about its environment. Is that accurate?
[309.56 → 311.02] Exactly. That's exactly right.
[311.40 → 316.32] So I guess I'd like to get a sense as we're tying some of this together in the beginning,
[316.50 → 320.38] you know, robotic perception has been around for a while with some other techniques, but in
[320.38 → 326.44] recent time, deep learning has really had a profound impact on it. And so I guess, can you describe the
[326.44 → 332.68] role of deep learning in robotic perception and maybe put it in some context with some of the other
[332.68 → 337.32] methodologies that either are also currently being used or maybe have been used in the past?
[337.32 → 343.38] Sure. So, you know, traditionally, we've used computer vision techniques that were not based
[343.38 → 350.18] on deep learning. So an example would be something like canny edge detection, huff line transforms.
[350.18 → 357.32] These are, these are more traditional approaches to detecting curves and lines and edges of objects.
[357.86 → 364.28] And then, and there's still a lot of that type of approach being used within robotic perception.
[364.28 → 371.64] But around, say, 2010, 11, 12, right, that's when we started to see deep learning being applied to
[371.64 → 380.16] computer vision tasks. So Alex Net came out in 2012, and it was one of the first algorithms that deep
[380.18 → 385.52] learning algorithms to try to classify objects. And then things have just kind of built on top of
[385.52 → 391.56] that. And so later algorithms came out, they get the neural networks became deeper and deeper and
[391.56 → 396.90] more capable of detecting and classifying these objects. And so really, that's sort of been the
[396.90 → 403.52] trend over the last few years is to move from that traditional approach of computer vision to the
[403.52 → 406.44] deep learning approach for computer vision and perception.
[406.44 → 413.58] And you mentioned kind of detecting and identifying is, is there really two parts of it? Is it,
[413.64 → 419.38] is it about like knowing, you know, knowing there's an object in my environment? And then secondly,
[419.38 → 425.92] knowing what that object is, are those typically separate things or those do those go together? How,
[426.00 → 427.12] how is that handled?
[427.66 → 433.60] So in deep learning, typically, we're doing a few things. So we're taking classification,
[433.60 → 439.74] which is typically thought of for single objects in an image. And you'd say, oh, that's a picture of a
[439.74 → 446.14] cat or a dog or a person. But the more advanced algorithms are able to detect multiple objects
[446.14 → 453.56] within that scene. So you might say, hey, I see two cats and two dogs and a person. And you would be
[453.56 → 460.70] able to identify where within the scene, each of those objects actually is. And so then this mask our CNN
[460.70 → 467.32] algorithm can actually go a step further and say, which pixels within that image that I'm seeing
[467.32 → 473.40] belong to which object. So these pixels go to this cat and these pixels below belong to this dog.
[473.84 → 479.66] Interesting. Yeah. And just for, for our audience members who are joining us in this episode,
[479.78 → 485.26] in a previous episode and in episode seven, we had a great discussion with, with Jared Lander about what
[485.26 → 491.42] deep learning is itself and how it fits into the landscape of AI. So definitely check that out if
[491.42 → 499.08] you're kind of first learning about these things. But you mentioned, you know, mask our CNN, maybe we
[499.08 → 504.86] could just kind of start moving that direction by talking about, you know, breaking down that,
[504.96 → 510.92] that acronym. So like the CNN part is, is not a news network, right? What, what, what are we,
[510.92 → 517.40] what are we talking about? So CNN is in the deep learning world known as convolutional neural network.
[517.40 → 525.36] So it's a neural network that's based on the idea of these convolutions. The R in our CNN is region.
[525.72 → 533.50] So the way that the algorithm goes about figuring out what's in each part of the image is by generating
[533.50 → 538.30] these regions, a region, they're called regions of interest. And then it looks at the regions of
[538.30 → 544.36] interest that it generates and tries to detect if there's an object in that region. And if it does
[544.36 → 550.78] detect an object, it tries to classify it. If it doesn't detect an object, it just says, oh, this
[550.78 → 556.80] area is just background. So quick question for you, Chris, as we start looking at mask our CNN,
[557.34 → 563.56] could you actually give us a little bit of a an understanding of, of how that fits into the
[563.56 → 570.82] larger category of convolutional neural networks and give us a baseline of what CNNs are able to do?
[570.82 → 575.00] And then contrast that as we start working into a mask or CNN.
[575.64 → 582.16] Okay. So maybe we'll talk a little bit about CNN versus just a traditional feed forward neural
[582.16 → 590.40] network. So maybe folks are lists are familiar with, uh, like a LSTM or, uh, RNNs, things like that.
[590.40 → 595.04] Yeah. If you could even give us, I think probably a lot of people in our audience are most familiar
[595.04 → 600.30] with, uh, just basic feed forward networks. And if you could talk about what a convolutional neural
[600.30 → 606.12] network does on top of that, what it's adding to it, and then we can kind of go into mask our CNN,
[606.12 → 611.02] uh, and go farther. And that way, if someone hasn't been exposed, um, uh, all three of us have
[611.02 → 615.90] been exposed to CNNs for quite some time, but it gives somebody a path on, uh, evolving where
[615.90 → 621.64] they're going with this. Perfect. So in a traditional feed forward network, um, you have
[621.64 → 628.30] the data coming in at one end of the network, and then you have, uh, several, maybe many hidden layers
[628.30 → 634.50] and the input, sorry, the output from one layer becomes the input to the next. And that's how it's
[634.50 → 642.34] a feed forward. And typically as you move through the network, you have fewer and fewer nodes within
[642.34 → 646.94] each layer. So you're doing fewer and fewer computations as you move along the network.
[647.42 → 651.70] That helps a lot. And how, what does, what does, uh, when you add convolutions in,
[651.84 → 653.44] what does that due to that architecture?
[653.68 → 658.30] Right. So the convolutions are important for images, especially because the convolutions are
[658.30 → 665.52] the best way to think of it is said a three by three grids. So you're looking at three pixels by three
[665.52 → 672.32] pixels at a time, and you're moving that grid across the image from left to right. And then you go
[672.32 → 678.12] to the next row, and you do it again from left to right. So you're moving down the image and going left to
[678.12 → 686.28] right, looking at a set defined number of pixels at a time. And those, we call them kernels. And that kernel
[686.28 → 692.96] varies in size. So you might start with a three by three and go across the entire image. And then you could do a
[692.96 → 699.56] maybe a nine by nine kernels and look at the image. And then a bigger one, maybe a, you know, 32 by 32.
[699.56 → 705.24] And the important thing to remember with CNNs is because those kernels are square,
[705.24 → 711.36] you are maintaining, maintaining that spatial relationship between the pixels, which for images
[711.36 → 716.70] is important, right? If you think about an image, and you're looking for say a cat, you know, that the
[716.70 → 723.24] eyes are going to be close together. So you want to maintain that spatial relationship because the eyes
[723.24 → 727.20] should be close together. You shouldn't be looking for an eye in the upper left corner and an eye,
[727.20 → 729.90] you know, in the bottom right corner, that would be unlikely.
[730.54 → 734.30] So there's a relationship between the pixels that matters because we're talking about images.
[734.56 → 737.24] Yes, the relationship, the spatial relationship. That's right.
[737.66 → 744.50] Yeah. And so you mentioned like things like Alex Net in earlier in our discussion, which, you know, are
[744.50 → 750.68] various, various models that have been developed over time for image related detections.
[750.68 → 759.54] Do a lot of these image based models or models trying to do object detection and images,
[759.98 → 764.38] is it fair to say that most of them involve convolutions in one way or another?
[764.64 → 770.00] That's right. They all involve convolutions in one way or another. The difference really is in
[770.00 → 776.16] the size of that kernel, the combinations of sizes that they're using, the values that are within those
[776.16 → 783.98] kernels for each of those cells. And then over time, how many layers there are in that network,
[783.98 → 789.92] because as the technology got better, as the GPUs got faster, they could do more and more training
[789.92 → 793.86] in a set amount of time. And so they were able to have deeper networks.
[794.56 → 800.68] Awesome. Yeah. So, I mean, we've kind of gotten into the convolutional part, and you've mentioned that
[800.68 → 807.08] there's kind of various incarnations of this. Maybe we can step back and kind of go back to the robot
[807.08 → 815.06] perception use case. And maybe you could share with us some of the challenges that you face in that
[815.06 → 822.24] particular use case and maybe challenges that might motivate you to use something like mask R or CNN,
[822.54 → 830.04] which we'll eventually get to. But what are the kind of motivating challenges in this field
[830.04 → 835.72] that make just kind of the normal convolutional neural network, quote unquote, normal? I don't know if
[835.72 → 843.32] any of them are normal, but what might not make it enough? Sure. So with the CNN networks, basically,
[843.32 → 850.14] they're used for the classification. So I see a cat or a dog or a person or whatever the object is.
[850.44 → 857.66] And then typically what we're doing is we're taking that network and also at sort of at the end of it,
[857.66 → 864.70] applying more technology to say, OK, can we identify where the object is in the image?
[865.28 → 869.98] Right. So that bounding box, if you're familiar with that term, where we try to draw the box around
[869.98 → 877.20] the object that kind of comes towards the very end. But we're still using the CNN network to identify
[877.20 → 883.30] what the object is. And so we do that additional processing later. So with something like mask,
[883.30 → 889.60] in addition to that bounding box regression to determine the position, we're also then doing
[889.60 → 895.98] another set of steps or calculations to say where within that bounding box is the image exactly.
[896.64 → 903.18] That makes sense. I'm wondering just kind of maybe off of one of my previous questions. So when you
[903.18 → 908.10] say you're kind of adding to the end, are you meaning like you have kind of different models for the
[908.10 → 913.58] bounding box thing and the detection thing or that's all kind of rolled into one end to end
[913.58 → 920.48] architecture? Is that kind of how it works or is? Yeah, good question. It's added on at the end.
[920.58 → 929.26] It becomes part of the overall network, but really it's tacked on at the end. And so the base,
[929.48 → 934.68] what we call feature extraction, which is pulling out those little features, the straight lines,
[934.68 → 941.22] the curves, a lot of the relationships between the pixels that can often and actually is often based
[941.22 → 947.98] on an existing classification network. So for instance, in the case of mask RCNN, it uses something
[947.98 → 954.12] called Reset to do its feature extraction and classification. And then on top of that,
[954.20 → 962.92] the creators of mask RCNN added the ability to define exactly where the pixels are within the object.
[962.92 → 967.92] And you mentioned something that I think would be worth taking a moment. You talked about feature
[967.92 → 974.04] extraction. And as we as you work toward doing classification, could you take just a second
[974.04 → 980.14] and talk about how you do feature extraction from the simplest lines, you know, up through the
[980.14 → 984.30] different things that eventually become the classification of an object? Can you speak
[984.30 → 987.40] to that for a moment for those who may not be familiar with it? Sure, I'll give that a try. It's a
[987.40 → 993.38] little tough without visuals. But basically, you know, a CNN network is perfect at extracting
[993.38 → 999.84] what we call features, which is the example I just gave. So we're looking for maybe curved lines to
[999.84 → 1005.42] one direction and then curved lines to the other direction. We're looking for those edges where
[1005.42 → 1011.10] maybe we have light and dark colours coming together. Maybe we're looking for straight lines.
[1011.10 → 1015.46] So if you think about like detecting something like an airplane, right, you would need a combination
[1015.46 → 1021.74] of all of these features to be recognized, right? So you would need straight lines to detect the wings,
[1021.74 → 1028.12] but you would need to need curved line detections for like the front of the aircraft. All right. So
[1028.12 → 1033.34] and then where they are, because we talked a little bit earlier about spatial relationships,
[1033.34 → 1039.16] where those features are matter, right? You need to have for it to be an airplane,
[1039.16 → 1045.34] you would have straight lines kind of out to the sides, and you would have more roundness in the centre,
[1045.58 → 1051.08] for instance. So would it be fair to say that you're starting with some of the most basic or atomic
[1051.08 → 1056.60] things, such as a simple line or a gradient from dark to white, and you're building up almost like
[1056.60 → 1063.92] Legos, an object out of these very primitive detections up into something that's more comprehensive
[1063.92 → 1068.98] leading to your object? That's exactly right. So the earlier layers of your network are
[1068.98 → 1074.26] detecting those simpler features like you described. And then as you add more layers,
[1074.66 → 1080.28] remember, remember the, the output of the earlier layers become inputs to the next layer. So the next layers are
[1080.28 → 1087.34] operating on those features that were detected. And so it's trying to build patterns from features. So the earlier
[1087.34 → 1093.64] feature detection is looking at like straight lines and curved lines and things like that. And then it's looking for
[1093.64 → 1099.56] maybe curves that are like an eye. And then you're looking for, oh, two eyes together that's that,
[1099.80 → 1103.80] you know, maybe it's the part of a face. And then you add more features that have the whole head.
[1103.88 → 1109.96] So you're building, as you said, Chris, you're building from the finer representation of the features to
[1109.96 → 1111.02] more complex.
[1111.38 → 1116.42] Yeah, so I mean, this, this all sounds great. So I mean, it sounds like you've got your network,
[1116.42 → 1122.70] it's got this, you know, portion that's, that's detecting all of these features and determining, you know,
[1122.70 → 1128.84] let's say if you have a cat in your image, and then you've got this portion tacked on that might be detecting
[1128.84 → 1136.76] bounding boxes of where that that cat's located within the image. What prompts someone to go further than that?
[1136.84 → 1140.60] So to go beyond CNN, kind of going back to where we started this conversation,
[1140.60 → 1148.48] why the mask are part? What challenges are still present, even if we're using kind of this CNN
[1148.48 → 1149.84] based network?
[1150.18 → 1155.66] Yeah, great question. So the example we use last night at the meetup from the Udacity robotics
[1155.66 → 1164.94] nondegree program, one of the assignments is to take a robot that has two arms, and in front of it is a
[1164.94 → 1173.46] desk with various objects, things like a bar of soap, I believe it was an eraser, a tube of toothpaste,
[1173.66 → 1181.02] etc. And you have to perceive what's on the desk. And then you have to manipulate the robot arms
[1181.02 → 1188.32] to grab the item and then put it into a basket to the side. So if you think about grabbing that tube
[1188.32 → 1195.46] of toothpaste, well, if it's perfectly aligned with the table, then you just kind of reach forward and
[1195.46 → 1201.78] you grab it. But if it happens to be turned at a 45-degree angle, you also have to adjust the arm
[1201.78 → 1208.34] to match that rotation, and then you can grab it. So if you think about a bounding box, so the bounding
[1208.34 → 1213.14] box just says, hey, somewhere in this box is this tube of toothpaste, but you don't know which way it's
[1213.14 → 1219.24] pointing or how it's oriented. The mask, since it fills in the pixels for you of where the object
[1219.24 → 1225.12] is, you can look at it and say, oh, it's not straight up and down, it's actually at a 45. And so I need to
[1225.12 → 1234.02] turn my arm. Okay, so I'd like to ask a question before we dive fully into NASCAR CNN about what the
[1234.02 → 1241.48] options are within the different CNN architectures that might be available for robotic perception, you know,
[1241.48 → 1248.50] such as YOLO or others. And, and at a very high level, if you could just give us a sentence or two
[1248.50 → 1255.34] and kind of what different options there are, and, and then why you might have chosen to go NASCAR CNN
[1255.34 → 1262.34] for a given solution that you're looking for. Okay, so something like a YOLO, which is a great
[1262.34 → 1268.02] algorithm, it only gives you the bounding boxes. So a lot of times, though, that's all you need,
[1268.02 → 1273.68] right? So trying to think of some good examples. So like, if you're doing maybe a self-driving car,
[1274.00 → 1281.04] if you're able to detect in front of you is a pedestrian, or another vehicle, and you have a
[1281.04 → 1286.42] bounty box around it, that's probably close enough, right for being able to make a decision as to
[1286.42 → 1291.94] what you should do, right? If this thing is clearly in front of you, it doesn't really matter exactly
[1291.94 → 1297.44] where the mask outline of that object is, you're able to detect that there's something in
[1297.44 → 1303.12] front of me, and I should perhaps slow down or stop. NASCAR CNN, because it gives you the masks,
[1303.20 → 1310.18] it's perfect for when that orientation matters. So the example we just gave about a robot arm having
[1310.18 → 1313.68] to pick objects off of a table is a good example.
[1321.68 → 1327.70] This episode of Practical AI is brought to you by Hired. One thing people hate doing is searching
[1327.70 → 1332.92] for a new job. It's so painful to search through open positions on every job board under the sun.
[1333.16 → 1339.32] The process to find a new job is such a mess. If only there was an easier way. Well, I'm here to tell
[1339.32 → 1340.32] you how to do it. And I'm here to tell you how to do it. And I'm here to tell you how to do it.
[1340.32 → 1344.32] Our friends at Hired have made it so that companies send you offers with salary, benefits,
[1344.32 → 1349.90] and even equity up front. All you have to do is answer a few questions to showcase who you are
[1349.90 → 1354.96] and what type of job you're looking for. They work with more than 6,000 companies from startups to large,
[1354.96 → 1360.18] publicly traded companies in 14 major tech hubs in North America and Europe. You get to see all of
[1360.18 → 1365.42] your interview requests. You can accept, reject, or make changes to their offer even before you talk with
[1365.42 → 1369.42] anyone. And it's totally free. This isn't going to cost you anything. It's not like you have to go
[1369.42 → 1372.92] there and spend money to get this opportunity. And if you get a job through Hired, they're even
[1372.92 → 1376.80] going to give you a bonus. Normally it's $300, but because you're a listener of Practical AI,
[1377.22 → 1382.14] it's $600 instead. Even if you're not looking for a job, you can refer a friend and Hired will send
[1382.14 → 1387.88] you a check for $1,337 when they accept the job. As you can see, Hired makes it too easy.
[1387.88 → 1391.10] Get started at Hired.com slash Practical AI.
[1395.42 → 1414.50] So in terms of, you know, some of the challenges with moving beyond this bounding box sort of idea
[1414.50 → 1422.82] and moving more towards the mask idea, it occurs to me that, you know, it's already a somewhat
[1422.82 → 1428.48] challenging problem to get good, you know, labelled training data for just like a bound,
[1428.68 → 1434.64] you know, the bounding boxes and labels of, of objects within images. It seems like that would
[1434.64 → 1441.26] be even more challenging if you're wanting to, you know, label the proper masks within an image for
[1441.26 → 1446.80] particular objects where you're getting even more detail, not just, you know, where the objects are
[1446.80 → 1453.56] within what region, but you know what the actual mask of the object is. Is that a problem or are
[1453.56 → 1457.32] there, are there, have there been techniques developed to deal with that?
[1457.82 → 1464.90] Yeah, it's a huge problem. So if you think about the simpler example of classifying an object, so
[1464.90 → 1470.98] is this a cat, a dog, a person? You could, if you were doing training on those images, you could do
[1470.98 → 1476.80] something simple like create a directory for each type of object. And for instance, you have a directory
[1476.80 → 1482.72] called dog and that directory name becomes the object name, the class name, and you put all of
[1482.72 → 1489.28] your pictures of dogs into that directory, and you train and that's, that's your labelling, right? But to
[1489.28 → 1496.32] do something like detecting the right location of the bounding box, you have to take those images and draw
[1496.32 → 1504.18] the bounding box around the individual objects and then train. So extending that further to something
[1504.18 → 1510.84] like mask, since you want to get accurate masks, you can't just draw bounding boxes around each of
[1510.84 → 1517.74] the objects. You have to draw the actual outline. So you end up generating a polygon typically, some
[1517.74 → 1525.42] really odd shape enclosed outline for each of the objects. So if you had an image, say, of, you know,
[1525.42 → 1530.26] four cats and four dogs, that's eight objects you have to outline. And it becomes really tricky
[1530.26 → 1536.22] when they're occluded or one is in front of the other. So it's only partially showing, and you have
[1536.22 → 1540.76] that common boundary between the two. You want to be really accurate when you do that. So yeah,
[1540.88 → 1546.76] labelling or annotating data for masks is cumbersome and tedious.
[1547.34 → 1552.78] And one thing I'd like to clarify in case we have any listeners that aren't familiar with what masks are,
[1552.78 → 1562.40] masks are specifically where you apply a bunch of pixels together to form that polygon that Chris was
[1562.40 → 1567.14] alluding to, to where if you were looking at it visually, it would almost be maybe you're applying
[1567.14 → 1573.04] a colour for those pixels, and you'd almost have like a green overlay over a person's body that you're
[1573.04 → 1577.78] masking in a picture. And you might have many of those masks, but I just wanted to define that for
[1577.78 → 1583.66] everyone so they could follow along. With, I guess, as you, I like to talk a little bit about as you're,
[1584.08 → 1589.98] as you're getting into labelling the data, and you're looking at the data sources that you're pulling in
[1589.98 → 1595.32] and how you do that, what are the typical data sources that are used in the process, and how do
[1595.32 → 1601.04] they come together for the training? So if you're familiar with the COCO data set, over the last few
[1601.04 → 1607.20] years, folks have been taking the COCO data set and providing the masks. So they've been going in and
[1607.20 → 1612.56] annotating, providing that, that polygon around the individual elements or the individual objects
[1612.56 → 1618.48] within each of the images. So that allows the people that created the original mask or CNN
[1618.48 → 1624.42] network to do transfer learning, which is your start with, you know, an existing set of weights.
[1624.88 → 1630.08] So they were able to use an existing set of images that were already annotated and create their
[1630.08 → 1637.80] algorithm. And then what we do now is we take those weights that they use to create the original
[1637.80 → 1645.22] mask or CNN network from, and we use that as the starting point to train for images that we want
[1645.22 → 1650.18] to now detect. So let's say there's something else that we want to detect that's not part of the
[1650.18 → 1657.58] original COCO data set. So we, we train with new images. So we have to go out and obtain those images,
[1657.58 → 1666.04] annotate those images, and then apply the training on those images with the COCO weights as our
[1666.04 → 1670.24] starting point. And that's actually called transfer learning. Awesome. Yeah. And when you're doing
[1670.24 → 1676.74] that, I mean, cause if I'm thinking of, you know, I'm, you know, listening to this podcast, listening
[1676.74 → 1683.16] to you, you know, talk about all of these exciting things, I might want to, you know, I might have a use
[1683.16 → 1687.92] case that it's fascinating for this, or I might want to try it on data that's maybe, you know,
[1687.92 → 1694.26] like you said, not, not already masked as part of say the COCO data set. Is that just like when you're,
[1694.46 → 1700.08] when you're doing that in, in your context, is it a matter of you and your team going through and, and
[1700.08 → 1709.10] annotating those, those images, or have you kind of found any efficient ways to, you know,
[1709.10 → 1713.58] crowdsource those within your organization or anything like that? Or have you, have you heard
[1713.58 → 1719.72] of any, any ways to kind of speed up that process or is it still just kind of a brute force getting
[1719.72 → 1724.36] through everything? Yeah. So that's a great question. Unfortunately, it was me and my team
[1724.36 → 1728.86] that had to annotate the first set of images. And that took, took quite a while. The images we were
[1728.86 → 1735.40] Like how long? So the images we were doing would have anywhere from say up to maybe 40 or 50 objects
[1735.40 → 1739.86] in it. And it might take 15 or 20 minutes to annotate one image. And so, you know, with deep
[1739.86 → 1743.54] learning, you want to have a lot of images. You want, you want to have a lot of training data.
[1744.04 → 1750.14] So after I think a few hundred of these images, we, we kind of said, you know what, let's just
[1750.14 → 1756.12] do a proof of concept with what we have because it's taking so long to annotate. And we got to that
[1756.12 → 1761.82] point, and we created our model. And then we said, okay, you know, we proved out the concept and said,
[1761.82 → 1766.28] okay, if we really want to go forward with this, we need to do this at scale. And so as you pointed
[1766.28 → 1771.90] out, uh, yeah, you want to either engage with a company that does this. There are a number of them,
[1771.90 → 1779.40] uh, that do this for you. Uh, they hire folks, um, really around the world that can go ahead and
[1779.40 → 1783.20] annotate your images for you. And that's, that's really the way to go at scale.
[1783.68 → 1789.48] Yeah. So it, you know, bribing people with, with, uh, pizza and getting together, you know,
[1789.48 → 1792.32] one night to annotate data sets only gets you so far.
[1792.54 → 1796.44] It really does. Especially if it's taking 15 minutes per image, you know, you wouldn't get
[1796.44 → 1798.34] too many done even with a couple of pizzas.
[1799.06 → 1805.64] So I guess I would draw us back to, uh, mask our CNN and, and I guess ask you, uh, to kind of,
[1805.82 → 1814.54] as we start, uh, talking about the algorithm itself, can you define what our CNN is and then define
[1814.54 → 1819.70] when you add mask over that, how would you do that with the intention here of, of taking us
[1819.70 → 1823.84] deeper into the specifics of the algorithm? Sure. So the CNN, as we said, that's the
[1823.84 → 1830.70] convolutional neural network. R is the is region proposal. So again, the way that this algorithm
[1830.70 → 1837.28] decides, uh, whether it sees any objects is it looks in different regions or different parts
[1837.28 → 1842.08] of the image. And it tries to classify what it sees in each of those parts as being either background
[1842.08 → 1848.38] or not background. And if it says, Hey, this is not background, then it tries to figure out what
[1848.38 → 1854.44] it is exactly that tries to classify it. So the regions, uh, are different sections of the overall
[1854.44 → 1858.68] image that it's looking at in different scale and different proportions, different sizes.
[1859.24 → 1864.96] And then the, the mask bit is just the, the idea. So instead of tacking on the end, the
[1864.96 → 1871.38] bounding box piece, you're, you're kind of tacking on the piece to actually map out these masks.
[1871.38 → 1876.94] Is that right? Does it work in the same way in that you would kind of bolt this onto the end or,
[1877.06 → 1881.96] or is that different? Exactly. Exactly. So towards the end of the network. And the reason it's at the
[1881.96 → 1886.88] end is because you're, you're using those same features that you've extracted earlier in the
[1886.88 → 1892.52] network that you're using to classify it. You're also using those features to decide where the mask
[1892.52 → 1898.40] should go. So, uh, a point about the mask, probably the best way, at least the way that I think about it
[1898.40 → 1904.26] is the mask gives me the X and the Y or the if you want to think of it in terms of the image,
[1904.36 → 1909.68] the row and the height coordinates of each of the pixels that belongs to that object.
[1909.92 → 1915.14] And that's really important in something like a robotic application because, uh, everything,
[1915.14 → 1919.84] uh, you, we said earlier, you have multiple sensors, right? So all of these sensors need to be
[1919.84 → 1926.26] triangulated and aligned so that you can, uh, make decisions from multiple sensors from the same point
[1926.26 → 1933.10] of view. So having that X and Y coordinate or that row height coordinate that exactly defines all of
[1933.10 → 1938.84] the points that make up this object is really important. So when you're, when you're considering
[1938.84 → 1945.84] mask RCNN as a as an architecture for, for your own use case, I guess when you're comparing it against
[1945.84 → 1951.72] alternative architectures, YOLO or others, is it really the use case that's dictating going there
[1951.72 → 1957.04] because your use case needs the benefits of, of the mask versus a bounding box? Is that how you
[1957.04 → 1962.18] would think about it? Definitely. So, you know, we've just talked a little bit about, uh, mask RCNN.
[1962.18 → 1968.06] It's great if you to have those masks, but you know, it comes at a little bit of a cost. It's,
[1968.06 → 1972.74] it's, uh, one thing we haven't specifically said, uh, but it is computationally expensive.
[1972.74 → 1980.10] These algorithms, they, the more you do, the longer they take. And so adding on or tacking on this extra
[1980.10 → 1985.20] functionality, these, these extra mathematical operations that have to be performed, even though
[1985.20 → 1993.06] it's being performed on a GPU, uh, highly parallelized, it still takes extra time. So it may not be
[1993.06 → 1998.28] necessary. It may not make sense that in your application, you want to spend that extra time
[1998.28 → 2004.52] generating these masks, especially if, if the bounding box is sufficient. Uh, as Daniel pointed
[2004.52 → 2010.42] out just a few minutes ago, training is more difficult. So, uh, the tedious task of generating
[2010.42 → 2016.82] all of these, uh, annotated images, you know, you have to do that as well. It's just, it's, it's a great
[2016.82 → 2022.50] algorithm when you need it, but if you don't need it, it probably doesn't make sense to implement it
[2022.50 → 2027.54] because something like a YOLO, uh, which Chris, you mentioned earlier is faster if all you need is
[2027.54 → 2033.48] bounding boxes. Yeah. It, I want to, I want to dig in a little bit to that, that idea you, that you
[2033.48 → 2039.16] brought up around efficiency. So, I mean, there's the, the training side of things, which is, is, is one
[2039.16 → 2045.92] piece of it. And, you know, I, I would imagine these, these, you know, networks being trained on, you know,
[2045.92 → 2053.20] huge GPU boxes, uh, wherever you have them or, or, or a big cluster in a distributed way. But when we get to
[2053.20 → 2059.36] talking about inference, so taking that trained model and then making inferences, so, uh, utilizing
[2059.36 → 2066.52] the model to actually detect objects, objects and masks in, in an environment, does the network size
[2066.52 → 2071.80] and the complexity also factor in on the inference side? I mean, I know we're talking about robots. So,
[2072.14 → 2077.72] um, if you're kind of shipping this model out to run on a robot, I'm assuming that that robot doesn't
[2077.72 → 2084.30] have, you know, a, a huge, uh, rack of servers on it necessarily, it might, you know, have a smaller
[2084.30 → 2090.34] amount of computation on the, on the actual robot. Has that been something that you've had to, had to
[2090.34 → 2094.88] factor in as well? Right. That's exactly right. Typically, when you're training, uh, you might be
[2094.88 → 2100.84] training in the cloud, and you can spin up however many GPUs you need for training and that reduces your
[2100.84 → 2106.68] training time. But for inference, you probably just have one GPU on your robot. And so, uh, yeah, you,
[2106.68 → 2111.68] you definitely have to consider that inference time. So if you're trying to do something in,
[2111.74 → 2116.40] you know, near real time with streaming video, um, mask RCNN is going to be a bit challenged
[2116.40 → 2123.06] because it may be only able to process two or three or 10 images, uh, depending on the size,
[2123.06 → 2128.86] uh, per, per second. So you're, you're absolutely right. And the other thing too, is oftentimes the
[2128.86 → 2135.72] GPU that you're using for training might be more powerful than the GPU on your robot. And so not only do
[2135.72 → 2140.06] you have fewer of them, you have a less powerful one. So inference becomes even longer.
[2140.64 → 2145.20] Could you just, you know, real quick, um, because we've talked about this, you know, mentioned it in,
[2145.26 → 2149.92] in, in a, uh, a bunch of times, but I think this would be the perfect context to really clarify,
[2149.92 → 2155.52] you know why in both of these cases, you've mentioned using the GPU, why in particular for
[2155.52 → 2162.34] these types of networks is a, is a GPU necessary? So good question. If you think about something like,
[2162.34 → 2172.04] uh, mask RCNN that's built on a Reset 101. So 101, uh, means it has 101 layers. And we talked before
[2172.04 → 2176.54] about these convolutions that happen. So you're looking at the this overall image. So if you have
[2176.54 → 2182.84] an image that's a thousand 24 by 1024 pixels, and you're looking at it in just one layer,
[2183.24 → 2188.40] three by three, and then spreading that over the entire image, and then looking at it again,
[2188.40 → 2195.74] maybe a nine by nine, and then, you know, 64 by 64, various size kernels. And the other thing too,
[2195.80 → 2201.18] we haven't talked about a colour image. It actually, actually has three channels deep, right? You have
[2201.18 → 2206.16] a channel for red, a channel for green, and a channel for blue. So those convolutions actually
[2206.16 → 2211.16] are doing three times the work on that first layer, because it has to look at the red, the green,
[2211.20 → 2216.98] and the blue value. So if you think about that, uh, just in one layer, and you're going to do this
[2216.98 → 2222.86] over 101 layers, you get into billions of floating point operations that have to happen.
[2223.54 → 2229.00] Cool. So let me ask you this, as we kind of start to wind up here, uh, moving in that direction,
[2229.00 → 2234.30] if you're listening to this and, and you've gotten all excited about being able to use
[2234.30 → 2242.22] mask or CNN, uh, for robotics or other uses that you might be interested in, what types of skill or
[2242.22 → 2248.52] knowledge are kind of prerequisite to get into this and to, to be able to, uh, work toward using
[2248.52 → 2254.54] it productively? How do you get started along that path? Good question. So at least for me,
[2254.54 → 2261.20] I'll talk a little bit about my experience, um, to go from say traditional data science into the deep
[2261.20 → 2266.32] learning algorithms. Um, I think one of the big, uh, skills that you have to have is coding skills,
[2266.38 → 2270.26] right? You're, you're going to be doing a lot of coding. You're going to be downloading
[2270.26 → 2276.40] other people's code, probably from GitHub. Um, you're going to be configuring it, installing it,
[2276.40 → 2281.96] and then you're going to be, uh, at minimum, you know, tuning some parameters, but very possibly,
[2281.96 → 2287.16] uh, especially if, if you're doing this in a, in a production setting where your code is going to be
[2287.16 → 2291.84] actually used for something, you'll have to make changes, code changes. So the ability to,
[2292.10 → 2297.32] to code is really important, particularly Python. Most of these algorithms are available in Python.
[2297.32 → 2302.58] I would say, and, and, and there's a lot of debate out there. I know, uh, you know, some folks say,
[2302.64 → 2307.96] oh, to, to do deep learning and data science, you really have to have a strong understanding of math
[2307.96 → 2313.84] and statistics. And, and I think if you are doing AI research, that's absolutely true. But if you are
[2313.84 → 2319.84] doing like we talked about earlier, that transfer learning, um, a lot of the math and statistics comes
[2319.84 → 2325.44] from training the initial model. So if you're using someone else's trained model as your starting
[2325.44 → 2330.52] point, the ability to do the math and statistics become less important. Um, and I know some folks
[2330.52 → 2335.48] are not going to like that, but, but that's been my experiences over the last six months, say most
[2335.48 → 2340.90] of my time has been spent coding, not so much worrying about statistics and, and, you know,
[2341.10 → 2345.58] derivatives and matrix multiplications because the software does that for you. So that's one of the
[2345.58 → 2350.52] great things about the frameworks like TensorFlow. And then again, for me to get started,
[2350.52 → 2357.26] I spent a lot of time watching YouTube videos. Uh, Stanford has a lot of great courses online.
[2357.38 → 2362.66] Their, their deep learning courses are online, and you can watch the lectures and really learn a lot
[2362.66 → 2368.30] from those. So for me, that was, that was just enormously valuable. Also, Udacity. I took a couple
[2368.30 → 2372.30] of Udacity courses. They have some free courses. They have some paid courses. Uh, those are really
[2372.30 → 2376.80] helpful. Yeah, no, I, I was just gonna, I was just gonna mention, I really appreciate you providing
[2376.80 → 2381.32] this, this perspective and being transparent. Cause, uh, I think there are a lot of people
[2381.32 → 2386.12] that get intimidated, um, kind of going into this space and thinking that, you know, they,
[2386.20 → 2391.52] they don't have a PhD in mathematics, right? So what, what difference can they make? But it is super
[2391.52 → 2396.68] encouraging, you know, for, for myself to, to hear you talk about, you know, some of the things that
[2396.68 → 2402.28] you've been involved with, and you've done, but, you know, coming at it from more of the coding
[2402.28 → 2406.96] perspective and from the transfer learning perspective and building up those skills as you
[2406.96 → 2411.76] have, I think, you know, uh, for me, it's an encouragement as, as I'm learning more things and
[2411.76 → 2416.76] I hope it is for, for the audience members as well. Yeah. And that's absolutely, uh, what I was
[2416.76 → 2420.68] hoping people would take away from my comments that, you know, if you're passionate about it,
[2420.68 → 2425.86] don't let anybody tell you, you can't do it. And it's not easy, but it's not impossible. And there
[2425.86 → 2430.52] are going to be days when you, you're looking at something, and you're looking at these crazy
[2430.52 → 2434.80] formulas, and you're going, I just don't want to deal with that today. And that's perfectly fine.
[2434.96 → 2438.18] And there are days when you look at it, and you go, you know what, I'm going to dig deeper and
[2438.18 → 2442.08] I'm going to see if I can't make sense of some of this. And over time it starts to make sense,
[2442.12 → 2446.34] especially it's repetitive. You see things over and over and over, and you start to connect the
[2446.34 → 2450.98] dots. And then, you know, just the you're the light bulb goes on one day and you, you go, Oh,
[2451.18 → 2456.30] I get, I understand batch normalization. Now I understand why we normalize things. I didn't understand
[2456.30 → 2460.48] that three months ago, but now I finally get it. And so that's, that's really for me,
[2460.52 → 2465.56] what it, what it takes to, to get, to be successful is, is that passion and enough
[2465.56 → 2470.46] of a foundation to just keep growing and growing and improving yourself and your skills.
[2471.18 → 2476.58] So as we wind down, I guess, as a kind of last thing to touch on here, I wanted to ask you,
[2476.68 → 2482.84] I know that you introduced me and the rest of our team at Honeywell to a particular GitHub repo.
[2483.08 → 2488.48] And then you talked again through that at the meetup and I wanted to bring that out, and we'll put
[2488.48 → 2492.88] it in the show notes, but for, for those of you may be listening, it's, it's on GitHub.com
[2493.52 → 2501.64] slash Matter port slash mask underscore RCNN. And, and if you would just give us a quick overview of
[2501.64 → 2507.98] the Matter port mask RCNN repo and what's possible there. And that way we can kind of leave that in
[2507.98 → 2509.94] our listeners' hands to go explore further.
[2510.06 → 2514.86] Sure. Happy to. So the mask RCNN algorithm actually came out of work that was done at Facebook,
[2514.86 → 2519.94] been several, at least that I'm aware of implementations of it. So Facebook has their
[2519.94 → 2525.68] own called, uh, Detection, which is written in, in café too. Uh, Google has an implementation
[2525.68 → 2531.26] in TensorFlow, pure TensorFlow, but the, the version, uh, Chris, that you mentioned that I really
[2531.26 → 2537.80] like, it's a combination of some Keras, some TensorFlow, and a lot of pre-processing and post-processing
[2537.80 → 2544.38] of your, your image, uh, in Python, uh, NumPy. And the thing I really like about it is they provide
[2544.38 → 2549.28] some Jupyter notebooks that they've written, which give you a good insight into what's actually
[2549.28 → 2554.04] happening with the algorithm. So it's not so much of a black box. You can, you can follow along with
[2554.04 → 2560.28] these notebooks and kind of learn your way through, uh, like the R and RCNN, where are those regions
[2560.28 → 2565.02] coming from and why are there so many and how do they figure out which ones to use and which ones
[2565.02 → 2570.88] to throw away. So the Matter port implementation is great for learning. Uh, they also have an active
[2570.88 → 2577.04] community. It's being updated. There's a lot of, uh, good information in the issue. So if you were
[2577.04 → 2583.04] to read through some of the issues that they have, uh, folks have contributed and talked about, uh,
[2583.04 → 2587.76] some improvements to the algorithm, and you can really glean a lot of information as to what's
[2587.76 → 2593.66] going on and how the NASCAR CNN algorithm works by reading those, uh, those posts, the actual structure,
[2593.66 → 2599.98] um, there are really a couple of main files. So the model. Python file kind of has the functions
[2599.98 → 2606.64] to do training and inference. There are a utilities, uh, dot by file, which has some utilities. Uh,
[2606.64 → 2612.78] the visualizations, uh, are all in the visualize dot by file. Um, there's a config file, which has
[2612.78 → 2618.02] all of your parameters. Uh, so when you're doing your training and your hyperparameter tuning,
[2618.02 → 2623.04] that's where you would go. You can go and set them there. It's, it's, it's also a class. So if you
[2623.04 → 2627.54] want to override the class, you can do that. If you're pretty familiar with, uh, classes in Python,
[2627.54 → 2631.96] Python, that's pretty easy to do. Uh, those are the main Python files. Uh, the way to get started
[2631.96 → 2638.04] in the samples' folder, there is a demo Python notebook. Uh, that's the place that I would
[2638.04 → 2643.36] start. There's also, uh, I believe in one of the samples they give you is for training shapes of
[2643.36 → 2650.58] triangles and squares and circles, uh, train shapes dot IPY notebook. That's it. That's how I would get
[2650.58 → 2655.04] started. That's how I got started. Um, read the information that they have a lot of good stuff,
[2655.04 → 2658.00] uh, and, and look at the notebooks and just get started.
[2658.28 → 2663.42] That's fantastic. Thank you so much for taking us through that and giving us that last orientation
[2663.42 → 2669.22] on the, uh, repo. Uh, I know that is, uh, I'm looking forward to, uh, to hearing back from listeners
[2669.22 → 2675.34] on what they've done with mask our CNN. Um, and so, uh, first, thank you so much for coming
[2675.34 → 2681.16] onto the show, uh, and, and giving us kind of this deep dive through mask our CNN. Uh, we really
[2681.16 → 2685.54] appreciate it. Yeah, my pleasure. It was a lot of fun. It was a little, uh, new experience for me
[2685.54 → 2689.64] doing this, uh, on a podcast without having visual. So hopefully it came across well.
[2690.18 → 2695.44] It came across great. I thought it was a fantastic tutorial. And for our listeners, uh, I hope you guys
[2695.44 → 2701.34] will, will reach out to us, uh, on social media. Uh, it's really easy to get to, uh, Daniel and me.
[2701.34 → 2707.64] We are on Twitter. We're on LinkedIn. We actually have a practical AI LinkedIn group that you can
[2707.64 → 2712.72] participate in. And then, uh, there's also, we have a community, uh, online, uh, with Slack
[2712.72 → 2718.26] at changelog.com slash community. And we're looking forward to your feedback. Uh, Chris,
[2718.36 → 2723.84] uh, is there any way that, uh, listeners can reach out to you? Uh, sure. Uh, probably the best way is
[2723.84 → 2731.12] just to find me on LinkedIn. It's Chris Rebellion, C-H-R-I-S-D-E-B-E-L-L-I-S. Uh, I think I'm the only
[2731.12 → 2736.44] Chris Rebellion out on LinkedIn, so hopefully you can find me. Well, thank you very much. And, uh, I'm looking
[2736.44 → 2740.86] after we, uh, get off the show, I'm going to dive into some NASCAR CNN and have some fun today.
[2741.18 → 2742.16] Awesome. Good luck with that.
[2744.72 → 2749.32] All right. Thank you for tuning into this episode of Practical AI. If you enjoyed this show, do us a
[2749.32 → 2754.12] favour, go on iTunes, give us a rating, go in your podcast app and favourite it. If you are on Twitter
[2754.12 → 2757.64] or a social network, share a link with a friend, whatever you got to do, share the show with a
[2757.64 → 2762.98] friend if you enjoyed it. And bandwidth for changelog is provided by Vastly. Learn more at fastly.com.
[2762.98 → 2767.48] And we catch our errors before our users do here at changelog because of Rollbar. Check them out at
[2767.48 → 2773.26] rollbar.com slash changelog. And we're hosted on Linde cloud servers. Head to linode.com slash
[2773.26 → 2778.44] changelog. Check them out. Support this show. This episode is hosted by Daniel Whiten ack and Chris
[2778.44 → 2784.52] Benson. Editing is done by Tim Smith. The music is by Break master Cylinder. And you can find more shows
[2784.52 → 2790.20] just like this at changelog.com. When you go there, pop in your email address, get our weekly email,
[2790.20 → 2795.32] keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2795.68 → 2797.42] Thanks for tuning in. We'll see you next week.
