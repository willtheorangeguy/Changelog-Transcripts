[0.00 --> 6.70]  Bandwidth for Changelog is provided by Fastly. Learn more at Fastly.com. We move fast and fix
[6.70 --> 11.42]  things here at Changelog because of Rollbar. Check them out at Rollbar.com and we're hosted
[11.42 --> 17.36]  on Linode servers. Head to linode.com slash changelog. This episode is brought to you by
[17.36 --> 23.72]  DigitalOcean. They now have CPU optimized droplets with dedicated hyper threads from best in class
[23.72 --> 29.18]  Intel CPUs for all your machine learning and batch processing needs. You can easily spin up
[29.18 --> 34.74]  their one-click machine learning and AI application image. This gives you immediate access to Python 3,
[35.20 --> 42.68]  R, Jupyter Notebook, TensorFlow, Scikit, and PyTorch. Use our special link to get a $100 credit for
[42.68 --> 51.30]  DigitalOcean and try it today for free. Head to do.co slash changelog. Once again, do.co slash changelog.
[59.18 --> 68.60]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[69.02 --> 74.52]  productive, and accessible to everyone. This is where conversations around AI, machine learning,
[74.56 --> 78.66]  and data science happen. Join the community and snag with us around various topics of the show
[78.66 --> 84.48]  at changelog.com slash community. Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[89.18 --> 95.48]  Hi there. This is Chris Benson. And welcome to another fully connected episode of Practical AI,
[95.82 --> 100.34]  where Daniel and I will keep you fully connected with everything that's happening in the AI community.
[100.70 --> 105.78]  We take some time to discuss the latest AI news, and we dig into learning resources to help you level
[105.78 --> 108.14]  up on your machine learning game. How's it going today, Daniel?
[108.60 --> 112.10]  Oh, it's going great. I'm excited about some of the news we got going on today.
[112.44 --> 117.66]  Yeah, I love the format, the way we're diving into it. For those of you who may have listened to our
[117.66 --> 122.68]  last fully connected episode, I think it was, hopefully it was as good experience for you.
[122.92 --> 127.96]  We're definitely listening to your feedback, trying to shape the show to better serve your needs.
[128.22 --> 132.12]  Yeah. And I think that there's, I mean, I've been talking to a couple people this week,
[132.16 --> 136.62]  there's just so much going on. It's good to just have a chance to, for me personally,
[136.98 --> 141.20]  just to have a chance to talk through some of these things, because there's so much going on.
[141.26 --> 146.86]  There's so many topics. There's so much jargon. To kind of try to put some of that into words is,
[146.86 --> 156.58]  I think, helpful. And we're kind of learning along with everybody listening. So keep us honest and let
[156.58 --> 159.20]  us know what we get right or wrong as we're going through this stuff.
[159.54 --> 163.14]  Yep. And if you haven't already, we hope you'll join us in our Slack community
[163.14 --> 168.98]  at changelog.com. And we have great feedback, great conversations that are happening there between the
[168.98 --> 174.94]  shows. We're also on LinkedIn, in a LinkedIn group, and we hope you'll join us on LinkedIn. You can just
[174.94 --> 180.90]  search for practical AI. Awesome. Well, this week, as I was kind of going through and looking through
[180.90 --> 187.12]  Twitter and various news sources, one of the things that, or the themes that came up when I was looking
[187.12 --> 195.26]  through things was really having to do with all the things that happen after we train our AI. So the
[195.26 --> 202.38]  question is, you know, we've trained an AI model. What next? So in your opinion, Chris, what happens next?
[202.38 --> 206.96]  What happens after you train an AI model? How, you know, what do you do? How is it useful?
[207.34 --> 211.26]  Yeah. And it's funny before I answer that, I'll just note that this is the side of things that
[211.26 --> 216.00]  we tend not to, uh, to think about too much until we get there. You know, the courses that are out
[216.00 --> 221.16]  there really focused on training and architecture and, you know, people will kind of say, okay,
[221.16 --> 224.90]  I've got it. And, but your model doesn't do any good until you deploy it into the real world.
[224.90 --> 230.46]  And it's, it's useful for your customer, for your own user. I know that as I was learning my way up
[230.46 --> 235.20]  through it, uh, through the field, this has been a bit of a challenge because, uh, the deployment
[235.20 --> 239.08]  environments and what you're targeting for deployment can be very different. And the
[239.08 --> 245.46]  standards have been slow to arrive there. That's changing now, but, um, it's definitely, uh, as I
[245.46 --> 250.82]  started out before some of the standard approaches were starting to come into being, every vendor was
[250.82 --> 255.54]  different and that was a real pain. Yeah. And for those of you that are new to some of this jargon
[255.54 --> 260.98]  to what we're talking about here, you know, you can kind of think about this AI model as a sort of
[260.98 --> 265.88]  really complicated function that's has a bunch of parameters in it. And so when we do training,
[265.88 --> 271.98]  we're using a whole lot of data through this training process to tune and tweak the, all of
[271.98 --> 276.22]  those parameters of our model. So we might have, you know, millions of these parameters that
[276.22 --> 282.54]  parameterize our AI model function to do something, you know, to, you know, transform an incoming image
[282.54 --> 287.94]  into an indication of objects in that image, for example. So the question is, you know,
[288.44 --> 293.70]  once we've gone through that process and set our parameters, now we have this function that can
[293.70 --> 298.60]  transform data. What do we do with it? So what are, what are some of the things that you've done
[298.60 --> 303.80]  after training or you've needed to do after training, or you've seen other people do after
[303.80 --> 309.78]  this kind of training process, Chris? Well, honestly, a lot of it involves, uh, cooperating with other
[309.78 --> 314.24]  teams in midsize or larger companies. If you're in a small company, it may be just yourself, but
[314.24 --> 319.88]  you've got to, a model is only useful if you are able to integrate it into some software that's going
[319.88 --> 325.60]  to go out, uh, onto your target device where you're deploying. And, um, and that's a whole different set
[325.60 --> 331.92]  of skills. Yeah. So when you say integrate it, what, what is the integration or what are you
[331.92 --> 339.66]  integrating really? So you would take a trained model and you have to put it into a software package and,
[339.66 --> 345.08]  and therefore the model has to be in a form that's usable. And by usable, it means you have a, a
[345.08 --> 350.94]  trained neural network that is able to operate on the hardware and software environment that you
[350.94 --> 355.90]  need to put it in, uh, in the end, and that it needs to be able to have access to the data that
[355.90 --> 359.92]  is going to be feeding through it for inferencing purposes so that you're actually operating. And,
[359.94 --> 365.84]  and those are, there's a lot of stuff to think about there that your traditional data scientists may
[365.84 --> 369.90]  never have had to deal with before. There's a lot of software engineering and maybe even systems
[369.90 --> 374.58]  engineering involved in trying to get it out there. And so I thought this was a great topic to go ahead
[374.58 --> 379.72]  and delve into and, uh, and talk about what those pain points are. Yeah. So I, I'm glad you kind of
[379.72 --> 384.30]  brought off the software engineering side of things. And, and, you know, if you're, if you're trying to
[384.30 --> 389.82]  code some, you know, AI stuff, whether you're a software engineer or not, you probably know that,
[389.82 --> 396.34]  you know, this idea of functions or handlers or classes are part of, uh, part of software that we
[396.34 --> 401.80]  build. And so I think, you know, in my mind, what, what, as I'm kind of translating what you're saying,
[401.88 --> 407.12]  Chris, I'm thinking about in a web server that's serving a website or something, right? We might have
[407.12 --> 412.02]  a whole bunch of functions that do something like you give it a specific request and it gives you
[412.02 --> 419.26]  content back, maybe a picture or a video or just some HTML or JSON or something. And so in,
[419.26 --> 426.12]  integrating AI into that really, we're saying that at some point in those functions or classes or
[426.12 --> 431.34]  other things that are part of the software that's running in production in our company, somewhere in
[431.34 --> 436.94]  there, we're actually accessing this model that you've mentioned. And so it has to be in some form,
[436.94 --> 442.06]  like you said, to be accessed. And most of the time that's a trained form. In other words,
[442.06 --> 448.82]  we train our model and then we save it somehow. And then we load that saved or serialized model into
[448.82 --> 453.88]  one of these functions and then just execute the data transformation that it does. Like I said,
[453.94 --> 459.54]  from image to objects or something like that. And that process of utilizing the function is,
[459.62 --> 466.32]  is called inference. So with that, I don't know, did I miss anything there, Chris, or any jargon that
[466.32 --> 471.70]  you think is relevant? No, I think another word that you might use is to simplify things is just think
[471.70 --> 476.98]  of it as you need to wrap your model up as a software component. And just as your, whatever
[476.98 --> 481.50]  your software that you're deploying may have a number of components that, that make it up,
[481.58 --> 486.10]  the models are also components. They're components wrapped in whatever language you're deploying in.
[486.26 --> 493.16]  So it may be that while you're training your model in Python, in TensorFlow or PyTorch or whatever
[493.16 --> 500.18]  you're using, it may be that you're deploying in C or C++ or Java, or I know you and I love Go as well.
[500.18 --> 504.20]  And those may, to where you're, you're, you're doing the inferencing as opposed to the training
[504.20 --> 508.06]  through that way. And that, so, and you, you think of the model as a piece of that software
[508.06 --> 513.22]  component going forward and, and it's part of deployment and you think of all the things that
[513.22 --> 515.66]  surround software engineering and deployment go into that.
[516.08 --> 522.02]  Yeah. So when you've deployed models in this way, a lot of times, how, what, what's been the
[522.02 --> 527.54]  access pattern or how have people interacted with the model? I know for me, it's been a lot of times
[527.54 --> 533.44]  integrating the model into some sort of API. We can talk about a little bit more later as related
[533.44 --> 539.10]  to some of the news, but essentially just where it's integrated into kind of like a web service
[539.10 --> 543.76]  where you would make a request for a prediction and get back a result. Have you seen other,
[543.76 --> 546.98]  other patterns? That's, that's the one I've seen most often probably.
[547.48 --> 553.22]  Yeah. It's always in, in the form using it loosely as a service. If I've seen web services used most often
[553.22 --> 559.68]  on server side where you may not be constrained by your connectivity and stuff. A lot of times though,
[559.72 --> 565.46]  if your deployment target is an IOT device or a mobile device, you still have an API, but it's really,
[565.62 --> 570.36]  it is operating as a function, you know, to use the phrase you were using earlier, that's, that's just
[570.36 --> 576.64]  the API may not be a public API that your software component is using inside your, your group of software
[576.64 --> 582.80]  components that constitute your solution. It doesn't really matter in my view, so long as that you are
[582.80 --> 587.20]  essentially following the best practices of the environment in which you're coding and what your,
[587.20 --> 591.94]  your deployment target is made up of. So. Makes sense. Yes. That brings us right into
[591.94 --> 597.64]  really some of the news that is related to this, that came up this week. First, let's,
[597.74 --> 604.04]  let's kind of focus in on this inference service or servers bit of things. One of the things that I saw
[604.04 --> 612.28]  come out this week was a announcement from NVIDIA that their Tensor RT inference server was now
[612.28 --> 618.56]  open source. So Tensor RT, I think it's been around a little bit, but this was the official announcement
[618.56 --> 627.10]  of the Tensor RT inference server officially as an open source project now. So this is, this is a project
[627.10 --> 637.14]  from NVIDIA. And part of the goal in my understanding of Tensor RT is to perform these inferences that we've
[637.14 --> 642.26]  been talking about. So post training your model, when you're actually utilizing your model is to do that
[642.28 --> 649.60]  in a very, very optimized way, maybe on certain specialized hardware, for example, on GPUs, which
[649.60 --> 657.04]  NVIDIA, of course, is concerned with. So, so it was exciting to see this actually be open sourced and
[657.04 --> 663.04]  available for the community. It seems like there's a bunch of great stuff in there. It also includes
[663.04 --> 669.18]  examples of how developers could extend Tensor RT to do things like custom pre and post processing,
[669.18 --> 676.32]  and integrate additional framework backends. So more than just TensorFlow, but like Cafe 2 and
[676.32 --> 681.32]  others via the Onyx framework that we've talked about here quite a bit, which is pretty cool.
[681.76 --> 686.22]  So yeah, I was excited to see this. I know that you've utilized GPUs probably more than,
[686.50 --> 692.04]  than I have. Chris, have you ever tried to integrate the inference side of things on GPUs?
[692.04 --> 698.08]  Uh, yeah, it's, I know it working at some of the, the employers that I've had. And for our cases,
[698.08 --> 702.48]  we always have a product or service that we're supporting. We're always deploying. And so,
[702.76 --> 708.80]  you know, one of the great things about Tensor RT was really the first one that I got into in it kind
[708.80 --> 716.38]  of at scale. And it does a number of optimizations to your model, uh, specific to deployment. So you're
[716.38 --> 721.54]  essentially taking your model and putting it through this process that Nvidia has where it,
[721.54 --> 726.60]  it optimizes it for inference and then deploys it. And, um, I'm not really surprised to see that
[726.60 --> 730.94]  Nvidia has open source their inference server because they have, uh, they've been leading the
[730.94 --> 737.32]  way in a lot of areas and, and forcing some of the other previous, um, you know, giants like Intel
[737.32 --> 741.78]  to play catch up for a while. But now we're starting to see the market stabilize a little bit and,
[741.78 --> 746.92]  and seeing more than one player out there. And so if they want to continue to be the leader,
[747.16 --> 752.50]  open sourcing their, uh, their Tensor RT technology is a, is a very sensible thing to do to make it
[752.50 --> 757.44]  accessible. So I applaud the move on their, on their part and, uh, which they had done this earlier
[757.44 --> 761.90]  when we were first learning it because it, you know, being open source now we can, we can figure
[761.90 --> 765.52]  out what our problems are on our own a little bit better, obviously by going through the source code
[765.52 --> 769.42]  and, uh, and not having to worry as much about bugs that aren't documented and that kind of thing.
[769.42 --> 771.42]  So, uh, it's, it's a great move on Nvidia's part.
[771.78 --> 777.62]  Yeah. And, um, I mean the, I guess one thing to point out here, um, and correct me if I'm wrong,
[777.62 --> 782.78]  cause I think you have more, more experience here, but it seems like Tensor RT, a lot of the
[782.78 --> 789.76]  focus is in optimization, not necessarily on the kind of setting up an API to access your,
[789.94 --> 790.68]  that's correct.
[790.68 --> 795.90]  Your model. Although I do see that, you know, they have this statement in the article about,
[796.02 --> 801.04]  you know, to help developers with their efforts, the Tensor, uh, inference server documentation
[801.04 --> 806.88]  includes various things, including, I think there is a tutorial in there that they've illustrated
[806.88 --> 812.66]  how to set up a REST API with Tensor RT. And, um, we'll link that in the, in the show notes,
[812.70 --> 817.46]  of course. But, um, I think that's definitely a helpful thing because at some points I've seen
[817.46 --> 822.78]  a bunch of, it's hard for me, at least when I see a bunch of stuff about optimization. Um,
[822.78 --> 827.00]  but then I still struggle with the integration part, like we talked about initially. So I'm glad
[827.00 --> 831.06]  to see them at least, uh, have some, some examples in that regard.
[831.64 --> 836.58]  Yeah, I think, uh, I think Tensor RT started with, with those deployment optimizations and that was
[836.58 --> 842.88]  kind of its foundation, but it's definitely provided more and more tools for developers and DevOps
[842.88 --> 846.76]  engineers to be able to get this out into the real world. And I, and I, and we're seeing a general
[846.76 --> 852.20]  push in industry to do that from these companies that are supporting, you know, with GPUs and other,
[852.20 --> 856.58]  and other technologies to get that out. So it's getting easier and easier to use these.
[856.58 --> 859.42]  And Tensor RT is, is definitely been a big part of that for NVIDIA.
[859.64 --> 867.34]  Yeah. And speaking of running inference on specialized hardware, you were mentioning to me right before
[867.34 --> 870.80]  the show about, um, something that you saw from Amazon, right?
[871.42 --> 876.94]  Yeah. Amazon is like we've seen with other providers. They have, uh, announced that they are
[876.94 --> 881.62]  launching their own, uh, machine learning chip. Uh, it's not something they're planning to sell.
[881.62 --> 887.34]  They're going to be driving some of the servers, uh, in AWS this way in the article that I was
[887.34 --> 892.68]  referencing, which was a CNBC article. They use the phrase taking on NVIDIA and Intel, but I think
[892.68 --> 898.06]  to some degree it's, it's them reducing their risk or dependency on specific vendors. I don't think
[898.06 --> 904.44]  we're going to see, you know, vendors out of, uh, AWS entirely anytime soon, but Amazon now, uh,
[904.46 --> 909.60]  not only is able to, has more tools in the tool set in terms of chips that support these,
[909.60 --> 914.40]  this type of, of work, but also it gives them leverage with those vendors, uh, in terms of
[914.40 --> 919.30]  the pricing they're going to go. So it's all good from my standpoint, uh, in the, in that I'm hoping
[919.30 --> 924.52]  that this drives prices down. It gives them a little bit of leverage and, uh, NVIDIA, Intel,
[924.62 --> 929.32]  and Amazon all end up lowering prices. Um, I hope it doesn't, uh, I hope it doesn't take another path
[929.32 --> 934.14]  from that. Yeah. Let me know if you, if you think this is a good, uh, analogy, cause I'm,
[934.14 --> 939.52]  I'm not sure that it is, but you know, Google, like all the cloud providers now pretty much have
[939.52 --> 946.42]  GPU support, right. And I think most of those are NVIDIA GPUs, but also Google has kind of developed
[946.42 --> 953.04]  this TPU architecture, right. Which is only available in Google cloud. It seems like now
[953.04 --> 960.08]  Amazon is kind of doing maybe not the same type of play, but doing some sort of, uh, specialized
[960.08 --> 967.48]  hardware that's maybe only going to be available in AWS. Um, is that, do you think kind of a similar
[967.48 --> 973.86]  play or? I do, I do. I think that, and you know, if we go back to the episode where we had NVIDIA's
[973.86 --> 981.88]  chief scientist, Bill Daly on, and he, he schooled us all in, you know, GPUs versus TPUs and ASICs and,
[981.88 --> 986.68]  and such, and, you know, all the different hardware possibilities here. Uh, he talked about kind
[986.68 --> 991.38]  of the rise of ASICs and, you know, the TP, you could think of the TPU to paraphrase him is,
[991.44 --> 996.62]  is almost a lighter version. A GPU has a whole bunch more to it other than just doing the math
[996.62 --> 1002.82]  necessary in a neural network. And so I think you're seeing these kind of very specific chips
[1002.82 --> 1008.08]  coming out, uh, with Amazon and with the, with the Google TPU and, you know, the GPUs have that
[1008.08 --> 1013.60]  same capability, but they also have a whole bunch more, but it, it seems to be that as people really
[1013.60 --> 1019.32]  focus on that specialization of doing the matrix mathematics, the matrix multiplication, it is,
[1019.58 --> 1023.62]  it's really kind of commoditizing the industry because they, instead of trying to recreate an
[1023.62 --> 1029.94]  entire GPU competitively, they're really focusing on this use case. Yeah. But it seems to me at least,
[1030.00 --> 1035.18]  um, and I, you know, I'm not a hardware expert, but it seems to me like all of these people are
[1035.18 --> 1040.48]  coming up with all of these different architectures, including, you know, Intel having the
[1040.48 --> 1046.36]  Movidius, uh, stuff and other people having specialized hardware. It seems like there's
[1046.36 --> 1052.80]  just a lot of kind of architectures to support now. And that does seem like a challenge, you know,
[1052.86 --> 1059.78]  maybe, maybe these projects like Onyx are a way to kind of mitigate that challenge. Cause now we might
[1059.78 --> 1067.30]  want to train model and we do that, let's say in PyTorch or TensorFlow, but we may want to deploy the
[1067.30 --> 1073.42]  inference on one of many different architectures. So I don't know that it seems like there needs to
[1073.42 --> 1082.56]  be a central point for standardizing our model artifacts. And I've at least had some success with
[1082.56 --> 1087.42]  Onyx in that respect. And so those aren't familiar, we've, we've mentioned Onyx on the show a few times.
[1087.42 --> 1092.68]  So it's the open neural network exchange format, which is a collaboration between a bunch of people,
[1092.68 --> 1099.02]  including, uh, Facebook and, um, Microsoft and Amazon, I think, but it's still pretty rough.
[1099.02 --> 1106.48]  So in some respects, like if you're trying to, uh, if you're trying to serialize a model from
[1106.48 --> 1110.98]  scikit learn to Onyx, for example, there's a little, a few rough edges there, at least in my
[1110.98 --> 1117.02]  respect or my history with, at least with the docs, but it is a really great ambitious project.
[1117.02 --> 1122.54]  And I certainly hope that they succeed because I definitely see a lot of problems that could arise
[1122.54 --> 1127.08]  from trying to support all of these different architectures. Um, seems hard.
[1127.76 --> 1134.46]  Yeah, I agree with you. And I think, I think Onyx was, was a fantastic first way of providing that,
[1134.58 --> 1139.86]  that commonality across these different technology platforms. And I think that there is still a lot
[1139.86 --> 1145.20]  of room, especially within the open source world of producing other tools that with, with a similar
[1145.20 --> 1150.02]  intent, just as Onyx has provided us that common format, there may be a number of deployment tools
[1150.02 --> 1157.04]  that come out where, where a deployer can focus on learning that as a, as kind of a standards-based
[1157.04 --> 1163.52]  approach rather than all the individual stuff. I know that in our prior company, uh, we were deploying
[1163.52 --> 1169.50]  to both TensorRT and, um, something that I'll, I'll bring up, which is the Snapdragon from Qualcomm.
[1169.92 --> 1175.14]  While the workflows had similarities, they work, they were completely different workflows that we
[1175.14 --> 1179.36]  had to learn. And we had people on the team that kind of specialized in either approach and stuff.
[1179.42 --> 1184.68]  It would be really great if you could target one workflow that would work across vendors in that way.
[1184.74 --> 1191.60]  Yeah. Abstract that away. So right before, uh, just a second ago, Chris, you mentioned that you had
[1191.60 --> 1198.10]  worked with this Snapdragon before, which, um, I'll let you describe here in a second. But one of the other
[1198.10 --> 1204.68]  trends that I saw kind of in the news and updates in, in the world of AI this, uh, this past week was
[1204.68 --> 1211.54]  some stuff having to do with running inference, running models in the browser on mobile, on client
[1211.54 --> 1218.64]  devices and IOT devices, this kind of idea of pushing models out of, you know, always being run
[1218.64 --> 1225.50]  in the cloud in some service in the cloud into kind of more towards the quote unquote edge or the
[1225.50 --> 1229.04]  client devices. Is this a trend that you've been seeing as well?
[1229.60 --> 1234.02]  Yeah, I think it's, it's interesting. Um, I think that you're seeing a lot of inferencing being pushed
[1234.02 --> 1239.46]  out to the edge. And I know that, uh, that has been specific use cases that I've dealt with have
[1239.46 --> 1244.98]  had to do with, um, mobile devices that were training, that were kind of leveling up and getting
[1244.98 --> 1251.80]  a Snapdragon in them that we've deployed to, uh, and also IOT. And so I think, you know, the world
[1251.80 --> 1256.88]  that we're at right now, you have lots of mobile and IOT devices that are not nearly powerful
[1256.88 --> 1260.94]  enough. I think with the recognition that inferencing is being pushed to the edge, you're seeing
[1260.94 --> 1266.30]  a number of vendors starting to, uh, to sign up with Snapdragon or similar types of technologies,
[1266.30 --> 1271.94]  basically low power inferencing engines that can be deployed to inexpensive hardware on the edge
[1271.94 --> 1277.68]  with very limited computing resource. And, and so, uh, I think you're going to see that type of thing
[1277.68 --> 1282.60]  all over the place. Um, and I think that's a given at this point where it's where your inferencing
[1282.60 --> 1287.84]  workload is distributed between the cloud and the edge as it makes sense. Uh, I think the big question
[1287.84 --> 1293.84]  now is whether or not, uh, uh, there's enough use cases of doing actually training on the edge,
[1293.84 --> 1298.32]  uh, on whether or not that, uh, becomes a thing. I don't think that's really taken hold. There's
[1298.32 --> 1303.02]  certainly lots of conversations around it, but I haven't seen it personally in industry,
[1303.06 --> 1308.26]  you know, actually being deployed in a production sense. Yeah. So in, in the cases where you're talking
[1308.26 --> 1314.88]  about when you were using the Snapdragon thing, the, the neural processing engine, the motivation
[1314.88 --> 1321.88]  for pushing that inferencing out to a mobile or, uh, sounds like in your case, an IOT device,
[1321.94 --> 1325.12]  maybe a sensor or something like that. What was the motivation for that? Was it
[1325.12 --> 1330.74]  like connectivity? Was it efficiency or timing or what, what was the primary motivation?
[1331.30 --> 1335.52]  Yeah. It really depends on the resource environment that you're deploying into
[1335.52 --> 1341.64]  and also what the performance parameters are of your, of actually operating, you know, on,
[1341.64 --> 1346.78]  on whatever. So by, by resource environment, you mean the actual resources on the device that
[1346.78 --> 1353.24]  you're deploying to or. Yeah. Well, the CPU or, or something. Yeah. And there can be a number of
[1353.24 --> 1359.54]  cases. An example that I had a personal experience in was in speech recognition and natural language
[1359.54 --> 1365.38]  processing where you may need to, uh, you don't have time or you may not have an environment equipped
[1365.38 --> 1369.86]  with the right network connections to pass to the cloud and then pass back there. There's latency
[1369.86 --> 1374.02]  involved in that. If you're in an environment where you simply don't have time for that, you know,
[1374.16 --> 1378.52]  you know, a few two tenths of a second delay or whatever it is that you're dealing with.
[1378.52 --> 1383.20]  In some cases there are speech recognition technologies where the use case requires that
[1383.20 --> 1388.60]  you start processing before you're even done necessarily speaking a sentence. So you may be
[1388.60 --> 1393.56]  already, uh, having processed the first part of this sentence I'm saying right now, before I finish
[1393.56 --> 1397.80]  this second part, it may be that the latency issues get in the way. I've seen some very specific
[1397.80 --> 1402.78]  constraints around that in industry. And there may be some situations where you can go either way,
[1402.78 --> 1407.62]  um, where you can have it be cloud-based, but I think, I think as inferencing becomes, uh, easier
[1407.62 --> 1411.46]  and cheaper on the edge, you're going to see it more and more to where instead of it being
[1411.46 --> 1415.40]  specifically a constraint, you're going to see where does it make sense to put this, you know,
[1415.40 --> 1421.70]  from a cost benefit analysis. Yeah. And thinking back to that, um, actually our way back at our episode
[1421.70 --> 1429.30]  three, where, uh, the, the team at Penn state was kind of deploying this app for African farmers that
[1429.30 --> 1434.52]  would classify plants. I'm guessing, I don't know, but I'm guessing that there's probably
[1434.52 --> 1439.16]  connectivity issues for the devices when they put them out in the field, which is literally
[1439.16 --> 1445.44]  the field, like the farming field, uh, right in this case. So I imagine that like they can't
[1445.44 --> 1452.82]  necessarily rely on inferencing cloud environment because they simply just can't connect. So I think
[1452.82 --> 1457.34]  there's like this one issue of, you know, maybe just not being able to connect and having to run
[1457.34 --> 1463.44]  that on the device. But of course there's issues with that. I remember them talking about inferencing,
[1463.44 --> 1467.94]  you know, really, if I remember right, kind of draining the battery of the device and that sort of
[1467.94 --> 1472.72]  thing. So there are, I know there are, you know, constraints here. I don't think, you know,
[1472.72 --> 1479.16]  you can totally just export everything right now to the, to these low power devices and expect things
[1479.16 --> 1484.52]  to work, work out great. But, um, there is some encouraging signs. One interesting thing that I
[1484.52 --> 1490.88]  wanted to bring up, which I've seen referenced a few times this week, one in particular, uh, I saw
[1490.88 --> 1501.12]  this release of the Onyx JS project from Microsoft, which is a project for running models and model related
[1501.12 --> 1508.28]  operations in your browser in JavaScript. Um, so there's, there's a similar project TensorFlow JS,
[1508.52 --> 1514.06]  which is specific to TensorFlow. And I'm sure that there's other JavaScript, uh, frameworks out there.
[1514.06 --> 1520.42]  I'm not, I'm not a huge JavaScript person, but in my understanding, so in addition to these things
[1520.42 --> 1526.72]  that we've talked about in terms of connectivity and all of that, there's actually a huge privacy and
[1526.72 --> 1534.68]  data element to where you run inferencing. So it could be that when you run training,
[1534.92 --> 1541.32]  you run it in a very, you know, uh, on a big beefy server in the cloud. And the reason why you do that
[1541.32 --> 1546.84]  is because you have to process a ton of data. Maybe you're processing 200 terabytes of data or something
[1546.84 --> 1553.28]  like that, but maybe that data, it doesn't include sensitive data or something. Maybe it's anonymized in
[1553.28 --> 1559.64]  some, some case, but then if you, if you transfer that model over and run it in someone's browser,
[1559.64 --> 1565.32]  and then you're running the inference in their browser, you may be processing their particular
[1565.32 --> 1571.82]  data. Like you're processing the feed off of their webcam, for example. Right. And if you're doing that,
[1572.16 --> 1576.94]  obviously that could be very sensitive data. And so one thing you could do is transfer all of that
[1576.94 --> 1581.46]  data up into the cloud, do your inferencing in the cloud, but then you're essentially, you know,
[1581.46 --> 1587.84]  taking possession of all of that sensitive data. Whereas if you run the model actually in the
[1587.84 --> 1594.78]  browser and do the inferencing there, then the user's sensitive data actually just stays on their
[1594.78 --> 1601.06]  device. So you can kind of totally, maybe not totally, but you can avoid many of these, uh, kind
[1601.06 --> 1608.38]  of privacy and security related issues in terms of how and what data you're processing where.
[1608.38 --> 1612.60]  Yeah. And, and, you know, and there's other considerations like a while back, uh, in an
[1612.60 --> 1618.56]  episode, we were talking about the general data protection regulation, GDPR, uh, in the European
[1618.56 --> 1623.78]  union, which is actually, though it's only officially applied there, many organizations are applying it
[1623.78 --> 1628.68]  globally. So they don't have to support multiple business approaches and processes. And it may very
[1628.68 --> 1633.40]  well be that by running, by doing the inferencing in your browser, for instance, instead of passing up to
[1633.40 --> 1638.38]  a cloud, you're able to, uh, fit within particular regulations in a given country where you're not
[1638.38 --> 1642.76]  actually moving the data. The model can be deployed widely, but the data has to stay where it is. And
[1642.76 --> 1647.30]  therefore that might be the only option or one of the only options that you have short of having
[1647.30 --> 1651.88]  servers in every jurisdiction that you're going to operate in. So there's, there's a strong use case
[1651.88 --> 1657.60]  going forward from a regulatory standpoint for being able to just do it right there in the end user's
[1657.60 --> 1662.26]  browser and let them keep the data private. It never moves. It takes the whole, uh, regulatory
[1662.26 --> 1667.72]  concern, at least that aspect of it out of the picture. Yeah. I think there are with everything
[1667.72 --> 1671.62]  that we've talked about before, and I guess everything related to this, there's always trade
[1671.62 --> 1678.52]  offs, right? It seems like I was talking to a friend of mine who is at a startup and part of their
[1678.52 --> 1685.62]  startup, you know, IP and, uh, really the, the secret sauce of what they're doing is in their
[1685.62 --> 1690.62]  machine learning model. Right. But then if you take that model and then you push it out to
[1690.62 --> 1695.42]  someone's client device and run it in their browser, of course, there's always the opportunity
[1695.42 --> 1700.30]  for you're releasing that model out into the wild and people can just maybe just take it and,
[1700.30 --> 1706.08]  you know, uh, look at the view source and browser and figure out how to get your model and, and utilize
[1706.08 --> 1712.22]  it and all of that. So I know that he was concerned about, about those risks, but it's probably,
[1712.22 --> 1717.04]  I don't know, in my mind, maybe the benefits outweigh the costs because in the same way,
[1717.06 --> 1721.70]  there've been a lot of papers that have shown, even for doing inferencing in the cloud, if you're
[1721.70 --> 1727.62]  exposing some service that does inferencing for like image recognition or, or, or something like
[1727.62 --> 1734.96]  that, it only takes a certain number of requests to that API to be able to kind of, uh, mock or,
[1734.96 --> 1740.74]  or spoof that machine learning model and actually create a, a duplicate of it. So I guess there'll
[1740.74 --> 1746.06]  always be those, you know, those trade-offs, but there is kind of this transfer of the model to
[1746.06 --> 1751.32]  the client's device, which is probably has some trade-offs there, but also, you know, these models
[1751.32 --> 1756.76]  aren't super small. And if you want to update them over time, maybe there are some, you know,
[1756.80 --> 1763.38]  storage or battery or other sorts of issues going on there. So I'll be interested to see,
[1763.52 --> 1769.10]  you know, how, how people deal with those trade-offs and what ends up becoming the,
[1769.10 --> 1774.66]  the driving force there. Yeah. And kind of to go back full circle, you know, that's when we talk
[1774.66 --> 1781.82]  about, uh, these deployment technologies, such as Nvidia's TensorRT or the Snapdragon neural processing
[1781.82 --> 1787.32]  engine, which is called Snappy for short, those optimizations we made, they literally will change
[1787.32 --> 1792.50]  the architecture of the model that you've trained when you're deploying. And they, and, um, there's a
[1792.50 --> 1797.34]  number of techniques that they apply to optimize that. So that's part of that deployment of models out.
[1797.34 --> 1802.62]  I think the way I see it is it's, it's great to have all these choices and options that are finally
[1802.62 --> 1808.32]  coming into, uh, into, into being, um, in, in the software engineering world, there have been, uh,
[1808.32 --> 1812.92]  over the years, uh, the evolution of software has given us many choices for client side and server
[1812.92 --> 1818.66]  side and how we're going to choose to distribute workloads and so, and fortunately we're seeing that
[1818.66 --> 1823.32]  same evolution happen fairly quickly. And so there's already, you know, there's already a roadmap
[1823.32 --> 1828.50]  on that from the software engineering world. We're seeing that being applied to, uh, data science
[1828.50 --> 1832.80]  and to AI technology specifically fairly quickly at this point, you know, we're measuring it now in,
[1832.86 --> 1838.04]  in weeks and months is instead of years or even decades, the way it took in software engineering.
[1838.04 --> 1844.34]  So I think having different ways of deploying a given thing, uh, a given model, uh, in the days
[1844.34 --> 1849.18]  ahead is going to, is going to make, allow us to best serve our customers in that way. So I think choice
[1849.18 --> 1853.78]  is good. Yeah. And choice is good. I mean, in the sense of cost too, like you've already mentioned,
[1853.78 --> 1858.70]  if there's more, more choices out there for this type of specialized hardware, you know, I know that
[1858.70 --> 1865.06]  this has been a big win for Intel's, uh, chips that are in drones and you can plug in via USB stick and
[1865.06 --> 1870.92]  stuff. It just allows people to do, you know, fun things really quickly with deep learning and also
[1870.92 --> 1877.18]  functional things that are really crucial to certain, um, certain products. And so I think that you
[1877.18 --> 1883.28]  ultimately win as a consumer, right? I I've kind of stopped. Well, part of me still wants to buy a big,
[1883.28 --> 1888.90]  you know, GPU workstation, which I probably will never do because I don't have all the money, but, uh,
[1889.04 --> 1894.16]  but the other side of me says, you know, well, at this point it doesn't matter because I can get any
[1894.16 --> 1900.26]  sort of specialized hardware for doing this stuff in the cloud. And moreover, I can, you know, go and buy
[1900.26 --> 1906.54]  one of these chips that I can integrate into my Raspberry Pi or another fun device and just build some
[1906.54 --> 1911.96]  fun projects. And when I need more compute power, then I just spin up more, more on the cloud. So
[1911.96 --> 1919.12]  yeah, I'm glad that I don't have to, you know, keep that saving going for a huge GPU machine that
[1919.12 --> 1924.66]  they'll sit in my, in my office. Although it'd probably be good for heating. Um, just through,
[1924.74 --> 1930.78]  through, uh, employers I've had, I've had the privilege of having, uh, access to DGX ones,
[1930.78 --> 1936.52]  uh, at this point DGX twos. And those are machines from Nvidia, right? Yeah. Those are
[1936.52 --> 1942.14]  supercomputers from Nvidia and, and also, uh, the workstation, which is essentially half of a DGX one,
[1942.14 --> 1946.48]  uh, at least that's what it was. The specs may have changed and they're, those are all very,
[1946.54 --> 1951.90]  very expensive, but those are for, uh, training at scale, uh, very, very complex models. And it's,
[1951.90 --> 1957.54]  it's great to see. I think right now we're seeing so many players getting into the space with ASICs and
[1957.54 --> 1963.80]  a TPUs are the equivalent and such. Uh, and, and there's now choice in hardware, uh, and, and that
[1963.80 --> 1968.54]  is really commoditizing the entire field. So I think, I think it's becoming very reasonable to get
[1968.54 --> 1972.64]  into deep learning for small projects, the way we do in software engineering, where, you know, you
[1972.64 --> 1976.72]  might, you might go to work and have a primary large scale project you're working on for your
[1976.72 --> 1980.94]  employer, but then you'd come home at night and on weekends and work on, on something that's really
[1980.94 --> 1986.50]  passion driven. And I think that is becoming more and more viable for, uh, data scientists who are
[1986.50 --> 1989.66]  really into deep learning and, and for software engineers who are getting into deep learning.
[1990.18 --> 1994.80]  So it's, uh, I think, I think we'll continue to see that. I still think we're going to have
[1994.80 --> 2000.62]  incredibly expensive AI supercomputers. Uh, you know, the DGX two is substantially more powerful
[2000.62 --> 2006.24]  and more expensive, uh, than the DGX one was we're seeing a breadth of what's available out there.
[2006.46 --> 2013.20]  Yeah. And kind of turning now from all of that news and great stuff about inference and hardware,
[2013.20 --> 2020.96]  uh, to some things that will help us as we build those, you know, passion projects or try to figure
[2020.96 --> 2027.10]  out, um, how we can do inference at our, at our new, uh, at our company or on their new project.
[2027.10 --> 2032.18]  We'll kind of turn now to the part of fully connected where we share some learning resources
[2032.18 --> 2037.36]  in particular, we're going to share some with you today as related to this topic of inference.
[2037.36 --> 2043.62]  One of the ones that I really like that I think if you're new to this whole idea of what happens
[2043.62 --> 2049.10]  after training my AI model, maybe you didn't know that there was something that happened
[2049.10 --> 2055.20]  after that. Maybe you didn't know about this whole idea of integrating models into APIs.
[2055.54 --> 2061.70]  This article, it's called rise of the model servers, which sounds very scary. Actually,
[2062.10 --> 2063.34]  sounds like a movie, doesn't it?
[2063.34 --> 2068.54]  It does. It should be made into a movie, but it's from, uh, sorry if I mispronounce the name,
[2068.62 --> 2075.06]  but Alex Vicati and it's on medium and it says rise of the model servers, new tools for deploying
[2075.06 --> 2079.66]  machine learning models to production. And I just found this to be a really good summary article
[2079.66 --> 2085.30]  in terms of first telling what a model server is, which we've kind of already discussed here,
[2085.30 --> 2090.26]  but she goes into a little bit more detail. And then she just goes through and gives you
[2090.26 --> 2096.62]  five different kind of common choices for this, which includes tensor RT, which we already discussed,
[2096.62 --> 2101.58]  but it also includes something that I've used before, which is model server for Apache MX net
[2101.58 --> 2106.76]  includes tensor flow serving clipper and deep detect. She goes through and talks about each one,
[2106.86 --> 2111.46]  but also gives you a link to the various repos and the papers that are relevant. So it's a good,
[2111.54 --> 2117.38]  it's a good jumping off point. If you're new to this whole side of how to do inference or set up
[2117.38 --> 2123.12]  inference servers. Yeah. There's a, another thing just to note is I know we've talked about, uh,
[2123.24 --> 2130.48]  tensor RT. NVIDIA has some, some great tutorials and references on their dev blogs, uh, NVIDIA,
[2130.66 --> 2136.76]  it's devblogs.nvidia.com that you can get into and learn about that. And, and since I also mentioned
[2136.76 --> 2142.74]  that Qualcomm Snapdragon and the snappy Snapdragon neural processing engine, their SDK, which you can
[2142.74 --> 2147.82]  find at developer.qualcomm.com has a lot of good material on, on how that you can jump into that.
[2147.92 --> 2152.78]  So those are two vendor specific, uh, sources that I know that I personally have used quite a lot,
[2152.78 --> 2157.92]  uh, over the last, over the last snappy. I didn't get that acronym until right now. I've never
[2157.92 --> 2165.12]  S M P E snappy. And that's a good one. I mean, it's not immediately obvious to me, but, uh,
[2165.12 --> 2170.66]  but still a good play on their part. That's a, that's a catchy one. Yep. The last thing I wanted to
[2170.66 --> 2177.72]  share was just, um, so as I mentioned, I'm a noob at JavaScript and a lot of things along with that.
[2177.72 --> 2184.04]  But if you've been, uh, kind of interested in that side of things about running AI in the browser,
[2184.40 --> 2189.58]  maybe you will just want to learn a little bit of JavaScript and want to learn a little bit of AI at
[2189.58 --> 2194.34]  the same time there. We'll put these in the show links, of course, all of these links, but if you're
[2194.34 --> 2200.14]  interested in this Onyx JS project that was just released, they have some examples, um, and demos
[2200.14 --> 2208.30]  and a demo site that's on their, uh, GitHub. And then also there's a link that we'll put there for
[2208.30 --> 2217.02]  the TensorFlow JS tutorials. So they have in these tutorials, kind of a natural progression from core
[2217.02 --> 2222.66]  concepts. So they talk about, you know, the, the specific things such as tensors and operations
[2222.66 --> 2228.12]  and models and layers and how those are represented in JavaScript all the way down to more complicated
[2228.12 --> 2239.56]  things like, you know, uh, doing, uh, synthetic data and webcam data, WebGL API layer for, for Keras, um,
[2239.86 --> 2244.86]  all of these sorts of things that, that might be a little bit more, um, little bit more advanced. So that,
[2244.96 --> 2249.28]  that will probably get you a little bit further at, at this point. So it's definitely something that I
[2249.28 --> 2255.06]  kind of want to explore a little bit. As I mentioned, I, I'm pretty new to the, that side of things.
[2255.06 --> 2260.06]  Yeah. I've done JavaScript over the years, uh, but more focused probably like mode people,
[2260.20 --> 2266.00]  most people on, uh, mostly front end development, uh, like Ember JS. And these days I use React and
[2266.00 --> 2271.12]  obviously you use Node JS for all sorts of stuff, whether you're coding or not, but, um, I haven't
[2271.12 --> 2277.40]  really delved into this applying the JavaScript skills into, uh, into the deep learning world. So I
[2277.40 --> 2282.12]  think I really need to dive into this and see what it has and understand how it can fit into other
[2282.12 --> 2287.44]  things that I've done in JavaScript. Yeah. So I, I heard a talk once and, um, I'll have to remember
[2287.44 --> 2292.10]  who it was, but I remember the statement was that, you know, no one codes in JavaScript, but everybody
[2292.10 --> 2298.22]  codes in JavaScript. I think that was the, the, the statement. So, uh, yeah. So I think that brings
[2298.22 --> 2304.70]  us to the, to the end of our fully connected episode. So for all of you, not JavaScript programmers
[2304.70 --> 2309.76]  slash JavaScript programmers out there, appreciate, uh, you're going through this, this journey and
[2309.76 --> 2313.24]  learning a little bit about inference with us. Like I say, we'll put all of these show,
[2313.38 --> 2319.86]  all of these links in our show notes and would really appreciate you finding us on, uh, changelog.com
[2319.86 --> 2325.64]  slash community connecting with us on LinkedIn and hope to hear about, uh, all of the things that
[2325.64 --> 2330.68]  you're finding interesting in the world of AI right now. And, uh, Chris, we'll talk to you later.
[2331.08 --> 2332.52]  Sounds good, Daniel. I'll talk to you later.
[2334.90 --> 2339.14]  All right. Thank you for tuning into this episode of Practical AI. If you enjoyed the show,
[2339.14 --> 2343.96]  do us a favor, go on iTunes and give us a rating, go in your podcast app and favorite it. If you are
[2343.96 --> 2347.68]  on Twitter or social network, share a link with a friend, whatever you got to do, share the show
[2347.68 --> 2352.22]  with a friend. If you enjoyed it and bandwidth for changelog is provided by Fastly. Learn more
[2352.22 --> 2356.64]  at fastly.com and we catch our errors before our users do here at changelog because of Rollbar.
[2356.90 --> 2362.06]  Check them out at rollbar.com slash changelog. And we're hosted on Linode cloud servers.
[2362.06 --> 2367.42]  Head to linode.com slash changelog. Check them out, support this show. This episode is hosted by
[2367.42 --> 2372.84]  Daniel Whitenack and Chris Benson. Editing is done by Tim Smith. The music is by Breakmaster
[2372.84 --> 2377.98]  Cylinder. And you can find more shows just like this at changelog.com. When you go there,
[2378.04 --> 2382.06]  pop in your email address, get our weekly email, keeping you up to date with the news
[2382.06 --> 2387.66]  and podcasts for developers in your inbox every single week. Thanks for tuning in. We'll see you next week.
[2387.66 --> 2387.86]  you
