[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[15.46 --> 20.08]  This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.20 --> 24.82]  And we're excited to share they now offer dedicated virtual droplets.
[24.82 --> 28.76]  And unlike standard droplets, which use shared virtual CPU threads,
[28.76 --> 32.60]  their two performance plans, general purpose and CPU optimized,
[33.14 --> 35.82]  they have dedicated virtual CPU threads.
[36.14 --> 40.60]  This translates to higher performance and increased consistency during CPU intensive processes.
[41.10 --> 44.94]  So if you have build boxes, CICD, video encoding, machine learning, ad serving,
[45.24 --> 49.72]  game servers, databases, batch processing, data mining, application servers,
[49.94 --> 54.66]  or active front end web servers that need to be full duty CPU all day every day,
[54.88 --> 57.66]  then check out DigitalOcean's dedicated virtual CPU droplets.
[57.66 --> 61.00]  Pricing is very competitive starting at $40 a month.
[61.28 --> 61.62]  Learn more.
[61.70 --> 65.30]  Get started for free with a $50 credit at do.co slash Changelog.
[65.52 --> 68.62]  Again, do.co slash Changelog.
[68.62 --> 81.30]  From Changelog Media, you're listening to the Changelog, a podcast featuring the hackers,
[81.74 --> 84.82]  the leaders, and the innovators of software development.
[85.26 --> 87.66]  I'm Adam Stukowiak, editor-in-chief here at Changelog.
[87.76 --> 92.32]  On today's show, we're at the expo hall floor of OzCon, talking with Ron Evans.
[92.32 --> 95.76]  We're talking with Ron about Go and how it's eating the world of software.
[95.76 --> 100.82]  Specifically, we talk about TinyGo and what they're doing to bring the Go programming language
[100.82 --> 103.30]  to microcontrollers and modern web browsers.
[103.30 --> 112.90]  It's been more than a five-year mission, actually, to seek out new life and new civilizations.
[114.18 --> 115.76]  I don't know if we're boldly going.
[115.98 --> 117.86]  We're more like creeping up timidly.
[117.96 --> 119.18]  You're getting close to boldness.
[119.90 --> 120.16]  Yeah.
[120.32 --> 121.04]  You're getting more bold.
[121.10 --> 124.00]  You come out from underneath your bunker.
[124.00 --> 128.34]  Yeah, this is my first time out in a while from the workshop.
[128.34 --> 138.52]  I have, I ensconced myself after Embedded World in March in Nuremberg, Germany.
[139.02 --> 140.64]  Great conference for Embedded.
[141.06 --> 143.92]  That was the first public appearance of GopherBot.
[143.92 --> 148.48]  And so I went around the whole conference with GopherBot.
[148.88 --> 156.48]  And it's amazing how a conference full of blinking LEDs and robots and stuff will literally stop in its tracks
[156.48 --> 159.90]  when they see a cute robotic gopher plushie.
[160.52 --> 162.26]  So it was a pretty big hit, huh?
[162.78 --> 165.44]  It really was, surprisingly.
[166.36 --> 168.94]  I mean, I thought it was cool, but I thought it was weird.
[169.24 --> 169.48]  Yeah.
[169.48 --> 173.70]  It's like an attention-getting device, you know, but in the form of a robot.
[173.70 --> 177.22]  I didn't even realize my battery died, but these things get so much attention.
[178.00 --> 179.48]  And they're just marquees.
[180.32 --> 181.98]  That's got to be even more so.
[182.56 --> 185.34]  Well, also, this is actually very programmable.
[186.20 --> 188.54]  So all the software is also open source.
[189.30 --> 191.38]  I just put the GitHub repo public.
[191.92 --> 196.34]  So it has all the tiny Go code, which is fairly high level.
[196.34 --> 205.62]  I mean, we were trying to create an API that people who are not really Go programmers could still decipher and use to program this device.
[207.02 --> 210.72]  You know, basically, you know, antenna.blink.
[211.74 --> 216.40]  And so you could say go antenna.blink, and it just launches a Go routine with the blinking antenna.
[216.64 --> 218.82]  And so it just keeps blinking while you do your other things.
[218.90 --> 222.22]  I mean, that's the big benefit of using Go is its concurrency.
[222.22 --> 226.52]  So if your Go is not concurrent, you know, why use Go?
[227.34 --> 231.72]  I mean, it's still nice, but this is a big part of Go's appeal.
[231.72 --> 237.64]  Well, the brevity of the language, the fact that there's very little to it as far as number of keywords.
[237.90 --> 238.14]  Right.
[238.14 --> 248.66]  That's really great when you're writing a compiler because it means there's less things that could go wrong, less misinterpretations, less ways to compile code.
[248.66 --> 256.84]  And, you know, TinyGo has a lot of work to do in order to take the Go SSA code.
[257.00 --> 271.58]  Well, the way TinyGo works, just TinyGo takes your text code, your regular Go, and it uses the Go standard libraries, which themselves are written in Go, to take and convert that to single static assignment form or SSA form.
[271.58 --> 277.30]  So normal Go, at that point, takes the SSA and compiles it to the binary code.
[278.04 --> 287.54]  This is where TinyGo kicks in and says, let's convert that SSA form instead to LLVM's intermediate representation.
[288.46 --> 292.22]  So LLVM is a framework for writing compilers.
[292.22 --> 292.56]  Yeah.
[292.80 --> 304.42]  It's being used by a few languages people might have heard of, like Swift or another little language that is getting a lot of attention called Rust and a bunch of other cool languages.
[304.56 --> 309.60]  A new one called Zig, which looks pretty interesting for WebAssembly and many other languages in TinyGo as well.
[309.60 --> 331.46]  So we take and we can then target whatever one of the LLVM backends, of which there are many, of which many of them are very, very small chips, microcontrollers, like the ARM Cortex-M0 or M4, which are types of chips that Go could never run on.
[331.46 --> 335.96]  They only have maybe 256K of memory total.
[336.72 --> 340.22]  And the Go program is, hello world, is 1.1 megabyte.
[340.56 --> 349.30]  So there's a gigantic disconnect about what you could even fit on the chip, let alone that it's not designed for that processor architecture.
[349.76 --> 352.42]  And there's no operating system on most microcontrollers.
[352.50 --> 353.42]  They just run bare metal.
[353.78 --> 353.92]  Right.
[353.92 --> 364.12]  So there was literally no possible way Go could run in this environment until my colleague I.K. Van Laten, he's actually the creator of TinyGo.
[364.48 --> 365.62]  I'm like the first follower.
[366.52 --> 368.70]  Never mind those 10K lines of code I wrote.
[368.94 --> 370.44]  You know, I'm a good follower.
[370.88 --> 371.82]  I'm a good follower.
[371.82 --> 374.76]  But he's the creator of TinyGo originally.
[375.38 --> 384.76]  And I discovered it through, I don't even remember, it may have been through Golang Weekly or just somehow it popped up through the internets into my attention.
[385.36 --> 388.90]  I took one look and I got very excited.
[389.54 --> 391.34]  I mean, I've been wanting to do this for five years.
[391.76 --> 393.52]  I could never convince anyone to help me.
[393.98 --> 399.16]  And here, this single individual had already done substantial amount of the heavy lifting.
[399.16 --> 404.34]  So we have a team of four official members.
[404.92 --> 408.56]  We have 25 other contributors, I believe now.
[409.76 --> 413.42]  But I.K. handles the compiler heavy lifting.
[414.12 --> 417.68]  I'm sort of responsible for the hardware peripheral interfaces.
[418.38 --> 420.18]  And I'm spokesmodel for the group.
[420.78 --> 426.56]  So I do a lot of the talks and promotion and just generally, you know, yell for attention.
[426.56 --> 433.74]  Then, uh, Johan Brandhurst does a lot of amazing work with TinyGo and WebAssembly.
[434.70 --> 441.60]  Uh, Justin Clift is also doing amazing work, even though he's not an official member of the organization yet.
[442.04 --> 446.40]  If you're listening to this, I just haven't gotten around to send you an email because I know you've been busy.
[446.40 --> 456.88]  And then, uh, Conejo Ninja, a.k.a. Daniel Esteban, who's also Spanish, who has basically been doing all of the amazing work with all of the displays.
[457.88 --> 463.76]  So, and then we have a lot of other contributors who have been, I mean, we have over 200 people on our Slack channel now.
[464.04 --> 466.64]  You know, it's sort of taking off by leaps and bounds.
[466.64 --> 472.30]  And that really segued nicely to the big announcements we made yesterday here at OSCON.
[473.00 --> 475.98]  So we had big, three huge things that came out yesterday.
[476.56 --> 480.00]  We thought OSCON was a great place for us to launch these things.
[480.18 --> 485.74]  Just sort of, it's the center of, of the legitimate open source world, if you will, in the U.S.
[486.20 --> 489.20]  So the first one is TinyGo powered by Arduino.
[489.86 --> 493.32]  So we've been developing a very special relationship with Arduino.
[493.80 --> 495.62]  I mean, they're the pioneers of open source hardware.
[495.62 --> 498.00]  They're a really cool company.
[498.70 --> 501.10]  You know, Arduino is love, they say, and they really mean it.
[501.18 --> 502.74]  I mean, they've been incredibly helpful to us.
[503.24 --> 507.74]  So we have TinyGo running on the new Arduino Nano 33 IoT chip.
[508.20 --> 516.20]  So that particular board is really interesting because it has both a microcontroller as well as a separate Wi-Fi chip.
[516.88 --> 520.04]  So it's really geared up for the Internet of Things.
[520.34 --> 522.08]  If you don't have Internet, it's just a thing.
[522.28 --> 523.64]  It's not an Internet of Things.
[523.94 --> 524.70]  Just things, yes.
[524.70 --> 526.84]  Internet thing, something like that.
[527.04 --> 527.22]  Right.
[527.22 --> 533.94]  So people ask, oh, so that means you can run the net package on TinyGo?
[534.24 --> 535.34]  No, not yet.
[535.96 --> 550.22]  However, since all of the net package is implemented in the form of interfaces, we can implement our own version of those interfaces designed specifically to communicate with the serial interface with this Wi-Fi chip.
[550.22 --> 553.36]  So it's the same code.
[553.36 --> 554.36]  So you just say, you know, we can do that.
[554.36 --> 564.70]  So we can do, you know, we can do, you know, net.dial.tcp.
[564.70 --> 572.06]  your net.dial. We support both TCP and UDP connections. And because of this, we were able
[572.06 --> 581.02]  to implement the same interfaces as the PAHO MQTT client. That's the official MQTT client
[581.02 --> 586.34]  from the Eclipse Foundation, which is used whenever you want to talk to an MQTT machine
[586.34 --> 591.96]  to machine messaging broker from Go. So it's the same interface. So you take your regular Go code
[591.96 --> 596.54]  that you've been using on your embedded Linux, and you copy and paste it into your new code
[596.54 --> 601.48]  that you're writing for your microcontroller, change a few things based on your authentication,
[602.02 --> 609.38]  and it just works. So it's a secure connection from your chip, from your Arduino Nano 33 IoT chip,
[609.54 --> 615.28]  to your secure messaging broker and whatever cloud service you're using. That is table stakes for the
[615.28 --> 620.74]  Internet of Things. If you don't have that, you're not ready. So that was sort of our, here we are.
[620.74 --> 622.86]  You're ready for IoT. We're ready for our close-up, Mr. DeMille.
[624.28 --> 632.64]  So the other two announcements were the future, the future's future. So the second one is the
[632.64 --> 638.00]  TinyGo Playground. Okay. So the TinyGo Playground is like the Go Playground. It's a website.
[638.44 --> 646.20]  You can find it at play.tinygo.org. And if you look at it, it looks very much like the Go Playground.
[646.20 --> 652.44]  It's a web page that you can enter in the left pane, your Go code. And in the right pane, you see the
[652.44 --> 662.00]  console output. But it's using TinyGo. The interesting part is we also support using our hardware boards
[662.00 --> 667.88]  emulated, simulated within this web browser. So you write your TinyGo code on the left pane,
[668.30 --> 673.94]  and it actually is compiling to WebAssembly, which is then executing against the simulator in the browser
[673.94 --> 679.68]  itself. So when you see the little JavaScript LEDs blinking, it's because your WebAssembly code is
[679.68 --> 682.44]  talking to this simulator in the browser to make them blink.
[683.12 --> 683.60]  That's cool.
[683.60 --> 690.28]  And you can click on the Flash button, and it downloads the hex file that you can flash right onto the real hardware.
[690.44 --> 692.72]  It's the actual binary for your code.
[693.22 --> 693.58]  Wow.
[693.90 --> 694.46]  That's cool.
[694.78 --> 701.24]  So then the third thing, which is related to the second thing. So a lot of people have been getting very excited about
[701.24 --> 707.40]  RISC-V. So for anyone who hasn't heard about RISC-V or doesn't know what it is, just because in the
[707.40 --> 715.08]  flurry of buzzwords that I tend to pontificate, it's hard to keep track of the acronyms, especially when
[715.08 --> 723.04]  there's like four-letter acronym plus a number. So RISC-V does for processors what open source software
[723.04 --> 730.00]  has done for the rest of the open source world. It actually provides open source instruction set
[730.00 --> 737.56]  and hardware reference platforms. So if you want to build a processor, you don't have to ask Intel,
[737.96 --> 744.96]  please build a processor that you'll sell me, or go to ARM and say, please let me license this for a lot
[744.96 --> 750.28]  of money so I can build them. Those are both really good options, and they've worked quite well. But
[750.28 --> 757.46]  there's a new third option, which is very exciting to me because we're really at the first steps of a
[757.46 --> 764.42]  Cambrian explosion of unique silicon that does very efficient things for processing deep learning
[764.42 --> 771.50]  models or other types of parallel processing where doing some silicon optimization can result in a
[771.50 --> 780.90]  substantially better amount of computation per watt. So the reason why I care about that
[780.90 --> 787.92]  is for two reasons. The first one is battery life. You know, if we're talking about edge devices,
[788.94 --> 793.48]  you know, we need to save on batteries. And the other one is we need to start using so much
[793.48 --> 798.90]  electricity in the world. Like we need to reduce our power consumption just so that we can preserve
[798.90 --> 806.18]  resources. Right? Like the external costs of burning carbon for a data center are not measured in your
[806.18 --> 815.48]  cost. I saw Searles the other day. He posted one of his provocative tweets, as he tends to do, great guy.
[816.14 --> 823.02]  It was, has anyone done a calculation of the carbon cost of your continuous integration servers? And like
[823.02 --> 829.68]  dead silence on the internet's like, oh, you just pulled the covers back. And you know, we don't like how we look
[829.68 --> 835.90]  right now. Don't answer that question. Right. You know, I think about that a lot, just because I think,
[836.50 --> 840.82]  you know, you can't leave the lights on all the time where I come from. The electrical bills are a lot
[840.82 --> 847.54]  more expensive. Anyway, RISC-V is a really important new technology. And we just announced experimental
[847.54 --> 855.16]  support for RISC-V in TinyGo. So you can compile for the Sci-5 is one of the companies that's
[855.16 --> 862.10]  manufacturing silicon based on this. They have a reference board called the High-5-1 that it's
[862.10 --> 867.06]  super hard to come by because the crowdfunding just finished and you didn't order from that. You
[867.06 --> 872.06]  have to wait for their first production run, I think. But it's actually a microcontroller board
[872.06 --> 873.58]  based on RISC-V. Okay.
[874.04 --> 880.36]  So we have experimental support in TinyGo for this board. And it's also in the TinyGo
[880.36 --> 885.82]  Playground. So if you go to the TinyGo Playground and you click on the dropdown to choose the High-5-1,
[886.30 --> 890.56]  it's simulating that. And if you click on the flash button, you download the hex file with the
[890.56 --> 895.54]  RISC-V code, you can flash on your board. So it's basically next year's demonstration,
[895.80 --> 901.08]  but it's today and it's all in our public repos right now. You're welcome.
[902.22 --> 903.42]  Thank you very much, Ron.
[903.60 --> 907.56]  We haven't left the lab that much over the last few months. We've been kind of busy.
[907.56 --> 912.90]  You're saying this the first you've really gotten out and you've been in the cave working
[912.90 --> 914.56]  hard. For how long now?
[915.72 --> 922.42]  The last conference I went to was in March. And well, it's not just me. I mean, there's a lot
[922.42 --> 926.04]  of contributors, you know, all the members I mentioned and a bunch of other contributors
[926.04 --> 931.78]  as well. You know, this is very much a collective effort. There's no way any one person can do
[931.78 --> 937.22]  anything really important. You know, it's a room full of geniuses. And I'm just really excited
[937.22 --> 943.52]  to be a part of the jam session. That's my, I have my role. I do my part. You know, I try,
[943.66 --> 949.64]  I try. But yeah, it's very much a collective effort and it's been growing by leaps and bounds.
[950.26 --> 954.86]  The number of people that want to do WebAssembly is fairly substantial.
[954.86 --> 955.30]  Really?
[955.30 --> 962.08]  And it's a very exciting new technology. But the ways to actually go about doing it right
[962.08 --> 968.90]  now are very, very difficult. You know, you can write C++ code and then compile it using
[968.90 --> 974.34]  something like mScripten. You know, if you already know C++, that's, you know, perfect, I guess,
[974.34 --> 981.60]  for you. You can use Rust. A lot of people are learning Rust and discovering it's a very hard
[981.60 --> 986.90]  language to learn and to use. You know, it does a lot of things for you, but, you know, it's
[986.90 --> 991.30]  non-trivial. You're not going to just knock off a quick little WebAssembly app in Rust without
[991.30 --> 995.38]  knowing what you're doing. Like, you actually have to learn the language to use it. True with many
[995.38 --> 1003.76]  languages, right? You can only fake your way around so far. So Go, the main Go implementation,
[1004.54 --> 1008.98]  the MGI, if you will, you can compile to WebAssembly.
[1009.12 --> 1009.56]  The MGI.
[1009.92 --> 1016.96]  And there's a couple of issues. One of them is that the actual executable file is quite large.
[1017.52 --> 1018.08]  How large?
[1018.08 --> 1024.70]  Just because Go is big. You know, I mean, hello world and Go. This is how I open my talk.
[1024.70 --> 1033.36]  Hello world and Go is about 1.1 megabytes. And hello world and tiny Go is 12K.
[1034.92 --> 1035.34]  Yeah.
[1035.70 --> 1036.30]  And what do they say?
[1036.30 --> 1038.52]  1.1 megabytes versus 12K.
[1038.66 --> 1040.36]  Does the crowd erupt in cheer?
[1040.52 --> 1042.40]  At this point, people are, like, stunned.
[1042.88 --> 1043.46]  There's silence.
[1043.82 --> 1051.30]  They're not really sure, like, does he speak English properly? Is he dyslexic? Both of those
[1051.30 --> 1053.66]  things. But I did not make an error in that number.
[1053.66 --> 1060.84]  It is two orders of magnitude smaller in terms of size of executable. In fact, it was a really
[1060.84 --> 1068.26]  great blog post written by not one of our team members, but a very cool collaborator. I'm sorry,
[1068.32 --> 1074.52]  I forgot this person's name. But the title of the blog post was, using Go for WebAssembly,
[1074.52 --> 1081.80]  and then compressing it down to a 16K file using TinyGo. Like, he had me at that point, a 16K file
[1081.80 --> 1083.58]  using TinyGo. I'm, like, in awe.
[1083.98 --> 1084.28]  Right.
[1084.28 --> 1092.56]  But they were able to, using our code that's on the public internets, take an application that they had
[1092.56 --> 1099.34]  written using WebAssembly, compile it down to this ridiculously small size. Well, it gets better.
[1099.94 --> 1107.12]  It actually gets better. So someone else then did some WebGL experiments. I think it was Justin
[1107.12 --> 1115.24]  Clift. And using the WebGL interface from the JavaScript bridge from WebAssembly, they discovered
[1115.24 --> 1124.78]  that TinyGo is actually 80% faster than the main Go implementation as well. Probably because we're
[1124.78 --> 1133.64]  using the LLVM compiler tool chain and, you know, between Clang and LDD, which is the LLVM linker,
[1134.20 --> 1138.64]  you know, it's getting rid of a lot of stuff. I mean, it's an unfair comparison just because,
[1138.74 --> 1142.04]  you know, we're a speedboat and they're a battleship. Of course we're going to win,
[1142.58 --> 1148.28]  if you want a cigarette boat race and you, you know, an oil tanker is not the way you win.
[1148.52 --> 1148.98]  Or a canoe.
[1149.50 --> 1153.58]  Or a canoe. You need a boat with a motor. You know, a good motor.
[1153.58 --> 1156.08]  Okay. Canoes have no motors. Not often the least.
[1156.14 --> 1160.20]  Canoes good for stealth, but not really for speed. I did a lot of canoeing as a kid in
[1160.20 --> 1164.60]  Wisconsin. Of course. It's also good for relaxation and enjoyment.
[1164.92 --> 1167.02]  Some would say that. Some would say. At least one.
[1167.28 --> 1171.58]  It's good for relaxation, like the first few miles. And then it's like, my arms hurt.
[1171.58 --> 1174.56]  Your arms are on fire. How many more miles downriver? 15?
[1174.92 --> 1176.80]  All right. Got it. Can we stop here?
[1177.70 --> 1180.00]  This is my last summer canoeing with my son.
[1180.10 --> 1182.08]  If you have a good enough current, you don't have to work that hard, right?
[1182.08 --> 1186.04]  You do if you ever want to get there in time for the water.
[1186.16 --> 1188.64]  Okay. Well, I didn't know we had scheduled events.
[1188.64 --> 1207.24]  This episode is brought to you by GoCD. With native integrations for Kubernetes and a helm chart to
[1207.24 --> 1213.20]  quickly get started, GoCD is an easy choice for cloud native teams. With GoCD running on Kubernetes,
[1213.20 --> 1219.16]  you define your build workflow and let GoCD provision and scale build infrastructure on the fly for you.
[1219.58 --> 1225.92]  GoCD installs as a Kubernetes native application, which allows for ease of operations, easily upgrade
[1225.92 --> 1231.72]  and maintain GoCD using helm, scale your build infrastructure elastically with a new elastic agent
[1231.72 --> 1235.00]  that uses Kubernetes conventions to dynamically scale GoCD agents.
[1235.48 --> 1241.20]  GoCD also has first class integration with Docker registries, easily compose, track,
[1241.20 --> 1246.62]  and visualize deployments on Kubernetes. Learn more and get started at GoCD.org slash Kubernetes.
[1247.12 --> 1249.28]  Again, GoCD.org slash Kubernetes.
[1249.28 --> 1255.20]  GoCD.org slash Kubernetes.
[1255.20 --> 1257.20]  GoCD.org slash Kubernetes.
[1257.20 --> 1259.20]  GoCD.org slash Kubernetes.
[1259.20 --> 1261.20]  GoCD.org slash Kubernetes.
[1261.20 --> 1263.20]  GoCD.org slash Kubernetes.
[1263.20 --> 1266.70]  So, you had next year's demo today.
[1267.62 --> 1272.18]  Dream with us a little bit. I think you're pretty good looking down a few years and dreaming, Ron.
[1272.76 --> 1278.08]  Five years from now, whatever the time frame you pick, let's just assume TinyGo does all the things
[1278.08 --> 1283.36]  that it's set out to do in terms of IoT and whatever you think is success.
[1283.36 --> 1290.86]  Like, what's happened five years from now or three, whatever makes sense, in the TinyGo world or in the embedded space or in IoT?
[1292.16 --> 1295.26]  What does success look like if it just continues apace?
[1296.66 --> 1303.40]  Well, I think it was Chris Dixon who said, no, no, it was Mark Anderson who said software is eating the world.
[1303.86 --> 1304.12]  Yeah.
[1304.12 --> 1307.08]  And so, I'll add to that.
[1307.36 --> 1310.90]  So, if software is eating the world, then Go is eating the world of software.
[1312.20 --> 1316.32]  You know, there was a blog post that came out saying Go was the new Java.
[1316.32 --> 1329.86]  What they meant by that was Go is the industrial strength technology that large mission-critical organizations can rely upon to, you know, keep service levels up,
[1330.00 --> 1336.54]  try not to kill anybody by accident, by failing at the wrong times, you know, for things that really, really matter.
[1336.80 --> 1337.04]  Yeah.
[1337.04 --> 1342.58]  You know, I think a lot of people tend to poo-poo Java, and that's a real mistake.
[1343.20 --> 1348.72]  You know, the JVM is either the number one or the number two most engineered piece of software in human history.
[1349.46 --> 1352.90]  You know, the other one being Beam, the Erlang VM.
[1353.94 --> 1362.20]  So, I mean, you really have to give incredible respect to the number of human hours devoted to taking seriously making this piece of software.
[1362.20 --> 1362.84]  Yeah.
[1362.98 --> 1372.36]  So, to say that Go is even in this very small, refined circle of reliability, to me, is extraordinary.
[1373.32 --> 1377.06]  You know, I mean, I've worked, I did a lot of work for AT&T a number of years ago.
[1377.78 --> 1379.24]  And, you know, carrier grade.
[1379.90 --> 1382.28]  Carrier grade is what is above enterprise grade.
[1383.26 --> 1383.44]  Right?
[1383.54 --> 1385.00]  Enterprise grade, yeah, that's nice.
[1385.12 --> 1386.70]  You know, that's like for consumer products.
[1386.84 --> 1390.64]  Carrier grade, that's like for maintaining the infrastructure of our entire continent.
[1390.86 --> 1391.18]  Right.
[1391.18 --> 1391.24]  Right.
[1391.24 --> 1391.84]  Right.
[1392.02 --> 1399.02]  So, the fact that we can say that Go is in this circle, very small circle, is very exciting.
[1399.54 --> 1411.54]  So, big companies would like, or small companies, any company, you want to reduce the number of programming languages you have in use just to reduce the cognitive friction of your ability to maintain all these systems.
[1412.12 --> 1416.08]  I mean, any interesting system, the half-life is going to be like five years long.
[1416.20 --> 1416.44]  Yeah.
[1416.44 --> 1424.72]  Especially when physical plants, you know, you install something at a physical plant in a factory or a retail store and you say, yeah, it has to be replaced in three years.
[1425.14 --> 1427.12]  You go back there in 10 years, it's still there working.
[1428.06 --> 1429.14]  Like, oh, yeah, it was still working.
[1429.20 --> 1429.86]  We didn't fix it.
[1429.90 --> 1430.72]  We didn't replace it.
[1430.72 --> 1433.34]  You know, and they're like, oh, we said it only had a three-year lifespan.
[1433.54 --> 1434.42]  Like, oh, wow, really?
[1434.70 --> 1435.36]  We didn't know.
[1435.38 --> 1435.96]  It's still working.
[1436.42 --> 1436.82]  Right.
[1436.86 --> 1442.70]  This is just very common in these type of physical locations because, you know, replacement is not easy.
[1442.88 --> 1444.86]  Really, software upgrades are even hard enough.
[1444.86 --> 1453.76]  So, say we need something that's going to be reliable enough and solid enough and Go as a language is making the cut.
[1454.18 --> 1461.72]  The problem is Go as a runtime has certain assumptions about the environments in which it runs.
[1461.86 --> 1463.62]  You know, embedded Linux Go is pretty great.
[1464.26 --> 1469.08]  But we're talking about systems even smaller that requires substantial reliability.
[1469.08 --> 1470.84]  You know, it's your braking system.
[1471.04 --> 1472.92]  You know, it's the airbag system.
[1473.08 --> 1477.70]  It's the system that controls the thermal rods in your nuclear power plants.
[1478.24 --> 1482.92]  You know, these are mission-critical applications where there are many microcontrollers in use.
[1483.58 --> 1487.64]  And, you know, no one ever got fired for using C for an embedded system.
[1488.06 --> 1492.04]  But why aren't we using C for all our mission-critical web systems?
[1492.26 --> 1497.10]  Well, we know why because it's very, very hard to use C in a safe way.
[1497.28 --> 1497.50]  Yeah.
[1497.50 --> 1501.72]  So, you know, all the cool kids, they're not just trying to be cool and new.
[1501.88 --> 1508.76]  They're saying, hey, maybe we could use a language that prevents us from doing things that are very bad ideas.
[1509.14 --> 1511.34]  You know, that's what Rust does.
[1511.52 --> 1511.64]  Yeah.
[1512.32 --> 1515.68]  But Rust puts all of the onus on the programmer.
[1516.14 --> 1518.04]  It's like the opposite of Ruby, right?
[1518.04 --> 1526.62]  Where Ruby says, we will forgive you your small errors and then try to do the best we can to interpret your meaning.
[1526.88 --> 1527.16]  Right.
[1527.16 --> 1528.44]  Rust just says no.
[1529.10 --> 1529.58]  Failure.
[1530.04 --> 1532.98]  And tries to give you some meaningful error messages if it can.
[1533.06 --> 1536.22]  But if you don't know what any of it means, then that's not helpful.
[1536.96 --> 1538.72]  You know, Go also will not compile.
[1539.72 --> 1540.16]  Right.
[1540.26 --> 1545.50]  It's still got a certain rigor of requiring, you know, like phumpt.
[1546.26 --> 1549.84]  You know, Go phumpt says, here's how Go code should be formatted.
[1549.84 --> 1555.88]  You know, and for the rebel hippie programmer, they're like, whoa, man, you know, like don't quash my creativity.
[1556.66 --> 1561.14]  You know, for the corporate coder, you're like, what idiot wrote this code?
[1561.46 --> 1562.46]  It was you, sir.
[1562.72 --> 1563.12]  It was you, sir.
[1563.12 --> 1564.18]  There's no way it was me.
[1564.90 --> 1565.74]  Get blame.
[1565.86 --> 1568.78]  Oh, well, somebody obviously modified the Git logs.
[1569.24 --> 1572.74]  You know, like that could never have been me.
[1572.74 --> 1576.64]  You know, so there's something to be said for a certain amount of discipline.
[1577.54 --> 1579.20]  You know, discipline leads to freedom.
[1579.76 --> 1586.08]  Like if you're disciplined about going to the gym, then you'll have the freedom to maybe eat some pizza because, you know, you've already worked out.
[1586.36 --> 1586.48]  Right.
[1587.08 --> 1592.36]  So in five years, I think Go will be much bigger than it is.
[1592.50 --> 1599.12]  I think all of these organizations will realize they need to do edge computing, not just cloud computing.
[1599.94 --> 1604.26]  And TinyGo will have completely conquered the world of the ultra small.
[1604.26 --> 1608.54]  I like to think that is what's going to happen.
[1608.90 --> 1611.52]  That's what happens if we all work together to make it happen.
[1612.54 --> 1617.32]  An alternate history would be that something else fills the needs that TinyGo is filling.
[1617.42 --> 1618.72]  Is there other projects?
[1618.90 --> 1619.92]  Is there competition?
[1620.50 --> 1621.26]  And that's...
[1622.44 --> 1624.52]  I like to think of it as more cooperative.
[1624.80 --> 1625.08]  Sure.
[1625.66 --> 1626.24]  But just alternatives.
[1626.24 --> 1630.72]  I mean, it's competition only in the sense of like you can only eat at one restaurant tonight.
[1631.14 --> 1631.42]  Right.
[1631.60 --> 1631.84]  Right.
[1631.84 --> 1636.92]  So is it the competition between the Szechuan place and the Thai place?
[1637.06 --> 1640.28]  Only in the sense that you're going to eat at one tonight and another tomorrow night.
[1640.30 --> 1640.96]  In the micro sense.
[1641.18 --> 1642.82]  But in the big picture, you can like both places.
[1643.46 --> 1645.38]  Big picture, you can like both restaurants.
[1646.00 --> 1652.46]  Well, and also, I mean, every programming language exists because it does something well.
[1652.46 --> 1661.40]  Like, I really just like when people are talking badly about some other programming language without having really used it.
[1661.76 --> 1663.84]  Because every single language does something well.
[1663.98 --> 1665.00]  That's what it was created for.
[1665.08 --> 1670.56]  Now, you maybe are using it for the wrong thing or the thing that it does well is not something you care about doing.
[1670.56 --> 1672.66]  You know, I'll give you a great example.
[1672.88 --> 1674.28]  This language called Fortran.
[1675.46 --> 1677.06]  A very ancient language.
[1677.32 --> 1677.64]  Never heard of it.
[1677.68 --> 1678.66]  Used for mathematics.
[1679.84 --> 1685.64]  Still being used by NASA in order to figure out the orbits of things in outer space.
[1686.60 --> 1687.08]  Fortran.
[1687.66 --> 1689.82]  You know, if you want to work at NASA, you should learn Fortran.
[1690.54 --> 1690.74]  Right.
[1690.74 --> 1692.06]  What does Fortran do well?
[1692.30 --> 1693.56]  Fortran does mathematics.
[1693.82 --> 1695.12]  It stands for formula translator.
[1695.92 --> 1702.30]  And it's probably the one of the, besides COBOL, it's one of the oldest languages still being used actively today.
[1702.46 --> 1706.54]  Because it does this thing really, really well of mathematical calculations.
[1706.54 --> 1719.54]  So it's worth learning Fortran if you really, really care about mathematical accuracy and being able to do substantial amount of processing quickly.
[1719.54 --> 1725.88]  You know, because doing these, you know, orbital plan calculations is quite difficult.
[1726.24 --> 1730.60]  You know, so every language does something really well.
[1731.36 --> 1732.84]  That's why it was created.
[1733.44 --> 1733.54]  Okay.
[1733.72 --> 1737.04]  But everybody wants to use their preferred language for everything.
[1737.34 --> 1737.98]  True.
[1738.20 --> 1739.14]  That's hard to do.
[1740.00 --> 1746.76]  So I think that there are other languages that are approaching the space of the extremely small.
[1746.94 --> 1747.18]  Yeah.
[1747.18 --> 1748.82]  You know, again, Rust.
[1749.52 --> 1752.10]  There's interesting things happening with Elixir.
[1753.18 --> 1756.26]  You know, people trying, people running Beam on microcontrollers.
[1756.26 --> 1756.56]  Yep.
[1756.72 --> 1758.52]  You know, that to me is extremely interesting.
[1758.52 --> 1765.10]  You know, C++ is not your father's C++ now.
[1765.28 --> 1778.12]  It has absorbed a lot of interesting syntax from dynamic languages like the auto keyword, you know, and defer things that are very, very interesting in dynamic languages being applied to static languages.
[1778.52 --> 1778.56]  Yeah.
[1778.56 --> 1782.70]  So, I mean, I think there's a lot of action, you know, happening in the small space.
[1782.70 --> 1787.70]  But, and a lot of us are running on top of LLVM.
[1787.70 --> 1799.18]  So, when we run into a problem, like most programmers, we assume it's our code and then only gradually come to the sinking realization that it's in the thing we're using.
[1799.18 --> 1805.52]  And we have to either figure out how to fix that or provide a coherent bug report so that the maintainers can do so.
[1805.52 --> 1824.02]  Well, I've had the magnificently wonderful experience over the last months of running into a problem, figuring that perhaps it's LLVM, going to the LLVM mailing list and discovering that a week ago, somebody on the Rust Embedded team reported this.
[1824.50 --> 1828.64]  Or a week ago, someone on the Zig team reported this other thing.
[1829.06 --> 1832.68]  Or in their case, going and finding that a week ago, our team reported it.
[1832.68 --> 1833.08]  Yeah.
[1833.08 --> 1840.32]  You know, so it's a really great collaborative effort on the, I mean, I consider open source the shared infrastructure of the 21st century.
[1840.72 --> 1841.82]  You know, the roads and bridges.
[1842.22 --> 1842.56]  Right.
[1842.62 --> 1847.40]  Of how we all perform our necessary daily functions of life and commerce.
[1847.92 --> 1851.46]  And so, we're just trying to do our part within that.
[1852.24 --> 1854.18]  You know, there doesn't have to be a single winner.
[1854.54 --> 1854.82]  No.
[1855.24 --> 1855.48]  Right.
[1855.48 --> 1855.66]  Right.
[1855.66 --> 1857.70]  In fact, we lose by that kind of monoculture.
[1857.70 --> 1865.28]  Because, you know, any given technology platform or group needs a foil to bounce off of.
[1865.34 --> 1865.60]  Oh, okay.
[1865.72 --> 1872.66]  If nothing else, to just, you know, to, you know, healthy competition is a kind of sportspersonship.
[1872.66 --> 1875.74]  It means we operate from a place of respect.
[1876.62 --> 1884.02]  And when the match is over, we celebrate the fact that we were able to compete together and then we go on.
[1884.16 --> 1884.46]  Right.
[1884.62 --> 1884.82]  Right.
[1885.22 --> 1887.62]  But open source is nothing like that at all.
[1887.72 --> 1888.84]  There is no winner and loser.
[1889.48 --> 1895.94]  You know, it's more like a, I like to call our hack sessions that we have at GopherCon and other places jam sessions.
[1895.94 --> 1898.84]  Because it's like a musical jam session.
[1899.12 --> 1899.98]  There's no winner.
[1900.50 --> 1900.54]  Right.
[1900.64 --> 1901.82]  There's no loser.
[1902.30 --> 1903.84]  You don't even have to participate.
[1904.00 --> 1906.16]  You could just show up and go, wow, this is really cool.
[1906.24 --> 1906.76]  Look what they're doing.
[1906.92 --> 1907.32]  Enjoy the music.
[1907.50 --> 1909.00]  Or you could jam as well.
[1909.12 --> 1909.64]  You can riff.
[1909.76 --> 1912.30]  You know, you win just by participating.
[1912.82 --> 1919.10]  I think it was Albert King, the late, great blues guitarist, said there's only three reasons to play music.
[1919.80 --> 1923.86]  You know, have fun, make some money, or learn something.
[1923.86 --> 1927.32]  So if you're playing music for some other reason, you should stop.
[1927.44 --> 1933.96]  You know, if you're trying to impress somebody or, you know, gun slinging, look good, make them feel bad, you should just stop and go home.
[1933.98 --> 1935.48]  Because that's not a good reason to do it.
[1935.84 --> 1941.38]  So I try to take that same sensibility and apply it to the things we're doing in open source.
[1941.76 --> 1946.96]  And so, you know, the winners are all of us if we collaborate and cooperate.
[1947.52 --> 1950.82]  The losers are all of us if we don't invite people.
[1950.82 --> 1953.66]  I mean, I'll go back to the musical thing.
[1954.78 --> 1963.70]  There have been plenty of cases where a person is sort of shyly standing on the side of a musical jam session that I've been at.
[1964.40 --> 1966.90]  And they don't, they're not participating.
[1967.68 --> 1968.60]  But they're there.
[1969.14 --> 1972.02]  And there's like a glint in their eye that they really want to.
[1972.02 --> 1976.12]  So if you do it well, you pull them up to a mic.
[1976.72 --> 1983.34]  And then this person who doesn't look anything out of the ordinary opens their mouth and your jaw drops to the ground.
[1983.34 --> 1992.60]  Because this voice comes out and you're like, wow, thank you for getting past whatever it was and singing for us.
[1992.60 --> 1995.60]  Because I'm just in awe at how great this is.
[1996.28 --> 1999.16]  And, you know, I think this is a great lesson for inclusion in tech.
[1999.76 --> 2005.36]  Like there's people with a great voice who are just like, they're not going to sing unless you almost make them sing.
[2005.74 --> 2006.14]  Right?
[2006.22 --> 2014.64]  So if it's sort of intimidating, they're definitely not going to, they're going to like stand on the side and like, well, this person's come to three jam sessions and never sung or play guitar.
[2014.76 --> 2015.48]  I wonder why.
[2015.88 --> 2017.36]  Let's see what we can get them.
[2017.36 --> 2026.76]  And, you know, many cases, they've got incredible hidden talents that if we could just allow them to flourish by giving them an opportunity.
[2027.14 --> 2028.42]  And it doesn't have to be forever.
[2028.52 --> 2029.32]  It's just one song.
[2029.76 --> 2031.02]  Then someone else steps up.
[2031.50 --> 2033.14]  You know, that's about sharing the space.
[2033.38 --> 2038.62]  So I try to apply these same principles because, you know, we think tech is about utility.
[2039.08 --> 2039.84]  It's not.
[2040.38 --> 2041.64]  Tech is about aesthetics.
[2042.44 --> 2042.62]  Okay?
[2042.82 --> 2045.86]  If tech was about utility, we'd all use one programming language.
[2045.86 --> 2047.42]  It's about aesthetics.
[2047.62 --> 2050.76]  Like I prefer fuchsia and you prefer green.
[2051.16 --> 2051.44]  Why?
[2051.60 --> 2052.84]  No actual reason.
[2053.38 --> 2053.48]  Yeah.
[2053.68 --> 2053.84]  Right?
[2053.90 --> 2056.30]  We don't have free will, my friend, the neuroscientist says.
[2056.50 --> 2057.24]  What do you mean?
[2057.86 --> 2059.48]  We only think we have free will.
[2059.70 --> 2059.86]  Here.
[2060.14 --> 2063.62]  This is my same friend who said I needed sleep when I didn't need sleep.
[2063.72 --> 2067.34]  He's like, okay, I'm going to do, let me prove to you, you actually need sleep.
[2067.40 --> 2069.70]  So I know better than to mess with this scientist.
[2069.90 --> 2070.16]  Okay.
[2070.30 --> 2071.62]  So he proved it to you.
[2072.02 --> 2072.86]  We don't have free will.
[2072.94 --> 2073.30]  All right.
[2073.40 --> 2073.86]  All right.
[2073.86 --> 2074.46]  Go ahead.
[2074.50 --> 2075.28]  Blow my mind.
[2075.86 --> 2080.94]  So basically by doing functional MRI, this is probably something for your brain show,
[2081.00 --> 2081.16]  right?
[2081.64 --> 2088.12]  So by doing functional MRI and some experiments with choosing options and button pushing, they
[2088.12 --> 2093.74]  were able to determine that the choice of pushing the button occurred before the cognitive
[2093.74 --> 2096.20]  part of the brain responsible for the decision making.
[2096.66 --> 2099.18]  That it was just a little tiny bit afterwards.
[2099.18 --> 2106.14]  So the current best interpretation is we make a random choice and then we explain to ourselves
[2106.14 --> 2110.86]  we made a conscious choice in order to maintain a consistent view of reality.
[2111.28 --> 2112.98]  But in fact, we have no free will.
[2113.10 --> 2114.06]  It's all completely random.
[2114.06 --> 2120.90]  Not to ruin your belief in self-determination.
[2121.02 --> 2121.76]  Way to ruin things, Ron.
[2122.98 --> 2128.24]  But so it's about aesthetics and that's what technology is about fashion.
[2128.80 --> 2132.14]  It's about fads as much as it is about utility.
[2132.80 --> 2134.20]  But it's still about utility.
[2134.20 --> 2138.16]  Like you're still going to need a pocket to put your cell phone in, right?
[2138.30 --> 2142.52]  So if you're making pants without pockets, you know, you're not doing a favor to cell
[2142.52 --> 2143.50]  phone users, right?
[2143.78 --> 2146.96]  You're making a purely aesthetic choice with no utility.
[2147.30 --> 2149.10]  That's the difference between art and design.
[2149.62 --> 2155.98]  Art is just to get an emotional response and design is about doing something functional,
[2156.48 --> 2156.66]  right?
[2156.66 --> 2160.54]  Like a glass hammer is beautiful to look at, but it's totally useless if you want to do
[2160.54 --> 2163.18]  some framing, you know, of wood, knocking down nails.
[2163.46 --> 2163.54]  Right.
[2164.74 --> 2165.06]  So...
[2165.06 --> 2166.16]  I'd probably suck at that job.
[2166.40 --> 2168.96]  We think we're purely utility-based, but we're not.
[2169.62 --> 2174.88]  So, you know, Go is aesthetically pleasing to many people.
[2175.38 --> 2181.12]  So if we can bring Go, you know, again, to like a good politician, bring it back around
[2181.12 --> 2181.74]  to my message.
[2181.74 --> 2189.30]  If we can bring Go to the smallest of platforms, then we are helping satisfy people's aesthetic
[2189.30 --> 2195.56]  desire to use Go and at the same time fulfilling the utility that they need to actually perform
[2195.56 --> 2201.50]  an important function that, generally speaking, is not taken very seriously by like, oh, it's
[2201.50 --> 2203.46]  just the sensors, you know, it'll be fine.
[2203.56 --> 2208.66]  It's like, yeah, those are the sensors that say, you know, turn off the heat because, you
[2208.66 --> 2214.06]  know, the people are about to be cooked or, you know, turn off the elevator because it
[2214.06 --> 2217.50]  appears that the automatic braking system of the elevator is not functional.
[2217.70 --> 2220.44]  It might plummet and, you know, hurt people.
[2221.32 --> 2221.48]  Right.
[2222.12 --> 2224.20]  That's a scary story right there, too.
[2225.02 --> 2226.64]  Just to change the world, nothing important.
[2226.64 --> 2226.96]  Got a scary twist.
[2227.20 --> 2228.38]  That's why we started with toys.
[2229.00 --> 2234.82]  Because Chris Dixon, the investor, he said something like, any sufficiently advanced technology
[2234.82 --> 2236.56]  starts out in the form of a toy.
[2236.56 --> 2238.32]  I'm paraphrasing a little bit.
[2238.68 --> 2240.46]  So we started with Tiny Go with a toy.
[2241.12 --> 2245.58]  You know, people said it was a toy language, so I said I'll build a toy with it just because,
[2245.70 --> 2247.72]  you know, I have a great sense of irony.
[2248.82 --> 2250.16]  Like, oh, yeah, it's just a toy.
[2250.22 --> 2250.92]  I'll just build a toy.
[2251.00 --> 2251.80]  Nothing to see here.
[2251.94 --> 2255.78]  You know, anyone who's ever saw the old 80s or 90s movie Small Soldiers.
[2256.04 --> 2256.36]  Right.
[2256.48 --> 2259.26]  You know, we're talking Tina, you know, child's play.
[2259.40 --> 2260.54]  Like, oh, yeah, it's just a toy.
[2260.66 --> 2261.76]  Nothing to be afraid of.
[2261.84 --> 2263.10]  You know, just a toy.
[2263.24 --> 2263.88]  Friendly toys.
[2263.88 --> 2273.56]  This episode is brought to you by Rollbar.
[2273.90 --> 2275.66]  Move fast and fix things.
[2276.00 --> 2278.04]  Resolve errors and minutes and deploy with confidence.
[2278.62 --> 2280.88]  Head to rollbar.com slash changelog.
[2280.96 --> 2281.76]  Request a demo.
[2281.92 --> 2282.78]  Get started today.
[2283.22 --> 2285.44]  It's loved by developers, trusted by enterprises.
[2285.88 --> 2288.46]  And most of all, we use it here at changelog.
[2288.82 --> 2291.46]  Move fast and fix things with Rollbar.
[2291.46 --> 2294.76]  Once again, rollbar.com slash changelog.
[2306.84 --> 2308.36]  A toy and a playground.
[2308.62 --> 2311.00]  So you have play.tinygo.org.
[2311.54 --> 2314.08]  Is tinygo.org the one-stop shop to get involved?
[2314.08 --> 2314.52]  Yes.
[2314.88 --> 2319.00]  We have a documentation website that's pretty good.
[2319.52 --> 2332.82]  There's been some great in-depth pages and also articles written, especially by IK, who, as I mentioned, IK Van Latem is the IKVL on Twitter and GitHub and all that.
[2333.08 --> 2334.66]  He's really the original project founder.
[2334.66 --> 2338.08]  Even though it's more than him, it's all of us now.
[2338.22 --> 2340.26]  But without IK, none of this could exist.
[2340.62 --> 2344.86]  So I always have to thank IK because you made my dream come true.
[2345.00 --> 2346.26]  I wanted to do this for years.
[2346.58 --> 2348.86]  And for me, this is truly a labor of love.
[2349.70 --> 2354.04]  But it also has tremendous value because this is something that needs to be done.
[2354.24 --> 2358.04]  If it didn't really need to exist, I'd probably be working on something else.
[2358.04 --> 2363.06]  Because, I mean, it's fun, but unless it's also important, you know, then it's a hobby.
[2363.70 --> 2363.78]  Yeah.
[2363.92 --> 2364.88]  Whereas, you know, this is a full-time thing.
[2364.88 --> 2365.64]  Let's play that game, then.
[2365.76 --> 2367.92]  If you couldn't do what you're doing now, what would you do?
[2369.02 --> 2375.52]  If for some reason you had to stop doing this mission, what would be another alternative mission that's just, that would be exciting?
[2375.64 --> 2376.80]  Like, the runner-up, let's say.
[2377.38 --> 2381.82]  Well, I think embedded systems and Go is the most exciting thing happening right now.
[2382.58 --> 2385.06]  But there's a lot of other exciting things happening in the world.
[2385.06 --> 2388.58]  And biotechnology, especially in genomics, is really interesting to me.
[2388.84 --> 2389.26]  What do you know about that?
[2389.26 --> 2391.56]  I think there's a huge opportunity for bioinformatics.
[2392.26 --> 2398.06]  You know, that's, bioinformatics and cloud computing hasn't really, it's not a problem that's been solved at all.
[2398.62 --> 2402.26]  You know, and that, material science, I think, is incredibly interesting.
[2403.00 --> 2408.50]  You know, things like shape memory alloys, which are plastic.
[2408.50 --> 2412.54]  They're polymers that have the property which is opposite of normal metals.
[2412.54 --> 2415.34]  It's like normal metals, when you heat them, they expand.
[2415.44 --> 2416.68]  And when you cool them, they contract.
[2417.42 --> 2419.12]  So, SMAs have the opposite.
[2419.32 --> 2420.66]  When you heat them, they expand.
[2421.68 --> 2423.80]  Sorry, when you heat them, they contract.
[2423.86 --> 2425.32]  And when you cool them, they expand.
[2425.76 --> 2430.06]  So, they are very, very strong and can be used for kind of artificial muscles.
[2431.32 --> 2437.54]  You know, new kinds of solar cells, other kinds of conductive materials, flexible electronics.
[2438.42 --> 2441.34]  That's the kind of stuff I'd like to be working on if I wasn't doing what I'm doing now.
[2441.34 --> 2442.02]  Where are you going with this?
[2442.56 --> 2443.44]  Where are you going with this?
[2444.12 --> 2444.62]  Reel it in.
[2444.72 --> 2445.44]  That's cool stuff.
[2445.52 --> 2446.76]  The future is already here.
[2447.00 --> 2447.52]  Oh, boy.
[2447.60 --> 2447.76]  Right?
[2447.84 --> 2450.54]  It's just like William Gibson said, it's just not equally distributed.
[2451.18 --> 2454.70]  What about, like, genome sequencing and stuff like that?
[2454.76 --> 2460.06]  Like, programming our cells and CRISPR and that kind of stuff.
[2460.26 --> 2460.86]  What are your thoughts?
[2460.86 --> 2464.60]  That's really in the bioinformatics and genomics.
[2465.38 --> 2466.76]  I think it's very exciting.
[2467.10 --> 2468.52]  What are the ethical boundaries there?
[2469.58 --> 2476.10]  Well, I think that ethics in technology is an under-touched subject.
[2476.10 --> 2483.82]  My oldest son is a student at the University of Portsmouth in the United Kingdom studying computer science.
[2484.70 --> 2489.06]  And last year when he finished his A-levels, which are the English equivalent of the last year of high school,
[2489.72 --> 2494.12]  they had to take a class in ethics and computer science.
[2494.12 --> 2498.16]  And it was all the IEEE ethics content.
[2499.32 --> 2502.80]  And I was really excited that this was part of the required curriculum.
[2503.50 --> 2506.28]  He, on the other hand, was sort of like, why do we have to study this?
[2506.72 --> 2509.68]  I'm like, aha, son, you have just opened Pandora's box.
[2509.82 --> 2510.82]  Allow me to explain.
[2510.84 --> 2511.82]  Sit down, young man.
[2512.06 --> 2514.48]  Allow me to explain the need for ethics in technology.
[2514.48 --> 2522.40]  So, I think there's a lot of biohacking going on right now that is completely unregulated.
[2522.56 --> 2523.56]  It's been going on for years.
[2524.24 --> 2525.00]  Describe biohacking.
[2525.66 --> 2526.54]  Describe biohacking.
[2526.88 --> 2534.36]  So, biohacking is when you decide to do some genetic engineering on your own
[2534.36 --> 2538.34]  using equipment you bought yourself through eBay or the internets.
[2538.34 --> 2545.34]  So, in 2009, there was a really amazing conference that took place in Canada called Future Ruby.
[2546.26 --> 2548.64]  Future Ruby was really a seminal conference.
[2549.28 --> 2553.56]  One of the speakers was the team of Nitobi, the creators of PhoneGap,
[2553.88 --> 2556.10]  that ended up selling their company to Adobe.
[2557.54 --> 2559.86]  You know, there was a lot of really amazing people at this conference.
[2560.00 --> 2563.46]  I was there with my brother Damon flying Ruby Howard blimps.
[2563.46 --> 2570.62]  And one of the talks was a professor from MIT who gave a workshop the day before on biohacking.
[2571.26 --> 2577.06]  So, what everybody did was they grew phosphorescent algae in a Petri dish.
[2577.56 --> 2578.70]  So, this is 2009.
[2579.18 --> 2582.20]  And he's talking about how you can buy a genome sequencer for, at the time,
[2582.26 --> 2584.34]  I think it was about $5,000 US on eBay.
[2585.36 --> 2590.46]  And needless to say, it has not gotten more expensive or harder to get this kind of equipment.
[2590.46 --> 2596.28]  So, I think that it's one of the big differences.
[2598.00 --> 2601.42]  What was the name of the guy who created the first internet virus?
[2603.30 --> 2605.44]  His dad worked for the NSA.
[2606.66 --> 2608.20]  I don't know. Me either.
[2608.58 --> 2609.72]  It's not Mitnick.
[2610.70 --> 2613.50]  Anyway, it was the first internet worm.
[2614.48 --> 2616.88]  So, it was not created maliciously.
[2616.88 --> 2623.78]  It was created originally because he wanted to map all the IP addresses within this space.
[2624.38 --> 2630.28]  And he wrote this code that would automatically download itself onto any computer and then do the same thing.
[2630.64 --> 2635.24]  Made an error in the code which caused it to escape the subnet.
[2635.92 --> 2638.46]  And it, you know, took down the entire internet at the time.
[2639.08 --> 2640.16]  Got in a bit of trouble.
[2640.28 --> 2644.50]  And if it hadn't been for dads, NSA connections would probably still be in an undisclosed location.
[2644.50 --> 2649.36]  Actually, back in those days, they still hired teenagers who were hackers to work for them as security people.
[2649.74 --> 2649.80]  Yeah.
[2649.92 --> 2650.54]  Not like now.
[2651.50 --> 2656.08]  But take that idea, but apply it to biohacking.
[2656.60 --> 2661.90]  Well-meaning person doesn't think they're doing anything bad in a basement,
[2662.40 --> 2668.82]  not fully understanding the implications of their work, and making an error.
[2669.92 --> 2671.60]  No bad intentions.
[2671.60 --> 2674.30]  I'm ignoring the bad intentions, people.
[2674.84 --> 2679.88]  Just because I think that it's very hard to do anything that works at all in this space yet.
[2680.08 --> 2686.36]  So, the odds of you making a mistake and having something happen are much greater than bad people doing awful things.
[2686.52 --> 2687.82]  But that's also a possibility.
[2689.02 --> 2695.80]  But if all we do is restrict it completely, like, you know, no man's land, you can't go there,
[2695.80 --> 2697.84]  then it's going to be done elsewhere.
[2698.56 --> 2705.52]  It's the same as saying you can't do computing on the internet because you might transfer an internet virus.
[2706.08 --> 2706.14]  Right.
[2706.26 --> 2706.48]  Right?
[2706.80 --> 2714.34]  So, one extreme means we remain in ignorance, and then it's like the demon-haunted world of Carl Sagan.
[2714.62 --> 2717.32]  We don't understand what's going on and it's affecting us.
[2717.32 --> 2723.80]  The other is every human for themselves with no control and no care over the implications,
[2724.08 --> 2730.08]  which I think has been a very common attitude in tech, which is poorly interpreting Grace Hopper's
[2730.08 --> 2732.14]  ask forgiveness, not permission.
[2732.14 --> 2737.38]  So, first of all, many people don't know that Admiral Grace Hopper said that, the attribution.
[2738.02 --> 2745.02]  But also, they don't realize what she was talking about, which was she was a military officer in a large organization.
[2745.70 --> 2751.46]  And if you've ever worked at a company or an organization that operates at that kind of global scale,
[2751.96 --> 2755.52]  it's very, very hard to get permission to do anything because, you know,
[2755.58 --> 2759.32]  you need to go up three or four levels in the hierarchy above your boss to get permission,
[2759.32 --> 2763.92]  especially if there's no, you know, cost to the organization and substantial benefit.
[2764.70 --> 2769.22]  So, ask forgiveness, not permission meant do the right thing within the organization,
[2769.22 --> 2770.76]  whether or not they know it.
[2771.04 --> 2774.02]  That way, you can help the people that you work for,
[2774.42 --> 2779.08]  not move the extrinsic cost to the public domain so that we can profit.
[2779.60 --> 2781.40]  That is not the same thing at all.
[2781.70 --> 2782.00]  No.
[2782.58 --> 2782.90]  That's true.
[2782.90 --> 2785.96]  So, you know, I don't want to pick on any particular company,
[2785.96 --> 2790.68]  but I think we could rattle off a list of companies whose primary business model
[2790.68 --> 2795.32]  is to take public goods and to turn them into private profits.
[2796.00 --> 2800.94]  And, you know, to me, that's sort of antithetical to this whole idea of, you know,
[2801.00 --> 2802.62]  what is technology for?
[2803.60 --> 2805.62]  Well, it's to improve human well-being.
[2806.40 --> 2807.92]  There is no other reason.
[2808.14 --> 2808.48]  Right.
[2808.64 --> 2810.98]  You know, have fun, make some money, or learn something.
[2812.14 --> 2813.54]  It keeps going back to that.
[2813.54 --> 2816.90]  To wrap it around, then, where are the Tiny Go Jam sessions?
[2817.08 --> 2818.16]  Is it the Slack community?
[2818.28 --> 2822.68]  Like, if you wanted to jam with you guys or just be a wallflower
[2822.68 --> 2827.26]  and maybe get talked into coming and singing, is it on GitHub?
[2827.54 --> 2828.36]  Is it in your Slack?
[2828.36 --> 2830.56]  Where does the actual community hang out?
[2831.28 --> 2832.40]  A lot of us are on Slack.
[2833.22 --> 2838.64]  You know, total disclosure, I would have preferred IRQ because I like open source.
[2838.80 --> 2839.36]  Total disclosure.
[2839.36 --> 2843.34]  But it's really hard to use IRC and IRQ.
[2843.52 --> 2847.04]  And these, you know, free node is great, but it requires too much knowledge.
[2847.52 --> 2847.98]  That's right.
[2848.00 --> 2850.12]  And so I kind of gave up that fight.
[2850.84 --> 2852.72]  You know, I can't fight everything all at once.
[2853.44 --> 2856.80]  You know, I was the one saying we should be using Git as a distributed version system
[2856.80 --> 2860.06]  and not as a hub-and-spoke system, but that didn't go anywhere either.
[2860.06 --> 2864.76]  You know, not because of pointing fingers and saying you're bad, but more, you know,
[2864.82 --> 2866.64]  can we have other possible options?
[2866.90 --> 2868.92]  So anyway, we're all on Slack.
[2869.22 --> 2870.52]  There's a lot of people joining.
[2871.14 --> 2875.16]  You know, Slack is certainly a good platform for this because it's relatively easy.
[2875.92 --> 2877.40]  We have a really active community.
[2878.12 --> 2879.18]  There's a bunch of us in Europe.
[2879.66 --> 2882.44]  There's a bunch of people in Asia.
[2882.44 --> 2884.46]  There's a bunch of U.S. people.
[2884.86 --> 2887.92]  So pretty much 24 hours a day there's somebody around to help.
[2889.02 --> 2891.94]  We're really active on our GitHub repositories.
[2892.42 --> 2896.12]  This is why we have a few members of the organization so that we can respond quickly
[2896.12 --> 2898.78]  to people's requests for assistance.
[2899.52 --> 2904.66]  You know, sometimes GitHub issues are support requests and not issues.
[2904.86 --> 2906.46]  But, you know, we're there to help.
[2906.56 --> 2911.04]  I mean, we're trying to, you know, get this technology out there and make it easier for people to use.
[2911.04 --> 2914.94]  So, you know, part of our responsibility as maintainers is to do that.
[2915.60 --> 2918.26]  You know, we've had a few people come into our Slack and say,
[2918.56 --> 2919.80]  why don't you use language X?
[2920.10 --> 2922.52]  Not X, another language that has a single letter.
[2922.92 --> 2925.50]  And we were like, oh, that's a totally cool language.
[2925.70 --> 2928.04]  But, you know, we're not really thinking of moving to that.
[2928.12 --> 2929.46]  No, just we're doing TinyGo.
[2930.14 --> 2931.36]  Cool language, too, though.
[2932.10 --> 2933.18]  Like, nothing wrong with it.
[2933.28 --> 2934.34]  And, you know, it should be done.
[2934.92 --> 2937.00]  I mean, we're not telling people rewrite it in TinyGo either.
[2937.10 --> 2938.40]  We're saying, check out TinyGo.
[2938.48 --> 2939.78]  It's cool and maybe it will help you.
[2939.78 --> 2941.80]  And, you know, if you like Go, you'll like this.
[2942.04 --> 2942.22]  Yeah.
[2942.42 --> 2946.86]  You know, but we're not saying, you know, you need to do this because we're so much better.
[2947.46 --> 2949.44]  I mean, we think it's better or we wouldn't be doing it.
[2949.48 --> 2952.30]  But, like, we don't expect it to be better for everyone all the time.
[2953.58 --> 2954.72]  But, yeah, Slack is great.
[2954.80 --> 2958.32]  Twitter, we're our TinyGo lang on Twitter.
[2958.64 --> 2960.36]  Because there already was a TinyGo.
[2960.36 --> 2965.00]  On GitHub, it's TinyGo-org.
[2965.32 --> 2967.34]  And that's where we have all our repositories.
[2967.46 --> 2969.64]  We have the main TinyGo repo with the compiler.
[2970.18 --> 2976.52]  We have a driver's repository that's got hardware drivers for a bunch of sensors and displays.
[2977.16 --> 2984.30]  We've got the TinyGo playground code, which I think needs an update since we moved to the serverless processing of the compilation jobs.
[2984.30 --> 2990.18]  And, yeah, we're doing WebAssembly, RISC-V, and serverless all in one app.
[2990.60 --> 2992.08]  Like, it's definitely buzzword compliant.
[2992.18 --> 2994.00]  Yeah, that's a bingo right there.
[2994.00 --> 3000.64]  Like, if you don't fund us because we hit all three of those, it's because, you know, you're just not buzzword compliant investors.
[3000.64 --> 3000.92]  That's right.
[3002.44 --> 3003.02]  Cool, Ron.
[3003.06 --> 3004.64]  Well, thanks so much for talking to us today, man.
[3005.04 --> 3006.94]  Hey, thank you so much for having me.
[3007.04 --> 3008.52]  I really appreciate what you guys do.
[3008.90 --> 3010.32]  It's a great podcast.
[3010.66 --> 3013.52]  You have lots of really interesting, wonderful people and me occasionally.
[3014.28 --> 3015.34]  So, thanks a lot.
[3015.42 --> 3017.30]  And check it out, tinygo.org.
[3017.74 --> 3018.06]  Yes.
[3018.42 --> 3018.90]  Thanks, Ron.
[3021.06 --> 3021.64]  All right.
[3021.64 --> 3024.06]  Thank you for tuning in to this episode of the Changelog.
[3024.14 --> 3024.64]  Hey, guess what?
[3024.70 --> 3027.66]  We have discussions on every single episode now.
[3027.80 --> 3031.58]  So, head to changelog.com to discuss this episode.
[3032.02 --> 3041.62]  And if you want to help us grow this show, reach more listeners, and influence more developers, do us a favor and give us a rating or review in iTunes or Apple Podcasts.
[3041.62 --> 3043.68]  If you use Overcast, give us a star.
[3043.82 --> 3045.18]  If you tweet, tweet a link.
[3045.18 --> 3049.18]  If you make lists of your favorite podcasts, include us in it.
[3049.18 --> 3053.24]  Huge thanks to our sponsors, DigitalOcean, GoCD, and Rollbar.
[3053.50 --> 3057.70]  And, of course, thank you to our sponsors, Linode, GoCD, and GetPrime.
[3057.96 --> 3060.56]  Also, thanks to Fastly, our bandwidth partner.
[3060.94 --> 3062.74]  Rollbar, our monitoring service.
[3063.12 --> 3065.48]  And Linode, our cloud server of choice.
[3065.94 --> 3069.54]  This episode is hosted by myself, Adam Stachowiak, and Jared Santo.
[3070.00 --> 3072.78]  And our music is done by Breakmaster Cylinder.
[3072.78 --> 3079.72]  If you want to hear more episodes like this, subscribe to our master feed at changelog.com slash master.
[3079.94 --> 3083.62]  Or go into your podcast app and search for changelog master.
[3083.74 --> 3084.40]  You'll find it.
[3084.62 --> 3085.94]  Thank you for tuning in this week.
[3086.18 --> 3087.04]  We'll see you again soon.
[3096.24 --> 3097.64]  Well, hello there, listeners.
[3097.90 --> 3098.40]  How are you?
[3098.58 --> 3100.34]  This is Adam Stachowiak.
[3100.34 --> 3104.08]  If you haven't heard yet, we're launching a new show called Brain Science.
[3104.34 --> 3106.42]  It's a podcast for the curious.
[3106.54 --> 3107.22]  Are you curious?
[3107.76 --> 3117.78]  Because if so, we're exploring the inner workings of the human brain to understand things like behavior change, habit formation, mental health, and what it means to be human.
[3118.24 --> 3120.08]  It's brain science applied.
[3120.54 --> 3126.64]  Not just how does the brain work, but how do we apply what we know about the brain that can transform our lives.
[3126.64 --> 3131.54]  Learn more about the show and subscribe at changelog.com slash brain science.
[3131.90 --> 3136.80]  Until then, here's a preview of episode one where we talk about the fundamentals of being human.
[3137.26 --> 3139.96]  We're also all designed to be in relationship.
[3140.72 --> 3146.70]  We are fundamentally hardwired to have social groups and this sense of attachment.
[3146.70 --> 3159.42]  And because I'm sort of a geek when it comes to research, what researchers have found is that attachment, which that's what we label how we relate and connect with others.
[3159.82 --> 3168.56]  Attachment is 100% learned, which means our genetics don't actually contribute to how we learn to stay in proximity with other people.
[3168.56 --> 3176.46]  And with that, that we all develop ways to manage the threat of the loss of a relationship.
[3177.10 --> 3181.90]  But nobody gets to opt out of going, I need to be in relationship with others.
[3182.50 --> 3185.94]  I mean, think about it within the context of the prison system.
[3186.12 --> 3192.44]  Like, why is it that the punishment for prisoners when they don't fall in line is isolation?
[3192.94 --> 3193.94]  Yeah, that's true.
[3193.94 --> 3194.22]  Right.
[3194.86 --> 3198.78]  That wouldn't be significant if in some way that doesn't actually harm our brain.
[3199.06 --> 3203.10]  It's almost like we need to have that echo from another human being to let us know that we.
[3203.52 --> 3204.00]  Yeah.
[3204.20 --> 3207.86]  We're there or we're alive or just some sort of feedback loop.
[3207.90 --> 3209.26]  I'm not really sure how to describe that.
[3209.82 --> 3212.74]  Well, it really is this sense of being with, right?
[3212.78 --> 3218.78]  Like, I can't fight battles on my friend's behalf or on my kid's behalf, right?
[3218.78 --> 3228.74]  But the simple fact that I know of what's going on makes a difference because I would contend it's sort of like I help them hold that weight emotionally.
[3229.64 --> 3231.94]  And so that actually leads me into the third thing.
[3232.02 --> 3239.06]  And the third thing that I would say in regards to the fundamentals of being human is that we all struggle.
[3239.20 --> 3240.16]  Oh, yes.
[3240.58 --> 3241.18]  Right?
[3241.74 --> 3242.38]  Big time.
[3242.38 --> 3248.34]  And that, you know, we don't always get to pick the way in which we struggle, but we all struggle.
[3249.04 --> 3253.32]  Well, if you like what you hear, you should go to changelog.com slash brainscience.
[3253.42 --> 3256.00]  The show is not out yet, so don't get too excited.
[3256.30 --> 3261.00]  But you can subscribe and be notified as soon as the show launches.
[3261.56 --> 3264.50]  Once again, changelog.com slash brainscience.
[3264.50 --> 3268.60]  Back in time.
[3272.52 --> 3276.58]  Well, thanks.
[3276.58 --> 3279.00]  Bye.
