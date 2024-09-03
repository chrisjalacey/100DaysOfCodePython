"""
Day 33 - File operations: Write
Write data to a text file.
"""

text = """Background Information
The voice gateway generates a ringback tone to the customer in specific call flows when the call is sent to the agent. In outbound dialer, this is something customers does not want end user to know that this is outbound call and they are being transferred

For dialer call flows, in order to prevent the generation of a ringback from gateway, Session Initiation Protocol (SIP) normalization script to the Unified Communications Manager SIP trunk.

In the scenario where the same gateway is used for outbound dialer and PSTN calls, the trunk for PSTN calls still needs a 180 RINGING SIP message for inbound calls in order to trigger the gateway to play ringback to the PSTN, but needs to be disabled for outbound dialer calls.

Here is an example of the two scenarios described:"""

file = "outputtext.txt"
with  open(file, "w") as f:
    f.write(text)
    