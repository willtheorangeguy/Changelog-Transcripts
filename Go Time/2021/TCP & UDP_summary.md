• Introduction to Adam Woodbeck, author of "Network Programming With Go" book
• TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) explained: stateful vs stateless, reliability, and differences in data transfer
• Why UDP is used for real-time applications like games, where packets don't need to arrive late but can be dropped if they don't arrive at all
• Analogy of baking a pie to explain TCP's conversation-based approach vs UDP's abrupt data transfer
• Explanation of the 3-way handshake process in establishing a TCP connection: SYN packet, acknowledgment packet, and establishment of session
• Discussion on how TCP provides reliability through buffering and acknowledgments, whereas UDP requires application-level handling for reliability
• TCP connection establishment process, including three-way handshake
• Keepalives to maintain connection and prevent disconnection due to latency
• Reliability mechanisms, including sequence numbers and acknowledgments
• Window size (receive buffer) management to control data transfer flow
• Maximum segment size (MTU) and packetization of data for transmission
• TCP handling out-of-order packet delivery
• Packet routing through different paths on the internet
• Packets being dropped by overloaded network devices
• Selective acknowledgments and retransmitting missing packets
• TCP connections being maintained across multiple IP addresses and networks
• Use of Wireshark to capture and analyze networking traffic
• Encoding bytes for transmission over a network
• Buffering and encoding methods for network communication
• Type-length-value (TLV) method of encoding data
• Standardized encoding and decoding formats for web communication (e.g. JSON)
• TCP connection establishment and closure
• Sequence numbers in TCP packets and potential overflow issues
• Wireshark's role in calculating sequence numbers and other packet information
• TCP and IP were once a single monolithic protocol
• UDP is stateless and does not require acknowledgement for sent data
• DNS uses UDP for requests due to its efficiency in sending small amounts of data
• Go has good support for UDP, with the net package providing Conn and PacketConn interfaces for working with UDP connections
• UDP receive buffers exist but do not provide feedback on packet receipt or overflow, packets may be dropped if buffer overflows
• UDP vs TCP behavior and implications for programming
• PacketConn vs net.Conn in Go programming
• Message size limitations and fragmentation in UDP
• Adding sequence numbers and acknowledgments for reliability in UDP applications
• Trivial File Transfer Protocol (TFTP) example of UDP-based protocol with application-layer reliability
• History and development of TCP and its limitations
• HTTP/2 and QUIC/HTTP/3 as examples of moving functionality from the transport layer to the application layer
• Head of line blocking problem in TCP
• HTTP/3 and QUIC protocols
• Multiplexing and framing in HTTP/2 vs. HTTP/3
• Connection ordering and UDP packetization
• Deadlines and timeouts in networking for connection maintenance
• Setting deadlines in network connections using Go
• HTTP clients not having a default timeout
• Giveaway of Adam's book "Network Programming With Go"
• Adam's unpopular opinion: removing trackpoint and adding larger touchpad on ThinkPad laptops
• Discussion about natural scrolling and gesture preferences