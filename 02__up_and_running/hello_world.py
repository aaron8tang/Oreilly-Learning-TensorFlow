import tensorflow as tf

h = tf.constant("Hello")
w = tf.constant(" World!")
hw = h + w

with tf.Session() as sess:
    print(hw)
    ans = sess.run(hw)

print(ans)
