import tensorflow as tf
hello = tf.constant('Hello, Tensorflow!')
sess = tf.Session()
print(sess.run(hello))

import tensorflow as tensorflow
a=tf.constant(5.0)
b=tf.constant(6.0)
c = a*b
sess = tf.Session()
print(sess.run(c))
sess.close()

import tensorflow as tensorflow
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b
sess = tf.Session()
print(sess.run(adder_node,{a:[1,3],b:[2,4]}))

#simple linear model
import tensorflow as tensorflow
W = tf.Variable([.3]. tf.float32)
b = tf.Variable([-.3], tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W*x+b 
y = tf.placeholder(tf.float32)
squared_delta = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_delta)
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
print(sess.run(loss, {x:[1,2,3,4],y:[0,-1,-2,-3]}))
for i in range(1000):
	sess.run(train,{x:[1,2,3,3], y:[0,-1,-2,-3]})

#evaluation
import tensorflow as tensorflow
a = tf.constant(3)
sess = tf.session(3)
with sess.as_default():
	print(a.eval())
sess.close()

import tensorflow as tf 
a = tf.add(2,3)
b = tf.multiply(a,4)
sess=tf.Session()
print(sess.run(b))
replace_dict = {a:15}
print(ses.run(b,replace_dict))
sess.close()

#constructor variable
import tensorflow as tf 
my_var = tf.variable(4, name = 'may_var')
add = tf.add(5, my_var)
mul = tf.multiply(8,my_var)
sess = tf.Session()
sess.run(my_var.initializer)
print(my_var.eval(session=sess))
print(add.eval(session=sess))
print(mul.eval(session=sess))

import tensorflow as tf 
a = tf.placeholder(tf.int32, shape=[2], name = "input")
b = tf.reduce_prod(a , name = "prod_b")
c = tf.reduce_sum(a, name = "sum_c")
d = tf.add(b, c, name = "add_d")
sess = tf.Session()
input_dict = {a:np.array([1,2], dtype=np.int32)}
print(sess.run{d, feed_dict=input_dict})

#printing variable number
import tensorflow as tf 
sess = tf.Session()
a = tf.constant(10)
b = tf.constant(22)
print(sess.run(a+b))
import numpy as np 
y = x *0.1 +0.3
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data *0.1 +0.3
y_data = W * x_data + b 
W = tf.Variable(tf.random_uniform([1]),-1.0,1.0)
b = tf.Variable(tf.zeros([1]))
y = W*x_data + b 
loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer{0,5}
train = optimizer.minimize(loss)
init = tf.initialize_all_variables()
sess = tf.Session()
sess = run(init)
for step in range(201):
	sess.run(train)
	if(step%20==0):
		print(step,sess.run(W),sess.run(b))