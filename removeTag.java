import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.client.builder.AwsClientBuilder;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.*;

public class RemoveObjectTag {

    public static void main(String[] args) {
        // Defina as credenciais da AWS
        String accessKey = "SEU_ACCESS_KEY";
        String secretKey = "SEU_SECRET_KEY";

        // Defina a região
        String region = "us-east-1"; // Substitua pela sua região

        // Defina o nome do bucket e o caminho do objeto
        String bucketName = "SEU_BUCKET_NAME";
        String objectKey = "SEU_OBJECT_KEY";

        // Crie o cliente AmazonS3
        AmazonS3 s3Client = AmazonS3ClientBuilder.standard()
                .withEndpointConfiguration(new AwsClientBuilder.EndpointConfiguration("https://s3." + region + ".amazonaws.com", region))
                .withCredentials(new AWSStaticCredentialsProvider(new BasicAWSCredentials(accessKey, secretKey)))
                .build();

        // Remova a tag específica do objeto
        removeTagFromObject(s3Client, bucketName, objectKey, "TagToRemove");
    }

    private static void removeTagFromObject(AmazonS3 s3Client, String bucketName, String objectKey, String tagKeyToRemove) {
        // Obtenha as tags atuais do objeto
        ObjectTagging objectTagging = s3Client.getObjectTagging(new GetObjectTaggingRequest(bucketName, objectKey));

        // Remova a tag específica
        objectTagging.getTagSet().removeIf(tag -> tag.getKey().equals(tagKeyToRemove));

        // Atualize as tags do objeto
        s3Client.setObjectTagging(new SetObjectTaggingRequest(bucketName, objectKey, objectTagging));
        
        System.out.println("A tag '" + tagKeyToRemove + "' foi removida do objeto '" + objectKey + "'.");
    }
}
