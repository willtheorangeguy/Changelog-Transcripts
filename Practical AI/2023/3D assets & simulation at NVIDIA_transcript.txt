[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.70]  No ops required.
[34.02 --> 36.08]  Learn more at fly.io.
[42.34 --> 45.34]  Welcome to another episode of Practical AI.
[45.72 --> 47.34]  This is Daniel Whitenack.
[47.44 --> 53.36]  I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[53.36 --> 56.42]  Benson, who is a tech strategist with Lockheed Martin.
[56.42 --> 57.38]  How are you doing, Chris?
[57.72 --> 58.64]  I'm doing good, Daniel.
[58.68 --> 59.28]  How are you today?
[59.96 --> 60.84]  Oh, I'm doing great.
[60.98 --> 66.56]  I had a conversation, I breakfasted on Monday this week with a company from the UK doing
[66.56 --> 70.58]  drones and automated or autonomous drones.
[70.80 --> 75.32]  And I felt very prepared for that because you've talked to me so many times about, you
[75.32 --> 78.00]  know, aeronautics and drones and all that.
[78.10 --> 79.28]  So thanks for your prep.
[79.76 --> 80.58]  No problem.
[80.68 --> 81.78]  Happy to do it, you know?
[82.06 --> 83.24]  Yeah, it was a good breakfast.
[83.24 --> 87.68]  Just think of the universe of possibilities out there, you know, so many things.
[88.00 --> 88.48]  Exactly.
[88.70 --> 88.86]  Yeah.
[88.94 --> 96.54]  Well, speaking of the universe, or I guess rather the omniverse or the metaverse or whatever
[96.54 --> 101.98]  verse you want to think of, we're going to get into all the verses today.
[102.10 --> 103.92]  We're going to be well-versed in those verses.
[104.14 --> 105.44]  Yes, we're going to be well-versed.
[105.50 --> 106.02]  Good stuff.
[106.02 --> 113.84]  We've got with us Beau Perschall, who is the director of Omniverse Sim Data Ops at NVIDIA,
[114.00 --> 117.84]  which I have to say is a really exciting title.
[118.10 --> 120.12]  One of the better ones we've had on the show.
[120.30 --> 121.10]  So welcome, Beau.
[121.36 --> 122.22]  Thank you very much.
[122.28 --> 123.40]  I'm pleased to be here.
[124.06 --> 129.48]  Yeah, I imagine that my title doesn't make a whole lot of sense to just about anybody.
[130.26 --> 131.54]  It's a lot of words.
[131.86 --> 134.64]  I bet it'll make more sense after this conversation.
[134.64 --> 136.26]  Hopefully so.
[136.46 --> 139.66]  I was going to say, you have a whole episode to explain it to us, so we're good.
[141.48 --> 142.20]  Fair enough.
[142.64 --> 146.98]  You know, I guess spinning off of kind of how Chris and I were starting that, it would be
[146.98 --> 152.04]  awesome to hear about, you know, what does Omniverse mean?
[152.04 --> 158.16]  And also maybe a little bit about like your background and how you came to be working on
[158.16 --> 158.82]  Omniverse.
[158.82 --> 165.44]  So this intersection of what I understand, some type of 3D stuff and AI and simulation.
[165.70 --> 167.26]  What was that journey like?
[167.26 --> 170.60]  And how can we understand generally what Omniverse is?
[170.84 --> 171.02]  Sure.
[171.20 --> 174.12]  So Omniverse is NVIDIA software.
[174.38 --> 180.58]  It is our computing platform for building and operating metaverse applications.
[180.58 --> 184.88]  And again, it's not necessarily so theoretical.
[184.88 --> 187.02]  These are like industrial metaverses.
[187.14 --> 193.10]  These are, you know, whether you're designing and manufacturing goods or you're simulating
[193.10 --> 200.18]  your factory of the future or building a digital twin of the planet, which NVIDIA is doing to,
[200.26 --> 202.60]  you know, accelerate climate research.
[203.20 --> 208.26]  Omniverse is a development platform to help with that kind of simulation work.
[208.26 --> 210.54]  And it's doing it in 3D.
[210.88 --> 211.04]  Yeah.
[211.14 --> 216.92]  So it's not just those people without the legs kind of hopping around in a place.
[217.18 --> 218.98]  No, this is very practical.
[218.98 --> 223.00]  As a matter of fact, we have big and small customers that are using it.
[223.38 --> 228.42]  Over 200,000 downloads for Omniverse is a platform that you can get from the NVIDIA site.
[229.02 --> 233.84]  You've got companies like BMW that are using it to plan their factory of the future.
[233.84 --> 236.68]  And part of that is worker safety.
[237.18 --> 238.26]  So they have to have legs.
[238.82 --> 243.26]  You know, you can't simulate the ergonomics of if you're doing a repetitive task, are you
[243.26 --> 245.52]  going to hurt somebody by doing it?
[245.56 --> 250.40]  Or are they in danger of getting, you know, hit by something in a work cell or something
[250.40 --> 251.48]  on the assembly line?
[251.54 --> 257.72]  So there's all sorts of simulation around that kind of information as part of Omniverse.
[257.72 --> 261.34]  But it's a really broad platform.
[261.60 --> 266.98]  You know, it's designed to be extendable so that, you know, customers can come in and
[266.98 --> 268.86]  write their own tools and connectors.
[269.38 --> 272.96]  It's not supposed to be just its own endpoint.
[273.18 --> 279.14]  In other words, we have connectors which are basically bridges to other applications, whether
[279.14 --> 284.56]  you're coming from manufacturing side like Siemens, or you're coming from architectural
[284.56 --> 291.22]  software like Revit, or you're coming from animation software like Blender or Houdini or
[291.22 --> 294.54]  Maya or Unreal for that matter.
[295.14 --> 298.20]  All of that data can be aggregated through USD.
[298.58 --> 304.10]  Universal Scene Description is the file format that Omniverse is based upon, which was a Pixar
[304.10 --> 305.34]  open file format.
[305.78 --> 307.78]  It is very robust.
[308.52 --> 315.12]  And basically, we figure we're the kind of the connective glue between all of these platforms
[315.12 --> 320.90]  so that simulations can be run inside of Omniverse, but all the data can move in and out.
[321.02 --> 323.06]  It's not like captive data.
[323.68 --> 327.64]  Hopefully that gives you a little bit of a background of Omniverse in and of itself.
[328.26 --> 329.68]  It is a visual platform.
[330.26 --> 330.54]  It does.
[330.62 --> 331.62]  That sounds fascinating.
[331.62 --> 336.28]  And as you know from our pre-chat, I know a little bit about Omniverse before coming
[336.28 --> 345.68]  into the conversation, but I know that there is a lot of confusion about how this fits in
[345.68 --> 347.48]  with all the other...
[347.48 --> 351.32]  We were joking in the beginning about the various verses that people are hearing.
[351.44 --> 352.80]  There's a lot of lingo out there.
[353.44 --> 360.36]  And as recently as yesterday, a friend of mine named Kevin texted me, and I haven't replied
[360.36 --> 365.84]  to him yet, but I will have by the time this is aired, texted me saying, I don't understand
[365.84 --> 367.80]  this verse thing, and I know that you're involved in this.
[367.86 --> 368.60]  Can you explain it?
[368.66 --> 372.08]  And I think Kevin represents a lot of people in that way.
[372.50 --> 374.02]  And so could you...
[374.02 --> 374.82]  We've heard Multiverse.
[375.14 --> 376.28]  We've heard Metaverse.
[376.72 --> 377.80]  We've heard now...
[377.80 --> 379.10]  We definitely have heard Omniverse.
[379.10 --> 381.48]  And how does all of...
[381.48 --> 385.76]  Can you give us some context to where how this whole industry fits together so that as we
[385.76 --> 390.94]  dive into Omniverse and back into it in just a moment, we kind of have a sense of where
[390.94 --> 394.12]  it fits within, you know, and some of the other companies.
[394.26 --> 398.26]  We know you're with NVIDIA and you're doing this great work, but we've heard things from
[398.26 --> 402.74]  other big companies, you know, the usual array of social media and cloud companies.
[402.74 --> 404.86]  So can you kind of set the stage for us a bit on it?
[404.86 --> 406.00]  A bit, yes.
[406.16 --> 412.46]  A metaverse is a very loaded term and everybody has kind of their own connotation of what that
[412.46 --> 412.80]  is.
[413.30 --> 422.24]  For NVIDIA, certainly we consider Omniverse a tool, a platform to help enable an industrial
[422.24 --> 424.36]  metaverse, something that is real world.
[424.36 --> 430.46]  Not only that is that can do simulation, but can communicate with the real world and back.
[430.46 --> 435.68]  So there's this kind of bi-directional, you know, messaging that's aspirational for us.
[435.74 --> 441.66]  That's where we want to be able to be so that if you have a production line, you can actually
[441.66 --> 447.98]  understand what's the uptime of the equipment in there and then basically schedule maintenance
[447.98 --> 455.46]  or be able to do factory planning and optimization so that you're getting the most throughput you
[455.46 --> 459.74]  can at any given moment if you have to move materials around a facility.
[459.74 --> 463.52]  Let me ask you a question there just to draw the distinction.
[463.80 --> 467.54]  As you just now were defining it, you kind of said industrial metaverse.
[467.80 --> 473.50]  And I'd like if you would, I know that people are reading things all the time and, you know,
[473.52 --> 476.86]  like there's more of a generic concept of metaverse.
[477.02 --> 481.10]  And then obviously there are certain companies that were formerly known as Facebook that have
[481.10 --> 483.82]  kind of taken the word as a brand in some ways.
[484.22 --> 487.70]  I sense that you were using the more generic version, obviously, of metaverse.
[487.70 --> 492.96]  Could you define what that is, what a metaverse is so that we can kind of understand what the
[492.96 --> 494.84]  omniverse branding of that fits into?
[495.12 --> 495.26]  Sure.
[495.40 --> 499.44]  So the metaverse, again, very overworked term, I think.
[499.74 --> 503.48]  But in general, it's the next evolution of the internet.
[503.48 --> 509.84]  Instead of having connected pages, you'll now have connected living ecosystems, living kind
[509.84 --> 513.24]  of worlds, if you will, that actually can intercommunicate.
[513.24 --> 518.56]  You'll do hopping between those worlds as opposed to just moving between pages.
[518.56 --> 525.64]  So it's all based on kind of this 3D centric, you know, representation of our existence in
[525.64 --> 526.20]  some ways.
[526.42 --> 531.38]  You've seen it, you know, the gaming industry has things like Fortnite and Roblox already
[531.38 --> 535.62]  that are very much kind of persistent, ongoing worlds.
[535.62 --> 543.14]  Um, the metaverse is designed to take that to a much broader level in everything from entertainment
[543.14 --> 544.72]  to business and industry.
[544.72 --> 553.74]  And so NVIDIA is taking their software platform and the hardware that supports it to help real
[553.74 --> 554.58]  world applications.
[554.58 --> 560.32]  I mean, it's why we're building an entire platform essentially around how we start to
[560.32 --> 565.88]  do weather prediction decades into the future called Earth 2 so that we can start to help
[565.88 --> 568.48]  with unlocking the climate as far as that goes.
[569.02 --> 577.26]  We have customers like Ericsson build digital twins of cities so that they could go ahead
[577.26 --> 582.38]  and place cell towers in optimal locations for maximum coverage before they ever deploy
[582.38 --> 583.32]  in the real world.
[583.90 --> 588.96]  So trying to find real world values, that's kind of the distinction between, you know, the
[588.96 --> 594.86]  gaming space and kind of the entertainment or personal spaces that the metaverse can represent
[594.86 --> 598.22]  with meta and different companies that are helping work on that.
[598.36 --> 600.02]  And everyone thinks everyone's competing.
[600.14 --> 602.12]  That's like saying, who's building the internet?
[602.48 --> 602.78]  Fair enough.
[602.88 --> 603.04]  Yeah.
[603.32 --> 608.30]  You know, at some level, it's like, it's going to require all of us cooperating at some level.
[608.30 --> 613.00]  There's so much greenfield as far as this space goes that, yeah, it's really exciting.
[613.38 --> 613.54]  Yeah.
[613.60 --> 618.76]  I really love this sort of parallel that you've given or metaphor of the internet because
[618.76 --> 623.04]  some of the applications that I've heard you talk about, like it's making some connections
[623.04 --> 626.62]  in my brain that's making this maybe a little bit more practical to me.
[626.78 --> 632.58]  So when I think of like the internet generally and what you can do on the internet and what
[632.58 --> 637.42]  has happened with the internet over time, there have been things that happened in the real
[637.42 --> 642.98]  quote unquote real world that kind of had a parallel on the internet, right?
[643.00 --> 646.20]  Like I can go into a bookstore and I can buy a physical book.
[646.20 --> 649.60]  Well, now there's a way for me to do that on the internet.
[649.88 --> 655.50]  But then the internet also had this sort of segment of new things that didn't happen before
[655.50 --> 658.10]  the internet, but now happened because of the internet.
[658.68 --> 664.06]  Would you say it's similar in terms of what you're seeing with the metaverse space, these
[664.06 --> 668.36]  3D worlds and the omniverse in terms of some of what you've talked about, like the cell
[668.36 --> 669.00]  tower thing?
[669.40 --> 673.50]  Like in theory, you could do that in the real world and, you know, learn what you need to
[673.50 --> 678.38]  learn. There's probably cost, you know, advantages to not doing that and that sort of thing.
[678.50 --> 679.74]  But it's a parallel there.
[679.86 --> 683.88]  Is there another set of things like, I don't know if this would fit into the climate modeling
[683.88 --> 687.96]  stuff or other things that you're talking about where you can do, you know, legitimately
[687.96 --> 694.22]  sort of new types of things in this world that maybe we don't know the full extent yet,
[694.22 --> 695.56]  but we're beginning to see those.
[695.72 --> 698.34]  Do you see it that way or you're much more plugged in?
[698.34 --> 704.04]  Absolutely. I certainly see autonomous vehicles, which is another, you know, big industry for
[704.04 --> 710.04]  us with our drive sim platform that's based on omniverse is that if you're trying to simulate
[710.04 --> 717.24]  multiple kinds of traffic situations and different scenarios, a lot of them you can't capture in
[717.24 --> 722.56]  the real world. They're dangerous. You know, what you want to do is be able to train the algorithms
[722.56 --> 729.62]  to react accordingly before you ever get it onto the real world. But you also want to have
[729.62 --> 736.72]  the connectivity so that the way that it's handled is that it doesn't matter if the data coming in is
[736.72 --> 742.64]  synthetic. So the sensors, the LIDAR and radar on the car with hardware in the loop, essentially,
[743.10 --> 748.90]  you're now at that point of saying it can't distinguish whether it's a real world scenario
[748.90 --> 755.50]  or it's a simulation. It treats them both equally. So that sort of thing, I think, is absolutely,
[755.86 --> 760.24]  you know, critical to safety. I think that that also kind of gets to the industrial and the
[760.24 --> 767.08]  manufacturing side of things as well, is that there will be ways to train things in more efficient ways
[767.08 --> 773.36]  as well. So you're saving cost. You're training a robotic arm on a production line for a new task
[773.36 --> 779.36]  instead of having to take that work cell down in the real world, accrue costs while you're going
[779.36 --> 785.64]  through and programming it and testing it. Now you can go in and actually test it and teach it
[785.64 --> 791.34]  essentially in the simulation and then just pass all of that data back to the physical world so that
[791.34 --> 798.06]  the robot now just changes its program pretty much on the fly. That's a huge, huge kind of benefit.
[798.06 --> 803.92]  For a moment, just as we kind of finish up kind of what the ecosystem looks like and you're kind of
[803.92 --> 810.30]  talking about these use cases, I wanted to go back for one second and talk about with both NVIDIA
[810.30 --> 815.44]  and the other organizations that are participating in this with their various solutions, some gaming,
[815.60 --> 822.50]  some not, what does that evolution of a user, if we're going into the future, a short distance,
[822.50 --> 832.00]  and it's becoming commonplace for users to have different destinations in terms of metaverse style
[832.00 --> 837.92]  3D worlds. In the beginning, are they all very distinct and separate, almost like using a separate
[837.92 --> 842.86]  application on your laptop where you close one and you go into another one? Or is there any,
[843.30 --> 848.88]  will it take a while to get to connection between those different types of environments? And what does
[848.88 --> 853.66]  that cross compatibility across multiple environments start to look like?
[853.66 --> 860.84]  I think that's part of why I was hired a year ago was to help kind of solve this. I was hired to
[860.84 --> 868.84]  create a new standard that we call SimReady for 3D content specifically because yes, what you're
[868.84 --> 873.94]  describing is essentially a walled garden kind of approach where everyone's doing their own thing and
[873.94 --> 879.40]  nothing talks to one another and it's all kind of disjointed. And that's not the goal of the
[879.40 --> 886.14]  metaverse. The whole idea of the metaverse is to be interconnected and allow people to move and allow
[886.14 --> 893.84]  data to move. And so with Omniverse being based on a file format called USD, again, universal scene
[893.84 --> 901.22]  description, a very robust format. Now what we're trying to do is understand how to standardize that,
[901.22 --> 907.52]  how to make it so that based on your needs, and this is what's been fascinating for me in the last
[907.52 --> 914.76]  year because I did not come from a data science background. I was a 3D artist for 20 plus years.
[914.94 --> 920.20]  In fact, I learned 3D before the internet was a thing, just to carbon date myself. I, you know,
[920.26 --> 924.80]  had manuals and didn't see my family for months and had to work on super slow computers.
[925.56 --> 931.10]  But we're now getting to a point where interchange is absolutely paramount. So everyone is starting
[931.10 --> 938.08]  to look at it from a very cooperative place. So USD being an open file format, being something that
[938.08 --> 946.38]  is open sourced. We've got, you know, connections to the Academy Software Foundation, which helps try
[946.38 --> 953.18]  and manage standards, the Linux Foundation for Standards. It's a long, hard process to figure out
[953.18 --> 959.60]  what is valuable for everybody. Because as you can imagine, everybody's use cases is different.
[959.60 --> 966.88]  It's, you know, what BMW is trying to do is going to be different than what a watchmaker does or what
[966.88 --> 972.82]  Ericsson is doing or what autonomous vehicle manufacturers are trying to handle directly.
[973.40 --> 979.96]  And what we're trying to do with SimReady is build this framework that allows SimReady to have
[979.96 --> 985.96]  flexibility based on your needs. If you're doing synthetic data generation where you need thousands
[985.96 --> 992.60]  and thousands of images to identify what a car is, that's one need. So you need semantic labeling.
[992.92 --> 1000.16]  You need something in the data in that 3D model that says, I am a car. Fairly simple, but you can get
[1000.16 --> 1006.72]  very specific even within a single 3D model. These are the tires. These are the doors. This is the windshield.
[1006.72 --> 1014.00]  And you can start to semantically label more and more granularly based on your needs. I've been dealing
[1014.00 --> 1022.12]  for just under a year trying to learn what is important. And it's like drinking from the fire hose.
[1022.28 --> 1028.44]  Everybody has different needs. Daniel, I assume being a data scientist that you have very specific
[1028.44 --> 1037.48]  needs for the kinds of data that you are processing and how you want that data organized is somewhat
[1037.48 --> 1045.54]  different than an NVIDIA researcher might need. So instead of trying to funnel people into one
[1045.54 --> 1052.98]  workflow, we're trying to make sure that SimReady becomes this living, breathing organism that must evolve
[1052.98 --> 1061.28]  over time and has that flexibility so that, you know, we're providing the planter and the soil and
[1061.28 --> 1067.26]  saying, plant your tree. Here's how you do it so that you can customize it to your own needs. Again,
[1067.34 --> 1075.18]  another practical example is with SimReady, specifically a piece of content right now has semantic labels.
[1075.52 --> 1081.18]  And what was shocking when I got here was finding out that our research scientists, I was like,
[1081.18 --> 1085.46]  well, what semantic labels are you using right now? What's your taxonomy? How are you identifying
[1085.46 --> 1091.74]  things? And what's coming with those data sets? And they're like, we get nothing. It's like, what?
[1092.50 --> 1097.96]  Yes, they are basically having to kind of like from whole cloth, create their own semantic label
[1097.96 --> 1103.50]  taxonomies. I'm like, well, that's crazy. But what taxonomy would you like to use? And they're like,
[1103.58 --> 1107.56]  well, everybody was kind of a little bit different. And so it's like, okay, what do we do there?
[1107.56 --> 1115.16]  So there's kind of the starting point. And in terms of a simple taxonomy that will allow people to
[1115.16 --> 1121.44]  identify the car, but some people want to call it a car. Some want to call it an automobile. Some
[1121.44 --> 1125.92]  want to call it, if you're a French researcher, you might call it a voiture. If my high school French,
[1126.02 --> 1130.54]  if I remember it correctly, it's like, how do you kind of synchronize all those? And it's like,
[1130.54 --> 1136.86]  you're crazy if you try. So essentially what we've done is we're building a framework and a reference
[1136.86 --> 1142.76]  implementation to be that planter so that we can say, here's how you can implement it for your
[1142.76 --> 1148.40]  specific needs. And what data do you want to manage? Do you want physics? Do you want to have
[1148.40 --> 1154.12]  rigid body physics on the objects right now? Great. We can go ahead and add those. You know,
[1154.14 --> 1159.52]  we have that as part of PhysX that is built into the Omniverse platform. So when I said simulation,
[1159.52 --> 1165.64]  it can do collisions and collision detection, but there's more. When you think about building digital
[1165.64 --> 1171.62]  twins, you're trying to represent the real world as accurately as possible. And that is an endless
[1171.62 --> 1177.28]  quest, which is why it has to evolve over time. We'll build stuff now, but in the future, we'll have
[1177.28 --> 1184.02]  more sophisticated electromagnetic materials that have thermal properties and have sonic properties
[1184.02 --> 1190.44]  and have, you know, deformation, you know, tensile strength and things like that, that we'll want to build
[1190.44 --> 1197.54]  in so that the simulation can actually process it. So it is a, you know, the rest of my life's work.
[1197.54 --> 1202.66]  And then some, I think, you know, it's going to continually evolve. So what we're trying to do
[1202.66 --> 1209.88]  right now is in the very early days, set the standard up that it does have that ability to kind of breathe
[1209.88 --> 1216.14]  and move along as we get more sophisticated. Well, Bo, I love how you kind of brought, um,
[1216.14 --> 1221.08]  what to me is honestly a little bit of an intimidating subject, which is this whole
[1221.08 --> 1227.60]  area of 3d. And, you know, I'm sure, uh, you have a different perspective, you know, coming from the
[1227.60 --> 1233.48]  art world, but I'm very much, let's just say I shouldn't design any sort of applications that
[1233.48 --> 1239.62]  human should humans look at with their eyes. I'm not that kind. I don't have that skill. Um,
[1239.70 --> 1244.68]  so it's, it's a little bit intimidating for me to think about these spaces, but I think the
[1244.68 --> 1251.22]  practicality that you just described around, you know, I can definitely see even applications.
[1251.66 --> 1256.12]  I don't work in manufacturing, but I can see those, but even in my own space, you know, I work in
[1256.12 --> 1261.66]  natural language processing and language. And of course, a big area that is, is really, um,
[1262.04 --> 1269.24]  neglected in the NLP spaces, sign language, which by its very nature is a 3d thing, right? A lot of
[1269.24 --> 1273.34]  people might think, Oh, it's just like, you know, hands and you can look from one direction. Well,
[1273.34 --> 1280.22]  there's gestures, there's facial, uh, movement, there's 3d movement that happens with sign language.
[1280.22 --> 1287.52]  And, um, you know, if you want to, for example, have an avatar where you could, you know, type
[1287.52 --> 1293.36]  something in and the avatar, you know, signed in American sign language or Japanese sign language
[1293.36 --> 1299.74]  or something that that's a 3d environment and would require certain labels, right? Around,
[1299.74 --> 1305.70]  you know, facial features and hands and all of those things. So all of that really connects with
[1305.70 --> 1311.88]  me. Well, I'm wondering if you could kind of break down this, uh, SIM ready, um, project that you've
[1311.88 --> 1318.44]  been working on and maybe think about it from the perspective of, let's say I am a manufacturer.
[1318.44 --> 1324.76]  I'm coming into the space. I want to kind of figure out, like you say, you've got the planners ready.
[1324.76 --> 1330.32]  What does it look like for me to come into the space and think about, you know, my use case and
[1330.32 --> 1338.06]  then map that onto SIM ready, the standard and the file formats and the, and the 3d space. What,
[1338.14 --> 1342.34]  what sort of required for me to enter that space as it stands now?
[1342.52 --> 1349.40]  That's a great question because a lot of people understand is 3d is still very hard to achieve
[1349.40 --> 1356.70]  in any kind of degree of fidelity and omniverse is trying to help create the highest visual fidelity
[1356.70 --> 1364.30]  on top of simulation fidelity possible. So that kind of pyramid of what it takes to build 3d content
[1364.30 --> 1371.86]  in the first place is still difficult, even with photogrammetry and the new, uh, nerf technologies
[1371.86 --> 1376.08]  and things that can help start to capture that. And those are going to evolve. And we, you know,
[1376.08 --> 1382.64]  Nvidia being an AI company is certainly pushing into those areas to make it easier for kind of this
[1382.64 --> 1393.58]  art asset acquisition. But in terms of what it takes right now is, well, let me back up here.
[1394.18 --> 1401.96]  I'm kind of front running myself in my head is that, um, essentially with 3d being difficult,
[1401.96 --> 1408.24]  it's hard for kind of anyone to come in and just have a data set and be able to do a lot with it.
[1408.80 --> 1414.66]  I've never taken an animation class or anything. So you're working with that sort of clay.
[1414.96 --> 1422.06]  That's okay. Neither have I, right. You know, essentially it's adding the value on top of the
[1422.06 --> 1428.26]  art asset. So if you're a manufacturer or if you're doing sign language, one, you have to have the asset
[1428.26 --> 1435.94]  library and, you know, ML researchers and data scientists have a voracious appetite for content
[1435.94 --> 1442.50]  because you can't have just one thing to train against. It is thousands or tens of thousands for,
[1442.62 --> 1450.80]  for humans, it's diversity, not, you know, just in terms of age and ethnicity and sex and,
[1450.80 --> 1457.98]  you know, clothing and look and facial. I mean, it's endless there just to be able to train the model
[1457.98 --> 1465.10]  you know, with as little bias as humanly possible. The same thing for any other kind of research where
[1465.10 --> 1471.20]  you're using 3d. I had a researcher ask me early on when I first started, can I get everything you
[1471.20 --> 1477.00]  find in a garage? I was like, no, that's an unbounded question. You, we had, let's focus.
[1477.14 --> 1481.20]  What do you want? Is it, you know, are you, there's a lot of strange garages out there.
[1481.20 --> 1487.18]  Exactly. Am I a woodworker? Am I a mechanic? Am I a hoarder? Is it my garage? Who's,
[1487.32 --> 1493.12]  all of that kind of comes into play as to kind of like focusing down on first, what is the data set
[1493.12 --> 1499.82]  consist of? And then what metadata is important for the use case? So that's really kind of where
[1499.82 --> 1506.12]  SimReady starts to differentiate is it says, okay, now that I've got this data set, what adds the value
[1506.12 --> 1512.60]  to it from this set of tooling that we're building also on top of Omniverse so that at the end of the
[1512.60 --> 1520.24]  day, I can take beautiful art assets, stuff that has no metadata for simulation or for AI at all,
[1520.98 --> 1527.46]  be able to push them through this tooling to add semantic labels, to add physics, to add physical
[1527.46 --> 1534.28]  materials, to add all of the kinds of things that matter to the dimensions of the object, whatever other
[1534.28 --> 1541.26]  kinds of metadata are important to that customer, and then be able to validate it and export it so
[1541.26 --> 1548.34]  that now you've got a data set that a data scientist can consume directly, practically, without having to
[1548.34 --> 1554.62]  spend their life trying to figure out how they add the value on their own. So that's weird because at the
[1554.62 --> 1561.36]  end of the day, I don't think NVIDIA envisions themselves or me having a team build all the content in
[1561.36 --> 1568.04]  the world for people. We want to enable all of the suppliers for BMW, the Siemens and Kukas and,
[1568.16 --> 1575.30]  you know, companies like that who build infrastructure and build content to also embrace the idea of SimReady
[1575.30 --> 1582.44]  and the tooling so that all of that content just plays nicely together. And then again, it flows into
[1582.44 --> 1589.12]  and out of other simulation platforms. So if you're pushing it somewhere else, it's a USD file. So that data is
[1589.12 --> 1596.20]  available to you, regardless of what platform you're using it within. So that's really kind of the benefit there.
[1596.20 --> 1602.86]  I just would like to extend exactly what you just said. Could you give us, and we often will ask guests
[1602.86 --> 1607.82]  just to kind of give us a nice clarifying way, like what you just said is you described the concepts
[1607.82 --> 1613.30]  of going through that process. Could you give us either a fictional or a real world, whatever works
[1613.30 --> 1619.18]  for you, and I suspect you probably have one ready to go, of like pick a manufacturer or whatever you
[1619.18 --> 1623.78]  want and kind of walk us for a moment at a high level through the steps of what they're doing,
[1623.78 --> 1629.20]  where you reference Omniverse, you reference SimReady, you reference the things in context,
[1629.62 --> 1635.08]  in a use case, so that we kind of follow your footsteps through that. And it kind of brings
[1635.08 --> 1639.74]  the concepts into a very tangible, you know, touchable kind of understanding.
[1640.34 --> 1645.82]  Right. So we actually have a project ongoing right now, and I can't mention who, but essentially
[1645.82 --> 1655.14]  there is a pick and place robotic arm on a conveyor system that actually has sensors to indicate where
[1655.14 --> 1661.62]  parts are on that platform at any given moment. And what they want to be able to do is build that
[1661.62 --> 1669.30]  simulation inside of Omniverse so that both the simulation can drive and time the real world
[1669.30 --> 1675.18]  application and the real world application can report back so that there is this kind of cyclical nature
[1675.18 --> 1681.46]  of having data moving both ways. So it is, you know, a feeder drops, you know, a part onto the
[1681.46 --> 1687.10]  conveyor belt. The system always knows where it is. It can count it. It can track where it is on the, in the
[1687.10 --> 1692.04]  process when the arm is supposed to pick it up. It knows how to do that and move it into the right
[1692.04 --> 1699.16]  location. Those are the kinds of use cases where now if you have SimReady content that knows it can
[1699.16 --> 1705.44]  identify itself, this is a package, this is a conveyor, this is, you know, this part of Omniverse
[1705.44 --> 1712.22]  can trigger when the real light sensor is tripped and be able to understand that as a, hey, this is
[1712.22 --> 1718.58]  where this product should be. So if the simulation or the real world is off, they can adjust on the fly
[1718.58 --> 1726.62]  so that now you've got kind of this self-fueling round trip ability to track content that way.
[1726.62 --> 1734.92]  So is it fair to say like you would take assets, 3D assets, and you would apply USD, the universal
[1734.92 --> 1743.24]  scene descriptor to it to give it the context so that it is quote unquote SimReady and you can use
[1743.24 --> 1749.52]  the SimReady tools on those assets to do whatever it is you're doing? Right. USD is actually the file
[1749.52 --> 1756.60]  format. I mean, but it's more than that. So in most applications now either export USD directly,
[1756.62 --> 1761.92]  just like you would if you're working in a CAD application, you might export a DWG file or a
[1761.92 --> 1768.38]  DXF file or something like that, or a SOLIDWORKS part file. If you're in manufacturing, you can now
[1768.38 --> 1774.14]  export USD directly in many of these apps. They're all starting to get on board, which is great for
[1774.14 --> 1781.68]  the 3D industry because I can tell you that when I was coming up, every 3D app, every tool had its own
[1781.68 --> 1788.86]  3D file format. And so nothing played well together. It was always a nightmare to try and get content from
[1788.86 --> 1798.24]  one place to another without question. It wasn't like 2D imagery where a pixel is a pixel. 3D is much
[1798.24 --> 1805.26]  more complex as far as that goes, orders of magnitude. And so now that we all have, we're starting to kind
[1805.26 --> 1811.72]  of hone in on USD as a primary file format with technically there's another file format that's
[1811.72 --> 1818.56]  open that's run by the Kronos group called GLTF. And it is essentially a web standard for 3D. And I was
[1818.56 --> 1826.52]  part of the group that was helping kind of define the standard for 3D commerce so that you could see
[1826.52 --> 1830.94]  things on your Apple phone and spin them around in the websites and things like that as well. So that's
[1830.94 --> 1836.76]  kind of the JPEG version of the 3D while the USD file is more like a layered Photoshop file, much more
[1836.76 --> 1842.46]  robust, but they play very well together. And Omniverse supports both of them too. So this is
[1842.46 --> 1850.06]  great. So one of the things that you mentioned briefly, Beau, which I think is really a fascinating
[1850.06 --> 1858.06]  topic, but also a really important topic for the future of sort of practical artificial intelligence,
[1858.06 --> 1865.02]  machine learning is the idea of simulated data. Now you kind of briefly mentioned this topic of,
[1865.02 --> 1872.34]  you know, creating 3D worlds, all the file formats and the things that are needed to label those to
[1872.34 --> 1878.74]  make them useful for data scientists. You talked about the example of kind of digital twin running in
[1878.74 --> 1886.08]  parallel with the real world robot arm. Could you set the context now for usage of this technology
[1886.08 --> 1893.16]  for synthetic data production? And from your perspective, where you've seen people do that,
[1893.26 --> 1899.34]  maybe a couple examples successfully, and maybe help people understand what synthetic data means and why
[1899.34 --> 1908.56]  it might be useful? Sure. So synthetic data, as far as I have been involved, is essentially generating
[1908.56 --> 1915.46]  randomized, what we call domain randomization, taking lots of objects, randomly placing them
[1915.46 --> 1922.92]  in scenes with all of their labels in place so that you can train machine learning for computer vision
[1922.92 --> 1931.44]  to be able to identify, you know, something in a room or in a space or in an environment. So it doesn't
[1931.44 --> 1938.90]  matter what the lighting conditions are. It doesn't matter what the material is. It doesn't matter the
[1938.90 --> 1945.56]  orientation of the model. It could be upside down in some arbitrary orientation. But at the end of the
[1945.56 --> 1952.66]  day, when you have that image, or that sequence, video sequences, or whatever that does all of this,
[1953.00 --> 1958.48]  the computer algorithm can always pick out whatever that piece is. We have a version of our CEO,
[1958.74 --> 1964.16]  Jensen, and we call him Toy Jensen. And there's a little 3D model, toy model. You've probably seen him
[1964.16 --> 1971.54]  in our GTC talks and keynotes. And they wanted to do kind of a where's Waldo for SDG for him as well,
[1971.54 --> 1977.58]  just to be able to train where is he in a scene with all sorts of other random 3D content. And so
[1977.58 --> 1983.06]  that you would change lighting, you would change materials, you would change the orientations of
[1983.06 --> 1988.70]  everything to train the algorithm to be able to spot Toy Jensen, no matter where he was in the scene,
[1988.70 --> 1996.62]  how much he was obscured by blocks or sofas or things like that. From a more practical standpoint,
[1997.40 --> 2002.92]  think about what furniture manufacturers are trying to do today with augmented reality.
[2003.86 --> 2009.70]  You know, they want to be able to scan your room. They want to eventually say, I know that that's a
[2009.70 --> 2015.60]  sofa, and that's a chair, and that's a table. And I want to be able to replace it with my stuff
[2015.60 --> 2022.26]  instead and show you what my stuff looks like in your space. And so having that computer vision
[2022.26 --> 2030.02]  trained against a huge variety of content now gives their algorithms the ability to
[2030.02 --> 2035.18]  kind of find and identify that stuff with high accuracy or, you know, good fidelity.
[2035.68 --> 2040.26]  I just wanted to say tongue in cheek that I think finding Jensen is not as hard as you say,
[2040.26 --> 2046.12]  because he always has his trademark motorcycle jacket on. I'm just saying, it's like, it's always the
[2046.12 --> 2051.86]  jeans and the motorcycle jacket. So he does indeed. They actually put him in the midst of all of our
[2051.86 --> 2057.36]  marbles content, the real time sequence that they put together for a real time demo for GTC
[2057.36 --> 2062.82]  two years ago, and there's hundreds of elements. And so he would get pretty obscured where you
[2062.82 --> 2067.70]  couldn't see either his jeans or his jacket. Okay, fair enough. And you would see like a part of his
[2067.70 --> 2072.10]  gray hair and that would be about it. Gotcha. Some fascinating stuff. You know, from what I'm
[2072.10 --> 2078.16]  trying to do with AI, just to kind of circle this all back around to SimReady, is that AI is important
[2078.16 --> 2085.36]  for SimReady in the future too. I mean, again, just starting less than a year in. But my vision is to
[2085.36 --> 2091.14]  work with our data researchers as well. So that at the end of the day, instead of having a tool that you
[2091.14 --> 2097.68]  manually have to process content with, why wouldn't our SimReady tools live in the cloud as a
[2097.68 --> 2103.78]  service for people to upload their content and doesn't matter how materials are named? Is it
[2103.78 --> 2109.86]  named metal? Is it named wood? Ideally, AI would help us identify what that material should be
[2109.86 --> 2116.02]  to name it properly and then do semantic labeling on it and be able to apply the right physics.
[2116.02 --> 2121.70]  I mean, so that you could upload your library. No one has to get involved. The system now can
[2121.70 --> 2127.56]  process your library, give you a dashboard and your data set that is now valuable. That's my
[2127.56 --> 2133.28]  long-term vision specifically for AI for SimReady. I'd like to ask you, and part of this just comes
[2133.28 --> 2138.96]  from the kind of the, you know, I work for a company that has to deal with edge scenarios that
[2138.96 --> 2144.00]  are adversarial and challenging in all sorts of ways. And so I'm always going to that. One of the
[2144.00 --> 2148.54]  things I'm always curious about is as we look at simulation and, you know, built on the larger
[2148.54 --> 2154.70]  cloud approach that we've been doing for the last 20 years, 15 years, I guess now, as you move
[2154.70 --> 2160.38]  these capabilities and you're talking about having 3D assets, you're doing augmented reality and you
[2160.38 --> 2164.60]  want to be able to merge those, as you mentioned, like with the room with your own stuff, but there's
[2164.60 --> 2169.22]  an infinite number of variations there that we could talk about from a use case standpoint.
[2169.72 --> 2175.20]  As you get out and you're doing things that are away from the cloud, you either don't have
[2175.20 --> 2182.40]  enough bandwidth to get all the GPU computation, you know, from the cloud back to where you are out in
[2182.40 --> 2187.12]  Everest-based camp because the, you know, that actually probably does have enough of an internet
[2187.12 --> 2192.20]  connection. But let's say you're up in camp two and you're doing something in a fairly remote region.
[2192.50 --> 2200.26]  How do you envision these starting to merge into that in terms of being able to have a consequential
[2200.26 --> 2205.98]  user experience, you know, something that's impactful in terms of augmented reality where you're combining
[2205.98 --> 2212.18]  all of these 3D assets that are SIM ready and it's merging with your world when you don't have
[2212.18 --> 2218.14]  bandwidth and cloud assets immediately available due to technical limitations and the, how is NVIDIA
[2218.14 --> 2223.72]  thinking about, because I know you want it to be everywhere. So how are you thinking about bringing
[2223.72 --> 2229.18]  this future that we're all hurtling toward and that you're inventing into those spaces that are not
[2229.18 --> 2233.26]  just, I'm on a gigantic internet connection sitting in my office doing my thing.
[2233.26 --> 2240.02]  Right. I mean, certainly NVIDIA wants things to live in the cloud as much as any company at this
[2240.02 --> 2244.62]  point. And it's been, you know, Jensen publicly announced that in the keynote for GTC this past fall.
[2245.08 --> 2252.68]  And having kind of that unique position of having hardware and software with our GPUs and the
[2252.68 --> 2259.34]  Omniverse platform give us some distinct advantages where you can actually do quite a bit from your own
[2259.34 --> 2265.90]  small workstation in terms of streaming content and how we might do that in the future. Honestly,
[2266.04 --> 2271.54]  I don't know, you know, to be completely fair, I don't know what that looks like at this point.
[2271.54 --> 2277.98]  You know, I'm only a year old here. So I would argue that NVIDIA is very well positioned for answering
[2277.98 --> 2283.14]  that question because you're not strictly a hundred percent in the cloud. You there's a, I have bought
[2283.14 --> 2288.18]  products from you that I can go place into a computer that is not in the cloud or that may have a
[2288.18 --> 2293.50]  connection, but I'm doing the GPUs out on the edge. You have a whole, a large product line of things.
[2293.56 --> 2296.84]  So I do think that you're well positioned for that, but I think it's a fair answer to say,
[2296.92 --> 2300.84]  I don't know because we're moving fast and you know, what's the cliche?
[2301.22 --> 2306.34]  It is still early days. There's no question. And it, there's going to be a lot of evolution. I know
[2306.34 --> 2312.72]  that, you know, what we're focusing on this year as a company is awe-inspiring and I can't wait to see
[2312.72 --> 2318.52]  how we progress throughout the next 12 months or 11 months now, um, to get closer to those goals.
[2318.52 --> 2323.60]  So it's, there is a lot to be done, but yeah, I don't know.
[2324.14 --> 2329.88]  As you do look to the future of, you know, your own work and what NVIDIA is doing, but maybe also
[2329.88 --> 2335.88]  like, you know, now that you're in this space of 3d and interfacing with data scientists, thinking about
[2335.88 --> 2341.46]  how that can influence AI, how AI could help you build the things that you're doing, you know,
[2341.46 --> 2346.90]  what's on your mind as you're looking towards the future, um, what excites you, what, uh, sorts of
[2346.90 --> 2351.66]  opportunities really keep you up at night and really keep you thinking about, you know, the potential in
[2351.66 --> 2356.74]  this space. I know that, you know, you mentioned your background in art and of course this last year
[2356.74 --> 2364.10]  has been an amazing year in terms of the generative capabilities of AI. And, you know, that even sparks
[2364.10 --> 2368.48]  things in my mind about how the things you're working on in 3d, you know, interface with that
[2368.48 --> 2372.84]  sort of generative capability. What are you thinking about? What's, uh, what are you looking forward to
[2372.84 --> 2378.34]  as you're moving forward? For me, one, there's almost nothing to not be excited about, including
[2378.34 --> 2385.34]  generative AI. But for me, it's when it comes to SimReady and kind of my focus is really the
[2385.34 --> 2393.42]  sophistication of what we're trying to achieve with AI. It's starting to kind of understand the, you know,
[2393.42 --> 2399.16]  what the value is today and how you start to extend it forward so that we can start to extrapolate
[2399.16 --> 2405.44]  out much further forward, building that bi-directional communication between the simulated
[2405.44 --> 2412.24]  world and the real world. Wow. Cannot wait to see how that starts to really kind of manifest where
[2412.24 --> 2418.68]  you have data cleanly flowing both ways and things start to synchronize so that you're not just
[2418.68 --> 2423.52]  simulating at this point. You are now kind of replicating things that way. I think that's huge.
[2423.80 --> 2430.00]  And I'm, you know, I was lucky enough to be around when 3d first kind of went mainstream where you could
[2430.00 --> 2437.02]  have computer PCs, consumer PCs, instead of, you know, $50,000 workstations that could do 3d,
[2437.42 --> 2443.92]  you know, and with AI, I feel like we're kind of in that similar early phase of creation and
[2443.92 --> 2450.34]  understanding so that there is just this enormous green field in front of us to kind of explore.
[2450.78 --> 2454.90]  And it's going to take all of us too. It's not just NVIDIA. I want to make that clear. It's like
[2454.90 --> 2460.72]  we're focusing on things that we feel we have distinct advantages on, but we need collaborators.
[2460.94 --> 2466.22]  Again, it's back to the adage of how do you build the internet with a lot of people, a lot of cooperation.
[2466.82 --> 2471.46]  There's so much opportunity across the board that we've all got to kind of pull together and do it.
[2471.46 --> 2477.16]  Awesome. Well, I think that's a super inspiring and encouraging way to close things out. It's
[2477.16 --> 2481.22]  been an awesome conversation, Beau. Really appreciate you taking time to talk about
[2481.22 --> 2485.44]  all the things that NVIDIA is doing in this space and the things that you're working on around
[2485.44 --> 2491.10]  standardization and making things useful and practical for people like myself and Chris. And
[2491.10 --> 2493.68]  yeah, thank you so much for your work and your contributions.
[2494.14 --> 2497.18]  Thank you guys for having me. This has been a blast. I've enjoyed it thoroughly.
[2501.46 --> 2512.96]  Thank you for listening to Practical AI. Your next step is to subscribe now, if you haven't already.
[2513.40 --> 2518.28]  And if you're a longtime listener of the show, help us reach more people by sharing Practical AI
[2518.28 --> 2523.32]  with your friends and colleagues. Thanks once again to Fastly and Fly for partnering with us to
[2523.32 --> 2529.18]  bring you all Change Talk podcasts. Check out what they're up to at Fastly.com and Fly.io.
[2529.18 --> 2534.92]  And to our Beat Freakin' Residents, Breakmaster Cylinder for continuously cranking out the best beats in the biz.
[2535.18 --> 2537.52]  That's all for now. We'll talk to you again next time.
[2537.52 --> 2547.52]  Game on!
[2547.52 --> 2550.52]  Game on!
[2550.52 --> 2551.24]  Game on!
