import messages_pb2

class RequestResponse():

    class Step():
        def __init__(self, name, duration):
            self.name = name
            self.duration = duration
            self.real_duration = 0

    def __init__(self):
        self.steps_hierarchy = {}
        self.steps_info = {}


    def calculate_duration(self, step_id):
        duration = self.steps_info[step_id].duration
        duration_child = 0
        if step_id in self.steps_hierarchy.keys():
            for child_id in self.steps_hierarchy[step_id]:
                duration_child += self.steps_info[child_id].duration
        return duration - duration_child

    def CreateHstep(self, id):
        hstep = messages_pb2.Response().HierarchicalStep()
        hstep.name = self.steps_info[id].name
        hstep.duration = self.steps_info[id].duration
        if id in self.steps_hierarchy.keys():
            for child_id in sorted(self.steps_hierarchy[id], key=lambda id :self.steps_info[id].real_duration, reverse=True):
                hstep.children.append(self.CreateHstep(child_id))
        return hstep


    def Transform(self, input):

        message = messages_pb2.Request()
        message.ParseFromString(input)

        for step in message.steps:
            if step.parent_id in self.steps_hierarchy:
                self.steps_hierarchy[step.parent_id].append(step.id)
            else:
                self.steps_hierarchy[step.parent_id] = [step.id]
            self.steps_info[step.id] = self.Step(step.name, int(step.duration))

        for id in self.steps_info.keys():
            self.steps_info[id].real_duration = self.calculate_duration(id)

        first = message.step_id
        if first == 0:
            first = self.steps_hierarchy[0]

        max_duration_step_name = None
        max_duration_step_duration = 0
        for step in self.steps_info:
            if self.steps_info[step].real_duration > max_duration_step_duration:
                max_duration_step_name = self.steps_info[step].name
                max_duration_step_duration = self.steps_info[step].real_duration

        output_message = messages_pb2.Response()
        output_message.hierarchical_step.CopyFrom(self.CreateHstep(first))
        output_message.max_duration_step_name = max_duration_step_name
        output_message.max_duration_step_duration = max_duration_step_duration

        output_message = output_message.SerializeToString()
        return(output_message)


if __name__ == "__main__":
    RR = RequestResponse()
    input = b'\n\x08\x08\x01\x18\x96\x01"\x01A\n\t\x08\x02\x10\x01\x18-"\x01B\n\t\x08\x03\x10\x01\x182"\x01C\n\t\x08\x04\x10\x02\x18\x14"\x01D\n\t\x08\x05\x10\x02\x18\x14"\x01E\x10\x01'
    print(RR.Transform(input))