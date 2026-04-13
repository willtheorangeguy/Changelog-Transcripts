[0.00 --> 5.22]  Bandwidth for JS Party is provided by Fastly. Learn more at Fastly.com.
[8.98 --> 13.04]  Welcome to JS Party, a weekly celebration of JavaScript and the web.
[13.42 --> 18.36]  Tune in live on Fridays at 3 p.m. U.S. Eastern at changelaw.com slash live.
[18.70 --> 22.74]  Join the community and Slack with us in real time. Head to changelaw.com slash community.
[23.26 --> 27.00]  Follow us on Twitter. We're at JS Party FM. And now on to the show.
[27.00 --> 31.40]  Hey, everybody. Welcome to JS Party, where it's a party every week with JavaScript.
[32.28 --> 34.82]  All right. Let's dive right into it.
[35.98 --> 40.58]  I want my voice to be heard that I think that's a dumb slogan. Move on.
[41.44 --> 44.66]  I kind of, I think it's dumb, but I like making Michael say it.
[45.04 --> 47.32]  Okay, that's fair. That's fair. That's very fair.
[47.42 --> 48.98]  That's really fair. That's really fair.
[49.34 --> 50.36]  All right. I'm Michael Rogers.
[50.74 --> 51.58]  I'm Alex Sexton.
[52.14 --> 53.34]  And I'm Rachel White.
[53.72 --> 56.18]  All right, everybody. Let's get this party started.
[56.18 --> 57.76]  Let's just dive right into the first topic.
[58.22 --> 59.42]  So Google broke the Internet.
[60.62 --> 67.48]  I don't know why they keep pointing out flaws in the Internet security, but they broke the Internet again.
[69.56 --> 75.68]  I thought they helped disclose it, but wasn't it like some German W, some acronym?
[76.32 --> 77.22]  I think it was the Germans.
[77.70 --> 78.08]  That's all I'm saying.
[78.88 --> 79.80]  It was the Germans.
[80.24 --> 80.40]  Yeah.
[81.58 --> 82.32]  Likely story.
[82.32 --> 83.78]  Okay. No, anyway.
[83.92 --> 87.04]  So SHA-1 hashing algorithm has been cracked.
[88.30 --> 94.22]  I guess like in 2005, there was a paper written that said theoretically it could be cracked, but nobody had done it yet.
[95.42 --> 101.66]  And apparently as of like 2010, the federal government said no government encryption can use any SHA-1 algorithms,
[101.76 --> 106.26]  which is a pretty good indication that foreign governments have been able to crack this for a while.
[106.26 --> 107.06]  Yeah.
[107.06 --> 107.12]  Yeah.
[107.52 --> 118.64]  The only person I've seen strongly support SHA-1 for the last six or seven years is Linus Torvalds and Git.
[119.30 --> 120.16]  It's so annoying.
[120.60 --> 122.24]  And not just kind of.
[122.34 --> 126.32]  He really was like, you guys are all super dumb for caring about this.
[126.84 --> 127.40]  I know.
[127.70 --> 128.58]  It's really crazy.
[128.84 --> 130.28]  He's still downplaying it, actually.
[130.52 --> 130.72]  Yeah.
[130.72 --> 136.72]  So backing up a little bit, let's just kind of get into like what is SHA-1 and what does it do?
[137.22 --> 139.70]  So does anybody else want to take a crack at this or do you want me to explain it?
[140.26 --> 143.94]  I only know it from like Git related stuff.
[144.44 --> 145.82]  So that's all.
[145.82 --> 146.22]  Right, right.
[146.42 --> 149.00]  Well, that's actually a really good way to explain it though, right?
[149.14 --> 153.60]  So the way that Git uses SHA-1 is kind of indicative of how everybody uses it,
[153.60 --> 158.44]  which is that you take a bunch of data and you say, oh, I want a unique identifier for this data.
[158.44 --> 159.48]  So you hash it, right?
[159.98 --> 163.86]  And that's what Git does to every change that comes into the Git tree.
[163.96 --> 166.98]  It gets this hash of the data and it uses that as the identifier.
[167.32 --> 171.58]  So if you like go to GitHub and you go to a project and then you click on commits
[171.58 --> 174.02]  and then you click on one of those commit links, in the URL bar,
[174.10 --> 176.78]  you'll see like this randomly kind of generated identifier.
[177.12 --> 180.06]  And that is a unique identifier for that hash.
[181.08 --> 184.84]  The problem is that if you could forge these, if you could, you know,
[184.84 --> 188.38]  like that's a very small amount of data representing a large amount of data.
[188.56 --> 190.92]  So theoretically, if you can reverse engineer the algorithm,
[191.00 --> 195.66]  you could come up with a different set of data that would also hash to that same thing.
[196.64 --> 200.58]  And people have been theoretically able to do this for a while and now they really can.
[201.96 --> 204.28]  It still costs like $100,000.
[206.82 --> 207.22]  Yeah.
[207.22 --> 212.64]  It'll get cheaper, but right now, like with the current algorithm, the current break,
[212.68 --> 216.26]  it's insane how much faster they can do it.
[216.34 --> 225.26]  But still, like with AWS, like spot instances, it costs around $100,000 to just like break a random thing.
[226.10 --> 229.28]  But how much do I have to pay like a Russian hackers that have a botnet?
[229.86 --> 230.44]  Oh, sure.
[230.44 --> 235.52]  Yeah, I mean, it's just like one Bitcoin, which is roughly $20,000.
[235.86 --> 236.18]  I wouldn't necessarily be worried about this.
[237.48 --> 238.56]  Sorry, I didn't hear that.
[238.94 --> 244.68]  I was saying I probably need to pay one Bitcoin, which is roughly $20,000 to get Russian hackers to break it.
[244.72 --> 245.44]  Oh, yeah, for sure.
[246.58 --> 253.96]  Yeah, the cost is still prohibitive to the point where no one's going to like troll you with this.
[253.96 --> 261.54]  Someone really needs to want, like there has to be a reason someone's doing this at this point.
[261.66 --> 264.40]  But that will only be true for like two months or something, right?
[264.44 --> 270.20]  Like people will make this better instantly and then exploit everybody across the board.
[271.10 --> 271.40]  Right.
[271.54 --> 274.76]  And it's pretty much a given now that governments can do this kind of at will.
[275.30 --> 275.62]  Oh, yeah.
[275.62 --> 288.90]  So what that means is that if your integrity checks involve you hashing with this algorithm, then now if you're just using those checks, people can just inject malware, just, you know, whatever they want.
[289.66 --> 289.74]  Right.
[289.84 --> 291.16]  So I have a question.
[291.16 --> 305.26]  If this has been relatively like not super secure for a while, what was the catalyst for people to be like, OK, it's finally time to stop using this thing?
[305.26 --> 307.52]  Was it was it something that Google did that you said?
[308.28 --> 308.52]  Oh, yeah.
[308.68 --> 309.02]  Yesterday.
[309.90 --> 310.22]  Yeah.
[310.46 --> 310.68]  Yeah.
[310.82 --> 317.82]  Well, honestly, I think most people in the security community have felt like since 2005 that you should stop using this.
[317.90 --> 320.86]  There are other algorithms that are just as good that don't have this problem.
[321.08 --> 325.26]  And in 2010, I think most reasonable companies said, hey, we should stop using this.
[325.26 --> 328.42]  Like I said.
[329.42 --> 336.08]  Browsers already like don't allow like you'll get a very big red X instead of a green lock.
[336.88 --> 341.10]  If, you know, the shot one is used for for web security stuff.
[341.50 --> 348.08]  It's been well known to be very crackable by someone with a ton of money for a long time.
[348.08 --> 348.84]  Yeah.
[349.02 --> 353.68]  But but like Alex said, Linus Torvald has just remained unimpressed by evidence.
[354.16 --> 358.72]  And so it is still in heavy use in Git and GitHub and a bunch.
[358.78 --> 363.36]  I mean, that's that's fine because I'm wholly unimpressed by him.
[363.64 --> 363.82]  So.
[366.50 --> 366.98]  Yeah.
[367.46 --> 369.30]  It's you're only going to make him stronger.
[369.30 --> 369.38]  Sure.
[371.08 --> 371.66]  But yeah.
[371.76 --> 382.22]  So to answer your question, the thing that happened yesterday was that some people from Google and the Germans came out and just said, hey, look, we cracked it.
[382.30 --> 383.68]  Like, here's exactly how we cracked it.
[383.68 --> 389.12]  So it went from theoretical to, you know, here is, you know, an open version of this.
[389.66 --> 395.42]  To be to be totally clear, though, it's it's still like they have to try a ton of things.
[395.42 --> 403.54]  It's it's like they were able to reduce the subset that you had to brute force to a small enough amount to be significant.
[403.54 --> 409.84]  But it still takes like one hundred and ten years of computing time or something like that.
[409.84 --> 412.44]  Like you had to you had to put a lot of machines into it.
[412.68 --> 417.46]  But that number will slowly turn down to, you know, seconds or whatever, I'm sure.
[418.56 --> 418.76]  Yeah.
[419.02 --> 419.20]  Yeah.
[419.96 --> 423.30]  So, you know, if you're future proofing, you know, don't use shot one.
[423.30 --> 426.62]  Or or past proof.
[426.72 --> 429.30]  If you're just proofing at all, don't use shot one.
[430.04 --> 430.46]  Yeah.
[430.54 --> 434.84]  There's shot two fifty six, which is essentially exactly the same with much higher entropy.
[435.48 --> 437.02]  So just use that instead.
[437.72 --> 437.86]  Yeah.
[437.94 --> 442.12]  I've actually become a big fan of multi hash.
[442.48 --> 443.50]  Have you ever heard about this?
[444.66 --> 444.84]  No.
[445.14 --> 445.78]  OK, nobody has.
[445.78 --> 449.64]  So one has been been pushing this really hard for quite a while.
[450.14 --> 451.84]  He is one of the people behind IPFS.
[451.84 --> 455.56]  So lots of kind of distributed peer to peer crypto stuff.
[456.12 --> 460.20]  And he's really wanted to kind of future proof everything that he's been working on.
[460.30 --> 463.74]  So he started this little open source project called multi formats.
[463.74 --> 474.24]  And what these are is essentially, you know, every time that you've got to sit down and use a codec or you've got to use like a particular encryption algorithm or a hashing function like this.
[474.24 --> 484.50]  Let's just create a format that allows you to define which format you're using so that libraries can just, you know, optionally support a bunch of different formats.
[484.70 --> 487.54]  And if in the future you want to change formats, you don't break all of your clients.
[487.66 --> 487.96]  Essentially.
[488.70 --> 496.66]  It's like very similar to MKV or MOV, but all the container things for video codecs, I suppose.
[496.66 --> 497.06]  Right.
[498.18 --> 498.32]  Right.
[498.54 --> 501.96]  Although containers oddly actually do implement a bunch of features.
[503.00 --> 503.14]  Sure.
[503.52 --> 506.32]  This gets really ugly, actually, in codecs and containers.
[507.88 --> 519.78]  But yeah, I mean, so they're like for multi hash, for instance, there's libraries and pretty much every language ever, including a very well maintained JavaScript implementation that works, you know, in the in the browser and in Node.
[519.78 --> 522.68]  So that's that's what I've used in a couple of projects recently.
[522.88 --> 527.76]  But Lenis, the funny thing is that Lenis is actually like still just not convinced.
[528.58 --> 538.66]  So he's basically said that, you know, well, the way that Git uses it is still not prone to these attacks because, you know, they have the length of the body and that makes the this harder.
[539.78 --> 542.42]  So, you know, we'll see how that ends up.
[543.20 --> 545.22]  I mean, it does make it a lot harder for what it's worth.
[545.28 --> 545.66]  It does.
[545.66 --> 548.44]  It does make that it does make the attack a lot harder.
[548.62 --> 557.98]  But like I do feel like he rather than future proofing or moving to like just a better algorithm, he's just kind of dangling out this like, oh, prove me wrong.
[558.24 --> 559.08]  Computer science.
[559.84 --> 560.02]  Yeah.
[562.30 --> 567.44]  Which which like didn't work out that well for, you know, his last round of this.
[567.86 --> 568.08]  Right.
[568.08 --> 568.16]  Yeah.
[568.64 --> 568.80]  Yeah.
[568.86 --> 573.26]  It seems silly to be like, well, you only half broke it.
[573.32 --> 580.58]  So I'm going to like if you got through a half of my lock, I'm going to go ahead and just change out the whole thing.
[581.16 --> 581.52]  Yeah.
[582.00 --> 586.36]  Rather than just like, no, I'm going to start just, you know, continuing to put these half locks on things.
[586.36 --> 586.76]  Yeah.
[589.08 --> 589.44]  Yeah.
[589.56 --> 597.70]  But this kind of reminds me that like the way that we think about security on the web tends to be like, oh, I put Cloud Slayer in front of it.
[597.80 --> 598.94]  So I'm secure now.
[599.84 --> 602.64]  You know, like I added SSL or added TLS or something.
[602.74 --> 603.52]  So I'm secure now.
[603.52 --> 612.26]  But really, security is like this really multilayered thing where when you when you break off one layer of the onion, you need the other layers around it to still be secure.
[612.42 --> 612.58]  Right.
[613.60 --> 613.96]  Yeah.
[614.08 --> 617.08]  I think you almost can't even break off any of the layers.
[617.08 --> 620.56]  I mean, yeah, security is really, really hard.
[620.68 --> 626.14]  It's just it is it needs to be there at every layer.
[626.64 --> 628.94]  Otherwise, the other ones just have no effect.
[629.10 --> 630.08]  You know, right.
[630.52 --> 630.74]  Right.
[631.14 --> 638.40]  Like you're it's I think an onion is a poor metaphor, I guess I'm saying the chain or whatever is much better.
[638.52 --> 641.28]  Like if you have a single weak link, then it doesn't matter.
[641.38 --> 642.44]  You can get you can get through.
[642.78 --> 643.18]  Yeah.
[643.38 --> 651.08]  I mean, if you look at like some of the stuff that people have been doing with auth for a while, you know, OAuth jumps through all of these hoops to basically do an extra layer of encryption.
[652.32 --> 657.02]  And initially they kind of did that so that you could do OAuth over HTTP without TLS.
[657.02 --> 663.00]  But when but like even when you added TLS to it, it's really nice to keep all that encryption there.
[663.28 --> 666.04]  And one of the things that OAuth 2 did was it just kind of got rid of that and was like, oh, whatever.
[666.10 --> 666.84]  We're using TLS.
[667.62 --> 669.86]  But like, you know, you can break TLS.
[670.22 --> 675.68]  We know that certain authorities have been compromised for TLS so people can give out bad certs like that.
[675.86 --> 678.62]  That's not a very good way to secure everything.
[678.62 --> 679.60]  Well, sure.
[680.04 --> 686.04]  I mean, if you operate under the assumption that TLS is broken, though, then the entire Internet's broken already.
[686.44 --> 692.30]  So it's like the auth channel, if you had that extra encryption, would be broken.
[692.42 --> 696.32]  But then as soon as you got to that website and used it, you'd be screwed anyways if TLS is broken.
[696.64 --> 700.38]  So I don't think it'd be any more broken than it would already be, I guess.
[700.38 --> 702.92]  So you're screwed if that if that's the case.
[703.68 --> 705.00]  No matter what.
[705.42 --> 710.56]  Maybe someone doesn't get your authentication credentials, but hopefully you haven't reused those anywhere else.
[710.84 --> 710.86]  So.
[712.88 --> 713.54]  All right.
[713.58 --> 716.40]  Well, I mean, do we have anything else to say about hashing algorithms?
[717.90 --> 721.18]  This is this is a pretty deep topic to start a JavaScript show with.
[721.30 --> 721.62]  Yeah, sure.
[721.62 --> 723.60]  You know, interesting choice.
[723.60 --> 735.92]  So like somebody that doesn't know anything about this kind of stuff, a.k.a. me or someone else that doesn't necessarily have to deal with the security side of the code that they write.
[736.26 --> 740.22]  What would be like the best thing for them to like?
[740.22 --> 752.20]  What would be the best resource for somebody that wants to know, like how to actually authenticate stuff in a secure way that I don't know, wouldn't anger Linus or Linus, whoever you say his name?
[752.20 --> 755.24]  I don't know if I'm answering your question directly.
[755.62 --> 763.98]  But if you're building a website and you want to make sure your website is secure, Mozilla Observatory is a really good option for like it will scan your website.
[764.10 --> 767.60]  It'll check your TLS certs, which is some of this is involved there.
[767.76 --> 774.00]  And then it'll it'll check content security policy, a bunch of different things.
[774.02 --> 777.90]  It'll kind of give you a prioritized list of things to do.
[777.90 --> 787.18]  So I would absolutely recommend like putting any website you build through Mozilla Observatory to kind of get that checklist of and score and things like that.
[787.74 --> 788.38]  Cool. That's awesome.
[788.48 --> 790.08]  I didn't even know about that site.
[790.20 --> 790.98]  So that is helpful.
[790.98 --> 797.92]  I think also like maybe we can call out a couple good like application layer authentication schemes as well.
[798.88 --> 808.52]  I mean, this is one of the problems with, you know, get not updating and getting rid of this is that, you know, people take their best practices from their common tools and and, you know, not using a secure hashing.
[808.68 --> 810.52]  It's just not sending a very good message.
[810.52 --> 814.66]  But I'd like to see, you know, like, Alex, you work for a bank extensively.
[815.34 --> 817.80]  You know, what authentication scheme are you using over there?
[817.80 --> 825.36]  But for I guess for which this is a seems like a very broad question.
[825.80 --> 828.28]  Like what how do we off our employees?
[828.40 --> 828.94]  How do we off?
[829.74 --> 830.88]  How do you off like customers?
[830.88 --> 837.84]  Like, do you do you actually, you know, encrypt or hash different pieces of, you know, the stripe thing?
[837.92 --> 838.88]  I hope you do.
[839.66 --> 842.62]  I hope my credit card number is not just like sitting there.
[842.62 --> 843.14]  Yeah.
[843.38 --> 850.90]  So PCI determines all of the algorithms for how you must store credit card numbers and things like that.
[851.00 --> 864.48]  So I would probably I have a pretty good guess on what it is, but I'm not even credentialed enough to touch or look at any of that code as an early employee at Stripe.
[864.48 --> 869.34]  So I think that's another one of the security precautions that PCI mandates.
[869.60 --> 872.50]  But yeah, it is.
[872.56 --> 874.46]  It is mandated by a body.
[874.76 --> 892.40]  But but as far as just like all of this off goes, I feel like maybe my security brain is coming out a little bit like the way that your password gets hacked is not hashing algorithm collisions currently.
[892.40 --> 894.16]  Um, this one's bad.
[894.28 --> 896.20]  I don't think too many people are using SHA-1.
[896.40 --> 898.70]  Even if you use like HMAC with SHA-1, it's fine.
[898.78 --> 898.92]  Right.
[899.00 --> 904.30]  Like, like there's even ways to to make SHA-1 fine.
[904.42 --> 908.42]  But like use Bcrypt to do passwords.
[908.84 --> 909.98]  Actually, don't.
[910.66 --> 916.66]  My number one recommendation is don't implement any security stuff yourself.
[916.94 --> 919.80]  Use libraries that are well known and well tested.
[919.80 --> 924.82]  Um, like the number one rule at Stripe is don't implement your own crypto.
[925.00 --> 928.94]  Don't don't invent your own crypto because you have not thought it through correctly.
[929.66 --> 932.54]  Um, so that that's my advice.
[933.56 --> 934.40]  Yeah, agreed.
[934.64 --> 938.18]  I tend to rely on people, modules written by smarter people than me.
[938.30 --> 939.72]  Um, right.
[939.80 --> 948.20]  Like the the wide use of something signals far more security than like a smart person to write.
[948.20 --> 954.02]  Like someone can be smart and have a glaring hole that they singularly forgot because there's only one set of eyes on it.
[954.12 --> 962.16]  Uh, but like you can be pretty sure like the rails off stuff works pretty well because every side of the internet would be down if it didn't.
[962.26 --> 964.32]  Unless Linus Torvalds is maintaining that library.
[964.72 --> 965.28]  Then sure, sure, sure.
[965.28 --> 968.54]  But at least it's well known, right?
[968.62 --> 968.94]  Like that.
[969.06 --> 972.12]  Like no one's, uh, no one's being quiet about it.
[972.84 --> 972.98]  Yeah.
[973.32 --> 973.56]  Yeah.
[973.88 --> 983.38]  I've, I've actually been using sodium encryption and signing, uh, for quite a while, which is, I don't know who came up with the standard, but, um, Matthias Boos and the node community has gotten really into it.
[983.42 --> 986.32]  And so there's really good libraries that work both in the browser end and node.
[986.32 --> 990.68]  Um, and it's a really, you know, good, consistent, easy way to do signing in crypto.
[991.32 --> 1003.36]  I, I, the stuff that I've seen, um, from previous jobs that I was at where we did a lot of node stuff, um, it was more like built into CI tests.
[1003.36 --> 1014.36]  So when it would check, uh, to make sure all the tests pass, it would also check for like known vulnerabilities, uh, and maybe like certain NPM packages or the way that like node was written.
[1014.36 --> 1023.52]  So it, would that be separate to other things that people would want to integrate into their like regular behavior?
[1023.52 --> 1028.02]  Or is that just another like good level of authentication?
[1028.02 --> 1038.88]  I mean, it's a good practice to, um, so SNK, S-N-Y-K, um, has a service that you can kind of plug your open source module into, I believe for free.
[1038.88 --> 1047.38]  And then, you know, on your GitHub PRs and stuff like that, um, it'll check if you have any vulnerabilities and there's obviously like a proprietary version as well.
[1047.38 --> 1052.04]  But that, you know, looks through your NPM tree and sees if there's any known vulnerabilities.
[1052.72 --> 1055.72]  Um, and in fact, even offers you ways to patch them and stuff like that.
[1055.78 --> 1056.94]  So it's, it's a pretty nice tool.
[1056.94 --> 1063.16]  Um, but that's really just for, for known vulnerabilities, you know, things that we, we've already seen out in the wild.
[1063.16 --> 1065.48]  It doesn't really protect against, it gets bad practices.
[1065.84 --> 1075.24]  Um, and also, you know, you run into this problem, like Alex was saying, you know, if, if nobody's using the module, then nobody's probably going to take the time to find these vulnerabilities early on.
[1075.78 --> 1080.92]  And so, you know, using well, well known, well trafficked modules will really help as well.
[1081.76 --> 1082.26]  All right.
[1082.30 --> 1083.90]  I think we're, I think we're pretty good there.
[1083.90 --> 1086.72]  I think that we're actually coming into a time for a break now.
[1086.94 --> 1090.90]  First sponsor of the show today is our friends at Rollbar.
[1091.06 --> 1093.06]  Put errors in their place with Rollbar.
[1093.32 --> 1095.04]  Easily get set up for your application.
[1095.50 --> 1097.94]  NPM install dash dash save.
[1098.20 --> 1098.64]  Rollbar.
[1098.90 --> 1100.60]  That'll get you set up with Rollbar's notifier.
[1101.10 --> 1102.16]  You also need an account.
[1102.30 --> 1104.84]  So go to rollbar.com slash changelog.
[1105.08 --> 1105.58]  Sign up.
[1105.62 --> 1107.92]  Get the bootstrap plan for free for 90 days.
[1107.92 --> 1110.00]  With Rollbar's full stack error monitoring.
[1110.00 --> 1114.70]  You get the context, the insights, and the control you need to find and fix bugs faster.
[1115.04 --> 1117.10]  No more relying on users to report your errors.
[1117.40 --> 1123.62]  Digging through log files to debug issues or dealing with a million alerts in your inbox ruining your day.
[1123.62 --> 1126.54]  Once again, rollbar.com slash changelog.
[1126.62 --> 1126.94]  Sign up.
[1126.96 --> 1128.94]  Get the bootstrap plan for free for 90 days.
[1129.14 --> 1130.42]  And now back to the show.
[1132.90 --> 1133.58]  All right.
[1134.52 --> 1136.30]  Let's dive into this a little bit.
[1136.46 --> 1140.58]  So a relatively routine new version of Node came out.
[1141.28 --> 1142.30]  7.6.
[1142.46 --> 1144.20]  Like we do these releases all the time.
[1144.20 --> 1151.18]  But this one is a big deal and people are making a big deal out of it because V8 got updated in the background.
[1151.44 --> 1158.92]  They've been doing a lot of work so that we can actually take new versions of V8 in point releases and not break the ABI for everybody.
[1159.04 --> 1159.72]  So that's been great.
[1160.76 --> 1166.24]  But in this release, async slash await came out from under a flag.
[1166.68 --> 1171.32]  So now in a current release of Node, you can do async await.
[1171.32 --> 1178.86]  So I'm curious what y'all think of this and what your views are on it.
[1179.14 --> 1181.22]  Because before I get into my view.
[1182.90 --> 1185.70]  I suppose I don't have a ton of opinions.
[1186.98 --> 1189.56]  I understand the two sides of this.
[1190.18 --> 1200.68]  And I feel like I think the primary, at least the thing people are calling their primary concern is performance of this versus callbacks or promises or whatever.
[1201.32 --> 1207.26]  But I think that's silly because A, it'll get faster, the next version.
[1207.66 --> 1211.30]  And B, it's such a small performance hit that who cares.
[1212.04 --> 1214.46]  It's primarily sugar.
[1214.82 --> 1219.16]  So I guess there are the people who dislike sugar and there are people who like sugar.
[1219.74 --> 1221.40]  And just use whatever you want.
[1221.84 --> 1222.40]  I don't know.
[1222.76 --> 1225.44]  I dislike that this is an issue.
[1225.44 --> 1229.64]  You're just trying to make yourself above the controversy.
[1230.00 --> 1230.32]  Exactly.
[1231.88 --> 1235.52]  Why don't you explain the controversy for us, Michael?
[1236.20 --> 1236.62]  Well, no, no.
[1236.70 --> 1237.66]  I don't think.
[1237.84 --> 1242.80]  Look, there's a long, long argument kind of against promises.
[1243.02 --> 1245.44]  There's just a lot of people that don't like promises.
[1245.44 --> 1251.62]  And in particular, like I actually don't care about promises.
[1252.10 --> 1255.44]  I'm fully in the do whatever you want and don't care camp.
[1255.72 --> 1256.90]  I'm telling your wife.
[1257.38 --> 1264.18]  But it does get annoying that people act like this is like revolutionary.
[1265.58 --> 1271.60]  You know, like a lot of the articles that were written about this feature coming into Node are like, Node finally tackles asynchronous programming.
[1271.60 --> 1276.64]  Like Node 0.02 tackled asynchronous programming.
[1277.12 --> 1279.58]  Like asynchronous programming has been part of Node since day one.
[1279.70 --> 1281.66]  It's been like the hardest thing for people to get over.
[1283.14 --> 1289.38]  And callbacks, for the most part of actually like the standard callback interfaces has kind of wrangled that into something usable and really fast.
[1291.44 --> 1295.48]  And I think promises landed, you know, a while ago in V8.
[1296.38 --> 1297.22]  Native promises.
[1297.22 --> 1301.56]  People have been using promises, though, since, you know, early promise standards.
[1301.90 --> 1304.08]  You know, Bluebird is based on the promise standard, right?
[1304.12 --> 1306.38]  Which is the really fast one that people tend to like.
[1307.00 --> 1313.62]  I feel like people use promises far before it was even standard in V8 or whatever.
[1314.32 --> 1314.84]  Right, right.
[1314.90 --> 1318.04]  And before it was a standard, there were all these competing standards for promises.
[1318.50 --> 1323.22]  So if you go back far enough, you know, you just could not get two people to agree on the same promise.
[1323.22 --> 1327.52]  Well, you couldn't get jQuery to agree with the rest of it.
[1327.72 --> 1332.96]  Like Chris Zippin and promises A, A+, like that was pretty early on, I feel like.
[1333.58 --> 1341.38]  So what Alex is hinting to is this fight in CommonJS over which standard would be the promise standard.
[1341.64 --> 1347.56]  And he said A slash A+, because there was also promises slash B and C and I believe D.
[1347.76 --> 1349.40]  And I don't know how many letters we got up to.
[1349.62 --> 1350.22]  It didn't get into...
[1350.22 --> 1351.02]  No one used those, though.
[1351.12 --> 1351.84]  They were just proposals.
[1351.84 --> 1353.44]  Right, right.
[1354.00 --> 1360.56]  But anyway, I think that Dominic Nicola did a ton of work just to get promised people to agree on the same spec.
[1361.38 --> 1365.46]  Or at least get everybody to stop listening to the people that weren't attracting.
[1366.68 --> 1368.72]  And got like a real standard in the language.
[1368.72 --> 1373.00]  Which a lot of people that don't like promises don't like.
[1373.10 --> 1378.90]  I personally prefer not to wrap this kind of state in an object myself.
[1378.90 --> 1389.46]  But one thing that you can say about it is that the browser, if you look at all browser standards, there's just no standard way to do IO handlers.
[1390.02 --> 1394.34]  There's, you know, if you look at every DOM API that has to do this, they do something slightly different.
[1394.34 --> 1395.66]  And all of them are awful.
[1395.66 --> 1400.64]  And even if you don't like promises, most of what people do in the DOM to do the same thing is just worse than promises.
[1402.34 --> 1403.76]  So, yeah.
[1403.88 --> 1405.90]  So it's nice to have a standard.
[1406.26 --> 1413.26]  And that going forward, you know, if you look at like the fetch API and some of these new browser APIs, you have something unified, which is so good.
[1413.44 --> 1414.92]  Like, I mean, yeah.
[1414.92 --> 1420.24]  To be clear, promises made it into the DOM specification, not ECMA, right?
[1420.84 --> 1423.06]  Well, it's sort of in both, right?
[1423.20 --> 1426.72]  So async await is a feature in the JS language.
[1427.16 --> 1429.46]  And it effectively yields a promise, right?
[1429.84 --> 1430.16]  Right.
[1430.16 --> 1431.80]  And it relies on that standard.
[1432.06 --> 1437.12]  So you're getting into like this annoying territory where we have two standards bodies working on the web platform.
[1437.50 --> 1437.70]  Yeah.
[1437.70 --> 1438.10]  Yeah, yeah, yeah.
[1438.40 --> 1445.40]  But like the promise object doesn't have to exist in Node, I guess, the native promise.
[1445.50 --> 1447.16]  It just kind of does because VA does.
[1448.72 --> 1449.08]  Right.
[1449.22 --> 1451.62]  But there's some really low level hooks.
[1451.62 --> 1455.36]  So now we're going to get into some Node.js details.
[1455.64 --> 1463.22]  But there's a lot of tracing and debugging that you can do in Node.js, especially in production systems, to really get at like the underlying state that's going on.
[1464.10 --> 1467.44]  And there's all kinds of different methods to get at this.
[1467.44 --> 1470.30]  Node.js is one of the more inspectable platforms out there.
[1470.74 --> 1472.82]  So there's different types of tracing that people do.
[1473.06 --> 1478.82]  And there's also this thing called async wrap, which is like an async hook into the low level event system.
[1479.46 --> 1486.48]  And in order to do that, in Node, there's this thing called make callback in C++ land that wraps the callback that happens.
[1486.60 --> 1487.56]  So it's just a little function.
[1488.44 --> 1491.18]  But promises don't have that kind of hook yet.
[1491.42 --> 1493.16]  Native promises don't have the hook yet in V8.
[1493.16 --> 1503.04]  So there's work that needs to be done to get an equivalent thing happening at the native level, which at that point actually will make it much more valuable to use native promises rather than something like Bluebird.
[1503.04 --> 1511.90]  But anyway, so what it all comes down to is that I think that people don't actually like composing all these promises into a bunch of things.
[1511.90 --> 1513.44]  They actually get kind of annoying and messy.
[1513.84 --> 1518.96]  And the end goal has been this async await feature, which essentially allows you to kind of yield out a promise.
[1518.96 --> 1524.48]  So it's a syntactic sugar on top of what people are doing now.
[1524.62 --> 1529.98]  But it is one of those more important pieces of syntactic sugar that makes us far more usable than it used to be.
[1530.16 --> 1530.18]  Right.
[1530.76 --> 1530.96]  Yeah.
[1531.00 --> 1537.64]  It doesn't it doesn't tackle a lot of the core problems people have with promises, namely error eating.
[1538.48 --> 1538.96]  Yeah.
[1539.10 --> 1539.26]  Right.
[1539.76 --> 1540.18]  But yeah.
[1540.18 --> 1547.96]  But I think if you're already using promises, I think await can be a nice update to to your code style.
[1548.14 --> 1551.90]  I think for the most part, it's it's fine.
[1552.02 --> 1552.78]  You don't have to use it.
[1552.80 --> 1554.14]  No one's forcing anyone to use it.
[1554.14 --> 1562.70]  You can almost always write a little wrapper around some dependent library that uses it to switch it back to whatever you like to use fibers or whatever.
[1564.92 --> 1566.08]  Nobody uses fibers.
[1566.34 --> 1566.74]  No, I know.
[1566.86 --> 1569.36]  I intentionally said something that no one uses.
[1569.36 --> 1577.52]  But the I think is a silly argument just because it's it's like it's sugar.
[1577.74 --> 1581.54]  Most of the time performance on it is it's not going to matter material at all.
[1581.84 --> 1584.00]  And you can choose to not use it.
[1584.40 --> 1586.04]  So deal with it.
[1586.68 --> 1588.54]  Yeah, that's that's that's a really good recap.
[1590.60 --> 1591.84]  I wanted more controversy.
[1592.26 --> 1595.18]  Come on, Rachel, come in and tell me how much you know promises real quick.
[1595.26 --> 1596.16]  I can get into it.
[1596.24 --> 1596.96]  I'm just kidding.
[1597.60 --> 1598.56]  That's the thing.
[1598.56 --> 1603.44]  Like now that I don't write a ton of production code, I can do whatever I want.
[1603.68 --> 1608.22]  So nothing makes me angry because if it does, I'll just do it a different way.
[1608.34 --> 1615.84]  So I'm pretty much indifferent about, you know, arguments in regards to like code preferences.
[1615.84 --> 1618.90]  As long as it works, I'm happy with it.
[1619.60 --> 1623.46]  We're not going to have very good arguments on this podcast if everybody's above arguing.
[1623.46 --> 1628.52]  I mean, I'll argue, but not about this.
[1628.52 --> 1629.52]  Yeah.
[1629.52 --> 1630.36]  Yeah.
[1630.36 --> 1630.44]  Yeah.
[1630.44 --> 1630.52]  Yeah.
[1630.52 --> 1637.96]  Uh, the question on our chat in Slack, you can join the changelog Slack and the JS Party
[1637.96 --> 1639.06]  channel.
[1639.06 --> 1644.28]  Uh, Seth Adder asked, is there any argument against a second weight other than performance
[1644.28 --> 1645.86]  and syntax sugar is bad?
[1645.86 --> 1651.84]  Um, eating well against a second weight, maybe not because it's just sugar.
[1651.84 --> 1658.28]  Uh, but there are plenty of more arguments against promises than just, uh, performance,
[1658.28 --> 1664.72]  namely error handling, uh, I think is, is the number one complaint, uh, that whenever you're
[1664.72 --> 1672.48]  inside of, um, promises, oftentimes you're many levels deep inside ends and, and, and stuff
[1672.48 --> 1678.42]  and, uh, errors can get swallowed, uh, you know, in a way that it's very, very hard to
[1678.42 --> 1679.16]  track them down.
[1679.16 --> 1683.20]  Um, and very hard to even get stack traces back out of them when you do catch them.
[1683.20 --> 1688.56]  So you need to be very explicit about every error step along the path.
[1688.78 --> 1693.00]  And if you're not, then things just get swallowed and you don't realize that bad things are happening in your code.
[1693.42 --> 1704.06]  So I think that's it may not be the number one like design flaw with them, but it's certainly the number one like thing people run into whenever they set up a giant promise based system.
[1704.06 --> 1714.02]  Yeah. And I think also like the way that it handles errors kind of conflicts with the way that not just node handles errors, because that wouldn't be accurate.
[1714.12 --> 1724.00]  Node doesn't have like a way to handle errors, but a lot of the debugging facilities and tracing facilities in node rely on errors and exceptions kind of bubbling up to the top.
[1724.70 --> 1729.08]  And so because it's swallowing them, you lose a lot of the state and you can't figure out where you're going.
[1729.08 --> 1733.34]  So a lot of like production node systems have have issues with that particular mode.
[1733.34 --> 1736.50]  And that's that's being worked on. Right. Like this is all really, really early days.
[1736.60 --> 1739.40]  So I think that all of this is going to get better over time.
[1740.30 --> 1744.18]  But people that are, you know, already have a big production system kind of don't like this.
[1744.26 --> 1751.54]  I think there's also a style argument or a way that people like to to write code argument.
[1751.54 --> 1757.82]  And it's the argument. This argument is as old as time, which is just a kind of OO versus functional programming argument.
[1757.82 --> 1765.86]  And essentially promises, you know, wrap up a bunch of state in this object abstraction that you can then stack and compose.
[1766.44 --> 1771.78]  And some people think that that is a bad style of writing code compared to more functional programming style.
[1772.22 --> 1774.30]  And so there's that argument out there as well.
[1774.78 --> 1782.72]  And I think that like people have different brains and different people's brains like these different ways of writing code.
[1782.72 --> 1792.00]  Sure. So so Seth also asked, is there a suggestion for avoiding like the error stuff and some of these other gotchas?
[1792.00 --> 1794.18]  And I don't think there's a great one.
[1794.32 --> 1802.86]  Like there are good like baseline rules for how to not write promises in a way that that accidentally swallow errors.
[1802.86 --> 1810.14]  But in practice, like with some of the most brilliant people, like it still happens almost every time once or twice somewhere.
[1811.68 --> 1815.90]  So there are other mechanisms for asynchronous coding.
[1816.04 --> 1823.18]  So the baseline won't be callbacks, but then you you get to what people hate about callbacks, which is callback hell or whatever.
[1823.56 --> 1831.10]  I'm sure Michael has some things to say about callback hell, but I don't think he can deny that callback hell exists for some people.
[1831.10 --> 1841.26]  But then there are other async mechanisms like async functions are coming in the future, which is a pretty fundamentally different model.
[1841.78 --> 1855.14]  And then generators, if if you know that model or another way to kind of yield control in certain sections and then and then pop back back to those.
[1855.14 --> 1865.84]  Not necessarily used in the same exact ways, but generators and async functions are kind of cool because they make they don't swallow errors in the same way.
[1866.10 --> 1873.16]  And they make programming asynchronously look somewhat synchronous, which is which is pretty cool.
[1873.16 --> 1888.98]  They are also because of that can be very confusing because you don't realize it's very hard to stretch your brain to say like, oh, this one character here, this one keyword caused all this stuff to happen behind the scenes.
[1889.32 --> 1892.66]  And so they can be somewhat difficult to reason about sometimes.
[1893.12 --> 1896.14]  Maybe Michael has more opinions on generators and async functions, though.
[1896.14 --> 1911.74]  Yeah, I mean, I think I think before we go too deep into this, though, I just want to point out that in the browser, there's actually some new features around promises and for error tracking and handling specific promises that I believe actually rely on the native promises.
[1912.74 --> 1919.74]  So for debugging the promises, though, it wouldn't be like your code would still swallow it, but you might be able to see it in your tooling.
[1919.74 --> 1920.70]  Does that make sense?
[1921.08 --> 1921.68]  Right, right, right.
[1921.74 --> 1922.50]  Exactly, exactly.
[1922.96 --> 1933.38]  But honestly, I mean, so the solution to callback hell is to write code that doesn't have callback hell the same way that the way to not swallow errors and promises to write code in a way that doesn't swallow the errors.
[1933.72 --> 1937.58]  Yeah, so it's not necessarily a good solution, but it's viable.
[1938.42 --> 1938.60]  Yeah.
[1939.34 --> 1941.06]  I'll also say just about coroutines.
[1941.26 --> 1948.28]  There's a library called co that is the main thing that people use on the node side to really do a lot of the asynchronous programming using generators.
[1948.28 --> 1957.52]  And it's not in super wide use generally, but it has this huge following in China, really big.
[1959.38 --> 1960.68]  It's actually really interesting.
[1961.00 --> 1972.22]  So there's this dude, Dead Horse, on GitHub, but he took over maintaining some of TJ Holloway Chuck's modules when TJ left.
[1972.60 --> 1973.38]  As we all did.
[1973.94 --> 1975.64]  Quit for Go, you know, as you do.
[1975.64 --> 1983.76]  And but yeah, he took over a lot of the co stuff and Dead Horse is actually like a really well known programmer in China.
[1983.98 --> 1988.34]  He he helps with some of the CNote and CNPM local stuff.
[1988.94 --> 1990.74]  He's actually a great dude.
[1990.84 --> 1991.86]  I met him when I went out to China.
[1991.86 --> 2000.32]  But because he's such a presence there, I think that he has sort of like, you know, by himself kind of propped up the coroutine stuff.
[2000.60 --> 2003.76]  And a lot of the people in a lot of programmers in China are actually using that.
[2003.98 --> 2005.88]  Like there's there's not as big of a promise following there.
[2005.96 --> 2007.42]  And it's much more around the coast stuff.
[2007.48 --> 2008.32]  It's a really interesting.
[2008.80 --> 2014.16]  It's one of the few like divergences in preferences that I know that are actually like geographic.
[2014.42 --> 2015.08]  Geographically based.
[2015.08 --> 2015.60]  Yeah.
[2015.96 --> 2018.38]  I actually only use the async module.
[2020.64 --> 2022.54]  That's kind of not maintained anymore.
[2022.84 --> 2025.86]  Oh, that was not not true.
[2026.00 --> 2028.20]  But back in the day, that was somewhat revolutionary.
[2028.20 --> 2038.04]  Like, I think some of people's love for promises came out of kind of the bridge between promises and callbacks that async was.
[2038.10 --> 2049.44]  It was like this weird middle ground where you didn't have to, you know, count the number of different things that had finished or introduce like multiple layers of callbacks in a row.
[2049.52 --> 2054.38]  You could kind of use the async module to to flatten some of those things.
[2054.38 --> 2063.36]  But it definitely wasn't by any means like a standard or even internally consistent in how it worked.
[2063.46 --> 2068.62]  But it was it was nice from a from a community growth standpoint.
[2068.74 --> 2069.78]  It was a stepping stone.
[2070.78 --> 2072.18]  So, yeah, yeah.
[2072.22 --> 2081.28]  I think like in the server space and in the front end space, if you get popular enough, somebody will make a promise version of your thing and there will be like a following around that.
[2081.28 --> 2082.92]  Like there's definitely a lot for request.
[2083.40 --> 2083.56]  Yeah.
[2083.76 --> 2083.92]  Yeah.
[2084.38 --> 2093.28]  But I'm actually curious, Rachel, if you see this in the hardware space at all, if like there are if there are as much of a problem that's following in node bots and whatnot.
[2094.38 --> 2101.34]  Um, I honestly couldn't tell you because I live in such a siloed thing.
[2101.34 --> 2109.76]  And I mean, most of the well, a lot of the node bot stuff is very single usage thing.
[2109.76 --> 2114.58]  So you'll have like one sensor being controlled by some other input.
[2114.58 --> 2122.30]  So there's not a lot of need for a ton of promises or stuff that you would need to have something special.
[2122.42 --> 2130.02]  You don't you just don't run into the same kind of problems that you run into when you're writing things for the web, which is probably why I like hardware so much.
[2130.02 --> 2132.16]  What about like sequential actions?
[2132.16 --> 2135.38]  Like you want some servo to do this, then this, then this, then this.
[2135.68 --> 2135.88]  Yeah.
[2136.02 --> 2141.72]  So you definitely will you the thing that you run into the most then is when you're like trying to run stuff on serial port.
[2141.72 --> 2159.90]  So when you're getting data from multiple places at once and sometimes, you know, the stuff that you're waiting to happen from your sensor over Wi-Fi isn't going to happen as quickly or in sync as the stuff coming over your serial port cord.
[2160.32 --> 2166.28]  So it is sort of an issue, but not that much.
[2166.34 --> 2168.64]  I at least haven't run into it that often.
[2168.64 --> 2186.52]  And plus, whenever I have to deal with a bunch of really intense, it usually happens whenever you have to rewrite more custom C to handle new kinds of chips and then have the C work with your own like Johnny five stuff on an Arduino or a TESOL.
[2187.00 --> 2189.60]  Yeah, that's it's all like really low level callback stuff.
[2189.66 --> 2189.86]  Right.
[2189.92 --> 2192.96]  So you don't get a lot of like composition at that layer.
[2192.96 --> 2198.94]  I'm trying to think of like anything that I've done recently that has been what I would refer to as callback hell.
[2199.18 --> 2204.68]  And it probably would be like some node application that I utilized graphics magic with.
[2204.92 --> 2211.50]  So I'm actually interested in going in and trying out the new node version with that kind of stuff.
[2211.50 --> 2220.34]  It might I think it might be really helpful, helpful for people that do a lot of procedural art based stuff on the Web, actually.
[2221.68 --> 2225.40]  Yeah, I mean, also, so there's these performance arguments right now.
[2225.48 --> 2231.22]  And honestly, even though I'm not a huge promise advocate, I think most of the performance arguments are really dumb.
[2231.22 --> 2235.78]  But in hardware, it actually makes sense.
[2236.06 --> 2248.36]  So the reason why I think that the performance arguments are stupid is that you're talking about like point zero two milliseconds, I think is like the largest difference between Bluebird and promises and native promises.
[2248.36 --> 2261.30]  And if you're talking to the network or the file system, that's really not a thing like your WebSocket delayed to local host is roughly like a three millisecond round trip time.
[2261.76 --> 2264.46]  So like it's just it's just not ever going to be noticeable.
[2264.46 --> 2267.70]  But with serial port, like you're talking to the hardware there.
[2267.80 --> 2270.32]  I mean, it is asynchronous, but it is really, really fast.
[2270.38 --> 2273.50]  And so you could actually see some of the performance stuff like stack up there.
[2273.84 --> 2275.02]  You might actually like start to care.
[2275.38 --> 2278.30]  I don't care about much, but we'll see.
[2278.36 --> 2286.00]  How fast can I AI this cat photo to blink this?
[2286.00 --> 2290.34]  OK, listen, don't pigeonhole me.
[2290.70 --> 2291.60]  Yes, exactly.
[2292.14 --> 2294.72]  I like I like other animals.
[2296.40 --> 2300.16]  I thought you were going to say I do more than just cat images.
[2301.78 --> 2303.26]  I wish I did.
[2305.58 --> 2306.44]  That's awesome.
[2306.44 --> 2312.16]  You know, I enjoy pigeons and raccoons and other various animals that love garbage.
[2314.56 --> 2317.30]  We should have Isaac on so you guys could discuss.
[2317.86 --> 2320.42]  Oh, I've already discussed raccoons with Isaac.
[2320.76 --> 2321.12]  No, I know.
[2321.18 --> 2324.06]  I just want that to be like a live voice thing.
[2324.42 --> 2327.34]  I don't know if I ever want to have that conversation again.
[2327.34 --> 2329.42]  Yeah, I made the mistake.
[2329.42 --> 2339.12]  For anyone that's wondering, Isaac from NPM, if you ever see them, talk to them about how much they love raccoons.
[2340.26 --> 2340.72]  They don't.
[2340.88 --> 2341.02]  OK.
[2341.02 --> 2346.64]  Oh, and on that note, we're about ready for another break.
[2346.74 --> 2350.58]  And when we come back, we'll talk a little bit about the featured project of the week.
[2350.58 --> 2354.74]  Our friends at Top Tower, longtime supporters of Change Log.
[2354.90 --> 2358.54]  If you've ever had to quickly scale your team, you know how hard it is.
[2358.72 --> 2367.68]  You have to go through all this hassle of writing job descriptions, adding them to your website, or maybe you have to hire somebody just to go out there and find the candidates for you.
[2367.68 --> 2372.32]  That's a lot of work, a ton of work that you don't have to do if you call my friends at Top Tower.
[2372.70 --> 2375.60]  They do all the work for you to find the right candidates for your positions.
[2376.14 --> 2384.04]  Plus, because they have a very rigorous screening process to identify the best, you know you're only getting qualified candidates for your open positions.
[2384.60 --> 2386.42]  Head to TopTile.com to learn more.
[2386.86 --> 2389.24]  That's T-O-P-T-A-L.com.
[2389.58 --> 2391.34]  Tell them Adam from the Change Log sent you.
[2391.76 --> 2396.12]  If you'd like a more personal introduction, email me, Adam at ChangeLog.com.
[2396.12 --> 2397.48]  And now back to the show.
[2397.68 --> 2401.62]  And we are back.
[2402.06 --> 2402.44]  All right.
[2402.66 --> 2406.60]  We're going to get into Feature Project of the Week, ARJS.
[2407.02 --> 2410.54]  Rachel's particularly stoked about this one, so I'm going to let you take this over.
[2410.86 --> 2412.30]  Is it about assault rifles?
[2413.18 --> 2413.62]  No.
[2414.66 --> 2415.00]  No.
[2415.24 --> 2416.30]  That's version 15.
[2417.62 --> 2418.78]  ARJS V15.
[2418.88 --> 2419.06]  Okay.
[2419.06 --> 2429.96]  So ARJS is this really awesome library that you can use now that is augmented reality for the web using ARToolkit.
[2430.58 --> 2434.04]  It's built of a couple other different technologies.
[2434.84 --> 2436.70]  It's using 3.js.
[2436.70 --> 2438.70]  It's using A-Frame from...
[2438.70 --> 2441.18]  Who made A-Frame?
[2441.38 --> 2442.12]  This is horrible.
[2442.30 --> 2443.54]  It's Mozilla's A-Frame.
[2443.54 --> 2444.88]  Which is...
[2444.88 --> 2449.54]  If you haven't messed around with A-Frame, what it does is it allows you to do WebGL VR in the browser.
[2449.54 --> 2464.08]  So you can either view things in the browser with a 3D appearance or if you have, you know, like a Google Cardboard or any other kind of virtual reality headset that phones go into.
[2464.08 --> 2471.10]  It allows you to actually see the 3D object that you have developed in virtual reality with your phone.
[2471.60 --> 2478.58]  And what ARJS does is it blends all of these things together and allows you to use digital markers.
[2479.34 --> 2484.92]  They're using hero markers, which are these squares that have...
[2484.92 --> 2485.52]  Little Greek burritos.
[2485.92 --> 2485.94]  Yeah.
[2486.32 --> 2486.90]  No.
[2489.18 --> 2491.58]  They're like QR codes.
[2491.58 --> 2502.72]  Basically, any kind of digital marker is just using image processing with, like, nearest neighbor type of mathy things.
[2503.24 --> 2505.42]  I'm great at explaining things technically.
[2506.20 --> 2512.92]  So basically, what ARJS does is, unfortunately, if you have an iOS phone, it doesn't work.
[2513.00 --> 2515.28]  So I can't even test it, which bums me out.
[2515.28 --> 2523.94]  But if you have an Android phone, you can set it up so that you have your 3D environment that you've crafted with A-Frame.
[2524.54 --> 2530.90]  And A-Frame is built on top of 3.js because it allows for the 3D objects in the browser.
[2531.60 --> 2539.70]  And then it uses the AR toolkit, which was originally a library in C, and they've made it work with JavaScript.
[2539.70 --> 2544.32]  And it does that nearest neighbor processing of the hero marker.
[2544.92 --> 2551.84]  And it assigns your 3D objects so that when you use your phone in a WebGL-supported browser,
[2551.84 --> 2558.46]  and you point it at the marker either on, like, a computer screen or on a piece of paper that's printed out,
[2558.80 --> 2569.84]  whatever 3D object you've assigned to that marker in your code will appear, like, on the phone or the device that you're viewing it through as a, like, hologram type thing.
[2570.66 --> 2571.88]  It's really cool.
[2573.14 --> 2577.26]  A-Frame is really accessible for people that are just starting out in JavaScript.
[2577.70 --> 2579.34]  Their documentation is amazing.
[2579.34 --> 2585.34]  And pretty much what this AR.js library does is it allows you to take...
[2585.96 --> 2592.48]  They basically took all of the difficult part, the difficult steps out of the equation.
[2592.78 --> 2594.90]  So everything is built together for you.
[2595.00 --> 2596.84]  The documentation on it is pretty good.
[2597.52 --> 2603.34]  It says that it runs at 60 frames per second on a Nexus 6, which is pretty impressive.
[2604.02 --> 2607.88]  And there's a lot of examples of 3.js things that you can do with it.
[2607.88 --> 2619.72]  So I'm excited to see what people make with it because I'm very, very interested in any kind of augmented reality, virtual reality, mixed reality situation that we can do with JavaScript.
[2620.08 --> 2621.10]  It's super exciting.
[2621.90 --> 2622.88]  I'm only going to...
[2623.40 --> 2625.40]  This is only a slight side check.
[2625.54 --> 2627.04]  So it runs at 60 frames a second.
[2627.04 --> 2636.88]  And if you look at the pictures of it, it's like this blob that sits on a piece of paper and you can look around and the blob stays on the piece of paper, which is pretty nifty.
[2637.34 --> 2640.18]  And, like, you can move it and animate it and things like that.
[2640.20 --> 2642.60]  So you can spin it on the piece of paper while you look around.
[2643.06 --> 2644.80]  And, like, that runs at 60 frames a second.
[2644.96 --> 2647.30]  And that's pretty verifiable on a phone.
[2647.30 --> 2658.90]  But, like, I can't get, like, a div to animate from 200 pixels high to 500 pixels high at 60 frames a second.
[2659.06 --> 2664.32]  I can't get my webpage to scroll at 60 frames a second by default half the time.
[2664.88 --> 2666.84]  It's because you're not using WebGL, man.
[2667.56 --> 2667.86]  I know.
[2668.32 --> 2675.50]  I'm just always so amazed at, like, the difference that, like, everybody is almost hitting 60 frames per second.
[2675.50 --> 2678.84]  But, like, the place where we're starting out is always so different.
[2679.76 --> 2682.58]  It always blows my mind when these things work quickly.
[2682.90 --> 2684.04]  That's all I wanted to say.
[2684.50 --> 2689.66]  I mean, obviously, that just means that the future of Web is that it's all going to be holograms.
[2689.66 --> 2690.14]  I'll buy it.
[2690.18 --> 2690.38]  Yeah.
[2691.46 --> 2692.40]  I'm into it.
[2693.12 --> 2696.76]  I actually would be really interested in finding out.
[2696.86 --> 2699.44]  I know that there's a device called the Leap Motion.
[2699.44 --> 2707.24]  It's a USB device that lets you essentially use your hand.
[2707.86 --> 2709.50]  I think it's, like, two cameras.
[2710.18 --> 2713.14]  And so it's essentially scanning the space above the Leap Motion.
[2713.64 --> 2717.38]  And when you put your hand in front of it, you get a 3D model.
[2717.54 --> 2720.96]  It's used a lot with, like, Unity and gaming type stuff like that.
[2720.96 --> 2724.74]  But I know that there is a way to use it with WebGL.
[2725.24 --> 2737.24]  So now I'm curious if I'm able to use a Leap Motion with this augmented reality application to not only be able to view holographic things through a device,
[2737.30 --> 2740.98]  but if I could couple it with another thing and try and move things around.
[2741.34 --> 2746.40]  I'm just, like, thinking of all the, like, really weird and awesome stuff that people can build with this.
[2746.80 --> 2748.44]  This is the stuff that I get excited.
[2748.44 --> 2752.76]  Thanks in advance to Leap Motion for sponsoring the JS Party podcast.
[2752.98 --> 2761.22]  And also thanks to, in advance to the next company I'll give free advertising to, the Mayo armband.
[2761.38 --> 2764.42]  I backed on Kickstarter or something like that a long time ago.
[2764.64 --> 2766.52]  It's not quite positional.
[2766.84 --> 2771.60]  So it might not know exactly where your hand is, but I feel like you could do that with a marker.
[2772.06 --> 2776.58]  But then it essentially can give you data about your exact hand position.
[2776.58 --> 2781.46]  So it's an armband that goes kind of, like, next to your elbow, like, pretty far back.
[2781.68 --> 2789.52]  And it just reads the tensions in, like, your different tendons to know that your hand is, like, doing, like, a motion,
[2789.86 --> 2793.24]  like a pull or a push or a squeeze or anything of those different things.
[2793.80 --> 2795.66]  Yeah, I remember seeing that.
[2795.66 --> 2805.72]  So I've actually given a few talks where you hook up the, like, the next slide and previous slide as just, like, swipes in the air or, like, behind your back.
[2805.82 --> 2809.82]  And then you can, like, start animations or different things like that with squeezes.
[2809.96 --> 2814.30]  And there's a whole set of default things for Keynote and stuff.
[2814.38 --> 2815.16]  It's pretty nifty.
[2815.16 --> 2821.38]  Though I find that sometimes you false positives switch a slide whenever you're gesturing wildly.
[2822.14 --> 2827.46]  But, yeah, that makes it, like, you could just put, like, a marker on your hand to know position.
[2827.64 --> 2829.98]  You know, you get a RFID tattoo.
[2831.14 --> 2833.12]  Or not an RFID, a QR code.
[2833.20 --> 2837.50]  You have the RFID baked into your hand or something, right, Rachel?
[2837.52 --> 2839.96]  Yeah, I have an RFID chip in my hand.
[2840.38 --> 2840.62]  Yeah.
[2840.62 --> 2844.06]  Yeah, that's in solidarity with your pets.
[2844.92 --> 2846.88]  Yeah, that's how much I love cats.
[2847.02 --> 2848.04]  I'm really dedicated.
[2849.14 --> 2851.42]  Yeah, but I think you could do some really cool stuff.
[2851.62 --> 2856.50]  Not just the position of your hand, but, like, the motion of your fingers and stuff like that, too.
[2856.56 --> 2859.50]  Like, picking it up versus pushing it versus all that stuff.
[2859.82 --> 2862.00]  Maybe a leap motion plus a Maya.
[2862.16 --> 2862.94]  You just mix them all together.
[2863.02 --> 2864.18]  Get a drone in there somehow.
[2864.82 --> 2868.34]  Yeah, every single kind of, like, crowdfunded device.
[2868.56 --> 2868.92]  Exactly.
[2868.92 --> 2870.60]  Put them all together and see what you can get.
[2871.48 --> 2872.78]  Yeah, this is a really cool project.
[2873.08 --> 2881.84]  This reminds me of, like, when they first used Emscripten to compile down, like, you know, Doom and, like, these 3D games.
[2882.12 --> 2884.10]  And they were first doing, like, 3D standards in the browser.
[2884.72 --> 2892.96]  And those, like, essentially demos that nobody really ever used were what ended up pushing the web's implementation of WebGL forward and all that.
[2893.00 --> 2897.42]  Yeah, I mean, Brendan toured the conference circuit for, like, three years on those demos.
[2897.42 --> 2899.62]  And he's so bad at playing it, too.
[2899.74 --> 2900.78]  It was so funny.
[2901.06 --> 2911.12]  He eventually, like, after dying so quickly, so fast, so many times in front of 500 people, hacked the parameters of the game to where he can't.
[2911.18 --> 2912.76]  He plays in god mode now.
[2912.76 --> 2916.08]  Are you talking about the Sentry Chicken talk?
[2916.86 --> 2920.22]  Yeah, I mean, the same version of that talk has different games.
[2920.50 --> 2920.94]  But, yeah, yeah.
[2920.94 --> 2944.78]  So, actually, one thing I'd really love to see, one mashup I'd love to see with this, just spitballing here, is some sort of, like, if you use, like, a piece of paper and then you're able to kind of draw shapes and then, you know, press some button on your keyboard and then it, like, AR-ifies it to where you can, like, pick up the shape.
[2944.78 --> 2946.96]  Does that make sense?
[2947.16 --> 2957.82]  Like, essentially, like, the style in, like, the super futuristic movies, I feel like we're almost there to where you can draw something and then manipulate it in 3D space.
[2958.42 --> 2961.12]  Well, there is something that exists like that.
[2961.20 --> 2970.24]  Not in the JavaScript world, but there is an application called Vuforia that allows you to create those kind of, like, augmented experiences where you can interact with things.
[2970.24 --> 2973.70]  So, maybe somebody should do that.
[2974.68 --> 2980.24]  Yeah, I look forward to one of our listeners from this week presenting that on the show next week.
[2980.92 --> 2982.26]  It just takes one week, right?
[2982.82 --> 2983.22]  Yeah.
[2985.46 --> 2991.20]  Yeah, like, so, have y'all done any WebGL programming at all or played around with any of the kind of raw stuff?
[2991.82 --> 2992.82]  Yeah, I have.
[2993.82 --> 2995.12]  I have a bit.
[2995.26 --> 2996.76]  I'm learning A-Frame.
[2996.76 --> 3004.46]  I'm messing around with a bunch of other various 3JS stuff.
[3005.04 --> 3009.60]  And I've done some WebGL video game things.
[3009.96 --> 3013.50]  But this is something that I am super interested in.
[3013.62 --> 3014.20]  I think people are...
[3015.02 --> 3016.60]  Plus, it's, like, happening so fast.
[3016.74 --> 3018.58]  Like, people are making cool stuff with this.
[3018.58 --> 3030.92]  And I find that the people that are actively developing interactive things for, like, WebGL-based art are not, like, software engineers for their day jobs.
[3031.02 --> 3037.56]  They're just, like, multi-faceted technologists and artists that were like, oh, this is cool.
[3037.82 --> 3039.54]  I want to make cool stuff for this.
[3039.68 --> 3040.98]  And that's really awesome.
[3040.98 --> 3044.88]  I haven't done a ton of WebGL stuff.
[3045.70 --> 3049.58]  A little bit for some of the Stripe splash page stuff.
[3049.76 --> 3053.84]  But I have met Mr. Doob, which I feel like is pretty much the same thing.
[3054.34 --> 3054.74]  Okay.
[3054.96 --> 3055.72]  There you go.
[3057.74 --> 3061.76]  I tried to use 3JS and I really couldn't get my head into it.
[3061.76 --> 3066.80]  But it's just one of those libraries that's just so massive that, yeah, I just...
[3066.80 --> 3067.44]  I really couldn't...
[3067.44 --> 3070.62]  Like, I could take a demo and kind of hack it up, but I couldn't really get my head around it.
[3071.04 --> 3072.38]  Let me get this straight.
[3072.58 --> 3079.36]  You'll build an oven to bake your own bread, but you didn't want to do a deep dive into 3JS?
[3079.96 --> 3080.46]  Well, no.
[3080.66 --> 3088.88]  It's because, like, to get at the low-level constructs that I actually want to figure out in order to understand how everything is built, it was just too much code in the way.
[3088.88 --> 3098.28]  So what I eventually ended up finding, though, is Makola Lysenko and Substack live on the Big Island in Hawaii now next to a volcano.
[3098.66 --> 3100.64]  And they hack on this thing called Regal.
[3101.12 --> 3101.56]  Wait.
[3102.58 --> 3104.18]  You kind of skipped over that kind of fact.
[3104.50 --> 3104.80]  Yeah.
[3105.16 --> 3105.34]  Wait.
[3106.24 --> 3108.76]  Substack lives on an island in Hawaii now?
[3109.34 --> 3109.58]  Yeah.
[3109.72 --> 3110.16]  Yeah, yeah.
[3110.22 --> 3118.08]  Substack and Makola and Marina all moved to the Big Island in Hawaii because it's cheap and because coconuts have 1,200 calories in them.
[3118.88 --> 3119.32]  Okay.
[3119.90 --> 3120.26]  Yeah.
[3121.76 --> 3122.68]  It's amazing.
[3122.86 --> 3125.44]  You have to eat the skin in order to get all 1,200, though.
[3125.88 --> 3126.62]  I don't know.
[3127.50 --> 3131.40]  But, no, they're building this thing called Regal, R-E-G-L.
[3131.40 --> 3137.90]  And essentially, it's various kind of Substack small modules philosophy.
[3138.68 --> 3143.56]  And Makola is just like this amazing math dude doing all these kinds of crazy algorithms.
[3143.56 --> 3152.38]  But it essentially gives you WebGL, but then adds a bunch of features and kind of modules, and you can plug in different algorithms and stuff really easily into it.
[3152.38 --> 3164.18]  But the most amazing thing about it is when you get an error in your WebGL code, you actually get line numbers out of the debugger that gives you your line number in your crazy abstract thing from Regal.
[3164.18 --> 3170.86]  So, it's really well put together, and they've done a really amazing job with the tooling and the debugging side of it.
[3171.34 --> 3176.06]  So, I was actually able to build much cooler, kind of quicker things with Regal than I could with 3.js.
[3176.06 --> 3182.40]  Because even though there's far less big demos and stuff with it yet, I did find it easier to just kind of pick up and learn.
[3183.38 --> 3187.18]  Anyway, I think we're nearly good.
[3188.08 --> 3189.30]  We're going to do picks now.
[3189.56 --> 3190.38]  It's time for picks.
[3190.84 --> 3198.56]  I hope you all picked something that you like that you can link to, or you can just pull one of the many things that you've already mentioned in the podcast so far.
[3198.56 --> 3206.78]  I think, yeah, I'll go back and I'll just pick Regal because it's an awesome library.
[3206.96 --> 3212.14]  I think they did a great job, and I love those guys, and I hope they don't die in a volcano eruption.
[3214.54 --> 3218.02]  Oh, and I'll plug bits.coop, B-I-T-S.coop.
[3218.66 --> 3226.88]  Actually, McCullough and Substack do consulting for any kind of 3D programming stuff that you need, or really just any programming that you need.
[3226.88 --> 3228.18]  They're pretty amazing.
[3228.56 --> 3230.18]  And they're available through Bits.coop.
[3230.30 --> 3239.02]  They're trying to do a kind of cooperative, anarcho-socialist style thing for a consulting business.
[3240.00 --> 3241.40]  So check that out.
[3242.48 --> 3249.32]  My pick will be Observatory from Mozilla, which is the security checker that I mentioned before.
[3250.28 --> 3257.84]  So if you have a website and you're interested in finding the security properties of that website and what you might want to do to increase them,
[3257.84 --> 3266.92]  such as get rid of your SHA-1 certs, then check out observatory.mozilla.org.
[3267.66 --> 3275.44]  My pick is actually a talk, and it's Marco Kosaka's talk on how computers read pixels.
[3275.44 --> 3287.68]  It's really, really interesting, and it has great diagrams if you're ever wondering how image processing works, which is a foundation for a ton of augmented and mixed reality stuff with WebGL.
[3287.68 --> 3295.62]  So it kind of helps you understand on a more fundamental level what is happening when you're looking at these kind of AR markers.
[3296.30 --> 3296.60]  Oh, man.
[3296.66 --> 3298.30]  Maria Kosaka's talks are always so good.
[3298.30 --> 3307.54]  She really dives into these concepts that everybody kind of takes for granted and really learns them and explains them in a really, really amazing way.
[3307.54 --> 3317.12]  I've told her that I really appreciate how she doesn't just explain how something's working so that it's accessible to everyone,
[3317.12 --> 3328.64]  but she also tells the journey of what led her to want to even do that in the first place and the struggles that she had while making it and then the successes.
[3328.64 --> 3330.94]  Those are my favorite kinds of talks.
[3331.04 --> 3340.86]  I'm going to try for the picks maybe every other week between maybe a library that's cool or a project that's cool and then other talks that I think are really great.
[3341.88 --> 3344.06]  And, of course, you can find links to all this stuff in the show notes.
[3344.60 --> 3345.62]  That's it for this week.
[3345.70 --> 3347.16]  We'll, of course, be back next week.
[3348.56 --> 3353.26]  Rate us on iTunes because that's a thing that people say at the end of podcasts, so you should probably do that.
[3353.74 --> 3354.02]  Subscribe.
[3354.18 --> 3354.52]  Be nice.
[3355.34 --> 3355.74]  Subscribe.
[3355.74 --> 3356.82]  Yeah, be nice.
[3356.82 --> 3360.88]  And, yeah, check us out at jsparty.fm.
[3362.04 --> 3364.70]  That's it for this episode of JSParty.
[3364.78 --> 3367.06]  Tune in live on Fridays at 3 p.m.
[3367.08 --> 3370.28]  U.S. Eastern at changelaw.com slash live.
[3370.60 --> 3371.50]  Follow us on Twitter.
[3371.62 --> 3373.56]  We're at jsparty.fm.
[3373.88 --> 3376.82]  Join the community and Slack with us in real time during the show.
[3377.08 --> 3378.68]  Head to changelaw.com slash community.
[3379.12 --> 3382.10]  Special thanks to our sponsors, Rollbar and TopTile.
[3382.10 --> 3387.68]  Also, thanks to our bandwidth partner, Fastly.com and BrakeMasterCylinder for the awesome beats.
[3388.08 --> 3388.96]  We'll see you next week.
[3389.32 --> 3389.98]  Thanks for listening.
[3389.98 --> 3419.96]  We'll be right back.
