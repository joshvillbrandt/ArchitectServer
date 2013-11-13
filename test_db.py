from Architect.models import *

# channeli1 = ExposedChannelInstance(part="my part", child_channel="my channel type", channel_instance="channel instance")
# channeli1.save()

# channeli2 = NativeChannelInstance(part="my part", channel_type="my channel type", name="channel instance")
# channeli2.save()

cis = ChannelInstance.objects.all()
print cis