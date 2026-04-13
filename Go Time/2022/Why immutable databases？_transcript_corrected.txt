[0.00 → 3.68] The cryptography itself and mathematics can be very theoretical.
[4.14 → 9.78] And as long as it doesn't find the practical place to give you some benefits, it's still a theory.
[10.16 → 15.24] And when I've learned about IMDB, that was this moment that you find something that is working,
[15.52 → 18.28] live database, that you can easily use it.
[18.42 → 22.12] And it has all this machinery behind it that is doing all these proofs
[22.12 → 26.26] and is cryptographically verifying everything and keeps everything in place.
[26.26 → 29.88] So that's something for me that is a great benefit for all of us.
[30.00 → 36.86] This episode is brought to you by Signal Wire.
[37.12 → 42.28] Signal Wire offers APIs, SDKs, and edge networks around the world
[42.28 → 46.48] for building the realest real-time video and video communication apps
[46.48 → 48.88] with less than 50 milliseconds of latency.
[49.16 → 54.14] They use WebSockets to deliver 300% lower latency than APIs built on REST,
[54.14 → 59.48] making it ideal for apps where every millisecond and responsiveness makes a difference.
[59.48 → 63.64] Like apps that need instant natural language understanding, real-time machine vision,
[63.98 → 66.54] or large-scale video and audio conferencing.
[66.90 → 67.68] Here's what makes them different.
[67.76 → 74.62] They use MCU, Multi-Point Control Unit, that mixes all video and all audio feeds on the server side
[74.62 → 79.34] and then distributes a single unified stream back to every participant.
[79.34 → 84.88] That way, every participant in the apps you ship experiences the same video and the same audio.
[85.26 → 89.40] Your apps have none of the awkward audio effects, obvious lag, and jumpy video.
[89.70 → 96.18] It's all smooth, great UX, creating a more lifelike virtual experience without compromising audio or the video quality.
[96.46 → 98.06] Head to SignalWire.com slash video.
[98.18 → 101.66] Mention go time to receive an extra 5,000 video minutes.
[101.66 → 104.56] Again, go to SignalWire.com slash video.
[105.06 → 106.22] And remember to mention go time.
[119.68 → 120.72] Let's do it.
[121.26 → 122.34] It's go time.
[122.82 → 124.34] Welcome to go time.
[124.74 → 128.06] Your source for diverse discussions from around the go community.
[128.06 → 132.60] Subscribe today at go time.fm and follow the show on Twitter.
[132.82 → 134.40] We are at go time.fm.
[134.76 → 139.80] Special thanks to our partners at Vastly for delivering go time superfast all around the world.
[140.10 → 142.68] Check them out for yourself at fastly.com.
[142.92 → 144.06] That's all for me.
[144.38 → 145.12] Here we go.
[145.12 → 161.56] Welcome, everybody, to this episode of Go Time, where we get to talk about immutable databases.
[161.56 → 171.96] Now, I must admit, I'm going to be a skeptic during this show because I've been looking for use cases, right?
[171.96 → 176.62] And the project we're going to be talking about does a very good job of sort of articulating those things.
[177.22 → 180.68] But I'm still very much old school, if you can call it that, right?
[180.74 → 184.70] The concept of immutable databases has been something I've ever had to use at work.
[184.76 → 187.50] So I'm looking to, well, let me take that back.
[187.52 → 188.44] I'm not going to be a skeptic.
[188.58 → 192.80] I'm going to approach this with an open mind, and I'm going to approach it as a learner, right?
[192.80 → 196.66] As a beginner to this space and to this kind of technology, okay?
[196.66 → 201.14] Joining me today is my co-host, John Calhoun.
[201.32 → 201.90] Say hi, John.
[202.16 → 202.52] Hey, Johnny.
[202.64 → 203.00] How are you?
[203.32 → 203.94] I'm good.
[204.06 → 207.78] Man, we haven't been on a podcast together for like a couple of months at least.
[207.96 → 208.80] It's been a little while.
[208.96 → 209.54] It's been a minute.
[209.66 → 211.30] Glad to have you with me here today.
[211.64 → 213.62] Also joining me are two.
[214.18 → 222.78] I don't know if it's co-founders or core contributors or all of the above, but the two of you work on the Code Notary team.
[222.78 → 228.66] And I did a quick Google around and see and see that's actually a company that actually has a product that they're selling.
[228.78 → 229.98] But we're not here to talk about that.
[230.08 → 236.68] We're here to talk about the open source project that the team is behind called Emu DB, right?
[236.96 → 241.08] Joining me to talk about this project are the folks who work on it all the time.
[241.34 → 250.44] I've got Bart Rienzi, who is a software engineer, and he's passionate about cryptography and applied math and open source.
[250.44 → 254.74] And he's been working on sort of Emu DB since last year.
[255.36 → 257.12] And obviously, he's been using Go to do that.
[257.18 → 263.16] So we're going to be peeling back that onion to figure out what makes you Go such a good tool for this particular kind of technology.
[263.44 → 266.66] Also joining Bart is Iranian Irazapal.
[267.18 → 272.12] So Iranian also works at the Code Notary on the team that works on Emu DB.
[272.70 → 276.70] And he's a software engineer, also passionate about cryptography and database.
[276.76 → 277.66] I'm seeing a theme here.
[277.66 → 286.16] And also, he's been working on Emu DB actually a little bit longer since the year before, since July 2020, on this particular project.
[286.26 → 290.50] And I'm also interested in hearing what your journey has been using Go to build these kinds of things.
[290.78 → 292.60] So welcome, Bart, and welcome, Iranian.
[292.92 → 294.36] Hi, nice to have me here.
[294.58 → 295.42] Pleasure to be here.
[295.94 → 296.64] Awesome, awesome.
[296.64 → 303.50] So, first, I think our audience, not everybody is going to be familiar with the concept, right?
[303.56 → 309.06] We all sort of share a common understanding for application developers, you know, writing business applications and whatnot.
[309.52 → 313.08] We all have a pretty common understanding of your database, right?
[313.08 → 315.46] You write things in, and you update records.
[315.66 → 317.56] And when you need to, you delete things.
[317.56 → 321.82] So it's almost like it's a tool for transactions, right?
[321.82 → 323.04] You record things in there.
[323.14 → 325.64] And when something is no longer needed, you delete it.
[325.80 → 326.94] Sometimes you might need to update it.
[326.98 → 331.80] But at any given time, the state of the data within the database is shifting, right?
[332.32 → 336.04] And in comes this concept of an immutable database.
[336.04 → 339.66] And to which I'm scratching my head, I'm thinking, okay, what is an immutable?
[339.66 → 342.20] Why would I want my database to be immutable?
[342.42 → 344.26] So please, let's start with you, Bart.
[344.42 → 347.74] Why don't you tell me what an immutable database is?
[348.40 → 353.44] Yeah, so when you have some information, and you put them inside your database,
[354.20 → 357.56] usually we tend to think that this is some kind of temporal state.
[357.66 → 360.10] We can change this, alter this after some time.
[360.34 → 364.64] But what if actually there is some information that you don't want to change?
[365.22 → 367.54] And that's where the immutability comes into play.
[367.54 → 371.78] So maybe there are some information like critical things,
[371.96 → 374.00] like maybe transactions on your account,
[374.26 → 380.90] or some records that, let's say, you write down the temperature on your room.
[381.10 → 383.16] This is not going to change in the future.
[383.90 → 386.92] So that's where the data itself is immutable.
[387.88 → 392.10] And immutable databases try to work with this kind of information, right?
[392.10 → 397.72] So with the information that won't be altered or maybe differently,
[398.52 → 399.96] sometimes the data can be altered,
[400.12 → 403.20] but some properties of this information should not be changed,
[403.24 → 405.52] like the history of the values.
[405.84 → 408.70] If you want to scan over a whole history of the values
[408.70 → 412.64] and you maybe have a use case where you have to look back
[412.64 → 416.62] what was the state of a time, this history will not change.
[416.62 → 419.94] So that's also a property that maybe you want to keep immutable.
[420.68 → 422.68] And also the database,
[422.98 → 426.94] maybe you want to have an extra layer of protection from the database
[426.94 → 431.40] so that you don't accidentally change and damage this information.
[431.82 → 434.68] I remember when I was working on some standard databases,
[434.86 → 435.64] this common database,
[436.04 → 441.02] there's this feeling when you do delete too many records from the database
[441.02 → 442.52] and suddenly you feel that,
[442.74 → 445.50] oh, how can I get out of this situation?
[446.40 → 448.68] And immutability here helps a lot.
[448.90 → 450.50] It gives you this peace of mind,
[450.58 → 452.58] but there's also much more to it.
[452.86 → 452.90] Right.
[453.26 → 456.30] Let me try to sort of state that back to you,
[456.42 → 457.76] but based on the way I understand it.
[457.80 → 460.22] So when we're talking about immutable data, right,
[460.22 → 463.08] let's just remove the database aspect of it for a second.
[463.18 → 464.34] When we talk about immutable data,
[464.40 → 467.02] we're talking about what is the state of things?
[467.76 → 469.64] What is the reality of things right now?
[469.64 → 471.50] Or at the time I choose to record this data,
[471.58 → 475.06] be it on a piece of paper or electronically in a database, whatever, right?
[475.26 → 477.22] What is the state of the world right now
[477.22 → 478.76] at the time I'm writing this piece of data?
[478.88 → 483.70] So if currently it is 50 degrees Fahrenheit at this hour, this minute, right?
[484.04 → 485.64] And in another hour, right,
[485.68 → 488.90] if the temperature rises by 10 degrees, and now it's not 60 degrees,
[489.26 → 490.86] you're not changing the past.
[490.92 → 492.78] You're not changing when it was 50.
[493.06 → 495.22] You know, you're basically adding a new record saying,
[495.22 → 499.98] okay, another snapshot of this data means that at this hour,
[500.08 → 501.48] now it is this temperature.
[501.66 → 505.84] So it's almost like you're dealing with sort of append-only logging kind of situation
[505.84 → 510.14] where at any given time, you're able to sort of go back in history
[510.14 → 513.94] to figure out what was the state of the world at this particular time,
[514.08 → 515.46] this particular point in time.
[515.46 → 519.28] But for, which is, I can see why sort of,
[519.36 → 521.90] this creates some sort of trail, a log, auditability,
[522.04 → 524.56] that kind of things and see, okay, well, how is this thing changing over time?
[524.64 → 525.32] Who changed it?
[525.40 → 526.60] You know, why, whatever, right?
[527.16 → 531.22] So that applies to this particular use case whereby in most cases,
[531.22 → 534.88] what I'm used to is give me the current temperature, right?
[535.20 → 538.40] Whether I ask for that an hour ago or an hour from now,
[538.54 → 540.72] I'm asking for the current temperature.
[540.80 → 541.62] Give me the current temperature.
[542.12 → 545.44] So what you're tracking behind the scenes, multiple versions of it,
[545.46 → 547.12] that's kind of your business.
[547.32 → 550.22] But sometimes I just want whatever the current value,
[550.32 → 552.90] however you determine that, I want whatever the current value is, right?
[552.90 → 554.84] So those are slightly different use cases.
[554.92 → 560.00] So it seems to me that immutable databases are about keeping history of things, right?
[560.00 → 564.28] Not about sort of being your own, almost like your primary database.
[564.40 → 566.06] Like if I'm building a weather app, right?
[566.30 → 569.60] I may want to see, right, what the historical value is.
[569.68 → 574.06] But if we change that a little bit and add, say, a financial services app or something,
[574.06 → 576.30] I may not for a bank, for example, right?
[576.64 → 580.16] When I can see my account balance over time,
[580.78 → 585.32] and every time this entry was sort of a every time my account is changed, right?
[585.48 → 589.22] Maybe a new purchase or a debit or some sort of deposit.
[589.22 → 591.06] I'm tracking that over time.
[591.58 → 594.02] But at any given time, I want to know what's my current balance.
[594.10 → 595.58] Can I buy this thing or not, right?
[595.80 → 597.22] So there are different use cases.
[597.38 → 599.34] One is not supposed to replace the other.
[599.54 → 600.54] Do I understand this correctly?
[601.08 → 602.30] In a sense, yes.
[602.76 → 606.22] So basically, this immutable database is like water over time.
[606.22 → 608.50] But it also contains the most recent state.
[609.02 → 611.90] Like if you want to check the balance, your current balance,
[612.28 → 614.20] it will still be inside this database.
[614.20 → 618.46] So there is still a use case as a primary source of information.
[618.62 → 623.94] But it's actually more about protection against some kind of tempering with the history.
[624.76 → 629.00] So if you want to make sure that the current balance is the true information,
[629.44 → 635.16] how can you be sure that someone did not do some kind of change in the history,
[635.58 → 636.38] alter the data?
[636.76 → 639.78] How can you be sure that the current state is actually valid?
[640.24 → 643.42] Let's have a use case where there is a banking application.
[643.68 → 644.86] Like a simplified use case.
[645.04 → 645.72] And there is a user.
[646.34 → 650.84] If you want to check your current balance, you open this application, check the balance.
[651.06 → 652.12] Then you do some purchases.
[652.60 → 653.92] And then you check the balance again.
[654.50 → 658.78] So you intuitively check if this thing match.
[659.44 → 663.98] So if the previous state, previous balance, and the price that you have to pay,
[664.22 → 665.08] if this all matches.
[665.66 → 667.96] If it doesn't match, you start being suspicious.
[668.56 → 669.40] Something is wrong.
[669.78 → 676.24] And immutability also and verifiability can be used to actually make sure that not only
[676.24 → 677.40] the user can do this.
[677.60 → 679.32] So you remember the old state.
[679.62 → 680.82] You know the current state.
[680.90 → 683.82] And you can somehow check if this is consistent.
[684.64 → 689.66] And immutability here, and especially in Timid, gives you tools, cryptographical tools,
[690.20 → 693.42] to make sure that actually the database did not fly to you.
[693.90 → 697.86] So once something was written in the history, the database cannot say that,
[697.86 → 699.24] oh, it was something different.
[699.24 → 700.40] It cannot lie to you.
[700.42 → 704.16] Because if it would lie, then you will immediately see this.
[704.16 → 706.52] Because of this mathematical proof.
[706.72 → 711.98] So if there is something crucial like audit logs, which after some time,
[712.34 → 715.58] you may want to do some investigation what happened over time.
[715.58 → 718.08] This gives us extra protection.
[718.08 → 720.82] But you can rely on this information.
[721.04 → 727.22] Because database has proven that up to this point in time, it is consistent with the whole
[727.22 → 727.62] history.
[728.16 → 728.24] Okay.
[728.54 → 728.82] Okay.
[728.82 → 734.96] I think you were covering a lot of problems that are addressed by immutability databases.
[735.56 → 739.56] First, I would like to clarify, immutability is an overloaded term.
[740.06 → 746.46] Because as Shōnen, you were mentioning, with immutability, we usually refer to systems or
[746.46 → 753.16] data structures that are a pen only, that treat changes or updates as a new data, actually.
[753.16 → 759.40] So when we are doing an update of a record, we are not mutating the original record, but
[759.40 → 763.64] treating the update as a new record, describing the change.
[764.38 → 767.50] So we are used to that for immutability.
[767.80 → 774.12] And actually, Immune relies on every component in Immune is an happen only data structure.
[774.64 → 778.12] Even the cryptographic data structure are treated as happen only.
[778.12 → 784.86] But in immutability in databases or even in blockchain, we tend to refer to another thing,
[785.06 → 791.92] not just to append only, but to the possibility to verify that the history hasn't changed.
[792.66 → 798.08] So every record is registered and cryptographic linked to what happened before.
[798.08 → 805.12] And then you have a way to verify if a given transaction or a given record was present and
[805.12 → 808.70] was not modified anymore once it was written.
[809.32 → 813.98] Doesn't mean that you cannot have the current state of your balance account.
[814.62 → 820.76] And as a traditional database, you will have either as the current, the latest value that
[820.76 → 825.92] was placed for a given record, because the record will be the key that identifies the address
[825.92 → 827.22] or the balance.
[827.82 → 833.66] But also, depending on the use case, it may be a cumulative set of changes, like in Git,
[833.76 → 835.48] where we are committing changes.
[836.14 → 840.78] So the current state or the history, it's independent of that.
[841.14 → 844.88] What we refer to this type of thing is verifiable.
[844.88 → 852.12] I prefer the term verifiable database rather than immutable database, because every system
[852.12 → 854.04] has integrity checks, right?
[854.14 → 860.84] Internal integrity checks to check the consistency of a given record or of a given file, if it
[860.84 → 864.86] was consistent, is consistent or not.
[865.36 → 871.14] But with tampering detection, it's like giving the possibility to the client application or the
[871.14 → 876.60] application that is using the database to do their integrity validation by themselves.
[877.14 → 878.46] That is one of the differences.
[879.00 → 884.50] It's the application that is receiving the data from the database who is able to run the
[884.50 → 891.72] integrity check to validate that the data that was received was not modified since it was
[891.72 → 892.08] written.
[892.38 → 894.12] Okay, let's pull on that thread a little bit.
[894.12 → 901.50] So we're not talking about the clients sort of being or maintaining a copy of whatever
[901.50 → 906.90] data you might have at a central sort of immutable database or verifiable database, right?
[906.92 → 911.88] You're talking about some sort of cryptographic verifiability of the data.
[912.12 → 918.92] So one of the particularities of an immutable database is that at every moment, the complete
[918.92 → 922.38] state of the database is captured by a hash value.
[922.38 → 929.28] So that denotes not only the current state, but what the complete history of changes up
[929.28 → 929.92] to that point.
[930.46 → 937.42] So the client in InnoDB, for instance, or in other immutable databases, is the client who
[937.42 → 940.06] needs to keep track of this current state.
[940.52 → 947.38] The latest state that is known is like in the example that Bar mentioned regarding your bank
[947.38 → 952.74] bank balance account, you may know what was the latest state that you can trust.
[953.20 → 957.14] And based on that and the new changes is where you can compare.
[957.38 → 962.56] You have the base to compare the new changes or the new results and so on.
[962.68 → 968.22] So, but the client only needs to keep track of the state of the database at any given point.
[968.36 → 970.10] That is the minimal information.
[970.10 → 974.60] So to make sure I understand this, that means that deleting records also isn't permissible.
[975.00 → 975.52] Is that true?
[975.88 → 977.56] Deletion is actually depending.
[977.90 → 979.08] We have two levels.
[979.46 → 982.40] We have logical deletion or physical deletion.
[982.86 → 988.08] Logical deletion is something that can be handled by the application or by the server.
[988.48 → 993.54] But the difference will be in terms of performance because the filtering out of the information will
[993.54 → 997.88] be done much faster if it's done directly by the database.
[997.88 → 1005.10] In Nemo DB, we currently have support for logical deletion in both manners, like deleting a key,
[1005.18 → 1008.28] for instance, or by providing an expiration date.
[1008.90 → 1011.86] But this currently is just a logical deletion.
[1012.04 → 1014.14] This means the data will be still there.
[1014.60 → 1018.66] It will be automatically filtered out, and the client won't receive it.
[1018.92 → 1021.28] But it's not yet physically deleted.
[1022.02 → 1026.16] And we are under discussions to incorporate physical deletion of data.
[1026.16 → 1032.98] And it's a very, very interesting topic to discuss what involves physically deleting the data
[1032.98 → 1035.46] and yet being able to prove.
[1035.78 → 1042.20] So depending on the data you delete, or you remove, is the possibility you have later on to build proof.
[1042.76 → 1044.60] So it's a very, very interesting topic.
[1045.14 → 1045.22] Yeah.
[1045.22 → 1049.48] And I'm assuming we're going to want to talk about good use cases for an immutable database.
[1049.84 → 1053.62] But I guess the first thing that comes to my mind is I feel like you'd have to be careful
[1053.62 → 1058.84] as to what applications you use this for because there are rules like GDPR where you have to be able
[1058.84 → 1060.18] to forget people, essentially.
[1060.84 → 1064.74] And I could imagine a weird situation where you write something to an immutable database
[1064.74 → 1067.90] accidentally and then realize, like, how do we fix this?
[1067.90 → 1074.98] And actually, GDPR is the main reason why we started actually thinking about physical deletion
[1074.98 → 1083.44] because some laws require from you to make sure that the data is not accessible at all after some time.
[1083.80 → 1089.04] Of course, the rules are not clear because sometimes you have to hide the data from the users,
[1089.04 → 1094.54] but then you have to keep it for a longer time because there may be some kind of investigation later on.
[1094.54 → 1098.72] But still, it is possible to actually remove the data.
[1098.94 → 1103.78] And maybe there is a different reason for that because if you have append-only structure,
[1104.00 → 1109.08] append-only data, and you start putting too much data into it, you will just run out of space.
[1109.86 → 1115.16] And after sometimes you want to reclaim maybe the space, or you have physical constraints of your server
[1115.16 → 1118.48] and you have to deal with that and there is a production system running.
[1118.48 → 1126.26] So maybe you want to just wipe data that is older than some point in time in the past.
[1127.18 → 1134.60] And still, the state, as Hirohito said, the state of the database, the hash of the database contains all the history.
[1135.24 → 1137.08] So this is a very interesting topic.
[1137.22 → 1143.38] So you no longer have the data, but the state needs to calculate this data in
[1143.38 → 1151.40] so that you can still prove that the new changes added to the database are consistent with the whole history since the beginning.
[1151.92 → 1160.86] Regarding use case, a few months ago, there was a situation with a famous tennis player and the COVID-19 results.
[1161.40 → 1168.38] And there was some news regarding multiple results depending on when it was acquired from the service.
[1168.38 → 1173.42] Of course, if that data is stored in multiple databases or in blockchain,
[1173.60 → 1179.24] then it will be possible to actually know if that data was consistent or was tampered with.
[1179.86 → 1184.70] That is kind of use case in a more traditional system or service,
[1185.30 → 1191.52] that it may take time to use a traditional immutable database in this type of system or service,
[1191.86 → 1194.78] but I'm sure it will happen with time.
[1194.78 → 1199.80] So it's not about just sensitive information like it.
[1224.78 → 1230.86] What would normally be manual error-prone tasks across the entire spectrum of responding to an incident?
[1231.20 → 1234.70] This can all be automated in every way with Fire Hydrant.
[1235.08 → 1240.88] Fire Hydrant gives you incident tooling to manage incidents of any type with any severity with consistency.
[1241.44 → 1244.56] You can declare and mitigate incidents all inside Slack.
[1244.94 → 1247.94] Service catalogues allow service owners to improve operational maturity
[1247.94 → 1250.92] and document all your deployments in your service catalogue.
[1250.92 → 1256.54] Incident Analytics like to extract meaningful insights about your reliability over any facet of your incident
[1256.54 → 1258.28] or the people who respond to them.
[1258.78 → 1260.68] And at the heart of it all, Incident Run Books,
[1260.76 → 1264.88] they let you create custom automation rules to convert manual tasks into automated,
[1265.24 → 1268.26] reliable, repeatable sequences that run when you want.
[1268.62 → 1273.42] Create Slack channels, Jira tickets, Zoom bridges instantly after declaring an incident.
[1273.84 → 1276.50] Now your processes can be consistent and automatic.
[1276.98 → 1278.66] Try Fire Hydrant free for 14 days.
[1278.66 → 1280.24] Get access to every feature.
[1280.38 → 1281.38] No credit card required.
[1281.70 → 1283.66] Get started at FireHydrant.io.
[1283.96 → 1285.72] Again, FireHydrant.io.
[1285.72 → 1285.84] FireHydrant.io.
[1305.60 → 1310.00] So it sounds like of the use cases, you know, some obvious ones are, you know,
[1310.02 → 1315.42] obviously financial transactions, you know, health records and things that basically you care about
[1315.42 → 1317.00] that basically change over time.
[1317.08 → 1321.72] You want to be able to go back at some point and say, hey, what was the state of things on this day, right?
[1322.10 → 1328.84] And have a high degree of confidence that this data hasn't been altered, hasn't been modified or anything like that.
[1329.06 → 1331.38] That's the key takeaway here from what I'm gathering.
[1331.98 → 1338.86] So I'm curious, what drives folks like you into this particular domain problem?
[1339.10 → 1340.38] Why immutable databases?
[1340.38 → 1342.86] All the things you could be working on.
[1343.86 → 1344.04] Yeah.
[1344.04 → 1348.04] I think we both say that we like playing with cryptography and math.
[1348.30 → 1354.48] For me personally, when I start learning about IMU-DB and what techniques it uses,
[1355.14 → 1359.02] the cryptography itself and mathematics can be very theoretical.
[1359.02 → 1367.54] And as long as it doesn't find the practical place to give you some benefits, it's still a theory, right?
[1367.78 → 1372.82] And when I've learned about IMU-DB, because I joined the team a few months ago,
[1373.32 → 1379.56] that was this moment that you find something that is working, live database, that you can easily use it.
[1379.56 → 1388.88] And it has all this machinery behind it that is doing all these proofs and is cryptographically verifying everything and keeps everything in place.
[1389.70 → 1395.02] So that's something for me that is a great benefit for basically all of us, right?
[1395.10 → 1397.92] So previously we could think of this.
[1398.34 → 1406.12] Maybe there is a project that I want to create, and it would use this technology, but then I find it hard to implement this.
[1406.12 → 1412.92] And suddenly I find this kind of database where I have very easy interface and I can just take it and use it.
[1413.66 → 1418.26] So for me, that's the major goal of a project like IMU-DB.
[1418.82 → 1427.80] So we have a lot of knowledge and actually the majority of the cryptography and all these algorithms were invented a long time ago.
[1428.30 → 1431.94] And right now we only started implementing them and implementing them practically.
[1431.94 → 1440.94] And that's where I think IMU-DB is, that's where the goal of the project is, give people the way to use immutable database in a simple way.
[1441.64 → 1446.92] Yes, before giving the explanation how I end up here.
[1447.54 → 1455.20] But actually using IMU-DB for application developer is exactly the same as using a traditional database.
[1455.20 → 1466.12] You can download the IMU-DB binary or docking container, and you will use like any other key value store or SQL database as well.
[1466.74 → 1471.52] So before I joined Country, I was working as a software engineer for IBM.
[1472.34 → 1477.34] And the last project were related to digital right management.
[1477.84 → 1483.00] And that was related to applied cryptography there for generating the crypto materials.
[1483.00 → 1488.80] And also I was a contributor for hyperlateral fabric by then.
[1489.28 → 1495.00] Also, I worked in an experimental project where we added SQL to hyperlateral fabric.
[1495.54 → 1501.40] And we added SQL support into the chain codes, like actually in the smart contracts.
[1502.06 → 1509.04] But by then I was convinced that the complexity of the project was quite big.
[1509.04 → 1521.06] There were many companies or organizations willing to use blockchain just to be sure or to prove themselves or to their clients that the data was not changed.
[1521.62 → 1524.94] But then they had to run a very, very complex system.
[1524.94 → 1532.88] So I always thought about the possibility to have just a traditional database with the verification possibilities.
[1533.28 → 1543.74] So to have the same verification capabilities like a blockchain provide, but thinking of single organizations being the owners of the data.
[1543.74 → 1552.40] But yet to fulfill with the auditory requirements or to prove to their clients that the data has not been changed.
[1553.20 → 1557.22] So by then I started to think about this type of system.
[1557.56 → 1562.22] And I got to know about the company and the initial release of Incudes.
[1562.22 → 1572.10] By then Incudes was implemented using Relay in another Go, another key value store that was written in Go.
[1572.68 → 1575.56] So that's where I started to work.
[1576.28 → 1583.84] And related to verified immutability, I think tampering detection is one of the type of verification we can do.
[1583.84 → 1590.12] But there are many other things that we are there to be explored or to be included.
[1590.44 → 1593.62] Like what is the latest record that was modified?
[1594.10 → 1600.62] How to be able to verify when you are dealing with higher level data models like SQL.
[1601.20 → 1608.14] If you have a database, and you have a document like data model, and you have queries, and you have to verify that.
[1608.14 → 1614.44] So there are a lot of things to get to investigate, to explore and of course to implement.
[1615.10 → 1617.68] So it's not law something you mentioned blockchain.
[1617.82 → 1618.56] We'll come back to that.
[1618.70 → 1619.46] We'll come back to that.
[1619.92 → 1623.14] You piqued my curiosity when you said that you support both SQL.
[1623.70 → 1629.96] You can use it both as a traditional sort of RDBMS, SQL database, or as a key value store.
[1630.18 → 1632.78] Why the dual modality for accessing data?
[1633.12 → 1636.08] Actually, everything started as a log.
[1636.08 → 1642.46] So InnoDB has a composite construction.
[1642.94 → 1645.36] Everything started as an embedded database.
[1645.74 → 1648.16] So InnoDB can be used as an embedded database.
[1648.80 → 1650.52] That is a set of logs.
[1651.08 → 1653.16] Append-only log that is verifiable.
[1653.28 → 1655.46] It's like a transparency log.
[1655.98 → 1664.22] So you can access one of the differences of traditional key value store is that you can access a given transaction by its ID.
[1664.44 → 1665.66] Its unique ID.
[1666.08 → 1676.54] If you only need to store records, logs, events, and then to query them, you don't need to query the data using an index.
[1676.54 → 1680.44] Just directly using the entry of the log.
[1680.84 → 1684.08] That is the initial, the basic way of using it.
[1684.66 → 1688.62] Then we have the possibility to build an index based on the key.
[1688.62 → 1694.84] So because every transaction or log entry consists of a list of key value entries.
[1695.08 → 1702.50] So then you can easily get what are the transactions that modify this particular entry.
[1702.50 → 1705.80] And you will, of course, you will get the latest one.
[1705.80 → 1712.06] But you also cannot get the history of transactions that modify this particular key.
[1712.06 → 1715.96] And that is how we implemented temporary capabilities.
[1715.96 → 1722.68] So you can go back in time in the database and query the database as it was sometime ago.
[1722.68 → 1725.04] And without seeing newer changes.
[1725.42 → 1729.16] On top of this, we implemented SQL capabilities.
[1729.16 → 1741.08] So when you create an entry thinking in SQL, it ends up being a transaction that consists of key and value entries.
[1741.08 → 1749.20] So SQL, all the SQL changes or SQL data model is backed by a key value database.
[1749.96 → 1753.94] So actually, the same transaction is what is happening.
[1754.10 → 1759.10] So we are using the key value transactions to store transactions that happen in SQL.
[1759.78 → 1762.58] So SQL was added afterward.
[1763.02 → 1766.08] So it's possible to use both.
[1766.08 → 1778.64] So, of course, they are isolated entries that are inserted using the key value are not seeing the internal changes or internal entries that are working with SQL.
[1779.02 → 1781.36] But both data models are possible.
[1781.98 → 1786.38] The advantage of using SQL, of course, is easier to model your application.
[1786.38 → 1797.12] Because you have to think it's easier to work when for later on, define index for is efficiently querying the data, for writing queries, of course.
[1797.84 → 1802.44] But we also added the possibility to verify in SQL.
[1802.66 → 1804.30] So that is one of the differences.
[1804.54 → 1807.88] So you can get a particular row based on the primary key.
[1808.46 → 1810.02] And this entry will be very fine.
[1810.64 → 1815.74] So you're still able to model your application just like you would in a relational system.
[1815.74 → 1816.14] Exactly.
[1816.38 → 1821.84] It's just basically the encrypted storage that is used in the verifiability once you pull data out.
[1822.00 → 1829.44] All these things you're adding sort of on top of the good old model that most developers who built web applications and whatnot are familiar with for example.
[1829.74 → 1832.46] So let's talk about the operability of this.
[1832.54 → 1836.26] But before we jump into that, I see John, you've got a burning question you want to ask.
[1836.58 → 1837.60] I don't have a burning question.
[1838.16 → 1839.02] It's a question.
[1839.02 → 1850.40] I was going to say that like the SQL stuff reminds me of the first time I ran into a use case where I didn't necessarily need an immutable database, but I needed to mimic its functionality in some way.
[1850.82 → 1853.56] Basically, I was working on like shipping stuff with addresses and everything.
[1853.56 → 1858.30] And one of the things that came up where people were like, well, I want to be able to change these addresses I used to ship to things.
[1858.30 → 1870.10] And it became very clear that in a relational database, if you have a bunch of previous shipments that all associate with some record, and then you change it, then all of a sudden your history is really weird at that point because that's not actually what those shipments were.
[1870.10 → 1880.34] And like seeing a database like this, it's kind of interesting to like, I think as developers, we encounter cases where immutable databases or something like that is useful.
[1880.62 → 1885.54] I mean, we all use package managers, which are another example of like not really having immutability.
[1885.72 → 1889.72] You can release a version, but once it's released to some package manager, you're kind of stuck.
[1890.04 → 1891.32] You know, you have to release a new one essentially.
[1891.62 → 1892.36] Or you're supposed to be.
[1893.22 → 1895.00] I mean, I don't want you to be able to change that.
[1895.14 → 1897.22] As I say, most package managers won't let you do it.
[1897.22 → 1915.40] So I think as developers, we use immutable systems at times, but we kind of like forget about it because I think a package manager is a great example of something that really benefits from something where you can verify nothing got changed because that would be terrible when you're downloading third party packages to like not know for sure that that's still the same version.
[1915.80 → 1922.28] But it's also like interesting in the sense that I feel like most systems we work with that use immutability have some sort of scapegoat.
[1922.28 → 1928.50] The best example I can give is like get we always get where you can have the history, and it's supposed to basically be immutable.
[1929.02 → 1934.48] But there's always ways to force changes into like to rewrite history, which is not necessarily a great thing, but it's possible.
[1935.30 → 1947.16] So knowing that developers at some point want to like rewrite history and stuff, do they have to come into using MUD like they can't come into it, I'm assuming, with the same mindset of like I can use this exactly like a SQL database.
[1947.16 → 1954.16] So are there any like tips or advice that sort of like help them get out of that mindset that you see people struggling with when they're starting?
[1954.16 → 1960.92] So in MUD what actually you could think of is that you can change the data, right?
[1960.96 → 1967.20] You can do corrections, but what you will still get, you have this auditability of the history.
[1967.60 → 1971.08] So it's like not lying to anybody that I did not make a mistake.
[1971.16 → 1971.82] I made a mistake.
[1972.08 → 1973.46] I just corrected it right now.
[1973.56 → 1974.28] This is the state.
[1974.62 → 1975.86] But let me be clear.
[1976.04 → 1977.02] This is what we see.
[1977.38 → 1978.44] This is the current state.
[1978.66 → 1980.38] And previously it was something different.
[1980.38 → 1991.04] And also this example with changing the address, I think this is something very interesting because on the key value level inside MUD, we have something like a reference to other key.
[1991.68 → 1998.66] So instead of getting some specific value, you just try to read it from other key and just forward it back.
[1998.96 → 2004.48] But what you can do is you can say that this reference is for that key at that transaction.
[2005.02 → 2009.02] So what it means is that it like freezes the value inside the history.
[2009.02 → 2018.48] So then you could create, let's say, a record that there was this kind of shipment to that person under that address at that point in time.
[2018.92 → 2020.08] So that is something unique.
[2021.16 → 2025.50] Also, I need to comment about one thing, this package managers.
[2026.42 → 2027.10] Let me say that.
[2027.34 → 2027.62] Please do.
[2028.18 → 2034.86] We have actually been using this immutable databases, but we just don't know it or just forgot about this.
[2034.86 → 2038.98] And a very good example is actually Good proxy.
[2039.66 → 2044.60] And actually the technology behind Good proxy is very similar to what we have.
[2044.68 → 2046.16] It's this kind of immutable ledger.
[2046.76 → 2052.96] And actually we had the situation where we released some kind of tag, some version of MUD.
[2053.28 → 2056.94] And once somebody just fetches it through the proxy, it's set in stone.
[2057.12 → 2058.66] You cannot change it.
[2058.66 → 2061.14] You cannot switch the tag to something else.
[2061.38 → 2063.40] And very weird situations happen.
[2063.62 → 2066.04] And actually this is for the security reasons.
[2066.30 → 2073.90] So if you release something, then everybody who downloads this particular version will only get this version of the code.
[2074.22 → 2077.02] You have to release a new patch version.
[2077.40 → 2078.42] And that's actually perfect.
[2078.42 → 2080.74] And that's good about the security.
[2081.24 → 2082.12] I agree that that's good.
[2082.30 → 2095.16] I guess I would imagine it would make adoption harder in the sense that developers are just weird about, like if somebody releases an invalid package, and they want to pull it back real quickly, they're still weird about like now I have to increment the version, and they don't want to do that.
[2095.34 → 2099.44] For whatever reason, mentally, they're like, I don't want to admit I made a mistake and show that to people.
[2099.76 → 2100.12] Too bad.
[2100.12 → 2103.88] So like, does that make adoption harder when like you're basically forcing them to do that?
[2104.10 → 2109.34] In this case, in MUD, you have to convince every other client.
[2110.18 → 2120.86] If you want to roll back the history in MUD, you will have to convince every auditor or client that already have that register, that state locally.
[2121.44 → 2122.50] That's the only option.
[2122.74 → 2124.00] Measure twice, cut once.
[2124.00 → 2129.18] But I think that's really making a mistake is not something huge.
[2129.26 → 2131.08] And we all made mistakes.
[2131.58 → 2135.46] And like in real life, there is always an option to correct the mistake.
[2135.62 → 2136.10] For example?
[2137.12 → 2137.54] Yeah.
[2137.80 → 2138.52] Like releasing.
[2138.74 → 2139.24] Let's hear it.
[2139.72 → 2142.04] Releasing a package that contains some bug.
[2142.42 → 2142.98] Right, right.
[2143.14 → 2145.24] And then why should we be ashamed of that?
[2145.24 → 2154.16] And actually, I see that people who can say that they made a mistake, and they corrected that, they tend to deal with those issues better than trying to hide it.
[2154.66 → 2155.98] So I would go that way.
[2156.52 → 2157.16] That makes sense.
[2157.36 → 2161.62] I mean, I guess there are definitely cases where it makes sense to want to delete things.
[2161.70 → 2166.20] Like if you released something on Git that had private keys, clearly you need to try to clean that up.
[2166.30 → 2168.36] But it's, I agree with you that it is hard.
[2168.54 → 2173.18] Like, I don't know, people should be okay with mistakes, but I feel like in practice, people are weird with them.
[2173.18 → 2176.56] And there is actually a technical situation that could happen.
[2176.86 → 2177.84] There is a rollback.
[2178.12 → 2186.34] If you are using, let's say, a single master, a single node, and then it crashes, and you cannot recover the data.
[2187.08 → 2196.80] So if the backup you have is old, then older than the state that the client has, they will comply about that situation.
[2197.26 → 2202.08] So that is a situation that could happen and has to be taken into account.
[2202.08 → 2207.80] So the mistake there will be on having only one node or not having a backup.
[2208.34 → 2209.86] I think it's okay to admit mistakes.
[2210.04 → 2211.60] I guess mistakes are part of life.
[2211.72 → 2212.16] It's okay.
[2212.38 → 2214.68] You know, just make a new thing and put that out there.
[2214.76 → 2219.32] And hopefully people don't download your mistake before you had a chance to replace it.
[2219.86 → 2223.82] Now, I do want to switch gears real quick to the operability aspect of things.
[2223.82 → 2233.46] Obviously, if one were to find a use case for MUD or really immutable databases in general, it's interesting.
[2233.82 → 2239.52] As I was researching the technology, I came across other things that I've come across before but didn't realize that's what they were.
[2239.66 → 2242.74] Like I came across Amazon's QLDB.
[2243.20 → 2244.90] I'm like, hey, that sounds familiar.
[2244.90 → 2248.18] And basically, I started tracking basically the origin of these things.
[2248.30 → 2250.10] When did these things become popular?
[2250.38 → 2252.76] And there are references going back a few years.
[2252.92 → 2264.00] But these types of technologies became very popular, I think, in part as a result of an executive order that was issued maybe like a year or so ago on cybersecurity and things like that.
[2264.00 → 2269.44] And there was mention of producing or having things like a software bill of materials.
[2269.76 → 2272.84] And then I'm like, hey, I'm starting to hear more and more about that now.
[2273.22 → 2278.12] There's like advancements we've made with shipping and packaging software and things like that.
[2278.28 → 2285.64] And all of a sudden, these dots are connecting for me about all these things that I've read in the past and didn't really know where did this thing come from kind of thing.
[2285.88 → 2288.48] And for those listening in, it's interesting.
[2288.66 → 2289.82] Basically, find the executive order.
[2289.94 → 2292.22] It's called a cybersecurity something, something.
[2292.22 → 2295.74] It's basically you can find it on the White House.gov website or whatever.
[2295.88 → 2301.48] But you'll see like this mandate, right, with lots and lots of requirements for cybersecurity and everything else.
[2301.58 → 2304.48] And you're going to find software bill of materials and stuff mentioned in there and whatnot.
[2304.70 → 2313.66] And you can see how things like that, right, are sort of pushing forward the innovation that's happening in this space, especially with things like EM UDB and whatnot.
[2313.66 → 2326.36] And one of the things that one of the use cases that you're enabling or solving for is the whole sort of software, you know, verifying the content of a software package.
[2326.48 → 2326.60] Right.
[2326.60 → 2332.68] So we just talked about how, you know, basically the Good proxy, right, basically part of the thing that is also part.
[2332.90 → 2348.78] And for those who basically download your modules, and you see this weird Go. Sum file with all the checksums in there and whatnot, that, you know, all these things sort of play a role, right, into basically verifying that the version of the piece of software that you just got is indeed, right.
[2348.78 → 2352.72] It's not going to basically, you're not going to get a different version that has the same checksum, right.
[2352.72 → 2356.50] So all these things come together to provide that sort of verifiability thing, right.
[2356.82 → 2363.48] So, but I know one of those use cases that you try to sort of solve for head on, right, is this BOM thing.
[2363.58 → 2365.34] Can you take a little bit about that?
[2365.40 → 2368.92] And then I want to talk about what it's like to actually run EM UDB in production.
[2369.32 → 2369.46] Yes.
[2369.56 → 2376.82] So BOM, so software bill of material, is a term that is used to, let's say, that you create a software and you create it.
[2376.82 → 2379.52] Today, you don't write all the software by yourself.
[2379.64 → 2381.56] You just use external packages.
[2382.24 → 2389.62] And when we look at, let's say, don't JS application, it usually has hundreds of different dependencies.
[2390.50 → 2391.98] And the same with Golang, right.
[2392.08 → 2395.54] You don't write HTTP server by yourself.
[2395.64 → 2400.98] You just take what in standard library, and you do the same with contributions from other people.
[2400.98 → 2408.30] And the software bill of material is basically describing that if we have this binary or this product, what is it made of?
[2409.08 → 2416.88] And here we can actually use this immutable ledger because we just produce those assets, those binaries once.
[2416.88 → 2427.38] And we can identify them by, let's say, taking a hash, which is uniquely specifying this specific binary and say that this consist of other components.
[2427.52 → 2431.80] And those components also have this unique ID, maybe some kind of hashes.
[2431.80 → 2438.40] So that means that if you change anything, even a smaller bit, you will get totally different binary.
[2439.12 → 2444.70] And you also have this specific set of components that it was built from.
[2445.10 → 2452.68] And when you take software companies that are running these binaries then, and then it turns out that there is one specific library that has vulnerability.
[2452.68 → 2458.68] How can you figure out where are those old components that are vulnerable?
[2459.86 → 2469.22] And by just taking the software bill of material information and by just scanning it, what is actually running in the production, you can very quickly identify vulnerable components.
[2469.44 → 2470.64] And then this, fix this.
[2471.06 → 2479.10] Because there were attacks where actually until now people may not know that their software that they are running is vulnerable.
[2479.10 → 2486.38] And this executive order is actually saying that you should have this software bill of material so that you can trace this information.
[2487.04 → 2494.30] And when we talk about immutable ledgers, you can also store this information securely.
[2494.36 → 2501.00] So that if it is persisted and database has given you the proof, then you can rely on this information.
[2501.36 → 2503.22] You can rely on the fact that it was not changed.
[2503.22 → 2519.24] Because maybe there would be an attack that someone goes into your database and your production environment changes some kind of libraries and then attacks also the database that stores information about this bill of material relations, the relations between packages, how you find this.
[2519.70 → 2523.12] And immutability here protects you that you can rely on this information.
[2523.12 → 2534.74] So if we're talking about sort of one of the recent vulnerabilities in Log4j, for example, that made, you know, basically the rounds a few weeks ago, if I wanted to find out, okay, I'm running Java software.
[2535.14 → 2539.84] Am I running the version of Log4j that was susceptible to that vulnerability?
[2540.54 → 2546.38] With the software bill of materials, I can find out exactly, okay, do I have this specific version anywhere in my infrastructure, right?
[2546.38 → 2556.26] And then with something like immutability, an attacker that is leveraging this vulnerability couldn't go and change the software bill of material in immutability.
[2556.60 → 2564.60] They couldn't say you're not really running the vulnerable software by changing the software bill of materials in immutability because you'd have to convince the clients that that wasn't true, right?
[2564.78 → 2567.38] That change was true, whatever it is that we're changing.
[2567.38 → 2568.22] Yes, exactly.
[2568.38 → 2582.84] And actually, that is what is the base for the Code Notary, the company that is building immutability, the base of their financial, let's say, base that there is this Code Notary cloud that is using immutability to actually store this information.
[2583.38 → 2591.44] Because it looks like even if you don't have to, if you're not obliged to have this software bill of material, then it's still good to have this information.
[2591.44 → 2604.50] Because Log4J came out a few months ago, and it was a very critical vulnerability where you could execute a code by just sending, in many cases, some packet to the server.
[2605.42 → 2610.18] And we know that there will be more vulnerabilities like that in the future.
[2610.60 → 2615.04] So it's better to right now be prepared and to start creating this software bill of materials.
[2615.54 → 2619.60] And when such vulnerability will happen, to quickly find it.
[2619.80 → 2621.20] Okay, cool, cool.
[2621.20 → 2631.76] Very briefly, does running immutability, is that process markedly different from, say, managing your traditional RDBMS or traditional key value store?
[2632.26 → 2633.62] All things being equal, right?
[2633.64 → 2641.02] Do I have to do more or less than I would need to, say, run a Postgres server or a Regis server or something like that?
[2641.06 → 2644.80] Just run Docker image or download binary and run it and that's it.
[2644.94 → 2645.54] And then run it.
[2645.68 → 2646.22] Yeah, yes.
[2646.34 → 2647.54] So the beauty of Go, right?
[2647.80 → 2648.52] That's the beauty of it.
[2648.56 → 2649.28] Got your executable.
[2649.28 → 2659.12] And depending on the amount of data you are dealing with, it will require some operational procedures like doing a compaction of the index.
[2659.12 → 2665.00] But there is some already, this is already implemented in UDB, for instance.
[2665.08 → 2672.90] But this is for reducing the space that is required for indexing because the index itself is an append-only data structure.
[2672.90 → 2679.20] So there is an operational procedure to automatically compact the index.
[2679.66 → 2682.44] That is one of the things to take into account.
[2683.16 → 2688.44] And the other is to be aware that you cannot fully the clients that are using.
[2688.44 → 2695.46] So if you try to revert to another backup, the clients will comply about that.
[2695.46 → 2714.80] Hey there, it's Jared again.
[2715.06 → 2716.72] Have you heard about Changelog++?
[2717.22 → 2718.80] It's our membership program.
[2719.00 → 2721.52] You can join to directly support our work on Go Time.
[2721.52 → 2728.70] As a thanks for your support, we hook you up with an ad-free feed, discounts on merch, plus some bonuses like extended episodes.
[2729.20 → 2732.44] Sign up today at changelog.com slash plus.
[2732.44 → 2753.10] I am interested in obviously understanding why you chose Go for this kind of work.
[2753.18 → 2755.52] Was there something you could have picked a different language?
[2756.16 → 2759.52] Was there something special about Go that made this kind of work easier to approach?
[2759.52 → 2765.26] And so when I joined Code Notary Team, actually it was already written in Go.
[2765.80 → 2767.84] Oh, you didn't have a choice.
[2768.38 → 2771.60] But the fact that it was written in Go is very important for me, actually.
[2772.10 → 2775.00] Because I was watching Go for a very long time.
[2775.60 → 2779.82] Initially, I didn't have a chance to work with this commercially, but in my day-to-day job.
[2779.94 → 2784.64] But right now I see all the benefits that Go gives, like having those Go routines.
[2784.64 → 2788.86] I remember the C++ times when I was writing HTTP servers.
[2789.60 → 2793.76] First thing was that you had to write the HTTP server by yourself in many cases.
[2793.96 → 2800.44] But then dealing with all those threads and trying to schedule things and make, you know, keep things under control.
[2800.66 → 2801.66] It was doable.
[2802.12 → 2805.70] And you could write a performance server, but it took a lot of time.
[2805.70 → 2815.66] So Golang is this sweet spot between the efficiency of programming and still having the performance application in the end.
[2816.56 → 2819.68] So I think that it is a very good system.
[2819.80 → 2823.62] And we know that Google is using it because they created it.
[2823.86 → 2825.90] So it must be bottle tested.
[2826.16 → 2834.50] It most likely contains this knowledge about large-scale deployments that are built in because of where it is used.
[2834.50 → 2840.12] And it simplifies so many things that, for me, it's a very good thing.
[2840.22 → 2844.64] And also, Monitory is a startup company where the efficiency is also very important.
[2845.00 → 2846.04] So these things matter.
[2846.56 → 2851.12] So we could write, let's say, something faster, maybe a little bit, a few percent,
[2851.54 → 2855.00] when writing in C++ or even something lower.
[2855.40 → 2861.14] But then it would take, I don't know how many times more time, maybe five, maybe ten even.
[2861.74 → 2862.66] Cool. What about you, Horatio?
[2862.66 → 2863.58] Yeah, exactly.
[2863.76 → 2867.82] When I joined, also, InnoDB was on the initial release.
[2868.40 → 2870.06] And it was already written in Go.
[2870.62 → 2875.14] But we cannot say that we have changed it, made drastic changes.
[2875.52 → 2877.58] So we didn't change the language.
[2878.12 → 2885.02] But we could, actually, because by then we completely write from scratch the storage system.
[2885.02 → 2888.50] Before, InnoDB was used in Batched.
[2889.22 → 2892.78] And that is another key value store that is written in Go.
[2892.98 → 2897.56] But I think it is a good choice for the reasons that Barb mentioned.
[2897.74 → 2902.62] I also like for the code, easy to read, the code readability.
[2902.62 → 2906.04] I found it very, very easy to read code.
[2906.44 → 2907.84] And that is written in Go.
[2907.84 → 2909.02] And it makes it easier.
[2909.50 → 2912.98] Having a standard format for the code is reasons.
[2913.16 → 2914.42] Yeah, you seem pretty content with it.
[2914.90 → 2915.38] Yeah.
[2915.72 → 2916.04] Oh, yeah.
[2916.12 → 2916.94] That's all I heard of.
[2917.02 → 2917.26] Yeah.
[2917.26 → 2917.80] That's awesome.
[2918.00 → 2920.16] Good you mentioned the formatting of Go.
[2920.16 → 2922.80] Because in C++ there was always a word.
[2923.16 → 2926.44] Which one is better and what to choose.
[2926.72 → 2926.88] Yeah.
[2926.90 → 2928.98] Nobody loves Go Fund, but everybody loves Go Fund.
[2929.46 → 2932.20] Actually, I love it since the first years.
[2932.74 → 2933.78] I must say.
[2934.32 → 2937.62] John, you got one final question before we switch it over to Unpopular Opinions?
[2937.78 → 2939.80] I'm fine with jumping to Unpopular Opinions.
[2940.42 → 2941.20] There we go.
[2941.24 → 2941.78] It's that time.
[2941.86 → 2943.70] Oh, I hope you brought the goodies, gents.
[2944.40 → 2944.78] All right.
[2944.80 → 2945.82] Let's get the tune going.
[2950.16 → 2951.32] Unpopular Opinions
[2951.32 → 2952.04] What?
[2952.32 → 2954.02] I actually think she'll probably leave.
[2956.60 → 2959.08] Unpopular Opinions
[2959.08 → 2965.84] All right.
[2965.98 → 2966.62] All right.
[2966.78 → 2967.40] All right.
[2967.84 → 2970.86] So, let's go with Geronimo first.
[2971.30 → 2971.80] What you got?
[2972.44 → 2974.76] Mine is not a technical one.
[2974.76 → 2983.48] But during the pandemics, I started to see that a lot of developers started to upload photos
[2983.48 → 2988.08] of their working environment outside, in a garden, in a beach.
[2988.56 → 2989.86] For me, it's impossible.
[2990.06 → 2996.94] I don't know if it's just me or those photos are just illustrative, like when you see a hamburger
[2996.94 → 2997.34] ad.
[2998.44 → 3000.08] So, that will be.
[3000.32 → 3000.96] I don't know.
[3001.00 → 3001.72] It's just me.
[3002.04 → 3004.14] I mean, you've got a whole gym sitting there behind you.
[3004.14 → 3004.74] Yeah.
[3006.16 → 3010.96] Actually, this is related to what Bar is going to mention, probably.
[3011.42 → 3013.36] It's like, these people are just stuffing their faces.
[3014.00 → 3017.56] I mean, instead of a gym, they just put some flowers and gardens behind them.
[3017.80 → 3018.34] All right.
[3018.54 → 3024.18] But once I went outside with my colleagues from a previous job to eat something, and we
[3024.18 → 3027.84] actually had some kind of alert and had to act very quickly.
[3027.84 → 3031.06] And we sat somewhere just outside.
[3031.72 → 3037.60] And honestly, the lightning makes it impossible to do anything, to see anything on the laptop.
[3038.32 → 3040.88] So, I kind of agree with that.
[3041.42 → 3044.62] So, it's not that unpopular because I also agree.
[3044.90 → 3048.06] You have to have a good environment to do work.
[3048.06 → 3051.44] Maybe it's indoor, it's much better.
[3051.58 → 3053.50] But out there, it will be very hard.
[3053.88 → 3057.74] I feel like every person's unique in what they can and can't work with.
[3058.22 → 3060.24] Because some people love co-working spaces.
[3061.24 → 3064.96] And it's not that I hate them, but I would never want to go to one every day of the week.
[3065.42 → 3068.94] For me, I feel like I'd be less productive there were other people just thrive.
[3069.32 → 3071.16] And the same with coffee shops or any of that.
[3071.16 → 3073.26] I can't work in a coffee shop.
[3073.80 → 3076.14] And I don't know if it's my back or what.
[3076.24 → 3080.04] But if I'm working on my laptop all day when I'm looking down, it eventually hurts my neck.
[3080.12 → 3081.60] So, I have my monitor up higher and everything.
[3081.74 → 3084.46] And I'm like, I don't know how these people work all the time.
[3084.60 → 3087.44] Sure, I can do it occasionally, but I can't do it all the time.
[3088.14 → 3091.96] But I literally know people who go to coffee shops most days of the week.
[3092.34 → 3093.78] And I don't know how they do it.
[3094.14 → 3094.84] Somehow they do.
[3095.14 → 3096.64] So, what's your unpopular opinion, Bart?
[3096.64 → 3101.24] Okay, so my is also about exercise, maybe.
[3101.82 → 3109.42] Because I think that as IT in general, the mistake that we are doing is that we start limiting ourselves physically.
[3109.96 → 3111.58] Like you have monitor.
[3112.00 → 3115.54] So, you work mostly with a head and hands and nothing else.
[3115.78 → 3120.18] So, it's like the majority of your body is suspended while you work.
[3120.18 → 3126.94] And we are flesh and bones mostly when we take the percentage of ourselves.
[3127.82 → 3133.68] And what it means is that if you just shut down part of your body, the whole body will be less efficient.
[3134.04 → 3135.30] It's a waste of resources.
[3135.82 → 3137.26] Yeah, waste of resources.
[3137.40 → 3140.78] And I was thinking that we approach this all in the wrong way.
[3140.78 → 3146.96] So, why don't we, let's say, have a big keyboard when you can punch things, like use your muscles.
[3147.82 → 3149.76] And maybe it will increase your productivity.
[3150.36 → 3154.78] Just think about all these genius doctors in our movies.
[3154.78 → 3163.74] Movies, like they all, when they do something, they do this with shouting and waving hands and things like that.
[3164.14 → 3171.18] Even if we read histories about some inventions in the past, they were not done while sitting.
[3171.68 → 3176.72] Maybe they were, but some inventions were done when, let's say, running after someone.
[3176.72 → 3180.16] And I think we are just limiting ourselves.
[3180.42 → 3187.92] And why don't we learn things like doing studies, like, I don't know, discussing projects during the run.
[3188.24 → 3193.60] Or maybe swimming and solving computations in your head.
[3194.12 → 3196.48] Maybe this will increase our brain power.
[3197.04 → 3204.80] So, if I understand you correctly, you are suggesting the outside working environment, but without taking the computer with you.
[3204.80 → 3205.12] Yeah.
[3205.26 → 3206.44] It's like going to the beach.
[3206.96 → 3208.00] Without the computer.
[3208.42 → 3210.24] And running after random strangers.
[3211.20 → 3213.52] You are solving the problem that they have with lighting.
[3214.22 → 3222.86] If I understand it correctly, I assume he's saying that we should explore other ways of doing work that involve our body more, rather than, like, limiting ourselves to sitting at a keyboard.
[3223.12 → 3223.80] Yes, exactly.
[3224.08 → 3230.84] But if Jared wants to summarize this as, you should chase after people while you're coding, we can do that too.
[3231.66 → 3232.78] We can do that too.
[3232.78 → 3233.60] We can do that too.
[3235.22 → 3236.20] John, did you bring one?
[3236.20 → 3237.18] I did not.
[3237.54 → 3238.08] You did not.
[3238.24 → 3239.60] I can say I agree with Bart, though.
[3239.66 → 3241.92] Like, I like the idea of thinking about other ways.
[3242.06 → 3243.32] Johnny, you have a standing desk, don't you?
[3243.72 → 3244.08] Yes.
[3244.28 → 3247.96] Yeah, I can raise it up and take it back down when I need to.
[3247.96 → 3249.72] So I used one of those for a while.
[3250.08 → 3253.90] And basically what I found was that I didn't like changing my setup all the time.
[3253.90 → 3260.40] And because I have enough space in my house, what I ended up doing was just getting a desk that's always standing and putting a walking treadmill under it.
[3260.40 → 3264.24] And I found that depending on, like, you can't do everything with it.
[3264.24 → 3265.80] Like, it's hard sometimes to walk.
[3265.98 → 3272.54] Like, walking three miles an hour while coding is not easy because you stop to think, and you're, like, pulling away from your keyboard, and you're like, whoa, whoa, whoa.
[3273.16 → 3274.66] So you have to, like, keep yourself going.
[3274.66 → 3290.16] But where it is really useful is, like, if I'm watching talks from a conference or if I'm doing anything like that where I don't really need to type as much, or it's just light emails or something, I can sit there and actually, like, it allows me to sort of move my body while also thinking in a little different way.
[3290.68 → 3293.74] And it's an awesome way to get a break from just sitting through the day.
[3294.20 → 3299.38] But I think the unfortunate part is that most offices are, like, kind of limited on space.
[3299.40 → 3301.64] So it's not like you can throw everything you want in there.
[3302.02 → 3303.40] So it kind of limits that.
[3303.40 → 3308.84] But I do agree that it'd be nice to see people exploring more interactive ways to do this stuff.
[3309.54 → 3309.78] All right.
[3309.88 → 3310.26] All right.
[3310.32 → 3310.74] All right.
[3311.26 → 3311.78] That's good.
[3312.12 → 3318.44] I didn't bring an unpopular opinion, but I thought of one as we were having this little powwow.
[3318.80 → 3322.24] One thing we didn't get to talk about that I am going to do a show on.
[3322.38 → 3323.68] So that's the unpopular opinion.
[3324.18 → 3327.54] I'm doing a show on blockchain at some point in the future.
[3328.36 → 3328.66] That's it.
[3328.74 → 3329.66] That's the unpopular opinion.
[3331.56 → 3332.86] It's dangerous opinion.
[3332.86 → 3336.00] So your unpopular opinion is that you think you should do a blockchain show.
[3336.24 → 3336.92] Yeah, exactly.
[3337.02 → 3338.70] I think I need to do an episode on blockchain.
[3339.04 → 3340.64] But yeah, that's going to be unpopular.
[3341.30 → 3342.78] Yeah, it's brutal out there, man.
[3343.76 → 3347.42] I'm honestly curious if that's unpopular or just incredibly polarizing.
[3347.88 → 3350.28] Because there's definitely some people who agree with you doing a show on that.
[3350.58 → 3351.36] Like, I can't imagine.
[3351.84 → 3352.84] I don't know how many, though.
[3352.92 → 3353.12] Right.
[3353.12 → 3355.62] Well, I'm hoping folks won't shoot the messenger, right?
[3355.68 → 3356.46] I'm just the messenger.
[3356.46 → 3360.42] Look, I just don't want us to, you know, bury our heads in the sand and pretend this thing doesn't exist.
[3360.42 → 3362.70] Because clearly it pisses off a lot of people.
[3363.10 → 3365.42] So, you know, let's just talk about it, right?
[3365.44 → 3366.42] Like we do most things.
[3366.42 → 3367.40] Let's just talk about it.
[3367.48 → 3370.34] And, you know, if there are merits, we'll raise them.
[3370.46 → 3373.08] And if it's complete garbage, we'll show that too.
[3373.32 → 3375.08] So, yeah, we'll see how well that goes.
[3375.60 → 3378.40] I hope people don't boycott the show after that.
[3378.88 → 3380.44] But, yeah, we shall see.
[3380.52 → 3381.02] We shall see.
[3386.70 → 3388.58] That is go time for this week.
[3389.26 → 3390.16] Immutable databases.
[3390.68 → 3391.34] Your thoughts?
[3391.86 → 3393.56] Let us know in the comments.
[3394.02 → 3397.50] There's a direct link to the discussion thread at the top of your show notes.
[3397.50 → 3400.72] Everyone on this episode will be notified of what you have to say.
[3400.88 → 3405.72] So it's a great place for follow-ups, clarifications, links to related projects, stuff like that.
[3406.04 → 3407.86] If you're a first-time listener, welcome.
[3408.34 → 3410.96] Don't forget to subscribe at gotime.fm.
[3411.18 → 3413.12] We are also in your favourite podcast app.
[3413.30 → 3414.20] Just search for Go time.
[3414.20 → 3419.02] If this is your 10th listen, your 100th, your 1,000th, whatever order of magnitude you have with us,
[3419.14 → 3421.26] we'd love a review and recommendation.
[3421.82 → 3425.14] Special thanks to Vastly for CD ending for us all these years,
[3425.36 → 3427.26] to Break master Cylinder for the Fresh Beats,
[3427.50 → 3428.42] and to you for listening.
[3428.64 → 3429.42] We appreciate you.
[3429.82 → 3432.34] Next week, Matt and John are joined by Ed Welch
[3432.34 → 3434.58] to discuss logging, logging, and more logging.
[3435.00 → 3436.24] Yeah, a lot of logging going on there.
[3436.88 → 3439.88] That's one to look forward to next time on Go time.
[3439.88 → 3447.68] END
[3447.68 → 3447.90] STAN
[3447.90 → 3449.44] TO believe in heart
[3449.44 → 3450.34] STAN
[3450.34 → 3450.70] END
[3450.70 → 3451.28] Nine
