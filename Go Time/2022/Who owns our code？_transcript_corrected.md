[0.00 → 6.04] If you manufactured a car wheel and the car wheel explodes because you used bad materials in that
[6.04 → 12.04] case in the car wheel, then we have some well-developed laws and intuitions around like,
[12.14 → 17.16] okay, well, we sue the car wheel manufacturer. Software doesn't have any of that really yet.
[17.42 → 21.70] We've sort of operated in this rules-free zone where everybody was like,
[22.08 → 28.76] software's so cool. I guess we'll just let it happen. And I think that age is coming to an end.
[30.00 → 38.14] This episode is brought to you by our friends at Square, developing the platform that sellers
[38.14 → 42.44] trust. Here's what you can do with Square. You can bridge more experiences. You can build online,
[42.66 → 47.24] mobile, and in-person commerce experiences that connect more customers and sellers.
[47.62 → 51.78] You can build custom booking solutions. You can create and track orders. You can accept payments.
[51.78 → 56.34] You can manage and curate inventory. You can organize customers. You can manage employees.
[56.34 → 62.60] You can extend Square gift cards to your app. You can use Afterpay. And all this is powered by the
[62.60 → 68.48] world-class Square APIs and SDKs that enable you to build full-featured business apps for yourself
[68.48 → 73.26] or millions of Square sellers. So much is available as a Square solutions partner.
[73.70 → 79.04] Learn more and get started at changelog.com slash Square. Again, changelog.com slash Square.
[79.04 → 101.84] Let's do it. It's go time. Welcome to go time, your source for diverse discussions from all around
[101.84 → 107.64] the go community. We record live each and every Tuesday at 3 p.m. U.S. Eastern. Subscribe at
[107.64 → 113.84] YouTube.com slash changelog to be notified and join the Go Time FM channel of Go4Slack to chat along with us.
[114.20 → 118.90] Special thanks to our partners at Vastly for delivering Go Time superfast all around the world
[118.90 → 126.62] and to Fly.io. Deploy your app servers close to your users. Learn more at Fly.io. Okay, here we go.
[126.62 → 140.20] Hello and welcome to Go Time. Today we are going to be talking about who owns your code. A question
[140.20 → 144.42] that certainly has been on my mind. So we're going to be exploring who owns the code. The company,
[144.64 → 149.96] is it the engineer, is it the team, is it all the open source contributors if it's a project.
[150.30 → 156.02] How about when you're using AI, machine learning, GitHub Copilot. Is it still your code?
[156.68 → 162.04] I'm really excited. We have a really brilliant guest with us today. We have Louis Veer, who is a
[162.04 → 168.40] programmer turned attorney who has been involved in open source since college. He's worked at
[168.40 → 175.26] Marcella, where he revised the Marcella public license at Wikimedia Foundation, where he also
[175.26 → 180.66] briefly led the community team. And as a lawyer, he's worked with Google, Amazon, and many other small
[180.66 → 186.26] startups. So currently he's the co-founder at Tide lift, which works to make open source better
[186.26 → 192.32] for everyone by paying maintainers. We'll hear more about that. But before that, I'd like to introduce
[192.32 → 197.58] our co-hosts. We have Chris. Hi, Chris. I haven't seen you in a hot second.
[197.58 → 205.14] Hello. I am back after a very, very long but much needed break. So I'm feeling rested, and I'm ready
[205.14 → 209.74] to get into the meta of this Who Owns Code. It's going to be fun.
[210.24 → 216.14] You're ready. I'm ready. It's a very interesting topic. And the beautiful Natalie, I've seen you,
[216.14 → 221.88] I think, far too often for your own liking in recent weeks, my wonderful co-hosts.
[221.92 → 224.38] It's like our weekly one-on-one, but it's not one-on-one.
[224.58 → 228.06] Weekly one-on-one with anyone who decides to tune into the live.
[228.98 → 230.44] Weekly anyone. I like that.
[230.58 → 234.12] Yeah, weekly anyone. Beautiful. Natalie and I don't do one-on-ones, we do anyone's.
[234.76 → 235.82] That sounds terrible.
[239.76 → 244.86] Lewis, would love to hear a little bit more about you and your thoughts on code ownership.
[244.86 → 252.20] Well, you know, it's been a long time since I wrote anything approaching useful code,
[252.38 → 257.72] but I've been involved. I had an interviewer ask me while I was interviewing for my first law school
[257.72 → 263.00] job out of law school, law firm job out of law school. And they said, well, why, you seem to
[263.00 → 267.88] really like tech. Why did you leave tech? And I said, look, I'm not leaving tech. Like I am only
[267.88 → 273.00] interviewing with law firms that are very much tech forward, tech first kind of law firms, right?
[273.00 → 279.50] So the goal was never to leave tech. The goal was I was at a startup, open source, back in the first
[279.50 → 285.46] year of the Linux desktop, I was at a small startup. We got acquired. During that acquisition process,
[285.46 → 292.60] I worked with the attorneys, and I was arrogant. I was young. I was like, oh, I can do a better job
[292.60 → 297.50] than these people. So I decided after a little bit of experimenting, and I took like a night school
[297.50 → 302.44] law class that I enjoyed, a couple of night school law classes that I enjoyed. And so I decided to go to law
[302.44 → 308.38] school, right? But the goal was always all along to continue to focus on tech and specifically very
[308.38 → 315.10] much to focus on open law, because there seemed to me at the time to be a body of lawyers who were
[315.10 → 322.26] sophisticated about technology, but they came at it very much from a patent first, control first kind
[322.26 → 327.04] of mindset. And that was something that was already starting to break down at the time. So I was in law
[327.04 → 335.66] school 2006, 2009. And it was beginning to be an understanding amongst legal academics that open was a
[335.66 → 343.64] thing. I had attended a conference of legal academics where Creative Commons was announced. That was 2001. So there
[343.64 → 350.20] were some legal academics who got it, right? And in fact, I pretty only applied to law schools that had at least one
[350.20 → 356.12] faculty member who had written something that indicated that they got it in the slightest amount.
[356.20 → 359.32] So that meant applications were easier because there wasn't that many schools to apply to.
[359.82 → 363.78] And I think that has worked out well, right? It's been a good career. It's been a fun career,
[363.90 → 371.28] right? Because I very much, you know, the point was not that, oh, I can like to make my piles of money and
[371.28 → 376.64] work 3000 hours a year or whatever it was. I have friends who are open lawyers who deserve better
[376.64 → 380.70] layering than the layering that they were getting at the time. And I think that's been
[380.70 → 388.28] that sense of, hey, I'm doing this to help open people get better layering has served me well as
[388.28 → 394.00] a sort of motto and mission and has led to a lot of fun outcomes, right? I mean, because open people
[394.00 → 398.06] are doing a lot of fun projects, have been doing a lot of fun projects, and that hasn't changed.
[398.20 → 402.80] And I certainly don't think it's going to change anytime soon. But a lot of it does come back to this
[402.80 → 408.66] question of like, who owns the thing, right? And I admit, I have enough lawyer brain worms at this
[408.66 → 413.36] point that my immediate thought goes to like, okay, well, the contract of the and the one of you
[413.36 → 417.30] during the top prep said, well, you know, well, what about like team ownership? And I was like, oh,
[417.70 → 424.70] right. We talk in law school about this analogy that ownership is for reasons I don't remember,
[424.70 → 430.40] or maybe never knew. We talk about ownership being a bundle of sticks. And the idea is that we sort of
[430.40 → 435.98] we talk about it as if it's like one big trunk. But it's actually like, a lot of different small
[435.98 → 442.52] things, right? And ownership in the code world is very fragmented, because there's a sense of like,
[442.60 → 447.82] well, okay, for almost all of you, if you are working for a company, at the end of the day,
[448.38 → 454.02] your company owns the code that you are writing, at least on the company time, as long as you're unless
[454.02 → 459.78] you're very careful to like, not do it on company time, not do it on company hardware, and to do it in
[459.78 → 464.24] areas that are unrelated to what the company is working on. If you're doing those things,
[464.24 → 469.54] and you keep it, but otherwise, as a general rule of thumb, the company owns it. So that's like the
[469.54 → 473.58] sort of lawyer brain answer, like, well, yeah, okay, we're done here. You know, it's been a nice
[473.58 → 479.82] podcast. Glad to talk to you all. But there's very much, of course, all these fractal little senses of,
[480.62 → 485.04] well, okay, but what does it mean when the team, you know, team versus individual ownership?
[485.04 → 489.60] Because in some, like in a lawyerly sense, like the company is the one who can sell it,
[489.60 → 494.74] but who has responsibility for it within the company? Like, that's not a legal question. That's
[494.74 → 502.40] a that's a team norms, team behaviours kind of question. And there's also these questions of
[502.40 → 506.92] what exactly is it that you own, right? Because I spent several years of my career, I am a
[507.46 → 512.30] what we call a transactional lawyer, like basically, I do contracts. If the contract goes wrong,
[512.30 → 516.88] for some reason, that is somebody else's problem to argue about it in court. And so I've only ever
[516.88 → 523.52] been to court for work once, which was a little case called Oracle v Google. And you might've heard
[523.52 → 531.78] of that one. And the question at some level was about who owns or can anyone own the idea of an API,
[532.74 → 536.08] right? And that's probably not something you're thinking about too much in your day to day,
[536.18 → 541.12] right? And your corporate lawyers probably aren't most of the time either. They're not thinking about
[541.12 → 546.08] who owns the API. They're just thinking about like this file, right? Or this binary that we're
[546.08 → 552.06] distributing, or these days, often this SAS that we're putting out over the internet, you know,
[552.06 → 558.04] your customers never actually see code except for whatever's Java Scripted or WASM or whatever. But,
[558.42 → 562.18] you know, and of course that's a whole nother thing. Anyway, I mean, it's just fractal, and we could
[562.18 → 567.72] talk about it for way more than an hour, but that's sort of my like 10,000-foot overview is that it's,
[567.72 → 573.70] there's both this ownership in the legal sense, but very much also in the code and culture sense.
[574.06 → 577.86] And we can talk about any or all of those, including, you know, to some extent how Go is
[577.86 → 582.78] different. I mean, its packaging system is one of those things that occasionally makes lawyers
[582.78 → 588.60] tear their hairs out a little bit because it's not something so many of our lawyers, not our lawyers,
[588.60 → 595.18] well, our lawyers too, but our licenses predate Go, right? They predate some modern language
[595.18 → 600.38] distribution practices. And sometimes that shows up. We wrote technology specific things
[600.38 → 606.82] for like C or C++ into our licenses. And then somebody says, well, how does that work in the
[606.82 → 611.88] case of Go? And the answer is, I have no idea. I guess those, those of you listening to this as a
[611.88 → 617.32] podcast can't see the face I just made. So just assume like perplexed search Giphy for your favourite
[617.32 → 621.76] perplexed GIF. And that was me just now. So yeah, so where do you all want to start with that?
[621.76 → 627.22] I also have a kind of meta view of some of this because I think similar to what you were,
[627.50 → 631.68] the line of thought you were going down where it's like, okay, well, there's the code that you've
[631.68 → 637.68] typed, the thing that you've written, but then there's like the knowledge of writing it and the
[637.68 → 642.18] idea of the thing. And that's where like the API question is very interesting because it's like,
[642.24 → 649.28] oh, well, someone else, like if you retype the same code, is that the same thing? Or like,
[649.28 → 653.28] what if you type it slightly differently, but it's conceptually the same thing? Like how far do you
[653.28 → 658.00] have to get away from, how different does something have to be before it's like, okay,
[658.80 → 664.56] now someone else can own this thing? I remember over the years talking to lawyers about, you know,
[664.60 → 668.32] all the non-competes and things that we tend to have. And one of the things that lawyers consistently
[668.32 → 674.16] told me, at least in New York, is that like your employer has no right to the knowledge that you
[674.16 → 678.62] gain. So they can have ownership over the code that you write and the things that you produce,
[678.62 → 682.40] but they're not allowed to say, well, we gave you this knowledge, so you can't take it over there
[682.40 → 686.96] and use it against, in one of our competitors. I'd always find that very interesting as well,
[686.96 → 690.80] because it's like, oh, well, this is like another aspect of things. It's like, is an API
[690.80 → 695.58] knowledge or is it like the code that you've written or is it, so there's this really meta aspect
[695.58 → 701.40] for me, at least to the whole idea of ownership. Oh, yeah. I mean, absolutely. Right. And by the way,
[701.52 → 707.82] you know, you specifically called out New York and Natalie said in pre-chat that she wanted to ask about the EU,
[707.82 → 713.68] we as open source programmers and open source developers of various sorts tend to make an
[713.68 → 721.26] assumption that we can write a license that applies across the entire world. And in most law,
[721.44 → 727.72] that's like a completely laughable idea, right? Like somewhere between laughable and like actively
[727.72 → 735.66] considered harmful. And so we're sort of lucky in some ways that the core concept of copyright,
[735.66 → 743.00] which is what applies to that actual written thing distinct from the ideas is actually a global
[743.00 → 751.96] standard, a treaty called the burn convention. That's 1908, maybe 1903. So copyright has been
[751.96 → 755.86] standardized across the entire world for a hundred years, which makes it a good platform for lawyers
[755.86 → 761.42] to build a global system on. If you're talking about databases, no global platform,
[761.42 → 766.86] no global legal platform. So writing a database license is responsible for a lot of these gray hairs.
[767.04 → 772.04] Again, sorry, podcast listeners, you should watch it live next time. And similarly with AI,
[772.86 → 777.40] we don't know how some of this is going to play out. We can offer guesses. And frankly,
[777.48 → 781.56] they're very interesting guesses. It's a very fun theoretical game, but we don't know how it's going
[781.56 → 785.56] to play out in court. And by the way, Chris, I think the other meta thing that's really
[785.56 → 793.34] interesting for programmers, I often like to remind developers that writing a contract is like
[793.34 → 798.52] writing code and then not executing it at all. And you just sort of are reading it. And like,
[798.58 → 803.54] we all agree more or less on what the output should be. But until it's actually been executed,
[803.54 → 809.46] which happens through a court, right? A court says, this is what the thing is, then we don't
[809.46 → 815.76] actually know what the outcome is. So everything that I say here is going to be based on like a
[815.76 → 820.32] handful of things, right? Part of the challenge in Oracle v. Google is that we'd all been operating
[820.32 → 826.00] under these assumptions about what copyright law was, but there had been no litigation over what,
[826.36 → 832.04] whether an API could be copyrightable since the 80s. So the closest analogy we had was
[832.04 → 839.16] Lotus 1, 2, 3 dropdown menus. And like, it turns out things have changed a lot since then.
[839.16 → 846.38] But because it hadn't been executed by a court, we really didn't know how this was going to turn
[846.38 → 850.60] out. And so that makes predictions. This is why lawyers' favourite phrase is, it depends.
[851.00 → 855.74] There's one thing I want to stick a pin in before we move on, Angelica. And it's that idea of AI.
[856.64 → 860.26] And I also want to call out code generation. And I really want to talk about that later,
[860.30 → 864.14] because I think that's also like a very interesting thing when you, the first thing you said was like,
[864.20 → 868.82] oh, who's typing the code at the end of the day? And that's how copyright is generated. So I just want to
[868.82 → 871.38] make sure we circle back to that later. Absolutely.
[871.84 → 874.66] I also want, for those of us who weren't following that Google
[874.66 → 881.26] law case step by step, every step of the way, once it had been litigated, what was the conclusion?
[882.08 → 888.88] Well, so to take a step real quick back just to the very beginning, Oracle, well, Sun had created Java.
[888.88 → 897.84] And originally the Apache project sort of funded by IBM had re-implemented Java, complete clean room,
[898.38 → 902.96] very strict, very effective clean room, as best as we could tell from the pieces afterwards,
[903.24 → 908.72] literally just a handful of lines, probably out of several hundred thousand in that re-implementation
[908.72 → 913.44] that ended up looking like they were actually perhaps copied and pasted rather than
[913.44 → 921.84] a true clean room re-implementation. And so Google used that Apache re-implementation in their Android
[921.84 → 930.38] phones. And ultimately what happened after literally a decade of litigation, I think I was on my fifth
[930.38 → 936.64] job by the time the case ended, like from when the case, actually six jobs from when the case started
[936.64 → 943.80] to when the case ended. The case started with essentially Oracle claiming, there's some other
[943.80 → 949.10] stuff I'm going to leave out for simplicity, but Oracle claimed that copying and re-implementing
[949.10 → 956.04] just the API headers was a copyright violation and that therefore all of Android should have to be
[956.04 → 960.76] licensed from Oracle for, they originally asked for 5 billion. I think by the end of the case,
[960.80 → 964.26] they were asking for 9, 15 billion, something like that.
[964.26 → 969.74] The courts found essentially through a series of rulings over the years in this case,
[970.04 → 980.14] that an API could be copyrightable, independent of the implementation, but there was a plausible,
[980.36 → 987.32] what we in the US call a fair use argument that essentially if you re-implement in a way that's
[987.32 → 992.16] particularly transformative, right? Like you're doing something that is really different from what
[992.16 → 1000.10] the original authors or copyright owners of the API intended to do with the API, then you have an
[1000.10 → 1005.32] argument that it's okay to reuse that API in that way through re-implementation.
[1006.30 → 1011.60] Lawyers like to say that fair use is simply the right to get sued. It's ambiguous. It's one of these
[1011.60 → 1016.58] things where, again, you can't know ahead of time what the outcome is going to be. And that,
[1016.58 → 1022.04] of course, makes it a playground mostly for large companies, unfortunately, right? So I think in
[1022.04 → 1026.46] some ways that was not a great outcome. It was a better outcome for open source than what could
[1026.46 → 1030.72] have been, than what Oracle wanted to have, but it wasn't an ideal outcome.
[1030.72 → 1048.54] Hey friends, this episode is brought to you by my friends and potentially your friends too at
[1048.54 → 1053.80] Fire hydrant. And I'm here with Robert Ross, founder and CEO of Fire hydrant. And Robert,
[1053.96 → 1059.32] there are several options out there for incident management, but what is it that makes Fire hydrant
[1059.32 → 1064.20] different? The reason that we think that Fire hydrant is, is onto something is because we're
[1064.20 → 1070.28] meeting companies really where they are. We face the same problems that every company in the industry
[1070.28 → 1076.26] that is building and releasing software is also facing. So where you want people to be able to sign
[1076.26 → 1082.64] up for Fire hydrant and immediately be able to kick off an incident using the best practices that we've
[1082.64 → 1087.18] built, and we've experienced and have gathered through the other amazing customers that use our tool.
[1087.18 → 1092.50] It really is a very quick time to value. And we want people to have a long jump from where they
[1092.50 → 1099.16] are to where they want to be in incident management. I love it. Thank you, Robert. Small teams up to 10
[1099.16 → 1103.86] people can get started for free with all Fire hydrant features included. There's no credit card required
[1103.86 → 1110.06] to sign up. They are making it too easy to get started. So check them out at firehydrant.com. Again,
[1110.06 → 1112.06] firehydrant.com.
[1112.06 → 1114.92] So
[1114.92 → 1121.76] do you want to ask? One step back. And when we talk about code ownership, what exactly does it
[1121.76 → 1142.28] I want to ask one step back and when we talk about code ownership what exactly does it mean
[1142.28 → 1147.82] I own the code whether I am an individual a company or anything does it mean I'm allowed
[1147.82 → 1153.58] to make money of it does it mean I can print it and hang it at home does it mean something else
[1153.58 → 1160.70] well I'm going to give you my lawyer answer to that those of you who whose GitHub accounts do things
[1160.70 → 1165.10] other than commit to other licenses which is pretty much all I do these days with my GitHub
[1165.10 → 1170.48] account will have better notions of code ownership as a cultural practice among programmers right like
[1170.48 → 1174.38] who's responsible I do want to talk a little bit about that one but let me put a pin in that come
[1174.38 → 1181.98] back to it the basic system since the at least the 60s in the US I'm not sure exactly the timeline
[1181.98 → 1189.64] in the EU, but I would imagine similar is that well actually let me go back even further copyright is
[1189.64 → 1196.88] intended to protect creative works so what do you have to do to get copyright in a thing, and I'll
[1196.88 → 1201.56] explain what copyright is in a second but let me start with what it what you have to do and what
[1201.56 → 1206.34] you have to do is you have to write down something that's creative write-down can be broad right it
[1206.34 → 1212.56] can be sculpting or you have to take it out of your head and put it out into the real world in
[1212.56 → 1218.38] some way that can be typing it in a computer can be like I said sculpting it into a sculpture sculptures
[1218.38 → 1224.22] can get copyright it can be a work of art you know so it can be oil painting or whatever it can be a
[1224.22 → 1229.86] vim poster I mean I'm an honestly these days my development environment is word, but I used to be an
[1229.86 → 1237.22] Emacs guy so that is the key thing is you are doing a creative thing and can be mediated by tools and
[1237.22 → 1244.38] Chris this gets to your point about the know AI and where is copyright in there you know it can be
[1244.38 → 1250.18] mediated by a typewriter or a paintbrush, or I believe that we don't really know for certain, yet it can be
[1250.18 → 1257.44] mediated by an AI, but you are doing some creative something and turning that into a fixed thing all
[1257.44 → 1261.30] right so what happens once you've done that actually before I get into what happens once you've done that
[1261.30 → 1268.92] is I think there's an important exception that's in the US at least that creative like what does it mean to be
[1268.92 → 1274.98] creative is not zero it's pretty close to zero, but it's not zero there's an important case called Feist
[1274.98 → 1281.26] versus rural telephone and the holding of that case is literally telephone books aren't creative and so
[1281.26 → 1285.64] they don't get copyright because what's the point of a telephone book the point of a telephone book is to
[1285.64 → 1290.60] literally just mechanically go through a town and have phone numbers for everybody so it's not
[1290.60 → 1296.94] it's hard work, but it's not creative and in the US at least you have to have some kind of creative
[1296.94 → 1302.24] something so if you do like a phone list of the hundred most awesome people in New York City
[1302.24 → 1309.38] that's creative right you had to select one of the ways which you can be creative under US copyright law
[1309.38 → 1315.48] is selection if you pick those hundred people then hey you've done something creative your list of
[1315.48 → 1320.94] hundred people is copyrightable but if you're just every single person who lives in Manhattan that's
[1320.94 → 1328.78] not creative you don't get protection and that plays into questions of databases and ultimately I
[1328.78 → 1332.98] think, and we might not have time to get time to get to this today but the question of the models
[1332.98 → 1339.00] themselves right because there's both the output of models what's the copyright on that and the
[1339.00 → 1343.76] models themselves we don't actually know if they're copyrightable that may be too esoteric might have
[1343.76 → 1347.92] to invite me back for another one for that you know but okay so you've you've created this thing
[1347.92 → 1352.66] so now what do you do so now you've got copyright what does copyright let you do copyright lets you
[1352.66 → 1358.54] control what others can do with it right it lets you decide who gets to use it who gets to share who
[1358.54 → 1365.04] gets to redistribute it who gets to modify it within certain limits, but it's pretty strong right so the
[1365.04 → 1371.10] limits include what's called first sale doctrine which is uh hey I sold it to somebody they can
[1371.10 → 1377.08] usually sell it to one other person first sale doctrine made a lot more sense in the era of like
[1377.08 → 1382.90] books and like that's what creates used bookstores is for sale doctrine it means that I bought the
[1382.90 → 1389.72] copyrighted thing, and now I can give it to a used bookstore, and they can resell it um in the digital age
[1389.72 → 1395.18] for sale doctrine is a little more complicated um but suffice to say like that's one of the
[1395.18 → 1402.38] limitations similarly fair use says hey if you're using this for education if you're using this for
[1402.38 → 1407.40] non-profit purposes I'm oversimplifying a little bit here the tests around fair use can be a little
[1407.40 → 1415.10] complicated critically in our digital age fair use in the U.S. has expanded quite a bit to include
[1415.10 → 1421.00] what's called transformative use which is to say hey you're doing something super new super different
[1421.00 → 1428.02] courts are often going to allow that in the name of sort of not impeding progress so for example
[1428.02 → 1434.80] google book search is in some sense like the biggest copyright violation in all history right
[1434.80 → 1441.04] because it's literally copied systematically millions of books made these digital copies but then
[1441.04 → 1447.82] a court said well, but actually it's so different it's so great, and they put strict controls around
[1447.82 → 1454.08] you know you can only get a few pages at a time and authors can opt out if they want after the copying
[1454.08 → 1460.80] has been done so like google book search is a good example of what transformation means and potentially
[1460.80 → 1466.68] analogous to what copilot is doing right, but we don't know I mean the flip side of this right is that
[1466.68 → 1472.32] we just had court cases we had a court case a couple of years ago about the song blurred lines some of you
[1472.32 → 1479.10] might have heard right and courts there has actually said that even just sort of copying the style of
[1479.10 → 1486.22] the artist could potentially be a copyright infringement which was a big surprise to a lot of a lot of lawyers
[1486.22 → 1492.34] a lot of lawyers still unhappy about that case next week there's going to be or no tomorrow morning
[1492.34 → 1498.72] actually maybe there's going to be a case about Andy Warhol doing and a photograph of prince that
[1498.72 → 1504.64] Andy Warhol transformed into one of his Andy Warhol canvases and the supreme court like it's a little
[1504.64 → 1508.90] weird, but I think that case might actually have a lot of impact on artificial intelligence because
[1508.90 → 1514.52] we've all done we've all played with Stable Diffusion or mid-journey or open AI or whatever
[1514.52 → 1521.84] to create foo in the style of bar right well if bar is still alive and still has a valid copyright
[1521.84 → 1527.60] maybe that's a problem we don't really know, yet I saw a research paper yesterday that said
[1527.60 → 1535.88] if you prompt copilot to do code in the style of forgetting the guy's name Petrov I think a top
[1535.88 → 1542.74] python programmer that you actually get fewer vulnerabilities in your code if you prompt copilot
[1542.74 → 1550.50] with the name of a top maintainer and flip side the paper's author was honest enough to note that
[1550.50 → 1555.40] they prompted with their own name and the number of vulnerabilities went up which I thought was
[1555.40 → 1561.82] nice and humble of them, so style is an issue that's gonna that could potentially come up in code as well
[1561.82 → 1566.92] that was a very long-winded answer to your question Natalie I apologize no that was interesting so you
[1566.92 → 1573.48] said that for code ownership basically means who is allowed to sell and profit of that who is allowed to
[1573.48 → 1585.92] give it their own personal interpretation yeah it's also who's who's there to answer in case of a problem right I wrote a piece of code that made my work lose a lot of money
[1585.92 → 1600.48] ownership on me yeah I mean so that's where it gets complicated, and we have perfect answers for that in the case of things like if you manufactured a car wheel and the car
[1600.48 → 1612.92] wheel explodes because you used bad materials in that case in the car wheel then we have some well-developed laws and intuitions around like okay well we sue the car wheel manufacturer
[1612.92 → 1624.50] software doesn't have any of that really, yet we've sort of operated in this rules-free zone where everybody was like software so cool I guess we'll just let it happen
[1624.50 → 1643.16] and um I think that age is coming to an end to be perfectly honest actually I think the European Union has published in the past year including one last week two weeks ago papers on liability for software right I the idea of
[1643.16 → 1654.32] if a car wheel explodes and causes a car accident we have a very clear idea of how we should figure out who is liable for that if an AI goes wrong or
[1654.32 → 1666.34] software goes wrong and the car goes off the road and causes the exact same accident we actually have very little idea how we should apportion liability right, and it's not necessarily about
[1666.34 → 1676.80] oh like that is for practical reasons those kinds of things tend to look the same right because at the end of the day the company that commissioned the code is also the company that sold the product
[1676.80 → 1688.54] so you tend to see those things tied together, but there's no formal reason for that right like copyright law doesn't especially because copyright law historically was about like things that didn't cause car crashes
[1688.54 → 1704.42] right historically copyright law like literally modern copyright law in the US is in large part because of player pianos like scrolling wheels like what you saw in West world like scrolling wheels with little punch holes that caused the piano to do things like pianos didn't run off and like to kill people
[1704.42 → 1715.46] so copyright law doesn't really have much to say inherently about product liability and that's something that we are I think screaming towards a very high velocity
[1715.46 → 1721.00] at least in the EU and I suspect because of AI in the US soon as well
[1721.00 → 1728.40] I feel like there's an interesting component to that as well because when you think about what we create we're just creating words on a page like
[1728.40 → 1737.04] the manufacturing process of turning that into something that does something is not necessarily something that the person who wrote the code does
[1737.04 → 1744.90] so it's like something that somebody else does and then there's all the like well the machine you run it on like if a bug does happen with like a car that's driving
[1744.90 → 1751.82] is it the fault of the person who wrote the code is it the fault of the machine is there a problem with the machine who like who gets the blame and I think that gets
[1751.82 → 1758.84] extremely murky because we're dealing with such like new stuff that we have never had in like the existence of humanity
[1758.84 → 1770.04] yeah I mean the original history of this in like the English and US law systems was that literally like to get to that point where hey the car wheel
[1770.04 → 1778.88] explodes we should sue the car manufacturer involved a lot of people dying in train accidents and the train companies being like oh, but that's not
[1778.88 → 1803.66] our fault we just laid the tracks bought the train bought the coal it's the guy who was driving its their fault so you can't sue us and that actually like as a matter of law was like a good argument for decades and then the number of accidents as trains became ever more present as part of our economy as part of simply how things moved around well the technological change
[1803.66 → 1811.52] drove a change drove a change in understanding right because that rule was originally from like hey some dude on a horse
[1811.52 → 1824.94] it's not my fault if he's like my squire or whatever pick your ancient British legal term you know if they're out on my horse like genuinely it's sort of not my problem if they like caused an accident
[1824.94 → 1831.70] you know I mean yeah I own the horse but like and so the train companies for a long time were like well look it's just like a horse
[1831.70 → 1838.32] this train is just like a horse I can't be responsible and so at some point the legal system was like actually this is ludicrous
[1838.32 → 1844.32] and so a combination of courts and congress changed the rules to make the train companies more liable
[1844.32 → 1853.50] no surprise the trains then started getting safer yeah Angelico I've actually got a British person on this podcast I believe, so why am I not asking you the proper terms here
[1853.50 → 1855.32] yeah sometimes the footman's fault
[1855.32 → 1862.04] well that's exactly it right it's the footman's fault, and so I think we're seeing we are is both an exciting and a terrifying time
[1862.04 → 1868.62] for lawyers that we are in the midst of one of these very rare technological changes right we are
[1868.62 → 1874.94] AI I think in particular is going to be that new train nobody really understands nobody wants to take responsibility
[1875.52 → 1882.32] for Chris as you say like perfect reasons this stuff is literally the most complicated system ever built by humankind
[1882.32 → 1886.26] we like even in the best case have only the vaguest sense of how it works
[1886.26 → 1890.70] and like good luck explaining it to a judge
[1890.70 → 1894.00] I had a conversation with some lawyer friends last week that was like
[1894.00 → 1898.32] how would you explain and these are like fairly sophisticated
[1898.32 → 1902.74] you know like most either are programmers or one of the people is like married to a programmer
[1902.74 → 1906.88] like we're fairly, and we've been doing tech law all for cumulatively many decades
[1906.88 → 1909.32] how would you explain machine learning to a judge
[1909.32 → 1914.60] and we all just sort of stuttered in horror at that thought right because it's a really
[1914.60 → 1918.00] again I mean even to programmers who haven't thought about it
[1918.00 → 1920.12] it can be really hard unintuitive
[1920.12 → 1924.50] the vocabulary is changing all the time the technology is changing all the time
[1924.50 → 1926.88] and to try to explain it to congress
[1926.88 → 1929.70] or to a judge is a scary proposition
[1929.70 → 1932.00] it's an exciting whoever gets to do it first
[1932.00 → 1935.20] that's going to be a super great lawyer job for somebody
[1935.20 → 1938.88] but also like boy when you screw it up
[1938.88 → 1941.74] and we felt a lot of pressure in the Google oracle trial right
[1941.74 → 1945.64] that this was something that if we got it wrong it would really hurt open source
[1945.64 → 1949.32] and I suspect every good lawyer of course cares about their client
[1949.32 → 1953.50] but some clients are just represent one client
[1953.50 → 1956.34] and other clients represent these big systemic changes
[1956.34 → 1958.42] and you feel that weight as a lawyer
[1958.42 → 1961.82] I feel like there's an other side of the problem as well
[1961.82 → 1967.60] because it's like if you try and assign blame to the person who like owns the copyright of code
[1967.60 → 1970.94] there is a huge amount of code that we all depend on all the time
[1970.94 → 1973.58] that's maintained by like some random dude in Nebraska
[1973.58 → 1975.30] like individual people
[1975.30 → 1977.62] and it's like well if you can sue to get to them
[1977.62 → 1980.40] because something they wrote caused some problem somewhere down the chain
[1980.40 → 1982.70] then that's obviously a problem
[1982.70 → 1985.36] because I can kind of see the chain where it's just like well
[1985.36 → 1989.32] who actually gets the blame for the bug that was written
[1989.32 → 1990.80] or the problem that happened with the code
[1990.80 → 1993.38] because you can easily just like keep tracing that back
[1993.38 → 1995.30] further and further and further and further
[1995.30 → 1997.12] by like passing on the blanks
[1997.12 → 1998.66] it's like once again with the train it's like
[1998.66 → 2000.80] well I didn't create that wheel
[2000.80 → 2002.02] someone else created that wheel
[2002.02 → 2003.36] so that's their problem
[2003.36 → 2006.40] or like with the Spectre meltdown hardware problems
[2006.40 → 2009.40] where it's like oh well it's not my fault there was a breach
[2009.40 → 2011.92] the processor shouldn't have been speculatively executing
[2011.92 → 2014.72] like there's so many like weird arguments that you have
[2014.72 → 2017.98] because of this stuff that we don't really understand what it is right now
[2017.98 → 2023.68] yeah and I think applying the old models is probably going to get us some very bad outcomes
[2023.68 → 2028.68] and unfortunately the way the legal system learns sometimes is by having bad outcomes
[2028.68 → 2030.56] everybody stubs their toe on it
[2030.56 → 2033.80] and then you sort of fix that up as we go
[2033.80 → 2036.06] but some people end up being caught in the middle
[2036.06 → 2037.36] that guy in Nebraska
[2037.36 → 2042.88] I assume all the listeners here have seen the XKCD comic about the guy in Nebraska
[2042.88 → 2045.98] the problem is of course it's not even just one guy in Nebraska
[2045.98 → 2048.28] it is a tower of 10,000 guys in Nebraska
[2048.28 → 2052.44] and so you know I do want to talk a little bit about the day job here
[2052.44 → 2055.96] because I founded co-founded a company called Tide lift
[2055.96 → 2059.52] and Tide lift's mission as we said at the top of the show
[2059.52 → 2061.38] is to make open source better for everyone
[2061.38 → 2063.42] in part by paying the maintainers
[2063.42 → 2065.58] because what we're seeing happen all the time
[2065.58 → 2067.44] we saw it happen a couple of times this week
[2067.44 → 2068.80] just in the JavaScript community
[2068.80 → 2074.10] is the solution to this kind of problem that you've identified Chris so far
[2074.10 → 2077.64] is we'll just start applying standards
[2077.64 → 2081.96] right so like we've got the open SSF standard security scorecard
[2081.96 → 2083.82] we've got salsa.dev
[2083.82 → 2086.60] which is a different kind of security scorecard
[2086.60 → 2090.16] GitHub caused some controversy by saying
[2090.16 → 2091.98] hey we've identified the most popular
[2091.98 → 2094.62] I think only NPM for right now
[2094.62 → 2095.52] projects
[2095.52 → 2099.10] and we're sending you all a free two-factor authentication key
[2099.10 → 2101.10] and also we're like
[2101.10 → 2103.90] mandatorily turning on two-factor authentication for everybody
[2103.90 → 2106.60] and a couple maintainers for various reasons
[2106.60 → 2107.20] were just like
[2107.20 → 2108.48] that's too much work
[2108.48 → 2110.58] that's going to complicate my life
[2110.58 → 2111.94] it's going to break my build scripts
[2111.94 → 2113.04] and like
[2113.04 → 2114.88] we can go back and forth about like
[2114.88 → 2115.66] whether
[2115.66 → 2117.16] two-factor authentication
[2117.16 → 2119.30] in some of these cases is a good idea
[2119.30 → 2121.32] but I want to step out
[2121.32 → 2121.56] I mean
[2121.56 → 2124.42] I generally think two-factor authentication is a good idea
[2124.42 → 2125.08] don't get me wrong
[2125.08 → 2127.04] but like that's the easy case
[2127.04 → 2128.68] it just gets harder from there
[2128.68 → 2129.72] right like okay
[2129.72 → 2132.26] well what do we need to do to sign our binaries
[2132.26 → 2133.08] you know
[2133.08 → 2134.92] go I understand that's a mostly solved
[2134.92 → 2137.50] probably like signing modules is a mostly solved problem
[2137.50 → 2139.66] and a lot of other language ecosystems it is not
[2139.66 → 2141.36] so okay
[2141.36 → 2142.38] so there's extra work
[2142.38 → 2142.86] right
[2142.86 → 2144.40] and we've just created this extra work
[2144.40 → 2145.14] Chris as you say
[2145.14 → 2146.76] on some guy in Nebraska
[2146.76 → 2149.02] or actually a stack of 10,000 some guys
[2149.02 → 2151.10] and I apologize to listeners
[2151.10 → 2153.16] it's probably grating for me to hear
[2153.16 → 2154.76] for me to say
[2154.76 → 2155.82] 10,000 guys
[2155.82 → 2157.22] but I think it's worth
[2157.22 → 2159.56] both admitting that this is a problem
[2159.56 → 2160.66] and I think saying that this
[2160.66 → 2161.76] the part of the problem
[2161.76 → 2163.20] of the gendering of open source
[2163.20 → 2164.42] is very much
[2164.42 → 2165.96] that in a world
[2165.96 → 2167.58] where women are often called on
[2167.58 → 2170.36] to take on more than their share of household duties
[2170.36 → 2172.06] and home care
[2172.06 → 2172.68] child care
[2172.68 → 2173.34] elder care
[2173.34 → 2176.20] if we're not paying people to do open source
[2176.20 → 2176.84] well guess what
[2176.84 → 2178.66] that's part of how we get guys doing it
[2178.66 → 2180.82] because guys for various cultured reasons
[2180.82 → 2181.90] have more free time
[2181.90 → 2183.92] that's an important side note
[2183.92 → 2184.84] that I try to
[2184.84 → 2186.46] I think is important to say
[2186.46 → 2187.72] anyway
[2187.72 → 2189.62] we're putting all these new requirements
[2189.62 → 2190.36] on people Chris
[2190.36 → 2191.96] because of exactly this intuition
[2191.96 → 2192.94] you've had about like
[2192.94 → 2194.20] but we're doing nothing
[2194.20 → 2195.90] to make open source more fun
[2195.90 → 2196.68] easier
[2196.68 → 2199.26] like all we're doing is loading more work on top
[2199.26 → 2200.34] and I think at some point
[2200.34 → 2202.86] I think we're already starting to see it
[2202.86 → 2203.70] in some communities
[2203.70 → 2205.64] that people are going to snap
[2205.64 → 2206.50] people are going to walk away
[2206.50 → 2207.38] people are going to say
[2207.38 → 2208.52] so what do we do
[2208.52 → 2209.64] so what Tide lift does
[2209.64 → 2210.96] to help address this problem
[2210.96 → 2212.30] is we say
[2212.30 → 2212.62] hey
[2212.62 → 2214.26] we go to our customers
[2214.26 → 2214.74] and we say
[2214.74 → 2216.02] you're going to get more predictable
[2216.02 → 2217.52] more reliable open source
[2217.52 → 2219.42] if developers follow these standards
[2219.42 → 2221.14] they're not going to follow these standards
[2221.14 → 2221.66] on their own
[2221.66 → 2222.60] you should pay them
[2222.60 → 2223.72] so if you want
[2223.72 → 2225.20] the stuff you use
[2225.20 → 2226.80] to follow those standards
[2226.80 → 2227.78] write us a check
[2227.78 → 2228.70] we will go out
[2228.70 → 2230.32] find those developers for you
[2230.32 → 2232.12] hopefully we already have a contract with them
[2232.12 → 2232.86] from other customers
[2232.86 → 2234.06] but we'll go out
[2234.06 → 2234.80] find them
[2234.80 → 2235.82] and pay them
[2235.82 → 2238.62] and in order to get some of these
[2238.62 → 2239.72] this work done
[2239.72 → 2240.32] now
[2240.32 → 2243.26] there are a lot of challenges around this
[2243.26 → 2243.54] right
[2243.54 → 2244.00] in part
[2244.00 → 2244.78] because guess what
[2244.78 → 2246.28] nobody wants to pay for open source
[2246.28 → 2247.44] it should be free
[2247.44 → 2247.98] and like
[2247.98 → 2248.70] well guess what
[2248.70 → 2249.94] if you're liable
[2249.94 → 2250.62] all of a sudden
[2250.62 → 2251.52] maybe it's not free
[2251.52 → 2252.98] and I think one of the interesting things
[2252.98 → 2253.98] that we're going to see in discussion
[2253.98 → 2254.44] about
[2254.44 → 2256.24] these EU regulations
[2256.24 → 2256.90] for example
[2256.90 → 2259.50] they contain exceptions for open source
[2259.50 → 2261.96] their definition of open source
[2261.96 → 2263.24] sort of looks like
[2263.24 → 2265.38] it excludes commercially sponsored open source
[2265.38 → 2266.78] which as we know
[2266.78 → 2268.30] is a lot of open source these days
[2268.30 → 2268.84] right
[2268.84 → 2270.96] we don't know how that's going to play out
[2270.96 → 2272.46] we don't know what it really means
[2272.46 → 2273.94] like their definition is vague enough
[2273.94 → 2274.46] that like
[2274.46 → 2276.04] maybe it only includes
[2276.04 → 2277.14] a small slice of open source
[2277.14 → 2278.50] or maybe it includes a lot of open source
[2278.50 → 2279.54] we don't really know yet
[2279.54 → 2281.66] I'm sure that's going to be lobbied over
[2281.66 → 2283.14] and in fact
[2283.14 → 2283.96] I'm going to publish something
[2283.96 → 2284.34] hopefully
[2284.34 → 2285.86] tomorrow or Thursday
[2285.86 → 2287.14] on dev.2
[2287.14 → 2287.76] about
[2287.76 → 2288.78] what
[2288.78 → 2290.18] open source developers
[2290.18 → 2290.94] can do
[2290.94 → 2291.64] to help
[2291.64 → 2293.18] lobby the US government
[2293.18 → 2293.82] on this topic
[2293.82 → 2294.64] but a lot of the same thing
[2294.64 → 2295.08] is going to apply
[2295.08 → 2296.36] to the EU government as well
[2296.36 → 2297.66] yeah I think
[2297.66 → 2298.94] one of the thoughts I had
[2298.94 → 2300.36] during what you were saying
[2300.36 → 2300.82] is
[2300.82 → 2302.62] I've expressed this in private
[2302.62 → 2303.24] to some people
[2303.24 → 2304.54] and I always get kind of the
[2304.54 → 2304.86] like
[2304.86 → 2306.04] you've just said heresy
[2306.04 → 2306.92] look
[2306.92 → 2308.00] or comments
[2308.00 → 2309.44] but I have been wondering
[2309.44 → 2309.70] like
[2309.70 → 2311.16] is open source
[2311.16 → 2312.22] sustainable
[2312.22 → 2313.26] as the method
[2313.26 → 2314.76] of how we do things
[2314.76 → 2315.78] in this industry
[2315.78 → 2316.02] like
[2316.02 → 2316.74] is this like
[2316.74 → 2318.06] focus on sharing
[2318.06 → 2319.10] so much of code
[2319.10 → 2319.56] like
[2319.56 → 2320.88] actually going to be
[2320.88 → 2321.58] something we can continue
[2321.58 → 2322.24] doing in the future
[2322.24 → 2323.50] since there's so much
[2323.50 → 2324.90] ambiguity around all of this
[2324.90 → 2325.88] and quite frankly
[2325.88 → 2326.56] I think it also
[2326.56 → 2327.04] just like
[2327.04 → 2328.06] atrophies
[2328.06 → 2329.62] the whole industry
[2329.62 → 2330.36] because we're not
[2330.36 → 2331.04] rewriting things
[2331.04 → 2332.30] we're not reimagining things
[2332.30 → 2333.46] like I think that's one of
[2333.46 → 2334.24] the core problems
[2334.24 → 2335.12] with copyright in general
[2335.12 → 2335.34] right
[2335.34 → 2335.96] there's this whole thing
[2335.96 → 2336.68] that Disney has done
[2336.68 → 2337.36] where it's just like
[2337.36 → 2338.42] copyright used to be
[2338.42 → 2339.80] like 20 years
[2339.80 → 2340.76] now it's like
[2340.76 → 2342.20] almost forever
[2342.20 → 2343.56] or as Disney would like to have
[2343.56 → 2343.66] it
[2343.66 → 2344.92] actually forever
[2344.92 → 2346.02] so it's like
[2346.02 → 2346.96] oh well now these things
[2346.96 → 2347.68] are just kind of
[2347.68 → 2348.48] sticking around
[2348.48 → 2349.44] and it's so much harder
[2349.44 → 2350.66] to like to move things forward
[2350.66 → 2350.88] right
[2350.88 → 2351.42] it was like
[2351.42 → 2352.70] if I remember the
[2352.70 → 2354.10] kind of genesis of copyright
[2354.10 → 2355.16] or the vague genesis
[2355.16 → 2355.64] it's like
[2355.64 → 2357.08] we want to protect people
[2357.08 → 2358.70] like make it so they can profit
[2358.70 → 2359.82] off of their creative work
[2359.82 → 2360.68] for some time
[2360.68 → 2362.00] but then it goes back
[2362.00 → 2363.30] into the general pool of things
[2363.30 → 2363.96] so we can kind of
[2363.96 → 2365.46] continue making progress forward
[2365.46 → 2366.34] yeah boy
[2366.34 → 2367.44] that sustainability question
[2367.44 → 2368.20] is a big one Chris
[2368.20 → 2369.10] and I really don't know
[2369.10 → 2370.48] I'd like to say that
[2370.48 → 2372.32] we have a real clear answer to it
[2372.32 → 2372.78] I mean certainly
[2372.78 → 2373.64] I think that Tide lift
[2373.64 → 2375.42] is part of the answer to that
[2375.42 → 2377.32] but I think it's a perfect question
[2377.32 → 2377.90] to be asking
[2377.90 → 2378.28] and I
[2378.28 → 2379.76] that heresy
[2379.76 → 2382.02] it is an elephant in the room
[2382.02 → 2383.50] that a lot of people
[2383.50 → 2384.78] I have to say
[2384.78 → 2385.72] I get a little frustrated
[2385.72 → 2386.62] when an employee
[2386.62 → 2387.82] of a trillion-dollar company
[2387.82 → 2388.30] is like
[2388.30 → 2389.34] I don't know
[2389.34 → 2390.32] paying people
[2390.32 → 2392.54] open source seems to work fine for me
[2392.54 → 2392.98] I'm like
[2392.98 → 2393.88] well yeah
[2393.88 → 2395.56] because you literally work
[2395.56 → 2396.80] for a trillion-dollar company
[2396.80 → 2398.52] but a lot of the software
[2398.52 → 2399.52] you rely on
[2399.52 → 2400.50] and you're certainly
[2400.50 → 2402.04] that of your customers rely on
[2402.04 → 2403.90] they don't have that luxury
[2403.90 → 2404.44] right
[2404.44 → 2406.18] it is the kind of thing
[2406.18 → 2407.14] you know
[2407.14 → 2407.92] you got a puppy
[2407.92 → 2409.48] puppies are often more fun
[2409.48 → 2411.08] than replying to pull requests
[2411.08 → 2412.14] from automated bots
[2412.14 → 2413.26] and Chris
[2413.26 → 2414.04] I think it's
[2414.04 → 2415.36] I think one of the interesting things
[2415.36 → 2416.92] we've been a little backward focused
[2416.92 → 2418.66] but I think there's a lot of cool stuff
[2418.66 → 2419.22] you know
[2419.22 → 2421.10] I know we're flying through this time
[2421.10 → 2423.56] I think there are a lot of interesting questions
[2423.56 → 2424.08] about this
[2424.08 → 2425.20] you know future looking
[2425.20 → 2427.14] around machine learning
[2427.14 → 2427.82] co-pilot
[2427.82 → 2428.38] things like that
[2428.38 → 2429.02] and part of those
[2429.02 → 2430.26] go to what you're saying
[2430.26 → 2431.10] you know Chris
[2431.10 → 2431.48] you were saying
[2431.48 → 2432.96] well the original motivation
[2432.96 → 2434.60] for copyright was to
[2434.60 → 2436.44] well there's sort of three
[2436.44 → 2438.54] original motivations for copyright
[2438.54 → 2439.70] that vary depending on
[2439.70 → 2440.46] who you're talking to
[2440.46 → 2441.38] so in the US
[2441.38 → 2442.58] in the constitution
[2442.58 → 2444.00] it says that the
[2444.00 → 2445.20] purpose of copyright
[2445.20 → 2447.02] is to encourage authors
[2447.02 → 2447.74] right
[2447.74 → 2449.66] so it is a very utilitarian
[2449.66 → 2450.24] like
[2450.24 → 2451.74] we're going to give you this copyright
[2451.74 → 2452.58] and as a result
[2452.58 → 2453.16] you're going to like
[2453.16 → 2454.08] create more stuff
[2454.08 → 2454.52] and every
[2454.52 → 2455.28] that's a bargain
[2455.28 → 2455.96] that we're going to have
[2455.96 → 2456.16] right
[2456.16 → 2457.22] like we're going to give you
[2457.22 → 2457.82] this monopoly
[2457.82 → 2458.40] which otherwise
[2458.40 → 2458.90] the founders
[2458.90 → 2460.40] super against monopolies
[2460.40 → 2461.38] but they created
[2461.38 → 2462.76] the copyright monopoly
[2462.76 → 2463.96] specifically in order
[2463.96 → 2465.24] for the rest of us
[2465.24 → 2465.64] to benefit
[2465.64 → 2466.82] from this incentive
[2466.82 → 2467.98] of a bunch of stuff
[2467.98 → 2468.52] being created
[2468.52 → 2469.60] so that's one story
[2469.60 → 2470.90] in the EU
[2470.90 → 2472.20] really actually
[2472.20 → 2473.08] most of the rest of the world
[2473.08 → 2473.60] except the US
[2473.60 → 2475.66] it's more like
[2475.66 → 2476.76] your creativity
[2476.76 → 2478.14] is like a part of you
[2478.14 → 2479.30] like it is part of your
[2479.30 → 2480.02] like human
[2480.02 → 2482.34] your human nature
[2482.34 → 2483.68] is to create
[2483.68 → 2484.46] and so
[2484.46 → 2486.06] there's often what are called
[2486.06 → 2487.62] moral rights
[2487.62 → 2489.10] the idea that inherently
[2489.10 → 2490.30] you have some control
[2490.30 → 2491.04] over the thing
[2491.04 → 2491.92] that you've created
[2491.92 → 2493.84] even if it's not productive
[2493.84 → 2494.34] right
[2494.34 → 2495.12] even if there's no
[2495.12 → 2496.56] social value to it
[2496.56 → 2498.40] and we're going to be
[2498.40 → 2499.14] running headlong
[2499.14 → 2499.66] into that
[2499.66 → 2500.56] with all the
[2500.56 → 2501.84] foo in the style
[2501.84 → 2502.34] of bar
[2502.34 → 2504.32] bar is going to be
[2504.32 → 2505.14] really irritated
[2505.14 → 2506.08] that their moral rights
[2506.08 → 2506.76] were infringed
[2506.76 → 2507.68] and by the way
[2507.68 → 2508.68] the third
[2508.68 → 2509.40] like historic
[2509.40 → 2510.84] the original copyright
[2510.84 → 2511.84] was literally
[2511.84 → 2512.56] just basically
[2512.56 → 2513.40] a tool of censorship
[2513.40 → 2514.56] for the UK government
[2514.56 → 2515.82] in the early 1600s
[2515.82 → 2517.26] it was a way for them
[2517.26 → 2518.04] to control printers
[2518.04 → 2519.42] and
[2519.42 → 2520.30] I think Chris
[2520.30 → 2520.96] there's a really
[2520.96 → 2521.62] interesting discussion
[2521.62 → 2522.44] we're going to have
[2522.44 → 2522.90] over
[2522.90 → 2524.88] how does
[2524.88 → 2525.68] open source
[2525.68 → 2526.86] probably won't be
[2526.86 → 2527.98] mediated through copyright
[2527.98 → 2529.26] but as you were saying
[2529.26 → 2529.92] about liability
[2529.92 → 2531.20] and security
[2531.20 → 2532.98] how does government
[2532.98 → 2533.98] interact with this
[2533.98 → 2534.80] because it's one thing
[2534.80 → 2535.88] if like these big businesses
[2535.88 → 2536.70] are running around
[2536.70 → 2537.24] saying like
[2537.24 → 2538.08] hey we should make
[2538.08 → 2538.96] this stuff more secure
[2538.96 → 2540.50] it's very different
[2540.50 → 2541.14] if governments
[2541.14 → 2541.82] are running around
[2541.82 → 2542.36] saying
[2542.36 → 2543.72] the whole world
[2543.72 → 2544.38] needs you to be
[2544.38 → 2545.38] more secure
[2545.38 → 2545.80] right
[2545.80 → 2547.00] like that's
[2547.00 → 2547.38] you know
[2547.38 → 2547.80] big thing
[2547.80 → 2548.40] that we still haven't
[2548.40 → 2548.82] really wrapped
[2548.82 → 2549.34] our heads around
[2549.34 → 2549.66] yeah
[2549.66 → 2550.34] it doesn't help
[2550.34 → 2550.86] that our
[2550.86 → 2551.64] legislators
[2551.64 → 2553.10] aren't
[2553.10 → 2554.04] very tech-savvy
[2554.04 → 2554.70] and don't
[2554.70 → 2555.64] they tend to write
[2555.64 → 2556.34] a lot of laws
[2556.34 → 2557.12] that you're like
[2557.12 → 2558.60] this makes no sense
[2558.60 → 2560.06] or ask questions
[2560.06 → 2560.54] in hearings
[2560.54 → 2561.06] that are
[2561.06 → 2562.42] questionable
[2562.42 → 2563.18] at best
[2563.18 → 2563.76] yeah
[2563.76 → 2564.74] there are two parts
[2564.74 → 2565.16] of that right
[2565.16 → 2565.98] like that's the one
[2565.98 → 2566.54] and again
[2566.54 → 2567.36] I'll try to be quicker
[2567.36 → 2568.08] that's the one
[2568.08 → 2568.86] that everybody thinks about
[2568.86 → 2569.36] because we've seen
[2569.36 → 2570.40] our legislators on TV
[2570.40 → 2571.08] and it's terrifying
[2571.08 → 2572.02] but there's also
[2572.02 → 2572.70] this thing where
[2572.70 → 2573.74] so legislators
[2573.74 → 2574.66] sort of provide you
[2574.66 → 2575.56] like a rough draft
[2575.56 → 2575.96] right
[2575.96 → 2577.10] and then the courts
[2577.10 → 2578.28] are used to refine that
[2578.28 → 2579.68] but because litigation
[2579.68 → 2580.82] has gotten so expensive
[2580.82 → 2582.38] and everybody hates it
[2582.38 → 2583.84] we don't do the refining
[2583.84 → 2584.86] of the rough drafts anymore
[2584.86 → 2585.82] right
[2585.82 → 2587.02] like it sort of
[2587.02 → 2588.28] becomes industry convention
[2588.28 → 2589.90] and that sticks us
[2589.90 → 2590.70] with a lot of cruft
[2590.70 → 2592.48] that I think is a problem
[2592.48 → 2593.88] Natalie you had a question
[2593.88 → 2594.48] you wanted to
[2594.48 → 2596.44] I wanted to say that
[2596.44 → 2597.72] that's like couple
[2597.72 → 2598.84] of topics back
[2598.84 → 2599.56] but I had a
[2599.56 → 2600.44] I'm a contractor
[2600.44 → 2601.86] so I have clients
[2601.86 → 2602.40] around the world
[2602.40 → 2603.22] I see all sorts
[2603.22 → 2604.14] of different contracts
[2604.14 → 2605.62] and one time
[2605.62 → 2606.26] I had a contract
[2606.26 → 2607.04] with a California
[2607.04 → 2607.76] based company
[2607.76 → 2609.10] and there was
[2609.10 → 2610.50] a clause
[2610.50 → 2611.20] that said that
[2611.20 → 2612.08] any damage
[2612.08 → 2613.32] that I cause
[2613.32 → 2614.14] I am responsible
[2614.14 → 2614.62] of it
[2614.62 → 2616.14] so back to the
[2616.14 → 2617.06] conversation about
[2617.06 → 2617.80] that Nebraska
[2617.80 → 2618.52] person
[2618.52 → 2620.34] I mean contrast
[2620.34 → 2621.26] can say that
[2621.26 → 2622.02] the good news
[2622.02 → 2622.84] slash bad news
[2622.84 → 2623.46] is that you are
[2623.46 → 2624.98] probably what is known
[2624.98 → 2625.62] as a
[2625.62 → 2627.72] not a deep pocket
[2627.72 → 2628.66] right
[2628.66 → 2629.90] like they're unlikely
[2629.90 → 2630.74] to sue you
[2630.74 → 2631.34] because what are you
[2631.34 → 2632.02] going to give them
[2632.02 → 2632.96] your collection
[2632.96 → 2633.60] of oldies
[2633.60 → 2635.28] would not be worth
[2635.28 → 2635.88] much to them
[2635.88 → 2637.12] I was really terrified
[2637.12 → 2637.52] exactly
[2637.52 → 2638.56] you probably should have
[2638.56 → 2639.70] negotiated that out
[2639.70 → 2640.80] but that's one of these
[2640.80 → 2641.58] ways in which the legal
[2641.58 → 2642.32] system is very
[2642.32 → 2643.50] unbalanced unfortunately
[2643.50 → 2644.56] and that's a whole
[2644.56 → 2645.42] other rant for a whole
[2645.42 → 2645.94] other show
[2645.94 → 2647.08] especially the American
[2647.08 → 2648.04] one, but the thing is
[2648.04 → 2648.62] some friends
[2648.62 → 2650.14] who work in California
[2650.14 → 2650.90] said that this is
[2650.90 → 2651.66] actually a normal
[2651.66 → 2652.56] clause that they had
[2652.56 → 2653.34] this in contract
[2653.34 → 2653.94] in the past
[2653.94 → 2655.10] I think nobody
[2655.10 → 2656.72] from working in
[2656.72 → 2657.36] California is on
[2657.36 → 2658.14] this panel so
[2658.14 → 2659.10] maybe somebody
[2659.10 → 2660.16] listening can keep
[2660.16 → 2660.74] me honest here
[2660.74 → 2661.48] but I've been just
[2661.48 → 2661.96] told yeah don't
[2661.96 → 2663.04] worry it's always
[2663.04 → 2663.78] there just don't
[2663.78 → 2664.36] take it seriously
[2664.36 → 2665.60] well there's a
[2665.60 → 2666.14] whole other thing
[2666.14 → 2667.12] about cruft in
[2667.12 → 2668.84] again another rant
[2668.84 → 2669.64] for another day
[2669.64 → 2671.36] how lawyers deal
[2671.36 → 2672.86] with cruft could
[2672.86 → 2673.52] learn a lot from
[2673.52 → 2674.12] how programmers
[2674.12 → 2674.90] deal with cruft
[2674.90 → 2676.04] because a lot of
[2676.04 → 2676.92] this stuff that is
[2676.92 → 2678.24] we don't have any
[2678.24 → 2679.18] sense of dependencies
[2679.18 → 2680.74] or module reuse
[2680.74 → 2681.62] or anything like
[2681.62 → 2682.26] that in law
[2682.26 → 2683.66] and so you get
[2683.66 → 2684.80] stuff that literally
[2684.80 → 2685.50] just gets copy
[2685.50 → 2686.44] pasted like imagine
[2686.44 → 2687.62] if you copied and pasted
[2687.62 → 2688.22] all your code
[2688.22 → 2689.32] all the time
[2689.32 → 2690.42] we as programmers
[2690.42 → 2691.80] know of course
[2691.80 → 2692.76] that creates errors
[2692.76 → 2693.82] right, and we have
[2693.82 → 2695.16] linters and dependencies
[2695.16 → 2695.94] and we have all that
[2695.94 → 2696.30] kind of stuff
[2696.30 → 2697.18] lawyers have none of
[2697.18 → 2699.48] that and that is a
[2699.48 → 2700.42] problem though I'm
[2700.42 → 2701.02] curious to see if
[2701.02 → 2701.80] machine learning helps
[2701.80 → 2702.38] us with that in the
[2702.38 → 2702.66] future
[2702.66 → 2716.66] this episode is brought
[2716.66 → 2717.62] to you by honeycomb
[2717.62 → 2718.50] find your most
[2718.50 → 2719.50] perplexing application
[2719.50 → 2721.54] issues honeycomb is a
[2721.54 → 2723.52] fast analysis tool that
[2723.52 → 2724.34] reveals the truth about
[2724.34 → 2726.04] every aspect of your
[2726.04 → 2727.34] application in production
[2727.34 → 2728.42] find out how users
[2728.42 → 2729.48] experience your code in
[2729.48 → 2731.02] complex and unpredictable
[2731.02 → 2732.24] environments find
[2732.24 → 2733.82] patterns and outliers
[2733.82 → 2734.86] across billions of
[2734.86 → 2735.78] rows of data and
[2735.78 → 2736.52] definitively solve your
[2736.52 → 2737.84] problems, and we use
[2737.84 → 2738.62] honeycomb here at
[2738.62 → 2739.26] change well that's why
[2739.26 → 2739.68] we welcome the
[2739.68 → 2740.96] opportunity to add them
[2740.96 → 2741.72] as one of our
[2741.72 → 2742.76] infrastructure partners
[2742.76 → 2744.26] in particular we use
[2744.26 → 2745.20] honeycomb to track
[2745.20 → 2745.98] down CDN issues
[2745.98 → 2747.02] recently which we
[2747.02 → 2748.14] talked about at length
[2748.14 → 2749.38] on the Kaiden edition
[2749.38 → 2750.62] of the ship it podcast
[2750.62 → 2751.56] so check that out
[2751.56 → 2752.26] here's the thing
[2752.26 → 2753.32] teams who don't use
[2753.32 → 2754.46] honeycomb are forced
[2754.46 → 2755.26] to find the needle in
[2755.26 → 2756.04] the haystack they
[2756.04 → 2757.30] scroll through endless
[2757.30 → 2758.30] dashboards playing
[2758.30 → 2759.54] whack-a-mole they deal
[2759.54 → 2760.82] with alert floods trying
[2760.82 → 2761.82] to guess which one
[2761.82 → 2763.04] matters, and they go
[2763.04 → 2764.24] from tool to
[2764.24 → 2765.30] tool playing sleuth
[2765.30 → 2766.30] try to figure out how
[2766.30 → 2767.26] all the puzzle pieces
[2767.26 → 2768.64] fit together it's this
[2768.64 → 2769.78] context switching and
[2769.78 → 2770.96] tool sprawl that are
[2770.96 → 2771.82] slowly killing teams
[2771.82 → 2773.28] effectiveness and
[2773.28 → 2773.92] ultimately hindering
[2773.92 → 2775.06] their business with
[2775.06 → 2775.94] honeycomb you get a
[2775.94 → 2777.88] fast unified and
[2777.88 → 2779.74] clear understanding of
[2779.74 → 2781.00] the one thing driving
[2781.00 → 2782.42] your business production
[2782.42 → 2783.66] with honeycomb you
[2783.66 → 2784.88] guess less and you
[2784.88 → 2786.10] know more join the
[2786.10 → 2787.00] swarm and try
[2787.00 → 2788.24] honeycomb free today
[2788.24 → 2789.86] at honeycomb.io
[2789.86 → 2791.68] slash changelog again
[2791.68 → 2793.82] honeycomb.io slash
[2793.82 → 2794.64] changelog
[2794.64 → 2814.26] I was going to say that
[2814.26 → 2814.74] like when you were
[2814.74 → 2815.62] talking about how we
[2815.62 → 2816.80] have like the laws get
[2816.80 → 2817.70] written and then they
[2817.70 → 2819.52] don't get tested or
[2819.52 → 2820.44] refined I'm like that's
[2820.44 → 2821.96] going to like writing code but
[2821.96 → 2823.42] without test, and it's
[2823.42 → 2824.06] kind of like I don't
[2824.06 → 2824.80] know it's just running
[2824.80 → 2826.24] out there, and we have
[2826.24 → 2827.40] no idea if it's like
[2827.40 → 2828.50] doing the right thing or
[2828.50 → 2829.64] doing what we intended we
[2829.64 → 2830.86] just we just wrote it
[2830.86 → 2832.12] there's no test
[2832.12 → 2833.12] frameworks there's no
[2833.12 → 2835.52] linters there's no by
[2835.52 → 2836.56] the way when you compile
[2836.56 → 2838.26] it is will be there will
[2838.26 → 2839.28] be somebody else trying to
[2839.28 → 2840.40] persuade the compiler to
[2840.40 → 2841.92] do things totally
[2841.92 → 2842.78] different from what you
[2842.78 → 2844.74] intended like it's a
[2844.74 → 2846.90] very adversarial system
[2846.90 → 2848.18] that is not set up for
[2848.18 → 2850.80] robustness it don't get me
[2850.80 → 2852.04] wrong it works reasonably
[2852.04 → 2853.08] well in a lot of cases
[2853.08 → 2854.58] but it's mostly because of
[2854.58 → 2855.98] humans this was the one
[2855.98 → 2856.72] thing that drove me nuts
[2856.72 → 2857.40] about all the smart
[2857.40 → 2858.98] contract stuff like
[2858.98 → 2860.06] contracts only work
[2860.06 → 2861.14] because humans are around
[2861.14 → 2862.06] to smooth off the rough
[2862.06 → 2864.06] edges bridge the gaps
[2864.06 → 2865.44] like as soon as you start
[2865.44 → 2866.50] making contracts into
[2866.50 → 2868.34] code like you're just
[2868.34 → 2869.82] doomed to failure because
[2869.82 → 2871.16] of all the failure modes
[2871.16 → 2872.86] of code that we as
[2872.86 → 2874.72] programmers know and that
[2874.72 → 2876.12] you know don't go away
[2876.12 → 2877.00] when you have contracts
[2877.00 → 2877.98] you just have a more
[2877.98 → 2879.08] forgiving at the end of
[2879.08 → 2879.72] the day execution
[2879.72 → 2881.38] environment because at
[2881.38 → 2882.16] the end of the day humans
[2882.16 → 2883.50] are in the loop in a way
[2883.50 → 2884.22] that they aren't with
[2884.22 → 2885.30] smart contracts and the
[2885.30 → 2885.94] way they aren't with
[2885.94 → 2887.24] code I find it
[2887.24 → 2888.52] interesting how it also
[2888.52 → 2890.50] causes some like class
[2890.50 → 2892.32] problems as well like I
[2892.32 → 2893.72] have legal insurance so
[2893.72 → 2894.46] every time I get a
[2894.46 → 2895.40] contract of any sort I
[2895.40 → 2896.48] like send it to lawyers
[2896.48 → 2897.98] to review I'm like is any
[2897.98 → 2899.70] of this weird but also
[2899.70 → 2900.40] knowing that I can just
[2900.40 → 2901.52] like take a pen and just
[2901.52 → 2902.58] strike through anything I
[2902.58 → 2903.66] don't like in a contract
[2903.66 → 2904.78] but so many people think
[2904.78 → 2905.90] that's like oh no
[2905.90 → 2907.18] I've gotten this thing
[2907.18 → 2908.08] this is like set in
[2908.08 → 2909.82] stone and I can't do
[2909.82 → 2910.62] any I have to take it
[2910.62 → 2911.38] or leave it, and it's
[2911.38 → 2911.90] like that's not how
[2911.90 → 2913.52] this really works so
[2913.52 → 2914.70] like knowledge also
[2914.70 → 2915.60] makes it so the legal
[2915.60 → 2916.64] system's kind of like a
[2916.64 → 2917.60] little a little bit more
[2917.60 → 2918.50] wonky than I think it
[2918.50 → 2919.08] would be otherwise
[2919.08 → 2920.82] yeah well and on the
[2920.82 → 2921.68] flip side of course
[2921.68 → 2923.28] especially in the US
[2923.28 → 2924.04] Natalie I think you're
[2924.04 → 2924.84] correct to say that
[2924.84 → 2925.54] this is less of a
[2925.54 → 2926.54] problem in the EU
[2926.54 → 2927.92] though definitely not
[2927.92 → 2929.56] unknown as a problem
[2929.56 → 2931.08] you get lawyers who end
[2931.08 → 2931.92] up working more
[2931.92 → 2932.94] defensively than they
[2932.94 → 2933.64] might otherwise
[2933.64 → 2934.82] because they're
[2934.82 → 2935.74] thinking of the person
[2935.74 → 2936.60] like you Chris
[2936.60 → 2938.90] and so extra effort
[2938.90 → 2939.66] gets put in
[2939.66 → 2941.18] extra layers get put in
[2941.18 → 2941.88] and that's not
[2941.88 → 2942.72] necessarily a bad
[2942.72 → 2943.74] thing, but it does
[2943.74 → 2945.60] mean there were
[2945.60 → 2946.66] virtues to the days of
[2946.66 → 2947.46] the handshake deal
[2947.46 → 2949.16] right high trust
[2949.16 → 2950.50] environments versus
[2950.50 → 2951.72] low trust environments
[2951.72 → 2953.26] is a real thing in
[2953.26 → 2955.00] in law unfortunately
[2955.00 → 2955.78] for better or for
[2955.78 → 2957.12] worse, and it's
[2957.12 → 2958.72] absolutely there's all
[2958.72 → 2959.72] kinds of class and
[2959.72 → 2961.54] privilege issues around
[2961.54 → 2963.20] that again
[2963.20 → 2964.08] another rant another
[2964.08 → 2965.44] day and that seems
[2965.44 → 2966.28] to be the case with
[2966.28 → 2967.58] every episode we do
[2967.58 → 2968.20] Natalie we're gonna
[2968.20 → 2969.16] have to get you back
[2969.16 → 2970.76] for a part two
[2970.76 → 2972.20] to go deeper dive I
[2972.20 → 2973.06] have one more question
[2973.06 → 2973.80] that I want to dive
[2973.80 → 2974.82] into before we go to
[2974.82 → 2976.08] kind of the unpopular
[2976.08 → 2977.32] opinion section which
[2977.32 → 2978.20] is, and you alluded to
[2978.20 → 2979.62] this earlier are there
[2979.62 → 2980.78] specific considerations
[2980.78 → 2981.48] when we're talking
[2981.48 → 2982.70] about go I know you
[2982.70 → 2983.32] talked about kind of
[2983.32 → 2984.90] package management but
[2984.90 → 2985.82] what are the specific
[2985.82 → 2987.66] I guess legal areas
[2987.66 → 2988.50] when it comes to
[2988.50 → 2989.78] ownership of code that
[2989.78 → 2991.34] are brought in specific
[2991.34 → 2992.36] to the go software
[2992.36 → 2993.40] engineering language
[2993.40 → 2994.88] you know I think
[2994.88 → 2996.62] there's one I'm
[2996.62 → 2997.40] getting a little over
[2997.40 → 2998.42] my skis here but go
[2998.42 → 3000.58] is very much a because
[3000.58 → 3001.40] of the way that you
[3001.40 → 3001.88] all have done
[3001.88 → 3003.74] packaging it has some
[3003.74 → 3005.04] real implications I
[3005.04 → 3006.64] think for it breaks
[3006.64 → 3007.56] the brain of a lot of
[3007.56 → 3008.46] people who come out of
[3008.46 → 3009.34] like other language
[3009.34 → 3010.82] package managers right
[3010.82 → 3012.54] and it has some stuff
[3012.54 → 3013.50] that really made sense
[3013.50 → 3014.46] internally to Google
[3014.46 → 3015.72] there's this real
[3015.72 → 3017.10] question Chris you were
[3017.10 → 3017.98] alluding to it earlier
[3017.98 → 3019.58] the guy in Nebraska
[3019.58 → 3022.32] xkcd my impression of
[3022.32 → 3023.14] it from an outside
[3023.14 → 3024.56] perspective is that go
[3024.56 → 3025.34] wants to make some of
[3025.34 → 3026.86] that not a problem by
[3026.86 → 3028.78] like oh we'll just grab
[3028.78 → 3030.26] this specific revision
[3030.26 → 3033.00] from this specific repo
[3033.00 → 3035.84] and voilà like we know
[3035.84 → 3036.88] exactly what this code
[3036.88 → 3038.52] is and that guy in
[3038.52 → 3039.84] Nebraska can't hurt us
[3039.84 → 3041.16] any more right he can't
[3041.16 → 3042.02] upgrade because we know
[3042.02 → 3043.34] exactly what it is that
[3043.34 → 3044.68] we've got here but of
[3044.68 → 3046.10] course that's ends up
[3046.10 → 3046.66] being a sort of
[3046.66 → 3047.92] adversarial relationship
[3047.92 → 3049.24] with that person right
[3049.24 → 3050.42] it means that when that
[3050.42 → 3051.54] person brings knowledge
[3051.54 → 3052.78] to the table brings new
[3052.78 → 3053.86] versions to the table
[3053.86 → 3055.34] there's this sort of
[3055.34 → 3057.24] assumption we never
[3057.24 → 3058.02] really got to it here
[3058.02 → 3058.80] Natalie, but I think
[3058.80 → 3061.22] there's this penumbra of
[3061.22 → 3062.78] it's not ownership but
[3062.78 → 3063.88] it's sort of entitlement
[3063.88 → 3065.50] almost right and this is
[3065.50 → 3066.28] certainly not go
[3066.28 → 3068.40] specific but this sense
[3068.40 → 3069.38] of like well I'm using
[3069.38 → 3071.16] it, and so I'm going to
[3071.16 → 3072.10] treat it a little bit
[3072.10 → 3073.14] like I have a support
[3073.14 → 3074.26] contract like traditional
[3074.26 → 3075.44] software and in fact
[3075.44 → 3076.28] open source has sort of
[3076.28 → 3077.06] encouraged this because
[3077.06 → 3078.78] people it started from
[3078.78 → 3079.94] this very collaborative
[3079.94 → 3081.26] community-based culture
[3081.26 → 3082.44] and so the norms are
[3082.44 → 3083.34] like hey I'm going to
[3083.34 → 3084.36] help everybody who shows
[3084.36 → 3085.42] up in my issue tracker
[3085.42 → 3086.58] and of course at some
[3086.58 → 3087.42] point you get too popular
[3087.42 → 3088.96] and that breaks but we
[3088.96 → 3089.48] haven't really
[3089.48 → 3091.54] acknowledged that that's
[3091.54 → 3093.80] I mean literally the
[3093.80 → 3094.98] word entitlement comes
[3094.98 → 3095.76] out of some of the same
[3095.76 → 3096.70] roots of like the same
[3096.70 → 3098.12] Latin legal roots as
[3098.12 → 3100.16] ownership when you own a
[3100.16 → 3101.58] thing you are entitled to
[3101.58 → 3103.84] do X, and we end up with
[3103.84 → 3106.22] entitlements without the
[3106.22 → 3107.48] ownership part without the
[3107.48 → 3108.62] payments part without the
[3108.62 → 3110.36] labour part and that
[3110.36 → 3112.06] really is what sends a lot
[3112.06 → 3113.86] of things sideways I think
[3113.86 → 3114.68] in open source that's
[3114.68 → 3115.64] again that's where Tide lift
[3115.64 → 3118.58] comes in, and I think
[3118.58 → 3121.06] also Go I think has
[3121.06 → 3122.44] tried to cabin some of
[3122.44 → 3123.48] that off with its module
[3123.48 → 3124.80] ownership but sometimes
[3124.80 → 3126.32] that where that makes
[3126.32 → 3127.52] technical sense it may not
[3127.52 → 3128.78] always make social sense
[3128.78 → 3131.24] and with more time some
[3131.24 → 3132.60] other time that would be a
[3132.60 → 3133.72] fun conversation to have
[3133.72 → 3135.02] in more depth with
[3135.02 → 3135.88] some of the folks you know
[3135.88 → 3137.16] more on the packaging side
[3137.16 → 3138.26] than I do that's for sure
[3138.26 → 3140.26] so you know I guess the
[3140.26 → 3141.82] the unpopular part is not
[3141.82 → 3143.14] Go specific, but that's
[3143.14 → 3145.60] definitely the responsibility
[3145.60 → 3147.28] lies with all of us
[3147.28 → 3148.08] because we specifically
[3148.08 → 3150.10] decided in open source
[3150.10 → 3151.18] that well I'm not owning
[3151.18 → 3152.22] this thing in like some
[3152.22 → 3153.84] sense but we very much
[3153.84 → 3155.20] decided in other senses
[3155.20 → 3156.90] that like one way of
[3156.90 → 3157.86] putting it is we decided
[3157.86 → 3160.22] that use of the code
[3160.22 → 3162.86] translates into ownership
[3162.86 → 3164.04] of somebody else's time
[3164.04 → 3166.56] and like that is not
[3166.56 → 3168.16] when open source runs
[3168.16 → 3169.32] the entire world which
[3169.32 → 3170.78] it really does at this
[3170.78 → 3172.76] point that doesn't scale
[3172.76 → 3173.98] and we don't know yet
[3173.98 → 3175.14] Chris to your earlier
[3175.14 → 3177.72] point of heresy we don't
[3177.72 → 3178.48] know how that's going to
[3178.48 → 3179.88] continue scaling we don't
[3179.88 → 3181.86] know what happens when we
[3181.86 → 3183.14] ask everybody to really
[3183.14 → 3184.92] complicated multifactor
[3184.92 → 3186.88] signatures on everything
[3186.88 → 3188.60] like with very few
[3188.60 → 3189.50] exceptions people don't
[3189.50 → 3191.14] hate this stuff they're
[3191.14 → 3192.18] software developers like
[3192.18 → 3193.58] they know security matters
[3193.58 → 3195.60] they know signatures help
[3195.60 → 3196.88] but they also know they've
[3196.88 → 3197.76] only got so much time in
[3197.76 → 3198.52] the world and sometimes
[3198.52 → 3199.38] they come home from work
[3199.38 → 3200.04] and they really just want
[3200.04 → 3201.22] to pitch their laptop into
[3201.22 → 3202.94] the lake and that does
[3202.94 → 3204.66] not help you close out
[3204.66 → 3205.66] your issues if you've
[3205.66 → 3206.60] pitched your laptop in
[3206.60 → 3208.72] the lake right so we're
[3208.72 → 3209.36] going to have to figure that
[3209.36 → 3210.54] out might involve buying
[3210.54 → 3211.58] some people some laptops
[3211.58 → 3213.00] or maybe writing them a
[3213.00 → 3214.50] check, or maybe it'll
[3214.50 → 3215.34] involve helping them with
[3215.34 → 3216.44] AI which we really didn't
[3216.44 → 3217.54] get to at all but again
[3217.54 → 3219.62] maybe next time, so I
[3219.62 → 3220.36] remember a conversation
[3220.36 → 3221.84] that happened I think
[3221.84 → 3223.02] among a smaller group of
[3223.02 → 3223.54] people within the
[3223.54 → 3224.14] community but when
[3224.14 → 3225.80] modules were being
[3225.80 → 3226.64] designed and developed
[3226.64 → 3227.64] one of the comments that
[3227.64 → 3228.74] kept coming up was like
[3228.74 → 3230.48] this is biasing toward the
[3230.48 → 3232.12] consumer instead of the
[3232.12 → 3232.90] you know the provider
[3232.90 → 3234.96] their maintainer and is
[3234.96 → 3235.80] that a thing we really
[3235.80 → 3237.02] want to do in the go
[3237.02 → 3238.28] community and what effect
[3238.28 → 3239.20] is that going to have on
[3239.20 → 3240.92] people's ability to
[3240.92 → 3242.16] actually maintain and
[3242.16 → 3243.32] build open source things
[3243.32 → 3244.48] and I think we're
[3244.48 → 3245.26] really starting to see
[3245.26 → 3246.26] some of the outcomes of
[3246.26 → 3247.08] that with like what Ben
[3247.08 → 3248.00] Johnson's been doing where
[3248.00 → 3249.28] he's just like I don't
[3249.28 → 3250.30] want contributions I don't
[3250.30 → 3251.84] want like I there's just I
[3251.84 → 3252.56] don't have enough bandwidth
[3252.56 → 3253.58] to kind of deal with some
[3253.58 → 3254.74] of these things and I
[3254.74 → 3255.42] think we're going to see a lot
[3255.42 → 3256.64] more people that just are
[3256.64 → 3258.50] like well I can't like if
[3258.50 → 3259.80] there is a bug and now I
[3259.80 → 3261.12] have almost no recourse to
[3261.12 → 3262.10] fix it, or I can't get
[3262.10 → 3263.26] people off old versions of
[3263.26 → 3264.92] things, or I can't that does
[3264.92 → 3266.44] kind of erode the ability
[3266.44 → 3268.40] of people to do open source
[3268.40 → 3269.70] really which erodes our
[3269.70 → 3271.08] ability to you know maintain
[3271.08 → 3272.34] the modern world in a sense
[3272.34 → 3274.20] yeah absolutely, and you know
[3274.20 → 3275.00] that's one thing I would
[3275.00 → 3276.94] say to the go folks you're
[3276.94 → 3278.26] not alone in that every
[3278.26 → 3279.56] ecosystem is struggling with
[3279.56 → 3280.50] that there are different
[3280.50 → 3281.90] flavours caused by different
[3281.90 → 3282.90] technical choices and
[3282.90 → 3283.82] different cultural choices
[3283.82 → 3285.58] along the way but the core
[3285.58 → 3288.02] problem I can't wait we did
[3288.02 → 3289.24] a tidal conference right
[3289.24 → 3290.92] before the pandemic I can't
[3290.92 → 3291.90] wait to do our next one
[3291.90 → 3293.20] because very much a theme is
[3293.20 → 3294.58] going to be how can people
[3294.58 → 3296.16] across many languages
[3296.16 → 3299.32] ecosystems share notes you
[3299.32 → 3300.60] know figure out what this
[3300.60 → 3301.92] looks like because it's very
[3301.92 → 3304.16] much not if you feel alone
[3304.16 → 3306.00] if you're having a bad day
[3306.00 → 3307.62] and you want to chuck your
[3307.62 → 3309.20] private keys away and never
[3309.20 → 3310.58] log into GitHub again like
[3310.58 → 3311.46] you're not alone in that
[3311.46 → 3313.08] that is a that is a common
[3313.08 → 3314.94] thing right and GitHub is
[3314.94 → 3316.42] going to bust their butts I
[3316.42 → 3317.56] will give them credit they're
[3317.56 → 3319.30] trying to do a lot to make
[3319.30 → 3320.06] some of this easier for
[3320.06 → 3321.42] maintainers but ultimately
[3321.42 → 3323.40] Chris as you say big
[3323.40 → 3325.12] companies are going to buy
[3325.12 → 3326.58] us towards doing the right
[3326.58 → 3328.20] thing for the consumer right
[3328.20 → 3329.80] like Microsoft has done a
[3329.80 → 3330.76] lot of amazing things for the
[3330.76 → 3331.70] open source community which
[3331.70 → 3334.20] 1997 me is like a gassed that
[3334.20 → 3335.40] I'm saying that out loud but
[3335.40 → 3336.76] like but at the end of the
[3336.76 → 3338.40] day I mean when that comes
[3338.40 → 3340.76] down to push or shove the
[3340.76 → 3341.72] decisions are often going to
[3341.72 → 3342.56] be made in favour of the
[3342.56 → 3344.32] consumer, and we do need to
[3344.32 → 3345.50] have some of those honest
[3345.50 → 3346.70] discussions about what that
[3346.70 → 3347.82] looks like because it's not
[3347.82 → 3349.94] because Natalie that to get
[3349.94 → 3350.72] back to some of what you're
[3350.72 → 3352.24] saying and the overall theme
[3352.24 → 3354.22] of the show legal ownership
[3354.22 → 3356.72] is only part of the story here
[3356.72 → 3357.82] cultural ownership
[3357.82 → 3360.32] responsibility entitlement all
[3360.32 → 3362.40] these things are related to
[3362.40 → 3365.84] but cannot be solved just by
[3365.84 → 3367.44] our legal systems and I think
[3367.44 → 3369.24] maybe that's my one regret I
[3369.24 → 3370.76] have very, very few regrets
[3370.76 → 3371.76] about going to law school it's
[3371.76 → 3372.78] a lot of fun I met a lot of
[3372.78 → 3374.72] great people but people often
[3374.72 → 3376.70] come to me seeking legal
[3376.70 → 3377.88] solutions for what are
[3377.88 → 3380.32] ultimately cultural problems and
[3380.32 → 3383.04] I can only do the best lawyers
[3383.04 → 3384.50] know how to straddle that gap
[3384.50 → 3386.60] right, and I like to think that
[3386.60 → 3388.06] that is certainly my biggest
[3388.06 → 3389.78] strength as a lawyer especially
[3389.78 → 3392.06] in this space is how to straddle
[3392.06 → 3394.02] that gap, but it's not easy
[3394.02 → 3395.10] which actually by the way
[3395.10 → 3397.02] reminds me side project fun
[3397.02 → 3398.56] project, and then we'll, we'll
[3398.56 → 3399.42] leave it I know we're running
[3399.42 → 3401.96] out of time here I am writing a
[3401.96 → 3404.32] newsletter called open ml dot FYI
[3404.32 → 3406.98] it is new I literally sort of
[3406.98 → 3408.58] launched it to some friends a
[3408.58 → 3410.30] couple weeks ago and more
[3410.30 → 3412.10] broadly yesterday but is
[3412.10 → 3413.54] literally about these questions
[3413.54 → 3414.66] about open and machine
[3414.66 → 3416.80] learning overlap which
[3416.80 → 3418.58] includes questions like is
[3418.58 → 3419.40] this the end of no
[3419.40 → 3421.26] warranties because every
[3421.26 → 3422.58] open source license as you
[3422.58 → 3423.46] pointed out Chris has like
[3423.46 → 3425.36] big all caps text that says
[3425.36 → 3427.22] no warranties if you break
[3427.22 → 3429.94] it you buy it and what does
[3429.94 → 3431.04] that mean in light of EU
[3431.04 → 3432.60] regulation you know be
[3432.60 → 3433.46] talking about a lot of this
[3433.46 → 3434.76] stuff like copilot there as
[3434.76 → 3436.12] well so would love to have you
[3436.12 → 3437.16] all back but for those of you
[3437.16 → 3438.28] who are curious about that
[3438.28 → 3440.78] topic it's a ghost a GPL
[3440.78 → 3443.08] powered newsletter open ml dot FYI
[3443.08 → 3444.44] we'll add it in the show
[3444.44 → 3445.66] notes I want to end with
[3445.66 → 3446.62] like because I know we got to
[3446.62 → 3447.66] get to unpopular opinions but I
[3447.66 → 3448.86] just want to say like one of
[3448.86 → 3449.50] the things I always think
[3449.50 → 3450.52] about when we get into these
[3450.52 → 3451.60] conversations is like people
[3451.60 → 3453.34] tend to think like humans are
[3453.34 → 3454.88] like transactional, and they're
[3454.88 → 3455.96] like kind of mean to each
[3455.96 → 3457.22] other, and we want a war and all
[3457.22 → 3458.84] of that, and I feel like the
[3458.84 → 3460.82] existence of open source and
[3460.82 → 3462.18] the existence of our industry as
[3462.18 → 3463.80] a whole proves that people are
[3463.80 → 3465.82] a lot of times selfless and will
[3465.82 → 3468.38] sacrifice a lot just to make
[3468.38 → 3470.26] other people feel good just for
[3470.26 → 3471.62] the happiness of other people
[3471.62 → 3473.50] and I think that's like shows
[3473.50 → 3475.24] how like incredible and how
[3475.24 → 3476.92] collaborative we are as a
[3476.92 → 3478.84] species, but I think more of us
[3478.84 → 3480.66] need to remember that especially
[3480.66 → 3482.18] in the times we are now we are
[3482.18 → 3484.50] not necessarily this always angry
[3484.50 → 3485.78] at each other always warring
[3485.78 → 3487.44] always territorial species quite
[3487.44 → 3488.96] often most of us are just like
[3488.96 → 3490.60] these we just want to help our
[3490.60 → 3492.64] fellow people out it's been too
[3492.64 → 3493.52] long since I worked at
[3493.52 → 3496.04] Wikipedia, but I mean here's this
[3496.04 → 3497.26] thing this is amazing cultural
[3497.26 → 3498.94] treasure and anyone can go and
[3498.94 → 3501.16] graffiti on it at any time and
[3501.16 → 3502.30] like something like one in a
[3502.30 → 3505.02] thousand edits are spam right
[3505.02 → 3506.76] like I mean think about what
[3506.76 → 3509.16] that says as like to exactly your
[3509.16 → 3510.98] point Chris right like actually
[3510.98 → 3513.90] most of the time most people we
[3513.90 → 3515.58] all want to make this work right
[3515.58 → 3519.90] and open source open data are very
[3519.90 → 3523.90] much I think like genuinely amazing
[3523.90 → 3525.94] that's why I enjoy doing it right
[3525.94 → 3528.56] like there are a lot more lucrative
[3528.56 → 3530.34] things probably all of us could be
[3530.34 → 3532.16] doing with our lives but yeah it's
[3532.16 → 3533.60] human and humane greatly
[3533.60 → 3536.02] lovely note to end the episode we're
[3536.02 → 3537.38] going to have to get you back for a part
[3537.38 → 3540.00] two for sure, but before we let you go
[3540.00 → 3541.52] we're going to be doing a little bit of
[3541.52 → 3543.20] unpopular opinions
[3543.20 → 3565.12] so over to you Lewis what is your go
[3565.12 → 3567.94] time on popular opinion oh boy I mean
[3567.94 → 3569.18] the one I have in the show notes is
[3569.18 → 3570.48] absolutely the one I already nailed
[3570.48 → 3573.16] which is hey we should all be paying
[3573.16 → 3574.94] for this right we got it for free for
[3574.94 → 3578.32] a long time and that train is running
[3578.32 → 3580.94] out for very human decent reasons
[3580.94 → 3582.62] right like it's not like I think
[3582.62 → 3584.40] companies are bad for having used this
[3584.40 → 3587.26] stuff but as Chris was saying sometimes
[3587.26 → 3589.98] you raise that employee company I will
[3589.98 → 3591.84] never forget, so there was this project
[3591.84 → 3594.48] that I was invited to like yeah come to
[3594.48 → 3595.94] a meeting about right I won't be
[3595.94 → 3598.00] specific, but it was one of many
[3598.00 → 3599.86] many many many open source metadata
[3599.86 → 3602.64] projects and people went on for like
[3602.64 → 3605.58] about 45 50 minutes, and I was like okay
[3605.58 → 3608.10] but why are volunteers going to create all
[3608.10 → 3612.18] this metadata for you quiet silence quiet
[3612.18 → 3614.86] silence okay but why what's their
[3614.86 → 3617.22] motivation I don't know it's probably
[3617.22 → 3619.18] just going to happen needless to say that
[3619.18 → 3621.80] project is having not really gone much of
[3621.80 → 3624.50] anywhere, but I was treated as like a
[3624.50 → 3626.60] pariah and like literally not invited to
[3626.60 → 3629.02] future meetings for a while because I had
[3629.02 → 3631.30] dared to ask this like question of why
[3631.30 → 3633.50] would people do this unfortunately I
[3633.50 → 3636.26] still get that all too often I think to
[3636.26 → 3638.24] be fair lots of people are getting the
[3638.24 → 3639.90] message finally, but it's taken longer
[3639.90 → 3642.06] than I should have that's my sadly
[3642.06 → 3643.92] unpopular opinion today it's like that
[3643.92 → 3645.46] meme about that guy that's being thrown
[3645.46 → 3646.60] outside the window
[3646.60 → 3650.28] wait which thrown outside the window
[3650.28 → 3651.84] now I have to google this where it's like
[3651.84 → 3653.36] they're all in the meeting this comic
[3653.36 → 3656.12] strip that oh yeah yeah
[3656.12 → 3659.24] mm-hmm yeah yep been there go
[3659.24 → 3661.72] intrigued to see how unpopular or in fact
[3661.72 → 3665.48] popular that opinion is, and then I want to
[3665.48 → 3667.36] ask you Chris for an unpopular opinion
[3667.36 → 3669.08] given that we're just getting you back
[3669.08 → 3670.84] and I'm sure you have something on your
[3670.84 → 3673.40] mind you always do I have so many
[3673.40 → 3675.92] unpopular opinions I don't think this is
[3675.92 → 3677.96] going to be unpopular, so I think most people
[3677.96 → 3680.10] probably agree, but it's like a thing I
[3680.10 → 3681.58] want to put out into the universe more
[3681.58 → 3685.10] and that is that every tech company
[3685.10 → 3689.50] larger than probably 20 or 30 people
[3689.50 → 3693.20] should hire a librarian we create
[3693.20 → 3696.34] ridiculous amounts of information but
[3696.34 → 3697.86] then we usually just dump it into a
[3697.86 → 3699.64] wiki, and then we're like we'll be able
[3699.64 → 3700.94] to find it just use the search
[3700.94 → 3702.98] functionality, or we like to try and make a
[3702.98 → 3705.60] docs page, and we're like users will be
[3705.60 → 3707.06] able to find stuff, and it's like there's
[3707.06 → 3709.22] an actual degree program of people who
[3709.22 → 3712.04] like get doctorates and how to arrange
[3712.04 → 3714.50] information, so people can find it like
[3714.50 → 3717.98] go hire them like it's not you don't
[3717.98 → 3719.26] even have to like they're not even that
[3719.26 → 3721.24] expensive to hire like just go get a
[3721.24 → 3723.18] couple like a librarian and archivist and
[3723.18 → 3725.66] then make your data and your information
[3725.66 → 3727.50] just much more clean and much more
[3727.50 → 3729.74] organized it will probably help you make
[3729.74 → 3731.06] a lot more money in the long run and
[3731.06 → 3732.80] make your engineers less frustrated with
[3732.80 → 3734.80] the world how come not all database
[3734.80 → 3736.66] companies in Google and so on hiring
[3736.66 → 3739.00] librarians and archivists to do this
[3739.00 → 3740.48] I'm assuming people don't hire
[3740.48 → 3742.68] librarians because they just never a
[3742.68 → 3743.66] think most people don't know what
[3743.66 → 3745.60] librarians actually do I think most
[3745.60 → 3747.00] people just think librarians are the
[3747.00 → 3748.92] people that like can help you find
[3748.92 → 3751.38] books in the library, and they don't
[3751.38 → 3752.86] think much more about that they don't
[3752.86 → 3754.32] think about like that but how do they
[3754.32 → 3756.18] help you find the books they're just
[3756.18 → 3757.94] like yeah they just help me find stuff
[3757.94 → 3759.64] so I think that's part of it, and it's
[3759.64 → 3762.34] just like an unless you're unless you sit
[3762.34 → 3763.78] down and think about what the problem
[3763.78 → 3765.34] is I don't think it's like that kind of
[3765.34 → 3766.72] clear thing you're not going to look
[3766.72 → 3769.22] necessarily outside the world you
[3769.22 → 3770.46] exist in you're going to be like oh no
[3770.46 → 3772.88] this is the world like you know we can
[3772.88 → 3774.42] do this with computers we can just write
[3774.42 → 3776.40] some code that'll do some indexing and
[3776.40 → 3779.10] that'll work like I always look at books
[3779.10 → 3780.82] and I always look at like the indexes
[3780.82 → 3783.26] they have, and I'm like someone is
[3783.26 → 3785.48] trained probably has like a high-level
[3785.48 → 3788.32] degree and how to actually pick what
[3788.32 → 3791.20] words go in an index that's like a
[3791.20 → 3793.30] really challenging job because there's a
[3793.30 → 3795.78] crap load of words in a book like well
[3795.78 → 3797.38] which ones do I pick and put in that
[3797.38 → 3799.26] it's like well no that's like a hard
[3799.26 → 3802.32] job and yet books forever well maybe
[3802.32 → 3803.72] forever but for a very long
[3803.72 → 3805.26] time had indexes, and it's like well we
[3805.26 → 3807.70] should probably get those people but
[3807.70 → 3808.70] yeah I think most of the time it's like
[3808.70 → 3810.74] we as technologists are just like no, no
[3810.74 → 3812.88] our technology will just do it for
[3812.88 → 3815.26] us we'll write some stat stuff or some
[3815.26 → 3817.34] ML or AI or whatever, and it can
[3817.34 → 3819.34] obviously replace the thing that humans
[3819.34 → 3820.46] have been doing very well for a very
[3820.46 → 3821.98] long time even though we have no idea
[3821.98 → 3824.36] about that degree program or industry
[3824.36 → 3826.34] is at all typical things that we do
[3826.34 → 3828.08] the Times published a book review
[3828.08 → 3830.90] yesterday of a book on the history of
[3830.90 → 3833.04] indexes which apparently has like three
[3833.04 → 3836.12] separate indexes this book on indexes so
[3836.12 → 3838.46] it looks fascinating, and I promise
[3838.46 → 3840.92] I did not tee that up it's not over
[3840.92 → 3844.52] company yeah the New York Times actually
[3844.52 → 3845.62] does some perfect work
[3845.62 → 3851.78] I genuinely forgot that there I'll drop
[3851.78 → 3856.02] your check off later just a discount on
[3856.02 → 3857.72] my subscription that's all I ask
[3857.72 → 3861.26] watch it is has been an absolute pleasure
[3861.26 → 3862.92] having you on the show thank you so much
[3862.92 → 3865.06] for joining us it's also wonderful to
[3865.06 → 3866.90] have you back Chris and wonderful as
[3866.90 → 3869.74] always to have you like co-presenting
[3869.74 → 3873.42] with me, and regrettably we're now gonna
[3873.42 → 3876.10] have to say goodbye so thank you all I'm
[3876.10 → 3877.78] hoping to have everyone together again
[3877.78 → 3879.86] soon absolutely thank you
[3879.86 → 3888.04] if you enjoyed hearing from Lewis on
[3888.04 → 3889.84] this topic take a listen to JS Party
[3889.84 → 3893.16] episode 188 that one's called we ask a
[3893.16 → 3895.58] lawyer about GitHub copilot and that
[3895.58 → 3898.36] lawyer is you guessed it Lewis via I
[3898.36 → 3900.04] loved that episode and I learned a lot
[3900.04 → 3902.94] from it, you might too at jsparty.fm
[3902.94 → 3905.58] slash 188 and of course you have to
[3905.58 → 3907.02] subscribe to go time if you haven't
[3907.02 → 3909.52] already head to go time.fm for all the
[3909.52 → 3912.12] ways lastly let me say if you get value
[3912.12 → 3913.90] from go time and anything else that we
[3913.90 → 3915.68] produce here at changelog return some
[3915.68 → 3918.36] value at changelog.com slash plus
[3918.36 → 3920.76] directly support our work make the ads
[3920.76 → 3922.92] disappear and get in on some fun bonuses
[3922.92 → 3924.80] while you're at it thanks again to our
[3924.80 → 3927.84] partners quickly and fly.io they help us
[3927.84 → 3929.70] make go time possible and to the
[3929.70 → 3931.26] mysterious break master cylinder for
[3931.26 → 3932.94] keeping our beats banging each and
[3932.94 → 3935.64] every week next time on go time we have
[3935.64 → 3937.92] a Halloween treat for you Matt Ryder
[3937.92 → 3940.44] hosts a gathering of ghouls and ghosts
[3940.44 → 3943.02] telling spooky stories to scare devs
[3943.02 → 3945.16] stay tuned for that it's going to be a good
[3945.16 → 3946.66] one, and we'll have it ready for you
[3946.66 → 3947.36] next week
[3947.36 → 3959.24] Bruce Wayne
[3959.24 → 3961.30] you
