[0.00 → 4.78] If we look at the hardware of a quantum computer, it actually has two main parts.
[4.86 → 7.34] It has the CPU itself, the quantum processor.
[7.56 → 9.02] That's the quantum hardware.
[9.26 → 15.74] That's where the magic happens, where you have these superpositions and the quits and all this crazy quantum stuff.
[16.10 → 18.20] And then you have what we call the control hardware.
[18.60 → 20.34] This is actually not quantum hardware.
[20.54 → 21.64] It's classical hardware.
[22.24 → 29.24] The hardware interfaces the quantum processor and talks to it and operates it, make it do what we want it to do.
[29.24 → 34.38] And that's very complicated hardware that one has to build specifically.
[34.72 → 37.08] So it's not regular servers or anything like that.
[37.18 → 40.36] It's really hard for controlling a quantum processor.
[40.82 → 42.28] And that's what the quantum machine does.
[52.60 → 58.28] Welcome to Practical AI, a weekly podcast making artificial intelligence practical,
[58.28 → 60.36] productive, and accessible to everyone.
[60.72 → 61.52] Subscribe now.
[61.66 → 65.50] If you haven't already, head to practicalai.fm for all the ways.
[65.88 → 71.50] Special thanks to our partners at Vastly for delivering our shows superfast to wherever you listen.
[71.82 → 73.66] Check them out at fastly.com.
[73.92 → 76.08] And to our friends at fly.io.
[76.42 → 80.00] We deploy our app servers close to our users, and you can too.
[80.34 → 82.22] Learn more at fly.io.
[82.22 → 92.14] Well, welcome to another episode of Practical AI.
[92.50 → 93.94] This is Daniel Whiten ack.
[94.04 → 97.00] I'm a data scientist with SIL International.
[97.32 → 102.76] And I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin.
[103.02 → 103.74] How are you doing, Chris?
[104.20 → 104.92] Doing well.
[105.00 → 105.44] Doing well.
[105.52 → 106.44] How are you today, Daniel?
[106.44 → 116.16] I'm doing great because any day is great when I get to sort of any sort of throwback to my old physics days,
[116.16 → 121.22] which mostly I don't get to dabble in much these days, is a fun day.
[121.32 → 124.60] And today we've got a cool intersection with that world.
[124.90 → 129.72] We've got Jonathan Cohen with us, CTO at Quantum Machines.
[129.72 → 136.82] And we're going to talk a little bit about an update on quantum computing and how that intersects with AI.
[137.00 → 137.58] Welcome, Jonathan.
[138.02 → 138.40] Hi.
[138.62 → 139.04] Thank you.
[139.18 → 141.00] It's very cool to be here.
[141.54 → 144.88] And I'm excited to talk to you about some quantum physics as well.
[145.96 → 146.50] Yeah.
[146.68 → 147.12] Great.
[147.34 → 147.62] Great.
[148.06 → 159.54] Well, I'm guessing most of the time on this show and most of our listeners are probably used to hearing us chat about neural networks or GPUs or classical computing.
[159.54 → 167.72] And we have talked about quantum computing on the show, but it's been quite some time, and I'm sure the field is advancing quickly.
[167.72 → 184.18] Maybe just as a starting point, could you remind us of the general pitch of what is quantum computing and maybe why people are interested in quantum computing more generally?
[184.60 → 184.94] Sure.
[184.94 → 194.68] So quantum computing is a new kind of way to build a computer that's based on the laws of quantum mechanics.
[195.08 → 207.06] So it's kind of interesting because quantum mechanics as a theory of nature was sort of developed in parallel to the development of computers the last hundred years or so.
[207.06 → 218.44] And, you know, on one hand, we developed this amazing technology that we now have, which is computing, that's based on classical physics.
[218.62 → 222.56] It's based on the classical laws of how the universe, you know, behaves.
[223.10 → 230.72] But in parallel, in the last hundred years or so, there is, you know, completely new understanding of how nature works on a very fundamental level.
[230.72 → 255.52] So, you know, somewhere in the very late 70s, early 80s, physicists started to understand that perhaps we can use these new laws of nature that we discovered to also build a new type of computer that's going to kind of harvest this weird behaviour of nature that we call quantum mechanics.
[255.52 → 270.00] And it turns out that you can do that, and it expands the notion of what we mean by a computer and essentially allows building a computer that has a stronger computational power, at least for some problems.
[270.00 → 278.12] Not for all problems, but for some very difficult problems that classical computers, we say classical meaning not quantum, regular computers.
[278.68 → 286.52] For some computational problems that classical computers have, you know, very hard time to deal with, quantum computers could solve them very easily.
[286.52 → 301.02] So, like, as you're talking about this new type of computer, would I be correct in thinking that I can't run out to the store and buy a Pentium or an AMD and pop it in with the RAM on the motherboard?
[301.26 → 305.44] Is there, what's different about that approach on the hardware side?
[305.84 → 312.40] And then what would you use it for that's different from that kind of classic idea that we all have been using all our lives?
[312.40 → 332.40] Yeah, so the main point of quantum mechanics and before quantum computers is that, you know, while we see things in the day-to-day that, you know, things are in a specific state, you know, I'm drinking coffee from my cup and I put it down, and it sits in one place, right?
[332.48 → 334.62] It's in one place and not in another place.
[334.62 → 339.88] So, in quantum mechanics, things can actually be in various states at the same time.
[340.24 → 347.00] And while we don't see it, you know, with coffee cups, we do see it with electron, for example.
[347.12 → 350.52] We can actually put an electron in what we call a superposition.
[350.70 → 354.42] That means, you know, it's in two places at the same time.
[354.98 → 357.90] And this is exactly what quantum computers take advantage of.
[357.90 → 363.82] So, you know, the basic building block of a classical computer is the bit, the bit of information.
[364.20 → 366.60] It's, you know, it's a system that has two states.
[366.66 → 369.16] It can be either in the zero state or in the one state.
[369.62 → 375.22] And then, you know, if you have two bits, then they can be 00, 01, 10, 11, and so on.
[375.36 → 378.96] If I have eight bits, I have 256 states, right?
[379.08 → 381.90] 0000 and 00001 and so on.
[381.90 → 389.98] But at every single point in time, the classical computer can only be in a single state of all the bits of information that it holds.
[390.60 → 392.68] And then we manipulate those bits.
[392.86 → 397.22] We go from one state to another state to another state and so on.
[397.26 → 399.00] So, it's like a state machine.
[399.20 → 402.88] We're moving from state to state in order to solve a computational problem.
[403.46 → 409.50] But quantum computers replace this notion of a bit with what we call a quantum bit or, in short, a quit,
[409.50 → 415.98] which is a system like the electron that I told you about that can actually be in two states at the same time.
[416.04 → 419.52] So, I can be in both zero and one at the same time.
[420.04 → 425.18] And in fact, the system can be in sort of, it can be in zero and one with different weights.
[425.26 → 431.90] So, I can be a little bit zero and a lot in one, or I can be a lot in zero and a little bit in one and so on.
[431.90 → 441.94] And when now I put a lot of quantum bits together, a lot of quits together, I now can be in this massive superposition of many, many, many states,
[442.02 → 444.34] all the states of the system at the same time.
[444.92 → 455.18] And you can use that to sort of, you can use this parallelism to, in some cases, again, do sort of parallel computation
[455.18 → 459.92] instead of going, you know, state by state, if that makes sense.
[459.92 → 470.44] So, it sounds like with that massive parallelism, it sounds like it can handle probabilities based on what you were saying in many states very well.
[470.90 → 483.36] What type of problems does that kind of capability lend itself to that maybe our traditional, you know, the laptop I'm on right now would not be as well suited for?
[483.36 → 489.96] Or what does a problem that, like having lots of quits, you know, to solve, what does it look like to address?
[490.38 → 491.78] Yeah, it's a great question.
[491.94 → 498.08] So, there are certain problems that we know for sure that quantum computers can give an advantage of.
[498.20 → 501.54] So, one great example is the Show's algorithm.
[501.54 → 509.70] So, that's an algorithm that actually breaks code because it finds the prime factors of a large number.
[509.86 → 516.38] So, you know, if you take a large number and try to factorize it to its basic prime factors,
[516.66 → 519.72] that's a problem that's very hard for classical computers.
[519.72 → 522.04] And it has some structure.
[522.12 → 534.44] The problem has some structure that allows us to use this parallelism of a quantum computer in order to solve this problem exponentially faster than what we can do today in a classical computer.
[534.44 → 544.20] Now, it's very hard to explain exactly what in this problem makes it so that we can use this quantum parallelism to solve it so much faster.
[544.80 → 553.58] You kind of have to look at the details of the problem, the structure of the problem, in order to see how you can take advantage of this quantum parallelism.
[553.58 → 564.50] So, we don't know exactly, and cannot actually categorize exactly all the problems that quantum computers will solve much faster than classical computers.
[564.90 → 566.36] But we have examples.
[566.52 → 567.66] So, we have the Show's algorithm.
[568.20 → 569.80] We have Grover's algorithm.
[570.04 → 580.30] So, Grover's algorithm is an algorithm that solves basically a search problem, searching in an unsorted list, finding an element, specific element of interest in an unsorted list,
[580.30 → 584.20] which also can map to very general optimization problems.
[584.76 → 591.80] But this algorithm, for instance, is not giving us an exponential speed-up.
[592.00 → 597.12] It actually only gives us a square root speed-up over what you could do with classical computers.
[597.90 → 604.92] So, there is this zoo of algorithms that gives different kinds of speed-ups for different kinds of problems.
[604.92 → 613.66] And people are still working very hard on the problem of categorizing exactly what quantum computers can solve faster than classical computers.
[614.46 → 623.42] The other thing is that there are also algorithms, quantum algorithms, that we have today that use this parallelism of these quits.
[623.90 → 627.00] And that we don't even know that they are going to work.
[627.00 → 630.64] So, these are heuristics, basically, that people have come up with.
[630.80 → 637.06] There are good reasons to think why they would give us a computational speed-up against classical computers.
[637.64 → 639.40] But nobody can prove those.
[639.74 → 639.84] Okay?
[640.02 → 650.72] So, we are basically in this kind of same situation that actually maybe AI was a decade or two ago, where, you know, we have some thoughts about these algorithms.
[650.72 → 653.36] People are very hopeful that they will work.
[653.88 → 657.74] And these are relevant for optimization problems, very general optimization problems.
[658.28 → 663.32] This is an algorithm that's called AOA that solves combinatorial optimization problems.
[663.58 → 668.86] And then another algorithm that's called VIE, which solves for chemistry problems.
[669.34 → 678.12] And these are heuristic algorithms that we just have to build a machine and try those algorithms on and see if they work better than classical computers.
[678.12 → 687.86] Yeah, I have one maybe naive question from my own perspective, because I think, obviously, you're well plugged into the state-of-the-art.
[688.04 → 690.64] Chris, actually, I think you know a little bit more as well.
[690.78 → 696.48] But for me, like, I'm thinking, okay, I've been hearing about quantum computers for some time.
[697.08 → 704.80] One sort of naive question from mine is, like, what quantum computers, actual quantum computers exist in the world right now?
[704.80 → 713.34] Because sometimes I go to, like, if I go to one of the cloud providers or something, sometimes I'll see, like, oh, here's the AWS quantum thing.
[713.46 → 718.60] But when I look at it, it's really just, like, so you can run simulations of quantum research.
[718.60 → 734.16] So if I'm wanting to, like, let's say I want to run something on an actual quantum computer, what would be my choices sort of right now in terms of where those actually exist and, you know, kind of the state of what they are?
[734.40 → 739.34] And how you see that sort of shaping up over the coming couple of years?
[739.34 → 747.40] Yeah, so today you can do, you can access quantum computers through the cloud with several players.
[747.78 → 754.78] So IBM, for example, has their quantum cloud service that actually gives you access to real quantum computers.
[755.06 → 757.52] You can log in, and you can actually run algorithms.
[757.84 → 762.60] Well, these are small quantum computers, of course, they're still a prototype of the technology.
[762.60 → 767.16] But you can actually run algorithms, and you can see how they behave, as well as on simulators.
[767.56 → 775.76] And you can compare, and then you can find that your quantum computer is doing not as well as the simulation because it has a lot of errors.
[775.86 → 777.98] This is the main problem with quantum computers today.
[778.32 → 779.10] But you can do that.
[779.24 → 780.52] And that's actually very cool.
[780.52 → 784.14] And IBM, for example, they give access to their own computers.
[784.44 → 795.10] But Azure and AWS have launched their quantum services in the last few years that give you access to third-party quantum computers.
[795.10 → 801.58] So many different computers that are built by full-stack quantum computing vendors.
[802.16 → 805.16] You're getting like IQ, like PCI.
[805.16 → 810.64] So these are startups in quantum computers that build full-stack quantum computers.
[810.88 → 815.50] And you can access those machines actually today through the cloud, which I think is very cool.
[816.12 → 824.26] And yeah, they also give you access to simulators, and you can run on those as well, which I think is quite amazing, to be honest.
[824.26 → 840.40] I mean, there are certain experiments that I used to do during my PhD at the Weizmann Institute only 12 years ago that used to take a PhD student maybe three or four years to set up such an experiment and to run it.
[840.82 → 851.76] And now I can just log into one of these cloud platforms and I can run the experiment that just 10 years ago used to take a few years to set up.
[851.82 → 853.50] I can do it in probably a few hours.
[853.50 → 855.92] But that's it, I think it's quite amazing.
[855.92 → 855.98] Thank you.
[883.50 → 908.94] So one of the things I was curious about, just to follow up on what you were talking about a moment ago, is just to kind of set my expectation with quantum computers, you know, assuming that obviously because we're going quantum, we're not going out and getting a typical CPU.
[908.94 → 916.12] Is there anything, is it mainly the CPU is a quantum CPU that you would put into the computer?
[916.46 → 922.30] And is there any other types of changes that you would make to a classical computer just to get a sense of it?
[922.36 → 931.60] Like how, so, you know, how close is kind of the generalized architecture of a quantum computer to a classical computer?
[931.60 → 933.66] Or how much has to change to make that leap?
[933.98 → 934.20] Okay.
[934.30 → 935.26] That's a very good question.
[935.26 → 942.84] I think that a lot of things need, I mean, are very different in quantum computers because the basic operations are fundamentally different.
[942.84 → 949.88] Like, you know, classical computers, again, they're built on, you know, based on the bits, and then you have gates, right?
[949.98 → 951.74] That's how you manipulate the information.
[951.96 → 955.78] So you can actually build an entire computer from an end gate, right?
[955.98 → 959.94] But in quantum, we don't even have the notion of an end gate.
[960.06 → 960.88] We have other gates.
[961.40 → 962.46] We have a Hadamard gate.
[962.56 → 963.46] We have a Synod gate.
[963.46 → 968.76] We have different elementary logical operations on quits, right?
[969.12 → 978.42] So that makes it so that the sort of the entire stack, or at least the low level parts of the stack needs to be very different.
[978.94 → 987.40] But then I would also say that eventually it's not, I mean, the way I see quantum computers, especially in the early days,
[987.40 → 1002.32] giving us an advantage is not just by being used as standalone computers, but actually as more of an accelerator inside a more heterogeneous data centre, right?
[1002.42 → 1006.40] So, you know, the quantum computer could do only certain problems.
[1006.50 → 1010.22] It's not going to replace the CPU, and it's not going to replace the GPU.
[1010.22 → 1017.54] You still, there are things that there's just no reason to do them using quantum devices.
[1018.00 → 1025.22] Maybe in 50 years, because everything's going to be quantum and quantum devices are going to be as cheap as classical computing devices.
[1025.44 → 1030.32] But right now you will have your CPU, you have a GPU, and you have your CPU.
[1031.06 → 1037.58] And the CPU will be used to accelerate certain types of subroutines that can help your entire application.
[1037.58 → 1046.64] And so that's why it's important that we also build integration of these quantum computers into a more heterogeneous computer environment
[1046.64 → 1052.12] and allow people to program what we call hybrid workflows.
[1052.62 → 1054.22] So quantum classical workflows.
[1054.78 → 1057.36] Could you describe what one of those workflows is like?
[1057.82 → 1063.58] So, and that was a great explanation, by the way, of kind of the difference in a quantum computer and stuff.
[1063.58 → 1072.36] But you've mentioned several times along the way about kind of that hybrid, fitting it into a larger architecture that includes a lot of those classical components.
[1073.04 → 1079.24] You know, and so like what, but I'm trying to get my head wrapped around what kind of problem as a user I might solve.
[1079.28 → 1086.62] An example that would use both quantum and the hybrid and like what part of the problem goes to each and stuff.
[1086.70 → 1088.42] Can you give us some sort of example on that?
[1088.42 → 1089.42] Yeah, sure.
[1089.64 → 1095.42] So the typical example is what we call the variational quantum algorithms.
[1096.44 → 1102.80] So actually both the algorithms I mentioned before, AOA and also VIE, these are variational quantum algorithms.
[1103.32 → 1109.64] What this means is that essentially what we're doing is we're trying to minimize the cost function of interest.
[1109.88 → 1111.40] That's the problem we're trying to solve.
[1111.40 → 1118.52] But then the way we do it is that the CPU, the quantum processor, is only computing the cost function.
[1118.58 → 1122.68] Let's say we have a cost function that's very hard to compute on a classical computer.
[1123.48 → 1130.40] So the quantum processor only basically calculates the cost function, giving it a set of parameters.
[1130.88 → 1134.22] But then the optimizer sits in the classical side.
[1134.22 → 1139.80] So what we're doing is we're running a quantum circuit, what we call a parameterized quantum circuit.
[1140.04 → 1144.38] So we're running a quantum program with some input parameters.
[1144.64 → 1148.04] Then the quantum processor computes the cost function.
[1148.62 → 1151.24] And then the result goes into the classical processor.
[1152.02 → 1157.14] And it would run an optimizer like, I don't know, like a gradient descent or something like that.
[1157.24 → 1163.18] And then the result, then that would generate new parameters for the quantum circuit, the quantum program.
[1163.18 → 1169.22] And then it goes back and forth like this until we find the parameters that would minimize the cost function.
[1170.10 → 1182.10] Yeah, this is a fascinating example because I've been thinking about like, okay, well, if I'm connecting maybe some of the challenges within the AI world to this space.
[1182.34 → 1184.38] I mean, you just mentioned gradient descent.
[1184.54 → 1187.68] You mentioned optimizing with a cost function.
[1187.68 → 1194.90] Like this is all definitely very connected to like what might happen in like an AI training scenario.
[1195.32 → 1204.38] Of course, like there are all sorts of problems or there are certain computations, like you say, that work well on a GPU.
[1204.62 → 1207.30] And that's sort of scaled up right now.
[1207.30 → 1220.12] But I'm wondering as you're kind of diving into these types of hybrid problems with quantum machines, what might you see right now like in the AI industry or certain sets of problems in the AI industry?
[1220.60 → 1224.98] Like the challenges that the AI industry is facing in terms of compute.
[1224.98 → 1235.64] What are people thinking about in terms of what might overcome some of those challenges on this sort of hybrid computing side with potentially a quantum advantage?
[1236.18 → 1238.06] What's the current thought process around that?
[1238.60 → 1238.78] Yeah.
[1238.78 → 1250.18] So, I mean, I hope that, for instance, using some of these hybrid algorithms would be able to solve some optimization problems that are also relevant to AI training.
[1250.74 → 1256.28] To be honest, I'm far from being an expert on quantum AI or quantum neural networks specifically.
[1256.92 → 1261.82] But I know a little bit about the subject and I know a little bit about the challenges in AI.
[1261.82 → 1268.30] And I know some of the algorithms that we have for quantum computers could solve this optimization problem.
[1268.54 → 1278.12] So when we train a neural network and want to optimize its parameters, in many cases, this is a very hard optimization problem.
[1278.60 → 1285.36] And in some cases, it could fit exactly this kind of optimization problems that a quantum computer could solve.
[1285.50 → 1289.00] And specifically, these hybrid algorithms might be able to solve.
[1289.00 → 1295.84] So then we could use this quantum or this hybrid quantum classical algorithms to train neural networks.
[1295.96 → 1296.76] That's one example.
[1297.62 → 1305.98] There are also some recent works about quantum neural networks that where the network itself is quantum.
[1306.66 → 1314.92] And some mathematical proofs that why such networks would require, again, in some specific cases,
[1314.92 → 1320.08] but important cases, why would they require much less data to train?
[1320.32 → 1327.96] And that, I think, is very important because, right, in many cases, we just need a lot of data to train those neural networks.
[1327.96 → 1331.22] And in many cases, we don't have enough data.
[1331.82 → 1336.40] So maybe quantum neural networks could be relevant in some of those situations.
[1336.40 → 1338.88] It's a fascinating subject.
[1338.88 → 1344.14] And I think that people are, you know, obsessively are looking into it.
[1344.24 → 1358.16] And I'm just dying to have the machine because I think many of those things are going to only start to reveal themselves once we have big enough quantum machines that we can try some of those things on.
[1358.16 → 1364.84] Because, again, a lot of those things are, you know, heuristic algorithms that cannot really prove that will give us an advantage.
[1365.20 → 1367.32] We just have to build a machine and try it.
[1367.32 → 1374.78] Yeah, and I think that gets a little bit to my follow-up question, which is, like, when these things start to come online,
[1374.92 → 1382.06] and I know that Quantum Machines is working on sort of platform software, hardware to do that, which we can get into here in a bit.
[1382.20 → 1387.94] But before we do that, one of the things that's on my mind is, like, as these computers come online,
[1388.06 → 1391.30] they're in some sort of, like, hybrid compute centre.
[1391.30 → 1394.58] I'm thinking just about, like, my own workflows.
[1394.86 → 1398.44] Like, how's my own workflow potentially going to change?
[1398.56 → 1405.74] Like, when I'm wanting to run something on a quantum computer, like, if I just search Google for pictures of quantum computers,
[1405.86 → 1408.80] I see people with, like, lab coats or something on, right?
[1408.86 → 1411.00] And they're, like, going in and doing things.
[1411.20 → 1416.12] And so do you see this as being, like, oh, I'm going to have TensorFlow.
[1416.38 → 1418.16] I'm going to have PyTorch, AXX, whatever.
[1418.16 → 1425.20] I have my Python code, which I'm, you know, executing some type of AI training,
[1425.42 → 1427.66] or I program the model architecture or something.
[1427.82 → 1436.84] And then at certain points, there's going to be a library that maybe reaches out to that hybrid quantum piece
[1436.84 → 1439.16] and executes some of the optimization.
[1439.56 → 1445.30] Or, like, how will that affect the actual kind of the day-to-day kind of workflow
[1445.30 → 1447.76] and what it might be like to program these things?
[1447.76 → 1455.28] Because I'm guessing, like, the common AI developer is not going to all of a sudden learn everything about quantum mechanics, right?
[1455.34 → 1458.54] So somehow there has to be a higher level kind of abstraction.
[1458.78 → 1460.32] What do you think that will look like?
[1460.60 → 1463.90] Yeah, I actually think it will look exactly like what you described.
[1464.66 → 1467.96] I mean, it's going to take some time to get to that place.
[1467.96 → 1473.04] But I think that eventually that's exactly how it's going to roll.
[1473.22 → 1481.44] Because, as you said, you know, not everybody is going to learn these new types of quantum programming languages
[1481.44 → 1487.12] and these, you know, fundamental new different operations in quantum and how we use them.
[1487.12 → 1492.18] And, in fact, this is not – I think this is even not necessary because, again, there is, you know,
[1492.48 → 1499.58] there will be certain subroutines that, of course, we can configure, and we can parameterize
[1499.58 → 1501.98] and we can use them in various different ways.
[1502.48 → 1507.26] But this is, you know, this could be done, as you said, as a library that you can – you know,
[1507.30 → 1512.82] one could use and embed in – and you could embed, you know, that in your workflows.
[1512.82 → 1517.28] Now, that's going to take some time and I think that in the very early days, actually,
[1517.42 → 1522.22] we're going to have experts that are really going deep into the machine,
[1522.44 → 1528.52] into the low-level kind of programming of these quantum machines
[1528.52 → 1535.42] and do all the optimizations to have a use case like that where you can use it at high level
[1535.42 → 1538.10] and just solve your problem, right, or accelerate your problem.
[1538.22 → 1541.50] Just as a follow-up, as we're getting into tooling
[1541.50 → 1543.34] and kind of getting to what your organization does,
[1543.52 → 1545.68] but more of a general follow-up real quick.
[1545.76 → 1548.48] I'm curious, like, you know, you mentioned IBM earlier
[1548.48 → 1551.08] and they're well-known in the quantum space, you know,
[1551.12 → 1552.88] for all that they do in the cloud and everything.
[1553.38 → 1558.18] They do have an open-source Python SDK, you know, for that.
[1558.28 → 1563.80] And so, you know, it is in Python, which makes it very convenient for other AI tooling and stuff.
[1563.80 → 1570.30] So would you expect things like TensorFlow and PyTorch and all to kind of wrap that library
[1570.30 → 1576.30] or other libraries like it to provide that kind of quantum accessibility, if you will,
[1576.44 → 1581.30] to people who are not otherwise quantum experts and kind of let the tooling make that?
[1581.40 → 1585.80] Do you think as a general, so I'm not talking about IBM or TensorFlow specifically,
[1585.80 → 1590.22] but like as a general way of introducing the public to quantum,
[1590.82 → 1595.60] is doing it through tooling that makes it easier kind of what we should expect going forward?
[1596.08 → 1596.98] Yes, absolutely.
[1597.44 → 1598.40] I really think so.
[1598.88 → 1600.66] Yeah, I mean, it has several layers.
[1600.84 → 1603.60] So there are programming languages and obstructions,
[1603.70 → 1608.30] and then there are just application libraries that I think are going to be important.
[1608.30 → 1615.82] And then, yes, and then even higher level, like things like TensorFlow or PyTorch,
[1615.98 → 1619.22] as you mentioned, that they could just wrap those things,
[1619.58 → 1623.94] and, you know, some people don't even need to know that it runs, you know, under the hood.
[1624.38 → 1626.90] So I think that eventually that's what's going to happen.
[1627.00 → 1629.86] And, yeah, people are starting to play with that for sure.
[1629.98 → 1633.44] I mean, IBM, you know, they, as you mentioned, they have,
[1633.44 → 1636.72] so they don't just have their open stack, you know,
[1636.90 → 1640.10] that you can access kind of low level, the quantum computer,
[1640.64 → 1643.60] and program the gates, but they also provide libraries.
[1643.72 → 1647.30] And there are many other startup companies that are doing that these days,
[1647.72 → 1649.38] sort of kind of going up the stack.
[1649.62 → 1653.26] And I think that these tools are going to be very important.
[1653.94 → 1658.54] I also think that we're going to discover a lot of things in the next five, six, seven years.
[1658.54 → 1665.38] And I hope that many of those tools don't have to sort of make a U-turn or something like that.
[1665.62 → 1670.90] But I think that, you know, we will have to learn a lot and change things as we go along.
[1671.10 → 1672.80] So, but that's a part of it.
[1672.88 → 1673.78] I mean, we have to start.
[1673.96 → 1676.08] We have to build the entire stack.
[1676.24 → 1677.26] That's why it's so exciting.
[1677.40 → 1679.76] I mean, we're waiting for the hardware to sort of mature,
[1679.88 → 1683.54] but we're building, you know, the low level software parts of the stack,
[1683.64 → 1685.78] the high level software parts of the stack,
[1685.78 → 1689.50] and kind of trying to see how all of it is going to fit together.
[1689.92 → 1692.18] And yeah, I do think that at the end of the day,
[1692.64 → 1696.22] there is no reason why someone would program quantum gates.
[1696.64 → 1697.82] Well, I mean, some people will,
[1697.92 → 1702.16] but most people will just want to use the machine for accelerants and other problems.
[1702.16 → 1719.04] So, Jonathan, I was just scrolling through your website
[1719.04 → 1722.78] and kind of with the view of what you've talked about in mind
[1722.78 → 1725.94] in terms of this sort of hybrid system that you envision,
[1726.28 → 1729.34] how people will kind of program these problems.
[1729.34 → 1733.08] And I see that, you know, quantum machines specifically
[1733.08 → 1739.42] is addressing some of the hardware and software platform things
[1739.42 → 1741.10] around this type of system.
[1741.28 → 1745.50] And I even see like a nice little GIF image showing like a data centre
[1745.50 → 1749.76] with, you know, racks of what I'm assuming is classical computers
[1749.76 → 1752.92] and racks of, you know, quantum machine equipment
[1752.92 → 1755.70] and then like a quantum computer in the middle.
[1755.70 → 1759.82] So I'm wondering if you could maybe generally let us know,
[1760.08 → 1765.64] like as quantum machines looked at this developing space,
[1765.84 → 1771.46] how did you decide like where you thought the opportunity was
[1771.46 → 1774.44] in terms of building out the infrastructure around this?
[1774.54 → 1778.18] Because I could, obviously there are different pieces of this
[1778.18 → 1782.02] in terms of building the A type of computer itself
[1782.02 → 1785.96] or working only on software, but it seems like you're kind of dipping
[1785.96 → 1787.98] a little bit into hardware and software.
[1788.34 → 1792.74] Could you kind of describe your approach and the motivation behind that?
[1793.00 → 1793.74] Yeah, definitely.
[1794.26 → 1797.32] So if we look at the hardware of a quantum computer,
[1797.58 → 1799.66] it actually has two main parts.
[1799.72 → 1802.24] It has the CPU itself, the quantum processor.
[1802.42 → 1803.92] That's the quantum hardware.
[1804.14 → 1805.80] That's where, you know, the magic happens,
[1805.80 → 1808.24] where you have these superpositions and the quits
[1808.24 → 1811.10] and all this crazy quantum stuff.
[1811.46 → 1813.52] And then you have what we call the control hardware,
[1813.82 → 1816.18] or this is actually not quantum hardware.
[1816.38 → 1819.56] It's classical hardware, but it's the interface.
[1819.78 → 1823.18] It's the hardware that interfaces the quantum processor
[1823.18 → 1825.42] and talks to it and operates it,
[1825.54 → 1827.16] make it do what we want it to do.
[1827.48 → 1829.90] And that's very complicated hardware
[1829.90 → 1832.52] that one has to build specifically.
[1832.86 → 1835.22] So it's not regular servers or anything like that.
[1835.22 → 1839.92] It's really hardware that's dedicated for controlling a quantum processor.
[1840.42 → 1841.82] And that's what the quantum machine does.
[1842.18 → 1844.26] Well, that's what we started from.
[1844.68 → 1848.22] And this was because, well, we saw a bottleneck there.
[1848.58 → 1852.22] So this was five years ago when we started thinking about those things
[1852.22 → 1856.76] and thinking about starting a startup in quantum in general.
[1857.02 → 1860.44] It was just the very early days when quantum industry sort of started.
[1860.44 → 1866.46] And there were some of the early investments in companies in the U.S.
[1866.46 → 1871.60] And me and one of my co-founders, Tamar Sivan, is the CEO of the company.
[1872.20 → 1875.24] We wanted to start our own company, and we wanted to do it in quantum
[1875.24 → 1879.94] because that's basically all we knew coming out of our PhDs in quantum devices.
[1879.94 → 1881.80] And we knew a guy.
[1882.54 → 1886.98] We had a friend who finished his PhD about four years before us
[1886.98 → 1890.54] and he left to do his postdoc at Yale University
[1890.54 → 1894.98] in one of the leading groups in the world in quantum computing
[1894.98 → 1897.42] in the group of Professor Rob Zhukov.
[1898.08 → 1903.40] And over there, he basically performed one of the milestones in the field
[1903.40 → 1905.42] in the last, let's say, decade,
[1905.42 → 1910.42] where he actually performed an experiment demonstrating quantum error correction
[1910.42 → 1911.68] on superconducting quits.
[1912.24 → 1914.66] So quantum error correction is one way,
[1914.96 → 1919.02] basically the mainstream way to deal with the fact that quantum computers
[1919.02 → 1920.56] are very noisy.
[1920.72 → 1921.62] They have a lot of errors.
[1921.76 → 1923.54] They just make errors all the time.
[1923.64 → 1925.16] The error rate is very, very high.
[1925.46 → 1929.78] And so the mainstream way that we think that we'll be able to deal with this
[1929.78 → 1931.18] is by doing quantum error correction.
[1931.28 → 1932.02] But it's very hard.
[1932.02 → 1936.72] So Nissan performed this first demonstration of quantum error correction
[1936.72 → 1939.38] on superconducting quits in his postdoc at Yale.
[1939.78 → 1943.06] And to do that, he had to deal with a lot of bottlenecks
[1943.06 → 1944.96] that came from the control system.
[1945.38 → 1949.66] So he had to develop by himself a new kind of control system
[1949.66 → 1950.92] to do that experiment.
[1951.90 → 1955.18] And this was because quantum error correction is sort of what pushes
[1955.18 → 1958.56] the control layer of the stack to its limits.
[1958.56 → 1963.62] He had to deal with some of the most challenging problems of that time.
[1964.16 → 1966.74] And when we started thinking about what are we going to do,
[1966.86 → 1969.08] we realized that these challenges,
[1969.38 → 1972.68] some people, like most people didn't hit those challenges yet,
[1972.76 → 1975.12] but they will in the next few years.
[1975.42 → 1978.04] And so we felt we had a sort of head start.
[1979.00 → 1984.20] And we wanted to be, you know, like startups want to be higher in the stack, right?
[1984.20 → 1985.84] You want to do software and everything.
[1986.12 → 1990.16] But in quantum, we felt that we were at the top of the stack
[1990.16 → 1994.46] where actually there is a true need in the market right now.
[1994.88 → 1996.38] So that's what we did.
[1997.08 → 1999.06] Let me ask you a question just to clarify,
[1999.22 → 2001.56] because I know it's central to your business.
[2002.24 → 2004.28] When you talk about control systems,
[2004.40 → 2005.88] can you talk a little bit about like
[2005.88 → 2008.56] what exactly a control system does,
[2008.90 → 2010.54] you know, in the context of quantum,
[2010.54 → 2014.26] just so that to make sure that we understand exactly
[2014.26 → 2015.86] kind of how that fits into the equation?
[2016.38 → 2016.52] Sure.
[2016.76 → 2019.84] So there are various ways to implement the quantum processor,
[2020.02 → 2021.50] but in 90% of them,
[2021.62 → 2025.84] the quits are sitting in some kind of array of quits.
[2026.28 → 2029.98] So they're physically stuck in space somewhere on the chip,
[2030.08 → 2031.96] for example, or in a vacuum chamber.
[2032.34 → 2034.36] And then you have an array of quits.
[2034.36 → 2038.10] And now, so you can kind of think about it as, you know,
[2038.26 → 2040.84] as a yeah, let's just say an array of quits.
[2041.14 → 2043.60] But then in order to perform the operations,
[2044.20 → 2047.00] that the logical operations, the quantum gates,
[2047.44 → 2050.50] you send signals from the outside
[2050.50 → 2053.74] in the form of pulses of electromagnetic waves.
[2054.10 → 2058.88] So just like your cell phone sends pulses of microwave signals
[2058.88 → 2060.82] to the cellular tower,
[2060.82 → 2066.72] our control system sends this orchestra of microwave RF signals
[2066.72 → 2069.12] to the CPU, to the quantum processor.
[2069.42 → 2073.94] And this is the quantum algorithm in its most kind of raw form, right?
[2074.20 → 2077.46] You shoot pulses on your quantum device,
[2077.86 → 2079.98] and it hits the quit, physically hits the quit,
[2080.08 → 2083.68] and it performs the operations on the quits.
[2084.24 → 2087.40] You need to orchestrate this sequence of microwave pulses
[2087.40 → 2088.68] very, very carefully.
[2088.68 → 2090.74] It has to be very well-timed.
[2091.08 → 2092.82] And you also want to measure signals
[2092.82 → 2094.66] coming back from the quantum processor.
[2095.08 → 2097.42] So signals, microEV or RF signals,
[2097.54 → 2099.18] come back from the quantum processor.
[2099.34 → 2100.44] You need to measure those.
[2101.00 → 2102.16] And sometimes, for example,
[2102.22 → 2103.50] if you want to do quantum error correction,
[2103.68 → 2104.58] you need to measure those.
[2104.68 → 2106.66] You need to perform classical calculations
[2106.66 → 2110.20] to understand what errors are cured on the chip,
[2110.28 → 2110.84] for instance,
[2111.02 → 2113.26] and then respond with new pulses.
[2113.80 → 2115.12] So that's what we call feedback
[2115.12 → 2116.54] in the control system.
[2116.54 → 2120.02] And it sounds like when you're talking about sending pulses and stuff,
[2120.14 → 2123.98] is that software and hardware in a quantum context
[2123.98 → 2125.22] that we're talking about there,
[2125.46 → 2129.08] or is it just one or the other for a control system?
[2129.48 → 2129.80] Exactly.
[2129.96 → 2131.02] So you build the hardware,
[2131.16 → 2134.20] but then you need to program the sequence of pulses, right?
[2134.20 → 2139.28] So you build the hardware that can generate these pulses,
[2139.48 → 2141.22] but now you need to program your sequence.
[2141.48 → 2142.56] The user, for example,
[2142.60 → 2144.44] needs to program the sequence of pulses
[2144.44 → 2147.44] that needs to go to the quantum processor and operate it.
[2147.44 → 2148.90] And if you want,
[2149.02 → 2151.20] this is the assembly language of a quantum computer.
[2151.76 → 2155.94] This is sort of the lowest level programming language
[2155.94 → 2159.34] that you talk to your quantum computer with, right?
[2159.42 → 2162.76] Because you tell the controller what pulse to send when,
[2163.18 → 2166.72] and this is really the lowest level structure of the operations.
[2167.08 → 2168.60] I appreciate the clarification.
[2169.40 → 2172.12] So if you're kind of going back for a moment
[2172.12 → 2173.82] to kind of having that,
[2174.14 → 2175.26] like as a practitioner,
[2175.26 → 2178.74] and I'm thinking about kind of my practical workflow,
[2179.14 → 2182.08] and I'm now integrating quantum computers
[2182.08 → 2185.62] and your control system for managing that
[2185.62 → 2187.50] into my workflow.
[2187.94 → 2189.76] In our context, we're doing AI.
[2190.12 → 2192.16] And so let's say that we're a little ways in the future
[2192.16 → 2194.38] and we're starting to look at algorithms
[2194.38 → 2196.28] on the AI side that could benefit
[2196.28 → 2197.96] where part of that is quantum.
[2198.34 → 2201.46] How does that workflow look in a practical,
[2201.60 → 2203.26] like from the practitioner standpoint,
[2203.98 → 2205.08] what should they expect?
[2205.26 → 2208.36] You know, how are they connected and such as that?
[2208.50 → 2209.26] So you mean like,
[2209.38 → 2214.26] how would this workflow actually run on the hardware or?
[2214.62 → 2215.62] Yeah, I guess I,
[2215.72 → 2216.40] well, to some degree,
[2216.48 → 2217.60] I'm trying to think like,
[2217.70 → 2219.46] so I'm trying to kind of bring it back around
[2219.46 → 2220.24] from our side
[2220.24 → 2224.38] to connect the quantum computing benefit
[2224.38 → 2228.42] with the things that our audience is typically engaged in,
[2228.42 → 2230.96] which is trying to get AI algorithms,
[2230.96 → 2231.70] you know,
[2231.70 → 2234.70] the models developed and then deployed out there.
[2234.70 → 2237.36] And so as they're going through that process,
[2237.36 → 2239.72] like I'm trying to kind of pull it all together now.
[2239.94 → 2240.10] Yeah.
[2240.18 → 2241.42] What does that look like?
[2241.46 → 2245.34] Is there a quantum computer with the control system
[2245.34 → 2249.78] that you've produced sitting beside a classical computer
[2249.78 → 2253.68] that has a GPU in it and a CPU in it in the classical sense?
[2253.68 → 2256.72] And there's some networking between them.
[2256.84 → 2256.92] Like,
[2256.98 → 2260.64] what does that look like if we're five years out or whatever?
[2260.80 → 2261.78] You can pick your timeframe,
[2261.78 → 2264.74] but the point where we're now starting to integrate that
[2264.74 → 2267.32] into some sort of practical workflow
[2267.32 → 2269.36] and people in our audience might be using it.
[2269.56 → 2272.22] What might that look like from your position today?
[2272.50 → 2272.76] You know,
[2272.80 → 2274.32] forecasting into the future.
[2274.32 → 2275.92] It's very similar to what you described.
[2276.14 → 2276.16] So,
[2276.48 → 2276.78] well,
[2276.82 → 2277.46] there are two models,
[2277.54 → 2277.86] I would say.
[2277.98 → 2278.24] One,
[2278.46 → 2279.26] let's say that everything,
[2279.48 → 2281.20] let's just imagine an on-prem system,
[2281.30 → 2281.50] right?
[2281.58 → 2284.68] Where basically I have my GPU and my CPU
[2284.68 → 2287.44] and then I have a quantum computer.
[2287.58 → 2289.04] And the way it looks like it's,
[2289.14 → 2289.28] yeah,
[2289.32 → 2290.44] it's the control system.
[2290.52 → 2291.32] That's the interface.
[2291.74 → 2294.02] So we are the interface between the classical
[2294.02 → 2294.96] and the quantum side.
[2295.10 → 2297.52] So you have your racks of servers
[2297.52 → 2300.20] with GPUs and CPUs and all that.
[2300.26 → 2303.10] And then you have some racks with the control electronics
[2303.10 → 2305.70] and they're connected through the network.
[2306.04 → 2308.80] And the control electronics runs the programs
[2308.80 → 2309.92] on the quantum processor.
[2310.64 → 2312.72] So we can just call that combination
[2312.72 → 2313.90] of the control electronics
[2313.90 → 2314.78] and the quantum processor,
[2314.94 → 2316.94] we can just call it the quantum accelerator.
[2317.62 → 2317.76] Yeah,
[2317.76 → 2319.26] so now you have a quantum accelerator
[2319.26 → 2320.64] and it's connected to the network
[2320.64 → 2322.44] and you can talk to it via,
[2323.00 → 2323.36] for example,
[2323.44 → 2324.40] our programming language,
[2324.54 → 2324.74] QA,
[2324.94 → 2326.50] which is this low level,
[2326.62 → 2327.46] very low level,
[2327.84 → 2329.92] we call it pulse level programming language
[2329.92 → 2331.26] in the quantum jargon.
[2331.26 → 2333.78] And you say it's pulse level programming language
[2333.78 → 2336.78] that now I can write a workflow.
[2336.96 → 2337.64] So for example,
[2337.88 → 2338.08] you know,
[2338.12 → 2339.82] I can use a workflow tool.
[2340.18 → 2340.40] Actually,
[2340.50 → 2342.62] we are developing such a tool
[2342.62 → 2346.10] for developing hybrid quantum classical workflows.
[2346.32 → 2347.02] We call it entropy,
[2347.48 → 2348.70] but you can use others.
[2348.70 → 2350.52] And then you write a workflow
[2350.52 → 2352.32] where you run something on the GPU
[2352.32 → 2354.06] and then something on the CPU.
[2354.46 → 2354.90] And then,
[2355.06 → 2355.36] you know,
[2355.40 → 2357.36] and maybe there's communication between them.
[2357.46 → 2358.80] So choose your favourite way
[2358.80 → 2360.04] to communicate between
[2360.04 → 2361.36] whether it's processes
[2361.36 → 2362.92] or functions that we call.
[2363.10 → 2363.36] And then,
[2363.42 → 2365.20] and then this entire thing
[2365.20 → 2366.68] would just run,
[2366.82 → 2367.16] you know,
[2367.34 → 2368.46] programs on the CPU
[2368.46 → 2369.60] and then program,
[2370.12 → 2371.88] this EQUAL program on the CPU
[2371.88 → 2374.38] and the result would be analyzed
[2374.38 → 2374.98] in the
[2375.12 → 2376.12] maybe in the GPU
[2376.12 → 2377.96] and so on and so forth.
[2378.08 → 2378.20] Right.
[2378.66 → 2380.26] And if we go back to,
[2380.58 → 2380.60] and,
[2381.14 → 2381.34] but,
[2381.68 → 2382.06] and again,
[2382.16 → 2382.36] like,
[2382.58 → 2382.78] you know,
[2382.78 → 2385.14] eventually you would probably not have to write
[2385.14 → 2386.56] this one code
[2386.56 → 2387.58] at such low level
[2387.58 → 2390.76] and you could take advantage of libraries
[2390.76 → 2391.66] that by themselves
[2391.66 → 2393.60] would run hybrid workflows,
[2393.78 → 2393.96] right?
[2394.02 → 2395.82] Because to solve
[2395.82 → 2397.34] a certain optimization problem,
[2397.34 → 2399.02] maybe you already have a library
[2399.02 → 2400.64] that runs an optimization
[2400.64 → 2402.20] that uses both the CPU,
[2402.34 → 2402.74] the GPU,
[2402.90 → 2403.56] and the CPU
[2403.56 → 2405.42] and just solves for you
[2405.42 → 2406.64] a certain subroutine
[2406.64 → 2407.46] and then you have
[2407.46 → 2408.86] an even higher level workflow
[2408.86 → 2409.88] that would solve,
[2410.02 → 2410.38] I don't know,
[2410.62 → 2411.60] predict weather better
[2411.60 → 2413.84] or something of that sort.
[2414.06 → 2414.22] Right.
[2414.60 → 2416.32] I don't know if this was clear or not.
[2416.54 → 2417.10] I don't know
[2417.10 → 2417.82] if this was a...
[2417.82 → 2418.08] No,
[2418.20 → 2418.58] that was,
[2418.68 → 2419.50] that was a good one.
[2419.58 → 2419.80] That's great.
[2420.20 → 2421.40] It tied it together for me.
[2421.46 → 2421.84] Thank you.
[2421.94 → 2422.24] Okay.
[2422.54 → 2424.60] I'm happy to do that.
[2424.88 → 2425.22] Yeah,
[2425.36 → 2425.72] yeah.
[2425.92 → 2427.12] And as we kind of
[2427.12 → 2429.76] get close to an end here,
[2429.92 → 2431.08] I'm just looking through
[2431.08 → 2432.00] some of the things
[2432.00 → 2433.80] that you're involved with
[2433.80 → 2435.72] or the companies involved with.
[2435.78 → 2437.02] It seems like there's a lot
[2437.02 → 2438.06] of exciting things
[2438.06 → 2439.60] kind of moving towards the future.
[2439.82 → 2441.84] I saw some of the press releases
[2441.84 → 2443.98] around kind of building,
[2444.34 → 2445.10] involved in,
[2445.18 → 2446.32] in building Israel's
[2446.32 → 2448.66] National Quantum Computing Centre
[2448.66 → 2449.60] and other things.
[2449.60 → 2451.12] As you're kind of looking
[2451.12 → 2453.42] to your next year ahead,
[2453.56 → 2454.82] what are some of those things
[2454.82 → 2456.26] that are really exciting for you
[2456.26 → 2457.78] in terms of how the industry
[2457.78 → 2458.68] is shaping up
[2458.68 → 2460.48] and what your company
[2460.48 → 2461.30] is involved with
[2461.30 → 2462.34] kind of moving
[2462.34 → 2463.74] into the next year or two?
[2464.50 → 2464.74] Yeah.
[2464.92 → 2466.02] So first and foremost,
[2466.22 → 2466.46] I mean,
[2466.50 → 2467.32] I'm just excited
[2467.32 → 2468.92] to be a part of people
[2468.92 → 2470.28] that are trying
[2470.28 → 2471.68] to build these computers,
[2471.82 → 2472.40] these machines
[2472.40 → 2474.24] that are based on,
[2474.24 → 2474.60] you know,
[2474.94 → 2476.46] kind of deep fundamental
[2476.46 → 2477.62] laws of nature
[2477.62 → 2479.46] and would help us
[2479.46 → 2480.50] compute faster
[2480.50 → 2482.02] and also understand
[2482.02 → 2483.28] nature better.
[2483.92 → 2485.26] So that to me
[2485.26 → 2486.26] is the most exciting thing.
[2486.38 → 2487.54] I'm super excited
[2487.54 → 2488.34] that, you know,
[2488.38 → 2488.98] so many people
[2488.98 → 2490.18] are using our products
[2490.18 → 2492.88] to make this field progress.
[2493.02 → 2494.36] So I'm just excited
[2494.36 → 2495.82] for people to use
[2495.82 → 2497.02] more and more products
[2497.02 → 2498.48] and improve them
[2498.48 → 2499.80] so that they could move faster.
[2499.80 → 2501.26] And this is our mission
[2501.26 → 2502.38] at QM is to accelerate
[2502.38 → 2503.18] the realization
[2503.18 → 2504.48] of useful quantum computers.
[2504.66 → 2505.70] So hopefully,
[2505.82 → 2506.60] we're building tools
[2506.60 → 2507.28] that allow people
[2507.28 → 2508.22] to accelerate
[2508.22 → 2509.18] the realization
[2509.18 → 2511.44] of those computers
[2511.44 → 2512.48] and make them useful.
[2513.00 → 2513.58] Other than that,
[2513.62 → 2514.54] I'm super excited
[2514.54 → 2515.74] to see how
[2515.74 → 2516.88] the industry shapes
[2516.88 → 2518.00] because this is a field
[2518.00 → 2519.28] that's in kind of like
[2519.28 → 2520.80] a formation, right?
[2520.88 → 2521.36] The stack,
[2521.64 → 2522.24] the entire,
[2522.42 → 2523.34] the structure
[2523.34 → 2524.64] of the technology stack,
[2524.84 → 2526.86] but also the value chain.
[2526.86 → 2528.40] The value chain is kind of
[2528.40 → 2530.32] where sort of the community
[2530.32 → 2532.02] is defining its value chain
[2532.02 → 2532.52] right now
[2532.52 → 2533.46] and defining itself.
[2533.62 → 2535.10] And this is very exciting
[2535.10 → 2536.72] to be in an industry
[2536.72 → 2537.96] in those early days.
[2538.40 → 2539.78] So I'm super excited
[2539.78 → 2540.66] for that.
[2541.12 → 2541.90] Well, thank you.
[2542.06 → 2542.98] Thank you so much,
[2543.26 → 2543.56] Yonatan,
[2543.70 → 2544.98] for joining us.
[2545.06 → 2546.10] This is really,
[2546.30 → 2546.84] fascinating.
[2547.10 → 2548.26] It's awesome to see
[2548.26 → 2548.86] these practicalities
[2549.64 → 2550.92] of the sort of
[2550.92 → 2552.78] integration layer
[2552.78 → 2554.34] and the hybrid systems
[2554.34 → 2555.28] coming together
[2555.28 → 2557.10] around like real
[2557.10 → 2557.86] scalable,
[2558.44 → 2558.74] you know,
[2558.80 → 2560.26] hardware and platforms.
[2560.64 → 2561.30] So, yeah,
[2561.32 → 2562.42] thank you for all the work
[2562.42 → 2563.02] that you're doing
[2563.02 → 2564.78] and for taking time
[2564.78 → 2565.80] to tell us
[2565.80 → 2566.64] a little bit about it.
[2566.98 → 2567.70] Thank you so much
[2567.70 → 2568.68] for hosting.
[2569.20 → 2569.80] This was great.
[2569.80 → 2579.20] All right.
[2579.36 → 2580.36] That is our show
[2580.36 → 2580.94] for this week.
[2581.20 → 2582.00] If you dig it,
[2582.16 → 2583.56] don't forget to subscribe.
[2584.04 → 2585.96] Head to practicalai.fm
[2585.96 → 2586.76] for all the ways.
[2587.26 → 2588.18] And if Practical AI
[2588.18 → 2589.42] has benefited your life,
[2589.62 → 2590.44] pay it forward
[2590.44 → 2591.38] by sharing the show
[2591.38 → 2591.98] with a friend
[2591.98 → 2592.66] or a colleague.
[2593.02 → 2593.52] Word of mouth
[2593.52 → 2594.64] is the number one way
[2594.64 → 2595.44] people find shows
[2595.44 → 2596.00] like ours.
[2596.40 → 2597.58] Thanks again to Vastly
[2597.58 → 2599.28] for fronting our static assets
[2599.28 → 2600.38] to fly.io
[2600.38 → 2602.10] for backing our dynamic requests
[2602.10 → 2603.52] to Break master Cylinder
[2603.52 → 2604.12] for the beats
[2604.12 → 2605.26] and to you for listening.
[2605.52 → 2606.18] We appreciate you.
[2606.48 → 2607.36] That's all for now.
[2607.56 → 2608.40] We'll talk to you again
[2608.40 → 2609.08] on the next one.
