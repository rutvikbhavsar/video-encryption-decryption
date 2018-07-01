package crypto_final;

import java.io.*;
import java.security.SecureRandom;
import java.security.spec.AlgorithmParameterSpec;
import javax.crypto.*;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class video_encryption {

	public static void main(String[] args) {
		File input = new File("test1.mp4");			//Input file
        File enc_out = new File("enc_vid.mp4");			//Output of encrypted file
        File dec_out = new File("dec_vid.mp4");		//Output of decrypted file
		try {
			SecretKey key = KeyGenerator.getInstance("AES").generateKey();		//Secret Key using AES
			byte[] ekey = key.getEncoded();
			SecretKey dkey = new SecretKeySpec(ekey, 0, ekey.length, "AES");
			byte[] iv = new byte[16];											//Initialization vector
			SecureRandom.getInstance("SHA1PRNG").nextBytes(iv);					
			AlgorithmParameterSpec paramSpec = new IvParameterSpec(iv);
			encrypt.main(key, paramSpec, new FileInputStream(input), new FileOutputStream(enc_out));		//Encrypt video
			decrypt.main(dkey, paramSpec, new FileInputStream(enc_out), new FileOutputStream(dec_out));	//Decrypt video
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}
}