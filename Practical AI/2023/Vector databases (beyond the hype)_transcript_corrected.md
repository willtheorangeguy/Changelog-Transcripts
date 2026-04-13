[0.00 → 8.64] Welcome to Practical AI.
[9.20 → 15.96] If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 → 18.78] are changing the world, this is the show for you.
[19.20 → 24.36] Thank you to our partners at Vastly for shipping all of our pods superfast to wherever you
[24.36 → 24.66] listen.
[24.92 → 26.76] Check them out at Fastly.com.
[26.76 → 32.02] And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 → 33.70] No ops required.
[34.02 → 36.08] Learn more at fly.io.
[42.74 → 45.88] Welcome to another episode of Practical AI.
[46.20 → 47.80] This is Daniel Whiten ack.
[47.92 → 53.98] I am the founder of Prediction Guard, and I'm joined as always by my co-host, Chris Benson,
[53.98 → 56.56] who is a tech strategist at Lockheed Martin.
[56.76 → 57.78] How are you doing, Chris?
[58.06 → 59.20] Doing well today, Daniel.
[59.24 → 59.66] How are you?
[59.96 → 68.34] I am doing so good because a lot of my dreams are coming true in terms of topics to talk
[68.34 → 68.56] about.
[68.64 → 73.40] I've been wanting to talk about vector databases on the show for quite some time.
[73.54 → 77.48] I know that we've mentioned them, but we haven't had a full episode on them.
[77.48 → 85.26] And I was scrolling through LinkedIn and saw a set of amazing posts and very practical posts
[85.26 → 91.84] about vector databases that I quickly shared and also sent a message to Prashant Rao, who
[91.84 → 96.22] is a senior AI and data engineer at the Royal Bank of Canada.
[96.94 → 97.62] Welcome, Prashant.
[97.96 → 98.14] Hi.
[98.22 → 99.10] Thanks for having me.
[99.44 → 99.74] Yeah.
[99.74 → 99.82] Yeah.
[99.92 → 100.14] Yeah.
[100.14 → 107.24] Well, now you have a three-part series on vector databases, a three-part blog series.
[107.62 → 109.06] What makes each one different?
[109.56 → 113.44] Understanding their internals and not all indices are created equal.
[113.66 → 115.94] I hope we can get into a bunch of that.
[116.04 → 122.40] But maybe to start out, could you just let us know what a vector database is?
[122.52 → 125.64] And in particular, why are people talking about them now?
[125.64 → 126.38] For sure.
[126.58 → 131.74] So I think the way I want to answer this question is I'd like to break it down into parts and
[131.74 → 133.10] answer each bit sequentially.
[133.52 → 133.66] Great.
[134.00 → 139.06] So to answer what a vector database is, well, let's start with what data is in the first
[139.06 → 139.56] place, right?
[139.92 → 145.54] The definition in my head is data is an organized collection of structured or semi-structured
[145.54 → 148.24] information, and it's stored digitally in a computer.
[148.76 → 151.42] Now, when you have data, you need somewhere to put it.
[151.64 → 153.80] So that brings us to the question, what is a database?
[153.80 → 159.42] So a database is a system that's built for easy access, management, and updating, and
[159.42 → 160.82] also querying the data at hand.
[161.32 → 163.14] We also need to talk about what vectors are.
[163.66 → 169.92] Vectors, you could call them a sort of compressed data representation that contains semantic information
[169.92 → 171.20] about any underlying entity.
[171.36 → 174.26] It could be text, images, audio, anything like that.
[174.70 → 176.24] So now we put all of these things together.
[176.36 → 177.54] What is a vector database?
[177.54 → 184.60] A vector database is a purpose-built database that efficiently manages, stores, and updates
[184.60 → 185.72] vectors at scale.
[185.98 → 187.64] I think the scalability is a very key factor there.
[188.26 → 194.32] And it also retrieves the most similar vectors to a given query in a way that considers the
[194.32 → 195.32] semantics of the query.
[195.82 → 200.14] So I think all of these terms holistically come together to form what we understand as a
[200.14 → 200.72] vector database.
[200.72 → 207.90] And when you say semantics, what do you mean in terms of semantics and how that maps onto
[207.90 → 208.36] a vector?
[208.88 → 213.58] So I'm sure everyone, most listeners, are familiar with the concept of language models.
[214.10 → 214.78] NNMs are everywhere.
[215.06 → 219.68] So the thing with semantics is typically a query that you have.
[219.78 → 223.56] Like if you write a query to like a search bar on Google or something, you're thinking
[223.56 → 224.42] in terms of keywords.
[224.42 → 229.18] You're just thinking in terms of, okay, I want this particular thing, this item, whatever
[229.18 → 229.80] you're thinking about.
[230.12 → 231.46] And you type the word in there.
[232.00 → 237.82] Where semantics comes in is, did you type in something along the lines of what the data
[237.82 → 238.60] itself has?
[238.96 → 246.04] So can the query actually translate into something that the database actually understands and
[246.04 → 250.26] produces the result that is most meaningful to the query that you put in?
[250.58 → 253.24] So it's not just about the words or the features of that word.
[253.24 → 257.40] It's also about the meaning of that word and how that comes together in the underlying
[257.40 → 258.18] internal of the data.
[258.62 → 258.90] Cool.
[259.18 → 265.22] So before we keep going, just because you have developers and data scientists, and they've
[265.22 → 269.62] worked with kind of all the other database types that most of us have worked with for
[269.62 → 270.16] decades.
[270.78 → 275.38] And we have multiple times over the years had to kind of like understand the new thing
[275.38 → 277.44] that's out and what the value is.
[277.62 → 278.26] No SQL.
[278.70 → 279.20] There you go.
[279.32 → 281.46] And so like, I'm going to jump on that.
[281.46 → 287.38] You know, we started with the SQL query language with these that are for relational databases.
[287.76 → 293.74] And then we went to NoSQL, which there are variants of and things called object databases.
[294.12 → 300.50] I understood your definition of vector, but I didn't understand how it related to the utility
[300.50 → 302.94] or lack thereof in some of those other approaches.
[303.18 → 306.94] Could you kind of lay the groundwork or the landscape of what that is?
[307.12 → 307.74] For sure.
[307.74 → 310.04] So yeah, I mean, I'm a total database junkie.
[310.14 → 313.08] I love thinking about the various kinds of databases out there.
[313.78 → 317.66] So actually, before we go to that, a quick summary in terms of where I'm coming from,
[317.72 → 317.86] right?
[317.92 → 320.42] So I started off as a data scientist.
[320.74 → 322.10] So I'm fully in your world, Daniel.
[322.30 → 325.34] And it's been a few years down that road for me.
[325.34 → 331.44] And I think for me, I've hit that point where I've been lost in the world of models and hyperparameter
[331.44 → 333.86] tuning and absolute data scientists will relate with that.
[334.50 → 338.36] But the more I began thinking about it, there are people who have entire PhDs in database
[338.36 → 339.14] theory, right?
[339.16 → 339.88] And their implementation.
[340.64 → 345.94] But then the more I've worked with data, I realized that you don't need a PhD to understand
[345.94 → 348.94] enough to build a working application built on top of a database.
[348.94 → 353.52] Because that's when you began thinking about what exactly are these different flavours that
[353.52 → 354.26] you have out there, right?
[354.30 → 358.42] I mean, of course, we've all come across SQL databases at some point in our careers if
[358.42 → 359.10] we worked in tech.
[359.90 → 364.54] So to answer that question, I think the general history of how these things panned out is quite
[364.54 → 365.04] interesting.
[365.42 → 371.74] I believe the origins of SQL databases come from way back in the 70s, I think, when this
[371.74 → 373.90] field called relational algebra was formalized.
[373.90 → 380.06] It's a kind of like a formalization of the mathematics around what it means to join data,
[380.24 → 383.28] query data, store data in a database in a way that is quarriable.
[384.00 → 386.50] I think SQL databases are so mature, so tried and tested.
[386.60 → 391.12] And the reason they've withstood the test of time is because they view the underlying storage
[391.12 → 392.78] or the underlying data as structured.
[393.28 → 397.62] And in many cases, you have structured data that is in the form of transactions.
[398.46 → 402.08] And what a transaction basically means is some event happens in the real world and you
[402.08 → 406.62] log that information, and you essentially build up a sequential chain of data, which is basically
[406.62 → 406.98] a table.
[407.60 → 410.46] And that's kind of what the relational data model came from.
[411.08 → 415.36] And where relational models get interesting is you have tables that are related to other
[415.36 → 415.74] tables.
[416.36 → 423.64] And that kind of maps into real world complexities where not all data is independent.
[423.78 → 425.30] Like some of the data depends on other things.
[425.70 → 430.04] Like a person's metadata could depend on what company they work at and things like that.
[430.04 → 433.44] So that's how relational data kind of became the norm.
[433.68 → 437.20] People were gathering data from digital systems and then putting them together.
[437.72 → 442.18] And SQL became the sort of standardized query language that you could use to query data.
[442.48 → 446.56] Fast forward to mid 2000s and the NoSQL movement starts to pick up.
[447.14 → 452.98] And where that comes from is there's a point beyond which relational data modelling can become
[452.98 → 453.72] a bit inflexible.
[453.82 → 459.16] Like it becomes a bit rigid because in the real world, you have data that comes in from various
[459.16 → 459.58] sources.
[460.34 → 462.34] Now, some of that data can come in very rapidly.
[462.54 → 467.94] With the advent of big data and streaming and all these rapid ways of gathering data that
[467.94 → 472.74] we have today, it became very obvious that the schema-based approach, a schema is basically
[472.74 → 475.72] what kind of data types exist in your table, right?
[475.76 → 479.30] So the way relational models were built was you needed to define a schema.
[479.70 → 481.72] And the schema kind of was the ground truth.
[481.72 → 483.78] The data has this data of this type only.
[484.32 → 486.46] And that's what you expect in there all the time.
[486.46 → 492.52] I think the NoSQL movement sort of built on top of the limitations of the relational approach
[492.52 → 495.38] of being pre-decided by a schema.
[495.54 → 499.62] Because to be truly flexible in terms of the massive amounts of data coming in from various
[499.62 → 502.70] systems, you need to have a schema-less approach at times.
[503.32 → 508.46] And the schema-less approach basically means you store documents, you dump data in semi-structured
[508.46 → 511.06] JSON blobs and things like that in a scalable way.
[511.16 → 514.26] And I think horizontally scalable became very, very important in that period.
[514.26 → 519.50] The earlier databases that were relational, I think they were more vertically scalable in
[519.50 → 524.00] the sense that you could just add more and more compute, and you essentially scaled up your
[524.00 → 524.46] data that way.
[524.52 → 530.64] But now with NoSQL, the idea of distributing the data as documents across multiple machines
[530.64 → 534.02] and having those machines communicate with one another, that became a new paradigm.
[534.02 → 539.46] But I think the challenge with NoSQL is because of the underlying nature that the data need
[539.46 → 545.68] not necessarily be dependent on itself, like in the sense of relational tables, they didn't
[545.68 → 547.86] adhere to the SQL language standard.
[548.84 → 550.26] And they kind of diverged.
[550.70 → 555.06] MongoDB was among the first and there were many others that came after it using JSON-based
[555.06 → 555.70] query languages.
[555.70 → 559.84] So there was a big bifurcation, I guess, in, you could say, the database community when
[559.84 → 564.76] on one hand, you have SQL enthusiasts who swear by the declarative nature of SQL.
[565.12 → 570.12] And then you have the other community, NoSQL, who uses JSON essentially to query the database.
[570.62 → 575.12] They claim it was developer-friendly and JSON is a developer-friendly interface, language
[575.12 → 576.20] agnostic and so on.
[576.54 → 578.32] So in some ways, it does have its benefits.
[578.50 → 582.44] But then depending on your use case and depending on what you're trying to do, there are people
[582.44 → 586.00] will argue on both parades that SQL should be the only thing you should use or no SQL
[586.00 → 587.58] should be the only thing you should use and so on.
[588.08 → 592.08] So does that clarify aspects of both those camps before we move into the modern ones?
[592.60 → 593.02] It does.
[593.18 → 596.92] And then if you could distinguish as you go kind of how Vector is different from those
[596.92 → 600.92] others, that would be helpful for me, I know, and maybe some other folks in the audience.
[601.46 → 601.64] Yeah.
[601.72 → 609.46] And I think maybe one thing that I loved about your blog post is I see some of the players
[609.46 → 615.18] from the world that we just talked about represented within that landscape and then also some that
[615.18 → 618.82] I'm not familiar with or at least that I've seen only recently.
[619.56 → 626.98] And so you've got these different axes like Postgres, which is a SQL-based query language
[626.98 → 633.68] to a relational database, has some part to play in this vector database ecosystem.
[634.18 → 637.48] But then others which seem to have their own query language.
[637.48 → 641.34] So maybe you could also start to break down for us.
[641.44 → 646.16] So we want to store vectors in databases now to do this sort of semantic queries.
[646.62 → 653.50] Does that need to be stored in one or the other of these types of databases that you've talked
[653.50 → 654.90] about developed over time?
[654.90 → 656.72] Or how has that happened?
[656.72 → 661.80] And what are the sort of major categories of players in the vector database space?
[662.26 → 662.48] Absolutely.
[662.64 → 666.92] So I think before we get into the specifics of databases, I think to answer Chris's point,
[666.92 → 669.44] we definitely do need to talk about the evolution, right?
[669.80 → 674.40] I see that vector databases are a natural evolution of the NoSQL class of databases.
[674.82 → 679.66] If you imagine a Venn diagram, you have like a circle that represents SQL and the other circle
[679.66 → 680.44] represents NoSQL.
[680.86 → 682.08] You have an intersection.
[682.58 → 685.90] That intersection point, I believe they're called New SQL now.
[685.94 → 687.12] I'm not sure if you've come across that term.
[687.54 → 688.24] It's quite interesting.
[688.24 → 695.42] But New SQL, they technically use SQL-like languages, but they also claim horizontal scalability and
[695.42 → 697.98] a bunch of other things related to asset compliance and all the other things.
[698.10 → 700.74] So it marries the benefits of both SQL and NoSQL paradigms.
[701.12 → 703.30] I was thinking initially, where do I place vector databases?
[703.56 → 706.68] Does it go in that intersection or does it sit purely in the NoSQL camp?
[707.12 → 712.02] Then I imagine this as you extend that circle that has NoSQL, it becomes like a blob, like
[712.02 → 713.40] a Buddy amorphous blob.
[714.34 → 715.12] NoSQL is huge.
[715.12 → 720.02] And I think in my head, vector databases are like an extension to NoSQL.
[720.48 → 725.00] And why they came about to understand what vectors are and how they're stored in database,
[725.10 → 730.70] I think it's important to understand what search is and what essentially you're doing
[730.70 → 732.28] when you query a NoSQL database.
[732.88 → 738.82] So where it comes from is in the early days, I guess people were just submitting an exact
[738.82 → 742.26] query using a JSON sort of query language like how MongoDB has.
[742.26 → 748.28] And that query has to have all the terms or parameters in there that tell you what you
[748.28 → 749.70] want to fetch from the database, right?
[750.12 → 754.18] In a SQL world, it will be done with a declarative query in SQL, whereas in NoSQL, you typically
[754.18 → 754.80] do it in JSON.
[755.34 → 760.36] Over time, I think the idea of full text search became very important because I think everyone
[760.36 → 764.46] wants to be able to retrieve information from massive blobs of data sitting around.
[764.46 → 766.56] And how do you query that, right?
[766.60 → 769.88] If it's in a NoSQL sort of format, if it's not, you can't write a SQL query to retrieve
[769.88 → 770.06] it.
[770.12 → 771.20] How do you get that information?
[771.90 → 774.96] So the idea of a full text index came about.
[775.66 → 781.30] And what essentially that is, is it uses a concept of inverted indexes, inverted file indexes,
[781.32 → 786.20] sorry, where you consider the term frequencies of terms that appear in a certain document.
[786.20 → 790.94] And obviously the relative frequency of how often those terms exist in a document versus
[790.94 → 792.76] the entire data set.
[793.26 → 797.28] So you combine all those things together, similar to how DF IDF is in data science.
[797.56 → 802.24] There's an algorithm called BN25, which is the most popular inverted file index algorithm.
[802.62 → 805.36] It's the most commonly used one for full text search.
[805.82 → 809.22] So the early days of search involved, how do you scale that up?
[809.32 → 812.38] Because you have massive amounts of data, how do you build that index very, very efficiently?
[812.38 → 816.34] And then the querying interface sits on top of that.
[816.50 → 820.78] So you essentially submit a query saying, okay, I want so-and-so term in the keyword
[820.78 → 821.42] that you put in.
[822.04 → 827.78] And the inverted file index, the BN25 algorithm, it considers the words frequency, and it considers
[827.78 → 833.02] subword features and a bunch of other things to intelligently retrieve relevant documents
[833.02 → 837.10] that contain that term, while also throwing out, you know, useless words, stop words and
[837.10 → 837.64] things like that.
[838.00 → 840.08] So it was more of like a bag of words sort of a question.
[840.08 → 844.82] If you consider an NLP analogy, it's kind of like a bag of words way of approaching text.
[845.66 → 849.86] Now, fast-forward a few years, I think ever since the transformer revolution happened, people
[849.86 → 855.26] began observing the obvious power of transformers in encoding semantics, right?
[855.30 → 861.26] A transformer is way better at isolating meaningful terms in a document, especially when you're
[861.26 → 863.60] doing things like classification, retrieval, and so on.
[863.60 → 868.84] So how could you merge those benefits of a transformer with what you have in a database?
[869.44 → 873.94] So I think vector databases, the term got coined, I think, much later after transformers
[873.94 → 874.40] came about.
[874.72 → 878.52] It was mostly called search engines before that, a more generic term, I think a catch-all
[878.52 → 879.96] term for anything that involves search.
[879.96 → 886.10] But nowadays, I believe search engine refers to a more, like you consider semantics as a
[886.10 → 886.86] key component.
[887.62 → 889.82] So essentially, vectors are the only thing that can do that.
[889.96 → 897.40] So to really describe what a vector is, essentially, you have a language model, typically a transformer-based
[897.40 → 904.74] language model that you use to embed the representation of a sentence into tokens.
[904.74 → 907.38] And the representation is stored as a vector.
[908.02 → 911.44] The vector that you have, essentially, for a particular sentence, typically those are
[911.44 → 914.82] done using sentence transformers, which is the most common kind of model you use.
[915.30 → 919.60] That essentially embeds the entire semantics of that sentence in the vector.
[920.24 → 926.28] And then the way this scales up is you consider the context of each and every token in that
[926.28 → 931.48] vector in a way that when you submit a query, the semantics of the query are mapped to the
[931.48 → 935.14] vector in your database, and you can find a similarity between what you entered as a query
[935.14 → 936.40] and what exists in the data.
[937.20 → 943.16] So a vector is a very powerful way of, you could say, compressing the representation of meaning
[943.16 → 950.36] in a sentence or a document in a way that scales up numerically, and you can rapidly query that
[950.36 → 951.14] in a digital.
[956.84 → 959.08] This is a Changelog News break.
[959.08 → 965.76] We've talked about prompt injection quite a bit since ChatGPT ushered in the LLM era.
[966.42 → 971.92] In brief, that's where you handcraft a prompt that tricks a chatbot into not following its
[971.92 → 972.44] own rules.
[973.02 → 978.90] Well, new research has uncovered some new LLM attacks on the block which aren't exactly
[978.90 → 979.34] that.
[979.84 → 980.16] Quote,
[980.16 → 987.52] Large language models like ChatGPT, BARD, or CLAD undergo extensive fine-tuning to not produce
[987.52 → 990.70] harmful content in their responses to users' questions.
[991.32 → 996.58] Although several studies have demonstrated so-called jailbreaks, which are special queries
[996.58 → 1001.70] that can still induce unintended responses, these require a substantial amount of manual
[1001.70 → 1006.04] effort to design and often can easily be patched by LLM providers.
[1006.04 → 1011.00] This work studies the safety of such models in a more systematic fashion.
[1011.00 → 1016.24] We demonstrate that it is in fact possible to automatically construct adversarial attacks
[1016.24 → 1022.94] on LLMs, specifically chosen sequences of characters that, when appended to a user query,
[1023.14 → 1027.44] will cause the system to obey user commands even if it produces harmful content.
[1027.80 → 1028.24] End quote.
[1028.24 → 1033.62] The biggest difference here is that they're achieving the jailbreak in an entirely automated
[1033.62 → 1039.60] fashion, and they make a case for the possibility that such behaviour may never be fully patchable
[1039.60 → 1040.92] by LLM providers.
[1041.20 → 1042.30] Game over, man!
[1042.38 → 1043.20] It's game over!
[1043.68 → 1044.68] What are we going to do now?
[1044.98 → 1045.80] What are we going to do?
[1045.80 → 1051.40] You just heard one of our five top stories from Monday's Changelog News.
[1051.76 → 1056.30] Subscribe to the podcast to get all the week's top stories and pop your email address
[1056.30 → 1062.66] in at changelog.com slash news to also receive our free companion email with even more developer
[1062.66 → 1064.16] news worth your attention.
[1064.60 → 1068.06] Once again, that's changelog.com slash news.
[1068.06 → 1077.76] So, Prashant, you kind of alluded to this, and I think that explanation was amazing of how
[1077.76 → 1084.70] this vector-based semantic search really exploded around the time that transformers and large language
[1084.70 → 1085.48] models did.
[1085.48 → 1091.70] I think even in this past, let's say, year, there's been this huge explosion of interest
[1091.70 → 1093.48] in vector databases.
[1094.30 → 1096.84] Could you maybe describe a little bit?
[1096.84 → 1103.00] So, we know that you can search a vector database to find similar statements, let's say, or similar
[1103.00 → 1106.58] chunks of text where the similarity is based on semantics.
[1107.30 → 1112.48] How are people using them in regard to their AI workflows?
[1112.48 → 1119.40] And how does that kind of correspond to what's sort of popular right now in terms of what people
[1119.40 → 1120.54] are exploring with AI?
[1121.40 → 1125.88] So, yeah, I think I need to highlight the fact that I'm both fascinated and frustrated by the
[1125.88 → 1128.74] current state of marketing in vector databases, both at the same time.
[1129.18 → 1131.82] I'm genuinely interested in the use cases, don't get me wrong.
[1132.22 → 1138.54] When combined with LLNs, large language models, like ChatGPT, you could say any sort of language
[1138.54 → 1142.92] model layered on top of a vector database can be used to build some very, very interesting
[1142.92 → 1143.42] applications.
[1143.42 → 1148.62] One of those interesting applications is querying your data via natural language.
[1148.96 → 1151.86] I think this has always been a dream of data scientists and people who work with data,
[1151.96 → 1152.12] right?
[1152.16 → 1157.58] Rather than writing my query by hand or constructing the query painstakingly from the ground up,
[1157.86 → 1163.54] can I just talk in natural language and have the database kind of respond to that query
[1163.54 → 1164.64] in natural language as well?
[1165.00 → 1167.68] The application will be built using an NLM at the core.
[1167.68 → 1172.60] And essentially, that would be powering the whole translation of human instruction to machine
[1172.60 → 1174.06] instruction and back to human.
[1174.72 → 1176.96] I could go into the details of specific applications.
[1177.62 → 1182.42] But one thing I do want to really throw back at you is, I know this is a practical AI podcast,
[1182.54 → 1182.68] right?
[1182.72 → 1189.40] So I guess what I was hoping to get into is I have an idea for a fourth blog post and in
[1189.40 → 1190.02] the series, basically.
[1190.46 → 1192.66] Part of it is the trade-offs, right?
[1192.72 → 1197.16] What really interests me about the various vector databases out there and why I began writing
[1197.16 → 1203.06] about these at length is when it comes to understanding what tool to use in the real world, when you
[1203.06 → 1207.26] have a business problem, when you have a particular case you're trying to address, obviously, there's
[1207.26 → 1208.34] tons of information out there.
[1208.44 → 1212.72] You could go out and read a bunch of blogs and papers and come up with your trade-offs.
[1212.84 → 1217.12] But I think it makes sense to actually walk through some of these trade-offs.
[1217.42 → 1222.06] And my understanding is that as you go through these trade-offs, you actually begin formulating
[1222.06 → 1225.22] the value of these things much more clearly.
[1225.22 → 1229.62] And in my head, I think it makes sense to talk about the use cases once we go through
[1229.62 → 1230.62] some of these key trade-offs.
[1230.72 → 1234.94] Because in many ways, using a tool depends on what goes into it and what you thought about
[1234.94 → 1235.74] the different options.
[1236.14 → 1241.12] You can dive right in because, yeah, I had follow-ups, which were essentially what I think
[1241.12 → 1242.06] you were about to cover anyway.
[1242.22 → 1244.16] So I'll just leave the mic with you, man.
[1244.96 → 1245.28] Oh, sure.
[1245.36 → 1245.54] Yeah.
[1245.86 → 1248.86] So basically, it makes a lot of sense to write about this.
[1248.90 → 1250.42] I obviously read it at your own time.
[1250.86 → 1252.86] But this is a great place for me to begin talking about it.
[1252.86 → 1254.98] And eventually, I'll put these down in words as well.
[1255.56 → 1259.20] So I've broken these down into, I think, roughly eight categories.
[1259.58 → 1263.32] And the trade-offs, I'm specifically speaking about what do you need to think about when
[1263.32 → 1264.10] you're thinking about a database?
[1264.54 → 1266.94] And this will answer exactly what you talked about earlier, Daniel.
[1267.48 → 1273.26] So the first thing I think Daniel mentioned is the idea of deciding between existing databases
[1273.26 → 1278.82] that have been around document format and things like that versus newly designed databases
[1278.82 → 1279.96] specifically for vectors.
[1279.96 → 1286.00] So I'm going to call it purpose-built vendors versus incumbent or existing vendors.
[1286.00 → 1289.02] So I think it's very important to understand.
[1289.24 → 1294.94] In many cases, you might just be looking to add semantic search capability or just retrieving
[1294.94 → 1298.20] information using semantics on top of an existing application.
[1298.20 → 1303.56] And that existing application could very well be built on a well-known tried and tested solution
[1303.56 → 1305.92] like Elasticsearch, Postgres, and so on.
[1305.98 → 1307.18] There are many solutions out there.
[1308.12 → 1312.88] And obviously, in those cases, it makes sense to just say, hey, why can't I just leverage
[1312.88 → 1316.42] the vector index or the vector storage of that database itself?
[1316.42 → 1317.62] Like, for example, you mentioned Postgres.
[1318.46 → 1324.34] One real big concern with this is if you look at some of the material online on the performance
[1324.34 → 1330.08] of these, the methods of PG Vector, PG Vector is basically the vector plugin add-on to Postgres.
[1330.72 → 1332.84] And there's been enough documentation about this.
[1333.32 → 1338.24] But essentially, the way it's been slapped on to Postgres is as like an add-on.
[1338.52 → 1340.40] It's like built by a third party called Super base.
[1340.96 → 1344.88] And they add a vector functionality to the existing engine that Postgres has.
[1344.88 → 1350.46] So by its very nature, because it's not tightly integrated with the underlying internals of
[1350.46 → 1354.60] the database itself, like the storage layer, the indexing, and all of that, you're going
[1354.60 → 1355.86] to miss out on a lot of optimization.
[1356.04 → 1361.68] Not you, but the technology is basically not optimized from the ground up to speed of indexing,
[1361.84 → 1363.56] performance during querying, and so on.
[1363.90 → 1365.04] And this has been well documented.
[1365.48 → 1366.82] So that is a very big concern.
[1367.14 → 1371.44] Depending on your use case and how much accuracy and what quality of results you want, are you
[1371.44 → 1376.48] better off using an existing database that you already have in your stack or actually
[1376.48 → 1381.12] bringing on a new tried and tested purpose-built database for that very reason, right?
[1381.62 → 1386.38] And from my experience, I've been tinkering around with quite a few options out there with
[1386.38 → 1387.24] purpose-built vendors.
[1387.50 → 1392.60] In my opinion, they are always a better solution in terms of scalability, efficiency, and also
[1392.60 → 1396.06] accessing the latest technology, like the latest algorithms out there.
[1396.06 → 1397.94] What indexing algorithms are out there?
[1398.40 → 1403.30] How do they get the best bang for buck in terms of your speed of indexing, the quality
[1403.30 → 1406.32] of query results, the latency of those results, and so on?
[1406.38 → 1412.00] So I feel like in the long term, if you actually are serious about building a vector search or
[1412.00 → 1416.84] large-scale information retrieval system that considers semantics, it makes far more sense
[1416.84 → 1418.78] to think about a purpose-built solution.
[1419.16 → 1420.46] Many, many database solutions are out there.
[1420.50 → 1421.68] I've listed some of those on my blog.
[1421.68 → 1428.66] And I think those are going to win out over the incumbent vendors who have kind of built
[1428.66 → 1430.80] vector offerings, as you can call them.
[1431.44 → 1434.82] What we're talking about is exactly what I had hoped we would talk about in this episode
[1434.82 → 1437.62] because your blog posts were so practical.
[1437.98 → 1444.32] In terms of how you think about the infrastructure that you work with day-to-day, would you recommend,
[1444.78 → 1450.00] because sometimes you don't know how much you need to optimize at the beginning and you
[1450.00 → 1451.40] can over-optimize, right?
[1451.48 → 1457.08] So would it be a valid maybe stepping stone to say, if I'm already working with Postgres,
[1457.86 → 1460.68] I could try out the vector capability of that.
[1460.84 → 1466.06] And if it works for my use case and I don't have, you know, three million documents that
[1466.06 → 1468.62] I'm searching over, maybe it's fine.
[1468.72 → 1471.84] I just have a, you know, I'm doing my personal blog or something.
[1471.84 → 1478.52] And then kind of optimize as you hit a wall or is there danger in kind of trying to make
[1478.52 → 1484.48] that, put a square peg in a round hole sort of thing and get yourself in trouble?
[1485.12 → 1486.00] You hit the nail on the head.
[1486.12 → 1490.36] I was going to exactly say put a square peg in a round hole because I face those issues
[1490.36 → 1490.78] myself.
[1491.00 → 1496.72] I wouldn't name exact database vendors, but I work with SQL and NoSQL databases and which
[1496.72 → 1497.84] obviously have vector solutions.
[1497.84 → 1502.88] I think the challenge and the issue with saying that, okay, I already have something that works
[1502.88 → 1508.16] is you got to remember that every single database that has existed for, I think, more than 10
[1508.16 → 1513.98] years, databases come with baggage, and they have their own tech debt that is associated
[1513.98 → 1516.54] with the underlying programming language they're built on.
[1516.90 → 1521.36] There are years of decision-making and architectural decisions under the hood that they've taken
[1521.36 → 1523.22] to implement solutions the way they have.
[1523.22 → 1526.90] So they can't just throw all of that away and then build a vector solution that is optimized
[1526.90 → 1528.10] from day one, right?
[1528.14 → 1532.56] It's going to take a fair amount of time before these incumbent vendors are able to optimize
[1532.56 → 1536.72] their offerings to a point that perform as well as purpose-built vendors because these
[1536.72 → 1542.10] purpose-built vendors have spent thousands of manners, I guess, per offering in just tuning
[1542.10 → 1544.22] and building for a very specific goal.
[1544.62 → 1549.18] So what I've noticed in my experiments is that a lot of features that you take for granted
[1549.18 → 1552.56] in a purpose-built offering are not even available in the existing solution.
[1552.56 → 1555.98] PG vector is a very, very young solution right now.
[1556.52 → 1558.38] Elasticsearch is vector offering.
[1559.10 → 1560.34] I've worked with that as well.
[1560.68 → 1564.72] It is also, I mean, considering Elasticsearch has been around for so long, they only released
[1564.72 → 1568.78] their first vector ANN algorithm, I think, last year, like 2022.
[1569.30 → 1572.80] So in terms of a database's capabilities, that's very, very young.
[1573.06 → 1576.48] So I would say there are a lot of things that you could potentially be missing or lacking.
[1576.56 → 1579.86] And I'll cover some of those in my other trade-offs that I missed as we go forward.
[1579.86 → 1580.46] Yeah, yeah.
[1580.50 → 1581.50] Let's go on to those.
[1581.64 → 1583.36] I'm curious what number two is.
[1583.84 → 1584.20] For sure.
[1584.54 → 1588.54] The number two is, I came across this in my first blog and reading some of the comments
[1588.54 → 1589.04] on there.
[1589.20 → 1594.04] And one of them brought up this fact that the trade-off between using a database that
[1594.04 → 1601.60] allows you to build your own embedding pipeline versus using a built-in hosted sort of embedding
[1601.60 → 1601.94] pipeline.
[1602.04 → 1605.62] And by that, I mean, how do you generate these embeddings or these vectors, right?
[1606.08 → 1608.30] Many people are familiar with sentence transformers.
[1608.30 → 1611.36] It's available on Hugging Face and a bunch of other open source platforms.
[1611.56 → 1617.46] So essentially, it's quite easy, or you could say it's trivial, to put your data into these
[1617.46 → 1622.34] pipelines and generate sentence embeddings that you can just use to ingest into a database
[1622.34 → 1623.74] alongside your actual data.
[1623.82 → 1627.78] So you have your document data that has all the fields and attributes that you have in
[1627.78 → 1632.12] there alongside the vectors that encode the useful information in that you want to
[1632.12 → 1632.52] query on.
[1632.52 → 1634.76] So that's a relatively trivial thing to do.
[1635.16 → 1639.92] But there are certain database vendors who offer convenience features on top of that,
[1639.98 → 1643.42] where they embed the API of these models inside their own offering.
[1643.78 → 1648.10] So if you're just getting started, and you don't know much about how vectors work or how, you
[1648.10 → 1651.38] know, LLMs work or any of these things, that might be something to consider.
[1651.70 → 1656.52] You might be better off using something like VV8, which has pipelines built in where you can
[1656.52 → 1661.88] just tell it, OK, connect to Hugging Face so-and-so model, and it will build the embeddings for
[1661.88 → 1666.44] you, as opposed to you writing your own custom transformer pipeline that actually takes in
[1666.44 → 1668.18] the vectors, generates the vectors, and so on.
[1668.64 → 1673.78] Now, if you have experience with transformer models, you might be far better off in doing
[1673.78 → 1680.44] all the embedding work upstream, paralyzing, you know, and optimizing that portion, generating
[1680.44 → 1685.42] those at scale, and optimizing from a cost perspective, getting those done with the least
[1685.42 → 1689.82] resources and, you know, most quality that you can, and then just sending the vectors
[1689.82 → 1690.74] over to your database.
[1690.88 → 1694.66] So this is an important thing to consider, depending on the level of experience that
[1694.66 → 1698.38] your developers have in your team, to actually bring the vectors in.
[1698.86 → 1698.98] Gotcha.
[1699.12 → 1700.22] That makes perfect sense.
[1700.50 → 1701.80] What are some of the other trade-offs?
[1701.98 → 1706.40] So then the other thing is the two key stages, right?
[1706.50 → 1710.80] You could say you could break down when you use a vector database as a developer.
[1710.80 → 1715.38] The first stage is the input, which is essentially building the index, right?
[1715.80 → 1718.44] I go into the indexing methods in a bit more detail.
[1718.64 → 1719.58] That's not really a trade-off.
[1719.64 → 1722.00] It's more about knowing what the indexing even does under the hood.
[1722.40 → 1728.02] But what indexing means is you have data that you need to encode into a vector, right?
[1728.48 → 1733.02] Now, it's not as simple as just dumping a vector, which is like an array of numbers onto
[1733.02 → 1733.52] your database.
[1733.78 → 1736.24] You have to be able to search through those vectors.
[1736.24 → 1744.38] So the goal of indexing is to design efficient data structures and store the vectors using
[1744.38 → 1748.70] those efficient index data structures in a way that they can be queried efficiently
[1748.70 → 1749.36] and at scale.
[1749.58 → 1751.02] So that is an upstream process.
[1751.12 → 1752.40] You do that once upfront.
[1752.62 → 1753.88] You bring all your data in.
[1753.96 → 1754.70] It's indexed.
[1754.74 → 1756.72] And now you have a bunch of vectors in there that are searchable.
[1757.18 → 1759.62] The downstream portion of that is querying, right?
[1759.70 → 1761.48] It's basically like inference in NLP.
[1761.48 → 1767.08] The query stage involves you taking the user input, transforming that into a vector just
[1767.08 → 1768.34] like you did your raw data.
[1769.08 → 1772.64] And the vector embedding that you use there is an embedding model that you use to basically
[1772.64 → 1774.46] transform your data so that they are compatible.
[1775.00 → 1776.10] So that's a downstream step.
[1776.18 → 1779.78] You're clearly separating the indexing step from the query step, right?
[1780.04 → 1787.18] So the trade-off here is, is your database optimizing for indexing speed or query speed?
[1787.44 → 1790.28] Or is it mature enough that it has optimized for both?
[1790.28 → 1795.18] And if you look through all the offerings out there, many of the existing vendors have
[1795.18 → 1798.54] focused more on one end of the pipeline and not so much on the other.
[1798.66 → 1802.42] Some of them are faster at indexing and not so much at querying, but some of them are way
[1802.42 → 1804.64] better at querying and much, much slower during indexing.
[1804.82 → 1809.76] So generating that index actually can be a very expensive step because it's not only about
[1809.76 → 1811.80] using a sentence embedding model or a transformer.
[1812.22 → 1818.30] It's also about the database being able to translate those vectors into an index, and it can actually
[1818.30 → 1818.54] query.
[1818.54 → 1821.88] So depending on the size of your data, this could take hours or even days.
[1822.14 → 1826.66] Like it's not unheard of here of indexing the periods of the order of days.
[1827.36 → 1831.46] And of course, depending on the amount of money you're throwing at it, you could use GPUs
[1831.46 → 1836.60] to speed up the vectorization and use multiple parallel instances of the database to scale
[1836.60 → 1837.28] that portion up.
[1837.66 → 1838.42] But that's exactly it.
[1838.44 → 1841.32] The trade-off here is how important is indexing speed?
[1841.32 → 1846.10] If your data is coming in a stream at a very rapid rate, it's important to consider
[1846.10 → 1847.82] indexing speed as an important criterion.
[1848.00 → 1852.96] But then if you're not so interested in dumping large amounts of data very quickly, but more
[1852.96 → 1858.62] interested in serving results to a very large number of users asynchronously, then query
[1858.62 → 1859.68] speed becomes very, very important.
[1859.68 → 1866.04] I know we don't want to necessarily call out certain players in this space, but I think
[1866.04 → 1869.48] a lot of people are already familiar with a lot of the names here.
[1869.72 → 1875.24] So maybe if you could just highlight from your perspective, what are maybe some of the ones
[1875.24 → 1879.86] that are maybe more, like you were saying, mature in how they're thinking about both of
[1879.86 → 1880.52] those phases?
[1880.52 → 1886.08] Whereas maybe certain ones that are optimizing more on one side or the other, which like
[1886.08 → 1890.74] you said, depending on your use case is going to be a good thing, or it might be a bad thing.
[1890.90 → 1892.32] So it's really about use case.
[1892.44 → 1898.56] It's not so much about the goodness or how amazing a certain offering is, but more about
[1898.56 → 1899.08] use case.
[1899.64 → 1900.00] Yeah, absolutely.
[1900.14 → 1901.80] So as you say, I'm not going to call out specific.
[1901.94 → 1905.00] I mean, to be fair, everyone, every vendor makes trade-offs, right?
[1905.04 → 1908.76] They themselves are obviously juggling a lot of their own trade-offs when they build these
[1908.76 → 1912.54] things, but I obviously haven't used every single one out there.
[1912.98 → 1917.94] But the ones I have worked with, the most mature ones, I think Miles is an open source
[1917.94 → 1919.44] purpose-built database.
[1919.60 → 1922.90] It's been around the longest, among the longest, I think, in the vector database market.
[1923.50 → 1924.74] It's extremely scalable.
[1925.10 → 1929.94] I mean, I like to think, I've written on my blog, I call it Miles throws the kitchen
[1929.94 → 1932.22] sink and the refrigerator at the vector problem.
[1932.68 → 1935.66] So it can really handle like billions of data points.
[1935.78 → 1937.52] I mean, it's designed for that.
[1937.52 → 1938.70] And obviously, it has had time.
[1938.82 → 1940.26] It's been around for over four or five years.
[1940.62 → 1942.80] I wouldn't say that that would be my go-to first choice.
[1943.24 → 1945.06] That's my own personal preference, to be honest.
[1945.14 → 1949.80] It's more about, I guess, usability, how accessible their Python client is and so on.
[1950.18 → 1954.42] Then other vendors like VBN and Quadrant, I think they're also very, very optimized for
[1954.42 → 1954.76] this reason.
[1954.90 → 1957.56] So you could say that these are very, very powerful solutions.
[1957.78 → 1958.76] They scale really well.
[1958.88 → 1960.02] They ingest data really quickly.
[1960.02 → 1963.94] And they also supply query results very quickly and relatively accurately as well.
[1963.94 → 1969.56] To be fair, I think the existing database vendors like Elasticsearch, Postgres, they're not there
[1969.56 → 1971.02] yet in terms of the speed.
[1971.36 → 1973.78] And that's partly because they're general purpose databases.
[1973.92 → 1975.38] They're not specialized vector databases.
[1975.70 → 1979.96] So it makes sense that they have to deal with other priorities, and they cannot optimize for
[1979.96 → 1983.84] all of these things with the laser focus that purpose-based vendors have.
[1983.84 → 1990.12] Thank you so much, Prashant, for helping us start to pick apart some of these trade-offs.
[1990.34 → 1996.44] And I'm starting to structure things in my mind in a useful way, which is really great
[1996.44 → 1999.32] because I've also been exploring a lot of these.
[1999.42 → 2000.12] And I agree with you.
[2000.24 → 2006.30] There are a lot of also new entrants into the field that show a lot of promise, even the
[2006.30 → 2007.96] ones that aren't quite as mature yet.
[2008.38 → 2009.32] What are some of the other?
[2009.48 → 2010.38] You mentioned eight.
[2010.52 → 2012.98] I think, I don't know if we've been through three or four yet.
[2012.98 → 2014.78] I wasn't keeping track.
[2014.94 → 2016.62] I might have to speed things up a bit.
[2016.70 → 2018.06] Just kind of list them off at least.
[2018.18 → 2018.34] Yeah.
[2018.48 → 2018.64] Okay.
[2018.70 → 2022.24] So maybe I'll quickly go through at a high level, then we can go into the finer details
[2022.24 → 2023.76] of which ones you think are the most interesting.
[2023.84 → 2023.94] Yeah.
[2024.28 → 2024.82] So, okay.
[2024.86 → 2026.28] Let me summarize the first three.
[2026.76 → 2030.44] It's basically purpose-built versus existing solution, right?
[2030.48 → 2030.98] That's number one.
[2031.46 → 2036.00] Number two was external embedding pipeline versus built-in hosting pipeline.
[2036.44 → 2039.58] Number three is indexing speed versus querying speed.
[2039.58 → 2044.78] So I think the others are going more into the actual indexes and generation of those indexes
[2044.78 → 2045.66] in more detail.
[2046.10 → 2046.78] So I'll go through them.
[2046.90 → 2049.30] Number four is recall versus latency.
[2049.68 → 2053.86] That's more related to how accurate are the results versus how fast I'm at retrieving
[2053.86 → 2054.42] those results.
[2055.18 → 2058.96] Number five is in-memory index versus on-disk index.
[2058.96 → 2060.82] I think this is a very big one for the future.
[2061.08 → 2063.40] So we definitely want to go into, I think, some of the details of that.
[2063.40 → 2069.92] Number six is sparse versus dense vectors, the kind of vectors themselves that are underlying
[2069.92 → 2070.78] the index.
[2071.28 → 2077.20] Number seven is the importance of hybrid search, where it's full-text search combined with vector
[2077.20 → 2077.52] search.
[2077.76 → 2078.96] They both have their own trade-offs.
[2079.92 → 2083.34] And I think the last one is the importance of filtering.
[2083.52 → 2088.28] So pre-filtering versus post-filtering to decide the quality of your search result.
[2088.28 → 2093.88] Yeah, I am very curious about this in-memory or on-disk one.
[2094.04 → 2098.16] Well, I'm interested in all of them, but I know one of the things that has come up in
[2098.16 → 2104.96] several of the applications that I've worked on has been, okay, do we self-host one of
[2104.96 → 2105.84] these things?
[2106.00 → 2110.72] Do we use the managed service because they're going to be able to scale up and optimize things?
[2110.82 → 2117.70] There's also the choice of, oh, well, I could just load one in memory, on the fly, ephemerally,
[2117.70 → 2118.14] right?
[2118.24 → 2123.00] I could have an embedded case where I load a bunch of vectors in, and then there's some
[2123.00 → 2126.36] persistent file that I can pass around, right?
[2126.44 → 2131.54] And then there's, I think, more of what you were getting at, which is like, is this index
[2131.54 → 2133.60] represented on disk or in memory?
[2134.10 → 2138.60] Could you maybe help us parse through some of those things and go into a little bit more
[2138.60 → 2140.00] detail of what you mean there?
[2140.36 → 2144.74] So yeah, now that you mentioned self-hosted versus cloud, I think that's a number nine that
[2144.74 → 2145.42] I will add eventually.
[2145.80 → 2147.18] That's a very good point that you brought that up.
[2147.18 → 2147.46] Perfect.
[2147.46 → 2147.78] Yeah.
[2147.92 → 2151.60] Maybe we can find a number 10 to round it out before the end of the episode.
[2151.74 → 2152.60] I'm sure there's way more.
[2152.72 → 2152.82] Yeah.
[2152.96 → 2153.86] I could go on all day.
[2153.94 → 2154.20] But yeah.
[2154.54 → 2156.80] So yeah, going back to your in-memory, I think it's a very important one.
[2156.92 → 2161.98] So I think this is one of the things that is defining the you would call it the race
[2161.98 → 2163.54] towards vector supremacy.
[2164.20 → 2165.64] I don't think the term is very accurate.
[2165.78 → 2170.54] But anyway, I think the challenge with most of the vector indexes out there, I think the
[2170.54 → 2175.12] most popular one by far is called HNSW, hierarchical navigable small world graphs.
[2175.12 → 2178.66] And I go into the details of the algorithm in part three of my blog.
[2178.76 → 2182.80] So I'd be happy to, I mean, discuss more with anyone else outside of this if required.
[2182.96 → 2189.58] But HNSW index is known for its relatively good trade-off between recall and latency.
[2189.58 → 2191.38] It's fast, and it's relatively accurate.
[2191.38 → 2193.40] But it is also memory hungry.
[2194.22 → 2199.34] And where this becomes an issue is as data sets get larger and larger and larger, this
[2199.34 → 2201.18] is called the trillion scale vector problem now.
[2201.28 → 2202.70] A lot of vendors are talking about it.
[2203.04 → 2206.92] It's not too far away to imagine that you're going to have to, at one day, at one point,
[2207.08 → 2208.36] index a trillion vectors.
[2209.02 → 2210.74] And that is by no means a mean feat, right?
[2210.76 → 2212.12] It's a very challenging problem.
[2212.12 → 2217.14] So the data set in that situation would be way too large to fit in memory.
[2217.30 → 2220.84] Now, HNSW already does a lot of optimizations under the hood.
[2221.24 → 2225.02] The algorithm is designed to store a sparse graph in memory.
[2225.78 → 2229.10] And essentially, you search through the sparse graph and then through the layers of that graph,
[2229.22 → 2232.66] you narrow down on the nearest neighbour to the query that you input.
[2233.16 → 2237.50] But as we go and get larger and larger in terms of data, even that sparse graph does not
[2237.50 → 2238.00] fit in memory.
[2238.00 → 2238.04] Right.
[2238.44 → 2242.68] So databases have come up with different solutions as to how to deal with this out of memory
[2242.68 → 2243.02] issue.
[2243.46 → 2244.62] One example would be Quadrant.
[2244.74 → 2246.12] They use this thing called Emma.
[2246.40 → 2250.94] It's like a sort of static RAM option where you don't actually store the vectors in memory,
[2251.04 → 2252.52] but you persist it to the page cache.
[2253.08 → 2257.50] And it's still better than directly loading, storing it on solid state drive, which is one
[2257.50 → 2257.96] level below.
[2258.42 → 2258.56] Right.
[2258.64 → 2262.14] So in terms of latency hit, it's not as bad.
[2262.26 → 2263.52] So you don't lose that much performance.
[2263.52 → 2270.20] And you'll notice that a lot of vendors fight really hard to avoid persisting any vectors
[2270.20 → 2271.42] or the index to disk.
[2271.54 → 2275.44] Because the moment you go onto a solid state drive, there is a massive performance hit
[2275.44 → 2276.40] in terms of retrieval.
[2276.70 → 2280.16] Because the speed at which you're able to retrieve things from memory is, as you know,
[2280.24 → 2282.66] much, much, much faster than what you could do on disk.
[2283.16 → 2285.34] That's a general trend, I think, across the board right now.
[2285.48 → 2291.48] Most vendors are largely working with storing the HNSW index in memory and then adding some
[2291.48 → 2295.46] sort of caching layer to avoid having to repeat the queries and waste time in that sense.
[2295.58 → 2298.38] But this is entirely new index called Va mana.
[2298.60 → 2299.90] So I've written about that in that log.
[2300.24 → 2303.30] It's optimized for solid state disk retrievals.
[2303.70 → 2306.08] And the algorithm they use is called disk ANN.
[2306.46 → 2308.62] Not every database vendor has implemented this.
[2308.68 → 2309.66] It's still in the early days.
[2310.02 → 2313.84] But if I look at where the future is going, there are many options that vendors could go
[2313.84 → 2314.86] down the road of, right?
[2314.86 → 2318.44] They could choose to implement HNSW on disk.
[2318.44 → 2322.78] But record suggests that that's not a great idea because its performance would drastically
[2322.78 → 2323.28] reduce.
[2323.62 → 2325.40] It would not perform that quickly as it does.
[2326.20 → 2329.36] Disk ANN seems to be the agreed upon standard across many vendors.
[2329.64 → 2334.32] But the challenge of disk ANN is the original research paper that implemented it, the Microsoft
[2334.32 → 2338.68] team that implemented it, their implementation does not directly translate into the database
[2338.68 → 2339.26] internals.
[2339.56 → 2342.94] Depending on the language that the database uses, many of these are written in Go or RAP.
[2343.54 → 2345.28] Disk ANN implementation was written in C++.
[2345.28 → 2350.82] So it's not a direct transplant of the algorithm from the source to the database.
[2351.24 → 2356.38] It required a lot of rewrites and a custom approach towards optimizing for that speed.
[2356.72 → 2360.26] But that being said, I have to point out one particular vendor that I think really stands
[2360.26 → 2361.98] out from everyone else on this front.
[2362.20 → 2363.26] They're called Lance DD.
[2363.70 → 2365.86] They're, I believe, the youngest database out there.
[2366.08 → 2369.66] They just come about, I think, end of 2022, early 2023.
[2369.66 → 2375.96] And they are the only solution, as far as I know who only support on-disk indexes.
[2376.14 → 2377.82] They don't do an in-memory index at all.
[2378.34 → 2380.70] And I was initially very surprised as to how they even do this.
[2380.72 → 2381.68] How can they go about this?
[2382.08 → 2385.52] But as I dug into it, and I've spoken to some of the team as well, they're really, really
[2385.52 → 2388.72] open about their research that they're doing and all the models that they're building.
[2388.72 → 2392.80] But essentially, they innovate on multiple fronts.
[2392.98 → 2395.98] But the biggest innovation is the underlying storage layer, the storage format.
[2396.42 → 2402.76] They built this format called Lance, which is essentially optimized for on-disk reads of
[2402.76 → 2403.02] data.
[2403.42 → 2406.88] And the database itself is built on top of this open-source format, Lance.
[2407.00 → 2408.08] So the whole thing is open-source.
[2408.46 → 2409.34] It's built in Rust.
[2409.76 → 2412.30] So the performance there is already close to bare metal.
[2412.44 → 2413.28] It's really, really fast.
[2413.72 → 2416.28] They have already built an experimental disk in an implementation.
[2416.28 → 2421.92] So when it comes to this on-disk versus in-memory trade-offs, Quadrant is going about their
[2421.92 → 2425.34] own path in terms of how they achieve on-disk larger-than-memory data.
[2425.88 → 2427.28] VV8 is going around its own path.
[2427.48 → 2428.94] Lanced is innovating on a different front.
[2429.30 → 2432.84] I feel like these are the three vendors who I've interacted with more and used.
[2433.24 → 2438.98] And I think the future is heading towards one where on-disk becomes a requirement and
[2438.98 → 2440.74] a standard way of implementing an index.
[2441.26 → 2442.94] But the engineering challenges are still ongoing.
[2443.48 → 2445.48] Let me ask you a slightly different question.
[2445.48 → 2446.98] It's not completely unrelated.
[2447.60 → 2452.04] The things that you've been kind of addressing there kind of are leading me to the next step
[2452.04 → 2452.50] on that.
[2453.18 → 2457.44] So when you're thinking about kind of environments that you want to put in, like I know if you
[2457.44 → 2463.24] look at the other database types before Vector, you would have some that are scaled massively
[2463.24 → 2464.32] in the cloud.
[2464.50 → 2470.56] You'd have others as we've moved more and more intelligence and data out onto edge devices.
[2470.56 → 2475.68] And they're either embedded or they're designed to serve in a very constrained environment.
[2476.12 → 2479.42] What are the options for vector databases in that?
[2479.52 → 2483.66] I'm assuming that there's obviously the cloud capability because that's kind of always the
[2483.66 → 2484.10] baseline.
[2484.10 → 2490.52] Do you also have, you know, as we're moving into an increasingly autonomous world out there
[2490.52 → 2494.94] and more and more things are being pushed out outside the data centres in the clouds,
[2495.10 → 2500.90] or at least the central parts of the clouds, are there options for either embedded or micro
[2500.90 → 2503.78] serving, if you will, on the vector side?
[2503.78 → 2505.20] Yeah, that's an amazing point.
[2505.32 → 2505.44] Yeah.
[2505.58 → 2509.98] And I covered this in my blog post number one, in terms of the architectures of these databases.
[2509.98 → 2510.90] And you're absolutely right.
[2511.02 → 2515.68] I think there is a lot of room for embedded databases to become the norm.
[2515.80 → 2519.18] I know Duck DB is making waves in the SQL market on this front.
[2519.28 → 2522.98] I think a lot of vendors are emulating what Duck DB has done in SQL.
[2523.54 → 2528.02] As you know, Duck DB is an embedded database, unlike Postgres, which is a client server architecture
[2528.02 → 2528.54] database, right?
[2528.62 → 2532.68] So what happened in the SQL world is now translating into, you could say, the vector world.
[2532.68 → 2538.20] Two databases that are following this embedded approach, Lanced, as I mentioned, and Chroma DB.
[2538.68 → 2540.22] These are the most, Chroma DB is quite well-known.
[2540.36 → 2541.74] People have been talking about it for a while.
[2542.14 → 2546.72] But between the two of these, I do think that Lanced has, it stands out more in the underlying
[2546.72 → 2550.86] technology because the Chroma, from what I understand right now, is it's still building
[2550.86 → 2552.14] out its underlying layer.
[2552.30 → 2556.40] It was kind of wrapped around an existing underlying internal database itself.
[2556.54 → 2560.26] It was not, it did have its own purpose-built offering to begin with, but they're kind of
[2560.26 → 2561.42] building that out as they speak.
[2561.42 → 2565.78] So I think between these two vendors, it'll be interesting to see how, you know, each
[2565.78 → 2569.40] of them rolls out their own features, a kind of target-specific part of the market.
[2569.64 → 2573.68] Going back to the point of cloud versus on-prem, that's another big thing I think that's going
[2573.68 → 2574.18] to come up.
[2574.42 → 2579.10] Honestly, like Pine cone and services like that, that are completely on cloud, there are, they
[2579.10 → 2583.76] could be real potential bottlenecks for companies to be okay with just, you know, sending out
[2583.76 → 2584.60] their data to some cloud.
[2584.84 → 2588.64] Even if Pine cone says they would deploy on your infrastructure, at the end of the day, it
[2588.64 → 2590.02] is still a purely cloud-based solution.
[2590.50 → 2592.90] There are a lot of infrastructure-related hurdles around that.
[2593.44 → 2596.10] Self-hosted is, I think, as you said, going to become more and more common.
[2596.32 → 2600.98] And certain options, like VV8 Quadrant, they offer self-hosted options in their licensing
[2600.98 → 2601.32] as well.
[2601.42 → 2607.20] So the question for me that remains unanswered is, which model in Vector's database, Vector's
[2607.20 → 2609.18] search, will dominate in the longer term?
[2609.72 → 2611.54] Embedded versus client-server, right?
[2611.54 → 2615.76] We are so used to the model of client-server that's been working for more than a decade
[2615.76 → 2616.26] right now.
[2616.72 → 2620.40] Pretty much every database we've used is based on the client-server architecture, where
[2620.40 → 2624.34] the server sits remotely, and I don't have to have the server running anywhere near where
[2624.34 → 2625.24] my application is running.
[2625.82 → 2630.58] But I think embedded databases, especially with LLMs in the picture, it makes a lot of
[2630.58 → 2632.64] sense in terms of data privacy and things like that.
[2632.96 → 2636.76] And the scalability of these have, I guess, not truly been tested.
[2637.04 → 2638.58] WDB is just three or four years old.
[2638.90 → 2640.10] Advanced DB is less than a year old.
[2640.10 → 2640.74] And CLOVA as well.
[2641.28 → 2646.10] So it'll be interesting to see how embedded databases compete on that front, like how
[2646.10 → 2650.72] well adopted they are, because I think industry generally tends to favour things that are tried
[2650.72 → 2651.14] and tested.
[2651.58 → 2655.50] At scale, this sort of thing to catch on, it would have to offer real, real business value.
[2655.94 → 2659.86] And the way these databases monetize their offering, I think that's going to be interesting
[2659.86 → 2660.22] to see.
[2661.06 → 2664.46] And I guess we've already started moving this direction a little bit.
[2664.46 → 2672.76] But as we draw closer to an end here, I'm curious, you have explored probably more than,
[2673.46 → 2679.46] well, many people, certainly myself, in terms of how all of these offerings compare, what
[2679.46 → 2682.34] the tradeoffs are related to vector databases.
[2682.34 → 2689.66] I'm curious, as you look towards the future, what are you excited to try that you haven't
[2689.66 → 2690.44] yet tried?
[2690.68 → 2694.94] And then maybe what excites you about this space?
[2695.02 → 2699.56] I know you mentioned, certainly there are things that are hyped or maybe different marketing
[2699.56 → 2700.62] that plays into this.
[2700.68 → 2706.00] But what are you actually practically excited about as a practitioner in the future of this
[2706.00 → 2707.86] vector database space?
[2707.86 → 2710.80] I think the low-hanging fruit is the immediately obvious one.
[2710.88 → 2711.72] So I'll start with that.
[2711.90 → 2717.40] I think in the past, when it came to search, we imagine the Google search bar and idea that
[2717.40 → 2720.44] to build something like that was inconceivable a few years ago.
[2720.66 → 2725.88] Having a scalable, reliable search engine that you could build in-house on your own proprietary
[2725.88 → 2728.20] data was really, really difficult to do at scale.
[2728.74 → 2734.96] But today, I think with the combination of vector databases and LLMs, with GPT-4 now and
[2734.96 → 2739.94] all the other models out there, I really think that it's kind of become available to the masses.
[2740.18 → 2746.06] The average company who does not have massive compute is still able to build very, very valuable
[2746.06 → 2750.34] search solutions, information retrieval solutions on top of their existing data.
[2750.78 → 2755.54] There are additional offerings like Haystack and their search engines that build on top of
[2755.54 → 2756.04] vector databases.
[2756.16 → 2761.10] But I think the foundation layer are actually being enabled by vector databases, which is why
[2761.10 → 2762.96] I'm so interested in those use cases.
[2762.96 → 2765.84] So those applications are very interesting at first.
[2766.18 → 2768.76] The other thing is retrieval augmented generation.
[2768.94 → 2772.14] This is a term that came about, I think it was introduced by Meta in one of the recent
[2772.14 → 2772.48] papers.
[2773.00 → 2778.26] Essentially, the idea behind retrieval augmented generation is typically information retrieval
[2778.26 → 2778.68] involved.
[2778.90 → 2783.20] You send a query, and you receive a response that retrieves information relevant to your query,
[2783.42 → 2783.60] right?
[2784.10 → 2788.28] Where the generation comes in is now LLMs add a layer on top of that.
[2788.28 → 2794.80] You could send a query in natural language, and you retrieve the most similar documents
[2794.80 → 2796.34] to that query, right?
[2796.84 → 2801.46] But rather than just retrieving the document itself, you could have the language model go
[2801.46 → 2806.42] through the document, look at your query, and then retrieve only the part of the document
[2806.42 → 2807.56] that is relevant to that query.
[2807.66 → 2812.18] And then generate a response that could potentially answer a question that you had.
[2812.18 → 2816.68] Like, what is the birthday of so-and-so person who runs this company, right?
[2817.20 → 2821.98] So these kinds of things were really, really almost impossible to do before.
[2822.16 → 2826.12] But now I think it's really actually achievable with the kinds of tools and technologies that
[2826.12 → 2826.72] are available today.
[2827.28 → 2830.88] I think retrieval augmented generation is really skyrocketing right now as a term.
[2831.00 → 2832.14] I think everyone's talking about it.
[2832.28 → 2836.24] But what I want to add to that is I want to throw this out here to any of the listeners
[2836.24 → 2840.14] and maybe potentially I'm going to talk about this to other people in industry as well.
[2840.14 → 2843.82] Can we add another layer to retrieval augmented generation?
[2844.42 → 2849.54] And what I'm really interested in is how the two worlds of graph databases and vector
[2849.54 → 2850.90] databases come together.
[2851.10 → 2852.78] And I've posted about this a couple of times.
[2852.96 → 2858.16] But what's fascinating right now is most graph databases, like Neo4j, for example,
[2858.70 → 2861.58] they use declarative query language interfaces like Cypher.
[2861.66 → 2864.06] Cypher is, you could say, the SQL equivalent for graphs.
[2864.60 → 2868.00] The good thing about knowledge graphs is they encode factual information.
[2868.00 → 2870.34] And in a very human interpretable way.
[2870.52 → 2875.02] So the things that form nodes and edges in knowledge graph, they are something that we
[2875.02 → 2879.92] as humans put in there and encoded our knowledge of the real world into the data.
[2880.08 → 2885.40] Where vector databases sit complementary to this is, in many cases, I might have connected
[2885.40 → 2889.14] data where, let's say, a person knows another person, like a social network situation.
[2889.34 → 2890.42] A person follows another person.
[2890.54 → 2891.44] A person lives in a city.
[2891.44 → 2892.14] And so on.
[2892.64 → 2896.16] These are all meaningful, connected entities in the real world.
[2896.60 → 2899.30] But you add some layers of data on top of this.
[2899.64 → 2901.56] You know data about a city.
[2901.74 → 2902.76] You know data about a person.
[2903.00 → 2903.84] You know where they worked.
[2904.14 → 2906.20] You know what company information that has.
[2906.58 → 2913.58] Like, there's so much additional unstructured data that attach onto the node in a graph that
[2913.58 → 2917.98] is actually hard to query using conventional graph algorithms or graph languages.
[2917.98 → 2924.44] So I think vector databases are uniquely placed to add new value in that space in terms of,
[2924.76 → 2926.54] I call it factual knowledge retrieval.
[2926.82 → 2931.38] Now, the problem with knowledge retrieval is sometimes the queries that you have need
[2931.38 → 2931.92] to be exact.
[2932.34 → 2936.90] The ability to submit a fuzzy query that does not exactly match your terms in the graph is
[2936.90 → 2937.94] something that you didn't have before.
[2938.02 → 2942.98] It's very difficult to actually generalize your query in a way that retrieves useful information.
[2942.98 → 2949.04] So I'm very interested to see how the power of natural language querying interfaces enabled
[2949.04 → 2954.98] by LNMs can be built on top of vector databases that store all the information related to an entity
[2954.98 → 2957.82] and then encode that entity into a knowledge graph.
[2958.32 → 2963.36] And then you tie all these things together in a way that you can actually retrieve information
[2963.36 → 2969.70] and explore and discover aspects about your data that you couldn't otherwise in a way that
[2969.70 → 2971.62] actually ties all these tools and technologies together.
[2971.62 → 2975.84] So I call it like an enhanced retrieval augmented generation sort of model.
[2976.16 → 2979.14] And this would obviously require tools like Lang chain or Lava Index.
[2979.70 → 2983.74] I mean, these additional frameworks that allow you to compose these different tools together
[2983.74 → 2988.18] and pass data and instructions back and forth between the human and the different underlying
[2988.18 → 2989.02] databases themselves.
[2989.58 → 2991.20] So I'm super excited about those technologies.
[2991.56 → 2994.82] Yeah, I think it's great to hear that perspective.
[2994.82 → 3003.36] Also, you know, usually the answer is not like only this technology and nothing else is the solution,
[3003.36 → 3008.14] but a strategic combination of things often is where things end up.
[3008.20 → 3012.56] And I think those are fascinating topics to explore.
[3012.70 → 3015.50] And I look forward to your mini part blog post.
[3015.50 → 3019.52] As you explore those, I'm definitely going to be following your writing now.
[3019.78 → 3027.58] And yeah, thank you from the community and from us for your work on this topic and sharing
[3027.58 → 3029.20] that work with the community.
[3029.20 → 3033.54] It's super practical, and we're very privileged and happy to have you on the show.
[3033.66 → 3034.74] Thank you so much, Prashant.
[3034.98 → 3035.60] No, I appreciate it.
[3035.60 → 3036.18] Thank you so much.
[3039.88 → 3047.16] Thank you for listening to Practical AI.
[3047.70 → 3051.50] Your next step is to subscribe now, if you haven't already.
[3051.94 → 3056.62] And if you're a longtime listener of the show, help us reach more people by sharing Practical
[3056.62 → 3057.96] AI with your friends and colleagues.
[3058.42 → 3063.36] Thanks once again to Vastly and Fly for partnering with us to bring you all Change Talk podcasts.
[3063.36 → 3067.74] Check out what they're up to at Fastly.com and Fly.io.
[3068.02 → 3072.72] And to our Beat Freakin' Residence Break master Cylinder for continuously cranking out the best
[3072.72 → 3073.44] beats in the biz.
[3073.72 → 3074.64] That's all for now.
[3074.90 → 3076.06] We'll talk to you again next time.
