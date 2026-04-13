[0.00 → 17.34] welcome to go time your source for diverse discussions from all around the go community
[17.34 → 22.98] thanks to our partners for helping us bring you the best developer pods each and every week
[22.98 → 29.28] fassi.com fly to Io and typesense.org okay here we go
[29.28 → 44.82] so I know that when I said crypto you all some maybe thought oh no yet another scam
[44.82 → 51.14] not that type we're talking about the library right the standard lip what is new in the crypto
[51.14 → 56.92] library what is going on there for maybe somebody who hasn't used it we'll also cover a little bit
[56.92 → 62.66] on why was it added what are some common uses of it and obviously what is new about that
[62.66 → 70.86] and I am joined today by the security go experts Filippo and Roland who wore and are on the go team
[70.86 → 76.76] would you like to introduce yourself briefly Filippo do you want to go first or of course yes
[76.76 → 85.76] scary spooky and awkward silence so i I'm Filippo I used to be on the go team working with
[85.76 → 90.98] Roland and I'm now um independent maintainer still working on the cryptography packages
[90.98 → 98.20] of the go standard library so you know of the crypto slash and goline.org slash access slash crypto
[98.20 → 103.64] so in a sense uh what we often say in the industries uh same team different company
[103.64 → 110.10] yeah and I'm uh Roland shoemaker I'm on the go team i I've been for about three years I think I was
[110.10 → 117.38] technically recruited by Filippo um and yeah so I'm responsible for additional maintenance of the
[117.38 → 123.58] not only the crypto libraries but all the libraries that have some kind of security impact on go
[123.58 → 131.44] and then also for responding to and uh triaging security issues in the standard library not just in
[131.44 → 136.54] security specific libraries but in everything before I worked on the go team I worked at the
[136.54 → 142.88] electronic frontier foundation and the internet security research group uh for five years on the
[142.88 → 149.78] let's encourage project one of my great successes right here uh recruiting Roland to take on all of
[149.78 → 157.24] the security reports yeah and then immediately leaving its kind of how I started my way in the go meetup
[157.24 → 163.46] in Berlin I was invited to be a co-organizer and then the co-organizer moved to London great tactic
[163.46 → 168.42] yeah always works fall for that I can recommend it i just yeah I just need to find my
[168.42 → 172.48] replacement now well if anybody's listening to this episode you know where to find Roland
[172.48 → 175.50] oh so we need to make this into a pitch
[175.50 → 181.50] it's like a blockchain that you sing the next person right sorry oh no
[181.50 → 190.34] spooky jokes um so when did the crypto library joined the standard libraries of go
[190.34 → 196.16] when why was it there from the beginning yeah very beginning I think you can find it all the way back
[196.16 → 202.44] to when the tree was open sourced I think, and originally they were mostly written by Adam Langley
[202.44 → 206.32] who pretty much did with me what I did with Roland
[206.32 → 213.40] blockchain all the way so yeah he uh designed a lot of the APIs, and we're now talking about 10
[213.40 → 222.74] 11 years ago something along those lines and for the time it was amazingly modern as a set of APIs
[222.74 → 228.80] and selection of things to implement now of course 10 years is a lot of time, but it's been one of the
[228.80 → 235.20] major things we've focused on has been trying to keep things modern and a good example in terms of
[235.20 → 241.70] API design and implementation and reducing complexity because that's what we were handed
[241.70 → 247.60] down from what existed already in the project I think it was relatively revolutionary at the time
[247.60 → 253.64] to have kind of cryptography code in the standard library rather than almost every other language
[253.64 → 259.78] requires you to rely on some third-party implementation of this kind of stuff which is
[259.78 → 264.58] you know for better or worse but I think go was really one of the languages first languages that
[264.58 → 270.62] really came with this stuff is like a first class implementation that you could kind of trust and
[270.62 → 276.10] rely on and not have to go and find kind of disparate implementations of all these different things
[276.10 → 284.46] yep, and specifically they made it about I think they uh they didn't focus on making a cryptography
[284.46 → 292.40] library but on what go developers would need so TLS right http sit I think they saw correctly that
[292.40 → 298.28] would be something that you would have to link into almost every program because doing a get request
[298.28 → 305.54] to HTTPS URL that's something we do almost all the time right API calls and all that and for that you
[305.54 → 311.02] need that the whole cryptography stack, and it was important that it could cross compile and that it
[311.02 → 317.08] be native go and all that and so-and-so from the beginning the go cryptography libraries are not
[317.08 → 323.26] about competing with other cryptography toolkits so we don't compete on performance or on how many
[323.26 → 330.06] different things we implement that the others don't, but instead we focus on are we providing go developers
[330.06 → 335.82] what they need to develop go applications and I think that helped a lot with reducing complexity and
[335.82 → 341.12] keeping it focused initially informally and more recently with the go cryptography principles
[341.12 → 346.88] which were just a written down version of what I just said and generally keeping the code quite secure
[346.88 → 351.10] kind of as a default yeah but I think that's something that's saved us from a lot of security
[351.10 → 356.44] vulnerabilities is that we don't implement everything you know there are a lot of things we have explicitly
[356.44 → 361.30] kind of put said like you can go and implement this yourself, but we don't think this is
[361.30 → 365.42] necessary in the standard library and that has meant that every time there has been a huge
[365.42 → 370.88] you know security disclosure about some you know custom curve parameters or something
[370.88 → 377.22] we have not been affected because we have explicitly made those decisions to just not implement it
[377.22 → 382.18] yeah and this is the part where we take the opportunity to apologize to everybody we said
[382.18 → 388.10] no to on issue tracker because they're probably listening to be like yeah tell me what's new because my
[388.10 → 395.36] thing didn't make it I mean yeah but I will say from jumping outside the go focus
[395.36 → 400.60] for one second um I'm preaching a lot the idea that I think go is the like one of the languages
[400.60 → 405.36] that will survive this AI revolution and one of the many reasons to back that that one of them is
[405.36 → 412.78] that all the code that is out there is secure by default we try we definitely try yes I mean
[412.78 → 417.36] no more secure than others let's say right yes I mean you just need to not be the slowest person
[417.36 → 423.84] to run when a cheetah is chasing exactly Roland and I are always talking about the things that we wish
[423.84 → 431.56] were better, but it is entirely fair to say that go has much better posture than the average language
[431.56 → 439.82] for sure so what is new in the crypto library for go and when you answer that and I will say that
[439.82 → 445.04] we have a show notes and document, and we have like a very long list there so many things that are new
[445.04 → 451.04] we only have this one hour so whatever you choose to tell us about it will be interesting also if
[451.04 → 457.04] you briefly say how it was and what does the change so pick your favourite and just share away and I'll be
[457.04 → 462.48] just asking you questions oh we absolutely pre-gamed this uh, and we're talking about all right so if we
[462.48 → 469.04] don't have time what do we kill, and we're both like well those are all very good things kill your
[469.04 → 474.30] darlings that did not quite work not something we get to talk about all that often so I think
[474.30 → 478.48] there's a backlog of very interesting things that we've done that we all want to talk about but
[478.48 → 483.82] may not have time to get to everything we can always have an episode number two on the topic
[483.82 → 490.66] and you know we have 17 things here so lets uh let's cover like eight well I think probably one
[490.66 → 495.68] of the biggest things that we've done recently and this is something that you worked on was the
[495.68 → 502.76] RSA backend change right we have this we've had for a very long time a RSA implementation that
[502.76 → 509.92] was based on a big integer library that we have in the standard library called math big it is because
[509.92 → 517.56] it is a generic big integer library is very hard to use and dangerous and not explicitly designed for
[517.56 → 525.00] cryptography yep if you have the spooky music this is where you put it yeah so we and that that was the
[525.00 → 532.02] basis of our RSA implementation since I think since the beginning which caused a lot of problems and the
[532.02 → 538.00] same was used in the ECDSA implementation it was a little bit all over the standard library because
[538.00 → 544.78] in cryptography you often need to do things with big numbers, and you know it's tempting to say oh great
[544.78 → 553.70] i will use this library that's called big numbers, and then you regret it because libraries that are not
[553.70 → 559.64] designed to be secure will optimize for things like feature completeness or performance and will end up
[559.64 → 564.92] you know having 2 000 lines of code that have code paths that might be reachable by attackers but not
[564.92 → 572.58] really looked at because they are only used if the number is a specific modulo value module something else
[572.58 → 578.66] some very edge case or something like that, so the result is that math big was really not a robust
[578.66 → 587.08] basis for cryptography so i set out to move math big out of the security perimeter the goal was even if
[587.08 → 593.46] there's a bug in math big okay it's a bug it's not immediately a vulnerability so that meant producing
[593.46 → 599.86] a new beginning to implementation that was specifically about cryptography which we call big mod and that
[599.86 → 606.14] started as an external contribution and was rewritten almost entirely over to make it even smaller and i think
[606.14 → 612.44] it worked out to 400 lines of code something like that down from the thousands of lines of math big
[612.44 → 619.26] and we used that to replace the back end of RSA half the back end of the leap tic curve implementations
[619.26 → 628.66] and so far so good you know last famous words uh Roland maybe even has i started to find any
[628.66 → 635.38] spooky tunes that are transition prides it'd be very funny if you know in a week of a security
[635.38 → 642.52] release comes out, and it has a vulnerability in it but of course Roland cannot tell us so
[642.52 → 647.22] I'll just I'll I'll you know I'll give you a wink if there's anything
[647.22 → 652.48] oh we're we're live on video two okay no
[652.48 → 661.68] can be one of the snippets oh okay so and this is uh from what like if you want to use that but what
[661.68 → 670.00] is it already available yeah so if you noticed RSA getting slower in go 120 that was that that was me I'm
[670.00 → 676.64] sorry and then i went and made it faster in go 121 so RSA decryptions and signatures are now faster
[676.64 → 681.90] than we started at, but that's because they just used the new thing but from the user point of view
[681.90 → 687.52] nothing changed it should still work exactly the same it's just much more secure maintainable constant
[687.52 → 695.20] time and so on so all the other hood yes it also helped us build a very visible change which is the
[695.20 → 703.82] new package crypto ECD and that one is a whole new package to do the elliptic curved fie Hellman which
[703.82 → 710.88] is a key exchange uh and before that package you had to use something even lower level which you'll
[710.88 → 717.14] be like ECD already sounds like something extremely specific and low level no, no you had to just throw
[717.14 → 721.46] around what does it stand for where when would you use it Ron do you want to I've been talking a bunch
[721.46 → 729.34] we use it in crypto TLS it's its the basis for a number of key exchanges that we have to do
[729.34 → 734.60] for intercompatibility and before yeah right before we just reached deep into parts of the standard
[734.60 → 741.56] library that nobody should ever see or touch uh that were in hindsight probably a big mistake to add
[741.56 → 748.50] but we have to live with our mistakes yeah and this new library is you know replaces tens of lines of
[748.50 → 755.24] very scary looking code with a single call to an API that is incredibly well-designed thanks to
[755.24 → 761.00] Filippo that as you know i think there's a part of what we've been trying to do over time is taking
[761.00 → 768.60] away the rough edges of the crypto libraries that we have accumulated over almost 15 years at this
[768.60 → 775.24] point of you know design and an experience with getting things wrong yeah exactly for example here
[775.24 → 782.20] the lesson is to not expose low level concepts in the API because before um so an elliptic curve
[782.20 → 789.16] point is a coordinate you know x and y it's a point to make it simple and the current API just takes
[789.16 → 794.94] some bytes that are decoding and if the bytes are wrong we can check and tell you the old API actually
[794.94 → 802.48] took numbers for x and y so what happens if the x is too big what happens if x is negative it's not
[802.48 → 807.06] supposed to go negative what happens if you pass in a negative number the answers were not pretty
[807.06 → 810.98] the answers are actually in the CV database in the list of vulnerabilities
[810.98 → 818.10] so the new API you just can't pass in a negative number because you can only pass in a bunch of bytes
[818.10 → 823.28] and we decide what they are and if they're valid or not and there's no way for you to forget to
[823.28 → 828.68] validate something because when you pass in the bytes we validate them because almost surely you didn't
[828.68 → 836.48] mean for us to skip the validation that the old API would don't let us do it in line so yeah a lot of
[836.48 → 843.00] this rewriting was deprecating the old elliptic curve API and designing the new one writing new backends
[843.00 → 850.04] just like with RSA one, so everything is constant time it uses better formulas it uses generics
[850.04 → 857.78] uh, and it uses some formally verified code generator for the hardest parts where there's a computer that
[857.78 → 865.28] actually knows how to count unlike most cryptographers and produces the code to do the arithmetic correctly
[865.28 → 872.30] automatically and that's machine checked and that's great because every library introduces bugs in the
[872.30 → 881.14] fiddly carries the one situations of arithmetic so yeah that's that's an exciting new thing that we're adding
[881.14 → 888.74] but Roland said something about the fact that we can never change things and i feel like that brings us to the next thing
[888.74 → 895.80] before we go to the next thing i want to say that i googled what ECD stands for and same as a many things in security
[895.80 → 902.32] it's just naming of people so it's elliptic curve Diffie-Hellman differ i know it's Whitfield differ but
[902.32 → 908.88] Hellman i don't know that person the first name i do not know the first name of Hellman although differ
[908.88 → 913.86] differ still comes to the conferences sometimes you're like just sitting there and sipping coffee and you
[913.86 → 920.22] think like yeah that's that's that's differ i share this excitement with you and when i saw him once
[920.22 → 924.24] in a conference i asked to take a selfie I'm very happy you said that i was like debating whether i should say
[924.24 → 931.96] it or not yes no i you know kind of started the entire field of uh public key cryptography i mean
[931.96 → 940.52] different people can claim that, but he definitely has a claim to it and yeah i once sat in the room
[940.52 → 947.88] in a lecture room with a professor Samir from RSA yes that who um i have a very brief story about
[947.88 → 955.00] this i love this uh fandomism that's going on well George tankers ley and i presented a thing
[955.00 → 962.90] it's now called privacy pass at a real world crypto one year and then in it was using RSA and George
[962.90 → 969.28] said in the presentation that we would like to replace RSA because you know RSA for the obvious
[969.28 → 974.28] reasons you don't want to use RSA and then somebody in the q a have to say what are those obvious
[974.28 → 979.12] reasons and not everybody goes to crypto well no, no that's the thing he didn't uh-huh he didn't he
[979.12 → 985.36] just said that and everybody in the room kind of nodded along because you know it's a little slower
[985.36 → 991.78] and it's some implementation some schemes built on RSA are not as secure RSA is fine it's just
[991.78 → 997.86] kind of building with legacy tools it's hard to get RSA right sometimes yeah, and you can build much
[997.86 → 1002.64] more fancier things on top of elliptic curves and in a room full of cryptographers everybody wants to be
[1002.64 → 1008.24] using elliptic curves and not and not RSA it's it's the new framework you know the new JavaScript
[1008.24 → 1014.76] framework uh that that's i think the parallel anyway in the q a somebody comes up and asks so
[1014.76 → 1020.62] just uh what is the problem with RSA just if you could elaborate, and they were super polite and
[1020.62 → 1025.90] and George goes like well you know it's its old, and it's slow and uh would like to use something
[1025.90 → 1031.12] better and modern and the person goes like yeah that makes sense thank you and then walks away
[1031.12 → 1035.68] and somebody taps on my shoulder because George was on the podium, and it was in the back backstage
[1035.68 → 1043.22] and goes like yeah so that's from divest so yeah that was great
[1043.22 → 1049.52] yeah but at least they know the limitations of their own invention
[1049.52 → 1056.04] yeah exactly um of course I'm not going to shout at you about it Ron divest being the r in RSA
[1056.04 → 1063.04] yeah yeah no he was very okay with it anyway you have to be a big person to take
[1063.04 → 1069.02] publicly criticism and that's that's good to know okay so we're covering the three things
[1069.02 → 1074.58] that you wanted to pick Roland tell us how we make changes without breaking the world
[1074.58 → 1082.52] so i go has this right probably one of the greatest things about go is the compatibility guarantee
[1082.52 → 1088.46] which is that every you know you will be able to take code that you wrote 10 years ago and compile
[1088.46 → 1093.72] it today and in theory it should basically do the same thing another reason for go surviving the
[1093.72 → 1099.14] i revolution yeah i you know I think it's one of the one of the greatest uh properties of the language
[1099.14 → 1105.94] the problem is sometimes you make the wrong decision, and you end up with an API that is
[1105.94 → 1111.56] unfortunately bad in some way the double-edged sword of the compatibility guarantee is that we cannot
[1111.56 → 1118.90] fix a lot of these problems we need to the security team technically is the only part of the go team
[1118.90 → 1127.38] that has the right to break things we know we have the uh the escape sometimes valves, but we try
[1127.38 → 1132.98] and use that as sparingly as possible but for you know for the things like the elliptic curve API
[1132.98 → 1137.46] you know that we in theory we could have designed a better elliptic curve API
[1137.46 → 1143.88] but there are too many things that rely on the old implementation and the ability to basically do
[1143.88 → 1150.76] whatever you want for better or worse so a lot of the time we kind of have to see what we can do
[1150.76 → 1157.22] behind the scenes to try and fix things as much as we can while leaving the old implementation
[1157.22 → 1163.62] basically is as make the change as invisible to the user as possible which I think is harder for us
[1163.62 → 1169.10] but makes the lives of users significantly better you know that the RSA backend change is a great
[1169.10 → 1174.30] example of this right there should be zero the user should see nothing change at all except for maybe
[1174.30 → 1180.16] performance yeah I think that it's one of the things that are most easily overlooked is how much time
[1180.16 → 1188.78] the go team spends discussing how to uphold the compatibility promise it's really a major part
[1188.78 → 1195.94] of the job is figuring out what can we do that maintains backwards compatibility which can be you
[1195.94 → 1201.28] know a whole new package and just deprecating the old one but again deprecating does not mean removing
[1201.28 → 1207.14] and people always show up and like you can't deprecate that I'm using it, and we're like that just means
[1207.14 → 1213.58] it says deprecated on it now that also means there's no more support well on you to maintain that
[1213.58 → 1218.60] like on the user who wants to keep using it right we will not add new features to it yes
[1218.60 → 1228.20] if is you want a new will you patch things to deprecate it so technically I promised hard questions
[1228.20 → 1235.56] we have a have an out to not consider vulnerabilities in deprecated packages as
[1235.56 → 1240.66] vulnerabilities but I don't think we ever exercised that right we will raise the bar slightly higher
[1240.66 → 1247.66] if there's a vulnerability that doesn't necessarily you know isn't really bad is something that like
[1247.66 → 1254.72] you know could cause a program to panic, or you know something with a slightly lower impact we may
[1254.72 → 1260.96] choose not to patch it or just make it a publicly known bug and say we're not going to patch this
[1260.96 → 1266.84] using the security patching process but if somebody wants to fix it we may accept a patch, but we still
[1266.84 → 1272.42] technically you know if something is a security a big enough security issue in a deprecated package
[1272.42 → 1278.98] it's still a package in the standard library people can still rely on it so I think we feel like we
[1278.98 → 1284.52] should still be fixing those issues I don't think we ever faced it and I can't quite speak for the policy
[1284.52 → 1290.12] of the security team anymore but I think it would also depend on how long something has been deprecated
[1290.12 → 1297.08] things that we deprecated six years ago I mean maybe things that we deprecated this year
[1297.08 → 1304.36] still fresh an example of this would be the open PGP package right there are known issues in the open
[1304.36 → 1311.08] PGP package, and you know minor security issues, but they're the kind of things that cannot really be
[1311.08 → 1316.66] fixed without breaking the API it is like an inherent problem with either the design of the open PGP package
[1316.66 → 1323.88] or the design of open PGP in general, so there's not much we can do there and in those cases we've
[1323.88 → 1329.70] you know we've taken our hands off that package and there is a open source maintained alternative
[1329.70 → 1335.76] which is another reason you know when there are work publicly known workarounds that a user can
[1335.76 → 1341.16] apply themselves such as using a different package or using an ap holding an API in a slightly different
[1341.16 → 1347.58] way it does mean that it lets us reconsider whether we need to be the people fixing the problem
[1347.58 → 1354.88] however there are times when we just can't do without visible changes and those are for example the
[1354.88 → 1364.92] the default changes of as time goes on and protocols advance and hashes get broken which is less of a thing
[1364.92 → 1370.92] now you know it's been what 15 years since a hash has been weakened uh significantly crossed yeah
[1370.92 → 1377.66] I wonder how many things will listen uh this podcast for and be like Filippo couldn't shut up could he
[1377.66 → 1381.54] oh the internet the connection's breaking
[1381.54 → 1391.46] but for example uh there are things like supporting md5 and sha1 in crypto x509 for those certificates uh or
[1391.46 → 1401.98] tls1.0 and tls1.1 that we have to at some point change, and we try to do that as this low uh staged
[1401.98 → 1409.86] rollout as possible for example sslv3 which was the very very very broken version which sslv3 is the
[1409.86 → 1416.44] one before tls1.0 because cryptographers can't do marketing for the life of them blame Netscape for
[1416.44 → 1425.04] that yeah that that was a fun time in cryptography that I wasn't around uh it was just anyway that one
[1425.04 → 1431.12] we first disabled by default uh and then removed the code years later, and now we're doing the same
[1431.12 → 1438.82] with tls1.0 and 1.1 we go look at how many clients will need that how many would break, and we are
[1438.82 → 1444.28] inching towards disabling it by default I think it's already disabled by default in clients
[1444.28 → 1451.64] and that's the thing I had the courage to do and now uh Roland is having the courage to push uh the
[1451.64 → 1459.18] disabling by default on the server side which I chickened out of the last time and applications
[1459.18 → 1465.88] can still turn it back on by setting min version, so this is just about the default and that's such a
[1465.88 → 1471.74] constant tension because we both want defaults to be secure right you should be able to just say hey
[1471.74 → 1478.54] make a TLS connection and not know anything about what I just said what the hell is the tls1.0 and
[1478.54 → 1484.50] surely not have an opinion on tls1.0 versus tls1.2 that's our job not the application developer
[1484.50 → 1491.46] but at the same time if we change defaults we changed behaviour and if we change behaviour we break
[1491.46 → 1496.74] applications that used to work and that's not great because then people don't upgrade and then they
[1496.74 → 1502.66] find us at gofer con, and they are lovely people, and we absolutely love them and I'm not kidding
[1502.66 → 1512.10] uh but still then the conversation becomes hey so that's sha1 deprecation thing
[1512.10 → 1519.82] so yeah, so there's a new mechanism uh Ron want to talk about go the bugs that that is the thing we
[1519.82 → 1526.08] talk about every time we are together so yeah I think sha1 was the first thing we tried to deprecate
[1526.08 → 1533.80] that ended up being a real painful experience but go debugs kind of did save us there and go debug
[1533.80 → 1539.88] is this idea that you can, it's a way of a kind of out-of-band way of enabling behaviour in the go
[1539.88 → 1546.02] runtime or the standard library via environment variables so you can, we can add a new behaviour
[1546.02 → 1553.10] and then gate it on the presence of a go a special go debug flag yeah which by the way is a terrible name
[1553.10 → 1559.08] for this mechanism but is a historical artifact there was already a go debug environment variable
[1559.08 → 1564.44] it's the one you used to say hey I want to know about the garbage collector poses or
[1564.44 → 1572.32] things like that and so we just kind of piggybacked on that um to be like oh you know if you want to
[1572.32 → 1579.18] turn sha1 back on uh you can do if it was already there yeah we probably shouldn't have but now
[1579.18 → 1584.66] everybody uses it yeah and so now it's called go debug, and it's a much wider yeah mechanism sorry i
[1584.66 → 1588.72] interrupted you yeah, and it's used all over the standard library now and there has been a lot of
[1588.72 → 1594.70] work to make this a kind of the way I mean really about we also have the go experiments flag
[1594.70 → 1600.24] really it would be probably well maybe there's a third name that we could have come up with but
[1600.24 → 1605.66] it's you know it's a really useful way for us to be able to preserve behaviour because there is often
[1605.66 → 1611.90] things that we want to change the default for or change the behaviour for in general because it
[1611.90 → 1617.30] provides a better experience for the user and there is no you often know with these things there's no
[1617.30 → 1623.50] elegant way to make it configurable through an API maybe that's because the API is designed in such a way
[1623.50 → 1629.48] that we cannot pass additional information or for a number of reasons, but we know that making the
[1629.48 → 1634.52] default change will break somebody and often there are you know there are valid use cases for things
[1634.52 → 1641.36] that we think aren't the thing that everyone should be doing you know for tls1 and tls1.1 there are
[1641.36 → 1648.56] servers out there and clients out there that do not support higher versions of TLS and users you know we
[1648.56 → 1655.34] should provide a way for users to support those use cases we just don't think it's safe for everyone
[1655.34 → 1661.04] to do that also because sometimes leaving something enabled is dangerous even if it's not used
[1661.04 → 1668.24] this is a thing with TLS cipher suites on the one hand we recently took away a little bit of
[1668.24 → 1674.42] configurability with the automatic cipher suite ordering which I'm so proud of by the way basically
[1674.42 → 1680.30] you can still turn on and off cipher suites which are the different primitives the different encryption
[1680.30 → 1688.78] methods used by TLS with the TLS.config.cipher suites so you can still use that to say I want to enable
[1688.78 → 1694.64] that one I want to disable that one, but it used to be that the order you put them in was important
[1694.64 → 1704.46] you are supposed to express an opinion about whether you liked TLS edge RSA cha-cha 20 poly 305
[1704.46 → 1717.00] better or SHA 256 better or worse than TLS RSA IAS 256 SHA 1 you know if you have picked a favourite
[1717.00 → 1724.42] which one do you like better, and it can be another unpopular opinion vote the answer to this
[1724.42 → 1731.44] and the thing is no application developer cares about this and that's not strictly true because
[1731.44 → 1737.94] people obviously yelled at me for taking away that uh configurability but most application developers
[1737.94 → 1743.42] don't care so now we'll take the hint on whether you turn something on or off, but then we will decide
[1743.42 → 1748.42] which ones are the better ones and which ones are the worst ones, and so we'll pick the priority order
[1748.42 → 1755.42] ourselves and that helps us because it lets us keep enabled things that are not as secure because we
[1755.42 → 1761.38] know we'll only pick them as the very last resort and that helps us keep things enabled but on the
[1761.38 → 1768.44] other hand there are things that just by being enabled expose you to security risks even if
[1768.44 → 1775.20] nobody uses them and these are the RSA cybersuites those give an attacker the opportunity to try to
[1775.20 → 1781.50] mount a specific attack the blickenbacker attack is the coppersmith or the blickenbacker
[1781.50 → 1787.34] blickenbacker yeah the 98 one right because blickenbacker has so many attacks that we have to use
[1787.34 → 1794.32] yeah which yeah it is resurfaced a number of times oh yes can you just elaborate about the two that is
[1794.32 → 1801.56] such an I was like are they saying things to see if I'm following um, so there are two very
[1801.56 → 1807.50] different attacks um the blickenbacker um 98 attack which is blickenbacker is just the name of a
[1807.50 → 1814.48] cryptographer as it is common in the field yep uh found a way to attack RSA in such a way that
[1814.48 → 1821.70] if you don't do everything in perfectly constant time so it needs to be impossible to tell apart
[1821.70 → 1827.22] whether a decryption succeeded or failed which you're saying wait but if a decryption fails
[1827.22 → 1833.70] you return an error right well no, no no that would be very bad because if the attacker can see the
[1833.70 → 1840.40] errors or even just time the operation and be like aha I saw you exited earlier because there was an error
[1840.40 → 1845.94] so now I know that this was not valid it can keep sending invalid things until it hits a valid one
[1845.94 → 1850.96] and then move to the next one you know how in uh Hollywood sometimes they figure out the combination
[1850.96 → 1856.30] of a safe one thing at a time and just goes like very fast one two three four five seven and then oh
[1856.30 → 1861.68] it hits the right one locks that one and moves to the next one clicks yeah exactly so that's actually a
[1861.68 → 1869.54] thing in cryptography a bunch of attacks work like that and the blickenbacker 98 one works like that so it
[1869.54 → 1875.26] searches when is it not the same time basically then it knows that that's an error exactly yeah and
[1875.26 → 1883.42] instead the blickenbacker 06 is an attack against signatures in that attack basically you can make a
[1883.42 → 1890.62] approximate value that looks like a signature but has some garbage in it and if the implementation
[1890.62 → 1896.40] ignores the garbage then you just made a fake signature, and it's another very fun one that keeps
[1896.40 → 1902.30] resurfacing from time to time wait it will it accept it or will it not accept it is will so if
[1902.30 → 1907.82] it's if it's a correct one with garbage is it considered fake well no that's the thing anybody
[1907.82 → 1913.36] with only the public key without the private key should not be allowed to make a signature right
[1913.36 → 1919.32] because only the person with the private key should be able to make a valid signature, but anybody can
[1919.32 → 1925.34] make something that's close to a valid signature but has a bunch of garbage in one of the fields
[1925.34 → 1932.72] imagine a Jason struct that has an additional entry with some garbage in it that one anybody can make
[1932.72 → 1941.24] so if you don't check in the verification code that there isn't extra garbage anywhere then you will
[1941.24 → 1946.30] end up accepting fake signatures that were generated by people without if you generate enough fields you
[1946.30 → 1952.88] get all the right ones and lots of trash yeah it's basically so the math behind it is that signatures
[1952.88 → 1961.04] are a cube root of a number, and you can approximate one by just doing the cube root like you do it on
[1961.04 → 1966.48] you know pen and paper cube roots which is not something I actually know how to do, but you can google it and
[1966.48 → 1972.16] find out how which is what I do when I have to implement this stuff and that one will come close
[1972.16 → 1978.76] but close is indistinguishable from right which some garbage at the end and so that's the blickenbacker
[1978.76 → 1988.66] i myself made a vulnerable implementation for the YouTube DL self-update um code and was saved by the
[1988.66 → 1997.18] fact that I had added some extra safeties that that that saved YouTube DL but yeah uh turns out you
[1997.18 → 2006.12] hardcoded the exponent yes i hardcoded the exponent to the 65k one so I remember the panic when years later
[2006.12 → 2013.62] I realized wait I remember years ago writing a from scratch implementation of RSA for YouTube DL because
[2013.62 → 2019.50] we couldn't use any dependencies, and it was just this self-contained python script and I was like oh i
[2019.50 → 2028.66] must have gotten that wrong I was like 17, and so I went back and yes I had gotten wrong but I had saved
[2028.66 → 2036.96] myself by uh anyway making better decisions than professional cryptographers at the time so
[2036.96 → 2042.14] I've got nothing nice to say
[2042.14 → 2050.58] so yeah go to bugs go to bugs allow us uh to make changes like turning off these RSA ciphers that
[2050.58 → 2058.08] allow the attacker to mount the blickenbacker 98 attacks and turning off TLS 1.0 and 1.0 and so on
[2058.08 → 2063.10] while giving people a way to escape also I don't know Ron if you want to explain how they relate
[2063.10 → 2070.04] to go versions and the new uh backwards compatibility policy you were explaining it to me earlier yeah
[2070.04 → 2077.28] there's this very nice new behaviour where we when you introduce a new go debug flag it, it enables
[2077.28 → 2083.70] some behaviour by default for everyone uh and there is you know if you look in your go module file there
[2083.70 → 2089.60] is this line that specifies what version of go this module is supposed to be used with and there are
[2089.60 → 2096.20] the new policy for go debugs is that you know we record which major version a go debug flag was introduced
[2096.20 → 2103.98] in and then the tool chain can kind of emulate older versions of the tool chain by saying you know if
[2103.98 → 2110.96] this go debugs flag was added in a version later than the go version recorded in your module file
[2110.96 → 2117.08] the tool chain will act as if you know that go debugs flag is enabled by default so you get the old
[2117.08 → 2122.74] behaviour, so your tool chain acts as if it is you know you're using go 120, but it's acting as if it's
[2122.74 → 2129.38] go 119 which allows us you know preserves the backward backwards compatibility degree because it allows
[2129.38 → 2134.82] you to kind of get the old behaviour that you were expecting um for some things that's you know that's
[2134.82 → 2139.88] good but some things you know we need to try and figure out a better way to handle security issues
[2139.88 → 2145.72] but that's on the roadmap to figure out yeah I'm very excited about it because it allows us to make
[2145.72 → 2150.94] this sort of changes with much more confidence that we're not just springing it on everybody and
[2150.94 → 2157.24] people can upgrade and notice when something is not working there's metrics connected to it so you can
[2157.24 → 2162.30] get a metric that warns you hey you're doing the non-default thing here so you're probably going
[2162.30 → 2167.92] to break uh and if you revert it then you have a metric that when it goes to zero then you can say
[2167.92 → 2173.56] oh great we don't have a need for that legacy behaviour anymore and that will eventually allow us you know
[2173.56 → 2178.52] with the telemetry proposal kind of covers some of this, but this will eventually also allow us to decide
[2178.52 → 2183.96] you know currently go debug flags are kind of there forever there are some you know sometimes we say oh
[2183.96 → 2188.52] we'll, we've added this go debug flag, and then we'll remove it in you know x number of major
[2188.52 → 2194.06] versions, but often that doesn't happen because it turns out that it's really hard to figure out who
[2194.06 → 2200.38] is using go debug flags whether they're actually still necessary um so these metrics you know the idea
[2200.38 → 2206.24] is that eventually these will be collected somewhere and exposed uh for analysis so that we can figure out
[2206.24 → 2214.12] you know maybe we don't need the sha1 re-enable flag anymore and we can actually we can finally remove
[2214.12 → 2219.74] it I don't expect that will happen for a couple of years but I've got a model for that day
[2219.74 → 2227.02] yeah exactly we'll have a party it will, I think it will happen about 10 years after we thought it would
[2227.02 → 2233.34] happen unfortunately all right so talking about certificates there is one thing that
[2233.34 → 2241.38] we added that uh I'm always excited to lead uh tell people about and by we I mean you the fallback
[2241.38 → 2249.30] roots yes this is a long time coming go is kind of unique the languages that provide a TLS stack
[2249.30 → 2255.76] go is slightly unique in that it doesn't or well it still technically doesn't provide a bundle of
[2255.76 → 2261.74] root certificates that it trusts most languages that have a TLS stack will come bundled with you know
[2261.74 → 2266.82] the set of root certificates that your computer should trust when making a TLS connection to a
[2266.82 → 2273.32] website and that's been a, and we use the system roots when we do that so on Windows that windows
[2273.32 → 2278.64] has its own root store apple has its own root store and Linux is very complicated in that it has 18
[2278.64 → 2284.60] different root stores depending on what distribution you're using and none of them are good no they're all
[2284.60 → 2291.20] bad well some of them are better than others fair, but this has been a problem for a long time because
[2291.20 → 2298.48] especially for people who use docker because if you build a very lightweight docker image often you
[2298.48 → 2304.10] will not end up with a root store and when you try and you know write a go program and you
[2304.10 → 2308.10] drop it into your docker image your lightweight docker image, and then you try and connect to a
[2308.10 → 2313.24] TLS you know a web server that uses TLS all of a sudden you're getting all these failures, and it's kind
[2313.24 → 2323.70] confusing why so we have in 121 I think we added a new API that allowed you to register a default set of
[2323.70 → 2329.12] root certificates to trust so if you don't get anything from the system you will get this special
[2329.12 → 2334.48] extra bundle of certificates that you will fall back on and this is I think solved a problem for a lot of
[2334.48 → 2342.66] people but maybe introduced new problems for us in that we now have to also provide a bundle of
[2342.66 → 2350.60] certificates which we have done as a separate module in the golang.org x crypto module as it's a
[2350.60 → 2357.64] special submodule which provides the Mozilla bundle of certificates yeah the trick is that we
[2357.64 → 2363.96] actually want nobody to use the new API except that one package that you can import if you import it is
[2363.96 → 2369.54] automatically registers the bundle, and it's a separate module because that way it can be updated
[2369.54 → 2376.88] separately and that way it can be flagged in given check the vulnerability database so that we can tell
[2376.88 → 2382.66] users when they really need to update it because the roots have changed and then Ron wrote a whole bot that
[2382.66 → 2389.06] sends yells automatically to update the list and I get these emails being like no changes abandoned or oh
[2389.06 → 2393.22] yeah a bunch of roots changed or yeah actually I've gone and deleted all the roots
[2393.22 → 2401.08] yeah it turned out that I had forgotten to check the http status code on the response that I got from
[2401.08 → 2406.68] the server that serves the text file that contains all the certificates so it was you know 404ing or
[2406.68 → 2410.72] 500ing or something and I was just like oh okay that just means there are no certificates
[2410.72 → 2418.06] but we fixed that yes and to be clear that just sends a PR an automated PR, so no harm was done
[2418.06 → 2424.88] yeah there still needs to be two humans who look at this before we actually make any change
[2424.88 → 2425.80] two googles
[2425.80 → 2427.72] anyway moving on
[2427.72 → 2430.66] moving on
[2430.66 → 2432.14] are they already AI people
[2432.14 → 2434.10] google AI books
[2434.10 → 2435.04] two barns
[2435.04 → 2436.58] oh that would make my life so much easier
[2436.58 → 2440.04] well maybe not I don't know
[2440.04 → 2442.10] yeah I don't know
[2442.10 → 2444.56] that's job security
[2444.56 → 2447.14] yeah we do like having jobs
[2447.14 → 2451.04] I think I will ask this at the end
[2451.04 → 2455.58] I'll ask this now so you'll think about this for like the next couple of minutes in the back of your
[2455.58 → 2463.00] head but at the end I will ask you what do you see the development of the security role in the world of AI
[2463.00 → 2464.32] oh god
[2464.32 → 2466.46] think about it, and then we'll come back to that
[2466.46 → 2472.58] oh this is gonna be an extra popular opinion like a bonus one
[2472.58 → 2477.36] yeah I think a good thing to follow on from the go debug discussion would be
[2477.36 → 2481.46] you know we have this great you know we try and keep everything as compatible as possible
[2481.46 → 2485.72] we have this great way to introduce behaviour that may be breaking
[2485.72 → 2489.90] but I think there is also a discussion about what we want to do in the future
[2489.90 → 2493.68] where you know there are APIs we cannot change
[2493.68 → 2497.72] just you know they are what they are and what we wanted kind of how
[2497.72 → 2502.74] in those cases our only real option is to introduce a completely new package
[2502.74 → 2506.26] and we've done this has been done very sparingly
[2506.26 → 2509.14] in the standard library thus far but I think it is probably
[2509.14 → 2512.60] you know the world has changed a lot since the
[2512.60 → 2516.90] not just the crypto tree was written but a lot of the packages in the standard library were written
[2516.90 → 2522.38] we're kind of looking at this point to what do you know if not a go-to
[2522.38 → 2527.42] but a v2 of certain packages in the standard library look like
[2527.42 → 2531.44] and the first big one that this has happened for is the math rand package
[2531.44 → 2532.88] I don't know if you want to talk about that as well
[2532.88 → 2536.68] yeah so math rand is one of the things that ended up on
[2536.68 → 2542.20] every presentation about go foot guns because there's crypto rand which is good
[2542.20 → 2547.08] and there's math rand which is bad, and they are both called rand
[2547.08 → 2552.40] and they both have a read method so you might be excused for using rand. Read
[2552.40 → 2557.58] to generate your session ticket keys and then find out that actually you are importing
[2557.58 → 2562.28] math rand in that packet in that file and so you ended up using math rand to generate keys
[2562.28 → 2566.50] which why is it bad it's bad because it's completely predictable
[2566.50 → 2571.40] and I'm not just saying it has like a bad seed or anything like that
[2571.40 → 2575.86] I'm saying if I look at a few of the outputs I can predict the future ones
[2575.86 → 2582.20] there is no secure way to use math rand up to now
[2582.20 → 2587.76] but math rand is getting a v2 and the v2 critically doesn't have a read method
[2587.76 → 2592.98] so it can't be mistakenly used as easily in place of crypto rand
[2592.98 → 2599.70] and it's switching its default and this is I think here I can only claim credit for lobbying
[2599.70 → 2604.06] for this but mascot then went and did all the actual implementation
[2604.06 → 2608.36] but I think I convinced Russ to make the default cha-cha 8
[2608.36 → 2614.74] which is this reduced round version of the cha-cha 20 things that you use in TLS sometimes
[2614.74 → 2618.52] it's a cryptographic cipher so it's actually secure
[2618.52 → 2623.82] and it's almost as fast as the non-secure fast thing
[2623.82 → 2628.90] so it will default to that so that if by mistake you use math rand
[2628.90 → 2633.38] you'll actually not have done that much damage
[2633.38 → 2637.00] it will probably still be secure and I am so happy about that
[2637.00 → 2639.12] and we're getting that in the v2
[2639.12 → 2642.28] and v2 will not even have
[2642.28 → 2644.70] it will have a default source which is this
[2644.70 → 2649.54] and it will not be locked to a specific sequence of outputs
[2649.54 → 2652.40] because that was the other major thing that was a problem in math rand
[2652.40 → 2654.94] it could never change what outputs it returned
[2654.94 → 2658.06] because programs had come to rely on those
[2658.06 → 2661.08] and that's how seriously we take the compatibility promise
[2661.08 → 2663.28] wait, rely on math rand being
[2663.28 → 2664.94] yeah, deterministically random
[2664.94 → 2665.38] okay
[2665.38 → 2668.46] so math rand will always return the same outputs
[2668.46 → 2670.30] if you give it the same seed
[2670.30 → 2673.24] yeah, yeah, but companies relying on math rand to be persistent
[2673.24 → 2675.52] is the thing I needed to hear twice
[2675.52 → 2675.80] okay
[2675.80 → 2679.38] oh yes, you change the sequence and things break
[2679.38 → 2679.98] it's great
[2679.98 → 2683.38] really, like, open source maintenance is great
[2683.38 → 2686.42] and if you are looking for something that's more mind-bending
[2686.42 → 2689.04] I can recommend standard library maintenance
[2689.04 → 2691.42] is that your other unpopular opinion?
[2694.00 → 2695.88] but yes, I'm excited about v2
[2695.88 → 2701.66] and we are starting to think about what v2s of packages in the crypto
[2701.66 → 2704.32] well, of the crypto packages would look like
[2704.32 → 2706.78] because there are things like Heads
[2706.78 → 2709.78] which are just a fancy name for the thing that encrypts stuff
[2709.78 → 2715.10] like AES256GCM or Chacha20POL1305
[2715.10 → 2719.20] so you have a key and a message, and you want to encrypt it
[2719.20 → 2721.80] and right now the API is kind of hard to use
[2721.80 → 2723.78] you have to separately generate the lungs
[2723.78 → 2726.34] and have opinions on how to generate the lungs
[2726.34 → 2728.08] and then where to put it
[2728.08 → 2730.14] and lungs is a number used once
[2730.14 → 2732.36] so it has to never, never, ever repeat
[2732.36 → 2734.14] and what happens if it repeats?
[2734.26 → 2734.80] it depends on
[2734.80 → 2735.82] it depends on what you were using
[2735.82 → 2736.92] it could be catastrophic
[2736.92 → 2737.68] it could be
[2737.68 → 2739.04] most of the time it's catastrophic
[2739.04 → 2740.68] but sometimes it's okay
[2740.68 → 2741.74] but how do you know?
[2741.82 → 2742.20] you don't
[2742.20 → 2745.62] so we want to make higher level APIs for that
[2745.62 → 2747.30] and things that just say
[2747.30 → 2748.06] yeah, you know
[2748.06 → 2750.04] we'll take care of generating it
[2750.04 → 2752.20] we'll prepend it to decipher text
[2752.20 → 2754.32] you don't even have to know it exists
[2754.32 → 2756.26] don't even need to know it's a thing
[2756.26 → 2758.16] and then we'll pick primitives
[2758.16 → 2760.24] where we can do that
[2760.24 → 2762.04] instead of having to ask the application
[2762.04 → 2764.96] to respect some strict rules or else
[2764.96 → 2766.20] and so that means
[2766.20 → 2767.20] for example
[2767.20 → 2770.04] making new APIs that expose x
[2770.04 → 2771.14] ChachaPOL1305
[2771.14 → 2773.16] instead of Chacha20POL1305
[2773.16 → 2773.92] which
[2773.92 → 2776.24] should anybody care about the difference
[2776.24 → 2777.88] between the x and the known x?
[2777.88 → 2780.16] well, nobody should
[2780.16 → 2780.60] but
[2780.60 → 2781.64] it is
[2781.64 → 2782.56] very important
[2782.56 → 2784.00] because it will make the difference
[2784.00 → 2784.40] between
[2784.40 → 2786.14] you're allowed to encrypt
[2786.14 → 2786.66] at most
[2786.66 → 2787.88] a couple million messages
[2787.88 → 2788.52] which
[2788.52 → 2788.98] you know
[2788.98 → 2791.24] sometimes you have more than 2 million files
[2791.24 → 2792.10] or
[2792.10 → 2793.68] not having that problem
[2793.68 → 2794.12] right
[2794.12 → 2794.56] and we
[2794.56 → 2796.14] we shouldn't require users
[2796.14 → 2796.98] to kind of know
[2796.98 → 2798.56] these arcane details
[2798.56 → 2799.44] in order to make
[2799.44 → 2800.68] secure decisions
[2800.68 → 2802.40] I think that's one of the real problems
[2802.40 → 2803.16] with a lot of
[2803.16 → 2803.80] the
[2803.80 → 2805.58] the cryptography libraries are good
[2805.58 → 2807.80] but they assume you
[2807.80 → 2809.22] have a lot of knowledge
[2809.22 → 2810.64] in order to use them safely
[2810.64 → 2811.14] which
[2811.14 → 2812.34] still less than
[2812.34 → 2813.58] other cryptography libraries
[2813.58 → 2814.26] I feel like
[2814.26 → 2815.64] we tend to be a little too
[2815.64 → 2816.38] doom and gloom
[2816.38 → 2817.12] the two of us
[2817.12 → 2819.40] because we want it to be better
[2819.40 → 2820.58] but
[2820.58 → 2821.36] I think that's
[2821.36 → 2823.22] because the bar is already so high
[2823.22 → 2823.78] for the Go
[2823.78 → 2824.88] standard library
[2824.88 → 2825.12] right
[2825.12 → 2826.84] we made good decisions
[2826.84 → 2828.46] we didn't make the best decisions
[2828.46 → 2829.66] but
[2829.66 → 2831.14] in the grander scheme of things
[2831.14 → 2832.34] we're still doing a lot better
[2832.34 → 2832.66] than
[2832.66 → 2834.32] a lot of other people
[2834.32 → 2835.00] yep
[2835.00 → 2835.66] but yeah
[2835.66 → 2836.42] I'm excited
[2836.42 → 2837.04] I think
[2837.04 → 2837.98] this is one of
[2837.98 → 2839.50] the most exciting times
[2839.50 → 2840.06] to be working
[2840.06 → 2840.94] on the
[2840.94 → 2842.02] cryptography libraries
[2842.02 → 2843.28] because we get to
[2843.28 → 2845.00] make the mistakes
[2845.00 → 2846.32] that will haunt us
[2846.32 → 2847.30] for the next 10 years
[2847.30 → 2848.00] and
[2848.00 → 2849.08] that's fun
[2849.08 → 2850.04] yeah
[2850.04 → 2851.02] yeah well
[2851.02 → 2851.34] and
[2851.34 → 2852.32] you say that right
[2852.32 → 2853.12] we're kind of
[2853.12 → 2854.44] probably the biggest thing
[2854.44 → 2855.96] that will come in the standard library
[2855.96 → 2857.64] the crypto part of the standard library
[2857.64 → 2858.96] in the next two or three years
[2858.96 → 2859.98] will be post-quantum
[2859.98 → 2860.68] algorithms
[2860.68 → 2862.34] which you know
[2862.34 → 2863.44] are very cutting edge
[2863.44 → 2863.92] at the moment
[2863.92 → 2865.42] and we are
[2865.42 → 2866.16] you know
[2866.16 → 2867.24] we will get
[2867.24 → 2868.10] exactly like you say
[2868.10 → 2868.86] we will get to make
[2868.86 → 2869.98] API design choices
[2869.98 → 2870.90] that may come back
[2870.90 → 2871.56] to haunt us
[2871.56 → 2873.70] in 5 or 10 years time
[2873.70 → 2875.34] we kind of
[2875.34 → 2875.78] you know
[2875.78 → 2877.28] we don't have the
[2877.28 → 2878.28] 20 years
[2878.28 → 2879.50] of design experience
[2879.50 → 2880.64] or usage experience
[2880.64 → 2881.64] of these algorithms
[2881.64 → 2882.22] that
[2882.22 → 2884.22] we have with RSA
[2884.22 → 2885.08] it sounds like
[2885.08 → 2886.58] an episode number 3
[2886.58 → 2887.90] on the topic
[2887.90 → 2889.12] where episode number 2
[2889.12 → 2890.06] is the second half
[2890.06 → 2890.68] of this list
[2890.68 → 2892.26] and episode number 3
[2892.26 → 2893.32] is all the quantum things
[2893.32 → 2893.86] that you're planning
[2893.86 → 2894.70] to put in it
[2894.70 → 2895.24] yeah
[2895.24 → 2896.72] or all the mistakes
[2896.72 → 2897.34] we've made
[2897.34 → 2897.92] and
[2897.92 → 2900.14] and we'll be making
[2900.14 → 2900.84] this is the list
[2900.84 → 2901.46] of the mistakes
[2901.46 → 2902.38] that I plan to do
[2902.38 → 2903.26] yeah
[2903.26 → 2905.18] right yeah
[2905.18 → 2905.46] indeed
[2905.46 → 2906.40] there was a lot
[2906.40 → 2907.06] more stuff
[2907.06 → 2907.74] on the list
[2907.74 → 2908.14] because
[2908.14 → 2908.98] it's exciting
[2908.98 → 2909.62] also because
[2909.62 → 2910.54] we're now getting
[2910.54 → 2911.76] to work
[2911.76 → 2912.40] on things like
[2912.40 → 2913.20] SSH
[2913.20 → 2913.90] and there are
[2913.90 → 2915.00] more people on board
[2915.00 → 2915.48] there's
[2915.48 → 2916.48] Nicola Marino
[2916.48 → 2917.36] now who's working
[2917.36 → 2917.86] on the
[2917.86 → 2919.40] golan.org
[2919.40 → 2920.00] slash x
[2920.00 → 2920.68] slash crypto
[2920.68 → 2922.32] slash SSH package
[2922.32 → 2923.16] which
[2923.16 → 2924.10] possibly
[2924.10 → 2925.04] one of the
[2925.04 → 2926.18] underestimated
[2926.18 → 2926.74] packages
[2926.74 → 2928.26] in our purview
[2928.26 → 2929.00] that really needed
[2929.00 → 2929.66] a maintainer
[2929.66 → 2930.12] yep
[2930.12 → 2931.06] it's second
[2931.06 → 2931.50] perhaps
[2931.50 → 2933.04] to the TLS package
[2933.04 → 2933.82] as one of the
[2933.82 → 2934.94] most important packages
[2934.94 → 2936.28] that nobody thinks about
[2936.28 → 2937.26] maybe because
[2937.26 → 2938.42] it works a little too well
[2938.42 → 2939.22] but you know
[2939.22 → 2940.84] that's not true forever
[2940.84 → 2942.88] that our SSH package
[2942.88 → 2944.18] had started to rot
[2944.18 → 2945.18] I remember
[2945.18 → 2946.68] just scrambling
[2946.68 → 2947.54] because it was about
[2947.54 → 2948.26] to stop working
[2948.26 → 2948.78] with GitHub
[2948.78 → 2950.50] and that would have
[2950.50 → 2951.02] been bad
[2951.02 → 2951.72] for all the
[2951.72 → 2952.46] CI companies
[2952.46 → 2953.64] for reasons
[2953.64 → 2954.32] you can imagine
[2954.32 → 2955.36] and so we had to
[2955.36 → 2957.04] roll out very quickly
[2957.04 → 2957.82] the changes
[2957.82 → 2958.64] but now instead
[2958.64 → 2959.88] we're much more
[2959.88 → 2960.86] ahead of the curve
[2960.86 → 2961.78] I think we implemented
[2961.78 → 2962.46] a thing like
[2962.46 → 2963.22] support for
[2963.22 → 2963.82] keystroke
[2963.82 → 2964.54] obfuscation
[2964.54 → 2965.80] at the same time
[2965.80 → 2966.46] as OpenSSH
[2966.46 → 2967.22] added it
[2967.22 → 2968.38] which is
[2968.38 → 2970.00] six years faster
[2970.00 → 2971.02] than we've usually
[2971.02 → 2971.96] been able to do
[2971.96 → 2973.46] so I'm very happy
[2973.46 → 2974.18] about what Nicola
[2974.18 → 2974.60] is doing
[2974.60 → 2976.10] maybe we will have
[2976.10 → 2976.88] Nicola on
[2976.88 → 2978.14] for episode two
[2978.14 → 2979.32] for part two
[2979.32 → 2980.40] yeah that
[2980.40 → 2981.58] sounds like a good plan
[2981.58 → 2982.76] what else sounds
[2982.76 → 2983.60] like a good plan
[2983.60 → 3007.60] so gentlemen
[3007.60 → 3008.26] what did you bring
[3008.26 → 3008.78] with you as an
[3008.78 → 3009.72] unpopular opinion
[3009.72 → 3011.80] I have an opinion
[3011.80 → 3012.28] that is
[3012.28 → 3013.70] tactically chosen
[3013.70 → 3014.26] to annoy
[3014.26 → 3015.20] the most people
[3015.20 → 3015.80] possible
[3015.80 → 3017.92] everything is legit
[3017.92 → 3018.60] in this section
[3018.60 → 3019.74] okay
[3019.74 → 3020.48] so
[3020.48 → 3021.74] there is
[3021.74 → 3022.02] you know
[3022.02 → 3022.56] one of the
[3022.56 → 3023.04] ongoing
[3023.04 → 3024.18] debates
[3024.18 → 3025.32] between software
[3025.32 → 3025.74] engineers
[3025.74 → 3026.44] is what is
[3026.44 → 3026.88] the best
[3026.88 → 3027.86] terminal text
[3027.86 → 3028.26] editor
[3028.26 → 3029.30] okay
[3029.30 → 3031.70] Filippo is making
[3031.70 → 3032.36] a great face
[3032.36 → 3034.50] it's a scary
[3034.50 → 3035.34] body language
[3035.34 → 3035.84] right
[3035.84 → 3036.24] this is
[3036.24 → 3037.50] typically this argument
[3037.50 → 3038.24] is between people
[3038.24 → 3039.00] who really enjoy
[3039.00 → 3039.66] Emacs
[3039.66 → 3040.16] and people
[3040.16 → 3041.00] who really enjoy
[3041.00 → 3042.04] Vi or Vim
[3042.04 → 3043.96] I take the third
[3043.96 → 3044.58] position
[3044.58 → 3045.34] because I think
[3045.34 → 3046.12] that they're both
[3046.12 → 3046.64] terrible
[3046.64 → 3048.66] and that in fact
[3048.66 → 3049.98] the best text editor
[3049.98 → 3051.06] is Pico
[3051.06 → 3054.50] which is a wonder
[3054.50 → 3056.00] it's incredibly lightweight
[3056.00 → 3058.28] it tells you all the
[3058.28 → 3059.52] shortcuts that you need
[3059.52 → 3059.80] you know
[3059.80 → 3060.86] you don't have to find
[3060.86 → 3062.00] a secret manual
[3062.00 → 3062.54] somewhere
[3062.54 → 3064.12] and it just does
[3064.12 → 3064.82] what you want
[3064.82 → 3065.56] and it's on
[3065.56 → 3066.68] almost every system
[3066.68 → 3068.70] I strongly disagree
[3068.70 → 3069.64] I actually think
[3069.64 → 3070.44] the best one
[3070.44 → 3071.60] is Joe
[3071.60 → 3073.00] which is the only one
[3073.00 → 3073.82] I ever learned
[3073.82 → 3074.52] to use
[3074.52 → 3076.38] you're going to have
[3076.38 → 3077.06] to add links
[3077.06 → 3077.78] to both of them
[3077.78 → 3078.46] in the show notes
[3078.46 → 3079.24] for people to know
[3079.24 → 3080.38] what are you talking about
[3080.38 → 3081.30] oh Joe
[3081.30 → 3082.66] is an even simpler
[3082.66 → 3084.30] and more for
[3084.30 → 3084.64] you know
[3084.64 → 3085.76] beginners version
[3085.76 → 3087.98] it's great for people
[3087.98 → 3088.70] who are programming
[3088.70 → 3089.54] in doctor scheme
[3089.54 → 3092.16] I think my opinion
[3092.16 → 3093.16] is very much
[3093.16 → 3094.16] formulated by the fact
[3094.16 → 3094.96] that the very first
[3094.96 → 3096.62] I learned how to use
[3096.62 → 3097.04] email
[3097.04 → 3099.04] from my mother
[3099.04 → 3100.42] who would
[3100.42 → 3101.28] had a
[3101.28 → 3101.78] you know
[3101.78 → 3102.72] an email account
[3102.72 → 3103.76] from her university
[3103.76 → 3104.90] and would tell
[3104.90 → 3105.22] you know
[3105.22 → 3106.64] tell that into a server
[3106.64 → 3108.22] at the university
[3108.22 → 3109.24] and use Alpine
[3109.24 → 3110.68] which is a very
[3110.68 → 3112.18] old email client
[3112.18 → 3112.72] that is
[3112.72 → 3114.44] Alpine is actually
[3114.44 → 3114.88] terrible
[3114.88 → 3115.62] but
[3115.62 → 3117.12] but Pico
[3117.12 → 3118.00] is a text editor
[3118.00 → 3118.98] based on the
[3118.98 → 3119.56] semantics
[3119.56 → 3120.20] of Alpine
[3120.20 → 3121.48] so
[3121.48 → 3122.26] when I first
[3122.26 → 3122.96] started actually
[3122.96 → 3124.04] doing software
[3124.04 → 3124.40] engineering
[3124.40 → 3125.14] and I was using
[3125.14 → 3125.44] you know
[3125.44 → 3125.82] I was like
[3125.82 → 3126.54] oh I can own
[3126.54 → 3127.30] you know
[3127.30 → 3128.44] now I use an IDE
[3128.44 → 3129.36] because I'm a normal
[3129.36 → 3129.84] person
[3129.84 → 3130.66] but
[3130.66 → 3131.96] at first I was like
[3131.96 → 3132.76] oh I have to use
[3132.76 → 3134.02] my terminal text editor
[3134.02 → 3134.88] because that's what
[3134.88 → 3136.20] all the cool people do
[3136.20 → 3137.02] and I
[3137.02 → 3137.46] you know
[3137.46 → 3139.02] Emacs and Vim
[3139.02 → 3139.92] both make
[3139.92 → 3141.06] make me cry
[3141.06 → 3141.32] I
[3141.32 → 3143.46] I've tried multiple
[3143.46 → 3144.56] times to use both of them
[3144.56 → 3145.26] and I just cannot
[3145.26 → 3146.82] get my head around it
[3146.82 → 3147.42] and Pico
[3147.42 → 3148.06] was just great
[3148.06 → 3148.74] because you know
[3148.74 → 3150.56] you just type in it
[3150.56 → 3151.96] like you would a normal text editor
[3151.96 → 3153.18] and it has shortcuts
[3153.18 → 3154.16] but it has a little bar
[3154.16 → 3154.60] at the bottom
[3154.60 → 3155.36] that tells you
[3155.36 → 3156.70] what the shortcuts are
[3156.70 → 3157.40] so if you
[3157.40 → 3158.18] if you forget
[3158.18 → 3159.12] it's very easy
[3159.12 → 3159.98] to figure out
[3159.98 → 3161.80] but I don't
[3161.80 → 3162.40] this is not something
[3162.40 → 3163.34] I will tell people
[3163.34 → 3163.66] when I
[3163.66 → 3165.42] you know
[3165.42 → 3166.06] I'm exposing
[3166.06 → 3167.00] my greatest secret
[3167.00 → 3167.66] right now
[3167.66 → 3170.24] I truly enjoy
[3170.24 → 3171.08] that we spent
[3171.08 → 3171.76] like an hour
[3171.76 → 3172.50] talking about
[3172.50 → 3173.14] the intricacies
[3173.14 → 3174.10] of cryptography
[3174.10 → 3174.88] and being like
[3174.88 → 3175.18] oh yeah
[3175.18 → 3176.32] the Go security team
[3176.32 → 3176.96] and then we just
[3176.96 → 3177.96] went all out
[3177.96 → 3178.50] when we
[3178.50 → 3179.60] we disagree
[3179.60 → 3180.62] on which editor
[3180.62 → 3181.12] is the best
[3181.12 → 3181.94] because we used
[3181.94 → 3183.46] two of the simplest
[3183.46 → 3185.74] editors possible
[3185.74 → 3187.80] this is like
[3187.80 → 3188.80] when people say
[3188.80 → 3189.04] oh
[3189.04 → 3189.88] real programmers
[3189.88 → 3191.26] use keyboard shortcuts
[3191.26 → 3191.98] for everything
[3191.98 → 3192.78] they don't touch
[3192.78 → 3193.18] the mouse
[3193.18 → 3194.06] and Rob Pike
[3194.06 → 3194.46] answers
[3194.46 → 3195.02] I guess
[3195.02 → 3195.72] I'm not a real
[3195.72 → 3196.58] programmer then
[3196.58 → 3198.92] yeah
[3198.92 → 3199.26] because
[3199.26 → 3200.18] plan 9
[3200.18 → 3200.84] is entirely
[3200.84 → 3201.74] mouse based
[3201.74 → 3203.18] well not entirely
[3203.18 → 3204.12] but you do a lot
[3204.12 → 3204.58] with the mouse
[3204.58 → 3205.26] because you know
[3205.26 → 3206.24] 2D input
[3206.24 → 3206.68] is actually
[3206.68 → 3207.52] kind of nice
[3207.52 → 3207.92] yeah
[3207.92 → 3208.44] it turns out
[3208.44 → 3208.76] the mouse
[3208.76 → 3209.72] was a good invention
[3209.72 → 3210.50] yeah
[3210.50 → 3211.38] it's okay
[3211.38 → 3213.18] it's totally okay
[3213.18 → 3213.92] to use the mouse
[3213.92 → 3216.26] or a keypad
[3216.26 → 3217.12] we're not judging
[3217.12 → 3217.76] yes
[3217.76 → 3218.32] Filippo
[3218.32 → 3218.78] do you have
[3218.78 → 3219.58] an unpopular opinion
[3219.58 → 3220.34] or have you been
[3220.34 → 3221.40] just sharing them
[3221.40 → 3222.08] throughout the episode
[3222.08 → 3224.46] I'm going to go
[3224.46 → 3225.56] with one that's
[3225.56 → 3226.34] more topical
[3226.34 → 3226.82] this time
[3226.82 → 3228.26] and this one
[3228.26 → 3228.96] I think will have
[3228.96 → 3229.78] the opposite effect
[3229.78 → 3230.24] of Rollins
[3230.24 → 3231.08] it will make
[3231.08 → 3232.08] very upset
[3232.08 → 3233.26] but a tiny
[3233.26 → 3234.08] amount
[3234.08 → 3235.66] of the listeners
[3235.66 → 3237.06] so there's
[3237.06 → 3238.36] these elliptic curves
[3238.36 → 3239.28] that are
[3239.28 → 3240.00] the NIST
[3240.00 → 3240.68] elliptic curves
[3240.68 → 3241.12] the ones
[3241.12 → 3242.28] standardized
[3242.28 → 3243.24] by the
[3243.24 → 3244.20] National Institute
[3244.20 → 3246.04] of Standards
[3246.04 → 3246.80] and
[3246.80 → 3247.60] technology
[3247.60 → 3248.38] and technology
[3248.38 → 3248.84] thank you
[3248.84 → 3249.96] and it's a
[3249.96 → 3251.06] US agency
[3251.06 → 3252.74] and they have
[3252.74 → 3253.52] collaborations
[3253.52 → 3254.46] with the NSA
[3254.46 → 3255.34] and you know
[3255.34 → 3255.96] there are people
[3255.96 → 3256.76] who think that
[3256.76 → 3257.90] they're clearly
[3257.90 → 3259.70] in cahoots
[3259.70 → 3260.82] and clearly
[3260.82 → 3261.78] trying to
[3261.78 → 3262.70] sabotage
[3262.70 → 3263.16] all the
[3263.16 → 3263.74] cryptography
[3263.74 → 3264.88] and including
[3264.88 → 3265.92] the new
[3265.92 → 3266.54] post-quantum
[3266.54 → 3267.00] stuff
[3267.00 → 3268.92] and so on
[3268.92 → 3270.14] and then there's
[3270.14 → 3270.96] these other curves
[3270.96 → 3271.60] which are
[3271.60 → 3272.68] half of their
[3272.68 → 3273.26] selling point
[3273.26 → 3273.76] is that they're
[3273.76 → 3274.46] not made by
[3274.46 → 3274.76] NIST
[3274.76 → 3275.38] who's evil
[3275.38 → 3275.76] right
[3275.76 → 3276.90] and my
[3276.90 → 3277.50] unpopular opinion
[3277.50 → 3278.02] is that the
[3278.02 → 3278.56] NIST curves
[3278.56 → 3279.42] are great
[3279.42 → 3280.70] they're absolutely
[3280.70 → 3281.22] fine
[3281.22 → 3282.18] they had the
[3282.18 → 3282.54] problem
[3282.54 → 3283.04] they used to
[3283.04 → 3283.30] have the
[3283.30 → 3283.60] problem
[3283.60 → 3284.06] that we
[3284.06 → 3285.16] didn't have
[3285.16 → 3286.08] good formulas
[3286.08 → 3286.76] for them
[3286.76 → 3287.56] like very
[3287.56 → 3287.98] specifically
[3287.98 → 3288.70] mathematical
[3288.70 → 3289.22] formulas
[3289.22 → 3290.10] and then
[3290.10 → 3290.62] was it
[3290.62 → 3291.00] Barrett
[3291.00 → 3291.84] I think
[3291.84 → 3292.66] anyway
[3292.66 → 3294.34] in 2016
[3294.34 → 3294.86] or something
[3294.86 → 3295.26] like that
[3295.26 → 3296.70] these cryptographers
[3296.70 → 3297.28] just published
[3297.28 → 3297.64] a paper
[3297.64 → 3298.20] with better
[3298.20 → 3298.82] formulas for
[3298.82 → 3299.02] them
[3299.02 → 3299.60] and now
[3299.60 → 3299.90] we have
[3299.90 → 3300.24] the good
[3300.24 → 3300.62] formulas
[3300.62 → 3301.12] for them
[3301.12 → 3301.92] and now
[3301.92 → 3302.40] they're great
[3302.40 → 3303.30] they're prime
[3303.30 → 3303.98] order curves
[3303.98 → 3305.10] they are generated
[3305.10 → 3306.34] from a hash
[3306.34 → 3307.28] do we know
[3307.28 → 3307.92] what the hash
[3307.92 → 3308.32] is
[3308.32 → 3309.26] no
[3309.26 → 3310.58] trying to
[3310.58 → 3311.02] work with
[3311.02 → 3311.62] on that
[3311.62 → 3312.18] if anybody
[3312.18 → 3312.98] finds it
[3312.98 → 3313.76] there I have
[3313.76 → 3315.16] $12,000
[3315.16 → 3315.94] for them
[3315.94 → 3316.38] I'm not
[3316.38 → 3316.66] kidding
[3316.66 → 3317.98] I actually
[3317.98 → 3318.84] have $12,000
[3318.84 → 3320.02] earmarked
[3320.02 → 3321.48] as a challenge
[3321.48 → 3322.02] you can
[3322.02 → 3322.56] search
[3322.56 → 3323.00] NIST
[3323.00 → 3326.28] not quite
[3326.28 → 3326.60] literally
[3326.60 → 3327.12] but yes
[3327.12 → 3327.76] honestly
[3327.76 → 3328.20] if you want
[3328.20 → 3328.58] to make
[3328.58 → 3328.80] it
[3328.80 → 3329.76] a suitcase
[3329.76 → 3330.22] delivery
[3330.22 → 3330.92] if you
[3330.92 → 3331.50] found the
[3331.50 → 3331.88] seeds
[3331.88 → 3332.64] I will
[3332.64 → 3333.08] deliver
[3333.08 → 3333.84] the bounty
[3333.84 → 3334.40] to you
[3334.40 → 3334.78] in a
[3334.78 → 3335.12] suitcase
[3335.12 → 3335.74] what about
[3335.74 → 3336.62] a burlap
[3336.62 → 3337.00] sack
[3337.00 → 3337.58] with a dollar
[3337.58 → 3337.90] side
[3337.90 → 3338.22] on the
[3338.22 → 3338.64] side
[3338.64 → 3339.16] it seems
[3339.16 → 3339.66] more appealing
[3339.66 → 3340.08] to me
[3340.08 → 3340.38] but
[3340.38 → 3341.10] I'm a
[3341.10 → 3341.66] theatre kid
[3341.66 → 3342.16] I will
[3342.16 → 3342.72] absolutely
[3342.72 → 3343.18] go for
[3343.18 → 3343.50] such a
[3343.50 → 3343.74] drama
[3343.74 → 3345.74] you would
[3345.74 → 3346.22] just make
[3346.22 → 3346.62] me happy
[3346.62 → 3347.32] there is
[3347.32 → 3347.62] the thing
[3347.62 → 3347.88] where you
[3347.88 → 3348.14] can't
[3348.14 → 3348.34] cross
[3348.34 → 3348.76] borders
[3348.76 → 3349.18] with more
[3349.18 → 3349.66] than 10k
[3349.66 → 3350.04] we will
[3350.04 → 3350.56] figure it
[3350.56 → 3350.74] out
[3350.74 → 3352.86] we'll
[3352.86 → 3353.18] figure it
[3353.18 → 3353.32] out
[3353.32 → 3353.86] I'm Italian
[3353.86 → 3354.56] I'm sure
[3354.56 → 3356.10] I can
[3356.10 → 3358.60] work it
[3358.60 → 3358.74] out
[3358.74 → 3359.32] but anyway
[3359.32 → 3360.48] do we know
[3360.48 → 3361.04] exactly
[3361.04 → 3362.24] the history
[3362.24 → 3362.54] of it
[3362.54 → 3362.78] no
[3362.78 → 3363.28] but they
[3363.28 → 3363.52] are
[3363.52 → 3364.68] safe
[3364.68 → 3365.00] enough
[3365.00 → 3365.24] they've
[3365.24 → 3365.36] been
[3365.36 → 3365.62] secure
[3365.62 → 3366.34] for years
[3366.34 → 3367.32] and they
[3367.32 → 3367.58] actually
[3367.58 → 3368.06] have less
[3368.06 → 3368.52] problems
[3368.52 → 3368.86] than
[3368.86 → 3369.46] alternative
[3369.46 → 3369.80] curves
[3369.80 → 3370.02] these
[3370.02 → 3370.28] days
[3370.28 → 3370.72] so
[3370.72 → 3371.20] actually
[3371.20 → 3371.96] NIST
[3371.96 → 3372.26] curves
[3372.26 → 3372.96] are fine
[3372.96 → 3373.80] and this
[3373.80 → 3374.14] will
[3374.14 → 3374.86] sound
[3374.86 → 3375.38] like
[3375.38 → 3376.12] the least
[3376.12 → 3376.48] unpopular
[3376.48 → 3376.86] opinion
[3376.86 → 3377.28] to a bunch
[3377.28 → 3377.66] of people
[3377.66 → 3378.18] and a
[3378.18 → 3378.48] bunch
[3378.48 → 3378.88] of
[3378.88 → 3379.52] a few
[3379.52 → 3379.84] other
[3379.84 → 3380.16] people
[3380.16 → 3380.46] instead
[3380.46 → 3380.74] will
[3380.74 → 3381.28] scream
[3381.28 → 3381.64] in my
[3381.64 → 3382.14] mentions
[3382.14 → 3382.96] in like
[3382.96 → 3383.92] two hours
[3383.92 → 3384.84] okay
[3384.84 → 3385.64] let's see
[3385.64 → 3386.26] let's see if
[3386.26 → 3386.70] the unpopular
[3386.70 → 3387.10] opinion
[3387.10 → 3387.40] and the
[3387.40 → 3387.82] prediction
[3387.82 → 3388.74] were working
[3388.74 → 3389.86] I'm coming
[3389.86 → 3390.20] with an
[3390.20 → 3390.60] unpopular
[3390.60 → 3390.98] opinion
[3390.98 → 3391.42] that is
[3391.42 → 3392.52] not fun
[3392.52 → 3392.82] and not
[3392.82 → 3393.06] easy
[3393.06 → 3394.16] and sure
[3394.16 → 3394.72] is loaded
[3394.72 → 3396.72] and affected
[3396.72 → 3397.20] by the
[3397.20 → 3397.64] situation
[3397.64 → 3398.16] recently
[3398.16 → 3398.80] or
[3398.80 → 3399.52] everything
[3399.52 → 3399.94] that's been
[3399.94 → 3400.42] going on
[3400.42 → 3401.58] I've just
[3401.58 → 3402.06] been talking
[3402.06 → 3402.74] started talking
[3402.74 → 3403.20] about how
[3403.20 → 3403.96] I'm coming
[3403.96 → 3404.62] out of
[3404.62 → 3405.84] the quite
[3405.84 → 3406.28] hard two
[3406.28 → 3406.58] weeks
[3406.58 → 3407.24] so I
[3407.24 → 3407.70] think
[3407.70 → 3408.30] that
[3408.30 → 3409.64] taking
[3409.64 → 3410.20] hostages
[3410.20 → 3410.68] babies
[3410.68 → 3411.18] and little
[3411.18 → 3411.42] kids
[3411.42 → 3411.78] should be
[3411.78 → 3412.04] condemned
[3412.04 → 3412.70] by everyone
[3412.70 → 3413.06] and should
[3413.06 → 3413.42] not be
[3413.42 → 3413.88] associated
[3413.88 → 3415.06] with one
[3415.06 → 3415.50] political
[3415.50 → 3415.90] opinion
[3415.90 → 3416.32] another
[3416.32 → 3417.52] or the
[3417.52 → 3417.74] lack
[3417.74 → 3418.14] of it
[3418.14 → 3418.90] good luck
[3418.90 → 3419.14] to me
[3419.14 → 3419.60] having this
[3419.60 → 3420.26] on the
[3420.26 → 3420.52] Twitter
[3420.52 → 3421.18] poll
[3421.18 → 3422.00] but I
[3422.00 → 3422.70] do want
[3422.70 → 3422.92] to say
[3422.92 → 3423.22] that
[3423.22 → 3425.00] and I
[3425.00 → 3425.44] want to
[3425.44 → 3426.00] say thank
[3426.00 → 3426.28] you very
[3426.28 → 3426.66] much to
[3426.66 → 3427.04] you both
[3427.04 → 3427.58] for joining
[3427.58 → 3428.26] thank you
[3428.26 → 3428.78] thank you
[3428.78 → 3429.08] for having
[3429.08 → 3429.32] us
[3429.32 → 3429.72] there will
[3429.72 → 3430.16] be episode
[3430.16 → 3430.70] number two
[3430.70 → 3431.62] on the
[3431.62 → 3432.08] second part
[3432.08 → 3432.30] of the
[3432.30 → 3432.52] list
[3432.52 → 3432.86] there will
[3432.86 → 3433.08] be an
[3433.08 → 3433.30] episode
[3433.30 → 3433.74] number three
[3433.74 → 3433.96] on the
[3433.96 → 3434.64] quantum stuff
[3434.64 → 3435.72] and until
[3435.72 → 3436.40] then have a
[3436.40 → 3436.88] happy Halloween
[3436.88 → 3449.56] if you like
[3449.56 → 3450.66] this spooky
[3450.66 → 3451.56] rendition of
[3451.56 → 3451.98] the go time
[3451.98 → 3453.02] theme check
[3453.02 → 3453.74] out our new
[3453.74 → 3454.78] music album on
[3454.78 → 3456.00] Spotify and
[3456.00 → 3456.68] Apple Music
[3456.68 → 3458.26] yes changelog
[3458.26 → 3458.74] beats
[3458.74 → 3459.56] is now a
[3459.56 → 3459.90] thing
[3459.90 → 3460.48] our
[3460.48 → 3460.90] zero
[3460.90 → 3461.80] volume is
[3461.80 → 3462.14] called
[3462.14 → 3462.80] theme songs
[3462.80 → 3463.56] and it
[3463.56 → 3463.96] includes
[3463.96 → 3464.32] special
[3464.32 → 3464.80] remixes
[3464.80 → 3465.56] in addition
[3465.56 → 3465.82] to the
[3465.82 → 3466.20] classics
[3466.20 → 3467.06] and our
[3467.06 → 3467.58] first volume
[3467.58 → 3467.98] is called
[3467.98 → 3468.76] next level
[3468.76 → 3469.76] featuring many
[3469.76 → 3470.14] of the
[3470.14 → 3470.58] video game
[3470.58 → 3471.38] inspired tracks
[3471.38 → 3471.80] you've heard
[3471.80 → 3472.26] on go time
[3472.26 → 3472.52] over the
[3472.52 → 3472.82] years
[3472.82 → 3473.64] just search
[3473.64 → 3474.18] for changelog
[3474.18 → 3474.50] beats
[3474.50 → 3474.96] in your
[3474.96 → 3475.52] music playing
[3475.52 → 3475.80] app of
[3475.80 → 3476.08] choice
[3476.08 → 3476.68] you'll find
[3476.68 → 3476.96] us
[3476.96 → 3477.82] thanks once
[3477.82 → 3478.14] again to
[3478.14 → 3478.26] our
[3478.26 → 3478.78] partners
[3478.78 → 3480.12] fastly.com
[3480.12 → 3481.18] fly.io
[3481.18 → 3482.72] and typesense.org
[3482.72 → 3483.42] and to
[3483.42 → 3483.80] break master
[3483.80 → 3484.18] cylinder
[3484.18 → 3485.22] for collabing
[3485.22 → 3485.68] with us
[3485.68 → 3486.28] on all our
[3486.28 → 3486.64] music
[3486.64 → 3487.44] that's all
[3487.44 → 3487.84] for now
[3487.84 → 3488.44] but we'll
[3488.44 → 3488.78] talk to you
[3488.78 → 3489.14] again next
[3489.14 → 3489.66] time
[3489.66 → 3490.44] on go
[3490.44 → 3490.84] time
[3490.84 → 3503.22] game
[3503.22 → 3503.88] 9
[3503.88 → 3533.86] Thank you.
