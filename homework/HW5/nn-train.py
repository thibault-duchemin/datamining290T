#learn rate
l = 10

#initial variables
i_1 = 1
i_2 = 2
w_25 = 0.5
w_24 = -3
w_23 = 2
w_15 = 4
w_14 = 2
w_13 = -3
o_3 = 0.7311
o_4 = 0.0179
o_5 = 0.9933
t_6 = 0
o_6 = 0.83867

w_56 = 1.5
w_46 = 0.7
w_36 = 0.7311

#Calculating error for hidden ouputs
err_6 = -0.11346127339699999
err_5 = -0.0011326458827956695
err_4 = o_4*(1-o_4)*err_6*w_46
err_3 = o_3*(1-o_3)*err_6*w_36

print "err_6: %s" %err_6
print "err_5: %s" %err_5
print "err_4: %s" %err_4
print "err_3: %s" %err_3

#Calculating adjusted weights
w_56 = w_56 + l*err_6*o_5
w_46 = w_46 + l*err_6*o_4
w_36 = w_36 + l*err_6*o_3

print "w_56: %s" %w_56
print "w_46: %s" %w_46
print "w_36: %s" %w_36

err_2 = i_2*(1-i_2)*(w_13*err_3+w_14*err_4+w_15*err_5)
err_1 = i_1*(1-i_1)*(w_23*err_3+w_24*err_4+w_25*err_5)
w_25 = w_25+l*err_5*i_1
w_24 = w_24+l*err_4*i_1
w_23 = w_23+l*err_3*i_1
w_15 = w_15+l*err_5*i_1
w_14 = w_14+l*err_4*i_1
w_13 = w_13+l*err_3*i_1

print "err_2: %s" %err_2
print "err_1: %s" %err_1
print "w_25: %s" %w_25
print "w_24: %s" %w_24
print "w_23: %s" %w_23
print "w_15: %s" %w_15
print "w_14: %s" %w_14
print "w_13: %s" %w_13



