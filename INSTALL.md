### Ubuntu: ###

1. Install apxs2 - Apache extension tool (prefork or threaded - depends on your Apache installation)  
`apt-get install apache2-prefork-dev`
or
`apt-get install apache2-threaded-dev`

2. Compile and install module into Apache modules dir  
`apxs2 -c -i mod_realip2.c`

3. Put realip2.conf and realip2.load into /etc/apache2/mods-available  
`cp ./ubuntu/realip2.* /etc/apache2/mods-available`  

4. Enable module  
`a2enmod realip2`

5. Restart Apache  
`service apache2 restart`


### CentOS: ###

1. Install apxs - Apache extension tool
`yum install httpd-devel`

2. Compile and install module into Apache modules dir  
`apxs -c -i mod_realip2.c`

3. Put realip2.conf into /etc/httpd/conf.d  
`cp ./centos/realip2.conf /etc/httpd/conf.d` 

4. Restart Apache  
`service httpd restart`


#### nginx setup ###

Put `proxy_set_header X-Real-IP $remote_addr;` into your config
