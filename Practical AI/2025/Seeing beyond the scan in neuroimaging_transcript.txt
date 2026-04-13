[0.00 --> 10.06]  Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 --> 11.46]  and accessible to all.
[11.46 --> 14.48]  If you like this show, you will love The Change Log.
[14.70 --> 19.52]  It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 --> 21.38]  talk show for your weekend enjoyment.
[21.84 --> 25.82]  Find us by searching for The Change Log wherever you get your podcasts.
[26.32 --> 28.36]  Thanks to our partners at Fly.io.
[28.36 --> 31.10]  Launch your AI apps in five minutes or less.
[31.40 --> 33.40]  Learn how at Fly.io.
[44.30 --> 48.06]  Welcome to another episode of the Practical AI podcast.
[48.52 --> 50.18]  This is Daniel Whitenack.
[50.28 --> 56.12]  I'm CEO at Prediction Guard, and I'm joined as always by my co-host, Chris Benson, who
[56.12 --> 60.06]  is a Principal AI Research Engineer at Lockheed Martin.
[60.38 --> 61.04]  How are you doing, Chris?
[61.28 --> 62.54]  Hey, I'm doing very well today.
[62.62 --> 63.20]  How's it going, Daniel?
[63.38 --> 64.32]  It's going great.
[64.46 --> 72.02]  I'm excited to kind of switch it up from all of the talk of language models and agents,
[72.28 --> 76.90]  although maybe that will feature somewhere in the conversation today, but turn to something
[76.90 --> 83.02]  that's really exciting and I'm really happy that we can feature on the show, which is all
[83.02 --> 89.50]  about neuroimaging and machine learning and AI, which will be an exciting topic to learn
[89.50 --> 89.80]  about.
[89.96 --> 94.64]  Today, we have with us Gavin Winston, who is professor at Queens University.
[94.88 --> 95.40]  Welcome, Gavin.
[95.72 --> 96.20]  Good afternoon.
[96.30 --> 97.36]  Thank you for the invite, Daniel.
[97.86 --> 98.62]  Yeah, yeah.
[98.96 --> 100.98]  Well, it's great to have you with us.
[100.98 --> 109.50]  Maybe if we can kind of backtrack from even the machine learning AI side of neuroimaging,
[109.62 --> 116.20]  even just to kind of the context of neuroimaging, a lot of our audience might be in the technology
[116.20 --> 120.14]  space or software developers or business leaders.
[120.32 --> 125.62]  Could you help us understand a little bit when we're talking about neuroimaging, we're talking
[125.62 --> 127.74]  about some of the work that you're involved with?
[127.74 --> 130.66]  What does that mean exactly?
[130.94 --> 137.00]  How does it impact people's lives and kind of the healthcare system and, you know, treatments,
[137.36 --> 137.64]  et cetera?
[138.12 --> 140.12]  So neuroimaging is a pretty broad term.
[140.24 --> 142.18]  It covers a variety of different techniques.
[142.72 --> 147.62]  And essentially, the general concept of these approaches is that we're looking at the structure
[147.62 --> 149.80]  and function of the brain.
[150.20 --> 153.76]  You can look at other parts of the nervous system as well, but for my work, I'm particularly
[153.76 --> 155.00]  interested in the brain.
[155.00 --> 160.64]  And so for things like structure, you can look at perhaps is there an abnormality within
[160.64 --> 165.10]  the brain that's causing someone seizures or other types of neurological problems?
[165.88 --> 169.96]  And on the function, you can look at which parts of the brain are responsible for different
[169.96 --> 171.04]  functions that people have.
[171.06 --> 175.64]  For example, which parts of the brain are people using for language, which parts of the
[175.64 --> 178.32]  brain are people using for memory and other tasks like that?
[178.32 --> 183.50]  So I guess I'm more concentrating on MRI, but there's a whole variety of techniques, things
[183.50 --> 186.30]  like CT scans and MRI scans and PET scans.
[186.40 --> 188.04]  There's a whole series of different things.
[188.64 --> 193.36]  But essentially, they're just techniques to look into the brain from the outside and try
[193.36 --> 196.50]  and give us an idea of the structure and function and how these might be altered.
[197.22 --> 202.04]  So I guess the most common thing people would see would be MRI scans as a thing, which is what
[202.04 --> 202.84]  I mainly work on.
[202.84 --> 211.38]  And maybe also give a little bit of context for some of the, I guess, more of a historical
[211.38 --> 221.88]  context for maybe when and how machine learning or AI techniques started coming into an intersection
[221.88 --> 225.02]  with neuroimaging or MRI.
[225.38 --> 227.92]  How recent has that been?
[227.92 --> 231.96]  Is that something that's been going on for quite some time?
[232.56 --> 235.38]  And yeah, maybe just give a little bit of context there as well.
[235.74 --> 241.08]  I think maybe we can step back and think about how neuroimaging has developed over many, many
[241.08 --> 241.30]  decades.
[241.30 --> 241.78]  That'd be great.
[242.28 --> 242.44]  Yeah.
[242.56 --> 248.00]  So of course, back at the beginning, you first developed the concept of doing x-rays and we
[248.00 --> 249.40]  could do an x-ray of the skull.
[250.16 --> 253.84]  But that wasn't particularly helpful because you couldn't see the brain inside the skull.
[253.92 --> 255.30]  You could just see the skull itself.
[255.30 --> 261.88]  So then people started developing other pretty barbaric techniques where you would inject air
[261.88 --> 266.14]  or other things into the brain and then you could somehow highlight them there.
[266.52 --> 269.02]  That was pretty risky and certainly not that helpful.
[269.44 --> 275.54]  But I guess it started really coming in the 70s, 1970s, when CT scans started to become available.
[275.70 --> 281.90]  So you could then get a nice illustration of the brain or other structures from the outside.
[281.90 --> 288.76]  And then that developed further to MRI, which gives us much more detailed pictures looking
[288.76 --> 289.94]  at the brain.
[290.42 --> 293.62]  And we can get higher and higher resolution and much more detailed now.
[293.62 --> 298.72]  As these techniques have developed, of course, we've got more and more data to analyze.
[298.72 --> 303.42]  And the more and more data we have to analyze, that's when we start thinking, well, how can
[303.42 --> 307.92]  we use techniques such as machine learning to learn from this vast amount of data we're
[307.92 --> 309.78]  now starting to collect?
[309.78 --> 318.86]  So when you think about an MRI scan, you could have a resolution of 256 by 256 by 256 voxels.
[319.20 --> 321.04]  So it's a three-dimensional picture.
[321.62 --> 326.58]  But then you have multiple different types of MRI scans looking at different types of things
[326.58 --> 327.22]  within the brain.
[327.72 --> 329.34]  So you have an absolute ton of data.
[329.34 --> 335.16]  And when someone who is a radiologist, in other words, a neurologist, sorry, a physician
[335.16 --> 340.54]  specialized in assessment of scans, they have a lot of information to look at.
[340.98 --> 342.68]  And that's extremely time consuming.
[343.26 --> 345.70]  And the number of scans we're doing is going up and up.
[346.22 --> 352.18]  So now we're starting to think, well, how can we help and sort of save time and also make
[352.18 --> 356.02]  it more easy to detect the abnormalities or automate things more effectively?
[356.02 --> 361.72]  Because the vast amount of data we have now, that's not possible for us to now keep up with.
[361.98 --> 367.64]  I'm curious, with the different types of scans and with all the data that they're producing,
[367.96 --> 373.74]  and now that you have machine learning techniques available, has that changed some of the choices
[373.74 --> 377.16]  that doctors are making in terms of what's possible yet?
[377.22 --> 379.12]  Or is that still more in the future?
[379.74 --> 384.44]  How has machine learning changed the practice of medicine in these areas?
[384.44 --> 388.88]  As with many things, when you're looking at the integration of machine learning and artificial
[388.88 --> 394.96]  intelligence into medical practice, the uptake of these techniques can be fairly slow.
[396.34 --> 403.76]  There's a fairly big chasm between what's possible technically versus what is actually used in practice.
[404.46 --> 410.80]  There's obviously a lot of concerns that people have around data quality, ethics around using the data,
[410.80 --> 415.36]  the accuracy of any techniques you might be using, because of course, it's going to be used for
[415.36 --> 418.92]  humans that are undergoing different diagnoses and treatments.
[419.50 --> 425.06]  So there's a big gap between what can be done and what is actually being done in practice.
[425.82 --> 431.54]  So the uptake, I mean, there's a lot of potential there, and you always see things being developed.
[431.72 --> 437.00]  But the uptake has been a little bit slower than I would like as someone working in this field.
[437.00 --> 442.60]  But I think given what we can do now, if we think forward over what's going to happen,
[442.70 --> 445.62]  definitely these are going to become much more important over time.
[446.36 --> 452.60]  And maybe before we get into how like a machine might process some of the data that you're talking
[452.60 --> 458.52]  about, if we just consider the human, the physician or whoever it is who's looking at some of the data
[458.52 --> 462.00]  coming off of these scans, what are some of the...
[462.00 --> 467.60]  I know there's probably a whole variety of things that could be discovered in that data,
[467.70 --> 468.92]  in the imagery, right?
[469.00 --> 477.12]  But just by way of example, what might the human observer be looking for in the neuroimaging
[477.12 --> 482.74]  data that would give them a sense of, I guess it would be a diagnosis or something to investigate
[482.74 --> 486.74]  further or a potential abnormality or whatever that is?
[486.74 --> 493.18]  What are some of those things and what would they be looking for with their own human eyes?
[493.74 --> 498.14]  So when you are seeing a patient as a neurologist, you will get a description of the symptoms and
[498.14 --> 499.44]  examine the patient as well.
[499.54 --> 504.52]  And that will give you an idea of where in the brain might be involved by whatever is going
[504.52 --> 504.78]  on.
[505.30 --> 509.58]  And then depending on the symptoms and the types of symptoms, you can get some idea of what
[509.58 --> 513.28]  types of abnormality could be occurring in that part of the brain.
[513.28 --> 518.16]  But the role of the neuroimaging is really to confirm that there is an abnormality in
[518.16 --> 520.18]  that region of the brain and what it is.
[520.56 --> 523.26]  So where is it and what is the problem?
[524.02 --> 528.72]  Because you may have a list, so-called a differential diagnosis, you have a list of the possibilities
[528.72 --> 531.56]  it could be based on what you've managed to get from the patient.
[532.14 --> 536.10]  But until you actually do the scan, you don't know exactly which one it is.
[536.96 --> 542.34]  So when a radiologist who's the physician looking at the scan, they will be provided the scan
[542.34 --> 548.70]  plus the clinical information and some hypothesis that the clinician is thinking about where
[548.70 --> 550.52]  and where it might be and what it might be.
[551.04 --> 555.48]  So then they're obviously going to look closely at those areas and try and identify something
[555.48 --> 556.62]  that correlates with that.
[557.50 --> 563.78]  And for a radiologist looking at things, a lot of it is about pattern recognition and
[563.78 --> 566.30]  recognizing things that they've seen before.
[566.30 --> 572.42]  So sometimes it's very hard for a person to define what it is in the image that they
[572.42 --> 574.04]  see that tells them it's a certain thing.
[574.14 --> 578.24]  But they've seen this before and that's what it is because there's a certain pattern that
[578.24 --> 581.10]  somehow they've learned that represents that.
[581.24 --> 583.00]  I've got a quick follow-up.
[583.16 --> 590.50]  You know, as Dan asked the question and you were answering it, it occurred to me how little
[590.50 --> 593.72]  I know about the topic as a layperson, obviously.
[594.36 --> 599.04]  And you kind of started with the notion of kind of two things that there was structure
[599.04 --> 601.58]  and there was function of the brain.
[601.72 --> 607.00]  And I'm kind of curious, could you take a second kind of backing away from the data side of
[607.00 --> 611.22]  things, but just kind of going into that and talk about if you're a neurologist, what is
[611.22 --> 617.00]  the relationship between structure and function in the practice even before you get to the data?
[617.00 --> 624.50]  So like how do they relate in terms of diagnosis and your evaluation of a patient and how might
[624.50 --> 629.56]  that inform bringing data into it as Dan brought up in that last question?
[630.06 --> 636.34]  So most of the scans that are done in day-to-day life would be scans looking solely at the structure
[636.34 --> 637.04]  of the brain.
[637.70 --> 642.52]  So for example, if someone has presented with symptoms that you think represent a stroke,
[642.52 --> 647.08]  or be wanting to do a scan to work out, is there a stroke and where is the stroke?
[647.68 --> 649.44]  So you're looking at the structure of the brain.
[649.98 --> 654.84]  So pretty much all the clinical scans out there being done are scans specifically looking at
[654.84 --> 655.34]  structure.
[655.92 --> 660.64]  So there's a whole separate side of imaging when we're talking about MRI imaging, which
[660.64 --> 662.24]  is looking at the function of the brain.
[662.76 --> 666.96]  And this is used in specialist centers and in specialist situations.
[666.96 --> 674.02]  So for example, if we're contemplating doing a surgical treatment on the brain to treat
[674.02 --> 678.36]  some underlying condition, of course, we don't want to know just what the brain looks like.
[678.44 --> 681.66]  We want to know which parts of the brain are performing different functions.
[682.26 --> 688.40]  We know in general that certain tasks are localized to particular parts of the brain, but each person
[688.40 --> 692.92]  is individual and it may be slightly changed by the underlying abnormality they have.
[693.10 --> 696.28]  So there are certain scans you can do to look at the function.
[696.28 --> 703.38]  So for example, if you want to do some brain surgery near the visual pathways of the brain,
[703.86 --> 708.60]  you might want to identify where the visual pathways are by some form of functional imaging.
[709.04 --> 713.50]  Or if you're doing surgery near where language function may be, you want to know exactly where
[713.50 --> 717.26]  in the brain language function is so you can try and avoid that area if possible.
[717.76 --> 721.50]  So these are so-called functional scans when you're looking at the function of the brain.
[721.76 --> 724.92]  But that's far, far less common in day-to-day practice.
[724.92 --> 732.82]  And this may be an interesting question, but it's not often we have someone who's on the
[732.82 --> 739.08]  show that's both an expert in kind of machine learning AI type of things and neuroscience
[739.08 --> 740.62]  or neuroimaging.
[741.32 --> 745.86]  I'm wondering, from over the years, of course, we've had many people on the show.
[746.32 --> 751.92]  There have been many parallels to, you know, between neural networks and the structure of the
[751.92 --> 756.40]  brain and how these things are, you know, maybe modeled after one another.
[756.66 --> 762.40]  I'm wondering from a kind of expert in the field who's also applying machine learning and AI
[762.40 --> 773.62]  techniques, just how maybe complicated or different the brain might be than these kind of, you know,
[773.62 --> 779.38]  neural networks or deep learning systems that, yes, are very powerful.
[779.66 --> 784.74]  But, you know, at least in my understanding at their root, contain, you know, very simplistic
[784.74 --> 790.64]  components and certainly aren't as efficient as the brain in many ways.
[790.72 --> 794.54]  I don't know if you have any thoughts on that, but I figured I would take the chance because
[794.54 --> 800.06]  we don't often have this intersection of expertise on the show.
[800.58 --> 801.96]  Yes, it's a great question.
[802.28 --> 807.24]  And I think if you think about neural networks, as you mentioned, of course, they are based
[807.24 --> 810.20]  on biology and what happens in reality.
[810.42 --> 816.40]  But there's quite a big difference between what we're simulating and what the reality is.
[817.02 --> 819.62]  And a lot of it is around the scale.
[819.62 --> 824.60]  So when we do when we have neural networks, although now, of course, we can have much more
[824.60 --> 828.50]  complicated neural networks with the computational power we have now than we used to, you don't
[828.50 --> 833.50]  realize just how complicated the brain is, just how many billions of neurons it has and
[833.50 --> 836.20]  how they're all vastly interconnected.
[836.58 --> 841.38]  So that's that type of complexity has been very, very difficult to emulate.
[842.16 --> 849.60]  And even when we try and emulate the nervous system of very simple organisms that only have
[849.62 --> 854.40]  a few hundred neurons, it's very difficult to replicate that precisely.
[854.98 --> 859.04]  So how can we possibly do the same for a structure like the human brain, which has
[859.04 --> 863.22]  so many more orders of magnitude neurons and synapses there?
[863.80 --> 867.80]  But yes, it's based on based on some underlying anatomy and function within the brain.
[867.90 --> 873.20]  But there's a big gap between the level of complexity of what we simulate and what we
[873.20 --> 874.90]  actually are doing in our own brains.
[874.90 --> 880.60]  So Gavin, now that now that we have a bit of context about neuroimaging and the brain
[880.60 --> 887.24]  in in general, I'm wondering if you could give us just now kind of zooming in in a level
[887.24 --> 894.06]  down, I guess, or more focusing on the computational techniques at kind of a high level.
[894.32 --> 901.64]  How would you categorize the ways in which, you know, machine learning or AI is being applied
[901.64 --> 904.00]  to tasks related to neuroimaging?
[904.00 --> 909.12]  There are a number of different ways that we're using machine learning applied to neuroimaging,
[909.86 --> 914.22]  tackling various different parts of the patient's diagnostic and treatment journey.
[915.30 --> 922.86]  So one example would be trying to classify scans as to what, whether they contain an abnormality
[922.86 --> 923.96]  or not.
[924.56 --> 926.62]  So that's a simple classification task.
[926.76 --> 932.72]  A lot of the literature out there, they collect data on some healthy individuals without the underlying
[932.72 --> 933.72]  condition.
[933.72 --> 937.84]  Then they also collect some data on some people with a particular condition.
[937.84 --> 943.46]  And the aim of the machine learning algorithm is to try and classify whether someone has a
[943.46 --> 946.90]  particular condition or not on the basis of the imaging.
[947.52 --> 949.46]  You can publish quite a lot of papers doing that.
[949.56 --> 952.88]  But the question is, how useful is that in the real world?
[953.34 --> 958.22]  Because it's very unlikely you'll be saying, us wanting to ask it, do you have condition
[958.22 --> 961.28]  X or not, which is what essentially what the classifier is doing?
[961.96 --> 965.74]  You have a patient in front of you and you want to know what condition they have, not do
[965.74 --> 967.32]  they have condition X or not?
[967.76 --> 973.78]  So therefore, you need to go a much, much higher level than that, trying to classify amongst
[973.78 --> 975.30]  different abnormalities.
[975.30 --> 982.18]  And another way that classification could be used is not just does a person have condition
[982.18 --> 987.44]  X or not, but it may be a condition that could be in various different parts of the brain.
[987.88 --> 992.20]  So what you're trying to classify is which part of the brain is affected by this condition
[992.20 --> 995.22]  and which part of the brain is normal health tissue.
[995.76 --> 999.32]  And that's particularly something I do in my work in epilepsy.
[999.32 --> 1003.66]  So epilepsy is a condition with recurrent seizures coming from the brain.
[1004.36 --> 1008.22]  And in some cases, those seizures may be coming from a particular part of the brain.
[1008.62 --> 1012.96]  And we want to know where the abnormality in the brain is causing that's causing those seizures
[1012.96 --> 1013.80]  is located.
[1014.94 --> 1020.62]  Apart from that, what I've just mentioned about diagnosis, then another thing that's being
[1020.62 --> 1026.14]  used is how can we use imaging to help us guide what type of treatment someone should
[1026.14 --> 1029.30]  have, which is the best treatment given this scatum.
[1029.32 --> 1029.90]  Can we have?
[1030.24 --> 1034.98]  And also, can we infer some information about the prognosis of a patient?
[1035.70 --> 1039.10]  If we treat them, what is the likelihood of a particular outcome?
[1039.80 --> 1045.14]  So for example, if it's brain tumor, for example, what's the likelihood of someone recovering
[1045.14 --> 1047.72]  from that or passing away from the underlying brain tumor?
[1047.82 --> 1049.80]  Can we predict that from our imaging data?
[1050.26 --> 1055.64]  So it's used for a whole variety of things from diagnostic purposes through to treatment options
[1055.64 --> 1057.08]  and prognosis as well.
[1057.08 --> 1065.00]  So I'm curious that the use cases that you were kind of talking about applying data and
[1065.00 --> 1068.44]  machine learning techniques to were really fascinating to me.
[1068.86 --> 1076.86]  You know, and could you take as an example one or more of them and kind of talk about which
[1076.86 --> 1080.98]  ML techniques that maybe our listeners are familiar with, you know, that they've used in
[1080.98 --> 1087.10]  different in their own jobs that are unrelated and talk about, well, I take this and I apply
[1087.10 --> 1093.64]  it to classifying what part of the brain is affected, you know, by epilepsy and kind of
[1093.64 --> 1098.82]  tie in a little bit about what a practitioner that is listening might have done themselves
[1098.82 --> 1102.72]  and they might never have occurred to them to use it in this way.
[1102.80 --> 1107.24]  And just kind of, I'm trying to kind of tie the technique with the application itself a
[1107.24 --> 1107.72]  little bit.
[1107.74 --> 1111.08]  If you could kind of just take us through a couple of examples possibly on that.
[1111.08 --> 1117.12]  With the first example I gave of just trying to classify as to whether someone has a disease
[1117.12 --> 1118.12]  or not.
[1118.84 --> 1124.68]  Typically, we extract a number of different parameters from the imaging and that could
[1124.68 --> 1126.18]  be designed in many different ways.
[1126.88 --> 1128.32]  And then we have a known output.
[1128.58 --> 1132.84]  So this is, they either have the disease or not because we've decided to scan people,
[1133.24 --> 1134.58]  predefined disease or not.
[1134.58 --> 1139.68]  So this is essentially a supervised learning approach and you can just use typical techniques
[1139.68 --> 1143.12]  such as a support vector machine that you may have seen in many other approaches.
[1143.56 --> 1147.28]  This is a very common thing that is used in this type of approach.
[1147.90 --> 1153.30]  Then some more of the advanced imaging techniques when you're looking at the whole three-dimensional
[1153.30 --> 1154.44]  picture of the image.
[1154.98 --> 1159.32]  This is very well suited to techniques such as convolutional neural networks.
[1159.64 --> 1162.80]  They're extremely good at doing this type of imaging analysis.
[1162.80 --> 1168.22]  So I just mentioned two techniques, but these are probably the most common two things you
[1168.22 --> 1169.10]  will see in the literature.
[1169.40 --> 1171.98]  But there are plenty of other options as well.
[1172.92 --> 1180.44]  And with that, I'm imagining that, you know, I've seen a lot of problems in supervised learning
[1180.44 --> 1184.30]  with, you know, I get a data set and, you know, I train the model.
[1185.16 --> 1187.40]  I've seen computer vision techniques.
[1187.40 --> 1195.08]  I'm imagining there's a number of unique challenges on the technical side with what you're doing,
[1195.20 --> 1197.34]  which may be related to the data.
[1197.50 --> 1199.60]  Maybe it's related to the scale.
[1199.82 --> 1203.04]  Maybe it's related to the correlations.
[1203.18 --> 1209.06]  Maybe it's related to the complexity of the number of target classes.
[1209.06 --> 1216.20]  Yeah, maybe just help us understand kind of what are the challenging elements in any of
[1216.20 --> 1222.72]  those aspects as you apply those kind of general purpose techniques in this specific case.
[1222.88 --> 1228.04]  One of the biggest challenges is having access to the data in the first place.
[1228.92 --> 1234.68]  So when you look at techniques such as large language models that have a vast trove of data
[1234.68 --> 1239.56]  on the Internet that they can tap into, unfortunately, we don't have the same thing when we're approaching
[1239.56 --> 1240.18]  neuroimaging.
[1241.04 --> 1246.22]  So if we want to train a model for whatever task we're trying to train it for, the more
[1246.22 --> 1248.52]  data we have in general, the better we can train the model.
[1249.18 --> 1251.50]  But the question is, where do we get this data from?
[1251.56 --> 1253.30]  And that's one of the biggest challenges.
[1254.44 --> 1261.12]  So if you are running a project at a university and you're scanning subjects for a research study,
[1261.56 --> 1263.42]  you may be able to get 100 subjects.
[1263.42 --> 1268.08]  But 100 subjects to someone in machine learning, that is a minuscule number.
[1268.32 --> 1273.38]  So that is nothing like hundreds of thousands of data points that you might want.
[1274.20 --> 1276.82]  So the first thing is getting the data.
[1277.52 --> 1281.86]  And there have been approaches to try and combine data from other centers and multi-center
[1281.86 --> 1282.98]  approaches and so on.
[1283.20 --> 1285.40]  But still, we're limited by the amount of data.
[1286.12 --> 1291.74]  And of course, if you're using a supervised learning approach, the data has to be labeled as
[1291.74 --> 1291.98]  well.
[1291.98 --> 1297.28]  And depending on the nature of the label, that could be extremely laborious and time-consuming
[1297.28 --> 1300.44]  and maybe inaccurate depending on who's doing that.
[1300.86 --> 1305.66]  If we're just classifying someone as having a condition, a disease or not, that's a pretty
[1305.66 --> 1307.26]  easy classification to make.
[1307.36 --> 1309.16]  But again, mistakes could be made.
[1309.16 --> 1314.34]  But if we're doing some of the more complex things, such as trying to work out which part
[1314.34 --> 1320.32]  of the brain is affected by a particular condition, then often the way that this is done is by someone
[1320.32 --> 1321.30]  labeling the image.
[1321.40 --> 1325.94]  In other words, someone draws manually in the brain which part of the brain is affected.
[1326.12 --> 1327.96]  And that's what's used to train the algorithm.
[1327.96 --> 1333.46]  But given how I mentioned that there's so many voxels in the brain, the amount of time it takes
[1333.46 --> 1339.76]  someone manually to draw around the abnormality in the brain, that can be extremely time-consuming,
[1340.30 --> 1341.92]  several hours per subject.
[1342.42 --> 1346.32]  So if you have to do that on 100 subjects, that's a lot of manual work.
[1346.32 --> 1352.60]  So it's extremely difficult to get the data plus also the labels for the data.
[1353.18 --> 1359.56]  So that's a pretty big challenge for any clinically-based study using machine learning and AI algorithms
[1359.56 --> 1361.46]  just getting that in the first place.
[1361.88 --> 1368.30]  Given the limitations of the available data, in this field, is there any role for synthetic
[1368.30 --> 1368.80]  data?
[1369.08 --> 1373.06]  You know, in some other areas, you know, unrelated, that is acceptable.
[1373.06 --> 1375.32]  And in others, I've heard reasons why it's not.
[1376.42 --> 1382.42]  Is any level of synthetic data that you're producing to support the research, is that
[1382.42 --> 1383.06]  a possibility?
[1383.30 --> 1384.86]  Is that something that you stay away from?
[1385.02 --> 1385.64]  Just curious.
[1386.04 --> 1392.44]  Sometimes people augment their data by synthesizing slightly modified versions of the data they
[1392.44 --> 1394.32]  have and use that for training.
[1394.54 --> 1394.66]  Right.
[1394.98 --> 1397.22]  So that is something that can be done.
[1397.86 --> 1401.28]  But I don't think you can synthesize data completely from scratch.
[1401.28 --> 1404.78]  You can just modify some existing data you already have.
[1405.50 --> 1407.14]  Yes, that's certainly a possibility.
[1407.92 --> 1412.70]  And, you know, mostly you've talked about some of these approaches, you know, convolutional
[1412.70 --> 1414.62]  neural nets, support vector machines.
[1415.14 --> 1420.44]  Again, I think a lot of the questions you're asking are coming from a place of those not working
[1420.44 --> 1426.26]  in the field and questions that people might have, you know, from outside of the medical
[1426.26 --> 1432.68]  field, you know, a lot of what I've heard is that there is definitely a, you know, more
[1432.68 --> 1437.44]  of a burden for explanation of certain predictions.
[1437.64 --> 1438.16]  Right.
[1438.22 --> 1442.64]  And a sort of audit trail potentially of how decisions were made.
[1442.64 --> 1449.04]  Obviously, that's easier potentially with a, you know, machine learning model than with
[1449.04 --> 1450.82]  a deep, deep neural net.
[1450.82 --> 1455.84]  You know, what is the reality there in terms of the techniques available to you?
[1455.94 --> 1462.46]  Not so much technically, but from a practicality of how they might be applied.
[1462.64 --> 1466.56]  I guess one thing is proving something in, you know, in a paper, right?
[1466.70 --> 1471.26]  But then actual adoption of that could be challenging.
[1471.60 --> 1473.46]  So what are the realities there?
[1473.80 --> 1478.24]  Yeah, we already discussed that, unfortunately, implementation is well behind what it would ideally
[1478.24 --> 1479.18]  be at this stage.
[1479.80 --> 1484.74]  And I think one of the challenges is if you develop an algorithm and you present it to
[1484.74 --> 1490.10]  a physician and say, look, this does such and such, they want to understand how that's
[1490.10 --> 1490.46]  working.
[1490.70 --> 1492.66]  They want to be able to trust the algorithm.
[1493.04 --> 1498.50]  So if you've developed an algorithm that's meant to detect disease X, how is it making that
[1498.50 --> 1498.90]  decision?
[1499.86 --> 1501.68]  Is it doing something that makes sense to me?
[1501.68 --> 1508.02]  Because ultimately, of course, a lot of the AI algorithms could be, just appear to be like
[1508.02 --> 1508.58]  a black box.
[1508.72 --> 1511.60]  You don't, you've got your input, you've got your output, but you don't really know what
[1511.60 --> 1513.74]  went on between those two steps.
[1514.70 --> 1520.76]  And particularly for physicians less familiar with these techniques, they want to know what's
[1520.76 --> 1522.90]  happening so they can trust the algorithm.
[1523.34 --> 1527.26]  Because at the end of the day, you're going to be making a decision that can affect someone's
[1527.26 --> 1529.16]  life on the basis of this information.
[1529.16 --> 1531.76]  So you want to be sure how that works.
[1532.58 --> 1539.46]  So certainly some of the imaging analysis programs are starting to work more towards
[1539.46 --> 1542.24]  the concept of explainable AI, as you mentioned.
[1542.82 --> 1550.10]  So actually, I can mention one study here that's a study that I'm contributing data to, but it's
[1550.10 --> 1552.00]  led by my colleagues at UCL.
[1552.14 --> 1553.54]  It's the MELD study.
[1554.14 --> 1556.86]  It's a multi-centre epilepsy lesion detection study.
[1556.86 --> 1563.84]  And this is a study which is meant to help us detect where in the brain is causing epileptic
[1563.84 --> 1564.24]  seizures.
[1564.62 --> 1568.34]  And they're collecting data from many different sites across the world.
[1568.72 --> 1574.96]  And one of their key aims is to develop something that explains why the decision is being made.
[1574.96 --> 1581.20]  So the output of the algorithm is not only just this is where in the brain we think there may
[1581.20 --> 1582.10]  be an abnormality.
[1582.70 --> 1587.40]  There is also then an output that says these are the features that were different in that
[1587.40 --> 1591.52]  region of the brain that have led us to believe that that is where the abnormality is.
[1591.52 --> 1597.80]  And then when we look at that, we could potentially even ask a radiologist to go back and look at
[1597.80 --> 1602.68]  that part of the brain again and say, look, this is what we're seeing is potentially different.
[1602.80 --> 1605.18]  Are you able to now see that on the image?
[1605.92 --> 1610.48]  I'm curious before, you know, a couple of points in the conversation.
[1610.48 --> 1614.66]  You've talked about kind of the speed of adoption of the technologies.
[1614.66 --> 1618.74]  And you addressed a little bit about, you know, what some of those root causes are in
[1618.74 --> 1623.08]  terms of the desire to understand algorithms such as that on behalf of the practitioner,
[1623.20 --> 1624.10]  the medical practitioner.
[1624.80 --> 1630.32]  Culturally, you know, within the profession, what do you what kinds of mind shifts do you
[1630.32 --> 1635.02]  think are going to need to take place maybe to accelerate adoption?
[1635.02 --> 1639.14]  Or what, you know, what is that natural progression that you're seeing?
[1639.22 --> 1643.66]  Because as we're seeing these technologies flood into completely different, you know,
[1643.72 --> 1650.46]  industries across the globe and in different capacities, we're seeing these kind of kind
[1650.46 --> 1653.98]  of cultural struggles, you know, within given professions on that.
[1654.04 --> 1659.58]  And I'm really curious as you as you look at these at these doctors that are at some level
[1659.58 --> 1664.58]  adopting the technology and moving forward with it, recognizing the benefits, but also some
[1664.58 --> 1666.94]  of the challenges based on their traditional thinking.
[1667.40 --> 1670.06]  What do you think it'll take to get there for that profession?
[1670.66 --> 1674.62]  Well, the use of AI in our day to day life has now become so widespread.
[1674.88 --> 1679.86]  I think people are becoming much more acceptable of the technology as a concept.
[1680.32 --> 1684.90]  But when we're working with clinical data, one of the limitations we have is what are the
[1684.90 --> 1686.94]  ethical considerations behind that?
[1687.00 --> 1689.32]  And that's one barrier to adoption.
[1690.12 --> 1694.00]  So where is the data that we've acquired from our patient going?
[1694.00 --> 1696.98]  Is it if we're submitting it to some algorithm?
[1697.14 --> 1698.08]  Where is it being processed?
[1698.22 --> 1699.10]  Where is it being stored?
[1699.18 --> 1699.94]  Is it being kept?
[1700.12 --> 1701.78]  Is it being used for other things in the future?
[1702.34 --> 1704.90]  Is it covered by privacy law, et cetera?
[1704.98 --> 1707.08]  So there's a lot of considerations there.
[1707.50 --> 1714.18]  But if we can get something which addresses all of all of those concerns, I think now is
[1714.18 --> 1716.12]  the time in the next decade and so on.
[1716.22 --> 1721.48]  We can actually start to get these things much more widely adopted because there is that
[1721.48 --> 1724.50]  the widespread acceptance of AI now.
[1725.12 --> 1732.76]  So Gavin, I'm wondering, obviously, you've done a variety of research in this area and
[1732.76 --> 1735.60]  are aware of other things that are going on.
[1736.26 --> 1740.36]  You know, we've mostly talked about kind of the context, the background of the problem,
[1740.58 --> 1742.92]  the technology, the challenges.
[1742.92 --> 1748.98]  I'm curious a little bit about the potential impact or performance.
[1749.44 --> 1752.56]  So let's say that you're doing, you know, one of these studies.
[1752.68 --> 1753.88]  Maybe you could give an example.
[1754.72 --> 1762.72]  What is the kind of comparison between, you know, a human maybe that's doing this sort of
[1762.72 --> 1769.42]  review manually and identifying either certain diagnoses or parts of the brain?
[1769.42 --> 1773.98]  I imagine, you know, things get more complicated as the problem gets more complicated.
[1774.20 --> 1779.74]  But what's kind of the human performance level and where have people been able to push the
[1779.74 --> 1782.30]  kind of machine learning AI performance level?
[1782.44 --> 1788.48]  Now, granted, as you mentioned, there's still challenges to overcome with the adoption.
[1788.72 --> 1794.66]  But I'm curious, at least in the studies that you've done or have seen, how is that stacking
[1794.66 --> 1799.44]  up and maybe also what does it seem like these models are really good at?
[1799.86 --> 1807.56]  And then maybe what are some of the open challenges that are, you know, not addressed currently?
[1808.06 --> 1808.28]  Yeah.
[1808.38 --> 1813.78]  So the performance of humans in addressing whether there's an abnormality on the scan is very,
[1813.94 --> 1814.56]  very variable.
[1815.16 --> 1819.32]  There are a lot of studies out there that look at inter-rater performance between different
[1819.32 --> 1821.82]  people looking at the same type of data.
[1822.84 --> 1827.66]  And unfortunately, the performance and the indigreement can be quite poor in some cases.
[1828.50 --> 1835.72]  And if you look at trying to detect some subtle alteration in the brain, there are studies out there that show that the more
[1835.72 --> 1842.86]  expertise and the more highly trained the specialist is, the more likely they are to detect the abnormality.
[1842.86 --> 1848.82]  So if you have someone who's a highly specialized neuroradiologist only looking at scans of people
[1848.82 --> 1855.20]  with epilepsy, they're much more likely to detect it than any abnormality than someone who's a
[1855.20 --> 1857.50]  neuroradiologist looking at all sorts of scans.
[1858.16 --> 1862.32]  And they're, in turn, more likely to detect it than someone who's a general radiologist,
[1862.32 --> 1864.92]  not just specifically looking at neuroradiology.
[1865.62 --> 1870.62]  So there's a lot of, as with anything in life, the more highly specialized and trained you are for
[1870.62 --> 1874.74]  something, the more likely you are to detect things on a scan.
[1875.38 --> 1881.86]  Having said that, the reason we want to try and use AI sometimes is to look for things that aren't
[1881.86 --> 1884.16]  easily detectable by the human eye.
[1884.68 --> 1890.10]  There are certain things that are very hard to visually perceive, but there are patterns in the
[1890.10 --> 1893.38]  imaging data there that can be picked up by the algorithms.
[1893.38 --> 1902.56]  I think that's a very strong case for the use of AI, for things that really are not visually apparent or easy to detect.
[1903.50 --> 1909.70]  But we can use it in a lot of other aspects of our life as well, all through the whole process.
[1909.70 --> 1917.16]  So if we're putting in requests for scans, of course, there's going to be a waiting list for scans because many scans are being requested.
[1917.34 --> 1924.88]  Perhaps there's some way you can look at the information given on the patient and decide which ones are the more urgent,
[1925.42 --> 1930.56]  which ones are more likely to yield something abnormal that affects how I treat the patient.
[1931.34 --> 1937.62]  And then once you've done the scans, a radiologist will be given a list of scans to look at.
[1937.62 --> 1944.98]  But if you can pre-assess those scans with some form of algorithm that prioritizes the scans and say,
[1945.52 --> 1948.00]  these five scans appear to have an abnormality.
[1948.40 --> 1949.94]  Look at these five scans first.
[1950.20 --> 1951.42]  That's much more useful.
[1951.68 --> 1955.08]  And then you can leave the other 100 scans that are probably normal to later.
[1955.20 --> 1959.34]  You prioritize the ones that are potentially going to change someone's treatment.
[1960.50 --> 1962.30]  And then we could go on.
[1962.34 --> 1965.74]  There's just many steps in the whole process that you could integrate this into.
[1965.74 --> 1974.94]  I'm curious, as you're kind of defining how it's changed the current workflow where the automation is,
[1975.04 --> 1978.16]  the model is kind of pre-selecting scans for the radiologists.
[1978.74 --> 1984.74]  But yet, with models advancing so fast right now in terms of the capabilities,
[1985.32 --> 1992.10]  would you expect that to kind of remain the relationship between the model's capability and the human radiologist?
[1992.10 --> 1995.36]  Or do you think that that's going to evolve over time?
[1996.18 --> 1999.32]  And is that a constant evolution that you anticipate?
[1999.52 --> 2011.24]  Or do you think there's some sort of kind of human AI steady state in terms of the collaboration between the technology and the human that's going?
[2011.72 --> 2011.90]  Yeah.
[2012.00 --> 2015.92]  I guess, I mean, we're often asked, is AI going to replace the physician?
[2016.02 --> 2016.28]  Indeed.
[2016.28 --> 2018.12]  Essentially, that type of question.
[2018.30 --> 2020.96]  I personally do not think it will.
[2021.58 --> 2025.44]  But I think it's going to be a technique that facilitates and helps.
[2025.76 --> 2029.46]  In other words, it's going to augment the abilities of whichever type of physician you are.
[2029.70 --> 2033.24]  It will make your workflow more efficient, more smooth, and so on.
[2033.24 --> 2036.50]  But it's never going to completely replace the human aspect.
[2036.50 --> 2045.04]  So, for example, now, if we use any of these techniques and identify things on imaging, which we think may be relevant from the AI,
[2045.66 --> 2054.22]  we always then present it back to the team of physicians to look at the scan again and then determine whether we think that's relevant or not.
[2054.48 --> 2057.24]  It's not replacing what we do.
[2057.40 --> 2060.72]  It's giving us some information, which we then go back and review ourselves.
[2060.72 --> 2066.30]  So, for example, there's something that may have been overlooked or very hard to see in the first place.
[2066.88 --> 2069.94]  An algorithm that says possibly there's an abnormality here.
[2070.32 --> 2074.80]  You can then go back and confirm or refute whether you think that's the case or not.
[2075.34 --> 2081.16]  So it's essentially, I think it's going to remain this type of thing, augmentation of what you do, but not a replacement.
[2081.16 --> 2088.98]  So if I could just follow up for a two-second thing on that, and I'm not disagreeing with you, but I am curious because people will say,
[2089.12 --> 2091.34]  oh, I think the human will stay in the loop and stuff in that.
[2091.92 --> 2095.90]  But what is in the way that you're looking at it?
[2096.04 --> 2098.00]  Why do you think the human will stay in the loop?
[2098.10 --> 2101.66]  And I'm not arguing against that or saying that's a bad thing at all.
[2101.66 --> 2109.52]  But I've gotten that when I tell people that I think a human will stay in various workflows in other industries and stuff.
[2109.66 --> 2111.76]  That's a common question is they go, well, why?
[2112.02 --> 2118.86]  Based on what you're telling me, you know, with the model increasing, I'm kind of curious what your kind of foundational belief is there.
[2119.34 --> 2123.04]  Well, however good algorithms are, they do make mistakes.
[2123.04 --> 2132.90]  And one of the big issues in the type of algorithm I'm talking about, which is trying to detect where an abnormality in the brain is that causes seizures, is a lot of false positives.
[2133.88 --> 2140.80]  So the technique looks good on the basis of that we are identifying where the abnormality is.
[2141.44 --> 2148.18]  But it doesn't address the fact that maybe three or four other brain regions that were also identified that were not involved at all.
[2148.18 --> 2150.30]  So you're getting a lot of false positives.
[2150.30 --> 2155.50]  So the performance of the algorithms is good, but it's far from perfect.
[2156.04 --> 2162.60]  So I think that's a key reason why you're always going to need some human oversight and looking into that.
[2163.18 --> 2168.38]  And of course, then there's a whole separate issue of what is the legal responsibility?
[2169.38 --> 2179.64]  If an algorithm says X and you make a decision based on that and it turns out what it said was wrong, whose responsibility is that?
[2179.64 --> 2182.24]  Is it the person who used the algorithm?
[2182.54 --> 2183.90]  Is it the person who wrote the algorithm?
[2184.76 --> 2185.50]  Is it the physician?
[2185.84 --> 2186.76]  Which physician is it?
[2186.86 --> 2188.22]  It's a difficult decision.
[2188.36 --> 2192.88]  So I think there's always going to have to be some form of human oversight in the process.
[2192.88 --> 2215.98]  And how on that front, on the legal side, are jurisdictions or governing bodies or whatever the relevant kind of association would be, are those bodies keeping up with this sort of work and kind of ahead and putting the sort of legal frameworks in place?
[2215.98 --> 2220.54]  Are they, you know, catching up a combination of the two?
[2221.14 --> 2226.60]  You know, what guidance is coming down and how does that legal situation look as of today?
[2227.14 --> 2231.38]  That's not something I've looked into a lot because each country has its own different rules.
[2231.38 --> 2240.02]  But in general, unfortunately, the legal system lags a lot behind the technological innovations that are being occurring in the world.
[2240.82 --> 2248.86]  So there's definitely a lot of scope to working out all of these legal issues and how they best dealt with.
[2248.86 --> 2269.50]  Yeah. And I know, you know, speaking of things changing in the world, obviously, we've seen a huge shift and perception shift and, you know, shift in technology and AI, you know, over the last couple of years with gen AI and language models and vision models and all sorts of things.
[2269.50 --> 2286.04]  You know, I imagine that there is discussion in the research community around how these types of generative technologies might play a role in maybe it's the decision support around this type of work or other things.
[2286.04 --> 2306.54]  Is there any perspective you have there or have you crossed paths with folks that are, you know, considering those sorts of techniques in addition to kind of the machine learning, you know, traditional machine learning models or kind of CNNs or deep learning type of type of models?
[2306.94 --> 2312.70]  What's the kind of status there in terms of reception or integration of this latest wave of technology?
[2312.70 --> 2319.14]  That's not an area I work in much myself as I mainly concentrate on the image analysis side of things.
[2319.74 --> 2326.70]  But I think that goes back to what I mentioned earlier about the potential triage opportunities of these type of approaches.
[2326.70 --> 2335.00]  So given this textual information on why we're doing a scan plus access to someone's medical records, what are the likely possibilities?
[2335.58 --> 2338.20]  What's the probability of these things actually being the case?
[2338.40 --> 2341.70]  Which is the most urgent scan that we should be doing next?
[2341.70 --> 2343.18]  I think I see it.
[2343.44 --> 2347.20]  I see it that area is when it's going to be the most useful.
[2347.90 --> 2351.48]  As you were looking at this, you know, it's I find it really fascinating.
[2351.96 --> 2361.22]  I'm of an age where I'm in my mid 50s and and having lots of medical procedures and seeing the advancement of technology pretty rapidly.
[2361.22 --> 2370.98]  As you look at this area that you focused on so much, where do you envision the technology taking the profession and the tools of the profession?
[2370.98 --> 2382.40]  And how do you think that will will go forward in terms of as as we have ever more AI capabilities and algorithmic capabilities and more data available?
[2382.78 --> 2387.88]  What does the what does the future of imaging look like to you and where do you think it might go?
[2387.88 --> 2396.16]  And are there any particular things that you would like to see happen as you've as you've thought about your work and where it's going and, you know, the rate of adoption?
[2396.16 --> 2398.66]  And I'm just curious what that future is.
[2399.20 --> 2399.60]  Yeah.
[2399.76 --> 2412.74]  What I would like to see is as a radiologist sits down to report 20 scans they've got instead of scan one to 20, it's scan most likely to be abnormal to least likely to be abnormal.
[2412.74 --> 2415.56]  So you've already got your list of the order you should be looking at them.
[2416.20 --> 2425.52]  And when you open the scan, rather than just seeing the scan itself, just just the scan, the there's an algorithm been run on it already.
[2426.04 --> 2428.42]  A form, the type of analysis you're interested in.
[2428.54 --> 2436.30]  And that's generated a report, some recommendations and ideas, which has already been fed back into the radiology system.
[2436.30 --> 2443.54]  So when you open it, it's not just the scan, it's the scan plus sort of computer generated recommendations report.
[2443.76 --> 2446.54]  So you already have that information ahead of you.
[2446.58 --> 2455.72]  So you can then focus on those areas and then potentially detect things that may have been overlooked before or get things more quickly.
[2455.72 --> 2465.80]  And then once the report has been done, then you need some way that that's going to be fed back to the treating physician in a useful manner.
[2466.18 --> 2477.48]  At the moment, what happens is the radiologist writes a report and that is sent electronically or sadly, in some cases, by paper to the referring physician to look at when they get around to looking at it.
[2477.48 --> 2486.50]  But maybe there's some AI that can be put in at that stage, which can generate a recommendation or prioritization of those information, those results.
[2486.70 --> 2495.34]  So that the physician actually requested the scan in the first place is alerted sooner when there's a significant abnormality that needs to be addressed.
[2495.88 --> 2496.52]  Sounds good to me.
[2497.04 --> 2497.62]  Yeah, definitely.
[2497.78 --> 2501.50]  I think that's a great picture to paint as we as we close up here.
[2501.62 --> 2505.36]  Gavin, it's been a great experience having you on the show.
[2505.36 --> 2514.46]  So I encourage people in the show notes, we'll include a couple links to where you can find some of Gavin's papers and presentations.
[2514.92 --> 2516.24]  I encourage you to check it out.
[2516.68 --> 2521.14]  Really appreciate the work that you're doing, Gavin, and appreciate you taking time to chat with us.
[2521.18 --> 2521.72]  It's been great.
[2522.12 --> 2522.48]  Okay, great.
[2522.56 --> 2523.16]  Thank you very much.
[2530.44 --> 2531.30]  All right.
[2531.60 --> 2533.40]  That is our show for this week.
[2533.40 --> 2539.70]  If you haven't checked out our ChangeLog newsletter, head to changelog.com slash news.
[2540.08 --> 2542.18]  There you'll find 29 reasons.
[2542.40 --> 2545.76]  Yes, 29 reasons why you should subscribe.
[2546.24 --> 2547.62]  I'll tell you reason number 17.
[2548.26 --> 2550.96]  You might actually start looking forward to Mondays.
[2551.22 --> 2553.82]  Sounds like somebody's got a case of the Mondays.
[2554.22 --> 2558.66]  28 more reasons are waiting for you at changelog.com slash news.
[2558.66 --> 2564.68]  Thanks again to our partners at Fly.io to Breakmaster Cylinder for the Beats and to you for listening.
[2565.10 --> 2567.74]  That is all for now, but we'll talk to you again next time.
[2567.74 --> 2575.06]  Game
[2575.06 --> 2576.32]  Game
[2576.32 --> 2577.32]  Gott...
