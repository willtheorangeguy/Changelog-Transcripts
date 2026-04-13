[0.00 → 7.06] big thanks to our partners Linde quickly and launch darkly we love leno they keep it fast
[7.06 → 12.50] and simple check them out at linode.com slash changelog our bandwidth is provided by fast
[12.50 → 17.40] learn more at fastly.com and get your feature flags powered by launch darkly get a demo at
[17.40 → 24.98] launchdarkly.com this episode is brought to you by our friends at o'Reilly many of you know o'Reilly
[24.98 → 29.48] for their animal tech books and their conferences, but you may not know they have an online learning
[29.48 → 35.16] platform as well the platform has all their books all their videos and all their conference talks
[35.16 → 39.72] plus you can learn by doing with live online training courses and virtual conferences
[39.72 → 45.64] certification practice exams and interactive sandboxes and scenarios to practice coding alongside
[45.64 → 51.50] what you're learning they cover a ton of technology topics machine learning AI programming languages
[51.50 → 58.80] DevOps data science cloud containers security and even soft skills like business management
[58.80 → 64.18] and presentation skills you name if it is all in there if you need to keep your team or yourself
[64.18 → 68.70] up to speed on their tech skills then check out o'Reilly's online learning platform learn more and
[68.70 → 74.16] keep your team skills sharp at o'reilly.com slash changelog again o'reilly.com slash changelog
[74.16 → 87.90] what's up this is Adam stachowiak editor-in-chief here at changelog, and you are listening to
[87.90 → 93.66] practically i am weekly podcast that makes artificial intelligence practical productive and accessible to
[93.66 → 100.14] everyone this is where conversations around AI machine learning and data science happen and today
[100.14 → 106.80] we have a special episode a crossover episode from the changelog podcast for you on a recent episode
[106.80 → 112.60] Daniel whiten ack joined jarred Santa talking with José valid elixir creator about numerical elixir
[112.60 → 117.88] this is José's newest project that's bringing elixir into the world of machine learning they discuss
[117.88 → 123.98] why José chose this as his next direction the team's layered approach influences and collaborators
[123.98 → 128.46] on this effort and their awesome collaborative notebook that's built on phoenix lab view
[128.46 → 141.32] all right I'm joined by José valid creator of elixir and frequent guest on the changelog I think
[141.32 → 145.62] this is your fourth time on the show welcome back thank you thanks for having me again excited to have
[145.62 → 149.38] you lots of interesting stuff going on in your neck of the woods and I'm also joined by hey that's
[149.38 → 156.38] not Adam that is practical AI co-host Daniel whiten ack what's up practical all yeah yeah
[156.38 → 163.36] practical AI sometimes it looks like with the font on zoom it looks like practical all yes so when we
[163.36 → 169.78] record on our podcast uh normally I'm known as practical all well welcome to the show I'd have a
[169.78 → 174.88] tool time reference you know you'd be my all bundy for the show, but that would be too old for most
[174.88 → 179.20] people to get that one yeah and I'll just say you can be my Adam I'll be your Chris Benson, and we'll uh
[179.20 → 183.62] co-host this sucker how about that that sounds wonderful I'm excited to be here well I had to
[183.62 → 188.36] call in the big guns because I know very little about this space in fact almost everything I know
[188.36 → 194.80] about the world of artificial intelligence I learned from producing practical AI and by listening to
[194.80 → 200.46] practical all do his thing each and every week so that's why Daniel is here I do know a thing or two
[200.46 → 206.90] about elixir but nowhere near as much as José and here we're at the intersection of those two worlds
[206.90 → 216.16] so kind of exciting time, and we're here first to talk about no so José what is this no thing here
[216.16 → 224.30] here tell us about all right so no stands for numerical elixir and back in November last year
[224.30 → 230.46] we started working on this I can tell more about the story later, but the important thing is that in
[230.46 → 239.00] February we finally unveiled no which is a library but also this idea of a collection of libraries
[239.00 → 247.48] of to improve elixir so we can start doing machine learning data science numerical computing and so on
[247.48 → 255.26] so I'll just give an overview of what we have out so far, so everybody's on the same page and then
[255.26 → 262.56] we expand on that so we started with no which is uh it's a library itself is the idea in the library
[262.56 → 271.36] itself and the main abstraction in no as you would expect is multidimensional tensors so you can do
[271.36 → 278.44] um when I announced no one of the things that I did was that I gave a talk and in this talk I built
[278.44 → 285.24] a moist classifier new network classifier for the moist data set from scratch just using no
[285.24 → 291.44] and so you know you can work with multidimensional arrays tensors and for those who are not familiar
[291.44 → 296.90] why multidimensional arrays and tensors one a simple example I like to give is like for example
[296.90 → 301.86] if you take an image if you need to represent that image if you need a data structure to represent that
[301.86 → 306.30] image you can represent that with tensor, and it's going to be a three-dimensional tensor
[306.30 → 310.70] was where one of the dimensions is going to be the height the other is going to be the width
[310.70 → 318.06] and then the third dimension is for the channels like RGB and so on so, and then you know if you can
[318.06 → 323.16] represent the data like this you're going to send this tensor for data networks and through
[323.16 → 329.42] neural networks and at the end it's going to tell hey is this a dog or a cat or more complex things
[329.42 → 335.40] so that's where we started that was the first building block that we built and one of the things
[335.40 → 341.82] that people ask a lot is that you know like elixir is a functional programming language and functional
[341.82 → 347.24] programming language they promote a lot of immutability they promote immutability a lot which
[347.24 → 353.24] means like if you have a multidimensional tensor like you know if you have a 50 megabytes image and
[353.24 → 358.92] you need to do something with it, you need to transform this image each transformation that you do is going to
[358.92 → 366.58] copy the whole image in memory you know and do a new copy so you are locating like 15 megabytes every
[366.58 → 372.68] step along the way so to solve this what we did and this is an idea that we've seen elsewhere for
[372.68 → 377.56] example in the python community we have jacks so a lot of the inspirations in the next come from jacks
[377.56 → 382.20] so the way we solve this in access that we have this thing called numerical definitions
[382.20 → 391.62] and what numerical definitions are is that they are a subset of elixir that can compile and is
[391.62 → 398.10] guaranteed to run on the GPU and that's how we can have you know numerical computing elixir machine
[398.10 → 403.02] learning and neural networks because we can effectively look at your elixir code and say hey I'm going to get
[403.02 → 408.60] all of this compile it to run the GPU, and it's going to be really, really fast, so those are the two
[408.60 → 413.08] building blocks we can come back to this and talk about a lot about those things later and then we
[413.08 → 421.78] release two bindings for an x, so one is the xla is a binding for the Google LA which stands
[421.78 → 427.64] for accelerated linear algebra so if you're using TensorFlow what is running the things in TensorFlow
[427.64 → 433.74] is googled LA so they're using google LA to compile it to run on the GPU to run the CPU as efficiently
[433.74 → 441.64] as possible so we have bindings for that we are also now working on bindings for PyTorch to be more
[441.64 → 447.74] precise lib torch so PyTorch for Facebook they have the lib torch which is the c library we are wrapping
[447.74 → 454.08] that as well and two months later so that was in February we released two other libraries, so one is
[454.08 → 459.24] axon so we started with the building block which was tensors multidimensional arrays numerical
[459.24 → 465.66] definition so we released axon which is a high level library for building neural networks and we
[465.66 → 472.12] just announced live book two which is interactive and collaborative code notebooks for elixir so that's
[472.12 → 477.80] kind of what we have released in the last two months, and it's just the beginning there's still a lot of
[477.80 → 483.76] things we want to do, but we are really starting on working on this ecosystem and build it up so José
[483.76 → 490.52] I'm curious from the AI perspective and i I'm going to have to admit for listeners that I know almost
[490.52 → 495.68] nothing about elixir except what I've learned on the changelog podcast from you in previous episodes
[495.68 → 503.96] so I'm curious like from the community standpoint what was really driving your motivation to spend so
[503.96 → 508.84] much time on these things and I see like, and we can dig into the individual components but like you're
[508.84 → 512.94] saying that like the main components that I think could make this very functional it sounds like are
[512.94 → 519.14] there and are being built but from the community standpoint were people requesting this were people
[519.14 → 525.26] trying to sort of roll their own sort of neural network stuff in elixir from your perspective what
[525.26 → 530.42] sort of led up to that side of things okay that's a great question and to give some context so
[530.42 → 535.82] one of the things like going way, way back it always started because of like the Ealing virtual
[535.82 → 540.74] machine the only reason that elixir as a programming language exists because of the Ealing virtual
[540.74 → 546.14] machine and the Ealing virtual machine was built by Ericsson which is a telecommunication company for
[546.14 → 553.20] building like concurrent distributed and fault-tolerant software I'm not going to expand on that
[553.20 → 559.22] like you can check elixir on the website but all these like stings for my love for the Ealing virtual
[559.22 → 565.10] machine so when I created elixir I was like I want to have as many people as possible building on this
[565.10 → 569.44] platform because I love it and I think other people they are really going to love it and enjoy it too
[569.44 → 575.62] so I've created elixir and I've always thought I think like in terms of like programming languages
[575.62 → 582.84] I really think like that python is a really stellar example of like tackling a bunch of different
[582.84 → 588.70] problems so I always had in mind that you know I want that for elixir and for their learning
[588.70 → 593.92] virtual machine for their learning ecosystem I think we can grow diverse to solve all the different
[593.92 → 599.80] kinds of problems so I come from a web background I was a member of the rails' car team almost like
[599.80 → 607.28] a life ago when I started with elixir I had this like obvious web background and that was one of the
[607.28 → 614.00] first like let's say dimension that elixir took off with the phoenix web framework, so people started
[614.00 → 620.24] using elixir more and more for the web elixir was already a good natural fit for building distributed
[620.24 → 626.34] systems or anything regarding the network due to the airline heritage, but it was like I always want
[626.34 → 633.72] to try to expand this and the first time I expanded this was back in 2016 we released abstractions for
[633.72 → 639.20] like data pipelines and data ingestion so if you need to consume like queues, and you need to do that
[639.20 → 645.78] very efficiently we released libraries for that and that brought elixir to a new domain which was like
[645.78 → 649.60] data processing and there are like some very nice use cases on our website so for example how
[649.60 → 656.60] change.org for example is using data abstractions that we wrote back then to process you know like
[656.60 → 661.46] because when somebody if you have a petition that one million people signed you need to send them an
[661.46 → 665.44] update now you have to email a million people how are you going to do that so we start that
[665.44 → 670.92] segment and then the community start to grow, so people start bringing elixir in the early virtual
[670.92 → 675.76] machine for embedded, so there is the nurse framework people started bringing that
[675.78 → 681.10] to auto video streaming and then there's always the question like you know why not numerical
[681.10 → 686.40] computing why not machine learning so I always had this interest like you know I feel like it's part
[686.40 → 691.72] of my responsibility part of my job to try to broaden the domains and the areas of the language
[691.72 → 697.46] the community is also doing that a lot for a bunch of areas, but you know if there's something where I feel
[697.46 → 703.74] like hey this is a good opportunity we can do it then why not then let's do it and this always started
[703.74 → 709.90] just to finish giving more context when prey prog I always had this interest actually like
[709.90 → 716.98] my thesis my master thesis was in test classification and by using test classification, but that was like
[716.98 → 722.42] 11 years ago so you know like that was deep learning we're not talking about deep learning at the time yet
[722.42 → 728.26] I think everything was still support vector machines or kind of state of the art but I never fall back
[728.26 → 735.50] but I always had this interest so in October last year prey prog announced a book which is genetic
[735.50 → 740.96] algorithms for elixir and then I was like hey apparently there's somebody who knows things about
[740.96 → 747.14] AI and machine learning in the elixir community, and he's shown show morality I emailed him and I was
[747.14 → 752.64] like hey I think the platform could be good for us to do everything in machine learning he said like I agree
[752.64 → 758.42] let's work on it, and we started working on it so it was basically you know like it's kind of like you
[758.42 → 764.84] know why not if we can make it happen let's make it happen and uh we will try to figure out how we are
[764.84 → 770.90] going to you know let's build this and then later we will continue working on how to package and how to
[770.90 → 775.64] sell this to people and say like hey what are the benefits of having those two words like joining
[775.64 → 781.60] together and working together so if we stay big picture, but we do a bit of a comparison trying to
[781.60 → 788.92] understand exactly your aim here if I was a happy NumPy slash PyTorch like that you know python
[788.92 → 796.46] data scientist kind of person are you hoping that maybe someday the no based and elixir based tooling
[796.46 → 803.80] would draw me over to elixir are there aspects of it that it is going to be well positioned better than
[803.80 → 809.90] python or are you more just saying well let's bring this area of computing to existing elixirs and
[809.90 → 815.88] hope to you know give them more tools or are you also thinking from the other direction honestly i
[815.88 → 823.90] never tried to look at it that much ahead so for me like my goal right now is that for example if
[823.90 → 829.46] imagine that you are building an application elixir, and then you need to resort to do something with
[829.46 → 834.38] machine learning or data science or like oh I need to go to python to solve this problem right if we have
[834.38 → 840.46] a tooling so you don't have to go there and can stay within the community I would already consider
[840.46 → 846.98] that a tremendous victory just because that was not an option in the past so if people they're starting
[846.98 → 853.72] to make this choice I would already be very, very happy and I would be like you know like mission
[853.72 → 860.38] accomplished gotcha, and then we'll see babe steps Daniel what tools do you use in your day-to-day work
[860.38 → 869.58] yeah I like the framing of how you just framed it José because actually my tool set my team's tool set
[869.58 → 877.82] we develop models in python using TensorFlow and PyTorch but typically in terms of the products that
[877.82 → 884.72] we're building, or you know what we're developing we're developing either API servers or you know
[884.72 → 891.50] something for the most part we're doing that in go so a lot of times what happens is exactly what
[891.50 → 898.70] you were saying so we're happy writing our API handlers and in go and everything's nice and
[898.70 → 906.44] wonderful, and then we basically just have to call into python to do an inference potentially now there's
[906.44 → 911.10] new stuff coming onto the scene in the go community as well to try to support that same
[911.10 → 916.66] sort of workflow where like I would love to not do that like if I was working in go and i and I didn't
[916.66 → 921.90] have to call into python that would be super cool and I think that's still developing so I totally get
[921.90 → 929.02] what you're saying like if you're working in elixir then it would be great for those developers to not
[929.02 → 935.60] have to do this sort of awkward call into python for inferencing it's awkward and always managing that
[935.60 → 941.44] and monitoring it and all that is sort of dicey also though I think that there is this sense
[941.44 → 951.02] in the python community or well I'll say the AI community that pythons sort of consume this whole
[951.02 → 959.06] world but I don't think necessarily out of like a particularly one good reason why it should consume
[959.06 → 964.54] that whole world because it's kind of like all these scientists or like grad students working on
[964.54 → 970.22] computational science and working on AI they're like well all our stuff that our advisor wrote is
[970.22 → 975.24] in FORTRAN I don't want to like write FORTRAN so I'm going to write this python stuff that wraps around
[975.24 → 981.44] my FORTRAN and then like people just start writing python a lot because it's like pretty easy to get
[981.44 → 986.16] into and they so they do all their scripting in that and eventually like the science world just sort of
[986.16 → 990.28] started latching into python and building things there I don't think it's necessarily like
[990.28 → 998.12] the best tools for AI will be built using python actually I think like a lot of my frustrations in
[998.12 → 1004.34] life are because of you know working in python and I'm not trying to bash that because it's its also
[1004.34 → 1008.68] great like you're saying I think there is an opportunity for both sides of things I guess is
[1008.68 → 1014.28] what I'm getting at that's interesting to hear that José one of the things that you did with elixir
[1014.28 → 1017.72] which I appreciated I think a lot of people appreciate it because you got a lot of people
[1017.72 → 1023.02] loving and using the language right as you took all these things that influenced you and that you
[1023.02 → 1028.44] appreciated, and you brought them together with the beam you know your love for Erlang was the
[1028.44 → 1033.28] reasoning right, but then you went to your language design, and you designed the language, and you pulled
[1033.28 → 1040.54] in ideas from ruby and ideas from pearl and ideas from functional languages I'm not sure which ones but
[1040.54 → 1045.78] you've told this story before, and you can probably reiterate all your influences and you kind of made this
[1045.78 → 1050.66] what I think is a really beautiful language out of it, but it was based on your history your knowledge
[1050.66 → 1057.22] your taste what you liked here you are doing numerical stuff right, and you're doing data
[1057.22 → 1062.02] science stuff and I just wonder like how do you acquire that taste how do you acquire that knowledge
[1062.02 → 1067.04] do you just know every domain very, very well or how do you learn this stuff I know you said in your
[1067.04 → 1071.66] back in school you were doing some of the stuff there are statistical things but how have you come up to
[1071.66 → 1078.70] speed on what would be an awesome way to do numerical elixir yeah so this time it has really been
[1078.70 → 1085.56] Sean and jackal so all the part of like deep learning and how things should work Sean he really the one
[1085.56 → 1093.36] leading it but like the main seed that led to this was actually jackal cooper so when I started talking
[1093.36 → 1099.12] with Sean by email before we started working together I sent a tweet I don't remember what it was
[1099.12 → 1105.42] asking about like some references, and then he pointed me to the jacks' library in python which a
[1105.42 → 1110.54] lot of people are taking it like to be the next big library potentially replace TensorFlow that's what
[1110.54 → 1115.18] some people speculate right, but it's from Google there's a lot of traction behind it and then I was
[1115.18 → 1120.74] reading the docs for jacks so we were saying you know like hey you know like elixir is a functional
[1120.74 → 1125.48] programming language and as a functional programming language everything is immutable so work with
[1125.48 → 1130.94] multidimensional data would actually be very expensive but then I'm reading the docs for
[1130.94 → 1137.88] jacks which is a python library, and then they have quotes like jack is intended to be used with a
[1137.88 → 1144.50] functional style of programming, and then they say unlike NumPy arrays jacks arrays are always immutable
[1144.50 → 1150.74] and then I was like what is happening here so it was like this reference like hey it's functional right
[1150.74 → 1156.06] like so that's like my spider senses they were like tingling like okay wait wait so there
[1156.06 → 1161.36] is something here that's when Sean and I like we jump with both feet, and they're like okay there's
[1161.36 → 1166.34] really something here and the whole idea in there is because the way that jacks works and the way
[1166.34 → 1172.30] that numerical definitions in an x works is that when you are doing all the operations in your neural
[1172.30 → 1180.28] network like hey you know we need to we need to multiply those tensors we need to calculate a soft
[1180.28 → 1184.42] max we need to do the sum when you're doing all those computations you're actually not doing those
[1184.42 → 1190.24] computations at the moment what you're doing is that you're building a computation graph with
[1190.24 → 1194.62] everything that you want to do in that neural network, and then they get this computation graph
[1194.62 → 1199.92] and when you call that function with a particular tensor with certain dimensions a certain size
[1199.92 → 1206.46] it emits highly specialized codes for that particular type of tensor for that particular graph
[1206.46 → 1210.90] and that's why everything is functional because what you're doing is building a graph you're not
[1210.90 → 1216.94] doing any computations, and then you compile that to run the GPU when we saw this idea it was like hey
[1216.94 → 1222.74] everything can be functional, and you know when it started it was like a bunch of happy accidents you
[1222.74 → 1227.88] know a book being published so I like to say like I really have a thank-you like for prorogue because
[1227.88 → 1232.60] you know if they did not publish this book if somebody read the proposal that Sean sent to prorogue
[1232.60 → 1236.74] say hey we don't need genetic algorithms book for elixir maybe none of these would have started
[1236.74 → 1242.76] and then somebody pointed us to jack so it was all those things happening and that kind of like gave
[1242.76 → 1248.52] me a path to for us to explore and come out of this and I really think so I said like you know we said
[1248.52 → 1254.80] we are going to start working and as we build the tools we are going to try to find like what
[1254.80 → 1261.40] advantages elixir can have compared to other programming languages for example, and it turned out that as i
[1261.40 → 1267.76] kept saying what I thought would be a negative aspect which is immutability really turned out to
[1267.76 → 1274.24] be to be a feature right, and it's fascinating because there are some pitfalls in jacks for example
[1274.24 → 1279.08] so if you go to the jacks' documentation they have a long list of pitfalls, so there are some pitfalls in
[1279.08 → 1285.32] the jacks' documentation that they do not happen in the elixir implementation in no because everything's
[1285.32 → 1290.82] immutable so the way that jacks works is that in python they call it the tape pattern
[1290.82 → 1295.68] so basically as you're calling methods in an object it is requiring all the methods that you
[1295.68 → 1302.30] call in ruby we know it as method missing, but there are some operations in python that they cannot be
[1302.30 → 1308.52] recorded so for example if you are setting a property for example in the object or if you pass
[1308.52 → 1313.66] that object to a conditional you don't know that that object is being used in a conditional so jacks
[1313.66 → 1318.34] cannot record that structure in your code so they have like some pitfalls like hey you know you have
[1318.34 → 1323.18] to be careful or if you have a for loop if you have a for loop in jacks what it's going to do
[1323.18 → 1329.30] is that it's going to unroll the loop and that can lead to very large GPU code but in the next everything
[1329.30 → 1334.22] is immutable so we don't have those operations in the first place and because we have macros I can
[1334.22 → 1342.26] actually rewrite the if to be an if that runs in the GPU, so this is really cool so in an x when you go to
[1342.26 → 1349.22] the numerical definitions, and you look at the code that code no pitfalls is going to run on the GPU is
[1349.22 → 1354.80] going to be sent on the GPU it's effectively a subset of elixir to run the GPU so yeah so you know it
[1354.80 → 1358.46] started with this small tip and then it kind of spreads from there
[1358.46 → 1369.14] this episode is brought to you by snowplow analytics snowplow is the behavioural data
[1369.14 → 1375.58] management platform for data teams maximize the value of your behavioural data using snowplow insights
[1375.58 → 1381.42] a managed data platform that's built on leading open source tech leveraged by tens of thousands
[1381.42 → 1387.14] of users capture and process high quality behavioural data from all your platforms and your products
[1387.14 → 1391.84] and deliver that data to your cloud destination of choice when marketing needs to make data informed
[1391.84 → 1397.48] decisions when product needs next level understanding and when analytics needs rich and accurate data
[1397.48 → 1402.94] snowplow is the solution for data teams who want to manage the collection processing and warehousing of
[1402.94 → 1407.56] data across all their platforms and products get started and experience snowplow data for yourself
[1407.56 → 1412.48] at snowplowanalytics.com again snowplowanalytics.com
[1412.48 → 1434.82] so sitting on top of no is axon which is no powered neural networks you want to give us the skinny on
[1434.82 → 1442.32] that tool José yeah so it's pretty much what the name says it's neural networks built on top of no and
[1442.32 → 1449.10] uh so Sean is the one so a lot of those things Sean is the person behind it so axon Ella it's all
[1449.10 → 1457.12] Sean's work and what he did for axon is that he built all the building blocks of a neural network
[1457.12 → 1462.26] uh he built just using functions they are regular numerical definitions they are regular
[1462.26 → 1467.34] numerical definitions and numerical definitions are regular functions so he just built a bunch of
[1467.34 → 1473.96] functions, and then you can compose them together to build uh the neural networks, and so he did like
[1473.96 → 1479.68] he built all of this it was hilarious because I think we can still find it in the repo he created
[1479.68 → 1486.20] the initial issue which I think had like a hundred check boxes which was just like all the functions
[1486.20 → 1494.12] that you use like all the initialization functions optimizers layers activations everything that you have
[1494.12 → 1501.44] in a neural network that you usually use so he listed all those then he implemented most of those
[1501.44 → 1506.98] and then he came up with a higher level is still inside axon the higher level API so you can say hey you
[1506.98 → 1513.34] know I have a neural network that is going to be this dense layer and this convolutional layer and this
[1513.34 → 1519.76] activation and this and I want to train it and you're done so you know the same level of API convenience
[1519.76 → 1525.02] that you would expect from like Keras or from PyTorch is there in axon but the building blocks
[1525.02 → 1531.40] as well that's what axon is about it's a little bit you know out of my reach of my understanding
[1531.40 → 1537.78] and it's kind of funny because I can run the basic examples but I still don't have a GPU and then if
[1537.78 → 1542.56] you get a convolutional like neural network if you're going to train it without a GPU it's going to take a lot
[1542.56 → 1547.98] of time so i I cannot run some of the examples but uh Sean he added already a good amount of
[1547.98 → 1553.76] exact examples to to to the repo story so you know that we have like some very classical data
[1553.76 → 1559.90] sets that people use in machine learning like moist uh car I don't know if I'm pronouncing those
[1559.90 → 1566.74] correctly Daniel, but you probably know what I mean the fashion moist and so on, and he has examples of
[1566.74 → 1571.76] and then no algorithms like reset and this kind of stuff, and they are examples already in the repo
[1571.76 → 1577.24] story and for those things running in elixir and compiling and running on the GPU which is very exciting
[1577.24 → 1582.14] don't you have a GitHub sponsors or a donation button man let's get this man a GPU someone's
[1582.14 → 1590.04] going to get you a GPU come on the world would be a better place if José valid owned a GPU I'm gonna
[1590.04 → 1595.74] put it on record yeah I was really like in uh just an aside i I was like I'm going to buy a Linux
[1595.74 → 1601.50] machine then so I can have the GPU and then apple came out I was like oh we have TensorFlow running on
[1601.50 → 1607.94] m1, but they released just like the compiled executables and not the source code so I'm like
[1607.94 → 1613.74] do I buy a new machine that is going to take space in my house and then three months later apple is just
[1613.74 → 1618.58] going to the thing is going to be merging TensorFlow and I'm never going to use it again so in this way
[1618.58 → 1625.22] like so I'm just like I'm suffering for like the social paralysis I'm like you know should I invest
[1625.22 → 1630.98] on this thing or not well you've come to the right place this is Daniel's expertise right here this guy
[1630.98 → 1637.46] he builds these things in his house unfortunately it's all uh crazy right now i I know we ordered
[1637.46 → 1643.64] a server and like we had to switch the GPUs because of like I don't know if you saw NVIDIA's
[1643.64 → 1650.80] they kind of got mad that everybody was putting uh consumer cards in their enterprise servers and so
[1650.80 → 1655.56] that all got switched up which I understand their business but yeah that whole world is crazy
[1655.56 → 1660.78] right now in terms of actually getting your hands on something as well supply shortages and everything
[1660.78 → 1667.90] yeah yeah it's insane just scrolling through this like I'm I'm pretty excited to try this on my
[1667.90 → 1674.68] you know little workstation with a GPU I think it's cool that again I'm coming not from an elixir
[1674.68 → 1680.68] standpoint but I recognize the API like it's very Keras like this high level API that you're talking
[1680.68 → 1685.42] about where you're I've got a dense layer I've got you know a dropout layer whatever it is
[1685.42 → 1691.54] that like instantly makes sense to me, I feel like I could take this API and create like my model
[1691.54 → 1697.96] definition fairly easily and i I really like that being a python user and coming from that outside
[1697.96 → 1704.72] world like it is makes me want to play with this if it was a totally like different sort of
[1704.72 → 1711.26] looking API I think I would have I would be sort of nervous to dive in but I also see like you have
[1711.26 → 1716.30] your model struct you have your layers you have your high level API, and you talk about it like
[1716.30 → 1722.76] it's just an elixir struct and so serializing it to multiple formats is possible, and we're
[1722.76 → 1728.90] talking about the model itself so I don't know a ton about elixir structs but this sort of serializing
[1728.90 → 1735.58] it to multiple formats is really like interesting to me because at least from my perspective what I'm
[1735.58 → 1743.48] seeing is a lot of sorts of push for interoperability in the AI world where like people like publish their
[1743.48 → 1750.24] model that they wrote in PyTorch on PyTorch hub and like then like I'm over here with TensorFlow but
[1750.24 → 1756.48] I can pull it down and like convert it using something like onyx tools or something and use it in TensorFlow
[1756.48 → 1760.94] or maybe there are all sorts of frameworks out there and I think people are generally realizing
[1760.94 → 1765.76] it's not going to be one that wins the day, but interoperability is really, really important
[1765.76 → 1772.34] if we're going to release models and expect people to be able to use them so I don't know what was that
[1772.34 → 1778.46] sort of factoring in your mindset as you're thinking about how to represent models in axon yeah definitely
[1778.46 → 1783.10] when Sean was working on it from the design he was we were thinking you know how can we get
[1783.10 → 1789.42] an axon model load that into an elixir data structure so we can get that and send to the GPU
[1789.42 → 1794.48] and have that running on the GPU, and it goes back you know to what we were talking about
[1794.48 → 1802.16] a while ago that I think like the first users of this maybe I'm wrong and I'll be very, very glad to
[1802.16 → 1807.10] be wrong but I think the first users they're going to be hey we have our data scientists that are really
[1807.10 → 1812.88] super familiar with this tooling in python that is very productive very useful for them, and it's
[1812.88 → 1817.80] harder to convince them to migrate but hey we are running elixir in production and I just want to
[1817.80 → 1823.30] bring that model and run directly from elixir and I think that's very important for that use case
[1823.30 → 1829.20] so and then I mean the whole purpose of interoperability one of the things that I think it's really worth
[1829.20 → 1835.08] talking about that I think with this idea so you know a lot of people they think about elixir they
[1835.08 → 1841.24] think about web, but elixir is also perfect thanks to the nurse framework for embedded and i
[1841.24 → 1848.34] think there's a lot of potential in this area of you know having machine learning neural networks
[1848.34 → 1853.86] running on the edge and nerves can help with that and that can be an interesting application as well
[1853.86 → 1858.92] and that requires kind of the same ideas because they're not going to train on the device right so
[1858.92 → 1865.52] you need to build the model elsewhere and do all the steps and then bring that into the device so
[1865.52 → 1871.60] serialization is there and I think it's a matter of time into a lot of those things we are working
[1871.60 → 1876.56] on them as you know it's like we also started a machine learning working group in their language
[1876.56 → 1881.90] system foundation, so people interested in this so it's something that we plan to work but if somebody
[1881.90 → 1886.38] is really excited about this so if you're listening to the show like hey you know I want to try this out
[1886.38 → 1892.98] and maybe I can implement like onyx serialization, and you would like to work with us and the PR
[1892.98 → 1899.66] it's definitely welcome we can have a link to the airline ecosystem foundation the machine learning
[1899.66 → 1904.84] working group in the foundation so we have a slack people can join can talk to us and there's a lot of
[1904.84 → 1910.74] work to be done, and this realization is definitely going to play a big part of it yeah so how long
[1910.74 → 1918.44] have you both been working on axon because it just seems like there's so much like there's so
[1918.44 → 1924.18] much implemented like you were talking about you know hey we need all of these different layers
[1924.18 → 1930.00] implemented that people know about typically i I see libraries like maybe that have a new API for
[1930.00 → 1935.08] machine learning or something it seems like it takes them so long to sort of add operations and add
[1935.08 → 1941.02] you know support for different layers and such and uh I'm wondering like what was your thought
[1941.02 → 1948.16] process and approach to building this in a way that you could come out of the gates supporting as much
[1948.16 → 1956.90] of that as possible to give you an idea so Sean has been working on it on his free time okay, and he's
[1956.90 → 1961.08] starting working on axon as soon as we announced the net so he has been working on it for two months on
[1961.08 → 1967.84] his free time, and it already has a bunch of stuff if you check like the README you know it already
[1967.84 → 1972.50] has the cool I'm not going to be able to say everything but the dense layers dropout convolutional
[1972.50 → 1981.16] layers a bunch of optimizers like seven eight so he has been able to add those things really
[1981.16 → 1986.18] fast and I think one of the reasons for that is because the foundation are just functions we're just
[1986.18 → 1992.22] building functions on top of functions so it's its very easy to compose and the other thing
[1992.22 → 1998.38] is also that I think like one of the reasons I'm speculating here to be clear I think maybe one of
[1998.38 → 2002.34] the reasons why some of those libraries it takes a lot of time for them to implement a layer
[2002.34 → 2009.44] it's because they are implementing everything right they are going maybe like from python all the way
[2009.44 → 2016.10] down to the c code and implementing or c++ code and implementing that while for us, it's a very
[2016.10 → 2021.88] layered approach where axon just works about an x and x is the tensor abstraction, and then we have
[2021.88 → 2028.50] the tensor compiler stuff that compiles for LA and working at those different layers when you're
[2028.50 → 2036.34] working at x or in axon you are really at a high level you're not really worrying about c++ any of
[2036.34 → 2040.98] that or just say hey you know what are the tensor operations that I need to do and I think like
[2040.98 → 2048.36] that's why he was able to be so productive in building you know all of those features in this short
[2048.36 → 2054.86] time frame and I think adding new like new activations layers they're relatively straightforward
[2054.86 → 2061.14] what I think what takes more time and discussion is when we need to change the topology because
[2061.14 → 2066.14] that requires to think about how the struct is going to represent that so for example if you have
[2066.14 → 2072.80] a an or a recurring neural network now you have to think like you know oh if it's recurring now
[2072.80 → 2076.54] we need to get the data fitted back inside so you have to think how you're going to model that
[2076.54 → 2083.30] but it's mostly it's just that you know at the high level representation so that's kind of how things
[2083.30 → 2090.76] have been structured yeah I cloned the repo and his first commit was January 25th of 2021 it's pretty
[2090.76 → 2095.10] amazing with a few to follow, and it was funny because like the first commits are like add some
[2095.10 → 2100.20] functions more functions adding some even more common functions so he's just like cranking out
[2100.20 → 2105.16] these functions like you said yeah so that was in January okay yeah so a couple of months yeahs but
[2105.16 → 2111.76] while working on that he was still working on LA and an x with me so we started in November
[2111.76 → 2118.46] so in November it was Sean and i we were working part-time so it took us about three months to
[2118.46 → 2126.38] release an x and LA and then Sean uh he's still working with an x and LA, and then he's focused
[2126.38 → 2132.06] after we announced it in February he changed it to be on x on until we announced it, and now we are
[2132.06 → 2138.58] probably all like kind of going back and forth between projects so because there's still a bunch of
[2138.58 → 2143.94] things that we want to build in an x so one of the things that I really want to work on is streaming
[2143.94 → 2149.66] because so elixir is perfect for streaming and I want to have a very good abstraction so you know
[2149.66 → 2157.70] we can start streaming data to be inferred like into the GPU so you don't have to load everything
[2157.70 → 2164.80] into memory or for example if you have a webcam or a camera that it's your embedded device, or you're
[2164.80 → 2170.00] getting from web RTC or something like that, and you want to send that straight to the GPU and stream
[2170.00 → 2176.52] it so we can do all this kind of stuff interesting stuff that I think we can do so yeah so we are going
[2176.52 → 2181.32] to be jumping back and forth on that I think it speaks to the power of a solid abstraction too and
[2181.32 → 2185.82] like a layered approach when done well when you get to those higher layers like you said unless you
[2185.82 → 2191.46] have to change the topology if you're just adding and building on top and not having to drill down
[2191.46 → 2196.78] through each time then you can move relatively fast there's probably also an aspect of this where
[2196.78 → 2205.52] it seems like axon's API is trying to be familiar and so a lot of times i at least for me the slow
[2205.52 → 2210.82] part of software is like getting that API figured out you know and like rewriting that API so that's
[2210.82 → 2215.00] better and maybe there's a step-up because of all these other projects that have come before
[2215.00 → 2219.76] that makes it familiar to Daniel and other people who are working in this world exactly that's a very
[2219.76 → 2224.72] good point and I think on the axon side one of the inspirations I think it's there is a project
[2224.72 → 2232.12] think AI in python which is a functional approach yeah there's a team in Europe that writes the spacey
[2232.12 → 2240.14] library which is a NLP library and I think that their main like backbone for that is thought I see yeah
[2240.14 → 2246.16] so that has been one of the inspirations as well and I think there's pi lightning or lightning torch or
[2246.16 → 2250.98] something like that that has also so yeah that's that's a very good point you know so if you can
[2250.98 → 2255.42] look at what people are doing say hey this is what I think it's good this is what I think it's going
[2255.42 → 2260.32] to fit very nicely at what we do that speeds up the process uh considerably as well
[2260.32 → 2278.90] changelog plus is the best way for you to directly support practical AI join today and
[2278.90 → 2285.02] unlock access to a private feed that makes the ads disappear gets you closer to the metal and help
[2285.02 → 2291.86] sustain our production of practical AI into the future simply follow the changelog plus link
[2291.86 → 2298.54] in your show notes or point your favourite web browser to changelog.com slash plus once again
[2298.54 → 2301.66] that's changelog.com slash plus
[2301.66 → 2305.36] changelog plus is better
[2305.36 → 2323.70] I mean there's just such diversity in the AI world in terms of the types of models that people
[2323.70 → 2328.80] are building but there is a fairly consistent like if you look at the implementations whether
[2328.80 → 2336.36] it's TensorFlow or pi torch, or you know these other frameworks you can kind of get a pretty quick
[2336.36 → 2342.28] sense of how they're building their architecture looking into the source code and I mean I'm just
[2342.28 → 2348.54] looking at some of the layers that are implemented in axon and like I said I think you've done a good
[2348.54 → 2354.36] job at like I don't know how to read elixir I can sort of get the sense of what's happening
[2354.36 → 2360.24] here and I think that's a testament to like yeah like following some of the inspiration the good
[2360.24 → 2366.02] inspiration that's already out there in the world and also I think it'll be easier for people maybe
[2366.02 → 2372.08] that do want to jump, and you know experiment in elixir from the python world, and they want to add
[2372.08 → 2378.30] their own cool layers into axon it's going to be a lot easier for them to jump in and do that I think
[2378.30 → 2383.56] if they feel like they're not in a total foreign world they recognize some of these components and all
[2383.56 → 2390.98] that so I definitely think that that's a good call I know that some like data science AI world
[2390.98 → 2398.24] kind of operates with a weird set of tooling that includes these things like called notebooks and
[2398.24 → 2404.90] other things I know I saw like there's even some functionality related to like interactive coding
[2404.90 → 2411.90] and cells and that sort of thing too isn't there yeah so there is a separate project another person has
[2411.90 → 2417.14] been working on this project uh Jonathan kiosk when Sean and I started talking like hey you know
[2417.14 → 2422.74] we want to build this foundation for machine learning numerical computing, and then we mapped a bunch of
[2422.74 → 2427.22] things that we have to do and there are a bunch of things that we have not started working on yet so
[2427.22 → 2432.22] for example we don't have an equivalent to data frames so that's another question that has to be solved
[2432.22 → 2439.36] we don't have plotting libraries yet but one of the things that we want to do was this idea of the
[2439.36 → 2445.50] interactive and collaborative notebook and to give a bit more context Daniel so we have the phoenix
[2445.50 → 2451.34] web framework in elixir and the phoenix web framework I think two years ago launched something called live view
[2451.34 → 2458.34] which makes it really easy for you to build interactive real-time applications but on the server
[2458.34 → 2463.86] so without having to write JavaScript which if you're not a JavaScript developer that can be a plus
[2463.86 → 2469.52] and because the logic is on the server it allows you to do like collaborative because if you have
[2469.52 → 2473.72] multiple people collaborating on the text on the text right like the server is the one that
[2473.72 → 2480.56] knows where people are what they should do how the text should change so it's perfect for building
[2480.56 → 2485.46] this kind of applications the elevator pitch is not correct but the one line somewhere that can say is
[2485.46 → 2490.98] like react on the server this way you can think about it if I view and I said I want to do this we want
[2490.98 → 2496.24] to build this notebook thing as well which we called live book so that's the live book project and the way
[2496.24 → 2502.60] it started was very funny so we have a project called doc which generates documentation for elixir
[2502.60 → 2506.26] and you're really proud of it we think that our documentation just looks great, and it's standardized
[2506.26 → 2512.20] all the projects in the community they generate this documentation with doc it has a bunch of great
[2512.20 → 2518.00] features and somebody sometime ago open up and say hey you know this project is using jquery is huge
[2518.00 → 2522.56] we probably don't need to use jQuery anymore, so somebody opened up this issue you should track her
[2522.56 → 2528.14] I was like sure sounds a good idea if somebody wants to do it and then out of nowhere somebody
[2528.14 → 2534.22] sends a request they didn't ask if they should do it right they just set up request replace jQuery
[2534.22 → 2539.46] by JavaScript and I was like this is great I reviewed the code was flawless I reviewed like the
[2539.46 → 2546.38] best of my power CCT JavaScript and then i I went to check and I was like oh Jonathan he lives in
[2546.38 → 2551.76] crackle which is where I live he goes to AJH which is where my wife studied this is very
[2551.76 → 2555.44] interesting, and it's like oh he has like some phoenix experience, and he's still a student and
[2555.44 → 2560.42] I was like you know what maybe he wants to work with us on this live book thing so I sent him an
[2560.42 → 2565.88] email like hey you know you want to talk you know at this time we had not announced the next yet but
[2565.88 → 2571.42] we have announced some benchmarks comparing like code running on the GPU and not on the GPU which was
[2571.42 → 2576.18] like 4 000 times faster or something like that and then I told him like hey do you want to work
[2576.18 → 2580.14] with us, and then he's like sure, but you know I'm a student like no problem you're going to work part
[2580.14 → 2587.98] time so he started in January working on live book and the idea so, and then we started talking to some
[2587.98 → 2594.18] people so there was at about the same time uh john another Jonathan john he had released
[2594.18 → 2599.80] something like a notebook for elixir as well a very bare bone one so we had some experience from
[2599.80 → 2603.60] python we brought him in like hey you know if you're going to do this how are you going to do
[2603.60 → 2608.22] it what are the benefits, and then we're like okay so one of the things that we want to do is that we
[2608.22 → 2613.38] want to leverage the fact that you know it's very easy to build collaborative and interactive
[2613.38 → 2621.30] applications in elixir so it needs to be collaborative from the one, and it is so i I gave an I there is a
[2621.30 → 2626.68] video on YouTube of me announcing live book, and it's really cool because it shows how live book works
[2626.68 → 2632.78] it shows Exxon as well so there are some good examples and so like hey it needs to be collaborative
[2632.78 → 2637.84] from day one, and we really want to be interactive because one of the things so for those who are not
[2637.84 → 2643.20] familiar with elixir like the elixir runtime it's very easy to extract a lot of information from the
[2643.20 → 2649.62] runtime like what your code is doing all we break our code into lightweight threads of execution so you
[2649.62 → 2655.42] can expect each of them so we said okay we wanted to be interactive not only for people that are
[2655.42 → 2660.50] working with like machine learning and numerical computing but if you want to get data out of an
[2660.50 → 2665.68] elixir system like a production system and try to see like hey where is my bottleneck you should be
[2665.68 → 2671.12] able to do all that you should be able to uh interact with a live system as well and interact with your
[2671.12 → 2676.30] neural network that is training so this feature is not there yet, but it's part of our vision and then
[2676.30 → 2681.26] I said well and what do people complain about in notebooks that's always part of the research right so if
[2681.26 → 2687.82] you go like to Jupiter uh what people usually complain a lot what don't they complain about
[2687.82 → 2693.64] what we heard was like well the formula that it writes to disk it's not good to deep it's not easy
[2693.64 → 2699.54] to virtual control right so how are we going to solve that the dependencies are not explicit so
[2699.54 → 2704.92] and the evaluation order is not clear as well so how we can solve all those things so you know we
[2704.92 → 2710.62] brought our set of inspirations we bought the problems, and we started working on how we want to solve
[2710.62 → 2716.16] this and then a couple of weeks ago we announced it maybe one or two weeks ago we announced live
[2716.16 → 2721.92] book, or maybe it was last week anyway it's there you can really see a four-hour vision is not complete
[2721.92 → 2728.42] you can see the important parts in there of like you know it's fully reproducible the evaluation order
[2728.42 → 2735.54] is clear your dependencies need to be explicitly listed so everybody who get a notebook knows exactly
[2735.54 → 2740.28] what they need to install and the notebook's going to install it for you john he created a format
[2740.28 → 2744.74] called live markdown which is a subset of Markdown that we use for the notebooks which is really
[2744.74 → 2750.80] great because now if we change a notebook we are just changing a markdown file which means you can
[2750.80 → 2756.78] put it on virtual control people can actually review your changes without having to you know
[2756.78 → 2763.40] spin an instance of that thing and make that work so for us, it's a step again into this ecosystem
[2763.40 → 2768.46] and I think there are a bunch of things that we want to explore and try out and really try to be like a
[2768.46 → 2775.72] a very modern approach to you know for interactive and collaborative notebooks and there are
[2775.72 → 2781.74] other things like happening in space so uh there's drummer notebooks there's also Pluto Jr
[2781.74 → 2788.20] call me from the Julia folks there's also deep note which is a software as a service so
[2788.20 → 2793.00] we're kind of looking at everything and coming up with our own takes and ideas as well that's awesome
[2793.00 → 2799.38] I'm glad that when you looked at this you like took that perspective of like not we need notebooks
[2799.38 → 2805.84] people love notebooks but what's what's wrong with them because I think there have been a lot of there's
[2805.84 → 2811.76] notebook kernels for all you know all sorts of different things for Jupiter, but they all suffer from
[2811.76 → 2817.66] similar issues and of course I love Jupiter, and it's powerful and people use it with great success
[2817.66 → 2823.70] but I think after people have used it for so long they've seen these consistent issues I think you
[2823.70 → 2829.68] know the whole managing state thing that you mentioned, and the execution flow is probably the
[2829.68 → 2834.82] top one on my list so now you're really tempting me to try out it also seems like you release something
[2834.82 → 2839.50] cool every week right I don't know how that works I don't release something cool every week so I'm
[2839.50 → 2845.30] feeling really deficient right now I'm with you, I don't have anything new to release for now
[2845.30 → 2849.98] until next week dang what you need to do is find some really talented university students and get
[2849.98 → 2855.96] them to you know inspire them to work on some stuff for you, I guess so yeah yeah so uh yeah
[2855.96 → 2861.12] Jonathan has been excellent into this as you know like and it was like his first live view application
[2861.12 → 2868.30] so uh I think it's both a testament to Jonathan and to live view the fact that he could build this thing
[2868.30 → 2874.40] in three months while still studying working part-time and go check it out go check the video I think
[2874.40 → 2879.12] I'm really excited about live book it's fascinating and so for example uh we just merged
[2879.12 → 2883.88] like auto-completion so when you're writing code there is now auto-completion as you would get from
[2883.88 → 2891.28] VS Code various Monaco editor and everything's like collaborative right like if we have to if
[2891.28 → 2896.24] we have multiple working on it is changes our broadcast and based on this idea that it's built
[2896.24 → 2901.16] on live view where you don't have to write JavaScript like the whole thing including all the Monaco
[2901.16 → 2906.50] extensions that we had to do so it had like the elixir flexor and so on it's like 2 000 lines of
[2906.50 → 2912.60] JavaScript that's it for everything that it does work the whole thing about the notebook is that
[2912.60 → 2918.00] in my opinion it was a very different approach to how we approach like no and exon it's like hey
[2918.00 → 2923.62] you know like for no and exon we're like okay let's build this and see where this leads us but for
[2923.62 → 2929.16] notebook it was like this is an area that elixir is perfect at and I really want to
[2929.16 → 2937.26] have our take on this I think we can make this ours like our version of this how our vision our
[2937.26 → 2942.56] understanding of this and of course that requires looking around, but it was a very different thought
[2942.56 → 2947.22] process just like hey I think we can build this and I think we can build this great because we have
[2947.22 → 2952.42] great tools for that and just to make it clear like out of the box it works distributed as well so
[2952.42 → 2956.24] for example if you have a bunch of people using notebooks for some reason and you want to
[2956.24 → 2961.32] start like five machines in production and have people connect to those machines from anywhere
[2961.32 → 2965.30] they want it just work out of the box there's no need for external dependencies you don't need to
[2965.30 → 2969.98] bring grad you don't need to bring a database, so everything was really built using like the
[2969.98 → 2974.46] the again like if we go to the beginning of the talk we're talking about their language machine
[2974.46 → 2980.22] right, and they're building telecommunication systems right imagine you have this platform, and you can
[2980.22 → 2987.04] build collaborative notebooks right so that was kind of our idea our take how does it do that because
[2987.04 → 2993.96] it looks like it only runs on like local host maybe there's like a way to how do you tell it hey I've got
[2993.96 → 3000.28] 10 nodes that I want you to run across is that just configuring phoenix so by default we run it on
[3000.28 → 3004.98] local host by default if I run it on our machine you don't want to expose that and have somebody access
[3004.98 → 3010.62] the notebook yeah it's like an evil it's like a public facing evil right yes right imagine if you
[3010.62 → 3016.84] are at an elixir cone somebody would just be who is running notebooks here that I can't right now i
[3016.84 → 3021.76] think we just need to tweak the configuration file but one of the things that we are working on we are
[3021.76 → 3027.52] going to get to the release we're going to ship both docker images and a command line executable
[3027.52 → 3033.74] then we'll have flags for all this kind of stuff you know okay do these and most likely what
[3033.74 → 3040.58] people they want to do is that they want to say hey you know I am deploying this to Kubernetes so
[3040.58 → 3046.80] I'm going to use something that uses the Kubernetes DNS manager to connect the nodes
[3046.80 → 3052.62] so in elixir you would use something like pure age or lib cluster that figure out the topology
[3052.62 → 3059.18] connects everything for you yeah and I can definitely confirm that people will want to spin these things
[3059.18 → 3064.32] up everywhere now I'm not surprised when I hear this but the first time I started hearing
[3064.32 → 3070.22] production notebooks and I was like how do you have a production notebook it's a notebook like how are you
[3070.22 → 3076.48] running a notebook in production, but this is like so pervasive people are like oh this is my production
[3076.48 → 3082.04] notebook and this is my you know dev notebook and all of these things I don't know if I go that far
[3082.04 → 3087.50] because I'm like i I don't know how to support a notebook and production but if it is such a pervasive
[3087.50 → 3093.40] idea it's cool to see that as a piece of this um and of course there are other things too like you were
[3093.40 → 3099.10] mentioning you know pandas and other things so for people that aren't familiar in python there's a
[3099.10 → 3105.82] library called pandas which deals with tabular data, and you can do all sorts of cool like data mugging
[3105.82 → 3111.70] stuff so yeah it's cool to hear you say that those things are on your mind and because you release a
[3111.70 → 3118.22] cool thing every week you know maybe that will be next week or the following one yeah right now like
[3118.22 → 3124.94] I think we are going to tackle graphing because graphs because it's part of the notebooks but I'm
[3124.94 → 3130.20] hoping for like the data frame stuff other people are going to step in, and we are having a bunch
[3130.20 → 3135.50] of related discussions on the Alain ecosystem foundation machine learning working group and this kind of
[3135.50 → 3140.28] stuff if you want to talk about like and there is ensured like machine learning right, and then we can
[3140.28 → 3145.30] talk about neural networks and there's like so much work to be done and so many things to explore so
[3145.30 → 3150.96] people that are excited like jumping when you're going to have a feast right because like we didn't
[3150.96 → 3158.68] talk about like hey clustering you know forests and classifiers regressions, and then we can talk about
[3158.68 → 3164.52] linear algebra there is just so many things in the ecosystem that one can build and explore that
[3164.52 → 3169.92] there is a lot of work to do, and we hope like people they'll get more and more excited and they
[3169.92 → 3175.56] are going to join us in this journey yeah it seems like if you've got the graphing thing going
[3175.56 → 3182.54] and you're talking about elixir having this sort of natural abilities with web development with live book
[3182.54 → 3190.92] and other things here you know a big thing in the AI world is monitoring your training runs with a bunch of
[3190.92 → 3195.64] cool graphs with you know something like a tensor board or something like that so it seems like
[3195.64 → 3201.36] yeah there's like that would enable a lot of things it'd be pretty sweet to have your you know your
[3201.36 → 3208.82] training run going in axon you kick it off from a live book, and then you can pull up a know
[3208.82 → 3215.48] interface to see all your nice training plots and all those things and that's all happening in a
[3215.48 → 3222.58] really nice unified robust way yeah that's definitely something you know that we explore at some point
[3222.58 → 3228.06] probably tensor board integration as well it's something that we are bound to have yeah it seems
[3228.06 → 3232.14] like live book really could be your marketing machine you know it could be like your way in
[3232.14 → 3238.48] for all the disillusioned notebook shares out there who've had you know like Daniel said they can do a lot
[3238.48 → 3243.72] of stuff with Jupiter notebooks or existing tooling, but there's pain points with collaboration with all
[3243.72 → 3249.54] these things I mean the fact that one of your headlines is sequential evaluation to me that
[3249.54 → 3254.50] seems like this is not how everything works it says code cells run in a specific order guaranteeing
[3254.50 → 3261.78] future users of the same life not so quick jarred I'm like that's a feature like how things work
[3261.78 → 3268.18] uh I mean it's kind of the wonderful thing about Jupiter notebooks and the really hard thing about
[3268.18 → 3273.70] them because like it's similar um like if you go back in history I don't know if any either of you
[3273.70 → 3280.02] ever used Mathematica, but it's a similar idea like you have these cells of execution it's really wonderful
[3280.02 → 3287.08] for like experimentation right because you can oh you did this but when you're in experimentation you
[3287.08 → 3293.20] expect things to fail almost all the time right so you don't expect to have like a script that runs
[3293.20 → 3298.94] and you unit test it and blah blah you expect to try something and fail and fail over and over and
[3298.94 → 3304.38] over until you like tweak it enough to where it works and so that's great in the notebook environment
[3304.38 → 3311.04] if you can tweak things like that the problem is than like oh what were the four million things that I did
[3311.04 → 3319.20] tweak to get this to go and what state is saved like in my notebook like I could get it to work and then
[3319.20 → 3324.68] reboot it and run it from top to bottom, and it's not going to work again right so it's its the good
[3324.68 → 3331.04] thing and the bad thing yeah and I'm pretty sure it's like this feature let's say this sequential
[3331.04 → 3336.46] evaluation is going to be a limitation at some point people will be like hey I started training my
[3336.46 → 3340.52] neural network but now I want to do something else in the same notebook while the neural network's
[3340.52 → 3348.18] training how can I do that so we'll have to come up with ways of like branching, but we want to be
[3348.18 → 3354.48] very explicit on the model like so we'll say hey you can branch here or what we have been calling it
[3354.48 → 3359.10] internally because everything is organized in sections we have to think maybe I can set up some
[3359.10 → 3365.18] asides so asides they fork from a particular point they branch from a particular point and execute
[3365.18 → 3372.78] the code based on those bindings so or from it's basically the state of the notebook from that moment on
[3372.78 → 3377.86] without ignoring the other side so it's something we'll have to tackle and if you look at the issue
[3377.86 → 3381.54] structure there are a bunch of things that we have been thinking about so for example one of the
[3381.54 → 3386.24] things that I want to do so we have the idea so when you persist in notebooks you're persisting to
[3386.24 → 3392.20] the file system so on the issues like for example pluggable file systems and I want to make GitHub a file
[3392.20 → 3399.14] system so you know you can easily like to persist your notebooks to GitHub and that works transparently
[3399.14 → 3404.12] from live book without you having to say hey I need to clone and stuff like that we can
[3404.12 → 3410.08] work directly on the repo story and I think that's going to be a boom for collaboration as well
[3410.08 → 3414.84] or not collaboration I mean a different kind of collaboration right you put on GitHub so somebody
[3414.84 → 3418.86] can fork and play with it, I know there's like this thing in the python world called binder
[3418.86 → 3424.62] so essentially you could create a GitHub repo with a notebook, and then you click on the little badge and it
[3424.62 → 3430.84] just pops up a hosted version of that notebook that that will run so you can like to give it a docker image
[3430.84 → 3437.44] or something with all the dependencies for someone like me if there was like that tie-in with GitHub and
[3437.44 → 3443.24] I could just launch a notebook and try like axon that's like I feel like people would just latch onto
[3443.24 → 3451.36] that so quickly then the barrier is not like oh like elixir's sort of new to me as a python person so
[3451.36 → 3456.58] I need to figure out the tool chain but really what I want to do is I just want to like quick shift enter
[3456.58 → 3461.34] through a few cells and see how it works and that's that's very powerful yeah that's a very
[3461.34 → 3465.90] good point something first to look into yeah well you guys have done a lot, but there's a lot left to
[3465.90 → 3470.28] do what's the best place to get involved like you said fertile ground what do you say hop in and have
[3470.28 → 3475.20] a feast or something if you're interested in the space and an elixir it sounds like there's lots of
[3475.20 → 3481.88] ways to get involved and to build out a lot of the stuff that's lacking so is there a discourse forum
[3481.88 → 3487.08] or is there a slack is there a community around this is just you and the dash bit folks working on it
[3487.08 → 3492.06] what's the situation there everything we have the elixir dash and x organization on GitHub
[3492.06 → 3497.60] but a lot of discussion is happening in the airline ecosystem foundation we have the machine learning
[3497.60 → 3503.50] working group so if you go to the beef website you can get all the working groups there you're going
[3503.50 → 3508.24] to find machine learning, and then you can create an account it's free, and then you can join this lack
[3508.24 → 3513.62] and we'll be there so that's where we are usually chatting things originally a lot of those things
[3513.62 → 3518.68] they were kept confidential like live book but now everything at least everything that dash bit was
[3518.68 → 3525.30] working on it's out in the public we don't have anything no more secret projects so that's the place to
[3525.30 → 3530.08] go and where we're talking about things we have a monthly meeting where we meet and discuss and
[3530.08 → 3537.80] exchange ideas so that's definitely the place is no bringing machine learning tools to Erlang or are there
[3537.80 → 3544.08] other Erlang but not elixir efforts in this space you understand what I'm saying yeah like is this the
[3544.08 → 3549.92] first time in Erlang the beam-based tooling around numerical computation is happening or is it like
[3549.92 → 3556.24] Erlang only things that have been going on I think it's the first time for the ecosystem and yeah
[3556.24 → 3562.14] and because you can call you know elixir from Erlang with no performance cost whatsoever yeah it's pretty
[3562.14 → 3566.70] cool right you can just call like the numerical definitions they don't work in Erlang because they
[3566.70 → 3572.74] they translate the elixir AST not the elixir AST, but it was like the elixir execution to the GPU
[3572.74 → 3578.08] that wouldn't work with Erlang but everything that we are building on top like exon because it's just
[3578.08 → 3584.10] building on top of the abstraction, so somebody could go get exon call it from Erlang build a neural
[3584.10 → 3589.50] network from Erlang and like just run it, and it should just work that's cool Daniel anything else
[3589.50 → 3593.86] from your side of the fence you want to ask José about before we let him go I'm just super excited
[3593.86 → 3599.36] about this hopefully there is some crossover from the python world it seems to me like the timing
[3599.36 → 3608.50] is such that people in the AI world very much are more open to trying like things outside the
[3608.50 → 3614.58] python ecosystem than they once were and so yeah that's my hope and I definitely want to play around
[3614.58 → 3619.66] with this and appreciate your hard work on this and I'm excited to try it out and also share it with
[3619.66 → 3625.70] with our practical AI community awesome and I'm really glad that uh you are having me on the show
[3625.70 → 3632.26] and I was able to share all those ideas and this work that we have been doing oh you're welcome back
[3632.26 → 3636.80] anytime all the links to all the things are in your show notes so if you want to check out José's
[3636.80 → 3641.68] live book demo on YouTube we got the link to that we'll hook you up with a link to the Erlang
[3641.68 → 3646.42] ecosystem foundation if you want to get involved of course axon and no are linked up as well
[3646.42 → 3650.44] so that's all thanks everybody for joining us, and we'll talk to you again next time
[3650.44 → 3658.92] thank you for listening to practical AI we appreciate your time and your attention if you
[3658.92 → 3664.48] enjoyed this episode help us out by spreading the word think of a friend think of a colleague
[3664.48 → 3668.90] somebody who would benefit from listening to it and send them a link we'd really appreciate it
[3668.90 → 3674.28] practical AI is hosted by Chris Benson and Daniel whiten ack it's produced by jarred Santa
[3674.28 → 3679.94] with music by break master cylinder thanks again to our sponsors quickly Linde and launch darkly
[3679.94 → 3684.06] that's our show we hope you enjoyed it, and we'll talk to you again next week
[3684.06 → 3686.06] you
[3704.28 → 3714.06] you
[3714.06 → 3716.06] you
[3716.06 → 3717.06] you
[3717.06 → 3721.06] you
[3721.06 → 3723.06] you
[3723.06 → 3725.06] you
[3725.06 → 3727.06] you
