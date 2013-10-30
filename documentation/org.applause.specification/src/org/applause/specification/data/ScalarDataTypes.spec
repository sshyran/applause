package org.applause.specification.data

import com.google.inject.Inject
import org.applause.lang.applauseDsl.ApplauseDslPackage
import org.applause.lang.applauseDsl.Model
import org.applause.specification.ApplauseDslInjectorProvider
import org.applause.specification.ApplauseDslTestCreator
import org.eclipse.xtext.junit4.InjectWith
import org.eclipse.xtext.junit4.util.ParseHelper
import org.jnario.runner.CreateWith

/**
 * Scalar data types make up the core of the Applause DSL. They are one of the central building blocks
 * for most of the other concepts in the Applause DSL. 
 */
 @InjectWith(ApplauseDslInjectorProvider)
 @CreateWith(typeof(ApplauseDslTestCreator))
describe "Scalar Data Types"{
	
	@Inject extension ParseHelper<Model>
	@Inject extension ApplauseValidationTestHelper
	
	/**
	 * Data types can have any name and can be defined anywhere in your DSL program.
	 */
	describe "Defining data types"{
		/**
		 * New data types can be defined using the `datatype` keyword.
		 * @filter('''|.isValid)
		 */
		fact "Simple data types" {
			'''
				datatype String
				datatype Integer
			'''.isValid
		}
	
		def void hasDuplicateDatatype(CharSequence sequence) {
			sequence.parse.assertError(ApplauseDslPackage.eINSTANCE.dataType, null, "Duplicate DataType 'String'")
		}
		
//		/**
//		 * @filter('''|.hasDuplicateDatatype)
//		 */
//		fact "Data types must be unique" {
//			'''
//				datatype String
//				datatype String // <-- invalid
//			'''.hasDuplicateDatatype
//		}
	
	}
	
//	/**
//	 * Applause supports mapping data types to platform types.
//	 */
//	describe "Platform Mapping" {
//		
//		/**
//		 * The `platform` keyword can be used to define a platform.
//		 * @filter('''|.isValid)
//		 */
//		fact "Defining platforms" {
//			'''
//				platform iOS {
//					// platform-specific configurations
//				}
//			'''.isValid
//		}
//		
//		/**
//		 * This makes sense when you want to support multiple platforms. This way, you can use the
//		 * platform-independent data type name and do not need to care about what's the right type 
//		 * on the target platform.
//		 * @filter(''')
//		 */
//		fact "A data type can be mapped to a different type" {
//			'''
//				platform foo {
//					typemapping String -> foo.Bar
//				}
//			'''.isValid
//		}
//		
//		/**
//		 * Applause comes with a number of pre-defined platform mappings for the supported platforms. 
//		 */
//		describe "Pre-defined platform mappings" {
//			
//			/**
//			 * @filter(''')
//			 */
//			fact "Scalar data type mappings for iOS" {
//				'''
//					platform iOS {
//					    typemapping String -> NSString
//					    typemapping Integer -> NSNumber
//					}			
//				'''.isValid
//			}
//			
//			/**
//			 * @filter(''')
//			 */
//			fact "Scalar data type mappings for Android" {
//				'''
//					platform Android {
//					    typemapping Integer -> java.lang.Integer
//					    typemapping String -> java.lang.String
//					    typemapping Date -> java.util.Date
//					    typemapping Bool -> boolean
//					}				
//				'''.isValid
//			}
//			
//			/**
//			 * @filter(''')
//			 */
//			fact "Scalar data type mappings for Windows Phone" {
//				'''
//					platform WP {
//						typemapping Integer -> int
//						typemapping String -> string
//						typemapping Bool -> bool
//					}				
//				'''.isValid
//			}
//			
//		}
//		
//	}
}