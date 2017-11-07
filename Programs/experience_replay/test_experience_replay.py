import unittest
from Programs.experience_replay.rank_based import Experience
from Programs.q_network import Q_network

class testReplayBuffer(unittest.TestCase):
    def setUp(self):
        conf = {'size': 50,
                'learn_start': 10,
                'partition_num': 5,
                'total_step': 100,
                'batch_size': 4}
        self.conf = conf
        self.replay_buffer = Experience(conf)
        self.network = Q_network()

    def test_store_to_replay_buffer(self):
        # insert to replay_buffer
        print('test insert replay_buffer')
        for i in range(1, 51):
            # tuple, like(state_t, a, r, state_t_1, t)
            to_insert = (i, 1, 1, i, 1)
            replay_buffer.store(to_insert)
        print(replay_buffer.priority_queue)
        print(replay_buffer._replay_buffer[1])
        print(replay_buffer._replay_buffer[2])
        print('test replace')
        to_insert = (51, 1, 1, 51, 1)
        replay_buffer.store(to_insert)
        print(replay_buffer.priority_queue)
        print(replay_buffer._replay_buffer[1])
        print(replay_buffer._replay_buffer[2])
        self.assertTrue(False, 'should store to buffer')

    def test_sample_from_replay_buffer(self):
        # sample
        print('test sample')
        sample, w, e_id = replay_buffer.sample(51)
        print(sample)
        print(w)
        print(e_id)
        self.assertTrue(False, 'should sample from buffer')

    def test_update_priority_replay_buffer(self):
        self.assertTrue(False, 'update priority')


