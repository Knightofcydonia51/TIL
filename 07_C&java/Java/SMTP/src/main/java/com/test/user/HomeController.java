package com.test.user;

import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.Properties;
import java.io.UnsupportedEncodingException;
import java.util.Date;

import javax.mail.Authenticator;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.AddressException;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

/**
 * Handles requests for the application home page.
 */
@Controller
public class HomeController {

	private static final Logger logger = LoggerFactory.getLogger(HomeController.class);

	/**
	 * Simply selects the home view to render by returning its name.
	 */
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String home(Locale locale, Model model) {
		logger.info("Welcome home! The client locale is {}.", locale);

		System.out.println("???");

		Date date = new Date();
		DateFormat dateFormat = DateFormat.getDateTimeInstance(DateFormat.LONG, DateFormat.LONG, locale);

		String formattedDate = dateFormat.format(date);

		model.addAttribute("serverTime", formattedDate);

		return "home";
	}
	
	@RequestMapping(value="daumMap.do", method=RequestMethod.GET)
    public String daumMap(){
 
        return "home/daumMap";
    }

	

	// ������ȣ ������ (6����)
	public String RandomNum() {
		StringBuffer buffer = new StringBuffer();
		for (int i = 0; i < 6; i++) {
			int n = (int) (Math.random() * 10);
			buffer.append(n);
		}
		return buffer.toString();
	}

	// �̸��� ������ �Լ�(gmail)
	@RequestMapping(value = "/sendEmail", method = RequestMethod.GET)
	public void sendEmail(String usermail) {
		System.out.println("EMAIL: " + usermail);
		//����̰� ������ ���� ���, Ư�� �� �� ���� ���� ���?? ����Ʈ����?
		String result = usermail.substring(usermail.lastIndexOf("@")+1);
		System.out.println(result);
		Session s = null;
		
		if (result.equals("naver.com")) {
			System.out.println("���̹�" + usermail);
			s=naver();
		} else if(result.equals("gmail.com")) {
			System.out.println("����" + usermail);
			s=gmail();
		}else if(result.equals("daum.net")){
			System.out.println("����" + usermail);
			s=daum();
		}else {
			System.out.println("�߸�����");
		}
		
		MimeMessage msg = new MimeMessage(s);
		try {
			
			String authNum = "";
			msg.setSentDate(new Date());
			
			msg.setFrom(new InternetAddress("routrip@routrip.com", "��Ʈ��������")); // �߼���
			InternetAddress to = new InternetAddress(usermail); // ������
			msg.setRecipient(Message.RecipientType.TO, to);
			msg.setSubject("��Ʈ���Դϴ�", "UTF-8");
			authNum = RandomNum();
			msg.setText("������ȣ�� [" + authNum + "]�Դϴ�.", "UTF-8");
			Transport.send(msg);
			
			System.out.println("almost done=====================");
			
			
			
			
		} catch (AddressException ae) {
			System.out.println("AddressException : " + ae.getMessage());
		} catch (MessagingException me) {
			System.out.println("MessagingException : " + me.getMessage());
		} catch (UnsupportedEncodingException e) {
			System.out.println("UnsupportedEncodingException : " + e.getMessage());
		}
	}
	
	public Session daum() {
		Properties props = new Properties();
		props.put("mail.smtp.host", "smtp.daum.net");
		props.put("mail.smtp.socketFactory.port", "465");
		props.put("mail.smtp.socketFactory.class", "javax.net.ssl.SSLSocketFactory");
		props.put("mail.smtp.auth", "true");
		props.put("mail.smtp.port", "465");

		Session session = Session.getDefaultInstance(props, new javax.mail.Authenticator() {
			protected PasswordAuthentication getPasswordAuthentication() {
				return new PasswordAuthentication("routrip@daum.net", "fnxmflq12!");
				
			}
		});

		return session;
		
	}
	
	
	public Session naver() {
		Properties props = new Properties();
		
		props.put("mail.smtp.host", "smtp.naver.com");
		props.put("mail.smtp.socketFactory.port", "465");
		props.put("mail.smtp.socketFactory.class", "javax.net.ssl.SSLSocketFactory");
		props.put("mail.smtp.auth", "true");
		props.put("mail.smtp.port", "465");

		Session session = Session.getDefaultInstance(props, new javax.mail.Authenticator() {
			protected PasswordAuthentication getPasswordAuthentication() {
				return new PasswordAuthentication("routrip@naver.com", "fnxmflq12!");
			}
		});
		return session;
	}

	public Session gmail() {
		Properties props = new Properties();
		props.put("mail.smtp.starttls.enable", "true");
		props.put("mail.smtp.host", "smtp.gmail.com");
		props.put("mail.smtp.auth", "true");
		props.put("mail.smtp.port", "587");

		Session session = Session.getDefaultInstance(props, new javax.mail.Authenticator() {
			protected PasswordAuthentication getPasswordAuthentication() {
				return new PasswordAuthentication("routrip12@gmail.com", "fnxmflq12!");
			}
		});
		
		return session;
		
	}

}
