# -*- coding: UTF-8 -*-

#Copy recurs files+folders
import os
import shutil
import time
import smtplib, socket

def mail_send(body, subject, from_mail):
    HOST = "192.168.0.5"
    SUBJECT = subject
    TO = "119_2@hosp13"
    FROM = from_mail
    
    text = body
     
    BODY = "\r\n".join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
    ))
    
    server = smtplib.SMTP(HOST)
    server.sendmail(FROM, [TO], BODY.encode('cp1251'))
    #server.sendmail(FROM, [TO], BODY.encode('utf-8'))
    server.quit()    


def copytree(root_src_dir, root_dst_dir):
    '''Это будет проходить через исходный каталог, создавать любые каталоги, которые еще не существуют в каталоге назначения, и перемещать файлы из источника в каталог назначения
    Перед тем, как заменить соответствующий исходный файл, все ранее существовавшие файлы будут удалены (через os.remove). Любые файлы или каталоги, которые уже существуют в месте назначения, но не в источнике, остаются нетронутыми
    '''
    for src_dir, dirs, files in os.walk(root_src_dir): 
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                # in case of the src and dst are the same file
                if os.path.samefile(src_file, dst_file):
                    continue
                os.remove(dst_file)
                print("File exist, overwrite file: ", dst_file)
            try:
                shutil.move(src_file, dst_dir)
            except OSError:
              print("Something wrong! Please call your system administrator...")        
    
def new_folder(new_folder_path):
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        
def recursive_copy(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.exists(d):
            try:
                shutil.rmtree(d)
            except Exception as e:
                print("Something wrong! Please call your system administrator...", e)
                os.unlink(d)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
    #shutil.rmtree(src)



                
if __name__ == "__main__":
    today = str(time.strftime("%Y_%m_%d", time.localtime()))
    body = 'Эпикризы скопированы, проверь папку эпикриз на наличие не отправленных файлов.'
    subject = "Отправка эпикризов по VIPNet"
    new_folder_path = r'D:\epikriz_backup'+ "\\" + today + "_epikriz_original"
    new_folder(new_folder_path)
    root_dst_dir = (new_folder_path) + "\\"
    sent_by_mail_folder = (r'C:\epikriz\\')
    
    root_src_dir = (r"\\192.168.0.5\public$\4_kardiology\\") 
    copytree(root_src_dir, root_dst_dir)
    
    root_src_dir = (r"\\192.168.0.5\public$\7_kardiology\\") 
    copytree(root_src_dir, root_dst_dir)
    
    root_src_dir = (r"\\192.168.0.5\public$\onmk\\") 
    copytree(root_src_dir, root_dst_dir)
    
    recursive_copy (root_dst_dir, sent_by_mail_folder)
    mail_send(body, subject, (socket.gethostname()))    
    '''
    root_src_dir = (r"E:\test\src\4_kardiology\\") 
    copytree(root_src_dir, root_dst_dir)
    
    root_src_dir = (r"E:\test\src\7_kardiology\\") 
    copytree(root_src_dir, root_dst_dir)
    
    root_src_dir = (r"E:\test\src\onmk\\") 
    copytree(root_src_dir, root_dst_dir)
    
    recursive_copy (root_dst_dir, sent_by_mail_folder)
    mail_send(body, subject, (socket.gethostname()))
    
    '''
    
    '''
    root_src_dir = (r'\\192.168.0.5\public$\4_kardiology\\')
    root_dst_dir = (r'C:\epikriz\\')
    print("Processing, please wait ...")
    copytree(root_src_dir, root_dst_dir)
    root_src_dir = (r"\\192.168.0.5\public$\7_kardiology\\") 
    copytree(root_src_dir, root_dst_dir)
    root_src_dir = (r"\\192.168.0.5\public$\onmk\\") 
    copytree(root_src_dir, root_dst_dir)
    time.sleep(5)
    print("Done ...")
    time.sleep(3)
    '''




