[0.00 --> 10.06]  Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 --> 11.46]  and accessible to all.
[11.84 --> 14.48]  If you like this show, you will love The Change Log.
[14.70 --> 19.52]  It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 --> 21.38]  talk show for your weekend enjoyment.
[21.84 --> 25.82]  Find us by searching for The Change Log wherever you get your podcasts.
[25.82 --> 28.32]  Thanks to our partners at Fly.io.
[28.70 --> 31.08]  Launch your AI apps in five minutes or less.
[31.40 --> 33.32]  Learn how at Fly.io.
[35.38 --> 36.34]  What's up, nerds?
[36.42 --> 39.68]  I'm here with Kurt Mackey, co-founder and CEO of Fly.
[40.06 --> 41.12]  You know we love Fly.
[41.62 --> 44.30]  So, Kurt, I want to talk to you about the magic of the cloud.
[44.94 --> 45.72]  You have thoughts on this, right?
[46.08 --> 46.28]  Right.
[46.62 --> 51.20]  I think it's valuable to understand the magic-minded cloud because you can build better features
[51.20 --> 53.34]  for users, basically, if you understand that.
[53.34 --> 57.60]  You can do a lot of stuff, particularly now that people are doing LLM stuff, but you can
[57.60 --> 60.26]  do a lot of stuff if you get that and can be creative with it.
[60.70 --> 65.54]  So, when you say clouds aren't magic because you're building a public cloud for developers
[65.54 --> 69.80]  and you go on to explain exactly how it works, what does that mean to you?
[70.14 --> 72.42]  In some ways, it means these all came from somewhere.
[72.64 --> 76.82]  Like, there was a simpler time before clouds where we'd get a server at Rackshack and we'd
[76.82 --> 83.70]  put SSH or Telnet into it even and put files somewhere and run the web servers ourselves to
[83.70 --> 84.72]  serve them up to users.
[85.12 --> 86.96]  Clouds are not magic on top of that.
[87.02 --> 90.94]  They're just more complicated ways of doing those same things in a way that meets the
[90.94 --> 92.88]  needs of a lot of people instead of just one.
[93.04 --> 97.34]  One of the things I think that people miss out on, and a lot of this is actually because
[97.34 --> 101.46]  AWS and GCP have created such big black box abstractions.
[101.76 --> 103.52]  Like, Lambda is really black boxy.
[103.52 --> 105.88]  You can't pick apart Lambda and see how it works from the outside.
[106.04 --> 107.76]  You have to sort of just use what's there.
[107.96 --> 110.30]  But the reality is, Lambda is not all that complicated.
[110.50 --> 115.42]  It's just a modern way to launch little VMs and serve some requests from them and let
[115.42 --> 120.00]  them kind of pause and resume and free up physical compute time.
[120.42 --> 124.24]  The interesting thing about understanding how clouds work is it lets you build kind of features
[124.24 --> 125.86]  for your users you never would have expected.
[125.86 --> 130.26]  And our canonical version of this for us is that when we looked at how we wanted to isolate
[130.26 --> 134.84]  user code, we decided to just expose this machines concept, which is a much lower level
[134.84 --> 137.88]  abstraction of Lambda that you could use to build Lambda on top of.
[138.00 --> 143.04]  And what machines are is just these VMs that are designed to start really fast or designed
[143.04 --> 147.42]  to stop and then restart really fast or designed to suspend sort of like your laptop does when
[147.42 --> 150.12]  it closes and resume really fast when you tell them to.
[150.12 --> 154.32]  And what we found is that giving people those primitives is actually, there's like new apps
[154.32 --> 160.40]  being built that couldn't be built before, specifically because we went so low level and made such a
[160.40 --> 164.50]  minimal abstraction on top of generally like Linux kernel features.
[164.84 --> 169.52]  A lot of our platform is actually just exposing a nice UX around Linux kernel features, which
[169.52 --> 170.82]  I think is kind of interesting.
[170.82 --> 174.12]  But like you still need to understand what they're doing to get the most use out of them.
[174.12 --> 174.84]  Very cool.
[175.00 --> 175.22]  Okay.
[175.38 --> 181.72]  So experience the magic of Fly and get told the secrets of Fly because that's what they want
[181.72 --> 182.14]  you to do.
[182.14 --> 186.54]  They want to share all the secrets behind the magic of the Fly cloud, the cloud for productive
[186.54 --> 189.16]  developers, the cloud for developers who ship.
[189.46 --> 192.66]  Learn more and get started for free at fly.io.
[192.94 --> 194.90]  Again, fly.io.
[212.14 --> 215.90]  Welcome to another episode of the Practical AI Podcast.
[216.28 --> 217.12]  I'm Chris Benson.
[217.36 --> 220.92]  I'm a principal AI and autonomy research engineer at Lockheed Martin.
[221.54 --> 225.76]  And with me today, I have two guests that are going to join in the conversation.
[225.98 --> 227.36]  They are both from BlackBerry.
[227.92 --> 234.26]  One is Gregory Richardson, who is vice president and global advisory CISO at BlackBerry.
[234.46 --> 237.60]  And there's also Ismael Valenzuela.
[237.78 --> 238.66]  Did I get that correct?
[238.66 --> 239.14]  Yes.
[239.14 --> 239.88]  Thank you, Chris.
[240.90 --> 242.68]  And I normally have Daniel for that.
[243.30 --> 247.48]  And he is vice president of threat research and intelligence at BlackBerry.
[247.64 --> 248.88]  Gentlemen, welcome to the show.
[249.02 --> 250.12]  Thank you so much for joining.
[250.52 --> 251.62]  Honor to be here, Chris.
[251.68 --> 252.08]  Thank you.
[252.52 --> 253.12]  Thank you, Chris.
[253.42 --> 254.68]  Really glad to have you.
[255.38 --> 261.84]  We're going to talk today all about security and threats and issues like that.
[261.84 --> 267.16]  I know that there's a blog post to get us started, and I'll let you guys kind of take
[267.16 --> 274.32]  it from there, that you have on the BlackBerry blog that was the AI standoff attackers versus
[274.32 --> 274.92]  defenders.
[275.74 --> 280.32]  And I know Daniel was the first person to see it and said, we got to get these guys on the
[280.32 --> 280.54]  show.
[280.68 --> 282.88]  And then ironically, he is not able to get here today.
[283.28 --> 285.14]  And I know he's disappointed about that.
[285.14 --> 292.16]  But wanted to kind of start off and kind of, can you tell us a little bit about the topic
[292.16 --> 297.00]  in general before we dive into the specifics and the landscape and who does it affect and
[297.00 --> 298.00]  why should they care?
[298.24 --> 301.22]  So maybe it has to do a little bit with our backgrounds as well, right?
[301.24 --> 304.22]  So I cannot really say I'm an expert in AI.
[304.38 --> 305.98]  Well, I cannot really say I'm an expert on anything.
[306.08 --> 310.46]  And the more I spend time in this industry, the less you feel you know, right?
[310.46 --> 315.86]  But I can say my career has been mostly dedicated to cyber defense.
[316.14 --> 320.98]  I started on the offensive side, but then I quickly moved into the, well, not quickly,
[321.08 --> 323.94]  but over years, I moved into the defensive side.
[324.26 --> 327.86]  So I've seen both sides, and I still like to, you know, pick on the offensive side to
[327.86 --> 328.74]  learn from it.
[328.76 --> 331.12]  I call that think red, act blue, right?
[331.18 --> 333.60]  Think as an attacker to become a better defender.
[334.18 --> 339.34]  So obviously, when I was writing about this, I had to bring the AI flavor to it.
[339.34 --> 344.70]  Like, is it really, is AI going to represent an advantage to attackers or defenders?
[344.96 --> 346.78]  And we usually get that question.
[347.42 --> 350.52]  So I wrote this from a cyber defense perspective, right?
[350.66 --> 352.28]  And that's what you see there.
[352.96 --> 358.64]  So before we dive fully into the article, what was driving the need?
[358.74 --> 359.44]  What are you seeing?
[359.52 --> 364.84]  You guys, both at BlackBerry, there's clearly a need driving, addressing cyber.
[364.84 --> 369.42]  Tell us a little bit about how you see the lay of the world from a cyber standpoint,
[370.00 --> 374.40]  and what it is that, you know, what's the problem you're trying to solve in the large?
[375.12 --> 375.34]  Yeah.
[375.64 --> 381.78]  Let me give you the contrasting kind of perspectives, because I actually didn't know that Ismail,
[381.86 --> 385.42]  who I've worked with for many years now, even at different companies before BlackBerry,
[385.62 --> 390.70]  I didn't know that you were, you started on the offensive side and then switched to the
[390.70 --> 391.52]  defensive side.
[391.52 --> 395.00]  I am very much the opposite, well, except for the switch.
[395.30 --> 398.92]  I started on the offensive side, and I remain on the offensive side.
[399.22 --> 404.48]  The part that I am most intrigued by and always have been is what I call, well, what's called
[404.48 --> 406.66]  attacker ontology.
[407.08 --> 412.66]  So I've always wanted to understand what makes the attacker behave like an attacker, so I
[412.66 --> 413.50]  can better defend.
[413.50 --> 419.96]  But my primary areas of research and areas of work and my primary focus has always been
[419.96 --> 425.60]  trying to anticipate what the attacker is going to do, you know, so that I can help our clients
[425.60 --> 427.10]  strategize, et cetera, et cetera.
[427.28 --> 433.20]  It's always been like, even before, and just from an AI perspective, cybersecurity has been
[433.20 --> 435.60]  using AI for well over 20 years.
[435.72 --> 437.98]  I'd say probably 30 years almost.
[437.98 --> 442.12]  So it's not as novel as it is to, you know, the average layperson.
[442.32 --> 447.38]  But even before the popularization or the democratization of AI that we've seen in the
[447.38 --> 451.96]  last two, three, four years with companies like OpenAI, et cetera, even before, you know,
[452.10 --> 459.24]  AI was so much in the forefront, I've been very intrigued with how we can build strategies
[459.24 --> 468.02]  that help customers, organizations, governments anticipate earlier what they need to be protecting
[468.02 --> 468.48]  against.
[468.60 --> 471.40]  And that's kind of where my perspective comes.
[471.40 --> 474.54]  So I didn't contribute to the blog.
[474.62 --> 477.88]  I believe it was primarily Ismail's blog and maybe Ismail and his team.
[478.08 --> 486.22]  But my perspective on the blog was very much how can we use AI to also help level the fields
[486.22 --> 487.08]  a little bit more.
[487.08 --> 492.24]  It's a constant, you know, battle with the fields going back and forth and kind of who's
[492.24 --> 496.32]  winning the race between attackers, cyber criminals and defenders.
[496.94 --> 502.42]  So anything we can use to help balance that out, that's always been my interest.
[503.02 --> 507.70]  I'm curious, before we fully dive into the AI stuff, can you describe, because, you know,
[507.76 --> 514.08]  we have a very AI focused audience diversely in that area, but a lot of folks maybe have
[514.08 --> 516.88]  never been really addressing cyber themselves.
[517.16 --> 522.14]  And when you talked about that, the ontology and kind of talked about maybe some of the
[522.14 --> 525.16]  motivators that, you know, why, what are these people out there?
[525.46 --> 526.26]  Who do they represent?
[526.50 --> 529.98]  What are they trying to do in a baseline, like with or without AI?
[530.16 --> 531.92]  What's, what are we dealing with in the world?
[531.92 --> 538.72]  I remember, and again, I've been at this for a while, probably longer than most.
[539.16 --> 541.22]  I'm, you know, like your age, Chris.
[541.44 --> 543.56]  So I'm approaching 60 years old.
[543.70 --> 543.82]  Yep.
[543.94 --> 544.42]  Exactly.
[544.58 --> 545.92]  Old curmudgeoning.
[546.26 --> 547.42]  Get off my lawn.
[547.72 --> 548.16]  That's right.
[548.32 --> 553.54]  So I'm approaching that age, that, you know, scary age of 60, at least it's scary to me.
[553.54 --> 560.58]  So I remember a lot of things historically about the cyber security industry that give me perspective.
[560.80 --> 566.14]  One was, I want to say it was around 2010, 11 or 12, somewhere around there.
[566.28 --> 572.60]  It was the first time that I noticed in the FBI's threat intelligence report that they
[572.60 --> 574.28]  used to release every year.
[574.46 --> 581.08]  In that report around 2010, 11, 12 was the first time that they reported, the FBI reported
[581.08 --> 592.02]  that profits derived from cybercrime surpassed, globally, surpassed profits from heroin, cocaine,
[592.60 --> 594.64]  marijuana sales combined.
[594.84 --> 595.18]  Wow.
[595.84 --> 601.56]  And for me, that, and I'm talking, this was, you know, 2010, like I said, that to me was
[601.56 --> 602.42]  a tipping point.
[602.42 --> 608.14]  That's, in my mind, I've built the narrative that right around then, or maybe a year or two,
[608.14 --> 614.80]  year or three before then, or after then, that's when criminal organizations focused
[614.80 --> 616.08]  in on cybercrime.
[616.22 --> 621.72]  And it switched from being, you know, the harmless hacker in the grandma's basement.
[621.98 --> 627.32]  You know, I'm thinking like a Kevin Mitnick type of a guy who kind of started off that.
[627.40 --> 629.82]  For those who are in the cyberspace, they know the name.
[629.88 --> 632.44]  You know, he was kind of like a quote unquote harmless hacker.
[632.62 --> 633.36]  He was arrested.
[633.36 --> 637.58]  I think he might've been one of the first cases of a full-fledged arrest and conviction
[637.58 --> 638.90]  for cybercrime.
[639.22 --> 643.64]  But, you know, his cybercrime was always focused on what can I learn?
[643.76 --> 647.78]  You know, what can I gain from these things that I'm illegally getting access into?
[648.30 --> 653.88]  It was less, if at all, it was not about, you know, what can I financially gain?
[654.16 --> 657.78]  Now, it is largely financially motivated.
[657.96 --> 661.34]  I'll let Ismael deal with this a little bit more because, you know, this is his forte.
[661.34 --> 663.56]  He runs our threat organization.
[664.00 --> 668.68]  But from my perspective, it is largely based on what can we monetize?
[669.38 --> 670.56]  Ismael, what do you have to add to that?
[670.90 --> 674.06]  Well, the first thing is I'm so happy to know that I'm the youngest one in the room.
[674.34 --> 674.46]  Okay.
[674.72 --> 677.68]  So it says me with a white beard, right?
[677.94 --> 679.82]  We're all showing it a little bit, but that's okay.
[679.86 --> 680.92]  We're on top of things, man.
[681.38 --> 681.72]  But yes.
[681.78 --> 687.78]  So as Greg says, my team, our job is to characterize the adversary and to translate
[687.78 --> 690.82]  that into, we call it countermeasures, right?
[690.84 --> 697.44]  So think about, you know, you're analyzing or your goal is to design a vest to protect
[697.44 --> 699.12]  law enforcement, for example, right?
[699.12 --> 701.04]  So we analyze the weapons.
[701.22 --> 702.26]  We analyze their tools.
[702.40 --> 703.72]  We analyze their motivation, right?
[703.72 --> 704.58]  How they operate.
[704.58 --> 709.86]  And then we take all of that and we use this information to design the most effective vest
[709.86 --> 712.10]  to protect against those bullets, right?
[712.32 --> 714.00]  But it's not just about the bullets.
[714.00 --> 717.80]  It's about like who is using these weapons and what's the reason they're using them for.
[718.14 --> 719.08]  That's the motivation.
[719.22 --> 720.32]  That's really the key piece.
[721.00 --> 725.54]  And this financial motivation, as Greg has been saying, has been growing very fast.
[725.60 --> 727.80]  And that's why we all know about ransomware, for example.
[727.80 --> 732.18]  But there's a lot of other motivations, and maybe we don't talk about that much.
[732.38 --> 733.52]  Well, some of them we do.
[734.26 --> 735.18]  Spionage, right?
[735.32 --> 740.84]  Nation states, the so-called APTs, advanced persistent threats that we often see in the
[740.84 --> 744.88]  news, and especially, you know, right now around election times, there's a lot of talking
[744.88 --> 749.48]  about this manipulation of information by these nation state actors.
[749.88 --> 753.92]  These are very well funded, and typically they're the most advanced of all of them.
[754.34 --> 755.72]  But there's other motivations too.
[755.72 --> 756.98]  There's hacktivism.
[757.62 --> 762.20]  You know, we have seen groups like Anonymous in the past, like many others, that they would
[762.20 --> 766.68]  target organizations just because they make money, I don't know, selling records, right?
[766.70 --> 768.06]  And they think that's evil.
[768.68 --> 771.70]  But at the end of the day, cyber is just a weapon, right?
[771.80 --> 773.02]  It's a weapon that can be used for good.
[773.42 --> 775.54]  It's a weapon that can be used for evil.
[776.02 --> 777.04]  Same as AI, right?
[777.08 --> 781.18]  AI is just one more tool in the arsenal of any of these people.
[781.18 --> 785.00]  So that's why I like to talk about the motivations, because it helps us to understand
[785.00 --> 791.58]  what's the purpose of using a tool, in this case, like AI, in this, you know, cyber world,
[791.68 --> 792.00]  if you want.
[792.56 --> 797.88]  So how does BlackBerry, can you kind of layer in BlackBerry, having kind of given us that
[797.88 --> 801.56]  landscape of what you're looking at in the world?
[801.74 --> 804.32]  And how does BlackBerry start layering into this?
[804.90 --> 807.24]  What are your interests in that capacity?
[807.24 --> 808.52]  And what are you trying to accomplish?
[808.82 --> 809.38]  Good question.
[809.38 --> 814.46]  Well, so we have been in the world of securing communications for quite some time, right?
[814.56 --> 818.30]  And I think everybody remembers those BlackBerry devices.
[818.60 --> 825.40]  We don't do devices anymore, but we do software to protect devices, not just phones, but also
[825.40 --> 828.82]  endpoints of, you know, all over the world.
[828.82 --> 834.96]  And specifically my team, what we do is to, as I mentioned before, try to characterize these
[834.96 --> 838.78]  attackers to be able to protect customers, right?
[838.84 --> 840.38]  And this takes the form of products.
[840.50 --> 850.18]  It takes also the form of services from endpoint software to zero trust network access to, you
[850.18 --> 858.44]  know, high military grade encryption, secure communications, to even software to manage a crisis,
[858.44 --> 863.04]  could be, you know, instant response, like the environment's on fire, the attacker's here,
[863.10 --> 865.88]  and we need to remediate that, or it could be even like a natural disaster.
[866.42 --> 870.28]  So when we talk about threats, we just even go beyond just the cybersecurity threats.
[870.40 --> 871.92]  That's a high level overview.
[872.02 --> 874.46]  I don't know, Greg, if you want to go deeper into that.
[875.02 --> 875.90]  I don't know if I'll go deeper.
[876.10 --> 878.80]  I might hang off of one of the branches.
[879.24 --> 885.32]  The side of BlackBerry that I'm maniacally focused on is really just, I want to say, purely
[885.32 --> 886.78]  the cybersecurity part.
[886.78 --> 888.80]  So obviously, BlackBerry does a lot of other things.
[888.94 --> 895.26]  We have our automotive and IoT section, segment that's very, very, very large, probably a
[895.26 --> 901.02]  billion-dollar business in and of itself with, you know, operating systems that run in any
[901.02 --> 903.50]  car that has anything digital in it, et cetera.
[904.02 --> 909.50]  The part that I'm focused on, though, is pretty much purely my area of expertise, which is cybersecurity.
[909.50 --> 918.24]  So what we've been doing from my side of the house is helping customers build their defenses
[918.24 --> 924.26]  in a way that allows them to do something that I call preemptive security.
[924.54 --> 929.12]  If you remember in my earlier preamble, I referred to, you know, we need to be able to predict
[929.12 --> 932.58]  what the attackers are going to do so that we can defend against it.
[932.58 --> 940.46]  I help my customers strategize around building those platforms, those tools, those combination
[940.46 --> 943.76]  of different tools to do exactly that.
[943.88 --> 949.84]  The nuance of it with cybersecurity is just because of organically how the industry has
[949.84 --> 955.32]  grown and, you know, VC investment and a million other reasons, we've sprawled very
[955.32 --> 959.44]  much into, you know, there's thousands of tools to get the job done.
[959.52 --> 965.12]  And there's probably thousands, if not tens of thousands of different little aspects that
[965.12 --> 968.08]  need to be protected in the average organization.
[968.08 --> 973.28]  You might have, you know, endpoints, you know, the computers, you might have servers, you might
[973.28 --> 978.38]  have a network, you might have stuff up in the cloud, you might have operational technology
[978.38 --> 984.88]  or IoT technology, all different aspects that all need to be protected that all require
[984.88 --> 986.58]  completely different tool sets.
[987.24 --> 993.94]  That sprawl has made it difficult for customers to have a homogenous approach to how do we
[993.94 --> 995.22]  defend against it all.
[995.58 --> 1001.10]  Ismail can probably talk more about one of the things that attackers do, I want to say
[1001.10 --> 1006.16]  very, very, very well, is attack the gaps between our tools.
[1006.56 --> 1011.64]  So if they detect that you have a great tool that, you know, the foremost tool on protecting
[1011.64 --> 1015.60]  computers, your endpoints, but your network stack is a little bit weak, they're going to
[1015.60 --> 1019.14]  attack right in the middle of that network stack and gain access to the endpoints.
[1019.64 --> 1024.72]  Vice versa, if they see your network and your endpoint, rock solid, but you have a weakness
[1024.72 --> 1026.82]  over in the cloud, you're going to start seeing cloud attacks.
[1027.34 --> 1032.94]  What the industry has not been very good at that BlackBerry is trying to help resolve is
[1032.94 --> 1040.42]  how do we help customers pull all of that telemetry in to be able to get, as I said, a homogenous
[1040.42 --> 1046.82]  view of everything that's attacking them and everything they're doing about defenses across
[1046.82 --> 1048.20]  all those little silos.
[1048.54 --> 1051.02]  That's what I help my customers strategize on.
[1051.26 --> 1053.02]  And my customers vary from governments.
[1053.10 --> 1057.68]  I met with the government of Morocco a couple of weeks ago to large corporations, the biggest
[1057.68 --> 1061.30]  banks in the world, the biggest airlines in the world, et cetera, et cetera.
[1061.30 --> 1066.82]  And it just spans the range, but all of them have that problem.
[1067.34 --> 1072.98]  The most mature organizations have well-developed tools that are unintegrated.
[1073.56 --> 1082.00]  And the least, like the SMBs, which are also our targets, our customers, have oftentimes less
[1082.00 --> 1083.46]  developed security stacks.
[1083.70 --> 1084.96]  But the problem is the same.
[1085.20 --> 1089.06]  Even if they say, well, you know, we can make an investment in this one little tool, then
[1089.06 --> 1093.66]  they have their gaps and they're not being able to ingest all of that intelligence that
[1093.66 --> 1094.08]  they have.
[1094.52 --> 1098.94]  It says something about the industry, and I'm going to kind of shoot at my own job now.
[1098.94 --> 1105.60]  It says something about the industry that a strategist at that level focused on those types
[1105.60 --> 1107.22]  of problems is even needed.
[1107.54 --> 1111.84]  Like you don't have that in the medical industry, as far as I know.
[1112.04 --> 1115.28]  You definitely don't have that in, for example, the automotive industry.
[1115.28 --> 1119.88]  Like there aren't integrators that need to help you with how to integrate, you know,
[1119.92 --> 1121.24]  your car to work properly.
[1121.36 --> 1123.90]  You go to Ford, you say, I want an SUV.
[1124.06 --> 1125.10]  They give you the whole SUV.
[1125.42 --> 1130.54]  They don't say buy the motor here and then go down the street and get four tires and go
[1130.54 --> 1132.16]  across the way and get a transmission.
[1132.44 --> 1134.46]  You glue it together and you make it work.
[1134.56 --> 1135.74]  They give you the whole thing.
[1136.30 --> 1137.44]  Cybersecurity doesn't do that.
[1137.58 --> 1139.18]  We don't give you the whole thing.
[1139.18 --> 1147.16]  So that necessitates a cross-section of strategists like myself and the team that supports me to
[1147.16 --> 1153.54]  go out and actually help customers parse through this web of tools that they've built.
[1153.82 --> 1156.94]  You probably don't go to cybersecurity industry events.
[1157.26 --> 1157.64]  I do.
[1157.86 --> 1158.86]  Ismail does as well.
[1159.16 --> 1160.56]  Ismail speaks at many of them.
[1161.00 --> 1167.66]  The amount of vendors on the expo floor, I remember going to RSA 13 years ago or so.
[1167.66 --> 1168.86]  A handful of vendors.
[1168.98 --> 1169.98]  It was a small convention.
[1170.28 --> 1171.62]  Now, it's early.
[1171.84 --> 1174.38]  Thousands, three, four, five thousand vendors.
[1174.72 --> 1176.02]  40,000 people last year.
[1176.46 --> 1177.30]  That's a lot.
[1177.40 --> 1179.74]  Dude, I thought it was big.
[1180.16 --> 1182.30]  I went to a conference called Jitex.
[1182.64 --> 1183.72]  Holy spook.
[1184.00 --> 1190.18]  Almost a million people at Jitex at a conference talking about technology.
[1190.30 --> 1192.04]  It was crazy insane.
[1192.42 --> 1194.96]  The amount of boots, I think it was 40,000 vendors.
[1194.96 --> 1201.44]  They're like insane that there's an appetite for all of these tools and customers are bobbling
[1201.44 --> 1201.90]  them up.
[1202.02 --> 1205.06]  And it makes their environment more complex.
[1205.06 --> 1207.04]  And that's where we oftentimes come in.
[1207.22 --> 1207.82]  And noisy too.
[1208.04 --> 1208.16]  Yeah.
[1208.28 --> 1210.32]  There's a lot of noise in this industry.
[1210.32 --> 1224.14]  Okay, friends.
[1224.20 --> 1225.84]  Here's what I love about Notion.
[1225.96 --> 1227.78]  And I'm a big fan of Notion.
[1228.14 --> 1232.96]  I think all the new improvements they've made recently with Notion AI built right in is just
[1232.96 --> 1233.58]  astounding.
[1233.58 --> 1238.46]  Being able to have your notes, your docs, your projects, your to-dos, your tasks, your dashboards,
[1238.88 --> 1242.24]  all the things in one single place, beautifully designed.
[1242.52 --> 1249.06]  And then add on top of that Notion AI with the ability to search, analyze, chat, and even
[1249.06 --> 1251.06]  describe to you how to build dashboards.
[1251.40 --> 1253.28]  You can ask it, hey, I want to do this.
[1253.64 --> 1259.44]  And it will help you build out a dashboard or a database or a template that makes sense for you,
[1259.70 --> 1262.30]  your workflows, your business, your orgs, or whatevers.
[1262.30 --> 1267.72]  Notion really is the perfect place to organize your tasks, track your habits, write beautiful
[1267.72 --> 1269.28]  docs, collaborate with your team.
[1269.64 --> 1271.74]  There's just so much you can do with it.
[1272.08 --> 1275.88]  And Notion AI already has the context of all that work.
[1276.22 --> 1279.12]  It's also connected to multiple knowledge sources.
[1279.68 --> 1284.56]  It uses AI knowledge from GPT-4 and Claude to chat with you about any topic.
[1284.96 --> 1289.80]  And you can search across thousands of Notion docs in seconds to quickly answer really any
[1289.80 --> 1294.00]  question you have about your context, which is all of your Notion docs.
[1294.42 --> 1295.78]  They also have AI connectors.
[1295.92 --> 1296.70]  This is now in beta.
[1297.30 --> 1302.48]  Notion AI can search across Slack discussions, Google documents, Google slides, Google sheets,
[1302.98 --> 1304.84]  and even tools like GitHub and Jira.
[1305.28 --> 1306.74]  Those are coming soon.
[1307.10 --> 1312.46]  And the cool thing with Notion is it could be used by small teams, individuals, or even
[1312.46 --> 1313.98]  Fortune 500 companies.
[1313.98 --> 1320.46]  It is a very scalable tool that can help you spend less time emailing, cancel more meetings,
[1321.00 --> 1326.44]  save your time searching for all your work, and reduce spending on multiple tools.
[1326.74 --> 1328.70]  And this helps everyone be on the same page.
[1329.06 --> 1333.50]  Try Notion today for free when you go to Notion.com slash practical AI.
[1334.00 --> 1341.28]  That's all of our case letters, Notion.com slash practical AI to try the powerful, easy to use
[1341.28 --> 1342.70]  Notion AI today.
[1342.96 --> 1345.90]  And when you use our link, of course, you are supporting our show.
[1345.90 --> 1346.96]  And we love that.
[1347.44 --> 1350.80]  Again, Notion.com slash practical AI.
[1371.28 --> 1379.18]  Okay, so as you guys have watched the industry explode and you're dealing with these things
[1379.18 --> 1384.06]  that other industries don't necessarily have to address, you talked about kind of just the
[1384.06 --> 1389.74]  sprawl of assets to defend and the gaps between them and the fact that there are so many tools
[1389.74 --> 1391.00]  addressing different components.
[1391.72 --> 1396.70]  I would imagine that's quite a challenge, which is one of the reasons I'm sure the industry
[1396.70 --> 1398.00]  has gotten as big as it is.
[1398.00 --> 1404.28]  As you're looking at that and you're starting to see these new things, and when I say new,
[1404.38 --> 1409.42]  meaning some of the more recent tools on the AI realm and stuff like that, as cyber experts,
[1409.78 --> 1412.92]  how is AI starting to layer into this ecosystem?
[1413.38 --> 1415.28]  What are you, how do you see that?
[1415.46 --> 1420.30]  What are the pros and cons, the risks and threats that it creates?
[1420.76 --> 1424.08]  Can you tell us a little bit about how those two converge?
[1424.08 --> 1429.38]  Yeah, this, as Gregor mentioned it before and explained really well that this is a, an industry
[1429.38 --> 1431.76]  that is always like chasing the new shiny, right?
[1431.78 --> 1434.80]  Like what's the new thing that can solve all of my problems?
[1435.00 --> 1436.24]  And there is no such a thing.
[1436.28 --> 1438.00]  It's a lot more complex than that.
[1438.32 --> 1444.82]  And every time that we try to find that single tool, that silver bullet, we often fail, right?
[1444.84 --> 1448.54]  Because of a lack of an understanding of how all these things need to come together.
[1448.54 --> 1450.68]  So we're, we're in the middle of that hype.
[1450.96 --> 1453.70]  And now the tool is of course, AI, right?
[1454.04 --> 1458.82]  And I would say even more specifically, LLMs, generative AI, because we know, and you guys
[1458.82 --> 1462.32]  in this show know well, that when we talk about AI, it's not one thing, right?
[1462.36 --> 1463.56]  It's a lot of different things.
[1463.98 --> 1468.74]  For example, at BlackBerry, we have been using for many years, coming from the silence engine,
[1468.84 --> 1473.10]  from the silence days, a predictive AI engine, right?
[1473.12 --> 1475.46]  We know we're talking about predictive machine learning, essentially.
[1475.46 --> 1480.56]  And I remember, well, I wasn't, I wasn't at silence at that time, but some of the, my
[1480.56 --> 1486.66]  colleagues that were told me that they were at Black Hat, I think probably 2000, 2016 or
[1486.66 --> 1487.46]  something like that, right?
[1487.46 --> 1489.60]  They were talking at Black Hat about this.
[1489.78 --> 1493.46]  And a lot of people were like, oh, boo, you know, that's, that's, that's not possible.
[1493.86 --> 1495.08]  You're selling smoke.
[1495.58 --> 1497.46]  You know, that's not the way you detect malware.
[1498.16 --> 1504.56]  Fast forward to today and everybody understands that you cannot fight malware with signatures,
[1504.56 --> 1505.12]  right?
[1505.12 --> 1508.82]  I mean, in our report, and we, we produce these reports on a quarterly basis, we talked
[1508.82 --> 1511.58]  about the latest increase in the last quarter.
[1511.68 --> 1515.80]  We're talking about a 53% increase in unique pieces of malware, right?
[1515.80 --> 1519.62]  I think, I don't know if the audience is familiar with the concept of a hash or a fingerprint.
[1520.02 --> 1525.26]  You take a binary blob of data and you create a fingerprint or a hash of that.
[1525.38 --> 1527.12]  And that says, okay, that's unique, right?
[1527.16 --> 1528.48]  Different hashes, different files.
[1528.48 --> 1536.66]  So we're talking about over 11,000 pieces of unique malware per quarter that we have seen
[1536.66 --> 1537.52]  with our telemetry.
[1537.86 --> 1542.70]  How in the world are you going to, you know, create a database or maintain a database?
[1543.00 --> 1544.54]  It's an unscalable issue.
[1544.58 --> 1545.50]  It's unscalable, right?
[1545.50 --> 1545.54]  Yeah.
[1545.94 --> 1549.50]  So predictive machine learning helps us with that.
[1549.54 --> 1553.96]  And it's been helping us for many years to have like really, really good detection of
[1553.96 --> 1554.94]  these type of things.
[1555.52 --> 1558.26]  Now, LLMs can also be useful for different things.
[1558.26 --> 1565.42]  So once again, I think the summary is AI is a useful tool in the hands of defenders.
[1565.60 --> 1569.46]  It is also used by attackers and we can maybe get into that if you want.
[1570.18 --> 1577.70]  But I would say that once we go over this hype cycle that we always have in this industry,
[1577.90 --> 1582.10]  we'll probably understand that it's just one more tooling in our arsenal and that we need
[1582.10 --> 1583.96]  to remain problem focused.
[1583.96 --> 1587.34]  Just because we have a solution to a specific thing, it doesn't mean that it's going to
[1587.34 --> 1590.08]  be the solution to absolutely everything, right?
[1590.24 --> 1591.68]  But of course, it helps.
[1592.74 --> 1592.88]  Yeah.
[1592.98 --> 1594.96]  I'll comment on that if I may, Chris.
[1595.20 --> 1595.52]  Sure.
[1595.74 --> 1596.18]  Absolutely.
[1596.48 --> 1598.20]  Ismail touched a little bit.
[1598.34 --> 1604.30]  He kind of grazed over LLMs and I'm glad you only grazed over it because of what I'm about
[1604.30 --> 1604.78]  to say.
[1605.16 --> 1610.98]  We think LLMs, as good as they are, and they have some excellent use cases and value, I think
[1610.98 --> 1616.20]  they contribute to a lot of the noise and the hype machines that we hear in the industry
[1616.20 --> 1616.86]  right now.
[1617.30 --> 1619.80]  I'll speak specifically for cybersecurity.
[1620.42 --> 1628.42]  I am not yet convinced of the utility, the usefulness of an LLM, particularly for its
[1628.42 --> 1632.60]  natural language ability, ability to process things via natural language.
[1632.80 --> 1635.20]  I'm not sure that that was the problem we had.
[1635.20 --> 1643.38]  I speak to SOC analysts and chief information security officers literally on a daily basis.
[1643.72 --> 1644.64]  That's my job.
[1645.36 --> 1652.86]  I can't remember in the last 30 years doing this that a group of operators, SOC analysts,
[1653.00 --> 1655.42]  et cetera, have told me, you know what would be great, Greg?
[1655.56 --> 1658.74]  We don't know how to extract the data from our tools.
[1658.88 --> 1662.24]  If we could only say that in natural language, that would really help.
[1662.56 --> 1663.58]  That's not the problem.
[1663.58 --> 1668.12]  The people that are doing these jobs in the SOCs, et cetera, et cetera, are very adept
[1668.12 --> 1668.86]  at their tools.
[1669.20 --> 1674.20]  They don't have the problem communicating with the tools and writing a parsing command or
[1674.20 --> 1676.76]  a query or whatever to extract the data.
[1676.86 --> 1677.70]  That's not the issue.
[1678.08 --> 1681.06]  There's other things that AI and machine learning can help with.
[1681.52 --> 1683.12]  Classification is a big one.
[1683.42 --> 1685.64]  Ismail has already referred to prediction.
[1685.94 --> 1689.46]  I think that's a very, very big one that is underutilized today.
[1689.46 --> 1696.52]  But classification, how do we classify not only files and hashes, but behaviors, indicators
[1696.52 --> 1698.26]  of attack, indicators of compromise?
[1698.52 --> 1703.28]  How are we able to classify these three things that are connected together?
[1703.28 --> 1709.14]  Or in the case of a cyber attack, these 50 things, these 50 behaviors or indicators we
[1709.14 --> 1713.40]  find, how can we pull them all together and say, listen, this is leading up.
[1713.40 --> 1714.62]  These all belong together.
[1715.02 --> 1719.68]  These 10 things that we found on your network and these 15 things that we found on your end
[1719.68 --> 1724.76]  points and these 12 other things that we found simultaneously in the same temporal window
[1724.76 --> 1726.16]  in your cloud environment.
[1726.16 --> 1728.90]  They all belong together and they're all part of one attack.
[1728.90 --> 1735.22]  That classification process, I think that's somewhere where AI can help because that's where
[1735.22 --> 1736.02]  the gap is.
[1736.02 --> 1742.70]  Taking the ton of data that comes in that swamps our security operation centers with alert
[1742.70 --> 1749.06]  fatigue, parsing through that to quote unquote make sense of it and kind of narrow it down
[1749.06 --> 1749.94]  to a few cases.
[1750.42 --> 1755.60]  And when I say few, that few may be thousands still, but it's an order of magnitude or more
[1755.60 --> 1759.18]  drop from the tens or hundreds of thousands of events that you get.
[1759.36 --> 1764.32]  If you can drop that down to a significantly smaller amount of cases and then tackle those cases,
[1764.32 --> 1769.66]  that's one of the problems that I see AI solving in cybersecurity extremely well.
[1770.08 --> 1772.14]  It's really interesting to hear you say that.
[1772.68 --> 1779.12]  And I want to, just as an aside for a moment, for our audience who is going episode to episode,
[1779.28 --> 1780.80]  this is a topic we talk about a lot.
[1780.88 --> 1786.04]  It sounds like you're going through, you're familiar with the Gartner hype cycle, and it
[1786.04 --> 1788.48]  goes up over the top, maximal hype.
[1788.66 --> 1789.88]  People become frustrated.
[1790.04 --> 1794.30]  It plunges down in the trough of disillusionment where they're very unhappy and they say this is
[1794.32 --> 1794.64]  stinks.
[1794.80 --> 1796.22]  I don't want to deal with it.
[1796.72 --> 1800.82]  And then people kind of take a second look and they go, well, it's good for some things.
[1800.96 --> 1803.72]  It's not, it's not the solve, you know, it doesn't solve everything.
[1804.06 --> 1807.82]  And they find their, their plateau of productivity where it's actually useful.
[1807.82 --> 1810.94]  And it sounds like you've been going through that same process.
[1810.94 --> 1814.92]  So like, like many other industries have, um, and, and you're really practical.
[1814.92 --> 1817.70]  And you also drew out another point that I'd like to emphasize.
[1817.70 --> 1823.02]  And that's that, uh, when it comes to generative AI and LLMs and such, we have a habit of forgetting
[1823.02 --> 1826.78]  that there are other, that there are other techniques in the AI realm out there.
[1827.56 --> 1828.00]  Classification.
[1828.20 --> 1828.64]  Other ways.
[1828.94 --> 1829.66]  Yeah, exactly.
[1829.66 --> 1834.28]  And, and you guys are like, we have other tools here that are really productive for
[1834.28 --> 1834.82]  what we're doing.
[1834.82 --> 1836.78]  Just maybe not the super hypey part of it.
[1837.10 --> 1842.06]  Um, so I'm, I'm really glad that you shared that with us because we're, we are practical
[1842.06 --> 1845.16]  AI on the show and we're trying to, to get people on track.
[1845.16 --> 1847.84]  I'll just give you an example of how absurd this is getting.
[1848.00 --> 1852.78]  I saw a large vendor and I'm really tempted to say the name, but I won't, uh, that was
[1852.78 --> 1857.88]  showing, um, you know, how cool these, uh, generative AI is applied to the SOC.
[1858.06 --> 1861.88]  So, you know, the, the SOC security operation center, they typically use dashboards, right?
[1861.90 --> 1865.46]  And they have dashboards and they're looking at, for example, number of, I don't know, DNS
[1865.46 --> 1868.42]  requests or number of alerts for these or for that.
[1868.56 --> 1872.76]  So there's this dashboard and there's a peak of activity at 7 PM.
[1872.76 --> 1878.38]  So now the, yes, the LLM is like, see, I saw a peak of activity at 7 PM.
[1878.42 --> 1880.86]  And I'm like, how much money are you paying for that?
[1880.98 --> 1881.14]  Right.
[1881.34 --> 1886.92]  There's a large cost in, in, in this type of subscriptions and I can easily train an analyst
[1886.92 --> 1888.24]  to catch that.
[1888.52 --> 1892.04]  And that person can give you even more context, right.
[1892.04 --> 1897.00]  And have probably more intuition, more, maybe even knowledge of the strategy, right.
[1897.02 --> 1901.22]  Talking about strategy, Gregory, and even more creativity than that.
[1901.22 --> 1902.44]  So absolutely.
[1902.56 --> 1904.56]  Like you gotta know what the tool is useful for.
[1904.56 --> 1910.40]  It's very useful for contextualization, summarization, pattern matching, generalization, hypothesis
[1910.40 --> 1911.34]  testing, right.
[1911.36 --> 1916.06]  I could go and say, Hey, based on all of these reports that I have written on all of this
[1916.06 --> 1922.60]  database that I have, give me a, going to the offensive side, Greg, give me a emulation
[1922.60 --> 1925.50]  plan for emulating this threat actor.
[1925.86 --> 1926.32]  Right.
[1926.32 --> 1930.26]  And it's not going to be super creative because it's going to be based on things that have
[1930.26 --> 1934.66]  already been the data that has already been gathered, but it will save me a lot of time
[1934.66 --> 1937.56]  because I will not have to go through all of these documents myself and have to, you
[1937.56 --> 1939.34]  know, extract all of these different things.
[1939.80 --> 1942.92]  So I may iterate over that faster and get to that faster.
[1943.16 --> 1944.86]  But yeah, there's a lot of hype.
[1945.06 --> 1951.02]  One of the things that I, and again, I've been in this industry for almost 40 years.
[1951.02 --> 1955.60]  So it's pretty much the only thing I've done professionally, you know, since I came out
[1955.60 --> 1956.10]  of college.
[1956.36 --> 1961.92]  So I'm very passionate about it in case that's not extremely evident to your audience yet.
[1962.30 --> 1968.32]  Therefore, I'm also, I also tend to look at myself and my industry with a really, sometimes
[1968.32 --> 1969.56]  a bit of a harsh lens.
[1969.70 --> 1975.52]  And so I'm going to say something now that might be applicable outside of cyber, but I
[1975.52 --> 1979.40]  see it from inside of cyber and we gut ourselves.
[1979.40 --> 1983.62]  We do legit harm to ourselves by feed.
[1983.78 --> 1991.10]  And when I say we, the vendors primarily by feeding into the hype cycles and selling stuff
[1991.10 --> 1998.82]  that we know good and gosh darn well are absolute smoke and mirrors or have limited usefulness,
[1998.82 --> 2000.60]  but they sell well.
[2000.76 --> 2004.84]  You know, the, the notion of we're going to have an AI powered sock and you're not going
[2004.84 --> 2006.44]  to need sock operators anymore.
[2006.44 --> 2009.50]  You know, you, you, you, you know, these analysts, you won't need them.
[2009.72 --> 2013.18]  You're going to get just less analysts because the AI is going to do all of that for you.
[2013.32 --> 2018.94]  The more we hype that up, the more you get that, the Gartner hype cycle where people try
[2018.94 --> 2019.08]  it.
[2019.14 --> 2021.36]  They go, this is doesn't work this way at all.
[2021.46 --> 2022.82]  I still need the humans.
[2022.82 --> 2029.00]  The humans add, as Ismail said, context and awareness and situational strategy, not to mention
[2029.00 --> 2031.46]  things like morality, which AI is terrible at.
[2031.46 --> 2036.40]  Now, can the AI do bulk volume of, of data processing?
[2036.54 --> 2037.46]  It absolutely can.
[2037.76 --> 2040.54]  And that's where, that's one of the places we should lead into.
[2040.74 --> 2045.24]  I've been touched on things like vision and, you know, some of the more esoteric parts of
[2045.24 --> 2047.56]  AI that we don't speak about every single day.
[2047.80 --> 2053.12]  So I'm not limiting it to prediction, classification and, and large language models, but I'm just
[2053.12 --> 2055.76]  saying large language models are amazing.
[2055.76 --> 2062.14]  I use them regularly for processing anything having to do with language, whether that's
[2062.14 --> 2066.76]  code language, indicator language, or spoken read language.
[2067.10 --> 2073.96]  One of my very practical things that I do with almost every piece of content I'm attempting
[2073.96 --> 2079.84]  to digest now is I try to get the audio and I run a transcript, send it to whisper, send
[2079.84 --> 2083.86]  it to whatever API, give me a transcript of it, analyze the transcript for me.
[2083.86 --> 2085.32]  Give me some key talking points.
[2085.54 --> 2086.60]  What are the things that I said?
[2086.72 --> 2089.68]  What are, what are some tweetable lines that I want to broadcast out?
[2089.76 --> 2095.00]  What are some key quotes that I, that I said, and I build my brand on social media and I
[2095.00 --> 2098.48]  flavor my other talks with that content that I've said already.
[2098.48 --> 2101.20]  I'm going to do it with the talk that I'm doing right now.
[2101.32 --> 2106.26]  That's why I'm in addition to as a backup, I'm also recording my own audio here so that
[2106.26 --> 2107.20]  I can extract that.
[2107.20 --> 2114.04]  And so that I use LLMs, they have utility, but it's, they're not the end all panacea,
[2114.16 --> 2115.24]  you know, oh my God, they're great.
[2115.30 --> 2117.32]  We should throw everything at an LLM.
[2117.80 --> 2123.88]  It's just, the more we do that, I think the more we do intrinsic harm to the industry and
[2123.88 --> 2130.66]  most importantly, to our customers ability to defend themselves because the threat actors
[2130.66 --> 2134.90]  are not, at least I don't see the threat actors out there building a hype cycle.
[2134.90 --> 2141.60]  I see them out there efficiently sharing threat intelligence and leveraging it to build new
[2141.60 --> 2146.86]  novel attacks so that there's unique ways that they can get their objective, which is,
[2146.92 --> 2149.72]  you know, monetize weaknesses in our environment.
[2150.08 --> 2154.56]  We are not as maniacally focused on our task at hand as that yet.
[2164.90 --> 2172.78]  What's up friends?
[2173.04 --> 2174.68]  I've got something exciting to share with you today.
[2174.90 --> 2179.06]  A sleep technology that's pushing the boundaries of what's possible in our bedrooms.
[2179.50 --> 2184.28]  Let me introduce you to Eight Sleep and their cutting edge Pod 4 Ultra.
[2184.84 --> 2186.64]  I haven't gotten mine yet, but it's on its way.
[2186.90 --> 2188.42]  I'm literally counting the days.
[2188.90 --> 2191.44]  So what exactly is the Pod 4 Ultra?
[2191.44 --> 2196.76]  Imagine a high-tech mattress cover that you can easily add to any bed.
[2197.00 --> 2198.48]  But this isn't just any cover.
[2198.98 --> 2204.16]  It is packed with sensors, heating and cooling elements, and it's all controlled by sophisticated
[2204.16 --> 2205.58]  AI algorithms.
[2206.12 --> 2212.18]  It's like having a sleep lab, a smart thermostat, and a personal sleep coach all rolled into
[2212.18 --> 2213.18]  a single device.
[2213.18 --> 2219.08]  It uses a network of sensors to track a wide array of biometrics while you sleep, sleep
[2219.08 --> 2223.32]  stages, heart rate variability, respiratory rate, temperature, and more.
[2223.78 --> 2228.02]  It uses precision temperature control to regulate your body's sleep cycles.
[2228.50 --> 2234.62]  It can cool you down to a chilly 55 degrees Fahrenheit or warm you up to a good, nice solar
[2234.62 --> 2236.28]  temperature of 110 Fahrenheit.
[2236.58 --> 2240.28]  And it does this separately for each side of the bed.
[2240.28 --> 2244.40]  This means you and your partner can have your own ideal sleep temperatures.
[2245.16 --> 2252.04]  But the really cool part is that the Pod uses AI and it uses machine learning to learn your
[2252.04 --> 2253.42]  sleep patterns over time.
[2253.42 --> 2258.12]  And it uses this data to automatically adjust the temperature of your bed throughout the
[2258.12 --> 2259.96]  night according to your body's preferences.
[2260.30 --> 2265.44]  Instead of just giving you some stats, it understands them and it does something about it.
[2265.82 --> 2268.96]  Your bed literally gets smarter as you sleep over time.
[2268.96 --> 2273.12]  And all this functionality is accessible through a comprehensive mobile app.
[2273.42 --> 2278.36]  You get sleep analytics, trends over time, and you even get a daily sleep fitness score.
[2278.90 --> 2280.32]  Now, I don't have mine yet.
[2280.46 --> 2281.24]  It is on its way.
[2281.54 --> 2283.32]  Thanks to our friends over at 8sleep.
[2283.52 --> 2286.68]  And I'm literally counting the days I get it because I love this stuff.
[2287.08 --> 2290.96]  But if you're ready to take your sleep and your recovery to the next level, head over
[2290.96 --> 2298.58]  to 8sleep.com slash practical AI and use our code practical AI to get 350 bucks off your
[2298.58 --> 2300.48]  very own Pod 4 Ultra.
[2300.94 --> 2302.94]  And you can try it free for 30 days.
[2303.30 --> 2306.52]  I don't think you want to send it back, but you can if you want to.
[2306.90 --> 2311.78]  They're currently shipping to the US, Canada, United Kingdom, Europe, and Australia.
[2311.78 --> 2315.74]  Again, 8sleep.com slash practical AI.
[2315.74 --> 2337.40]  So, Greg, that was great kind of explaining how you're approaching that, you know, trying
[2337.40 --> 2342.10]  to keep the AI practical, trying to have the right AI in the right place.
[2342.10 --> 2347.50]  And great call out for the fact that like so many other industries, there is a proclivity
[2347.50 --> 2352.34]  in your industry to also do the kind of, you know, AI and everything.
[2352.84 --> 2356.46]  You know, you said you use the phrase, you know, selling smoke and mirrors and stuff.
[2356.46 --> 2363.30]  And you guys working really hard to productively give solutions and strategies that are not
[2363.30 --> 2365.30]  built around the hype side of all this.
[2365.44 --> 2367.48]  Could you dive into a little bit more of that?
[2367.48 --> 2373.34]  And also, Ismail, if you could also address a bit about the blog itself that you wrote
[2373.34 --> 2378.24]  so that we can draw some of our listeners into that and they can also read that as they're
[2378.24 --> 2380.84]  finishing up the episode and understand that.
[2380.94 --> 2382.00]  I really appreciate that.
[2382.10 --> 2387.92]  So, kind of both the, what are you doing in that practical sense and what are you producing
[2387.92 --> 2388.74]  for your customers?
[2388.90 --> 2391.22]  And then kind of, how is the blog contributing to that?
[2391.86 --> 2393.22]  Do you want me to start maybe with the blog?
[2393.28 --> 2396.40]  And then, Greg, you can talk about the solutions we're building.
[2396.40 --> 2401.20]  Yeah, so the blog is essentially trying to address the hype that we were just talking
[2401.20 --> 2402.02]  before, right?
[2402.10 --> 2406.10]  And saying, okay, so what is AI being used for by the attackers?
[2406.18 --> 2406.92]  Let's start with that.
[2407.52 --> 2411.84]  Some people may think that, oh, you know, attackers are crafting this malware that is
[2411.84 --> 2417.34]  autonomous, that it just goes out and finds a vulnerability like a zero day, right?
[2417.36 --> 2420.54]  We call zero day this industry, like something that we haven't found yet.
[2420.60 --> 2421.50]  It's Novell.
[2421.98 --> 2423.36]  Nobody knows about that vulnerability.
[2423.36 --> 2426.60]  Now this autonomous agent is going to exploit it.
[2426.66 --> 2430.68]  It's going to get into the company, steal the data, ransom the environment.
[2431.18 --> 2433.52]  And no, then you wake up, right?
[2433.66 --> 2434.70]  There's no such thing.
[2435.58 --> 2437.70]  Not as of today, at the very least.
[2438.24 --> 2441.54]  I think we're talking about people among the same, I'm going to say around the same age.
[2442.06 --> 2444.32]  You probably remember Blade Runner from 1982.
[2444.32 --> 2444.52]  Of course.
[2444.52 --> 2445.82]  The original one, right?
[2445.90 --> 2446.60]  The replicants.
[2446.82 --> 2449.16]  There is no replicants as of today.
[2449.28 --> 2449.98]  There's deep fakes.
[2450.06 --> 2452.52]  That's a different thing that could look like humans.
[2452.58 --> 2453.56]  That's the closest thing.
[2454.22 --> 2458.28]  But there's no autonomous agents that can do all of these things.
[2458.52 --> 2464.88]  Or we don't see people that, I don't know, like you are training dolphins, right?
[2464.88 --> 2465.80]  For your entire life.
[2465.80 --> 2471.48]  And then all of a sudden, now because of AI, you can hack into companies and make a lot of profit out of that.
[2471.98 --> 2472.92]  Probably not.
[2473.86 --> 2480.18]  So what we see is attacker system, this is a tool essentially for the initial phases of the attack.
[2480.74 --> 2485.52]  And that means that they're getting a lot better at writing phishing emails.
[2485.52 --> 2490.90]  We have seen an increase in phishing emails with language that's non-English.
[2491.34 --> 2501.00]  For example, before, we would see some of these Eastern European organizations or Russian criminals sending emails in English that was like broken English.
[2501.32 --> 2506.00]  And you could quickly spot them and say, oh yeah, this is phishing or spam.
[2506.56 --> 2511.08]  These days, everybody speaks not only perfect English, also perfect Japanese.
[2511.08 --> 2520.40]  We have seen an increase in number of phishing against Japanese companies or other languages that hardly would be used by these cyber criminals.
[2520.50 --> 2522.28]  And that's a clear use of LLMs.
[2522.80 --> 2525.22]  Now, in terms of coding, there's a lot of debate.
[2525.34 --> 2526.62]  It's very controversial, right?
[2526.68 --> 2528.70]  Like, can you learn coding from scratch?
[2528.76 --> 2531.58]  Or can you just like use this to create code from scratch and we'll do these things?
[2532.32 --> 2533.54]  Probably not today.
[2533.86 --> 2535.06]  These models are getting better.
[2535.06 --> 2548.80]  But I still find out that every time I ask any of these agents to create some code for me, I still have to understand the code, understand what I'm trying to do, and being able to refine it and to tune it.
[2549.32 --> 2557.56]  Also, bear in mind that these models are crafting things based on the training that it has received, based on previous data that is already known.
[2557.56 --> 2571.20]  Therefore, when Greg maybe talks about predictive solutions and AI, that makes us also even more successful in the use of our AI because we have trained these models with everything that has been seen in the past as well.
[2571.20 --> 2578.68]  So, at the end of the day, I think that AI is not going to be that much of an advantage to us hackers.
[2578.80 --> 2588.72]  There's always a little advantage, but just because they're attackers, because they take the first step and you're on the defense side and you don't know, right, if they're coming tonight or if they're coming tomorrow morning or if they're coming next month.
[2589.32 --> 2590.84]  You may anticipate that.
[2590.92 --> 2597.88]  And that's where, you know, my team does threat intelligence, which is looking at the geopolitics, looking at, you know, like the weather forecast, right?
[2597.88 --> 2599.70]  What are the clouds signaling?
[2599.70 --> 2602.62]  And then based on that, you adapt your threat model.
[2602.86 --> 2605.40]  But you're always like one step behind by nature.
[2605.70 --> 2606.84]  That's what defense is about.
[2607.68 --> 2622.70]  But even though defenders may have that temporal advantage, I think when used properly by defenders, the field could be leveled and AI could be effectively used to do more things at scale, especially when you have a solid strategy.
[2622.70 --> 2627.26]  It's interesting that Ismail referred to updating our threat model.
[2627.26 --> 2636.24]  And he drew that analogy back to, you know, like the weather, you know, like you look at the clouds and based on what you see in the clouds, you react accordingly.
[2636.24 --> 2638.46]  You might pack an umbrella or something along those lines.
[2638.46 --> 2641.86]  I think that's such a propos analogy.
[2641.86 --> 2655.10]  Because interestingly, as a kid in the 70s, growing up in the Caribbean in a hurricane zone, I remember sitting around the big box TV in the living room.
[2655.10 --> 2660.10]  I think it was even black and white at one point because I'm old and primogeny, as I said earlier.
[2660.30 --> 2669.36]  And watching the predicted hurricane track for some storm that left the western coast of Africa that's barreling towards the Caribbean islands.
[2669.36 --> 2672.34]  My island is a small five mile by seven mile island.
[2672.58 --> 2676.14]  We could get and routinely got decimated by a hurricane.
[2676.44 --> 2683.74]  So if a hurricane's coming, you need to know those predictive tracks with the little circles and saying the storm looks like it's going to go there.
[2684.12 --> 2690.08]  Those in the 70s already were drawn and calculated by AI.
[2690.28 --> 2696.22]  It was one of the first very widely used use cases for predictive AI.
[2696.22 --> 2702.18]  So it's interesting that Ismail uses that as an analogy because that is exactly what we're doing.
[2702.26 --> 2708.32]  We're taking a use case that was well developed with weather prediction, and that's what we're applying to attacker prediction.
[2708.62 --> 2713.70]  So you asked how we can apply this to the customer environment.
[2714.18 --> 2722.08]  One of the things that I am maniacally focused on right now is helping customers, as I said earlier, draw this all together.
[2722.08 --> 2732.02]  So I'm not going to get into product names because this isn't a sales pitch, but we've just developed something in the category called a managed extended detect and response tool set.
[2732.64 --> 2738.24]  And what's unique about our approach to that, that approach in that space is not unique at all.
[2738.32 --> 2739.08]  It's been existed.
[2739.62 --> 2743.94]  Just about every large cybersecurity vendor has something that plays in that space.
[2743.94 --> 2752.52]  What's unique about our take on it, we are heavily focused on regardless to what your security stack consists of.
[2753.12 --> 2754.40]  That's what we're going to ingest.
[2754.82 --> 2764.32]  Most of the other vendors use a XDR type tool to say, listen, to get the maximum benefits out of our tool, you should really be using all of our stuff.
[2764.48 --> 2769.20]  So you should get our firewalls, you should get our endpoints, you should get our cloud stuff, and then it's going to be maximized.
[2769.58 --> 2770.50]  Our take is different.
[2770.50 --> 2779.84]  Our take is we understand that you, the customer, probably struggle with two things, a widely diverse ecosystem of security tools.
[2780.26 --> 2787.78]  And the second thing, especially for medium to smaller companies, you're probably struggling with finding the human resources to do these jobs.
[2787.78 --> 2808.86]  So we have a managed solution where our threat analysts, our security analysts, our well-trained human experts, combined with predictive AI that, as Ismail said, has been well-trained on sensors and sensor data and threat data that we've been receiving for the last 10, 15 years.
[2808.86 --> 2825.22]  That's how we are able to not just ingest all of the data, classify and recognize that this is an attack that we've seen before, even if it's using novel and brand new unseen before malware, and then provide you defensive strategies against it.
[2825.22 --> 2831.18]  That's how I believe BlackBerry can help the market, the customers the most.
[2831.40 --> 2835.26]  I mentioned that I started on the attacker side.
[2835.46 --> 2837.50]  I was never an illegal attacker.
[2837.70 --> 2842.76]  I started as a pen tester and then pivoted into reversing code and doing some other things like that.
[2843.06 --> 2844.82]  And I went from there.
[2844.82 --> 2849.00]  But most of my career was on the customer side.
[2849.24 --> 2860.02]  I proactively switched or maybe was convinced to switch to the vendor side probably about 10 years ago because I saw that gap.
[2860.02 --> 2867.20]  I saw that as a customer, I could buy all of these new widgets and toys, and it really wasn't making me more secure.
[2867.20 --> 2881.22]  So I came to the vendor side to try to influence the vendor defensive motion and product strategy to put out more products that legitimately can help customers solve those two problems.
[2881.32 --> 2885.32]  The manpower problem, the diversity of tool set problem.
[2886.02 --> 2892.26]  The amount of times I am told by a customer, Greg, we'll rip everything out and put in whatever you tell us.
[2892.58 --> 2893.54]  That's infinitesimum.
[2893.68 --> 2894.50]  It has happened.
[2894.50 --> 2898.90]  I have had a couple of Greenfield customers that said, listen, none of it's working.
[2899.24 --> 2901.14]  Take it all out and help us replace it.
[2901.26 --> 2902.20]  But that's rare.
[2902.78 --> 2907.52]  Most of the customers either have financial constraints, time constraints, or some other constraint.
[2907.64 --> 2909.88]  So they need to make do with what they have.
[2910.50 --> 2916.20]  Let's build a tool set that allows customers to use what they have and maximize the value they extract out of it.
[2916.20 --> 2925.78]  So as we wrap up here, and you've done great kind of level setting how you guys are able to add value for your customers in this realm.
[2925.78 --> 2928.98]  This is such a fast changing arena.
[2929.18 --> 2935.78]  You've got AI playing at some productive place in your approach, your strategy, and your solutions.
[2936.16 --> 2939.08]  But this is a fast changing world that we're dealing with.
[2939.40 --> 2947.68]  As we wind up, do you have any thoughts from either of you or both of you about what you're expecting to see over the next few years?
[2947.68 --> 2949.62]  How you think things will change?
[2950.68 --> 2953.92]  What that outweighs a little bit looks like?
[2954.52 --> 2955.74]  Yeah, so I'll get started.
[2955.86 --> 2964.40]  I think we're going to see more deception used by attackers leveraging AI, especially with deep fakes.
[2964.54 --> 2969.24]  I think that's a very powerful application of AI to offensive capabilities.
[2969.24 --> 2974.46]  We already see a trend in the increase of volume and scale, right?
[2974.48 --> 2983.04]  I think that's one of the key things that AI also enables its hackers with, which is the augmenting their existing capabilities, make them scale.
[2983.52 --> 2986.30]  But that's exactly what defenders can do as well, right?
[2986.80 --> 2990.38]  But the main thing is starting with the definition of the problem.
[2990.46 --> 2994.22]  I think that's the most powerful question you can ask as a defender.
[2994.34 --> 2996.62]  Like, what is the problem I'm trying to solve?
[2996.62 --> 3003.36]  Because AI or any other technology, it doesn't really change the mission of your organization, right?
[3003.40 --> 3006.22]  Are you a hospital, small hospital or a large hospital?
[3006.52 --> 3014.34]  Your goal, your mission is to protect the citizens, the people that go to have care.
[3014.86 --> 3020.24]  And you don't want this environment to get ransomed and admissions to be done by pen and paper.
[3020.50 --> 3024.10]  So people could effectively die because they didn't get admitted to the hospital.
[3024.56 --> 3026.54]  That's the kind of thing that we're looking at here, right?
[3026.54 --> 3030.36]  Protecting critical infrastructure, protecting the school where our kids go to.
[3031.34 --> 3034.22]  So AI doesn't change the mission of your organization.
[3034.48 --> 3038.78]  AI doesn't change even the approach, the strategic approach to cybersecurity.
[3039.36 --> 3047.20]  You just need to find out where are the areas that can help you to scale and maybe cover some of the gaps that you have.
[3047.20 --> 3049.46]  And I think we talked a little bit about that, right?
[3049.50 --> 3059.20]  But improving detection and response times, disrupting attacks at specific places of the attack chain, giving you the ability to contextualize a lot of data to give you some...
[3059.20 --> 3062.26]  I'm a firm believer in the human machine teaming, right?
[3062.26 --> 3063.20]  To give you some input.
[3063.20 --> 3068.28]  So now the human can, with that information, take an action.
[3068.28 --> 3076.46]  And then also the models, the machine learning models, learning from that to effectively combine that human machine teaming, right?
[3076.50 --> 3082.14]  That Blade Runner, or in this case, the replicant, that takes the best out of both worlds.
[3082.42 --> 3085.12]  That's kind of my vision about that.
[3085.12 --> 3086.88]  I'll chime in on that as well.
[3087.50 --> 3099.78]  The top five companies in the world by market capitalization right now are tech companies, all founded or co-founded by individuals with heavy technical background.
[3100.16 --> 3105.00]  This is very unique in this era that we find ourselves in now.
[3105.00 --> 3109.36]  This is changing leadership in a way that we...
[3109.36 --> 3114.24]  Leadership, entrepreneurship, and just vision and strategy in a way that we haven't seen before.
[3114.24 --> 3128.50]  I think we're at a unique precipice to where we can maximize some technological applications that 10, 20 years ago, we wouldn't have even been having the conversation.
[3128.62 --> 3135.52]  The technology was there, was readily available, like AI that was written in textbooks in the late 1950s.
[3135.90 --> 3137.62]  The technology has been there.
[3137.62 --> 3145.64]  It's being popped into the forefront now because of that seismic shift where the biggest companies are tech companies.
[3146.02 --> 3149.40]  So my daughter, who's 15 years old, is very tech savvy.
[3149.64 --> 3153.58]  When I was 15 years old, I was an oddball because I was tech savvy.
[3153.72 --> 3156.06]  Like they looked at me like, you know, I had three heads.
[3156.52 --> 3158.08]  So what do I predict?
[3158.08 --> 3167.52]  I predict we're going to see acceleration in how those types of use cases and opportunities and candidly business opportunities are going to appear.
[3167.52 --> 3169.52]  But I also see...
[3169.52 --> 3171.30]  So there's always the positive and the negative.
[3171.30 --> 3194.80]  I see a risk, a huge risk of moral and character failures at the level of those leaders who have an unbalanced sense of high technical prowess, but potentially low morals, potentially low leadership acumen, potentially low spiritual acumen.
[3194.80 --> 3198.14]  There's an opportunity to balance that out as well.
[3198.54 --> 3200.70]  Personally, that's where my focus is.
[3200.76 --> 3210.10]  That's how I met Daniel from this podcast because his, you know, we've spoken at events or met each other at events where we're trying to talk about those types of topics.
[3210.44 --> 3219.80]  You know, how do you pull together technology and other things that are more from a moralistic perspective and, you know, help have the technology, but balance that out and vice versa?
[3219.80 --> 3227.20]  I think that's where we're going to have to be very cautious that we don't over-rotate and, you know, end up accidentally...
[3227.20 --> 3238.28]  And I'm not talking about politics now at all, but end up accidentally handing the reins over to people whose gifting got them to a place where their character potentially could not sustain them.
[3238.74 --> 3240.94]  And I think we're at very big risk of that.
[3241.02 --> 3245.30]  So those are the two things that I see kind of for the future, both opportunity and risk.
[3245.30 --> 3247.86]  Fantastic insights from both of you.
[3248.28 --> 3251.70]  Gentlemen, thank you very, very much for coming on the show.
[3251.78 --> 3252.70]  It was a great conversation.
[3252.88 --> 3253.64]  I learned a lot.
[3254.76 --> 3263.22]  And I hope I can, as things progress going forward, I hope you guys will come back on and give us updates on where cyber is going forward.
[3263.84 --> 3264.94]  Love having you on the show.
[3265.02 --> 3265.38]  Thank you.
[3265.90 --> 3266.30]  My pleasure.
[3266.60 --> 3267.10]  Thank you, Chris.
[3267.26 --> 3267.86]  Thank you, Chris.
[3267.86 --> 3267.92]  Thank you, Chris.
[3267.92 --> 3267.98]  Thank you, Chris.
[3267.98 --> 3269.92]  Thank you, Chris.
[3269.92 --> 3271.86]  Thank you, Chris.
[3271.86 --> 3273.92]  Thank you, Chris.
[3273.92 --> 3274.92]  Thank you, Chris.
[3274.92 --> 3276.36]  All right.
[3276.74 --> 3278.56]  That is our show for this week.
[3279.20 --> 3284.86]  If you haven't checked out our ChangeLog newsletter, head to changelog.com slash news.
[3285.08 --> 3287.34]  There you'll find 29 reasons.
[3287.54 --> 3290.90]  Yes, 29 reasons why you should subscribe.
[3291.38 --> 3292.76]  I'll tell you reason number 17.
[3293.34 --> 3296.10]  You might actually start looking forward to Mondays.
[3296.26 --> 3298.96]  Sounds like somebody's got a case of the Mondays.
[3299.32 --> 3303.92]  28 more reasons are waiting for you at changelog.com slash news.
[3303.92 --> 3309.82]  Thanks again to our partners at Fly.io to Breakmaster Cylinder for the Beats and to you for listening.
[3310.26 --> 3312.86]  That is all for now, but we'll talk to you again next time.
[3312.86 --> 3317.04]  Thank you.
[3317.04 --> 3320.92]  Bye.
[3320.92 --> 3321.40]  Bye.
[3321.46 --> 3321.54]  Bye.
[3321.54 --> 3322.32]  Bye.
[3322.32 --> 3322.68]  Bye.
[3322.68 --> 3323.24]  Bye.
[3323.24 --> 3323.90]  Bye.
